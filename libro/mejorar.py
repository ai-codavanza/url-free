"""Capa de diseño v2: cabecera corrida, portada con sellos, aperturas ricas y certificado.
Se ejecuta sobre el HTML ya generado: mejorar("libro_selva.html", 2)"""
import re

SERIE = "Serie Pequeños Exploradores"


def _lineas(n):
    return '<div class="lineas">' + "<div></div>" * n + "</div>"


def mejorar(ruta, numero):
    html = open(ruta, encoding="utf-8").read()
    n_exp = len(re.findall(r'class="chip">[^<]*Experimento', html))
    capitulo = ""

    def sec(m):
        nonlocal capitulo
        clase, cuerpo = m.group(1), m.group(2)
        es_cover = 'Este libro pertenece' not in cuerpo and 'class="folio"' not in cuerpo and "SERIE PEQUEÑOS EXPLORADORES" in cuerpo
        if es_cover:
            sello = (f'<div class="marco-portada"></div><div class="sello"><b>{n_exp}</b><span>experimentos</span></div>'
                     f'<div class="sello2">🔬 Ciencia real<br>🧭 Aventura</div>')
            return f'<section class="page cover {clase.strip()}">{cuerpo}{sello}</section>'
        if "CERTIFICADO OFICIAL" in cuerpo:
            cuerpo = cuerpo.replace("<h1 style", '<div class="estrellas">⭐⭐⭐</div><h1 style', 1)
            return f'<section class="page cert {clase.strip()}">{cuerpo}</section>'
        if 'class="folio"' not in cuerpo:
            return m.group(0)
        if "opener" in clase:
            mm = re.search(r'<div class="num">Capítulo (\d+)</div>\s*<h1>([^<]+)</h1>', cuerpo)
            if mm:
                capitulo = f"Capítulo {mm.group(1)} · {mm.group(2)}"
                cuerpo = cuerpo.replace('<div class="num">', f'<div class="bignum">{mm.group(1)}</div><div class="num">', 1)
            extra = (f'<div class="opener-extra"><div><h4>🔮 Mi predicción</h4><p class="small" style="margin:0">Antes de leer: ¿qué crees que vas a descubrir?</p>{_lineas(2)}</div>'
                     '<div><h4>✅ Mi progreso</h4><ul class="check"><li>Leí el capítulo</li><li>Hice el experimento</li><li>Completé las actividades</li><li>Cumplí el reto</li></ul></div></div>')
            cuerpo = cuerpo.replace('<div class="folio">', extra + '<div class="folio">', 1)
            return f'<section class="page {clase}">{cuerpo}</section>'
        chip = re.search(r'<div class="chip">([^<]*)</div>', cuerpo)
        etiqueta = chip.group(1) if chip else ""
        if etiqueta.strip() == "Experimento" and capitulo:
            etiqueta = capitulo
        if etiqueta.startswith(("Gran final", "Soluciones", "Índice", "Antes", "Lo más", "Conoce")):
            capitulo = capitulo if etiqueta.startswith("Conoce") else capitulo
        head = f'<div class="runhead"><span>{SERIE} · Libro {numero}</span><span>{etiqueta}</span></div>'
        return f'<section class="page {clase}">{head}{cuerpo}</section>'

    html = re.sub(r'<section class="page ([^"]*)">(.*?)</section>', sec, html, flags=re.S)
    open(ruta, "w", encoding="utf-8").write(html)
    print(f"  diseño v2 aplicado a {ruta} ({n_exp} experimentos)")
