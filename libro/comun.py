"""Piezas comunes de la serie «Pequeños Exploradores»: maquetación de páginas,
cajas, experimentos, pasatiempos, soluciones, certificado y contraportada."""
import re

import ilustraciones as I
import pasatiempos as P

SERIE = "Serie Pequeños Exploradores"
LIBROS_SERIE = [
    (1, "¡Sobrevive en el Bosque!", "Orientación, agua, fuego, refugio, nudos, plantas y señales", "🌲"),
    (2, "¡Sobrevive en la Selva!", "Ríos, lluvia, humedad, insectos, camuflaje y plantas tropicales", "🦜"),
    (3, "¡Sobrevive en la Isla!", "Sol, agua dulce, mareas, playa, navegación y vida marina", "🏝️"),
]


def lineas(n):
    return '<div class="lineas">' + "<div></div>" * n + "</div>"


def caja(tipo, titulo, cuerpo):
    return f'<div class="box {tipo}"><h4>{titulo}</h4>{cuerpo}</div>'


def ciencia(cuerpo, titulo="🔬 La ciencia detrás"):
    return caja("ciencia", titulo, cuerpo)


def seguridad(cuerpo, titulo="⚠️ Seguridad"):
    return caja("seguridad", titulo, cuerpo)


def sabias(cuerpo, titulo="💡 ¿Sabías que…?"):
    return caja("sabias", titulo, cuerpo)


def reto(cuerpo, titulo="🏅 Reto de explorador"):
    return caja("reto", titulo, cuerpo)


def mito(cuerpo, titulo="🤔 ¿Mito o realidad?"):
    return caja("mito", titulo, cuerpo)


def chip(t):
    return f'<div class="chip">{t}</div>'


def emoji(e, size=120):
    return f'<span style="font-size:{size}px;line-height:1;display:inline-block">{e}</span>'


def pasos(items, color=None):
    st = f' style="--c:{color}"' if color else ""
    return f'<ol class="pasos"{st}>' + "".join(f"<li>{p}</li>" for p in items) + "</ol>"


def tarjetas(items, cols=3, fondo="var(--cc,#f3f5f2)"):
    """items: (emoji, título, texto)."""
    cel = "".join(
        f'<div style="background:{fondo};border-radius:16px;padding:0.13in 0.15in;border:2px solid #fff;box-shadow:0 0 0 1.5px var(--c,#d5dbd5)"><div style="font-size:32px;line-height:1.1">{e}</div>'
        f'<h4 style="margin:0.04in 0">{t}</h4><p class="small" style="margin:0">{d}</p></div>' for e, t, d in items)
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:0.14in;margin:0.08in 0 0.14in">{cel}</div>'


def vf_tabla(frases):
    filas = "".join(f'<tr><td>{chr(97 + i)}) {f}</td><td style="width:1.1in" class="center"><span class="vf">V</span> <span class="vf">F</span></td></tr>' for i, f in enumerate(frases))
    return f"<table>{filas}</table>"


def unir(izq, der):
    a = "".join(f"<p>{i + 1}. {t} ●</p>" for i, t in enumerate(izq))
    b = "".join(f"<p>● {chr(97 + i)}) {t}</p>" for i, t in enumerate(der))
    return f'<div class="cols" style="font-size:12pt"><div>{a}</div><div>{b}</div></div>'


class Libro:
    def __init__(self, numero, titulo, subtitulo, archivo):
        self.numero = numero
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.archivo = archivo
        self.paginas = []
        self._indice = None

    # ── maquetación básica ──
    def pagina(self, html, clase="", folio=True):
        n = len(self.paginas) + 1
        f = f'<div class="folio"><span>{n}</span></div>' if folio else ""
        self.paginas.append(f'<section class="page {clase}">{html}{f}</section>')

    def apertura(self, num, titulo, sub, color, ilus, aprenderas, dato):
        items = "".join(f"<li>{a}</li>" for a in aprenderas)
        self.pagina(f'''
        <div class="banda">
          <div class="num">Capítulo {num}</div>
          <h1>{titulo}</h1>
          <div class="sub">{sub}</div>
          <div class="ilus">{ilus}</div>
        </div>
        <div class="cuerpo">
          <h3>En este capítulo vas a…</h3>
          <ul class="aprenderas">{items}</ul>
          {sabias(dato)}
        </div>''', f"opener {color}")

    def experimento(self, titulo, color, tiempo, dificultad, materiales, pasos_, ciencia_txt, pregunta,
                    extra="", seg="", n_lineas=3, resultados=""):
        mats = "".join(f"<li>{m}</li>" for m in materiales)
        ps = "".join(f"<li>{p}</li>" for p in pasos_)
        bloque_mat = (f'<div class="cols" style="grid-template-columns:1.1fr 1fr;align-items:center"><div class="materiales"><h4>Materiales</h4><ul style="columns:1">{mats}</ul></div>{extra}</div>'
                      if extra else f'<div class="materiales"><h4>Materiales</h4><ul>{mats}</ul></div>')
        self.pagina(f'''
        {chip("Experimento")}
        <div class="exp-head"><div class="exp-badge">¡A<br>probar!</div><h2 style="margin:0">{titulo}</h2></div>
        <div class="meta"><span>⏱️ {tiempo}</span><span>⭐ Dificultad: {dificultad}</span><span>👨‍👩‍👧 Con un adulto</span></div>
        {bloque_mat}
        <h3 style="margin-top:0.14in">Pasos</h3>
        <ol class="pasos">{ps}</ol>
        {seg}
        {ciencia(ciencia_txt)}
        <h4>{pregunta}</h4>
        {resultados}
        {lineas(n_lineas)}''', color)

    # ── páginas estándar de la serie ──
    def portada(self, escena, temas, fondo_cielo="linear-gradient(#bfe3f5,#e4f3fa)", color_titulo="#1f4d29"):
        self.pagina(f'''
<div style="position:absolute;inset:0;background:{fondo_cielo}"></div><div style="position:absolute;left:0;right:0;bottom:0">{escena}</div>
<div style="position:absolute;top:0.6in;left:0.6in;right:0.6in;text-align:center">
  <div style="display:inline-block;background:#fff;color:#2f6b3a;font-family:Fredoka;font-weight:600;border-radius:30px;padding:6px 20px;font-size:12pt;letter-spacing:.06em">{SERIE.upper()} · LIBRO {self.numero}</div>
  <h1 style="font-size:52pt;color:{color_titulo};margin:0.2in 0 0.05in;text-shadow:0 3px 0 #fff">{self.titulo.replace(" en ", " en<br>", 1) if len(self.titulo) > 18 else self.titulo}</h1>
  <div style="font-family:Fredoka;font-weight:600;font-size:19pt;color:#e0702a;background:rgba(255,255,255,.85);display:inline-block;padding:4px 18px;border-radius:12px">{self.subtitulo}</div>
  <div style="margin-top:0.18in"><div style="display:inline-block;background:#fff;border-radius:16px;padding:8px 20px;font-family:Fredoka;font-size:12.5pt;color:#26302a">{temas}</div></div>
  <div style="margin-top:0.12in;font-family:Fredoka;font-weight:600;color:#26302a;font-size:11pt">LIBRO DE ACTIVIDADES · 8 A 12 AÑOS</div>
</div>''', "", folio=False)

    def propiedad(self, icono):
        self.pagina(f'''
<div class="center" style="margin-top:0.3in">{icono}</div>
<h1 class="center" style="margin-top:0.2in">Este libro pertenece a</h1>
<div style="border-bottom:3px dashed var(--linea);height:0.6in;margin:0 0.6in 0.4in"></div>
<h2 class="center" style="color:var(--naranja)">Mi ficha de explorador</h2>
<div class="cols" style="margin-top:0.2in">
  <div class="marco" style="height:2.6in;display:flex;align-items:center;justify-content:center;color:var(--gris);text-align:center;padding:0.2in">Dibújate aquí con tu equipo de explorador</div>
  <div>
    <p><strong>Nombre de explorador:</strong></p>{lineas(1)}
    <p><strong>Edad:</strong></p>{lineas(1)}
    <p><strong>Mi animal favorito de este libro:</strong></p>{lineas(1)}
    <p><strong>Mi compañero/a de aventuras:</strong></p>{lineas(1)}
  </div>
</div>
<div class="box reto" style="margin-top:0.35in">
  <h4>🏅 Mi promesa de explorador</h4>
  <p class="mano" style="font-size:15pt;line-height:1.5">Prometo explorar con curiosidad, cuidar la naturaleza, no dejar basura, respetar a los animales y las plantas, y hacer los experimentos siempre con un adulto.</p>
  <p style="margin-top:0.25in">Firma: ______________________________</p>
</div>''')

    def reservar_indice(self):
        self._indice = len(self.paginas)
        self.pagina("__INDICE__")

    def sopa(self, palabras, color, semilla=5, n=14):
        grid, sol, _ = P.sopa_de_letras(palabras, n=n, semilla=semilla)
        self._sopa = (grid, sol, n)
        filas = "".join("<tr>" + "".join(f"<td>{ch}</td>" for ch in fila) + "</tr>" for fila in grid)
        lista = "".join(f'<span style="display:inline-block;width:1.35in;font-family:Fredoka;font-weight:600">☐ {p}</span>' for p in palabras)
        self.pagina(f'''
{chip("Gran final · Pasatiempos")}
<h2>Sopa de letras del explorador</h2>
<p>Encuentra las {len(palabras)} palabras escondidas. Pueden estar en horizontal, vertical, diagonal… ¡y algunas al revés!</p>
<table class="grid-sopa" style="margin:0.15in auto 0.25in">{filas}</table>
<div class="marco" style="padding:0.14in 0.2in;border-style:solid">{lista}</div>''', color)

    def _cruci_html(self, mostrar):
        f, c, celdas, numeros, _, _ = self._cruci
        h = ""
        for r in range(f):
            h += "<tr>"
            for cc in range(c):
                if (r, cc) in celdas:
                    n = numeros.get((r, cc))
                    h += f'<td class="l">{f"<span class=n>{n}</span>" if n else ""}{f"<span class=s>{celdas[(r, cc)]}</span>" if mostrar else ""}</td>'
                else:
                    h += "<td></td>"
            h += "</tr>"
        return f'<table class="cruci{" mini" if mostrar else ""}" style="width:{c * (0.27 if mostrar else 0.34):.2f}in">{h}</table>'

    def crucigrama(self, entradas, color, titulo="Crucigrama del explorador"):
        self._cruci = P.crucigrama(entradas)
        _, _, _, _, horiz, vert = self._cruci
        ph = "".join(f"<li><strong>{n}.</strong> {p} <span class='tiny'>({len(w)})</span></li>" for n, w, p in horiz)
        pv = "".join(f"<li><strong>{n}.</strong> {p} <span class='tiny'>({len(w)})</span></li>" for n, w, p in vert)
        self.pagina(f'''
{chip("Gran final · Pasatiempos")}
<h2>{titulo}</h2>
<p class="small">Todas las respuestas están en este libro. Escríbelas sin tildes. El número entre paréntesis indica cuántas letras tiene la palabra.</p>
<div style="margin:0.12in 0 0.18in">{self._cruci_html(False)}</div>
<div class="cols small">
<div><h4>➡️ Horizontales</h4><ul style="list-style:none;padding-left:0">{ph}</ul></div>
<div><h4>⬇️ Verticales</h4><ul style="list-style:none;padding-left:0">{pv}</ul></div>
</div>''', color)

    def mochila_examen(self, mochila, preguntas, intro, color="c-verde"):
        mitad = (len(mochila) + 1) // 2
        qs = "".join(f"<li>{q} &nbsp; " + "".join(f'<span class="opcion">{chr(97 + i)}) {o}</span>' for i, o in enumerate(ops)) + "</li>" for q, ops in preguntas)
        self.pagina(f'''
{chip("Gran final")}
<h2>La mochila del explorador</h2>
<p>{intro}</p>
<div class="cols">
<ul class="check">{"".join(f"<li>{m}</li>" for m in mochila[:mitad])}</ul>
<ul class="check">{"".join(f"<li>{m}</li>" for m in mochila[mitad:])}</ul>
</div>
<div class="box reto"><h4>📝 Antes de salir, deja una nota en casa</h4>
<div class="cols small"><div><p>Vamos a: ______________________</p><p>Salimos a las: _________________</p></div><div><p>Volvemos a las: ________________</p><p>Vamos con: ____________________</p></div></div></div>
<h3>El gran examen del explorador</h3>
<ol class="small" style="padding-left:0.22in">{qs}</ol>''', color)

    def soluciones(self, bloques_izq, bloque_der=""):
        izq = "".join(f"<h4>{t}</h4><p>{d}</p>" for t, d in bloques_izq)
        self.pagina(f'''
{chip("Soluciones")}
<h2>Soluciones</h2>
<div class="cols small" style="gap:0.2in{";grid-template-columns:1fr" if not bloque_der else ""}">
<div>{izq}</div>
{f"<div>{bloque_der}</div>" if bloque_der else ""}
</div>''', "c-morado")

    def soluciones_pasatiempos(self):
        grid, sol, n = self._sopa
        h = ""
        for r in range(n):
            h += "<tr>" + "".join(
                f'<td style="background:#fde9d9;color:#c8412f">{grid[r][c]}</td>' if sol[r][c] else f'<td style="color:#c9cfc9">{grid[r][c]}</td>'
                for c in range(n)) + "</tr>"
        self.pagina(f'''
{chip("Soluciones")}
<h2>Solución del crucigrama</h2>
<div style="margin:0.1in 0 0.25in">{self._cruci_html(True)}</div>
<h2>Solución de la sopa de letras</h2>
<div style="margin-top:0.1in"><table class="grid-sopa mini" style="font-size:9.5pt">{h}</table></div>''', "c-morado")

    def glosario(self, terminos):
        filas = "".join(f'<tr><td style="width:1.6in"><strong>{t}</strong></td><td>{d}</td></tr>' for t, d in sorted(terminos, key=lambda x: __import__("unicodedata").normalize("NFD", x[0]).encode("ascii", "ignore").decode().lower()))
        self.pagina(f'''
{chip("Soluciones")}
<h2>Glosario del explorador</h2>
<table>{filas}</table>''', "c-morado")

    def colorear(self, escena_color, pregunta):
        self.pagina(f'''
{chip("Gran final · Para colorear")}
<h2>Colorea tu aventura</h2>
<p>Usa los colores de la naturaleza. ¡Y agrega los animales, huellas o nubes que quieras!</p>
<div class="marco" style="border-style:solid;overflow:hidden;margin-top:0.15in">{I.para_colorear(escena_color)}</div>
<p class="small" style="margin-top:0.15in">{pregunta}</p>
{lineas(2)}''', "c-verde")

    def notas(self):
        self.pagina(f'''
{chip("Gran final")}
<h2>Mis notas de explorador</h2>
<p>Anota aquí tus descubrimientos, preguntas nuevas y las aventuras que quieres vivir.</p>
{lineas(22)}''', "c-verde")

    def certificado(self, rango, temas):
        self.pagina(f'''
<div style="position:absolute;inset:0.4in;border:6px double #2f6b3a;border-radius:24px;padding:0.5in;text-align:center">
<div style="margin-top:0.1in">{I.brujula_icono(120)}</div>
<div style="font-family:Fredoka;font-weight:600;color:var(--naranja);letter-spacing:.2em;font-size:13pt;margin-top:0.2in">CERTIFICADO OFICIAL · LIBRO {self.numero}</div>
<h1 style="font-size:36pt;margin:0.1in 0 0.3in">{rango}</h1>
<p style="font-size:14pt">Se otorga este certificado a</p>
<div style="border-bottom:3px solid var(--tinta);width:5in;margin:0.5in auto 0.3in"></div>
<p style="font-size:13pt;max-width:5.4in;margin:0 auto">por completar su entrenamiento en <strong>{temas}</strong>, y por demostrar curiosidad, prudencia y respeto por la naturaleza.</p>
<div style="display:flex;justify-content:space-around;margin-top:0.8in">
<div><div style="border-bottom:2px solid var(--tinta);width:2.2in;height:0.4in"></div><p class="small">Fecha</p></div>
<div><div style="border-bottom:2px solid var(--tinta);width:2.2in;height:0.4in"></div><p class="small">Firma del adulto guía</p></div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0.25in">{I.camino_bosque_deco(620)}</div>
</div>''', folio=False)

    def contraportada(self, escena, pregunta, parrafos, color_fondo="#2f6b3a"):
        ps = "".join(f'<p style="font-size:13pt;max-width:6.2in">{p}</p>' for p in parrafos)
        serie = "".join(
            f'<div style="flex:1;background:{"#fff" if n == self.numero else "rgba(255,255,255,.14)"};color:{"#26302a" if n == self.numero else "#fff"};border-radius:12px;padding:8px 10px;font-size:9.5pt">'
            f'<div style="font-size:20px">{e}</div><strong style="font-family:Fredoka;font-size:10.5pt">Libro {n}: {t}</strong><br>{d}</div>'
            for n, t, d, e in LIBROS_SERIE)
        self.pagina(f'''
<div style="position:absolute;inset:0;background:{color_fondo}"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:3.6in;overflow:hidden">{escena}</div>
<div style="position:relative;color:#fff;padding:0.2in 0.2in 0">
<h1 style="color:#fff;font-size:30pt">{pregunta}</h1>
{ps}
<p style="font-family:Fredoka;font-size:13pt;background:rgba(255,255,255,.15);display:inline-block;padding:6px 16px;border-radius:12px">🔬 Ciencia real &nbsp;·&nbsp; 🧭 Aventura &nbsp;·&nbsp; ⚠️ Seguridad primero &nbsp;·&nbsp; 👨‍👩‍👧 En familia</p>
<h3 style="color:#fff;margin-top:0.12in">Colecciona la {SERIE}:</h3>
<div style="display:flex;gap:0.12in">{serie}</div>
</div>''', folio=False)

    # ── salida ──
    def construir(self, extras_indice):
        titulos = []
        for i, p in enumerate(self.paginas):
            m = re.search(r'<div class="num">Capítulo (\d+)</div>\s*<h1>([^<]+)</h1>', p)
            if m:
                titulos.append((f"Capítulo {m.group(1)}", m.group(2), i + 1))
        extra = []
        for clave, nombre, despues in extras_indice:
            for i, p in enumerate(self.paginas):
                if clave in p:
                    extra.append((nombre, i + 1, despues))
                    break
        filas = ""
        for nombre, pg, despues in extra:
            if not despues:
                filas += f'<tr><td colspan="2"><strong>{nombre}</strong></td><td class="center">{pg}</td></tr>'
        colores = ["var(--verde)", "var(--azul)", "var(--naranja)", "var(--cafe)", "#6d4c9f", "var(--verde)", "var(--azul)"]
        for (cap, nombre, pg), col in zip(titulos, colores):
            filas += f'<tr><td style="width:1.3in;color:{col};font-family:Fredoka;font-weight:600">{cap}</td><td style="font-family:Fredoka;font-size:14pt;font-weight:600">{nombre}</td><td class="center" style="width:0.8in">{pg}</td></tr>'
        for nombre, pg, despues in extra:
            if despues:
                filas += f'<tr><td colspan="2"><strong>{nombre}</strong></td><td class="center">{pg}</td></tr>'
        indice = f'''
{chip("Índice")}
<h1>Tu mapa del libro</h1>
<p>Puedes leerlo en orden o saltar al capítulo que más te guste. ¡Pero no te saltes las reglas de oro!</p>
<table style="font-size:12.5pt;margin-top:0.2in">
<tr><th colspan="2">Sección</th><th class="center">Página</th></tr>
{filas}
</table>
<div class="fig" style="margin-top:0.4in">{I.camino_bosque_deco()}</div>'''
        if self._indice is not None:
            self.paginas[self._indice] = self.paginas[self._indice].replace("__INDICE__", indice)
        html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>{self.titulo} {self.subtitulo}</title>
<link rel="stylesheet" href="estilos.css"></head>
<body>
{"".join(self.paginas)}
</body></html>'''
        open(self.archivo, "w", encoding="utf-8").write(html)
        print(f"{self.archivo}: {len(self.paginas)} páginas")
