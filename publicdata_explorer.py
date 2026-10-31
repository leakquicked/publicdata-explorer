import argparse,json,re
from pathlib import Path
RULES=[["email","\\b(email|e-mail)\\b","review"],["location","\\b(city|country|region|address)\\b","info"],["identifier","\\b(id|identifier|account)\\b","review"]]
def analyze_text(text):
 out=[]
 for rule,pattern,severity in RULES:
  for m in re.finditer(pattern,text,re.I): out.append({"rule":rule,"severity":severity,"line":text.count("\\n",0,m.start())+1,"match":m.group(0)[:120]})
 return out
def main():
 p=argparse.ArgumentParser(description="Inspect a local CSV header for potentially sensitive columns");p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args()
 if not a.input.is_file(): p.error("input file not found")
 findings=analyze_text(a.input.read_text(encoding="utf-8",errors="replace"));report={"tool":"publicdata-explorer","count":len(findings),"findings":findings};data=json.dumps(report,indent=2,ensure_ascii=False)
 if a.output:a.output.write_text(data+"\\n",encoding="utf-8")
 print(data)
if __name__=="__main__":main()
