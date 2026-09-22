# uso: python3 mm_gen.py spec.json salida.html
# spec: {title, eyebrow, h1, sub, chips[], palette:"cool"|"warm"|..., branches:[{n,h2,p,nodes:[{h3,tag,items[],seq?}]}], star?:{lbl,h3,html}, flags:[{lbl,h3,p}], footer}
import json, sys, re, html as H
spec=json.load(open(sys.argv[1])); out=sys.argv[2]
css=open(__file__.replace("mm_gen.py","mm_style.css")).read()
PAL={
 "cool":  ({'c1':('#0B6E64','#E4F1EE'),'c2':('#1D4ED8','#E4EAFC'),'c3':('#9A3412','#FBEBE2'),'c4':('#6D28D9','#EEE8FB'),'c5':('#A21457','#FAE4EE')},
           {'c1':('#4FD1BE','#0E2B28'),'c2':('#8AB0FF','#121F3A'),'c3':('#F0A87A','#2E1A11'),'c4':('#BFA3FF','#211537'),'c5':('#F58FBC','#31101F')}),
 "data":  ({'c1':('#0E6F7A','#E1F1F3'),'c2':('#2B4FC7','#E5EAFB'),'c3':('#6A2FB8','#EFE7FA'),'c4':('#0B7A52','#E0F2EA'),'c5':('#A02A1D','#FAE6E2')},
           {'c1':('#5FD0DC','#0D2A2E'),'c2':('#8FAEFF','#131F3D'),'c3':('#C3A2FF','#221638'),'c4':('#5FD6A6','#0D2B20'),'c5':('#F5988A','#311512')}),
 "steel": ({'c1':('#1E5A8A','#E3ECF5'),'c2':('#6B3FA0','#EEE7F7'),'c3':('#0F7A6B','#E0F2EF'),'c4':('#A0520F','#F8EBDD'),'c5':('#8A1F4A','#F6E2EA')},
           {'c1':('#7FB6E6','#10212F'),'c2':('#C09CF0','#1F1731'),'c3':('#5ED1BE','#0D2A26'),'c4':('#EFB172','#2B1D0F'),'c5':('#F08BB1','#2E1220')}),
 "warm":  ({'c1':('#1F6F5C','#E3F0EB'),'c2':('#8A5212','#F8EDDD'),'c3':('#1B4F8A','#E2ECF7'),'c4':('#96203C','#F9E4E8'),'c5':('#57338F','#EDE6F7')},
           {'c1':('#63CCAF','#0F2A23'),'c2':('#E0AE63','#2C2012'),'c3':('#7FB2EA','#121F30'),'c4':('#EE8199','#2F1219'),'c5':('#B79BE8','#1F1630')}),
 "earth": ({'c1':('#7A4B12','#F6ECDD'),'c2':('#2F6A3A','#E5F1E7'),'c3':('#8C2F39','#F7E3E5'),'c4':('#2C5577','#E3ECF4'),'c5':('#5B4A8C','#ECE8F6')},
           {'c1':('#E2B06C','#2B1E0F'),'c2':('#79C98A','#12261A'),'c3':('#EE8E98','#2E1316'),'c4':('#86B6E0','#122130'),'c5':('#B3A3EA','#1D1830')}),
}
light,dark=PAL[spec.get("palette","cool")]
parts=re.split(r'(@media \(prefers-color-scheme:dark\)|:root\[data-theme="dark"\])',css)
def sub(b,p):
    for k,(h,bg) in p.items():
        b=re.sub(rf'--{k}:#[0-9A-Fa-f]{{6}}',f'--{k}:{h}',b); b=re.sub(rf'--{k}-bg:#[0-9A-Fa-f]{{6}}',f'--{k}-bg:{bg}',b)
    return b
parts[0]=sub(parts[0],light)
for i in range(2,len(parts),2): parts[i]=sub(parts[i],dark)
css=''.join(parts)
def items(it,seq=False):
    MUTED=' style="color:var(--ink-3)"'
    lis=''
    for x in it:
        attr=MUTED if x.startswith("~") else ''
        lis+='<li'+attr+'>'+x.lstrip("~")+'</li>'
    cls=' class="seq"' if seq else ''
    return '<ul'+cls+'>'+lis+'</ul>'
b=[]
for i,br in enumerate(spec["branches"]):
    c=f"c{(i%5)+1}"
    nodes=''
    for nd in br["nodes"]:
        tag=f' <span class="tag">{nd["tag"]}</span>' if nd.get("tag") else ''
        body=''.join(items(g, s) for g,s in nd.get("groups",[(nd.get("items",[]), nd.get("seq",False))]))
        nodes+=f'<div class="node"><h3>{nd["h3"]}{tag}</h3>{body}</div>'
    b.append(f'<section class="branch" style="--hue:var(--{c});--bg:var(--{c}-bg)"><div class="stem"><div class="n">{br["n"]}</div><h2>{br["h2"]}</h2><p>{br["p"]}</p></div><div class="nodes">{nodes}</div></section>')
    for fl in spec.get("flags",[]):
        if fl.get("after")==i:
            b.append(f'<div class="flag"><div class="lbl">{fl["lbl"]}</div><h3>{fl["h3"]}</h3><p>{fl["p"]}</p></div>')
    st=spec.get("star")
    if st and st.get("after")==i:
        b.append(f'<div class="star"><div class="lbl">{st["lbl"]}</div><h3>{st["h3"]}</h3>{st["html"]}</div>')
chips=''.join(f'<span class="chip">{c}</span>' for c in spec.get("chips",[]))
doc=(f'<title>{spec["title"]}</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@500;600;700&display=swap">\n'
     +css+f'\n<div class="wrap"><header><div class="eyebrow">{spec["eyebrow"]}</div><h1>{spec["h1"]}</h1><p class="sub">{spec["sub"]}</p><div class="meta">{chips}</div></header>'
     +''.join(b)+f'<footer><span>{spec.get("footer","")}</span><span>Tec de Monterrey · The Learning Gate</span><span>Sept 2026</span></footer></div>\n')
open(out,"w").write(doc); print("ok",out,len(doc))
