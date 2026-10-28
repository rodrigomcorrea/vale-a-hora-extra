"""Gera docs/index.html (site do GitHub Pages) a partir de index.html (fonte do artifact).

O index.html é escrito sem <!doctype>/<head>, porque o Claude adiciona isso ao publicar.
Aqui montamos o mesmo cabeçalho para o site rodar sozinho, com manifest para instalar no celular.

Uso: python build.py
"""
from pathlib import Path

raiz = Path(__file__).parent
fonte = (raiz / "index.html").read_text(encoding="utf-8")

cabecalho = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Marque os dias de hora extra e veja quanto sobra no holerite depois do INSS e do IR.">
<meta name="theme-color" content="#3341A6">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Hora Extra">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon.svg">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px system-ui,-apple-system,"Segoe UI",sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
</head>
<body>
"""

saida = raiz / "docs"
saida.mkdir(exist_ok=True)
(saida / "index.html").write_text(cabecalho + fonte + "\n</body>\n</html>\n", encoding="utf-8")
print("docs/index.html gerado")
