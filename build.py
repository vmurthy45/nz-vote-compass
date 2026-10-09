# Inlines data.json into src.html. Writes artifact.html (fragment for the Artifact viewer)
# and index.html (standalone page for local use / GitHub Pages).
import json, pathlib
here = pathlib.Path(__file__).parent
data = json.dumps(json.load(open(here / "data.json")), ensure_ascii=False).replace("</", "<\\/")
frag = (here / "src.html").read_text().replace("/*DATA*/", data)
(here / "artifact.html").write_text(frag)
(here / "index.html").write_text(
    '<!doctype html>\n<html lang="en-NZ">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<title>Policy Compass NZ</title>\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<meta name="theme-color" content="#0d0e11">\n'
    '<style>[hidden]{display:none!important}body{margin:0}</style>\n</head>\n<body>\n' + frag + '\n</body>\n</html>\n')
print("built", len(frag), "bytes")
