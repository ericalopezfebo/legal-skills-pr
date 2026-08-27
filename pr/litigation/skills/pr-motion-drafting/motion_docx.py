#!/usr/bin/env python3
"""DOCX renderer for pr-motion-drafting. Includes casp-calderon fidelity profile."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
try:
    import yaml
except Exception:
    yaml = None

FORUMS={
 "casp":{"header":["GOBIERNO DE PUERTO RICO","COMISIÓN APELATIVA DEL SERVICIO PÚBLICO"],"salutation":"A LA HONORABLE COMISIÓN:","case_label":"Caso Núm.","matter_label":"SOBRE:"},
 "aep-ja":{"header":["AUTORIDAD DE EDIFICIOS PÚBLICOS","JUNTA DE APELACIONES","SAN JUAN, PUERTO RICO"],"salutation":"A LA HONORABLE JUNTA:","case_label":"Caso Núm.","matter_label":"SOBRE:"},
 "tpi":{"header":["ESTADO LIBRE ASOCIADO DE PUERTO RICO","TRIBUNAL DE PRIMERA INSTANCIA"],"salutation":"AL HONORABLE TRIBUNAL:","case_label":"Civil Núm.","matter_label":"SOBRE:"},
 "admin-generic":{"header":["GOBIERNO DE PUERTO RICO"],"salutation":"AL HONORABLE FORO:","case_label":"Caso Núm.","matter_label":"SOBRE:"}}

def borders(cell,**edges):
 tc=cell._tc.get_or_add_tcPr(); b=tc.first_child_found_in("w:tcBorders")
 if b is None: b=OxmlElement("w:tcBorders"); tc.append(b)
 for n,a in edges.items():
  e=b.find(qn("w:"+n))
  if e is None: e=OxmlElement("w:"+n); b.append(e)
  for k,v in a.items(): e.set(qn("w:"+k),str(v))

def page_borders(sec):
 sp=sec._sectPr; pg=sp.find(qn("w:pgBorders"))
 if pg is None: pg=OxmlElement("w:pgBorders"); sp.append(pg)
 for n,a in (("left",{"val":"double","sz":"12","space":"4","color":"FF0000"}),("right",{"val":"single","sz":"12","space":"4","color":"FF0000"})):
  e=OxmlElement("w:"+n)
  for k,v in a.items(): e.set(qn("w:"+k),v)
  pg.append(e)

def font(doc,name="Times New Roman",size=12):
 s=doc.styles["Normal"]; s.font.name=name; s.font.size=Pt(size)
 for k in ("ascii","hAnsi","cs"): s._element.rPr.rFonts.set(qn("w:"+k),name)

def run(p,text,b=False,u=False):
 r=p.add_run(text); r.bold=b; r.underline=u; return r

def header(doc,lines):
 for x in lines:
  p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after=Pt(0); run(p,x)

def caption(doc,d,prof):
 t=doc.add_table(rows=1,cols=2); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
 l,r=t.rows[0].cells; l.width=Inches(3.35); r.width=Inches(3.15)
 l.vertical_alignment=r.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
 for c in (l,r): borders(c,top={"val":"nil"},bottom={"val":"nil"},left={"val":"nil"},right={"val":"nil"})
 borders(l,bottom={"val":"double","sz":"6","space":"0","color":"auto"},right={"val":"single","sz":"8","space":"0","color":"auto"})
 parties=d.get("parties",{}).get("left",[])
 for i,x in enumerate(parties):
  p=l.paragraphs[0] if i==0 else l.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; run(p,str(x.get("name","[PARTE]")).upper(),True)
  q=l.add_paragraph(); q.alignment=WD_ALIGN_PARAGRAPH.CENTER; run(q,str(x.get("role","")))
  if i==0 and len(parties)>1:
   q=l.add_paragraph(); q.alignment=WD_ALIGN_PARAGRAPH.CENTER; run(q,"v.")
 p=r.paragraphs[0]; run(p,f"{prof['case_label']} {d.get('case_number','[POR COMPLETAR]')}")
 q=r.add_paragraph(); run(q,prof['matter_label'])
 q=r.add_paragraph(); q.alignment=WD_ALIGN_PARAGRAPH.CENTER; run(q,str(d.get('matter','[POR COMPLETAR]')))

def body(doc,text,indent=0):
 p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.line_spacing=1.5; p.paragraph_format.space_after=Pt(3)
 if indent: p.paragraph_format.left_indent=Inches(indent)
 run(p,text); return p

def bold_leads(p,text,leads):
 pos=0
 for token in sorted(leads,key=lambda x:text.find(x) if x in text else 10**9):
  i=text.find(token,pos)
  if i<0: continue
  run(p,text[pos:i]); run(p,token,True); pos=i+len(token)
 run(p,text[pos:])

def page_num(sec):
 p=sec.footer.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER; run(p,"- "); f=OxmlElement("w:fldSimple"); f.set(qn("w:instr"),"PAGE"); p._p.append(f); run(p," -")

def build_motion(d:dict[str,Any])->Document:
 forum=d.get("forum_profile","admin-generic"); prof=FORUMS.get(forum,FORUMS["admin-generic"]); visual=d.get("visual_profile","official-neutral"); cal=visual=="casp-calderon"
 doc=Document(); sec=doc.sections[0]; sec.page_width=Inches(8.5); sec.page_height=Inches(11)
 if visual in {"pr-litigation-redline","casp-calderon"}:
  sec.left_margin=Inches(0.35 if cal else 1.5); sec.right_margin=Inches(0.35 if cal else .5); sec.top_margin=Inches(.55); sec.bottom_margin=Inches(.35); page_borders(sec)
 else:
  sec.left_margin=sec.right_margin=sec.top_margin=sec.bottom_margin=Inches(1)
 font(doc,d.get("font","Times New Roman"),float(d.get("font_size",12)))
 h=prof["header"][:]
 if cal and forum=="casp": h=["GOBIERNO DE PUERTO RICO","COMISIÓN APELATIVA DEL SERVICIO PÚBLICO","SAN JUAN, PUERTO RICO"]
 header(doc,h+list(d.get("extra_header",[]))); caption(doc,d,prof)
 p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(8); p.paragraph_format.space_after=Pt(14); run(p,str(d.get("title","MOCIÓN")).upper(),True,cal)
 sal=d.get("salutation") or ("A LA HONORABLE COMISIÓN U COMISIONADA ASOCIADA" if cal and forum=="casp" else prof["salutation"])
 p=doc.add_paragraph(); run(p,sal,False if cal else True)
 if d.get("appearance"):
  p=body(doc,str(d["appearance"]));
  if cal:
   # optional explicit tokens to bold without rewriting text
   for rr in p.runs: rr.bold=False
   text=p.text; p.clear(); bold_leads(p,text,d.get("appearance_bold",[]))
 for x in d.get("body",[]):
  text=str(x.get("text")) if isinstance(x,dict) else str(x); p=body(doc,text,.55 if cal else 0)
  if cal and isinstance(x,dict) and x.get("bold"):
   p.clear(); bold_leads(p,text,list(x["bold"]))
 if d.get("prayer"):
  text=str(d["prayer"]); p=body(doc,text,.55 if cal else 0); p.clear(); bold_leads(p,text,["POR TODO LO CUAL","CON LUGAR"] if cal else ["POR TODO LO CUAL,","POR LO EXPUESTO,","EN MÉRITO DE LO ANTERIOR,"])
 if d.get("respectfully_submitted",True):
  p=body(doc,str(d.get("respectfully_text","RESPETUOSAMENTE SOMETIDO.")),.55 if cal else 0); p.runs[0].bold=True
 if d.get("place_date"): body(doc,str(d["place_date"]),.55 if cal else 0)
 sig=d.get("signature") or {}
 if sig:
  p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(3.7 if cal else 0); p.paragraph_format.space_before=Pt(10)
  for k in ("name","rua","address","phone","email"):
   if sig.get(k): run(p,str(sig[k]),False); run(p,"\n")
 if cal and d.get("certification"):
  p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(28); run(p,"CERTIFICADO DE NOTIFICACIÓN",True,True)
  p=body(doc,str(d["certification"])); text=p.text; p.clear(); bold_leads(p,text,["CERTIFICO:"])
  if sig.get("name"):
   p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(4.0); run(p,"Lcdo. "+str(sig["name"]).upper())
 elif d.get("certification"):
  body(doc,str(d["certification"]))
 if d.get("page_numbers",True): page_num(sec)
 return doc

def load(p):
 text=p.read_text(encoding="utf-8")
 if p.suffix.lower()==".json": return json.loads(text)
 if yaml is None: raise SystemExit("Use JSON or install PyYAML")
 return yaml.safe_load(text)
def main():
 a=argparse.ArgumentParser(); a.add_argument("input",type=Path); a.add_argument("output",type=Path); x=a.parse_args(); doc=build_motion(load(x.input)); x.output.parent.mkdir(parents=True,exist_ok=True); doc.save(x.output)
if __name__=="__main__": main()
