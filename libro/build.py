"""Genera libro.html (listo para imprimir en tamaño Carta). Ejecuta: python3 build.py"""
import ilustraciones as I
import pasatiempos as P

paginas = []


def pagina(html, clase="", folio=True):
    n = len(paginas) + 1
    f = f'<div class="folio"><span>{n}</span></div>' if folio else ""
    paginas.append(f'<section class="page {clase}">{html}{f}</section>')


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


def apertura(num, titulo, sub, color, ilus, aprenderas, dato):
    items = "".join(f"<li>{a}</li>" for a in aprenderas)
    html = f'''
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
    </div>'''
    pagina(html, f"opener {color}")


def experimento(titulo, color, tiempo, dificultad, materiales, pasos, ciencia_txt, pregunta, extra="", seg="", n_lineas=3, resultados=""):
    mats = "".join(f"<li>{m}</li>" for m in materiales)
    ps = "".join(f"<li>{p}</li>" for p in pasos)
    html = f'''
    {chip("Experimento")}
    <div class="exp-head"><div class="exp-badge">¡A<br>probar!</div><h2 style="margin:0">{titulo}</h2></div>
    <div class="meta"><span>⏱️ {tiempo}</span><span>⭐ Dificultad: {dificultad}</span><span>👨‍👩‍👧 Con un adulto</span></div>
    {f'<div class="cols" style="grid-template-columns:1.1fr 1fr;align-items:center"><div class="materiales"><h4>Materiales</h4><ul style="columns:1">{mats}</ul></div>{extra}</div>' if extra else f'<div class="materiales"><h4>Materiales</h4><ul>{mats}</ul></div>'}
    <h3 style="margin-top:0.14in">Pasos</h3>
    <ol class="pasos">{ps}</ol>
    {seg}
    {ciencia(ciencia_txt)}
    <h4>{pregunta}</h4>
    {resultados}
    {lineas(n_lineas)}'''
    pagina(html, color)


# ─────────────────────────── PORTADA ───────────────────────────
pagina(f'''
<div style="position:absolute;inset:0;background:linear-gradient(#bfe3f5,#e4f3fa)"></div><div style="position:absolute;left:0;right:0;bottom:0">{I.portada_escena()}</div>
<div style="position:absolute;top:0.7in;left:0.6in;right:0.6in;text-align:center">
  <div style="display:inline-block;background:#fff;color:#2f6b3a;font-family:Fredoka;font-weight:600;border-radius:30px;padding:6px 20px;font-size:12pt;letter-spacing:.06em">SERIE PEQUEÑOS EXPLORADORES · LIBRO 1</div>
  <h1 style="font-size:52pt;color:#1f4d29;margin:0.2in 0 0.05in;text-shadow:0 3px 0 #fff">¡Sobrevive en<br>el Bosque!</h1>
  <div style="font-family:Fredoka;font-weight:600;font-size:19pt;color:#e0702a;background:rgba(255,255,255,.85);display:inline-block;padding:4px 18px;border-radius:12px">Ciencia y supervivencia en la naturaleza</div>
  <div style="margin-top:0.18in"><div style="display:inline-block;background:#fff;border-radius:16px;padding:8px 20px;font-family:Fredoka;font-size:12.5pt;color:#26302a">🧭 Orientación · 💧 Agua · 🔥 Fuego · ⛺ Refugio · 🪢 Nudos · 🌿 Plantas · ☁️ Señales</div></div>
  <div style="margin-top:0.12in;font-family:Fredoka;font-weight:600;color:#26302a;font-size:11pt">LIBRO DE ACTIVIDADES · 8 A 12 AÑOS</div>
</div>
''', "", folio=False)

# ─────────────────────────── PROPIEDAD ───────────────────────────
pagina(f'''
<div class="center" style="margin-top:0.3in">{I.brujula_icono(130)}</div>
<h1 class="center" style="margin-top:0.2in">Este libro pertenece a</h1>
<div style="border-bottom:3px dashed var(--linea);height:0.6in;margin:0 0.6in 0.4in"></div>
<h2 class="center" style="color:var(--naranja)">Mi ficha de explorador</h2>
<div class="cols" style="margin-top:0.2in">
  <div class="marco" style="height:2.6in;display:flex;align-items:center;justify-content:center;color:var(--gris);text-align:center;padding:0.2in">Dibújate aquí con tu equipo de explorador</div>
  <div>
    <p><strong>Nombre de explorador:</strong></p>{lineas(1)}
    <p><strong>Edad:</strong></p>{lineas(1)}
    <p><strong>Mi animal favorito del bosque:</strong></p>{lineas(1)}
    <p><strong>Mi compañero/a de aventuras:</strong></p>{lineas(1)}
  </div>
</div>
<div class="box reto" style="margin-top:0.35in">
  <h4>🏅 Mi promesa de explorador</h4>
  <p class="mano" style="font-size:15pt;line-height:1.5">Prometo explorar con curiosidad, cuidar la naturaleza, no dejar basura, respetar a los animales y las plantas, y hacer los experimentos siempre con un adulto.</p>
  <p style="margin-top:0.25in">Firma: ______________________________</p>
</div>
''')

# ─────────────────────────── ÍNDICE (se rellena al final) ───────────────────────────
INDICE_POS = len(paginas)
pagina("__INDICE__")

# ─────────────────────────── CÓMO USAR ───────────────────────────
pagina(f'''
{chip("Antes de empezar")}
<h2>Cómo usar este libro</h2>
<p>¡Hola, explorador o exploradora! Este libro es tu manual para entender <strong>cómo funciona la naturaleza</strong> y cómo usar ese conocimiento para <strong>cuidarte en el bosque</strong>. Los exploradores de verdad no dependen de la suerte: dependen de la <strong>ciencia</strong>.</p>
<p>Cada capítulo tiene explicaciones, experimentos para hacer en casa o en el parque, y actividades para poner a prueba lo que aprendiste. Busca estas señales:</p>
<table style="margin:0.15in 0 0.2in">
<tr><th style="width:1.6in">Señal</th><th>Qué significa</th></tr>
<tr><td>🔬 <strong>La ciencia detrás</strong></td><td>Te explica <em>por qué</em> funciona lo que haces. ¡Es lo más importante!</td></tr>
<tr><td>🧪 <strong>Experimento</strong></td><td>Una prueba práctica con materiales sencillos. Anota lo que observes.</td></tr>
<tr><td>⚠️ <strong>Seguridad</strong></td><td>Reglas que <strong>siempre</strong> debes cumplir. Aquí no hay excepciones.</td></tr>
<tr><td>💡 <strong>¿Sabías que…?</strong></td><td>Datos curiosos para sorprender a tu familia.</td></tr>
<tr><td>🤔 <strong>¿Mito o realidad?</strong></td><td>Cosas que mucha gente cree… y que la ciencia pone a prueba.</td></tr>
<tr><td>🏅 <strong>Reto de explorador</strong></td><td>Un desafío para practicar. ¡Marca cada reto cuando lo completes!</td></tr>
</table>
{caja("sabias", "👨‍👩‍👧 Nota para madres, padres y docentes", "<p>Este libro está pensado para leerse y practicarse <strong>en familia</strong>. Las técnicas se enseñan para comprender la ciencia y para actuar con calma ante una emergencia, no para que los niños salgan solos al bosque. Todas las actividades con fuego, herramientas cortantes o agua natural requieren supervisión adulta. Las soluciones de los pasatiempos están al final del libro.</p>")}
<div class="fig" style="margin-top:0.25in">{I.camino_bosque_deco()}</div>
''', "c-verde")

# ─────────────────────────── SEGURIDAD ───────────────────────────
pagina(f'''
{chip("Lo más importante")}
<h2>Las 8 reglas de oro del explorador</h2>
<p>Antes de aprender a encender un fuego o construir un refugio, aprende estas reglas. Un buen explorador es, sobre todo, un explorador <strong>prudente</strong>.</p>
<ol class="pasos" style="--c:var(--rojo);font-size:12pt">
<li><strong>Nunca vayas solo.</strong> Explora siempre con un adulto de confianza.</li>
<li><strong>Avisa a dónde vas.</strong> Alguien en casa debe saber tu ruta y a qué hora vuelves.</li>
<li><strong>Si te pierdes, quédate quieto.</strong> Abraza un árbol, silba y espera. Es más fácil encontrar a alguien que no se mueve.</li>
<li><strong>No comas nada silvestre</strong> (plantas, frutos, hongos) a menos que un adulto experto lo identifique con total seguridad. Muchas plantas venenosas se parecen a las comestibles.</li>
<li><strong>No bebas agua sin desinfectar.</strong> Aunque se vea limpia, puede tener microbios invisibles. Siempre hay que hervirla.</li>
<li><strong>El fuego y las navajas son solo con un adulto.</strong> Siempre.</li>
<li><strong>Respeta a los animales.</strong> Obsérvalos de lejos, no los toques ni les des comida.</li>
<li><strong>No dejes rastro.</strong> Llévate tu basura, apaga el fuego por completo y deja el lugar mejor de como lo encontraste.</li>
</ol>
{seguridad("<p>Si alguna vez estás en una emergencia real, tu mejor herramienta es tu <strong>cabeza</strong>: mantén la calma, busca a un adulto y pide ayuda. En muchos países puedes llamar al <strong>911</strong> (o al número de emergencias de tu país) incluso desde un teléfono sin saldo.</p>", "⚠️ Recuerda")}
<p><strong>Número de emergencias de mi país:</strong> ____________ &nbsp; <strong>Teléfono de mi familia:</strong> ____________________</p>
''', "c-rojo")

# ─────────────────────────── REGLA DE 3 + STOP ───────────────────────────
tres = [("3 minutos", "sin aire", "🫁", "#dcecf7", "#2d7fb8"),
        ("3 horas", "sin refugio en clima extremo", "⛺", "#fde9d9", "#e0702a"),
        ("3 días", "sin agua", "💧", "#dcecf7", "#2d7fb8"),
        ("3 semanas", "sin comida", "🍎", "#e3f0dc", "#2f6b3a")]
celdas = "".join(f'<div style="background:{bg};border-radius:14px;padding:0.15in;text-align:center"><div style="font-size:30pt">{ic}</div><div style="font-family:Fredoka;font-weight:700;font-size:17pt;color:{c}">{t}</div><div class="small">{d}</div></div>' for t, d, ic, bg, c in tres)
stop = [("S", "Stop · Detente", "Para. Respira hondo. Siéntate si puedes. El miedo nos hace correr, y correr nos pierde más."),
        ("T", "Think · Piensa", "¿Qué pasó? ¿Dónde estuve la última vez que sabía dónde estaba? ¿Qué tengo en la mochila?"),
        ("O", "Observe · Observa", "Mira a tu alrededor: ¿hay caminos, agua, refugio? ¿Cómo está el clima? ¿Cuánta luz queda?"),
        ("P", "Plan · Planea", "Decide qué hacer primero: quedarte en un lugar visible, abrigarte y hacer señales.")]
filas = "".join(f'<div style="display:flex;gap:0.15in;align-items:flex-start;margin-bottom:0.1in"><div style="flex:none;width:0.55in;height:0.55in;border-radius:12px;background:var(--naranja);color:#fff;font-family:Fredoka;font-weight:700;font-size:24pt;display:flex;align-items:center;justify-content:center">{l}</div><div><strong style="font-family:Fredoka;font-size:13pt;color:var(--naranja)">{t}</strong><br>{d}</div></div>' for l, t, d in stop)
pagina(f'''
{chip("Lo más importante")}
<h2>La regla de los 3</h2>
<p>Los expertos en supervivencia usan esta regla para decidir <strong>qué es más urgente</strong>. Son números aproximados, pero te ayudan a pensar en orden:</p>
<div class="cols-4" style="margin:0.15in 0 0.1in">{celdas}</div>
<p class="small">Por eso, en el bosque, casi siempre lo primero es <strong>protegerte del frío, el calor o la lluvia</strong>; después, conseguir <strong>agua</strong>. La comida puede esperar mucho más de lo que crees.</p>
<h2 style="margin-top:0.25in">S.T.O.P.: tu plan si te pierdes</h2>
{filas}
{ciencia("<p>Cuando tenemos miedo, el cuerpo libera <strong>adrenalina</strong>: el corazón late rápido y queremos huir. Eso servía para escapar de un depredador, pero no para pensar con claridad. Respirar lento durante un minuto (inhala contando 4, exhala contando 6) le dice al cerebro que se calme y te ayuda a tomar mejores decisiones.</p>")}
''', "c-naranja")

# ═══════════════════════════ CAPÍTULO 1: ORIENTACIÓN ═══════════════════════════
apertura(1, "Orientación", "Aprende a encontrar el norte con el sol, las estrellas y una aguja.", "c-verde",
         f'<div style="margin:0 0.5in 0.35in 0">{I.brujula_icono(200)}</div>',
         ["Descubrir por qué el sol «camina» de este a oeste.", "Usar un palo y su sombra como brújula.",
          "Construir una brújula casera con una aguja.", "Encontrar el norte o el sur mirando las estrellas.",
          "Separar los mitos de la ciencia."],
         "<p>La Tierra es un <strong>imán gigante</strong>. En su núcleo hay hierro fundido en movimiento que crea un campo magnético. ¡Por eso la aguja de una brújula siempre apunta hacia el norte!</p>")

pagina(f'''
{chip("Capítulo 1 · Orientación")}
<h2>El sol: tu primera brújula</h2>
<p>Todos los días el sol sale por el <strong>Este</strong> y se oculta por el <strong>Oeste</strong>. En realidad el sol no se mueve: es la <strong>Tierra la que gira</strong> sobre sí misma, de oeste a este, como un trompo. Por eso vemos al sol «pasar» por el cielo.</p>
<p>A mediodía, el sol está en su punto más alto. Si vives al norte del ecuador (México, Centroamérica, el Caribe, España), a mediodía el sol queda hacia el <strong>sur</strong>. Si vives bien al sur del ecuador (Argentina, Chile, Uruguay, sur de Brasil), a mediodía el sol queda hacia el <strong>norte</strong>. Cerca del ecuador, a mediodía queda casi justo encima de tu cabeza.</p>
<h3>El método del palo y la sombra</h3>
<div class="fig">{I.palo_sombra()}</div>
<ol class="pasos">
<li>En un día soleado, clava un palo recto de aproximadamente un metro en un suelo plano.</li>
<li>Pon una piedrita justo en la punta de la sombra. Esa es tu <strong>1ª marca</strong> (el Oeste).</li>
<li>Espera de 15 a 20 minutos. La sombra se habrá movido. Pon otra piedrita en la nueva punta: tu <strong>2ª marca</strong> (el Este).</li>
<li>Traza una línea de la 1ª a la 2ª marca: va de <strong>Oeste a Este</strong>. Párate con la 1ª marca a tu izquierda y la 2ª a tu derecha: estarás mirando hacia el <strong>Norte</strong>.</li>
</ol>
{ciencia("<p>La sombra siempre apunta al lado contrario del sol. Como el sol avanza hacia el oeste, la sombra se mueve hacia el <strong>este</strong>. ¡Este método funciona en cualquier parte del mundo!</p>")}
''', "c-verde")

pagina(f'''
{chip("Capítulo 1 · Orientación")}
<h2>El truco del reloj de agujas</h2>
<div style="display:flex;gap:0.25in;align-items:center">
<div style="flex:none">{I.reloj_metodo()}</div>
<div>
<p><strong>Hemisferio norte:</strong> apunta la aguja de las <strong>horas</strong> hacia el sol. La línea que queda justo en medio entre esa aguja y el número 12 apunta al <strong>Sur</strong>.</p>
<p><strong>Hemisferio sur:</strong> apunta el <strong>número 12</strong> hacia el sol. La línea en medio entre el 12 y la aguja de las horas apunta al <strong>Norte</strong>.</p>
<p class="small">Si en tu país se usa horario de verano, usa el 1 en lugar del 12. Es un método aproximado, ¡pero muy útil!</p>
</div></div>
<h2 style="margin-top:0.2in">Las estrellas de noche</h2>
<p>Los navegantes antiguos cruzaron océanos guiándose por las estrellas. Tú también puedes:</p>
<div class="fig">{I.estrellas()}</div>
<div class="cols">
<div><h4 style="color:var(--azul)">Hemisferio norte</h4><p class="small">Busca la <strong>Osa Mayor</strong>, que parece un cucharón. Toma las dos estrellas del borde del «cazo» y prolonga la línea unas <strong>5 veces</strong> su distancia: llegarás a la <strong>Estrella Polar</strong>, que casi no se mueve y marca el <strong>Norte</strong>.</p></div>
<div><h4 style="color:var(--azul)">Hemisferio sur</h4><p class="small">Busca la <strong>Cruz del Sur</strong>, cuatro estrellas brillantes en forma de cometa. Prolonga su brazo más largo unas <strong>4 veces y media</strong> hacia abajo y luego baja la vista al horizonte: ahí está el <strong>Sur</strong>.</p></div>
</div>
{mito("<p><strong>«El musgo siempre crece en el lado norte de los árboles».</strong> ¡Mito! El musgo crece donde hay <strong>humedad y sombra</strong>, y eso depende del bosque, de la pendiente y de los árboles vecinos. Puede crecer en cualquier lado. Nunca te orientes solo por el musgo.</p>")}
''', "c-verde")

experimento("Fabrica una brújula casera", "c-verde", "20 minutos", "fácil",
            ["1 aguja de coser", "1 imán (de nevera sirve)", "1 hoja de árbol o un corcho", "1 plato hondo con agua", "Cinta adhesiva (opcional)"],
            ["Con ayuda de un adulto, frota la aguja con el imán <strong>unas 50 veces</strong>, siempre en la <strong>misma dirección</strong> (del ojo a la punta) y separando el imán al final de cada pasada.",
             "Coloca la hoja o el corcho a flotar en el centro del plato con agua.",
             "Pon la aguja con cuidado encima de la hoja flotante.",
             "Observa: la hoja girará poco a poco hasta quedar quieta. ¡La aguja está señalando la línea <strong>norte-sur</strong>!",
             "Para saber qué punta es el norte, compara con el sol: recuerda que sale por el este."],
            "<p>El hierro de la aguja está formado por millones de pequeñísimos «imanes» llamados <strong>dominios magnéticos</strong>, cada uno apuntando hacia donde quiere. Al frotarla con el imán, muchos se alinean en la misma dirección y la aguja se convierte en un imán. Como el agua deja que la hoja gire casi sin rozamiento, la aguja se alinea con el campo magnético de la Tierra.</p>",
            "¿Qué pasó cuando giraste el plato? ¿La aguja volvió a apuntar al mismo lado?",
            seg=seguridad("<p>Las agujas pinchan. Manipúlala con cuidado y guárdala al terminar. Aleja la brújula de objetos de metal y de teléfonos: pueden desviarla.</p>"), n_lineas=2)

laberinto_abiertas, laberinto_camino = P.laberinto(13, 15, semilla=21)
pagina(f'''
{chip("Capítulo 1 · Actividades")}
<h2>¡Pon a prueba tu orientación!</h2>
<div class="cols" style="align-items:start">
<div>
<h3>1. Completa la rosa de los vientos</h3>
<p class="small">Escribe los puntos que faltan: E, S, O, NE, SE, SO y NO.</p>
<div class="fig">{I.rosa_vientos(vacia=True, size=270)}</div>
</div>
<div>
<h3>2. Escapa del bosque</h3>
<p class="small">Entra por arriba y encuentra el camino hasta la salida, abajo.</p>
<div class="fig">{P.laberinto_svg(13, 15, laberinto_abiertas, cel=22)}</div>
</div>
</div>
<h3>3. Responde</h3>
<p>a) Son las 5 de la tarde y ves el sol muy bajo en el cielo. ¿Hacia qué punto cardinal estás mirando?</p>{lineas(1)}
<p>b) Clavaste un palo; la 1ª marca de la sombra quedó a tu izquierda y la 2ª a tu derecha. ¿Hacia dónde miras?</p>{lineas(1)}
<p>c) ¿Por qué no es buena idea orientarse solo por el musgo?</p>{lineas(2)}
''', "c-verde")

# ═══════════════════════════ CAPÍTULO 2: AGUA ═══════════════════════════
apertura(2, "Agua", "El agua es vida. Aprende dónde encontrarla y cómo hacerla segura.", "c-azul",
         f'<div style="margin:0 0.4in 0.25in 0"><svg viewBox="0 0 200 240" width="200" height="240"><path d="M100,10 C140,80 180,120 180,160 C180,205 145,235 100,235 C55,235 20,205 20,160 C20,120 60,80 100,10z" fill="#8cc3e8" stroke="#fff" stroke-width="6"/><path d="M60,160 C60,185 75,200 95,205" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round"/></svg></div>',
         ["Entender el ciclo del agua.", "Aprender a leer las pistas del paisaje para encontrar agua.",
          "Construir un filtro con arena y carbón.", "Sacar agua de las hojas de una planta.",
          "Saber por qué hay que hervir el agua siempre."],
         "<p>Tu cuerpo es aproximadamente un <strong>60 % agua</strong>. Si pesas 30 kilos, ¡unos 18 kilos son agua! Por eso, sin beber, el cuerpo empieza a fallar en pocos días.</p>")

pagina(f'''
{chip("Capítulo 2 · Agua")}
<h2>El gran viaje del agua</h2>
<p>El agua de la Tierra está siempre de viaje. El agua que bebes hoy pudo haber estado en un océano, en una nube o ¡en un dinosaurio! Este viaje sin fin se llama <strong>ciclo del agua</strong>:</p>
<div class="fig">{I.ciclo_agua()}</div>
<table class="small" style="margin-bottom:0.15in">
<tr><td><strong>1. Evaporación:</strong> el sol calienta el agua y la convierte en vapor invisible que sube.</td><td><strong>2. Condensación:</strong> arriba hace frío; el vapor se junta en gotitas y forma nubes.</td></tr>
<tr><td><strong>3. Precipitación:</strong> las gotas crecen, pesan y caen como lluvia, nieve o granizo.</td><td><strong>4. Escorrentía:</strong> el agua baja por el suelo hacia ríos, lagos y el mar… y todo vuelve a empezar.</td></tr>
</table>
<h3>Pistas para encontrar agua</h3>
<div class="cols small">
<ul>
<li><strong>Baja, no subas:</strong> el agua siempre corre hacia abajo. Busca en valles y quebradas.</li>
<li><strong>Busca verde intenso:</strong> plantas muy verdes y frondosas indican agua cerca.</li>
<li><strong>Escucha:</strong> en silencio puedes oír un arroyo desde lejos.</li>
</ul>
<ul>
<li><strong>Sigue a los animales:</strong> los senderos de animales que bajan suelen llevar al agua.</li>
<li><strong>Observa insectos:</strong> mosquitos y libélulas viven cerca del agua.</li>
<li><strong>El rocío:</strong> al amanecer, un paño pasado por la hierba mojada puede recoger agua.</li>
</ul>
</div>
{seguridad("<p>El agua de ríos, lagos o charcos puede tener <strong>bacterias y parásitos</strong> invisibles que causan enfermedades. Por muy transparente que se vea, un adulto debe <strong>hervirla</strong>: dejarla en ebullición fuerte al menos <strong>1 minuto</strong> (3 minutos si estás en lo alto de una montaña) y dejarla enfriar antes de beber.</p>")}
''', "c-azul")

FILTRO_SVG = I.filtro_agua().replace('width="470" height="440"', 'width="290" height="272"')
experimento("Construye un filtro de agua", "c-azul", "40 minutos", "media",
            ["1 botella de plástico grande", "Algodón o un trozo de tela limpia", "Carbón vegetal triturado", "Arena fina", "Arena gruesa", "Piedritas (grava)", "Agua con tierra y hojitas", "Un vaso transparente"],
            ["Con ayuda de un adulto, corta la base de la botella y colócala <strong>boca abajo</strong> sobre el vaso.",
             "Pon las capas en este orden, desde el pico: algodón, carbón, arena fina, arena gruesa y grava (mira el dibujo).",
             "Echa despacio el agua sucia por arriba y observa cómo baja por las capas.",
             "Compara el agua que sale con el agua sucia que tenías al principio."],
            "<p>Cada capa es un colador más fino que el anterior: la grava atrapa hojas y trozos grandes; la arena, partículas pequeñas; y el carbón tiene poros diminutos donde se pegan sustancias que dan mal olor y sabor (<strong>adsorción</strong>). Pero los microbios son tan pequeños que <strong>pasan por el filtro</strong>. Por eso el agua filtrada todavía hay que hervirla.</p>",
            "¿De qué color salió el agua? ¿Qué capa trabajó más?",
            extra=f'<div class="fig" style="margin:0">{FILTRO_SVG}</div>',
            seg=seguridad("<p><strong>No bebas el agua de este experimento.</strong> Se ve más limpia, pero no es segura.</p>"), n_lineas=1)

pagina(f'''
{chip("Capítulo 2 · Experimento")}
<div class="exp-head"><div class="exp-badge">¡A<br>probar!</div><h2 style="margin:0">Las plantas «sudan» agua</h2></div>
<div class="meta"><span>⏱️ 3 a 4 horas al sol</span><span>⭐ Dificultad: fácil</span><span>👨‍👩‍👧 Con un adulto</span></div>
<div class="cols" style="align-items:center;margin-bottom:-0.1in">
<div class="materiales"><h4>Materiales</h4><ul style="columns:1"><li>1 bolsa de plástico transparente</li><li>1 cordel o liga</li><li>1 árbol o arbusto con muchas hojas, a pleno sol</li><li>1 piedrita</li></ul></div>
<div class="fig">{I.bolsa_transpiracion()}</div>
</div>
<ol class="pasos">
<li>Mete la piedrita en la bolsa, para que haga peso en una esquina.</li>
<li>Cubre con la bolsa una rama con muchas hojas <strong>sin arrancarla</strong>.</li>
<li>Cierra bien la bolsa alrededor de la rama con el cordel.</li>
<li>Déjala al sol 3 o 4 horas y vuelve a mirar. ¡Habrá gotitas y un poquito de agua en la esquina!</li>
<li>Retira la bolsa con cuidado para no dañar la planta.</li>
</ol>
{ciencia("<p>Las plantas toman agua por sus raíces y la sueltan por agujeritos microscópicos de sus hojas llamados <strong>estomas</strong>: es la <strong>transpiración</strong>. El vapor queda atrapado en la bolsa, choca con el plástico más fresco y se <strong>condensa</strong> en gotas, como en las nubes. ¡Un árbol grande puede soltar cientos de litros de agua al día!</p>")}
{sabias("<p>Con la misma idea funciona el <strong>alambique solar</strong>: un hoyo cubierto con plástico. El sol evapora la humedad de la tierra, el vapor se condensa bajo el plástico y gotea en un recipiente.</p>")}
<h4>Mide: ¿cuántas cucharadas de agua juntaste?</h4>
{lineas(1)}
''', "c-azul")

pagina(f'''
{chip("Capítulo 2 · Actividades")}
<h2>¡Pon a prueba tu sed de saber!</h2>
<h3>1. Ordena el ciclo del agua</h3>
<p>Numera del 1 al 4 en el orden correcto:</p>
<div class="cols-4 center" style="margin-bottom:0.2in">
<div class="marco" style="padding:0.12in">☐<br>Precipitación</div><div class="marco" style="padding:0.12in">☐<br>Evaporación</div>
<div class="marco" style="padding:0.12in">☐<br>Escorrentía</div><div class="marco" style="padding:0.12in">☐<br>Condensación</div>
</div>
<h3>2. ¿Verdadero o falso?</h3>
<table style="margin-bottom:0.2in">
<tr><td>a) Si el agua de un río se ve transparente, se puede beber sin problema.</td><td style="width:1.1in" class="center"><span class="vf">V</span> <span class="vf">F</span></td></tr>
<tr><td>b) Para buscar agua es mejor bajar hacia los valles que subir a una colina.</td><td class="center"><span class="vf">V</span> <span class="vf">F</span></td></tr>
<tr><td>c) Un filtro de arena y carbón elimina todos los microbios.</td><td class="center"><span class="vf">V</span> <span class="vf">F</span></td></tr>
<tr><td>d) Las plantas sueltan agua por unos agujeritos llamados estomas.</td><td class="center"><span class="vf">V</span> <span class="vf">F</span></td></tr>
<tr><td>e) Hervir el agua al menos 1 minuto elimina los microbios peligrosos.</td><td class="center"><span class="vf">V</span> <span class="vf">F</span></td></tr>
<tr><td>f) Las libélulas y los mosquitos pueden ser una pista de que hay agua cerca.</td><td class="center"><span class="vf">V</span> <span class="vf">F</span></td></tr>
</table>
<h3>3. Dibuja el ciclo del agua de tu ciudad</h3>
<p class="small">¿De dónde viene el agua de tu grifo? ¿Adónde va cuando se va por el desagüe? Pregunta en casa y dibújalo.</p>
<div class="marco" style="height:3.2in"></div>
''', "c-azul")

# ═══════════════════════════ CAPÍTULO 3: FUEGO ═══════════════════════════
apertura(3, "Fuego", "El fuego da calor, luz y agua segura. Entiéndelo para respetarlo.", "c-naranja",
         f'<div style="margin:0 0.6in 0.3in 0"><svg viewBox="-60 -110 120 130" width="200" height="216">{I.fogata(0, 0, 1.0)}</svg></div>',
         ["Conocer el triángulo del fuego.", "Distinguir yesca, astillas y leña.",
          "Aprender dos formas de armar una fogata.", "Descubrir el papel del oxígeno con un experimento.",
          "Saber apagar un fuego por completo."],
         "<p>Los seres humanos usamos el fuego desde hace <strong>cientos de miles de años</strong>. Cocinar los alimentos nos dio más energía y, según muchos científicos, ¡ayudó a que nuestro cerebro creciera!</p>")

pagina(f'''
{chip("Capítulo 3 · Fuego")}
<h2>El triángulo del fuego</h2>
<div style="display:flex;gap:0.2in;align-items:center">
<div style="flex:none;width:3in">{I.triangulo_fuego().replace('width="360" height="310"', 'width="288" height="248"')}</div>
<div>
<p>El fuego es una <strong>reacción química</strong> llamada <strong>combustión</strong>. Para que exista necesita tres cosas a la vez:</p>
<ul>
<li><strong style="color:var(--rojo)">Calor</strong> para empezar (una chispa, un fósforo).</li>
<li><strong style="color:var(--cafe)">Combustible</strong>: algo que se queme (madera, hojas secas).</li>
<li><strong style="color:var(--azul)">Oxígeno</strong>: el gas del aire que respiramos.</li>
</ul>
<p>Si quitas <strong>uno solo</strong> de los tres lados, el fuego se apaga. Por eso el agua (quita calor) o la tierra (quita oxígeno) sirven para apagarlo.</p>
</div></div>
<h3>De pequeño a grande: el secreto de todo fuego</h3>
<p>Una llama pequeña no puede encender un tronco grueso. Hay que ir <strong>de lo más fino a lo más grueso</strong>:</p>
<div class="fig">{I.combustibles()}</div>
<div class="cols small">
<div><p><strong>Buena yesca natural:</strong> hierba muy seca, agujas de pino secas, corteza fina de algunos árboles, pelusa de plantas como la totora o el algodoncillo.</p></div>
<div><p><strong>Truco del explorador:</strong> una rama seca buena se quiebra con un <strong>«¡crac!»</strong>. Si se dobla sin romperse, está verde o húmeda y hará mucho humo.</p></div>
</div>
{ciencia("<p>Las cosas finas prenden antes porque tienen mucha <strong>superficie</strong> en contacto con el aire y se calientan rápido. Un tronco grueso reparte el calor en todo su volumen y tarda mucho en llegar a la temperatura necesaria para arder.</p>")}
''', "c-naranja")

pagina(f'''
{chip("Capítulo 3 · Fuego")}
<h2>Cómo arma una fogata un explorador</h2>
<div class="fig">{I.estructuras_fuego()}</div>
<h3>Las reglas de la fogata segura</h3>
<ol class="pasos" style="--c:var(--naranja)">
<li><strong>Un adulto enciende y cuida el fuego.</strong> Tú ayudas a juntar y ordenar los materiales.</li>
<li><strong>Revisa las normas del lugar:</strong> en muchos parques y en época seca está <strong>prohibido</strong> hacer fuego.</li>
<li><strong>Limpia un círculo</strong> de unos 3 metros sin hojas ni ramas secas, lejos de árboles, raíces y de tu refugio.</li>
<li><strong>Rodea el fuego con piedras secas.</strong> Nunca uses piedras sacadas de un río: el agua que tienen dentro puede calentarse y hacerlas <strong>explotar</strong>.</li>
<li><strong>Ten agua o tierra cerca</strong> antes de encender.</li>
<li><strong>Nunca dejes el fuego solo</strong>, ni un minuto.</li>
</ol>
<div class="box seguridad"><h4>⚠️ Apaga el fuego: ¡ahoga, remueve, ahoga!</h4>
<p>Echa agua sobre las brasas, remueve las cenizas con un palo y vuelve a echar agua. Acerca el dorso de la mano (sin tocar): si todavía sientes calor, repite. Un fuego solo está apagado cuando las cenizas están <strong>frías</strong>.</p></div>
<div style="display:flex;gap:0.2in;align-items:center">
<div style="flex:none">{I.lupa()}</div>
{ciencia("<p>Una <strong>lupa</strong> es una lente que dobla los rayos del sol (esto se llama <strong>refracción</strong>) y los junta en un puntito llamado <strong>foco</strong>. Ahí se concentra tanta energía que puede encender yesca seca. Es un experimento de óptica fascinante, <strong>pero solo con un adulto</strong>: jamás apuntes una lupa al sol cerca de tus ojos, ni sobre la piel.</p>", "🔬 Ciencia: fuego con una lupa")}
</div>
''', "c-naranja")

experimento("¿El fuego respira?", "c-naranja", "10 minutos", "fácil",
            ["1 vela pequeña (tipo té)", "1 plato", "1 frasco de vidrio transparente", "Fósforos (¡solo el adulto!)", "Un reloj con segundero"],
            ["Pon la vela en el centro del plato, sobre una mesa lejos de cortinas y papeles.",
             "El adulto enciende la vela.",
             "Tapa la vela con el frasco boca abajo y empieza a contar los segundos.",
             "Anota cuánto tarda en apagarse la llama.",
             "Repite con un frasco más grande. ¿Qué crees que pasará?"],
            "<p>La vela necesita <strong>oxígeno</strong> para arder. Dentro del frasco hay una cantidad limitada de aire. Mientras la llama quema, el oxígeno se gasta y se produce otro gas, el <strong>dióxido de carbono</strong>. Cuando ya no queda suficiente oxígeno, la llama se apaga: ¡acabas de quitar un lado del triángulo del fuego! En un frasco más grande hay más aire, así que la vela dura más.</p>",
            "Anota tus resultados:",
            resultados='<table style="margin-top:0.06in"><tr><th>Frasco</th><th>Segundos hasta apagarse</th><th>¿Por qué crees que pasó?</th></tr><tr><td style="height:0.4in">Pequeño</td><td></td><td></td></tr><tr><td style="height:0.4in">Grande</td><td></td><td></td></tr></table>',
            seg=seguridad("<p>El fuego y el frasco caliente queman. <strong>Solo un adulto</strong> enciende la vela y retira el frasco, y siempre después de dejarlo enfriar. Ten el pelo recogido y no acerques la cara.</p>"),
            n_lineas=0)

clasificar = [("Tronco del grosor de tu brazo", "L"), ("Hierba muy seca", "Y"), ("Ramitas del grosor de un lápiz", "A"),
              ("Agujas de pino secas", "Y"), ("Rama del grosor de tu muñeca", "L"), ("Palitos finos que hacen «¡crac!»", "A")]
filas_c = "".join(f'<tr><td>{t}</td><td class="center">☐</td><td class="center">☐</td><td class="center">☐</td></tr>' for t, _ in clasificar)
pagina(f'''
{chip("Capítulo 3 · Actividades")}
<h2>¡Enciende tu mente!</h2>
<h3>1. Clasifica los materiales</h3>
<p>Marca con una ✔ si es yesca, astilla o leña:</p>
<table style="margin-bottom:0.2in"><tr><th>Material</th><th style="width:0.9in">Yesca</th><th style="width:0.9in">Astilla</th><th style="width:0.9in">Leña</th></tr>{filas_c}</table>
<h3>2. Completa el triángulo del fuego</h3>
<div style="display:flex;gap:0.3in;align-items:center">
<svg viewBox="0 0 300 250" width="260" height="217"><polygon points="150,20 280,230 20,230" fill="#fde9d9" stroke="#e0702a" stroke-width="6" stroke-linejoin="round"/><rect x="20" y="105" width="95" height="32" rx="6" fill="#fff" stroke="#8a938c" stroke-dasharray="4 3"/><rect x="185" y="105" width="95" height="32" rx="6" fill="#fff" stroke="#8a938c" stroke-dasharray="4 3"/><rect x="100" y="210" width="100" height="32" rx="6" fill="#fff" stroke="#8a938c" stroke-dasharray="4 3"/></svg>
<div><p>¿Qué lado del triángulo quitas en cada caso?</p>
<p>a) Echas agua a una fogata: ____________________</p>
<p>b) Tapas una vela con un frasco: ______________</p>
<p>c) Ya no queda madera que quemar: ___________</p></div>
</div>
<h3 style="margin-top:0.15in">3. Detective de riesgos</h3>
<p>Tomás quiere hacer una fogata bajo un árbol, sobre hojas secas, rodeada de piedras del río y sin agua cerca. Escribe <strong>todos los errores</strong> que encuentres:</p>
{lineas(4)}
''', "c-naranja")

# ═══════════════════════════ CAPÍTULO 4: REFUGIO ═══════════════════════════
apertura(4, "Refugio", "Tu casa en el bosque: la ciencia de no pasar frío.", "c-cafe",
         f'<div style="margin:0 0.3in 0.1in 0"><svg viewBox="-80 -120 160 125" width="260" height="203">{I.tienda(0, 0, 1.0, "#e0b24f")}</svg></div>',
         ["Descubrir las 4 formas en que tu cuerpo pierde calor.", "Elegir un buen lugar para un refugio.",
          "Conocer tres tipos de refugio hechos con ramas y hojas.", "Comprobar con un experimento qué materiales abrigan más."],
         "<p>El suelo frío le quita calor a tu cuerpo mucho más rápido que el aire. Por eso, en un refugio, <strong>lo que pones debajo de ti</strong> es tan importante como el techo.</p>")

pagina(f'''
{chip("Capítulo 4 · Refugio")}
<h2>¿Por qué pasamos frío?</h2>
<p>Tu cuerpo es como una estufa que produce calor todo el tiempo (unos 37 °C por dentro). El calor siempre viaja de lo <strong>caliente a lo frío</strong>, así que tu cuerpo lo pierde de cuatro maneras:</p>
<div class="fig">{I.perdida_calor()}</div>
<table class="small" style="margin-bottom:0.15in">
<tr><th>Cómo se pierde</th><th>Cómo lo evita un explorador</th></tr>
<tr><td><strong>Conducción</strong>: tocando algo frío, como el suelo o una roca.</td><td>Hace una «cama» gruesa de hojas secas o ramas de pino para no tocar el suelo.</td></tr>
<tr><td><strong>Convección</strong>: el viento arrastra el aire tibio que rodea tu piel.</td><td>Busca un lugar protegido del viento y cierra bien el refugio.</td></tr>
<tr><td><strong>Radiación</strong>: tu cuerpo emite calor al aire, sobre todo por la cabeza si está descubierta.</td><td>Usa gorro y construye un refugio pequeño que guarde el calor.</td></tr>
<tr><td><strong>Evaporación</strong>: el sudor y la ropa mojada se secan robándote calor.</td><td>Se mantiene seco, no suda de más y se quita la ropa mojada.</td></tr>
</table>
<h3>¿Dónde construir? Elige bien el lugar</h3>
<div class="cols small">
<div><p><strong style="color:var(--verde)">✔ Sí:</strong></p><ul><li>Terreno plano y un poco elevado, para que no se inunde.</li><li>Protegido del viento (detrás de rocas o arbustos).</li><li>Cerca de materiales: ramas y hojas secas.</li><li>Visible, para que te puedan encontrar.</li></ul></div>
<div><p><strong style="color:var(--rojo)">✘ No:</strong></p><ul><li>En el cauce seco de un río: puede llegar una crecida.</li><li>Bajo ramas secas o árboles muertos que puedan caer.</li><li>Bajo un árbol solitario si hay tormenta eléctrica.</li><li>Pegado al agua: hace más frío y hay más mosquitos.</li></ul></div>
</div>
''', "c-cafe")

pagina(f'''
{chip("Capítulo 4 · Refugio")}
<h2>Tres refugios de la naturaleza</h2>
<div class="fig">{I.refugios()}</div>
<div class="cols-3 small">
<div><h4 style="color:var(--cafe)">Cobertizo</h4><p>Apoya una rama larga y fuerte entre dos árboles o dos troncos con horquilla. Inclina muchas ramas contra ella, del lado de donde viene el viento, y cúbrelas con hojas y ramas con follaje, de abajo hacia arriba, como las tejas de un techo.</p></div>
<div><h4 style="color:var(--cafe)">Tienda en A</h4><p>Igual que el cobertizo, pero con ramas en los <strong>dos lados</strong> de la viga, formando una letra A. Te protege mejor del viento y la lluvia que vienen de cualquier lado.</p></div>
<div><h4 style="color:var(--cafe)">Refugio de hojarasca</h4><p>Una viga apoyada en un tocón o una roca, costillas de ramas a los lados y una capa <strong>muy gruesa</strong> de hojas secas encima (¡tanta como el largo de tu brazo!). Por dentro, apenas más grande que tu cuerpo.</p></div>
</div>
{ciencia("<p>¿Por qué un refugio pequeño abriga más? Porque tu cuerpo es la única estufa. Cuanto <strong>menos aire</strong> haya que calentar, más rápido se calienta. Y las hojas secas abrigan porque atrapan millones de bolsitas de <strong>aire quieto</strong> entre ellas. El aire quieto es un mal conductor del calor: es un <strong>aislante</strong>. ¡Así funcionan también tu chaqueta de plumas y el pelaje de los animales!</p>")}
{reto("<p>Con un adulto, en un parque o en el jardín, construye un <strong>mini-refugio</strong> para un muñeco usando solo palitos y hojas. Échale un vaso de agua por encima como si fuera lluvia: ¿se mojó el muñeco? Mejora el techo hasta que quede seco.</p><p>☐ ¡Reto completado!</p>")}
{seguridad("<p>Practica siempre acompañado. Usa ramas que ya estén caídas en el suelo: nunca cortes árboles vivos. Revisa que no haya hormigueros, avispas ni espinas antes de empezar.</p>")}
''', "c-cafe")

experimento("¿Qué abriga más?", "c-cafe", "40 minutos", "fácil",
            ["3 frascos o botellas iguales", "Agua tibia del grifo (que no queme)", "Hojas secas y una bolsa", "1 calcetín grueso o un gorro", "1 termómetro (si tienes)", "Un reloj"],
            ["Llena los tres frascos con la <strong>misma cantidad</strong> de agua tibia y ciérralos.",
             "Frasco A: déjalo sin nada. Frasco B: métele en el calcetín o el gorro. Frasco C: rodéalo con una capa gruesa de hojas secas dentro de la bolsa.",
             "Pon los tres en un lugar fresco, como el patio o cerca de una ventana abierta.",
             "Espera 30 minutos. Mide la temperatura del agua o tócala con el dedo.",
             "Ordena los frascos del más caliente al más frío."],
            "<p>El calor del agua quiere escapar hacia el aire frío. El frasco sin nada lo pierde rápido. El calcetín y las hojas atrapan <strong>aire quieto</strong> alrededor del frasco y frenan el paso del calor: son <strong>aislantes</strong>. Lo mismo hace una buena capa de hojas en tu refugio… ¡contigo dentro!</p>",
            "Anota tus resultados:",
            resultados='<table style="margin-top:0.06in"><tr><th>Frasco</th><th>Temperatura o sensación después de 30 min</th><th>Puesto</th></tr><tr><td style="height:0.36in">A · Sin nada</td><td></td><td></td></tr><tr><td style="height:0.36in">B · Calcetín</td><td></td><td></td></tr><tr><td style="height:0.36in">C · Hojas secas</td><td></td><td></td></tr></table>',
            n_lineas=0)

pagina(f'''
{chip("Capítulo 4 · Actividades")}
<h2>Diseña tu refugio ideal</h2>
<p>Eres el arquitecto del bosque. Dibuja tu refugio perfecto y señala con flechas: la viga principal, las ramas, la capa de hojas, la cama aislante, la entrada y de dónde viene el viento.</p>
<div class="marco" style="height:4.6in;position:relative"><div style="position:absolute;bottom:10px;right:14px;color:var(--gris);font-size:9pt">Viento → dibuja aquí su dirección</div></div>
<h3 style="margin-top:0.2in">Une cada forma de perder calor con su solución</h3>
<div class="cols" style="font-size:12pt">
<div><p>1. Conducción ●</p><p>2. Convección ●</p><p>3. Radiación ●</p><p>4. Evaporación ●</p></div>
<div><p>● a) Ponerse un gorro</p><p>● b) Quitarse la ropa mojada</p><p>● c) Hacer una cama de hojas secas</p><p>● d) Buscar un lugar sin viento</p></div>
</div>
''', "c-cafe")

# ═══════════════════════════ CAPÍTULO 5: CUERDAS Y NUDOS ═══════════════════════════
apertura(5, "Cuerdas y nudos", "Con fibras de plantas y unos buenos nudos, puedes construir casi cualquier cosa.", "c-morado",
         '<div style="margin:0 0.5in 0.4in 0"><svg viewBox="0 0 220 200" width="220" height="200"><path d="M20,180 C60,20 160,20 200,180" fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round"/><path d="M20,180 C60,20 160,20 200,180" fill="none" stroke="#c9a458" stroke-width="8" stroke-linecap="round" stroke-dasharray="10 8"/><circle cx="110" cy="62" r="26" fill="none" stroke="#fff" stroke-width="12"/></svg></div>',
         ["Fabricar una cuerda con fibras naturales.", "Entender por qué la fricción hace fuertes a las cuerdas.",
          "Aprender 4 nudos esenciales del explorador.", "Completar el reto de los nudos."],
         "<p>Los seres humanos fabricamos cuerdas desde hace más de <strong>40 000 años</strong>. ¡Se han encontrado restos de cuerdas hechas con fibras de árbol en cuevas de la prehistoria!</p>")

pagina(f'''
{chip("Capítulo 5 · Cuerdas")}
<h2>Haz una cuerda con plantas</h2>
<p>Muchas plantas tienen <strong>fibras</strong> largas y fuertes: las hojas de pita, maguey o fique, la corteza interior de algunos árboles, las hojas de palma y algunas hierbas largas. Con ellas puedes hacer una cuerda usando la técnica de la <strong>torsión inversa</strong>:</p>
<div class="fig"><svg viewBox="0 0 600 150" width="600" height="150">
<g transform="translate(20,20)"><path d="M0,40 L150,40" stroke="#c9a458" stroke-width="10" stroke-linecap="round"/><path d="M0,40 L0,40" /><text x="75" y="90" font-family="Fredoka" font-size="14" text-anchor="middle" fill="#6d4c9f" font-weight="600">1. Dobla el manojo</text><text x="75" y="108" font-family="Fredoka" font-size="11" text-anchor="middle" fill="#8a938c">por la mitad</text><path d="M150,40 C165,40 165,20 150,20 L10,20" stroke="#b08a3e" stroke-width="10" fill="none" stroke-linecap="round"/></g>
<g transform="translate(220,20)"><path d="M0,30 C20,10 30,50 50,30 C70,10 80,50 100,30 C120,10 130,50 150,30" stroke="#c9a458" stroke-width="10" fill="none"/><path d="M0,30 C20,50 30,10 50,30 C70,50 80,10 100,30 C120,50 130,10 150,30" stroke="#b08a3e" stroke-width="10" fill="none"/><text x="75" y="90" font-family="Fredoka" font-size="14" text-anchor="middle" fill="#6d4c9f" font-weight="600">2. Tuerce y cruza</text><text x="75" y="108" font-family="Fredoka" font-size="11" text-anchor="middle" fill="#8a938c">una y otra vez</text></g>
<g transform="translate(420,20)"><path d="M0,30 C10,15 20,45 30,30 C40,15 50,45 60,30 C70,15 80,45 90,30 C100,15 110,45 120,30 C130,15 140,45 150,30" stroke="#c9a458" stroke-width="12" fill="none"/><path d="M0,30 C10,45 20,15 30,30 C40,45 50,15 60,30 C70,45 80,15 90,30 C100,45 110,15 120,30 C130,45 140,15 150,30" stroke="#b08a3e" stroke-width="12" fill="none"/><text x="75" y="90" font-family="Fredoka" font-size="14" text-anchor="middle" fill="#6d4c9f" font-weight="600">3. ¡Cuerda firme!</text><text x="75" y="108" font-family="Fredoka" font-size="11" text-anchor="middle" fill="#8a938c">no se desenrolla</text></g>
</svg></div>
<ol class="pasos" style="--c:#6d4c9f">
<li>Junta un manojo de fibras y dóblalo por la mitad, pero no exactamente: deja un lado un poco más largo. Así las uniones quedarán en lugares distintos y la cuerda será más fuerte.</li>
<li>Sujeta el doblez con una mano. Con la otra, toma el mechón de <strong>arriba</strong> y <strong>tuércelo alejándolo de ti</strong>.</li>
<li>Ahora <strong>crúzalo hacia ti</strong> por encima del otro mechón, que queda arriba.</li>
<li>Repite: toma el de arriba, tuércelo alejándolo, crúzalo hacia ti. Cuando un mechón se acabe, añade fibras nuevas.</li>
</ol>
{ciencia("<p>Una sola fibra se rompe fácil. Pero al torcerlas, las fibras quieren desenrollarse… y como cada mechón se tuerce en sentido contrario al que se cruza, <strong>se bloquean entre sí</strong>. Además, se aprietan unas contra otras y aparece la <strong>fricción</strong> (el roce), que impide que se deslicen. La fuerza se reparte entre todas las fibras: ¡juntas son mucho más fuertes!</p>")}
{reto("<p>Haz una cuerda de 30 cm con hierba larga, hojas de palma, rafia o incluso con tiras de papel de periódico retorcido. ¿Puede levantar tu estuche? ☐ ¡Reto completado!</p>")}
''', "c-morado")

nudos = [
    ("Nudo de ocho", "Tope: evita que la cuerda se escape de un agujero o de tu mano.",
     ["Haz una gaza (un bucle) con la punta de la cuerda.", "Pasa la punta <strong>por detrás</strong> de la parte larga.", "Métela por el bucle desde el frente.", "Aprieta: debe verse como un número 8."]),
    ("Nudo llano", "Unir dos cuerdas del mismo grosor, atar un vendaje o un paquete.",
     ["Punta derecha <strong>sobre</strong> la izquierda y da una vuelta (como el primer paso de atarte los zapatos).", "Ahora punta izquierda <strong>sobre</strong> la derecha y otra vuelta.", "Aprieta. Si queda torcido, cambiaste el orden: ¡prueba otra vez!", "No lo uses para cargar peso importante."]),
    ("Ballestrinque", "Atar una cuerda a un palo o un árbol, por ejemplo para empezar a armar un refugio.",
     ["Da una vuelta alrededor del palo.", "Cruza la punta por encima de la primera vuelta y da una segunda vuelta.", "Mete la punta por debajo de esa segunda vuelta.", "Tira de los dos extremos: las vueltas se cruzan en forma de X."]),
    ("As de guía", "Hace un lazo fijo que no se cierra ni se aprieta: el rey de los nudos de rescate.",
     ["Haz un pequeño bucle en la cuerda: es el <strong>pozo</strong>. La punta es el <strong>conejo</strong> y la parte larga, el <strong>árbol</strong>.", "El conejo <strong>sale del pozo</strong> (pasa la punta por el bucle desde abajo).", "El conejo <strong>rodea el árbol</strong> por detrás.", "El conejo <strong>vuelve a entrar al pozo</strong>. Sujeta y aprieta."]),
]
bloques = ""
for t, uso, pasos_n in nudos:
    li = "".join(f"<li>{p}</li>" for p in pasos_n)
    bloques += f'<div class="marco" style="padding:0.12in 0.16in;border-style:solid;border-color:#d9cfe8"><h3 style="margin-bottom:0.04in">{t}</h3><p class="small" style="color:var(--gris)"><em>Para qué sirve:</em> {uso}</p><ol class="small" style="margin:0;padding-left:0.2in">{li}</ol><p class="small" style="margin:0.06in 0 0">☐ Lo hice solo &nbsp; ☐ Lo hice con los ojos cerrados</p></div>'
pagina(f'''
{chip("Capítulo 5 · Nudos")}
<h2>Los 4 nudos del explorador</h2>
<p>Busca un cordón o una cuerda de un metro y practica cada nudo. Cuando te salga, marca las casillas.</p>
<div class="cols" style="gap:0.18in">{bloques}</div>
{sabias("<p>Los marineros dicen que un buen nudo cumple tres reglas: es <strong>fácil de hacer</strong>, <strong>aguanta</strong> lo que necesitas y es <strong>fácil de deshacer</strong> después. ¡El as de guía cumple las tres, por eso lo usan los rescatistas!</p>")}
''', "c-morado")

# ═══════════════════════════ CAPÍTULO 6: PLANTAS Y ANIMALES ═══════════════════════════
apertura(6, "Plantas y animales", "Conviértete en detective de la naturaleza: hojas, huellas y secretos.", "c-verde",
         f'<div style="margin:0 0.4in 0.25in 0">{I.svg(220, 210, I.arbol(110, 205, 200, "#7cbf6a"))}</div>',
         ["Entender cómo fabrican su alimento las plantas.", "Identificar árboles por la forma de sus hojas.",
          "Reconocer plantas que pican o son peligrosas.", "Leer huellas de animales.", "Descubrir los colores escondidos de las hojas."],
         "<p>Casi todo el <strong>oxígeno</strong> que respiras lo produjeron plantas y algas. Un árbol grande puede producir en un año el oxígeno que necesitan varias personas.</p>")

pagina(f'''
{chip("Capítulo 6 · Plantas")}
<h2>Las hojas: fábricas de comida</h2>
<p>Las plantas no comen como nosotros: <strong>fabrican su propio alimento</strong> usando la luz del sol. Esto se llama <strong>fotosíntesis</strong>:</p>
<div class="box ciencia center" style="font-family:Fredoka;font-size:14pt;font-weight:600;color:var(--azul)">☀️ luz + 💧 agua + 🌬️ dióxido de carbono → 🍬 azúcar + 🫧 oxígeno</div>
<p>El responsable es un pigmento verde llamado <strong>clorofila</strong>, que atrapa la luz. ¡Por eso casi todas las hojas son verdes!</p>
<h3>Identifica árboles por sus hojas</h3>
<div class="fig">{I.hojas()}</div>
<p class="small">Fíjate en: ¿la hoja es <strong>una sola</strong> (simple) o está formada por <strong>varias hojitas</strong> (compuesta)? ¿El borde es liso, dentado o con lóbulos? ¿Las nervaduras son paralelas o se ramifican como una red?</p>
<div class="box seguridad"><h4>⚠️ La regla de oro de las plantas</h4>
<p><strong>Nunca comas ninguna planta, fruto, semilla ni hongo del bosque</strong> sin que un adulto experto la haya identificado con total seguridad. Muchas plantas comestibles tienen «gemelas» venenosas casi idénticas. Con los hongos, el peligro es todavía mayor: algunos pueden ser mortales.</p></div>
<h3>Plantas que debes reconocer… ¡para no tocarlas!</h3>
<div class="cols-3 small">
<div class="marco" style="padding:0.1in;border-style:solid"><strong>Ortiga</strong><br>Tiene pelitos que funcionan como agujas diminutas y te inyectan sustancias que pican y arden.</div>
<div class="marco" style="padding:0.1in;border-style:solid"><strong>Hiedra venenosa</strong><br>Hojas agrupadas de a <strong>tres</strong>. Dicho del explorador: «Hojas de tres, déjala como es».</div>
<div class="marco" style="padding:0.1in;border-style:solid"><strong>Manzanillo de playa</strong><br>Árbol de costas del Caribe y Centroamérica: su savia quema la piel. ¡No te refugies bajo él cuando llueve!</div>
</div>
''', "c-verde")

huellas = [("perro", "Perro, zorro, coyote", "4 dedos con marcas de uñas; forma ovalada."),
           ("gato", "Gato, puma, lince", "4 dedos, sin marcas de uñas (las esconden); forma redonda."),
           ("venado", "Venado, ciervo", "Pezuña partida en dos, como un corazón al revés."),
           ("conejo", "Conejo, liebre", "Las patas traseras largas quedan delante de las delanteras al saltar."),
           ("ave", "Aves", "Tres dedos hacia delante y uno hacia atrás."),
           ("mapache", "Mapache", "Cinco dedos largos, ¡parece una manita humana!")]
cel = "".join(f'<div class="center"><div style="background:#f3ecdf;border-radius:14px;padding:0.06in">{I.huella(k)}</div><h4 style="margin:0.06in 0 0.02in">{t}</h4><p class="tiny">{d}</p></div>' for k, t, d in huellas)
pagina(f'''
{chip("Capítulo 6 · Animales")}
<h2>Detective de huellas</h2>
<p>Los animales del bosque suelen esconderse de los humanos, pero dejan pistas: <strong>huellas</strong>, plumas, nidos, ramas mordidas y excrementos. Leer estas señales es un arte que se llama <strong>rastreo</strong>. Los mejores lugares para buscar huellas son el barro junto a ríos y charcos, la arena y la nieve.</p>
<div class="cols-3" style="gap:0.2in">{cel}</div>
{sabias("<p>Puedes «fotografiar» una huella con yeso: rodea la huella con un anillo de cartón, vierte yeso mezclado con agua (como una crema espesa), espera unos 30 minutos a que endurezca y levántalo con cuidado. ¡Tendrás un molde para tu colección!</p>")}
{seguridad("<p>Si encuentras huellas frescas de un animal grande, aléjate con calma por donde viniste y avisa a un adulto. Nunca sigas a un animal salvaje ni te acerques a sus crías.</p>")}
''', "c-verde")

experimento("Los colores escondidos de las hojas", "c-verde", "1 hora y media", "media",
            ["Hojas verdes de distintas plantas", "Alcohol de farmacia", "1 frasco pequeño por tipo de hoja", "Tiras de filtro de café", "1 cuchara", "1 lápiz y cinta adhesiva", "Tijeras"],
            ["Corta las hojas en trocitos muy pequeños y ponlas en el frasco.",
             "Un adulto añade alcohol hasta cubrirlas. Aplástalas con la cuchara hasta que el alcohol se ponga verde.",
             "Pega la tira de filtro al lápiz y apoya el lápiz sobre el frasco, de modo que <strong>solo la punta</strong> de la tira toque el líquido.",
             "Espera de 30 a 60 minutos y observa cómo sube el color por el papel.",
             "¿Ves bandas de distintos colores? Busca el verde, el amarillo y el naranja."],
            "<p>Esta técnica se llama <strong>cromatografía</strong>. El alcohol sube por el papel y arrastra los pigmentos de la hoja; cada pigmento viaja a distinta velocidad, así que se separan en bandas. Además del verde de la <strong>clorofila</strong>, aparecen pigmentos amarillos y naranjas (los <strong>carotenoides</strong>) que siempre estuvieron ahí, escondidos. En otoño, en los lugares donde los árboles pierden las hojas, la clorofila se deshace y esos colores ocultos por fin se ven.</p>",
            "¿Cuántos colores encontraste en cada hoja?",
            seg=seguridad("<p>El alcohol es inflamable y su olor es fuerte: úsalo con un adulto, en un lugar ventilado y <strong>lejos de cualquier llama</strong>.</p>"), n_lineas=2)

pagina(f'''
{chip("Capítulo 6 · Actividades")}
<h2>Mi diario de campo</h2>
<p>Los científicos de la naturaleza anotan todo lo que observan. Sal con tu familia a un parque o al bosque y completa esta ficha.</p>
<div class="cols" style="gap:0.2in">
<div><p><strong>Fecha:</strong> ___________________</p><p><strong>Lugar:</strong> ___________________</p>
<p><strong>Clima:</strong> ☀️ ☁️ 🌧️ 🌬️ (encierra uno)</p><p><strong>Temperatura:</strong> 🥶 fresco &nbsp; 🙂 templado &nbsp; 🥵 calor</p></div>
<div><p><strong>Animales o rastros que vi:</strong></p>{lineas(3)}</div>
</div>
<div class="cols" style="gap:0.2in;margin-top:0.1in">
<div><h4>Calco de corteza</h4><p class="tiny">Apoya el papel sobre un tronco y frota con un crayón acostado.</p><div class="marco" style="height:2.5in"></div></div>
<div><h4>Dibujo de una hoja</h4><p class="tiny">¿Es simple o compuesta? ¿Cómo es su borde?</p><div class="marco" style="height:2.5in"></div></div>
</div>
<h4 style="margin-top:0.18in">Lo más sorprendente que descubrí hoy fue…</h4>
{lineas(3)}
''', "c-verde")

# ═══════════════════════════ CAPÍTULO 7: CLIMA Y SEÑALES ═══════════════════════════
apertura(7, "Clima y señales", "Lee el cielo como un meteorólogo y aprende a pedir ayuda como un rescatista.", "c-azul",
         f'<div style="margin:0 0.3in 0.3in 0">{I.svg(260, 180, I.nube(40, 90, 2.2, "#ffffff") + I.sol(60, 50, 26))}</div>',
         ["Reconocer 4 tipos de nubes y lo que anuncian.", "Calcular a qué distancia está una tormenta.",
          "Aprender las señales internacionales de auxilio.", "Usar un espejo para enviar señales de luz.", "Descifrar mensajes en código Morse."],
         "<p>La luz viaja tan rápido que el relámpago lo ves casi al instante, pero el sonido del trueno avanza a unos <strong>340 metros por segundo</strong>. ¡Esa diferencia te dice a qué distancia está la tormenta!</p>")

pagina(f'''
{chip("Capítulo 7 · Clima")}
<h2>Leer el cielo</h2>
<p>Las nubes son gotitas de agua (o cristalitos de hielo) flotando en el aire. Su forma y su altura nos dan pistas sobre el tiempo que viene:</p>
<div class="fig">{I.nubes_tipos()}</div>
<h3>¿A qué distancia está la tormenta?</h3>
<div style="display:flex;gap:0.2in;align-items:flex-start">
<div class="box ciencia" style="flex:1;margin-top:0"><h4>🔬 Calcúlalo tú</h4>
<ol style="margin:0"><li>Cuando veas un relámpago, empieza a contar segundos: «uno mil, dos mil, tres mil…».</li>
<li>Para cuando oigas el trueno.</li>
<li><strong>Divide entre 3</strong> los segundos que contaste. El resultado son los <strong>kilómetros</strong> que te separan de la tormenta.</li></ol>
<p class="small" style="margin-top:0.06in">Ejemplo: 9 segundos ÷ 3 = 3 km.</p></div>
<div class="marco" style="flex:none;width:2.3in;padding:0.12in;border-style:solid" ><h4>¡Practica!</h4>
<p class="small">6 segundos = ___ km</p><p class="small">15 segundos = ___ km</p><p class="small">3 segundos = ___ km</p></div>
</div>
{seguridad("<p><strong>Si oyes truenos, la tormenta está lo bastante cerca como para que te alcance un rayo.</strong> Busca refugio en un edificio o en un vehículo cerrado. Si estás en el campo: baja de las colinas, aléjate del agua y de las cercas de metal, y <strong>nunca te refugies bajo un árbol solitario</strong>. Espera 30 minutos después del último trueno antes de salir.</p>")}
''', "c-azul")

pagina(f'''
{chip("Capítulo 7 · Señales")}
<h2>¡Aquí estoy! Señales de rescate</h2>
<p>Si te pierdes, lo más importante es <strong>quedarte en un lugar</strong> y ayudar a que te encuentren. Los rescatistas de todo el mundo reconocen estas señales:</p>
<div class="cols" style="gap:0.2in">
<div class="box reto" style="margin:0"><h4>3️⃣ El número mágico: tres</h4><p class="small">Tres de cualquier cosa significa <strong>«¡auxilio!»</strong>: tres silbidos, tres destellos de luz, tres montones de piedras o tres fogatas en triángulo. Descansa un minuto y repite.</p></div>
<div class="box reto" style="margin:0"><h4>📣 El silbato vale oro</h4><p class="small">Un silbato se escucha <strong>mucho más lejos</strong> que tu voz y no te cansa ni te deja afónico. ¡Llévalo siempre colgado en tu mochila!</p></div>
</div>
<h3 style="margin-top:0.2in">Mensajes en el suelo para aviones y helicópteros</h3>
<div class="fig">{I.senales_suelo()}</div>
<p class="small">Hazlos <strong>enormes</strong> (de al menos 3 pasos de largo) con piedras, ramas o ropa, en un claro, y que contrasten con el suelo: oscuros sobre nieve o arena, claros sobre hierba.</p>
<div style="display:flex;gap:0.2in;align-items:center">
<div style="flex:none">{I.espejo_senal()}</div>
{ciencia("<p>Un espejo <strong>refleja</strong> la luz del sol. El ángulo con que llega la luz es igual al ángulo con que rebota. Un destello de espejo puede verse ¡a muchos kilómetros! Apunta formando una «V» con dos dedos hacia el avión o el helicóptero y mueve el espejo para que el reflejo pase por tus dedos.</p>", "🔬 Ciencia: espejo de señales")}
</div>
{seguridad("<p>Jamás apuntes un reflejo a los ojos de una persona ni a los de un piloto por diversión. Y no uses señales de auxilio como juego: son solo para emergencias reales.</p>")}
''', "c-azul")

morse = {"A": "·—", "B": "—···", "C": "—·—·", "D": "—··", "E": "·", "F": "··—·", "G": "——·", "H": "····", "I": "··", "J": "·———",
         "K": "—·—", "L": "·—··", "M": "——", "N": "—·", "O": "———", "P": "·——·", "Q": "——·—", "R": "·—·", "S": "···", "T": "—",
         "U": "··—", "V": "···—", "W": "·——", "X": "—··—", "Y": "—·——", "Z": "——··"}
tabla_m = "".join(f'<div style="border:1.5px solid var(--linea);border-radius:8px;padding:3px 6px;display:flex;justify-content:space-between"><strong style="font-family:Fredoka">{k}</strong><span style="letter-spacing:3px;font-weight:800;font-size:13pt">{v}</span></div>' for k, v in morse.items())
MENSAJE = "ABRAZA UN ARBOL"
codigo = " / ".join(" ".join(morse[ch] for ch in palabra) for palabra in MENSAJE.split())
casillas = "".join('<span style="display:inline-block;width:0.3in;height:0.36in;border-bottom:2px solid var(--tinta);margin:0 2px"></span>' if ch != " " else '<span style="display:inline-block;width:0.25in"></span>' for ch in MENSAJE)
pagina(f'''
{chip("Capítulo 7 · Actividades")}
<h2>El código Morse</h2>
<p>Inventado en el siglo XIX para el telégrafo, el código Morse convierte cada letra en <strong>puntos</strong> (·, señal corta) y <strong>rayas</strong> (—, señal larga). Se puede enviar con sonidos, con una linterna, con un espejo… ¡o golpeando una piedra!</p>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:5px;font-size:11pt;margin:0.12in 0 0.18in">{tabla_m}</div>
<div class="box sabias"><h4>La señal más famosa del mundo: SOS</h4><p style="font-size:18pt;letter-spacing:4px;font-family:Fredoka;text-align:center;margin:0">··· ——— ···</p><p class="small center" style="margin:0">Tres cortas, tres largas, tres cortas. Fácil de recordar y de reconocer.</p></div>
<h3>Descifra el mensaje secreto</h3>
<p>Este es el consejo más importante que te da un rescatista si te pierdes en el bosque:</p>
<p style="font-size:17pt;font-weight:800;letter-spacing:3px;word-spacing:10px;text-align:center;margin:0.1in 0">{codigo}</p>
<p class="center" style="margin:0.15in 0">{casillas}</p>
<h3>Ahora tú: escribe tu nombre en Morse</h3>
{lineas(2)}
{reto("<p>Con una linterna y un familiar en otra habitación (o en la ventana de enfrente), envíense mensajes cortos en Morse. ¿Cuál es la palabra más larga que lograron descifrar? ☐ ¡Reto completado!</p>")}
''', "c-azul")

# ═══════════════════════════ GRAN FINAL ═══════════════════════════
SOPA = ["BRUJULA", "REFUGIO", "FOGATA", "YESCA", "NUDO", "HUELLA", "BOSQUE", "AGUA", "SILBATO", "MAPA", "NUBE", "ESTRELLA", "SOMBRA", "FILTRO", "CUERDA"]
grid, sol_sopa, pos_sopa = P.sopa_de_letras(SOPA, n=14, semilla=5)
filas_s = "".join("<tr>" + "".join(f"<td>{ch}</td>" for ch in fila) + "</tr>" for fila in grid)
lista = "".join(f'<span style="display:inline-block;width:1.35in;font-family:Fredoka;font-weight:600">☐ {p}</span>' for p in SOPA)
pagina(f'''
{chip("Gran final · Pasatiempos")}
<h2>Sopa de letras del explorador</h2>
<p>Encuentra las 15 palabras escondidas. Pueden estar en horizontal, vertical, diagonal… ¡y algunas al revés!</p>
<table class="grid-sopa" style="margin:0.15in auto 0.25in">{filas_s}</table>
<div class="marco" style="padding:0.14in 0.2in;border-style:solid">{lista}</div>
''', "c-verde")

CRUCI = [("CUMULONIMBO", "Nube de tormenta con forma de torre o yunque."),
         ("CONDUCCION", "Pérdida de calor al tocar el suelo frío."),
         ("CLOROFILA", "Pigmento verde que atrapa la luz del sol en las hojas."),
         ("OXIGENO", "Gas del aire que el fuego necesita para arder."),
         ("BRUJULA", "Instrumento con una aguja magnética que señala el norte."),
         ("SILBATO", "Se escucha más lejos que tu voz y no te cansa."),
         ("HERVIR", "La forma más segura de desinfectar el agua del bosque."),
         ("TRUENO", "Sonido que llega después del relámpago."),
         ("YESCA", "Material fino y seco que prende primero."),
         ("POLAR", "Estrella que marca el norte."),
         ("SOMBRA", "Con un palo y su ___ puedes encontrar el este y el oeste."),
         ("NUDO", "El «as de guía» es uno de ellos.")]
filas_x, cols_x, celdas_x, numeros_x, horiz_x, vert_x = P.crucigrama(CRUCI)


def cruci_html(mostrar):
    h = ""
    for r in range(filas_x):
        h += "<tr>"
        for c in range(cols_x):
            if (r, c) in celdas_x:
                n = numeros_x.get((r, c))
                h += f'<td class="l">{f"<span class=n>{n}</span>" if n else ""}{f"<span class=s>{celdas_x[(r, c)]}</span>" if mostrar else ""}</td>'
            else:
                h += "<td></td>"
        h += "</tr>"
    return f'<table class="cruci{" mini" if mostrar else ""}" style="width:{cols_x * (0.27 if mostrar else 0.34):.2f}in">{h}</table>'


pistas_h = "".join(f"<li><strong>{n}.</strong> {p} <span class='tiny'>({len(w)})</span></li>" for n, w, p in horiz_x)
pistas_v = "".join(f"<li><strong>{n}.</strong> {p} <span class='tiny'>({len(w)})</span></li>" for n, w, p in vert_x)
pagina(f'''
{chip("Gran final · Pasatiempos")}
<h2>Crucigrama de la supervivencia</h2>
<p class="small">Todas las respuestas están en este libro. Escríbelas sin tildes. El número entre paréntesis indica cuántas letras tiene la palabra.</p>
<div style="margin:0.12in 0 0.18in">{cruci_html(False)}</div>
<div class="cols small">
<div><h4>➡️ Horizontales</h4><ul style="list-style:none;padding-left:0">{pistas_h}</ul></div>
<div><h4>⬇️ Verticales</h4><ul style="list-style:none;padding-left:0">{pistas_v}</ul></div>
</div>
''', "c-naranja")

mochila = ["Silbato", "Agua suficiente en botella", "Linterna con pilas de repuesto", "Capa o chaqueta impermeable", "Ropa de abrigo extra y gorro",
           "Mapa y brújula", "Botiquín pequeño", "Manta térmica", "Comida energética (frutos secos, barritas)", "Gorra y protector solar",
           "Espejo pequeño de señales", "Bolsa para la basura", "Cuaderno y lápiz", "Cordón de 3 metros"]
pagina(f'''
{chip("Gran final")}
<h2>La mochila del explorador</h2>
<p>Un explorador preparado casi nunca necesita «sobrevivir». Revisa tu mochila antes de cada salida y marca lo que llevas:</p>
<div class="cols">
<ul class="check">{"".join(f"<li>{m}</li>" for m in mochila[:7])}</ul>
<ul class="check">{"".join(f"<li>{m}</li>" for m in mochila[7:])}</ul>
</div>
<div class="box reto"><h4>📝 Antes de salir, deja una nota en casa</h4>
<div class="cols small"><div><p>Vamos a: ______________________</p><p>Salimos a las: _________________</p></div><div><p>Volvemos a las: ________________</p><p>Vamos con: ____________________</p></div></div></div>
<h3>El gran examen del explorador</h3>
<ol class="small" style="padding-left:0.22in">
<li>Si te pierdes, lo primero que haces es… &nbsp; <span class="opcion">a) correr a buscar el camino</span><span class="opcion">b) detenerte y pensar (S.T.O.P.)</span><span class="opcion">c) gritar sin parar</span></li>
<li>¿Qué necesitas con más urgencia en una noche fría? &nbsp; <span class="opcion">a) comida</span><span class="opcion">b) refugio y abrigo</span><span class="opcion">c) una linterna</span></li>
<li>El agua de un arroyo transparente… &nbsp; <span class="opcion">a) se puede beber</span><span class="opcion">b) hay que hervirla</span><span class="opcion">c) solo hay que filtrarla</span></li>
<li>Para encender un fuego se empieza por… &nbsp; <span class="opcion">a) la leña gruesa</span><span class="opcion">b) las astillas</span><span class="opcion">c) la yesca</span></li>
<li>Las hojas secas abrigan porque… &nbsp; <span class="opcion">a) atrapan aire quieto</span><span class="opcion">b) producen calor</span><span class="opcion">c) son de color café</span></li>
<li>Tres silbidos seguidos significan… &nbsp; <span class="opcion">a) «estoy jugando»</span><span class="opcion">b) «¡auxilio!»</span><span class="opcion">c) «ya voy»</span></li>
<li>Una huella sin marcas de uñas y redonda es de un… &nbsp; <span class="opcion">a) felino</span><span class="opcion">b) perro</span><span class="opcion">c) venado</span></li>
<li>Cuentas 12 segundos entre el rayo y el trueno. La tormenta está a… &nbsp; <span class="opcion">a) 12 km</span><span class="opcion">b) 4 km</span><span class="opcion">c) 36 km</span></li>
</ol>
''', "c-verde")

# ─────────────────────────── SOLUCIONES ───────────────────────────


def sopa_sol_html():
    h = ""
    for r in range(14):
        h += "<tr>"
        for c in range(14):
            estilo = ' style="background:#fde9d9;color:#c8412f"' if sol_sopa[r][c] else ' style="color:#c9cfc9"'
            h += f"<td{estilo}>{grid[r][c]}</td>"
        h += "</tr>"
    return f'<table class="grid-sopa mini">{h}</table>'


pagina(f'''
{chip("Soluciones")}
<h2>Soluciones</h2>
<div class="cols small" style="gap:0.2in">
<div>
<h4>Cap. 1 · Orientación</h4>
<p>Rosa: N arriba; en sentido del reloj NE, E, SE, S, SO, O, NO. a) Oeste (el sol se oculta por el oeste). b) Al Norte. c) Porque el musgo crece donde hay humedad y sombra, no en un lado fijo.</p>
<h4>Cap. 2 · Agua</h4>
<p>Orden: 1 Evaporación, 2 Condensación, 3 Precipitación, 4 Escorrentía. V/F: a) F, b) V, c) F, d) V, e) V, f) V.</p>
<h4>Cap. 3 · Fuego</h4>
<p>Yesca: hierba seca, agujas de pino. Astilla: ramitas de lápiz, palitos que hacen «crac». Leña: tronco del brazo, rama de la muñeca. Triángulo: a) calor, b) oxígeno, c) combustible. Errores de Tomás: bajo un árbol, sobre hojas secas, piedras de río (pueden explotar), sin agua cerca, y no dice que haya un adulto.</p>
<h4>Cap. 4 · Refugio</h4>
<p>1-c, 2-d, 3-a, 4-b.</p>
<h4>Cap. 7 · Clima y señales</h4>
<p>6 s = 2 km; 15 s = 5 km; 3 s = 1 km. Mensaje: <strong>ABRAZA UN ARBOL</strong> (si te pierdes, quédate en un lugar).</p>
<h4>Gran examen</h4>
<p>1-b, 2-b, 3-b, 4-c, 5-a, 6-b, 7-a, 8-b.</p>
<h4>Para colorear</h4>
<p>Falta un balde de agua (o tierra) junto a la fogata… ¡y un adulto cuidándola!</p>
</div>
<div>
<h4>Laberinto</h4>
<div>{P.laberinto_svg(13, 15, laberinto_abiertas, laberinto_camino, cel=19)}</div>
</div>
</div>
''', "c-morado")

pagina(f'''
{chip("Soluciones")}
<h2>Solución del crucigrama</h2>
<div style="margin:0.1in 0 0.25in">{cruci_html(True)}</div>
<h2>Solución de la sopa de letras</h2>
<div style="margin-top:0.1in">{sopa_sol_html()}</div>
''', "c-morado")

pagina(f'''
{chip("Soluciones")}
<h2>Glosario del explorador</h2>
<table>
<tr><td style="width:1.5in"><strong>Adsorción</strong></td><td>Cuando partículas se quedan pegadas a la superficie de un material, como en el carbón del filtro.</td></tr>
<tr><td><strong>Aislante</strong></td><td>Material que frena el paso del calor, como las hojas secas o la lana.</td></tr>
<tr><td><strong>Clorofila</strong></td><td>Pigmento verde de las plantas que atrapa la luz del sol.</td></tr>
<tr><td><strong>Combustión</strong></td><td>Reacción química del fuego: combustible + oxígeno + calor.</td></tr>
<tr><td><strong>Condensación</strong></td><td>Cuando el vapor de agua se enfría y se convierte en gotitas.</td></tr>
<tr><td><strong>Cromatografía</strong></td><td>Técnica para separar las sustancias de una mezcla, como los pigmentos de una hoja.</td></tr>
<tr><td><strong>Estomas</strong></td><td>Agujeritos microscópicos de las hojas por donde la planta respira y suelta agua.</td></tr>
<tr><td><strong>Evaporación</strong></td><td>Cuando el agua líquida se convierte en vapor por el calor.</td></tr>
<tr><td><strong>Fotosíntesis</strong></td><td>Proceso con el que las plantas fabrican su alimento usando la luz.</td></tr>
<tr><td><strong>Fricción</strong></td><td>Fuerza de roce que aparece cuando dos superficies se frotan.</td></tr>
<tr><td><strong>Magnetismo</strong></td><td>Fuerza invisible de los imanes. La Tierra también es un imán.</td></tr>
<tr><td><strong>Meteorólogo</strong></td><td>Científico que estudia el clima y el tiempo atmosférico.</td></tr>
<tr><td><strong>Punto cardinal</strong></td><td>Cada una de las cuatro direcciones principales: Norte, Sur, Este y Oeste.</td></tr>
<tr><td><strong>Rastreo</strong></td><td>Arte de leer las huellas y señales que dejan los animales.</td></tr>
<tr><td><strong>Refracción</strong></td><td>Cuando la luz se dobla al pasar por el agua o por una lente, como la lupa.</td></tr>
<tr><td><strong>Transpiración</strong></td><td>Cuando las plantas sueltan vapor de agua por sus hojas.</td></tr>
</table>
''', "c-morado")

# ─────────────────────────── COLOREAR Y NOTAS ───────────────────────────
pagina(f'''
{chip("Gran final · Para colorear")}
<h2>Colorea tu campamento</h2>
<p>Usa los colores de la naturaleza. ¡Y agrega los animales, huellas o nubes que quieras!</p>
<div class="marco" style="border-style:solid;overflow:hidden;margin-top:0.15in">{I.para_colorear(I.portada_escena())}</div>
<p class="small" style="margin-top:0.15in">¿Encuentras algo que falta en este campamento para que sea seguro? <em>Pista: mira las reglas de la fogata.</em></p>
{lineas(2)}
''', "c-verde")

pagina(f'''
{chip("Gran final")}
<h2>Mis notas de explorador</h2>
<p>Anota aquí tus descubrimientos, preguntas nuevas y las aventuras que quieres vivir.</p>
{lineas(22)}
''', "c-verde")

# ─────────────────────────── CERTIFICADO ───────────────────────────
pagina(f'''
<div style="position:absolute;inset:0.4in;border:6px double #2f6b3a;border-radius:24px;padding:0.5in;text-align:center">
<div style="margin-top:0.1in">{I.brujula_icono(120)}</div>
<div style="font-family:Fredoka;font-weight:600;color:var(--naranja);letter-spacing:.2em;font-size:13pt;margin-top:0.2in">CERTIFICADO OFICIAL</div>
<h1 style="font-size:36pt;margin:0.1in 0 0.3in">Explorador Científico<br>de la Naturaleza</h1>
<p style="font-size:14pt">Se otorga este certificado a</p>
<div style="border-bottom:3px solid var(--tinta);width:5in;margin:0.5in auto 0.3in"></div>
<p style="font-size:13pt;max-width:5.4in;margin:0 auto">por completar su entrenamiento en <strong>orientación, agua, fuego, refugio, nudos, plantas, animales, clima y señales</strong>, y por demostrar curiosidad, prudencia y respeto por la naturaleza.</p>
<div style="display:flex;justify-content:space-around;margin-top:0.8in">
<div><div style="border-bottom:2px solid var(--tinta);width:2.2in;height:0.4in"></div><p class="small">Fecha</p></div>
<div><div style="border-bottom:2px solid var(--tinta);width:2.2in;height:0.4in"></div><p class="small">Firma del adulto guía</p></div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0.25in">{I.camino_bosque_deco(620)}</div>
</div>
''', folio=False)

# ─────────────────────────── CONTRAPORTADA ───────────────────────────
from comun import SERIE, LIBROS_SERIE
SERIE_HTML = "".join(
    f'<div style="flex:1;background:{"#fff" if n == 1 else "rgba(255,255,255,.14)"};color:{"#26302a" if n == 1 else "#fff"};border-radius:12px;padding:8px 10px;font-size:9.5pt">'
    f'<div style="font-size:20px">{e}</div><strong style="font-family:Fredoka;font-size:10.5pt">Libro {n}: {t}</strong><br>{d}</div>'
    for n, t, d, e in LIBROS_SERIE)
pagina(f'''
<div style="position:absolute;inset:0;background:#2f6b3a"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:3.6in;overflow:hidden">{I.portada_escena()}</div>
<div style="position:relative;color:#fff;padding:0.3in 0.3in 0">
<h1 style="color:#fff;font-size:32pt">¿Podrías sobrevivir en el bosque?</h1>
<p style="font-size:13.5pt;max-width:6in">Encontrar el norte con una sombra. Sacar agua de las hojas de un árbol. Entender por qué el fuego necesita oxígeno. Construir un refugio que guarde el calor. Leer las nubes y las huellas de los animales.</p>
<p style="font-size:13.5pt;max-width:6in">Este libro convierte la supervivencia en <strong>ciencia divertida</strong>: más de 10 experimentos y retos, explicaciones sencillas, pasatiempos, un diario de campo y un certificado para el explorador que lo complete todo.</p>
<p style="font-family:Fredoka;font-size:14pt;background:rgba(255,255,255,.15);display:inline-block;padding:6px 16px;border-radius:12px">🔬 Ciencia real &nbsp;·&nbsp; 🧭 Aventura &nbsp;·&nbsp; ⚠️ Seguridad primero &nbsp;·&nbsp; 👨‍👩‍👧 En familia</p>
<h3 style="color:#fff;margin-top:0.12in">Colecciona la {SERIE}:</h3>
<div style="display:flex;gap:0.12in">{SERIE_HTML}</div>
</div>
''', folio=False)

# ─────────────────────────── ÍNDICE ───────────────────────────
import re
titulos = []
for i, p in enumerate(paginas):
    m = re.search(r'<div class="num">Capítulo (\d+)</div>\s*<h1>([^<]+)</h1>', p)
    if m:
        titulos.append((f"Capítulo {m.group(1)}", m.group(2), i + 1))
extra = []
for i, p in enumerate(paginas):
    for clave, nombre in [("Cómo usar este libro", "Cómo usar este libro"), ("Las 8 reglas de oro", "Reglas de oro y la regla de los 3"),
                          ("Sopa de letras del explorador", "Gran final: pasatiempos y examen"), ("<h2>Soluciones</h2>", "Soluciones y glosario"),
                          ("CERTIFICADO OFICIAL", "Tu certificado de explorador")]:
        if clave in p:
            extra.append((nombre, i + 1))
filas_i = ""
for nombre, pg in extra[:2]:
    filas_i += f'<tr><td colspan="2"><strong>{nombre}</strong></td><td class="center">{pg}</td></tr>'
colores = ["var(--verde)", "var(--azul)", "var(--naranja)", "var(--cafe)", "#6d4c9f", "var(--verde)", "var(--azul)"]
for (cap, nombre, pg), col in zip(titulos, colores):
    filas_i += f'<tr><td style="width:1.3in;color:{col};font-family:Fredoka;font-weight:600">{cap}</td><td style="font-family:Fredoka;font-size:14pt;font-weight:600">{nombre}</td><td class="center" style="width:0.8in">{pg}</td></tr>'
for nombre, pg in extra[2:]:
    filas_i += f'<tr><td colspan="2"><strong>{nombre}</strong></td><td class="center">{pg}</td></tr>'
indice = f'''
{chip("Índice")}
<h1>Tu mapa del libro</h1>
<p>Puedes leerlo en orden o saltar al capítulo que más te guste. ¡Pero no te saltes las reglas de oro!</p>
<table style="font-size:12.5pt;margin-top:0.2in">
<tr><th colspan="2">Sección</th><th class="center">Página</th></tr>
{filas_i}
</table>
<div class="fig" style="margin-top:0.4in">{I.camino_bosque_deco()}</div>
'''
paginas[INDICE_POS] = paginas[INDICE_POS].replace("__INDICE__", indice)

html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>¡Sobrevive en el Bosque! Ciencia y supervivencia en la naturaleza</title>
<link rel="stylesheet" href="estilos.css"></head>
<body>
{"".join(paginas)}
</body></html>'''
open("libro.html", "w", encoding="utf-8").write(html)
print(f"Páginas: {len(paginas)}")
from mejorar import mejorar; mejorar("libro.html", 1)
