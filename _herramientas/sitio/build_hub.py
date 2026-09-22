import glob,re,json,sys,os,urllib.parse
ROOT='/Users/luisparra/Desktop/CTO'; mode=sys.argv[1]; out=sys.argv[2]
GROUPS=[("SC 1","Mentalidad digital"),("SC 2","Tecnologías estratégicas"),("SC 3","Organización y estrategia"),("SC 4","Centrado en la persona"),("SC 5","Ejecución y roadmap")]
maps=[]
for f in sorted(glob.glob(ROOT+'/*/mapa-mental*.html')):
  t=open(f).read()
  g=lambda p:(lambda m:re.sub('<[^>]+>','',m.group(1)).strip() if m else '')(re.search(p,t,re.S))
  code=re.search(r'SC (\d\.\d)',g(r'class="eyebrow"[^>]*>(.*?)</')).group(1)
  sub=g(r'class="sub"[^>]*>(.*?)</'); sub=re.split(r'(?<=[.:])\s',sub)[0]
  rel=os.path.relpath(f,ROOT)
  href=urllib.parse.quote(rel) if mode=='repo' else 'mapas/sc'+code.replace('.','')+'.html'
  cid='sc'+code.replace('.',''); pre='sitio/' if mode=='repo' else 'estudio/'
  maps.append(dict(id=cid,guia=pre+cid+'-guia.html',resumen=pre+cid+'-resumen.html',code='SC '+code,title=g(r'<h1[^>]*>(.*?)</h1>'),short=g(r'<title>(.*?)</title>'),sub=sub,href=href,src=rel))
if mode!='repo': json.dump([[m['src'],m['href']] for m in maps],open(os.path.dirname(out)+'/files.json','w'),ensure_ascii=False)
html=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'template.html')).read()
html=html.replace('/*MAPS*/[]',json.dumps(maps,ensure_ascii=False)).replace('/*GROUPS*/[]',json.dumps(GROUPS,ensure_ascii=False))
open(out,'w').write(html); print(len(maps),'mapas →',out)
