# Convierte GUIA y RESUMEN de cada módulo a páginas HTML para el sitio.
# uso: python3 render_md.py <carpeta_salida>
import glob, os, re, sys, markdown, html
ROOT = '/Users/luisparra/Desktop/CTO'
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--ground:#F2F5F8;--surface:#FFFFFF;--ink:#16202B;--muted:#5B6875;--line:#DCE2E8;--accent:#1F5F8B;--soft:#E3EEF6;--warn:#8A4B0F;--warn-soft:#FBF1E4;
--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--serif:"IBM Plex Serif",Georgia,serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ground:#0F151B;--surface:#151D25;--ink:#E6ECF1;--muted:#93A1AE;--line:#26323D;--accent:#7DB3DA;--soft:#1B2B38;--warn:#F0B37A;--warn-soft:#2A2016}}
:root[data-theme="dark"]{--ground:#0F151B;--surface:#151D25;--ink:#E6ECF1;--muted:#93A1AE;--line:#26323D;--accent:#7DB3DA;--soft:#1B2B38;--warn:#F0B37A;--warn-soft:#2A2016}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font:16px/1.6 var(--sans)}
main{max-width:860px;margin:0 auto;padding-block:32px 64px;padding-inline:20px}
.eyebrow{font:600 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}
h1{font:600 30px/1.2 var(--serif);margin:0 0 6px;text-wrap:balance}
h1+h3{font:400 17px/1.4 var(--sans);color:var(--muted);margin:0 0 24px}
h2{font:600 22px/1.3 var(--serif);margin:40px 0 12px;padding-top:20px;border-top:1px solid var(--line);text-wrap:balance}
h3{font:600 17px/1.35 var(--sans);margin:28px 0 8px}
p,li{max-width:72ch}
a{color:var(--accent)}
hr{display:none}
strong{font-weight:600}
code{font:500 .88em var(--mono);background:var(--soft);padding:1px 5px;border-radius:4px}
blockquote{margin:16px 0;padding:10px 16px;background:var(--warn-soft);color:var(--ink);border-radius:6px}
blockquote p{margin:4px 0}
ul,ol{padding-left:22px}
li{margin:3px 0}
.tbl{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:8px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:14.5px;line-height:1.45}
th,td{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}
th{font:600 12px/1.3 var(--mono);letter-spacing:.03em;text-transform:uppercase;color:var(--muted);background:var(--ground)}
tr:last-child td{border-bottom:0}
td:first-child{font-weight:500}
@media (max-width:600px){main{padding-inline:16px}h1{font-size:25px}}
"""
PAGE = """<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@600&display=swap">
<style>{css}</style>
<main><div class="eyebrow">{eyebrow}</div>
{body}
</main>"""

def code_of(folder):
    m = glob.glob(os.path.join(folder, 'mapa-mental*.html'))
    t = open(m[0]).read()
    return re.search(r'SC (\d\.\d)', t).group(1).replace('.', '')

def render(md_path, kind, code, siblings):
    src = open(md_path).read()
    # enlaces: a los .md hermanos -> páginas del sitio; el resto -> texto plano
    def fix(m):
        text, href = m.group(1), m.group(2)
        base = os.path.basename(href.split('#')[0])
        if base.startswith('RESUMEN'): return f'[{text}](sc{code}-resumen.html)'
        if base.startswith('GUIA'): return f'[{text}](sc{code}-guia.html)'
        if href.startswith('http'): return m.group(0)
        return text
    src = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', fix, src)
    body = markdown.markdown(src, extensions=['tables', 'sane_lists'])
    body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    title = re.search(r'^# (.+)$', src, re.M).group(1)
    short = ('Guía' if kind == 'guia' else 'Resumen') + ' SC ' + code[0] + '.' + code[1]
    eyebrow = ('Guía para la evaluación y el Reto' if kind == 'guia' else 'Resumen de estudio') + f' · SC {code[0]}.{code[1]}'
    open(os.path.join(OUT, f'sc{code}-{kind}.html'), 'w').write(PAGE.format(title=html.escape(short), css=CSS, eyebrow=eyebrow, body=body))

n = 0
for folder in sorted(glob.glob(ROOT + '/*/')):
    if not glob.glob(folder + 'mapa-mental*.html'): continue
    code = code_of(folder)
    for kind, pat in (('guia', 'GUIA-*.md'), ('resumen', 'RESUMEN-*.md')):
        f = glob.glob(folder + pat)
        if f: render(f[0], kind, code, None); n += 1
        else: print('FALTA', kind, folder)
print(n, 'páginas →', OUT)
