"""Ilustraciones SVG en línea para el libro. Todo vectorial para impresión nítida."""

VERDE = "#2f6b3a"
VERDE2 = "#4f9a4a"
VERDE3 = "#7cbf6a"
CAFE = "#7a5230"
CAFE2 = "#a8764a"
NARANJA = "#e0702a"
AMARILLO = "#f4c542"
AZUL = "#2d7fb8"
AZUL2 = "#8cc3e8"
ROJO = "#c8412f"
TINTA = "#26302a"
GRIS = "#8a938c"
FONT = 'font-family="Fredoka, sans-serif"'


def svg(w, h, body, extra=""):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {extra}>{body}</svg>'


def txt(x, y, s, size=14, color=TINTA, anchor="middle", weight=600):
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{s}</text>'


def flecha_def(id_, color):
    return (f'<defs><marker id="{id_}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker></defs>')


def pino(x, y, h, color=VERDE, tronco=CAFE):
    w = h * 0.55
    t = (f'<rect x="{x - h * 0.05}" y="{y - h * 0.18}" width="{h * 0.1}" height="{h * 0.18}" fill="{tronco}"/>')
    for i, (f, off) in enumerate([(1.0, 0.15), (0.8, 0.42), (0.6, 0.66)]):
        base = y - h * off
        top = base - h * 0.42
        ww = w * f
        t += f'<polygon points="{x - ww / 2},{base} {x + ww / 2},{base} {x},{top}" fill="{color}"/>'
    return t


def arbol(x, y, h, color=VERDE2):
    return (f'<rect x="{x - h * 0.06}" y="{y - h * 0.45}" width="{h * 0.12}" height="{h * 0.45}" fill="{CAFE}"/>'
            f'<circle cx="{x}" cy="{y - h * 0.62}" r="{h * 0.3}" fill="{color}"/>'
            f'<circle cx="{x - h * 0.2}" cy="{y - h * 0.5}" r="{h * 0.2}" fill="{color}"/>'
            f'<circle cx="{x + h * 0.2}" cy="{y - h * 0.5}" r="{h * 0.2}" fill="{color}"/>')


def sol(x, y, r, color=AMARILLO):
    rays = ""
    import math
    for i in range(12):
        a = i * math.pi / 6
        rays += (f'<line x1="{x + math.cos(a) * r * 1.3:.1f}" y1="{y + math.sin(a) * r * 1.3:.1f}" '
                 f'x2="{x + math.cos(a) * r * 1.7:.1f}" y2="{y + math.sin(a) * r * 1.7:.1f}" stroke="{color}" stroke-width="{r * 0.18:.1f}" stroke-linecap="round"/>')
    return rays + f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'


def nube(x, y, s=1.0, color="#ffffff", stroke=None):
    st = f' stroke="{stroke}" stroke-width="2"' if stroke else ""
    return (f'<g transform="translate({x},{y}) scale({s})"{st} fill="{color}">'
            '<circle cx="0" cy="0" r="22"/><circle cx="26" cy="-10" r="28"/><circle cx="56" cy="0" r="22"/>'
            '<rect x="0" y="0" width="56" height="22"/></g>')


def fogata(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="-40" y="-8" width="80" height="14" rx="7" fill="{CAFE}" transform="rotate(12)"/>'
            f'<rect x="-40" y="-8" width="80" height="14" rx="7" fill="{CAFE2}" transform="rotate(-12)"/>'
            f'<path d="M0,-95 C25,-60 35,-40 28,-15 C22,0 -22,0 -28,-15 C-35,-40 -20,-55 -8,-70 C-5,-55 5,-50 0,-95z" fill="{NARANJA}"/>'
            f'<path d="M0,-55 C14,-38 18,-25 12,-12 C8,-4 -8,-4 -12,-12 C-16,-25 -8,-35 0,-55z" fill="{AMARILLO}"/>'
            '</g>')


def tienda(x, y, s=1.0, color=NARANJA):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<polygon points="-70,0 70,0 0,-90" fill="{color}"/>'
            f'<polygon points="-18,0 18,0 0,-50" fill="#8a3d12"/>'
            f'<line x1="0" y1="-90" x2="0" y2="-104" stroke="{TINTA}" stroke-width="4"/></g>')


def portada_escena():
    b = ""
    b += '<defs><linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfe3f5"/><stop offset="1" stop-color="#fdf1d6"/></linearGradient></defs>'
    b += '<rect width="816" height="620" fill="url(#cielo)"/>'
    b += sol(650, 120, 45)
    b += nube(120, 110, 1.2) + nube(420, 70, 0.9)
    b += f'<polygon points="0,420 180,230 330,400 470,210 640,380 816,250 816,620 0,620" fill="#9cc4a3"/>'
    b += f'<polygon points="0,470 150,360 300,470 500,330 700,460 816,400 816,620 0,620" fill="{VERDE3}"/>'
    for i, (x, h) in enumerate([(40, 190), (110, 150), (740, 200), (680, 150), (790, 130), (170, 120), (600, 110)]):
        b += pino(x, 560 + (i % 2) * 10, h, VERDE if i % 2 == 0 else VERDE2)
    b += f'<rect x="0" y="540" width="816" height="80" fill="{VERDE2}"/>'
    b += tienda(300, 560, 1.3)
    b += fogata(510, 575, 0.9)
    for i in range(5):
        b += f'<circle cx="{470 + i * 20}" cy="580" r="9" fill="{GRIS}"/>'
    return svg(816, 620, b, 'preserveAspectRatio="xMidYMax slice" style="display:block;width:100%;height:auto"')


def palo_sombra():
    b = flecha_def("fa", ROJO)
    b += f'<rect width="520" height="250" fill="#fff"/>'
    b += sol(70, 55, 24)
    b += f'<line x1="20" y1="200" x2="500" y2="200" stroke="{CAFE2}" stroke-width="4"/>'
    b += f'<rect x="0" y="202" width="520" height="48" fill="#efe3cf"/>'
    b += f'<line x1="260" y1="200" x2="260" y2="95" stroke="{CAFE}" stroke-width="8" stroke-linecap="round"/>'
    b += f'<polygon points="260,200 395,200 395,204 260,206" fill="#555" opacity="0.5"/>'
    b += f'<polygon points="260,200 450,212 450,216 260,206" fill="#555" opacity="0.3"/>'
    b += f'<circle cx="395" cy="202" r="8" fill="{AZUL}"/><circle cx="450" cy="214" r="8" fill="{ROJO}"/>'
    b += f'<line x1="395" y1="226" x2="448" y2="236" stroke="{ROJO}" stroke-width="3" marker-end="url(#fa)"/>'
    b += txt(360, 240, "1ª marca", 13, AZUL) + txt(478, 242, "2ª", 13, ROJO)
    b += txt(395, 180, "OESTE", 15, AZUL, weight=700) + txt(462, 192, "ESTE", 15, ROJO, weight=700)
    b += txt(260, 85, "palo", 14, CAFE)
    b += txt(170, 235, "la sombra se mueve de Oeste a Este", 13, TINTA)
    return svg(520, 250, b)


def reloj_metodo():
    b = f'<circle cx="90" cy="90" r="70" fill="#fff" stroke="{TINTA}" stroke-width="4"/>'
    for i in range(12):
        import math
        a = i * math.pi / 6
        b += f'<line x1="{90 + math.sin(a) * 58:.1f}" y1="{90 - math.cos(a) * 58:.1f}" x2="{90 + math.sin(a) * 66:.1f}" y2="{90 - math.cos(a) * 66:.1f}" stroke="{TINTA}" stroke-width="3"/>'
    b += f'<line x1="90" y1="90" x2="90" y2="30" stroke="{GRIS}" stroke-width="4"/>'
    b += f'<line x1="90" y1="90" x2="140" y2="118" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/>'
    b += f'<line x1="90" y1="90" x2="146" y2="55" stroke="{ROJO}" stroke-width="3" stroke-dasharray="6 4"/>'
    b += sol(172, 132, 13)
    b += txt(160, 40, "SUR", 13, ROJO, weight=700)
    return svg(210, 180, b)


def estrellas():
    b = f'<rect width="520" height="250" rx="16" fill="#1f2a44"/>'
    # Osa Mayor (hemisferio norte)
    osa = [(40, 190), (80, 180), (115, 185), (145, 200), (205, 205), (215, 160), (160, 150)]
    pts = " ".join(f"{x},{y}" for x, y in osa[:5]) + f" {osa[5][0]},{osa[5][1]} {osa[6][0]},{osa[6][1]} {osa[3][0]},{osa[3][1]}"
    b += f'<polyline points="{pts}" fill="none" stroke="#6f7fa8" stroke-width="1.5"/>'
    for x, y in osa:
        b += f'<circle cx="{x}" cy="{y}" r="4.5" fill="#fff"/>'
    b += f'<line x1="205" y1="205" x2="225" y2="50" stroke="{AMARILLO}" stroke-width="2" stroke-dasharray="6 5"/>'
    b += f'<circle cx="227" cy="42" r="7" fill="{AMARILLO}"/>'
    b += txt(227, 26, "Estrella Polar = NORTE", 12, AMARILLO)
    b += txt(120, 232, "Osa Mayor (hemisferio norte)", 12, "#cfd8ee")
    # Cruz del Sur
    cruz = {"top": (400, 40), "bot": (400, 110), "izq": (372, 80), "der": (425, 70)}
    b += f'<line x1="400" y1="40" x2="400" y2="110" stroke="#6f7fa8" stroke-width="1.5"/>'
    b += f'<line x1="372" y1="80" x2="425" y2="70" stroke="#6f7fa8" stroke-width="1.5"/>'
    for x, y in cruz.values():
        b += f'<circle cx="{x}" cy="{y}" r="5" fill="#fff"/>'
    b += f'<line x1="400" y1="110" x2="400" y2="200" stroke="{AMARILLO}" stroke-width="2" stroke-dasharray="6 5"/>'
    b += f'<line x1="330" y1="205" x2="470" y2="205" stroke="#8fa0c8" stroke-width="2"/>'
    b += txt(400, 222, "SUR (baja la vista al horizonte)", 12, AMARILLO)
    b += txt(400, 242, "Cruz del Sur (hemisferio sur)", 12, "#cfd8ee")
    return svg(520, 250, b)


def rosa_vientos(vacia=False, size=260):
    import math
    c = size / 2
    b = f'<circle cx="{c}" cy="{c}" r="{c - 30}" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
    for i in range(8):
        a = i * math.pi / 4
        L = (c - 45) if i % 2 == 0 else (c - 80)
        wdt = 16 if i % 2 == 0 else 10
        x, y = c + math.sin(a) * L, c - math.cos(a) * L
        lx, ly = c + math.sin(a - math.pi / 2) * wdt, c - math.cos(a - math.pi / 2) * wdt
        rx, ry = c + math.sin(a + math.pi / 2) * wdt, c - math.cos(a + math.pi / 2) * wdt
        col1 = VERDE if i % 2 == 0 else VERDE3
        b += f'<polygon points="{x:.1f},{y:.1f} {lx:.1f},{ly:.1f} {c},{c}" fill="{col1}"/>'
        b += f'<polygon points="{x:.1f},{y:.1f} {rx:.1f},{ry:.1f} {c},{c}" fill="#cfe6c6" stroke="{col1}" stroke-width="1"/>'
    etiquetas = ["N", "NE", "E", "SE", "S", "SO", "O", "NO"]
    for i, e in enumerate(etiquetas):
        a = i * math.pi / 4
        x, y = c + math.sin(a) * (c - 14), c - math.cos(a) * (c - 14) + 6
        if vacia and e != "N":
            b += f'<rect x="{x - 17:.1f}" y="{y - 20:.1f}" width="34" height="26" rx="6" fill="#fff" stroke="{GRIS}" stroke-width="1.5" stroke-dasharray="4 3"/>'
        else:
            b += txt(f"{x:.1f}", f"{y:.1f}", e, 17, ROJO if e == "N" else TINTA, weight=700)
    return svg(size, size, b)


def ciclo_agua():
    b = flecha_def("fb", AZUL)
    b += f'<rect width="560" height="270" rx="16" fill="#eaf5fb"/>'
    b += sol(60, 55, 24)
    b += f'<polygon points="0,270 0,190 110,90 210,200 260,170 300,270" fill="#9cc4a3"/>'
    b += f'<polygon points="85,113 110,90 135,117 118,112 105,120" fill="#fff"/>'
    b += pino(200, 250, 60) + pino(240, 255, 45, VERDE2)
    b += f'<path d="M280,270 Q380,215 560,225 L560,270 z" fill="{AZUL2}"/>'
    b += nube(250, 55, 1.0, "#fff", "#b8cfdd") + nube(390, 45, 0.8, "#fff", "#b8cfdd")
    for i in range(6):
        b += f'<line x1="{255 + i * 12}" y1="95" x2="{248 + i * 12}" y2="118" stroke="{AZUL}" stroke-width="3" stroke-linecap="round"/>'
    b += f'<path d="M470,215 C500,170 490,120 470,85" fill="none" stroke="{AZUL}" stroke-width="3" stroke-dasharray="7 5" marker-end="url(#fb)"/>'
    b += f'<path d="M440,50 C400,20 360,20 340,35" fill="none" stroke="{AZUL}" stroke-width="3" marker-end="url(#fb)"/>'
    b += f'<path d="M160,170 C200,210 240,225 285,235" fill="none" stroke="{AZUL}" stroke-width="3" marker-end="url(#fb)"/>'
    b += txt(510, 150, "1. Evaporación", 13, AZUL, "end")
    b += txt(470, 24, "2. Condensación", 13, AZUL)
    b += txt(270, 145, "3. Precipitación", 13, AZUL, "start")
    b += txt(125, 262, "4. Escorrentía", 13, AZUL, "start")
    return svg(560, 270, b)


def filtro_agua():
    b = f'<rect x="120" y="20" width="140" height="300" rx="20" fill="#f4fbff" stroke="{AZUL}" stroke-width="3"/>'
    capas = [("grava (piedritas)", 60, "#a3a3a3"), ("arena gruesa", 50, "#d8b98a"), ("arena fina", 50, "#ecd7ad"),
             ("carbón triturado", 45, "#3d3d3d"), ("algodón o tela", 30, "#ffffff")]
    y = 60
    for nombre, h, col in capas:
        b += f'<rect x="123" y="{y}" width="134" height="{h}" fill="{col}" stroke="#ccc"/>'
        b += f'<line x1="258" y1="{y + h / 2}" x2="290" y2="{y + h / 2}" stroke="{GRIS}" stroke-width="1.5"/>'
        b += txt(296, y + h / 2 + 5, nombre, 13, TINTA, "start")
        y += h
    b += f'<path d="M175,325 L205,325 L195,345 L185,345z" fill="{AZUL2}" stroke="{AZUL}"/>'
    b += f'<rect x="150" y="355" width="80" height="55" rx="6" fill="{AZUL2}" opacity="0.6" stroke="{AZUL}" stroke-width="2"/>'
    b += txt(190, 430, "agua más clara", 13, AZUL)
    b += f'<path d="M150,5 q40,40 80,0" fill="#8b6a3e" opacity="0.7"/>'
    b += txt(60, 45, "agua turbia", 13, CAFE, "middle")
    b += txt(60, 62, "entra por arriba", 11, GRIS, "middle", 400)
    b += txt(55, 200, "botella", 12, GRIS, "middle", 400)
    b += txt(55, 216, "boca abajo", 12, GRIS, "middle", 400)
    return svg(470, 440, b)


def bolsa_transpiracion():
    b = f'<path d="M20,210 C80,190 120,150 150,100" stroke="{CAFE}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    for (x, y, r) in [(160, 90, 0), (190, 70, 30), (175, 125, -30), (215, 105, 10), (205, 45, -20), (240, 80, 25)]:
        b += f'<ellipse cx="{x}" cy="{y}" rx="24" ry="11" fill="{VERDE2}" transform="rotate({r} {x} {y})"/>'
    b += f'<path d="M140,110 C130,20 280,0 275,90 C272,130 250,170 205,178 C170,180 145,150 140,110z" fill="#dff1ff" fill-opacity="0.45" stroke="{AZUL}" stroke-width="2.5"/>'
    b += f'<line x1="140" y1="112" x2="158" y2="98" stroke="{ROJO}" stroke-width="5"/>'
    for (x, y) in [(170, 150), (190, 160), (215, 162), (235, 150), (250, 128), (262, 100)]:
        b += f'<path d="M{x},{y - 7} q5,8 0,10 q-5,-2 0,-10z" fill="{AZUL}"/>'
    b += f'<ellipse cx="208" cy="172" rx="28" ry="5" fill="{AZUL}" opacity="0.7"/>'
    b += sol(300, 30, 16)
    b += txt(95, 245, "rama viva al sol", 12, CAFE)
    b += txt(270, 205, "gotitas de agua", 12, AZUL)
    return svg(340, 255, b)


def triangulo_fuego():
    b = f'<polygon points="180,20 330,270 30,270" fill="{NARANJA}" opacity="0.14" stroke="{NARANJA}" stroke-width="6" stroke-linejoin="round"/>'
    b += fogata(180, 220, 0.8)
    b += f'<g transform="translate(88,140) rotate(-59)">{txt(0, 0, "CALOR", 20, ROJO, weight=700)}</g>'
    b += f'<g transform="translate(272,140) rotate(59)">{txt(0, 0, "OXÍGENO", 20, AZUL, weight=700)}</g>'
    b += txt(180, 300, "COMBUSTIBLE", 20, CAFE, weight=700)
    return svg(360, 310, b)


def combustibles():
    b = ""
    # yesca
    for i in range(14):
        b += f'<path d="M{30 + i * 6},110 q{(-1) ** i * 12},-40 {(-1) ** i * 4},-70" stroke="#c9a458" stroke-width="2" fill="none"/>'
    b += txt(70, 140, "YESCA", 16, NARANJA, weight=700) + txt(70, 158, "fina como cabello", 12, GRIS, weight=400)
    # astillas
    for i in range(6):
        b += f'<line x1="{180 + i * 9}" y1="112" x2="{205 + i * 9}" y2="40" stroke="{CAFE2}" stroke-width="5" stroke-linecap="round"/>'
    b += txt(220, 140, "ASTILLAS", 16, NARANJA, weight=700) + txt(220, 158, "grosor de un lápiz", 12, GRIS, weight=400)
    # leña
    for i in range(3):
        b += f'<rect x="{320 + i * 26}" y="40" width="20" height="74" rx="9" fill="{CAFE}"/>'
    b += txt(360, 140, "LEÑA", 16, NARANJA, weight=700) + txt(360, 158, "grosor de tu muñeca", 12, GRIS, weight=400)
    b += flecha_def("fc", GRIS) + f'<line x1="120" y1="75" x2="165" y2="75" stroke="{GRIS}" stroke-width="3" marker-end="url(#fc)"/>'
    b += f'<line x1="262" y1="75" x2="308" y2="75" stroke="{GRIS}" stroke-width="3" marker-end="url(#fc)"/>'
    return svg(430, 170, b)


def estructuras_fuego():
    b = ""
    # tipi
    for i, dx in enumerate([-40, -20, 0, 20, 40]):
        b += f'<line x1="{110 + dx}" y1="160" x2="{110 + dx * 0.1}" y2="50" stroke="{CAFE2 if i % 2 else CAFE}" stroke-width="6" stroke-linecap="round"/>'
    b += f'<ellipse cx="110" cy="150" rx="18" ry="10" fill="#e6c77a"/>'
    b += txt(110, 190, "Tipi", 17, NARANJA, weight=700)
    b += txt(110, 208, "prende rápido", 12, GRIS, weight=400)
    # cabaña
    y = 160
    for row in range(5):
        if row % 2 == 0:
            b += f'<rect x="265" y="{y - 10}" width="110" height="10" rx="5" fill="{CAFE}"/>'
            b += f'<rect x="265" y="{y - 10}" width="110" height="10" rx="5" fill="{CAFE}" transform="translate(0,-2)"/>'
        else:
            b += f'<rect x="275" y="{y - 12}" width="12" height="12" rx="6" fill="{CAFE2}"/><rect x="353" y="{y - 12}" width="12" height="12" rx="6" fill="{CAFE2}"/>'
        y -= 14
    b += f'<ellipse cx="320" cy="150" rx="22" ry="8" fill="#e6c77a"/>'
    b += txt(320, 190, "Cabaña", 17, NARANJA, weight=700)
    b += txt(320, 208, "dura más y da buenas brasas", 12, GRIS, weight=400)
    return svg(430, 215, b)


def perdida_calor():
    paneles = [
        ("Conducción", "tocar algo frío (el suelo)", AZUL),
        ("Convección", "el viento se lleva el calor", AZUL),
        ("Radiación", "el cuerpo emite calor al aire", ROJO),
        ("Evaporación", "el sudor y la ropa mojada", AZUL),
    ]
    b = flecha_def("fd", ROJO)
    for i, (t, d, col) in enumerate(paneles):
        x = i * 150
        b += f'<rect x="{x + 4}" y="4" width="140" height="160" rx="14" fill="#fff" stroke="#dfe3de" stroke-width="2"/>'
        cx, cy = x + 74, 80
        # persona
        b += f'<circle cx="{cx}" cy="{cy - 38}" r="11" fill="{NARANJA}"/><rect x="{cx - 11}" y="{cy - 25}" width="22" height="34" rx="9" fill="{NARANJA}"/>'
        if i == 0:
            b += f'<rect x="{cx - 11}" y="{cy + 5}" width="22" height="16" rx="6" fill="{NARANJA}"/>'
            b += f'<rect x="{x + 20}" y="{cy + 20}" width="110" height="10" fill="{AZUL2}"/>'
            b += f'<line x1="{cx}" y1="{cy + 5}" x2="{cx}" y2="{cy + 24}" stroke="{ROJO}" stroke-width="3" marker-end="url(#fd)"/>'
        elif i == 1:
            b += f'<rect x="{cx - 9}" y="{cy + 8}" width="7" height="22" fill="{NARANJA}"/><rect x="{cx + 2}" y="{cy + 8}" width="7" height="22" fill="{NARANJA}"/>'
            for k in range(3):
                b += f'<path d="M{x + 15},{cy - 40 + k * 22} q15,-8 30,0 t30,0" stroke="{AZUL}" stroke-width="3" fill="none"/>'
            b += f'<line x1="{cx + 14}" y1="{cy - 12}" x2="{cx + 52}" y2="{cy - 12}" stroke="{ROJO}" stroke-width="3" marker-end="url(#fd)"/>'
        elif i == 2:
            b += f'<rect x="{cx - 9}" y="{cy + 8}" width="7" height="22" fill="{NARANJA}"/><rect x="{cx + 2}" y="{cy + 8}" width="7" height="22" fill="{NARANJA}"/>'
            for ang in [(-40, -55), (40, -55), (-50, -10), (50, -10)]:
                b += f'<line x1="{cx + ang[0] * 0.35}" y1="{cy - 20 + ang[1] * 0.2}" x2="{cx + ang[0]}" y2="{cy - 20 + ang[1] * 0.6}" stroke="{ROJO}" stroke-width="3" stroke-dasharray="4 3" marker-end="url(#fd)"/>'
        else:
            b += f'<rect x="{cx - 9}" y="{cy + 8}" width="7" height="22" fill="{NARANJA}"/><rect x="{cx + 2}" y="{cy + 8}" width="7" height="22" fill="{NARANJA}"/>'
            for (dx, dy) in [(-22, -30), (20, -18), (-18, 0), (24, 8)]:
                b += f'<path d="M{cx + dx},{cy + dy - 7} q5,8 0,10 q-5,-2 0,-10z" fill="{AZUL}"/>'
            b += f'<path d="M{cx + 30},{cy - 40} q6,-8 0,-16 q-6,-8 0,-16" stroke="{GRIS}" stroke-width="2.5" fill="none"/>'
        b += txt(cx, 135, t, 14, col, weight=700)
        b += txt(cx, 153, d, 9.5, GRIS, weight=400)
    return svg(600, 170, b)


def refugios():
    b = ""
    # cobertizo
    b += f'<line x1="20" y1="60" x2="170" y2="60" stroke="{CAFE}" stroke-width="7" stroke-linecap="round"/>'
    b += f'<line x1="30" y1="60" x2="30" y2="150" stroke="{CAFE}" stroke-width="7"/><line x1="160" y1="60" x2="160" y2="150" stroke="{CAFE}" stroke-width="7"/>'
    for i in range(8):
        b += f'<line x1="{30 + i * 18}" y1="58" x2="{50 + i * 18}" y2="150" stroke="{CAFE2}" stroke-width="5"/>'
    b += f'<polygon points="28,64 170,64 188,150 48,150" fill="{VERDE2}" opacity="0.65"/>'
    b += f'<rect x="10" y="150" width="190" height="6" fill="#c9b08a"/>'
    b += txt(105, 185, "Cobertizo", 16, CAFE, weight=700) + txt(105, 203, "techo inclinado contra el viento", 11, GRIS, weight=400)
    # tienda en A
    ox = 230
    b += f'<polygon points="{ox + 10},150 {ox + 90},55 {ox + 170},150" fill="{VERDE2}" opacity="0.8"/>'
    for i in range(7):
        b += f'<line x1="{ox + 90}" y1="55" x2="{ox + 20 + i * 24}" y2="150" stroke="{CAFE2}" stroke-width="4"/>'
    b += f'<line x1="{ox}" y1="58" x2="{ox + 185}" y2="52" stroke="{CAFE}" stroke-width="7" stroke-linecap="round"/>'
    b += f'<polygon points="{ox + 72},150 {ox + 108},150 {ox + 90},112" fill="#3b2a1a"/>'
    b += f'<rect x="{ox}" y="150" width="190" height="6" fill="#c9b08a"/>'
    b += txt(ox + 90, 185, "Tienda en A", 16, CAFE, weight=700) + txt(ox + 90, 203, "dos lados cubiertos", 11, GRIS, weight=400)
    # hojarasca
    ox = 460
    b += f'<path d="M{ox},150 Q{ox + 20},80 {ox + 50},70 L{ox + 180},135 L{ox + 185},150z" fill="#b5873f"/>'
    for i in range(24):
        import random
        random.seed(i)
        x = ox + 15 + random.random() * 160
        y = 80 + random.random() * 65
        if y > 70 + (x - ox - 50) * 0.5:
            b += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="8" ry="4" fill="{["#d49a3a", "#a5652a", "#e0b24f"][i % 3]}" transform="rotate({i * 37 % 180} {x:.0f} {y:.0f})"/>'
    b += f'<line x1="{ox + 45}" y1="72" x2="{ox + 185}" y2="140" stroke="{CAFE}" stroke-width="6" stroke-linecap="round"/>'
    b += f'<path d="M{ox + 8},150 Q{ox + 20},118 {ox + 34},112 L{ox + 36},150z" fill="#3b2a1a"/>'
    b += f'<rect x="{ox - 5}" y="150" width="200" height="6" fill="#c9b08a"/>'
    b += txt(ox + 95, 185, "Refugio de hojarasca", 16, CAFE, weight=700) + txt(ox + 95, 203, "el más calentito", 11, GRIS, weight=400)
    return svg(660, 210, b)


def hojas():
    formas = []
    # simple borde liso
    formas.append(("Simple, borde liso", f'<path d="M50,15 C80,35 80,85 50,110 C20,85 20,35 50,15z" fill="{VERDE2}"/><line x1="50" y1="20" x2="50" y2="130" stroke="{VERDE}" stroke-width="3"/>'))
    # dentada
    d = "M50,15 "
    pts_r = [(58, 22), (62, 26), (68, 34), (70, 40), (75, 50), (74, 56), (76, 66), (72, 72), (70, 82), (64, 88), (60, 98), (54, 102)]
    for i in range(0, len(pts_r), 2):
        d += f"L{pts_r[i][0]},{pts_r[i][1]} L{pts_r[i + 1][0]},{pts_r[i + 1][1]} "
    d += "L50,110 "
    for i in range(len(pts_r) - 1, -1, -2):
        d += f"L{100 - pts_r[i][0]},{pts_r[i][1]} L{100 - pts_r[i - 1][0]},{pts_r[i - 1][1]} "
    d += "z"
    formas.append(("Simple, borde dentado", f'<path d="{d}" fill="{VERDE2}"/><line x1="50" y1="20" x2="50" y2="130" stroke="{VERDE}" stroke-width="3"/>'))
    # lobulada (roble)
    formas.append(("Lobulada", f'<path d="M50,12 C62,14 60,28 68,28 C80,26 82,40 72,46 C84,50 86,64 72,66 C82,74 76,90 62,86 C62,98 56,106 50,110 C44,106 38,98 38,86 C24,90 18,74 28,66 C14,64 16,50 28,46 C18,40 20,26 32,28 C40,28 38,14 50,12z" fill="{VERDE2}"/><line x1="50" y1="20" x2="50" y2="130" stroke="{VERDE}" stroke-width="3"/>'))
    # compuesta
    comp = f'<line x1="50" y1="10" x2="50" y2="130" stroke="{VERDE}" stroke-width="3"/>'
    for y in [30, 55, 80]:
        comp += f'<ellipse cx="32" cy="{y}" rx="16" ry="7" fill="{VERDE2}" transform="rotate(-20 32 {y})"/><ellipse cx="68" cy="{y}" rx="16" ry="7" fill="{VERDE2}" transform="rotate(20 68 {y})"/>'
    comp += f'<ellipse cx="50" cy="12" rx="7" ry="14" fill="{VERDE2}"/>'
    formas.append(("Compuesta", comp))
    # palmeada
    palm = ""
    for a in [-60, -30, 0, 30, 60]:
        palm += f'<ellipse cx="50" cy="45" rx="9" ry="32" fill="{VERDE2}" transform="rotate({a} 50 80)"/>'
    palm += f'<line x1="50" y1="80" x2="50" y2="130" stroke="{VERDE}" stroke-width="3"/>'
    formas.append(("Palmeada", palm))
    # aguja
    ag = f'<line x1="50" y1="130" x2="50" y2="100" stroke="{CAFE}" stroke-width="3"/>'
    for a in [-25, -12, 0, 12, 25]:
        ag += f'<line x1="50" y1="100" x2="{50 + a * 1.2}" y2="15" stroke="{VERDE}" stroke-width="3" stroke-linecap="round"/>'
    formas.append(("Aguja (pinos)", ag))
    b = ""
    for i, (t, f) in enumerate(formas):
        x = i * 110
        b += f'<g transform="translate({x + 5},0)">{f}</g>'
        b += txt(x + 55, 152, t, 10.5, TINTA, weight=600)
    return svg(660, 160, b)


def huella(tipo):
    """Huellas simplificadas, dibujadas en una caja de 120x150."""
    c = "#4a3a2a"
    if tipo == "perro":
        b = f'<path d="M60,80 C85,80 90,110 78,120 C70,128 50,128 42,120 C30,110 35,80 60,80z" fill="{c}"/>'
        for (x, y) in [(38, 62), (52, 42), (70, 42), (84, 62)]:
            b += f'<ellipse cx="{x}" cy="{y}" rx="9" ry="12" fill="{c}"/><path d="M{x},{y - 13} l-2,-10 l4,0z" fill="{c}"/>'
    elif tipo == "gato":
        b = f'<path d="M40,90 C40,72 80,72 80,90 C88,96 86,118 76,120 C68,112 52,112 44,120 C34,118 32,96 40,90z" fill="{c}"/>'
        for (x, y) in [(34, 66), (50, 50), (70, 50), (86, 66)]:
            b += f'<ellipse cx="{x}" cy="{y}" rx="9" ry="11" fill="{c}"/>'
    elif tipo == "venado":
        b = f'<path d="M57,30 C40,40 36,90 44,118 C50,124 57,118 57,110z" fill="{c}"/><path d="M63,30 C80,40 84,90 76,118 C70,124 63,118 63,110z" fill="{c}"/>'
    elif tipo == "conejo":
        b = f'<ellipse cx="44" cy="45" rx="11" ry="26" fill="{c}"/><ellipse cx="76" cy="45" rx="11" ry="26" fill="{c}"/>'
        b += f'<ellipse cx="60" cy="98" rx="8" ry="10" fill="{c}"/><ellipse cx="60" cy="128" rx="8" ry="10" fill="{c}"/>'
    elif tipo == "ave":
        b = f'<g stroke="{c}" stroke-width="6" stroke-linecap="round" fill="none"><line x1="60" y1="110" x2="60" y2="130"/><line x1="60" y1="110" x2="60" y2="35"/><line x1="60" y1="110" x2="28" y2="50"/><line x1="60" y1="110" x2="92" y2="50"/></g>'
    else:  # mapache
        b = f'<path d="M40,80 C40,70 80,70 80,80 L78,118 C70,126 50,126 42,118z" fill="{c}"/>'
        for (x, y, r) in [(28, 60, -30), (42, 44, -12), (60, 38, 0), (78, 44, 12), (92, 60, 30)]:
            b += f'<ellipse cx="{x}" cy="{y}" rx="6" ry="16" fill="{c}" transform="rotate({r} {x} {y})"/>'
    return svg(120, 150, b)


def nubes_tipos():
    b = f'<rect width="640" height="300" rx="16" fill="#eaf5fb"/>'
    b += f'<line x1="0" y1="270" x2="640" y2="270" stroke="{VERDE2}" stroke-width="30"/>'
    # cirros
    for i in range(3):
        b += f'<path d="M{30 + i * 40},{40 + i * 8} q40,-20 90,-6" stroke="#9fb6c6" stroke-width="4" fill="none" stroke-linecap="round"/>'
    b += txt(95, 90, "Cirros", 15, AZUL, weight=700) + txt(95, 106, "plumas muy altas:", 11, GRIS, weight=400) + txt(95, 120, "el tiempo puede cambiar", 11, GRIS, weight=400)
    # cúmulos
    b += nube(215, 150, 1.1, "#fff", "#b8cfdd")
    b += txt(245, 205, "Cúmulos", 15, AZUL, weight=700) + txt(245, 221, "algodones: buen tiempo", 11, GRIS, weight=400)
    # estratos
    b += f'<rect x="345" y="175" width="120" height="26" rx="13" fill="#c9d3da"/>'
    b += f'<rect x="355" y="160" width="95" height="22" rx="11" fill="#d6dee4"/>'
    b += txt(405, 225, "Estratos", 15, AZUL, weight=700) + txt(405, 241, "manta gris: llovizna", 11, GRIS, weight=400)
    # cumulonimbos
    b += f'<path d="M500,240 C490,200 505,150 520,120 C525,90 530,70 525,50 L600,45 C595,70 600,100 605,120 C625,160 630,210 615,240z" fill="#7b8a97"/>'
    b += f'<path d="M500,50 L630,40 L612,58 L515,62z" fill="#8d9ba7"/>'
    b += f'<polygon points="560,240 548,262 558,262 548,285 572,255 562,255 570,240" fill="{AMARILLO}"/>'
    b += txt(560, 20, "Cumulonimbos: ¡tormenta!", 14, ROJO, weight=700)
    return svg(640, 300, b)


def senales_suelo():
    b = f'<rect width="560" height="170" rx="14" fill="#e9dfc9"/>'
    b += f'<g stroke="{ROJO}" stroke-width="14" stroke-linecap="round"><line x1="50" y1="40" x2="90" y2="120"/><line x1="130" y1="40" x2="90" y2="120"/></g>'
    b += txt(90, 150, "V = necesito ayuda", 13, TINTA)
    b += f'<g stroke="{ROJO}" stroke-width="14" stroke-linecap="round"><line x1="220" y1="40" x2="300" y2="120"/><line x1="300" y1="40" x2="220" y2="120"/></g>'
    b += txt(260, 150, "X = necesito médico", 13, TINTA)
    b += f'<g stroke="{ROJO}" stroke-width="14" stroke-linecap="round"><line x1="380" y1="80" x2="510" y2="80"/><line x1="510" y1="80" x2="480" y2="50"/><line x1="510" y1="80" x2="480" y2="110"/></g>'
    b += txt(445, 150, "→ = me fui por aquí", 13, TINTA)
    return svg(560, 170, b)


def espejo_senal():
    b = flecha_def("fe", AMARILLO)
    b += sol(40, 40, 18)
    b += f'<line x1="60" y1="55" x2="170" y2="130" stroke="{AMARILLO}" stroke-width="4" marker-end="url(#fe)"/>'
    b += f'<rect x="165" y="115" width="40" height="50" rx="4" fill="#cfe3ef" stroke="{AZUL}" stroke-width="3" transform="rotate(-20 185 140)"/>'
    b += f'<line x1="200" y1="125" x2="330" y2="40" stroke="{AMARILLO}" stroke-width="4" marker-end="url(#fe)"/>'
    b += f'<path d="M330,40 l30,-8 l6,10 l-30,8z" fill="{GRIS}"/><path d="M345,30 l20,-6 l-4,-6 z" fill="{GRIS}"/>'
    b += f'<line x1="185" y1="140" x2="185" y2="170" stroke="{GRIS}" stroke-dasharray="4 3"/>'
    b += txt(90, 115, "luz del sol", 12, GRIS, weight=400) + txt(300, 95, "reflejo", 12, GRIS, weight=400)
    return svg(380, 180, b)


def camino_bosque_deco(w=660):
    b = ""
    import random
    random.seed(3)
    x = 10
    while x < w:
        h = random.randint(35, 60)
        b += pino(x, 70, h, random.choice([VERDE, VERDE2, VERDE3]))
        x += random.randint(28, 50)
    return svg(w, 75, b)


def lupa():
    return svg(120, 120, f'<circle cx="50" cy="50" r="32" fill="#dff1ff" stroke="{TINTA}" stroke-width="8"/><line x1="74" y1="74" x2="110" y2="110" stroke="{CAFE}" stroke-width="14" stroke-linecap="round"/>')


def brujula_icono(s=140):
    b = f'<circle cx="70" cy="70" r="62" fill="#fff" stroke="{TINTA}" stroke-width="6"/>'
    b += f'<polygon points="70,20 82,70 58,70" fill="{ROJO}"/><polygon points="70,120 82,70 58,70" fill="#9aa3a0"/>'
    b += f'<circle cx="70" cy="70" r="6" fill="{TINTA}"/>' + txt(70, 18, "N", 14, ROJO, weight=700)
    return svg(140, 140, b, f'style="width:{s}px;height:{s}px"')


def para_colorear(svg_txt):
    """Convierte una ilustración a color en dibujo de líneas para colorear."""
    import re
    out = re.sub(r'<rect width="816" height="620" fill="url\(#cielo\)"/>', '<rect width="816" height="620" fill="#fff"/>', svg_txt)
    out = re.sub(r'<defs>.*?</defs>', '', out)
    out = re.sub(r'stroke="#[0-9a-fA-F]{3,6}"', 'stroke="#26302a"', out)
    out = re.sub(r'fill="#[0-9a-fA-F]{3,6}"', 'fill="#fff" stroke="#26302a" stroke-width="2.5"', out)
    out = out.replace('<rect width="816" height="620" fill="#fff" stroke="#26302a" stroke-width="2.5"/>', '')
    out = out.replace('preserveAspectRatio="xMidYMax slice" style="display:block;width:100%;height:100%"', 'style="display:block;width:100%;height:auto"')
    return out
