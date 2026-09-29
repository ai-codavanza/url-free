"""Libro 2 de la serie: ¡Sobrevive en la Selva! Ejecuta: python3 build_selva.py"""
import ilustraciones as I
from comun import (Libro, lineas, caja, ciencia, seguridad, sabias, reto, mito, chip, emoji, pasos, tarjetas,
                   vf_tabla, unir)

L = Libro(2, "¡Sobrevive en la Selva!", "Ciencia y supervivencia en el bosque tropical", "libro_selva.html")

# ─────────────── INICIO ───────────────
L.portada(I.selva_escena(), "🧭 Ríos · 🌧️ Lluvia · 🦟 Insectos · 🔥 Fuego · 🐸 Camuflaje · 🌿 Plantas · 📣 Señales",
          fondo_cielo="linear-gradient(#c7ecd9,#eef7df)", color_titulo="#1d5a36")
L.propiedad(emoji("🦜", 120))
L.reservar_indice()

L.pagina(f'''
{chip("Antes de empezar")}
<h2>Bienvenido a la selva</h2>
<p>¡Hola de nuevo, explorador o exploradora! En el Libro 1 aprendiste a orientarte, conseguir agua, encender fuego y construir un refugio en el bosque. Ahora viajamos a un lugar todavía más asombroso: la <strong>selva tropical</strong>, el ecosistema con más vida de todo el planeta.</p>
<p>La selva es caliente, húmeda y está llena de sonidos. Allí casi todo lo que aprendiste funciona… <strong>pero con cambios</strong>. Descubrirás por qué, gracias a la ciencia.</p>
<h3>Lo que ya sabes (del Libro 1)</h3>
{tarjetas([("🛑", "S.T.O.P.", "Si te pierdes: detente, piensa, observa y planea."),
           ("3️⃣", "La regla de los 3", "Primero refugio, luego agua; la comida puede esperar."),
           ("🔥", "El triángulo del fuego", "Calor + combustible + oxígeno."),
           ("💧", "Agua segura", "El agua natural siempre se hierve."),
           ("📣", "Tres = auxilio", "Tres silbidos, tres destellos, tres fuegos."),
           ("🌿", "Regla de oro", "Nunca comas nada silvestre sin un experto.")])}
<p>Busca las mismas señales de siempre: 🔬 <strong>La ciencia detrás</strong>, 🧪 <strong>Experimento</strong>, ⚠️ <strong>Seguridad</strong>, 💡 <strong>¿Sabías que…?</strong>, 🤔 <strong>¿Mito o realidad?</strong> y 🏅 <strong>Reto de explorador</strong>.</p>
{caja("sabias", "👨‍👩‍👧 Nota para madres, padres y docentes", "<p>Este libro enseña ciencia a través de la supervivencia, para leer y practicar <strong>en familia</strong>. Los experimentos usan materiales de casa. Todo lo relacionado con fuego, herramientas cortantes, agua natural y animales requiere supervisión adulta. Las soluciones están al final.</p>")}
''', "c-verde")

L.pagina(f'''
{chip("Lo más importante")}
<h2>Las 8 reglas de oro de la selva</h2>
<p>La selva es hermosa, pero exige respeto. Estas reglas se suman a las del Libro 1:</p>
{pasos(["<strong>Siempre con un guía o un adulto que conozca el lugar.</strong> En la selva es muy fácil desorientarse.",
        "<strong>Mira dónde pisas y dónde pones las manos.</strong> Nunca metas la mano en huecos, bajo troncos o entre hojas sin mirar antes.",
        "<strong>Sacude tus botas, tu ropa y tu hamaca</strong> antes de usarlas: a algunos bichos les encantan los lugares oscuros.",
        "<strong>No toques animales</strong>, aunque parezcan tranquilos o sean muy bonitos. Los colores brillantes suelen ser una advertencia.",
        "<strong>Protégete de los mosquitos</strong>: manga larga, pantalón largo, repelente y mosquitero para dormir.",
        "<strong>No te bañes en ríos sin permiso de un adulto que conozca el lugar.</strong> Las corrientes y algunos animales pueden ser peligrosos.",
        "<strong>Bebe agua segura a menudo</strong>, aunque no tengas sed. Con tanto calor sudas muchísimo.",
        "<strong>Si te pierdes, quédate cerca de un claro o de la orilla de un río</strong>, donde es más fácil que te vean."], "var(--rojo)")}
{seguridad("<p>En la selva, los peligros más comunes no son los jaguares ni las serpientes, sino <strong>el calor, la deshidratación, las picaduras de insectos y perderse</strong>. Por eso estas reglas son tan importantes.</p>", "⚠️ Recuerda")}
''', "c-rojo")

L.pagina(f'''
{chip("Conoce la selva")}
<h2>Un edificio de cuatro pisos</h2>
<p>La selva tropical crece cerca del <strong>ecuador</strong>, donde hace calor todo el año y llueve muchísimo. Está organizada como un edificio con pisos, y cada piso tiene su propio clima y sus propios habitantes:</p>
<div class="fig">{I.capas_selva()}</div>
{ciencia("<p>Las copas de los árboles del dosel atrapan casi toda la luz del sol. Al suelo de la selva llega muy poquita, ¡a veces apenas un <strong>2 %</strong>! Por eso abajo está oscuro aunque sea mediodía, y muchas plantas del sotobosque tienen hojas enormes: son como antenas parabólicas para atrapar la poca luz que llega.</p>")}
{sabias("<p>Las selvas tropicales cubren una parte pequeña de la Tierra, pero en ellas vive <strong>alrededor de la mitad</strong> de todas las especies de plantas y animales terrestres. ¡En un solo árbol de la Amazonía se han encontrado más especies de hormigas que en países enteros!</p>")}
<h3>Encuentra la selva en el mapa</h3>
<p>Algunas grandes selvas tropicales son la <strong>Amazonía</strong> (Brasil, Perú, Colombia, Ecuador, Bolivia, Venezuela y más), la <strong>Selva Lacandona</strong> (México), el <strong>Darién</strong> (Panamá y Colombia), la cuenca del <strong>Congo</strong> (África) y las selvas de <strong>Borneo</strong> (Asia). ¿Hay alguna cerca de tu país? Escríbela:</p>
{lineas(1)}
''', "c-verde")

# ═════════════ CAP 1: ORIENTARSE ═════════════
L.apertura(1, "Orientarse en la selva", "Cuando no ves el sol ni las estrellas, el agua y tu ingenio te guían.", "c-verde",
           f'<div style="margin:0 0.6in 0.5in 0">{emoji("🧭", 170)}</div>',
           ["Descubrir por qué es tan fácil desorientarse en la selva.", "Aprender por qué el agua es la mejor guía.",
            "Marcar tu camino para poder volver.", "Construir una maqueta de una cuenca de ríos.", "Usar coordenadas en un mapa."],
           "<p>El río <strong>Amazonas</strong> lleva más agua que cualquier otro río del mundo. ¡Descarga en el mar alrededor de una quinta parte de toda el agua dulce que llega a los océanos!</p>")

L.pagina(f'''
{chip("Capítulo 1 · Orientación")}
<h2>Bajo el techo verde</h2>
<p>En el bosque del Libro 1 aprendiste a encontrar el norte con la sombra de un palo o con las estrellas. En la selva eso es mucho más difícil:</p>
{tarjetas([("🌳", "No ves el sol", "El dosel tapa el cielo. Casi no hay sombras claras para el método del palo."),
           ("🌙", "Ni las estrellas", "De noche, las copas de los árboles esconden la Estrella Polar y la Cruz del Sur."),
           ("🔁", "Todo se parece", "Árboles, lianas y hojas por todas partes. Es fácil caminar en círculos sin darte cuenta.")])}
{mito("<p><strong>«Si caminas recto, siempre llegarás a algún lado».</strong> En realidad, sin puntos de referencia las personas tendemos a <strong>caminar en círculos</strong>. Los científicos lo comprobaron pidiendo a voluntarios que caminaran en línea recta en un bosque y en un desierto: sin ver el sol, muchos volvieron sin querer al punto de partida.</p>")}
<h3>Tus mejores herramientas</h3>
<div class="cols">
<div><h4>🧭 Brújula y mapa</h4><p class="small">Una brújula funciona igual bajo los árboles: el campo magnético de la Tierra atraviesa las hojas. Por eso los guías de selva la llevan siempre.</p></div>
<div><h4>👂 Tus oídos</h4><p class="small">El rumor de un río, el motor de una lancha, voces o perros pueden llegar desde lejos. Detente, cierra los ojos y escucha un minuto.</p></div>
</div>
<div class="cols">
<div><h4>🌊 El agua</h4><p class="small">Los arroyos bajan, se juntan en ríos más grandes, y en la selva los pueblos suelen estar a orillas de los ríos.</p></div>
<div><h4>🪧 Tus propias marcas</h4><p class="small">Marca tu camino para poder volver por donde viniste. ¡Lo verás en la página siguiente!</p></div>
</div>
''', "c-verde")

L.pagina(f'''
{chip("Capítulo 1 · Orientación")}
<h2>Sigue el agua… con cuidado</h2>
<div class="fig">{I.cuenca()}</div>
<p>El agua de lluvia siempre corre <strong>cuesta abajo</strong>. Los hilitos de agua forman arroyos, los arroyos se unen en ríos, y los ríos en ríos más grandes. Todo el terreno que envía su agua a un mismo río se llama <strong>cuenca</strong>. Como la gente usa los ríos para beber, pescar y viajar en canoa, en la selva muchos pueblos están junto a ellos.</p>
{sabias("<p>En 1971, una joven llamada <strong>Juliane Koepcke</strong> quedó sola en la selva de Perú. Su padre, un biólogo, le había enseñado que siguiendo el agua se llega a la gente. Caminó por los arroyos durante 11 días hasta encontrar a unos trabajadores que la ayudaron. ¡El conocimiento de la naturaleza le salvó la vida!</p>", "💡 Una historia real")}
{seguridad("<p>Seguir un río es <strong>caminar por la orilla</strong>, no meterse en él: el agua puede tener corrientes fuertes. Si un adulto te pide cruzar un río poco profundo, <strong>arrastra los pies</strong> por el fondo: así espantas a las rayas de río que se esconden en la arena.</p>")}
<h3>Marca tu camino</h3>
<div class="cols small">
<div><p><strong>Ramitas quebradas:</strong> dobla (sin arrancar) una ramita a la altura de tus ojos, con la punta hacia donde vas.</p><p><strong>Cintas de colores:</strong> ata una cinta brillante cada pocos pasos, que puedas ver una desde la otra. ¡Recógelas al volver!</p></div>
<div><p><strong>Montoncitos de piedras:</strong> tres piedras apiladas se ven fácil y no dañan nada.</p><p><strong>Mira hacia atrás:</strong> cada cierto tiempo date vuelta. El camino de regreso se ve distinto del de ida.</p></div>
</div>
''', "c-verde")

L.experimento("Crea ríos en una maqueta", "c-verde", "30 minutos", "fácil",
              ["1 hoja de papel grande", "Marcadores lavables (azul, café, verde)", "1 bandeja o tapa de caja", "1 atomizador (rociador) con agua"],
              ["Arruga la hoja de papel hasta hacer una bola y luego estírala un poco, sin aplanarla del todo: tendrá montañas y valles.",
               "Colócala en la bandeja. Pinta las «crestas» (las partes más altas) con marcador café y las zonas planas con verde.",
               "Con marcador azul, dibuja dónde crees que se formarán los ríos.",
               "Rocía agua desde arriba, como si lloviera, y observa por dónde baja la tinta.",
               "Compara: ¿los ríos aparecieron donde pensabas? ¿Dónde se juntaron?"],
              "<p>La <strong>gravedad</strong> tira del agua hacia abajo, así que siempre busca el camino más bajo. Las crestas funcionan como el techo de una casa: separan el agua hacia un lado o hacia el otro (se llaman <strong>divisorias de aguas</strong>). En los valles, el agua de muchas laderas se junta y forma ríos cada vez más grandes. ¡Acabas de construir una <strong>cuenca</strong>!</p>",
              "Dibuja o describe lo que pasó en tu maqueta:", n_lineas=3)

# actividad coordenadas
mapa_items = {(1, 1): "🏕️", (4, 2): "🐒", (6, 5): "🌊", (2, 4): "🦜", (5, 1): "🌳", (3, 6): "🐸", (7, 3): "⛺", (0, 6): "🐊"}
cols_l = "ABCDEFGH"
filas_m = '<tr><th></th>' + "".join(f'<th class="center">{c}</th>' for c in cols_l) + "</tr>"
for r in range(7):
    filas_m += f'<tr><th class="center">{r + 1}</th>'
    for c in range(8):
        e = mapa_items.get((c, r), "")
        bg = "#d7f0ff" if (c, r) in [(6, 4), (6, 5), (6, 6), (5, 6), (7, 4), (7, 5), (7, 6)] else "#eef7e6"
        filas_m += f'<td class="center" style="height:0.5in;font-size:22px;background:{bg}">{e}</td>'
    filas_m += "</tr>"
L.pagina(f'''
{chip("Capítulo 1 · Actividades")}
<h2>El mapa de la expedición</h2>
<p>Los mapas usan <strong>coordenadas</strong>: una letra para la columna y un número para la fila. Por ejemplo, el campamento 🏕️ está en <strong>B2</strong>.</p>
<table style="width:auto;margin:0.1in auto 0.2in">{filas_m}</table>
<div class="cols">
<div><h3>1. ¿Dónde está…?</h3>
<p>🐒 El mono: ______ &nbsp; 🦜 El loro: ______</p><p>🐸 La rana: ______ &nbsp; ⛺ El refugio: ______</p><p>🐊 El caimán: ______ &nbsp; 🌳 La ceiba: ______</p></div>
<div><h3>2. Dibuja en el mapa</h3>
<p>Un ⭐ tesoro en <strong>E4</strong>, una 🐍 serpiente en <strong>A3</strong> y una 🌺 flor en <strong>H1</strong>.</p></div>
</div>
<h3>3. El camino al río</h3>
<p>Desde el campamento (B2), el río 🌊 está en G6. Si solo puedes moverte en línea recta (sin diagonales), ¿cuántas casillas necesitas como mínimo para llegar? Explica tu ruta:</p>
{lineas(3)}
''', "c-verde")

# ═════════════ CAP 2: AGUA Y LLUVIA ═════════════
L.apertura(2, "Agua y lluvia", "En la selva llueve casi todos los días. Aprende a aprovecharlo.", "c-azul",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("🌧️", 170)}</div>',
           ["Descubrir los «ríos voladores» de la selva.", "Encontrar agua en lugares sorprendentes.",
            "Construir un pluviómetro para medir la lluvia.", "Recordar por qué siempre hay que hervir el agua."],
           "<p>En muchas zonas de la Amazonía caen más de <strong>2 000 litros de lluvia por metro cuadrado al año</strong>. ¡Es como si cada metro cuadrado recibiera 2 000 botellas de un litro!</p>")

L.pagina(f'''
{chip("Capítulo 2 · Agua")}
<h2>La selva fabrica su propia lluvia</h2>
<p>¿Recuerdas la <strong>transpiración</strong> del Libro 1, cuando las plantas «sudaban» dentro de una bolsa? En la selva hay miles de millones de árboles haciéndolo a la vez. Tanto vapor de agua sube al cielo que forma enormes corrientes de humedad que viajan por el aire: los científicos las llaman <strong>ríos voladores</strong>. Ese vapor forma nubes y vuelve a caer como lluvia, a veces a miles de kilómetros.</p>
{ciencia("<p>Por eso cuidar la selva es cuidar la lluvia. Cuando se talan muchos árboles, hay menos transpiración, se forman menos nubes y puede llover menos en otras regiones, incluso en zonas de cultivo lejanas.</p>")}
<h3>¿Dónde hay agua en la selva?</h3>
{tarjetas([("🌧️", "La lluvia", "La fuente más limpia. Una hoja grande de plátano o una lona funcionan como embudo hacia un recipiente."),
           ("🌺", "Las bromelias", "Estas plantas forman una copa con sus hojas que guarda agua. ¡Son piscinas para ranitas e insectos!"),
           ("🎋", "El bambú", "Algunos tallos de bambú guardan agua dentro de sus segmentos."),
           ("🌊", "Ríos y arroyos", "Abundan, pero su agua puede traer microbios y barro."),
           ("💦", "El rocío", "Por la mañana, las hojas amanecen empapadas."),
           ("🌿", "Las lianas", "Los expertos conocen lianas que guardan agua… pero algunas tienen savia tóxica. ¡No las pruebes!")])}
{seguridad("<p>Aunque la selva está llena de agua, <strong>toda el agua natural debe hervirse</strong> (al menos 1 minuto de ebullición fuerte) antes de beberla, incluso la de lluvia que haya tocado hojas o techos. En clima caluroso, además, los microbios se multiplican más rápido.</p>")}
''', "c-azul")

L.experimento("Construye un pluviómetro", "c-azul", "20 minutos + una semana de mediciones", "fácil",
              ["1 botella de plástico transparente de lados rectos", "Tijeras (con un adulto)", "1 regla y marcador permanente", "Piedritas", "Cinta adhesiva"],
              ["Un adulto corta la parte de arriba de la botella, donde empieza a curvarse.",
               "Pon piedritas en el fondo para que no se vuele, y agrega agua hasta cubrirlas. Marca ese nivel como <strong>0</strong>.",
               "Pega la regla por fuera, con el 0 en esa marca (o dibuja una escala cada centímetro).",
               "Da la vuelta a la parte que cortaste y colócala como embudo. Pon el pluviómetro al aire libre, lejos de techos y árboles.",
               "Cada día a la misma hora anota cuánta agua cayó y vuelve a dejar el nivel en 0."],
              "<p>Los meteorólogos miden la lluvia en <strong>milímetros</strong>. Si tu pluviómetro marca 10 mm, significa que, si el agua no se escurriera ni se evaporara, el suelo quedaría cubierto por una capa de agua de 1 cm. ¡Y <strong>1 mm de lluvia equivale a 1 litro de agua por cada metro cuadrado</strong>! Así se comparan las lluvias de lugares muy distintos.</p>",
              "Mi registro de lluvia:",
              resultados='<table><tr><th>Día</th><th>L</th><th>M</th><th>M</th><th>J</th><th>V</th><th>S</th><th>D</th></tr><tr><td>mm</td><td style="height:0.4in"></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>',
              n_lineas=0)

L.pagina(f'''
{chip("Capítulo 2 · Actividades")}
<h2>¡Pon a prueba tus gotas de saber!</h2>
<h3>1. ¿Verdadero o falso?</h3>
{vf_tabla(["En la selva, el agua de lluvia que corre por las hojas se puede beber sin hervir.",
           "Los árboles de la selva ayudan a formar nubes con su transpiración.",
           "Las bromelias guardan agua entre sus hojas.",
           "Cualquier liana con agua se puede beber sin problema.",
           "1 mm de lluvia equivale a 1 litro de agua por metro cuadrado.",
           "Talar muchos árboles puede hacer que llueva menos en otros lugares."])}
<h3 style="margin-top:0.2in">2. Problema de explorador</h3>
<p>En tu pluviómetro mediste esta semana: <strong>12 mm, 0 mm, 25 mm, 8 mm, 0 mm, 30 mm y 5 mm</strong>.</p>
<p>a) ¿Cuántos milímetros llovieron en total? ______ mm</p>
<p>b) ¿Cuántos litros cayeron sobre un metro cuadrado? ______ litros</p>
<p>c) Si tu techo mide 20 metros cuadrados, ¿cuántos litros podrías recoger? ______ litros</p>
<h3 style="margin-top:0.2in">3. Diseña un recolector de lluvia</h3>
<p class="small">Solo con cosas de la selva (hojas grandes, bambú, lianas, cáscaras…). Dibújalo y señala cómo llega el agua al recipiente.</p>
<div class="marco" style="height:2.6in"></div>
''', "c-azul")

# ═════════════ CAP 3: SECO Y SANO ═════════════
L.apertura(3, "Seco y sano", "Calor, humedad e insectos: los verdaderos retos de la selva.", "c-naranja",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("🦟", 170)}</div>',
           ["Entender por qué la humedad hace sentir más calor.", "Cuidar tus pies y tu ropa.",
            "Protegerte de mosquitos y otros insectos.", "Dormir lejos del suelo.", "Descubrir la capilaridad con agua que «camina»."],
           "<p>Los mosquitos encuentran a las personas por el <strong>dióxido de carbono</strong> que exhalamos, el calor de nuestro cuerpo y el olor del sudor. ¡Pueden detectar tu aliento a varios metros!</p>")

L.pagina(f'''
{chip("Capítulo 3 · Seco y sano")}
<h2>El calor pegajoso</h2>
<p>En la selva, la temperatura suele estar entre 25 y 32 °C, pero lo que más se nota es la <strong>humedad</strong>: el aire está tan cargado de vapor que la ropa nunca termina de secarse.</p>
{ciencia("<p>Tu cuerpo se enfría <strong>sudando</strong>: cuando el sudor se evapora, se lleva calor de tu piel (es la <strong>evaporación</strong> que viste en el Libro 1). Pero si el aire ya está lleno de vapor, el sudor se evapora muy despacio. Entonces sudas, te mojas… ¡y no te refrescas! Por eso con humedad sentimos más calor que el que marca el termómetro.</p><p><strong>Pruébalo:</strong> moja un dedo y sóplalo; luego sopla un dedo seco. El mojado se siente más frío porque el agua, al evaporarse, le roba calor.</p>")}
<h3>Consejos del explorador tropical</h3>
<div class="cols small">
<ul>
<li><strong>Bebe agua segura a menudo</strong>, en pequeños sorbos, aunque no tengas sed.</li>
<li><strong>Descansa a la sombra</strong> en las horas de más calor.</li>
<li><strong>Ropa ligera, de manga larga</strong> y colores claros: te protege del sol, las espinas y los insectos.</li>
<li><strong>Observa tu orina:</strong> si es oscura, tu cuerpo necesita más agua.</li>
</ul>
<ul>
<li><strong>Cuida tus pies:</strong> sécalos cada noche y cambia los calcetines. Los pies siempre mojados se lastiman y se infectan.</li>
<li><strong>Guarda una muda seca</strong> en una bolsa cerrada solo para dormir.</li>
<li><strong>Revisa tu piel</strong> cada noche buscando picaduras, garrapatas o raspones, y cuéntale a un adulto.</li>
<li><strong>Limpia cualquier herida</strong> enseguida: con tanta humedad se infectan rápido.</li>
</ul>
</div>
{mito("<p><strong>«Si sudas mucho, estás bien hidratado».</strong> ¡Al revés! Sudar mucho significa que estás <strong>perdiendo</strong> agua y sales. Hay que reponerla bebiendo.</p>")}
''', "c-naranja")

L.pagina(f'''
{chip("Capítulo 3 · Seco y sano")}
<h2>Pequeños pero peligrosos: los insectos</h2>
<p>El animal más peligroso de la selva no es el jaguar: es el <strong>mosquito</strong>. Algunos pueden transmitir enfermedades como el <strong>dengue</strong> o la <strong>malaria</strong>. La buena noticia: ¡se pueden evitar!</p>
{tarjetas([("👕", "Cubre tu piel", "Manga larga y pantalón largo, metido dentro de los calcetines."),
           ("🧴", "Repelente", "Que un adulto te lo aplique en la piel descubierta, siguiendo la etiqueta."),
           ("🕸️", "Mosquitero", "Duerme siempre bajo un mosquitero bien cerrado."),
           ("🌅", "Horas clave", "Muchos mosquitos pican más al amanecer y al atardecer."),
           ("💧", "Agua quieta", "Los mosquitos ponen sus huevos en charcos y recipientes con agua estancada."),
           ("🐜", "Hormigas", "Nunca te sientes sobre un hormiguero ni cerca de un sendero de hormigas.")])}
<h3>Duerme en las alturas</h3>
<div class="fig">{I.refugio_elevado()}</div>
<p class="small">En la selva, los exploradores no duermen en el suelo: está húmedo, lleno de insectos y puede inundarse con una tormenta. Usan una <strong>hamaca con mosquitero</strong> y un techo de hojas grandes o una lona, bien inclinado para que escurra la lluvia.</p>
''', "c-naranja")

L.experimento("El agua que camina", "c-naranja", "1 hora (y mirar después)", "fácil",
              ["3 vasos transparentes", "2 tiras de papel de cocina (toalla de papel)", "Agua", "Colorante de alimentos (rojo y azul)", "1 calcetín de algodón viejo (opcional)"],
              ["Pon los tres vasos en fila. Llena el primero y el tercero de agua; deja vacío el del medio.",
               "Pinta el agua: rojo en el primer vaso y azul en el tercero.",
               "Dobla cada tira de papel a lo largo. Une el vaso rojo con el vacío usando una tira, y el azul con el vacío usando la otra.",
               "Espera y observa cada 15 minutos. ¿Qué pasa en el vaso del medio?",
               "Extra: mete la punta de un calcetín de algodón en un vaso con agua y déjalo colgando fuera. ¿Hasta dónde se moja?"],
              "<p>El papel y el algodón están hechos de fibras con espacios diminutos entre ellas. El agua es atraída por esas fibras y <strong>sube por los huequitos</strong>, ¡incluso en contra de la gravedad! Esto se llama <strong>capilaridad</strong>. Así suben el agua las plantas desde sus raíces… y así se empapa un calcetín de algodón en la selva y tarda tanto en secarse. Por eso los exploradores prefieren calcetines de lana o de materiales sintéticos que se secan rápido.</p>",
              "¿De qué color quedó el vaso del medio? ¿Por qué?", n_lineas=2)

L.pagina(f'''
{chip("Capítulo 3 · Actividades")}
<h2>El detective de la salud</h2>
<h3>1. ¿Qué harías?</h3>
<p>a) Llevas todo el día con los calcetines mojados y te duelen los pies:</p>{lineas(1)}
<p>b) Tu orina es muy oscura y te duele la cabeza por el calor:</p>{lineas(1)}
<p>c) Está atardeciendo y empiezas a oír zumbidos de mosquitos:</p>{lineas(1)}
<p>d) Vas a ponerte las botas que dejaste afuera toda la noche:</p>{lineas(1)}
<h3 style="margin-top:0.15in">2. Encuentra los criaderos de mosquitos</h3>
<p>Los mosquitos ponen huevos en el agua quieta. Encierra los lugares donde podrían nacer mosquitos cerca de tu casa o tu escuela:</p>
{tarjetas([("🪣", "Cubeta con agua de lluvia", "☐ Sí &nbsp; ☐ No"), ("🛞", "Llanta vieja en el patio", "☐ Sí &nbsp; ☐ No"), ("🏞️", "Río que corre rápido", "☐ Sí &nbsp; ☐ No"),
           ("🪴", "Platito bajo una maceta", "☐ Sí &nbsp; ☐ No"), ("🥥", "Cáscara de coco tirada", "☐ Sí &nbsp; ☐ No"), ("🚿", "Ducha que se usa y seca", "☐ Sí &nbsp; ☐ No")], 3)}
{reto("<p>Con un adulto, da una vuelta por tu casa buscando recipientes con agua estancada. Vacíalos, voltéalos o tápalos. ¡Acabas de proteger a tu familia del dengue! ☐ ¡Reto completado!</p>")}
''', "c-naranja")

# ═════════════ CAP 4: FUEGO EN LA HUMEDAD ═════════════
L.apertura(4, "Fuego en la humedad", "Encender fuego donde todo está mojado es un reto de ciencia.", "c-rojo",
           f'<div style="margin:0 0.6in 0.3in 0"><svg viewBox="-60 -110 120 130" width="190" height="206">{I.fogata(0, 0, 1.0)}</svg></div>',
           ["Descubrir por qué la madera mojada no arde bien.", "Encontrar materiales secos en un lugar húmedo.",
            "Entender para qué sirve el fuego en la selva.", "Hacer el experimento del globo que no explota."],
           "<p>Algunos árboles tropicales producen <strong>resinas</strong> que arden aunque estén húmedas. Una de ellas, el <strong>copal</strong>, se usa desde hace siglos en México y Centroamérica como incienso.</p>")

L.pagina(f'''
{chip("Capítulo 4 · Fuego")}
<h2>¿Por qué no arde la madera mojada?</h2>
{ciencia("<p>Para que la madera arda, primero hay que calentarla mucho. Pero si está mojada, el calor se gasta en <strong>evaporar el agua</strong> que tiene dentro, y mientras quede agua la madera no puede calentarse lo suficiente. El agua es una gran «esponja de calor»: necesita muchísima energía para calentarse y evaporarse. Por eso el humo de la madera húmeda es blanco y espeso: ¡está lleno de vapor de agua!</p>")}
<h3>Dónde encontrar material seco en la selva</h3>
{tarjetas([("🪵", "Ramas muertas que siguen en el árbol", "Se secan más que las que están en el suelo empapado."),
           ("🪓", "El corazón de la madera", "Un adulto puede partir una rama muerta: por dentro suele estar seca."),
           ("🌰", "Resinas", "Algunas gotas de resina arden aun con humedad. Solo un experto sabe reconocerlas."),
           ("🥥", "Cáscaras y fibras", "La fibra seca de coco y algunas hojas muertas de palma prenden bien."),
           ("🎒", "Tu propia yesca", "Los exploradores llevan yesca seca en una bolsa cerrada. ¡Nunca falla!"),
           ("🔥", "Secar poco a poco", "Poner leña cerca (no encima) del fuego la va secando para después.")])}
<h3>¿Para qué sirve el fuego en la selva?</h3>
<div class="cols small">
<ul><li><strong>Hervir agua</strong> para que sea segura.</li><li><strong>Secar la ropa</strong> y calentarse en noches de lluvia.</li></ul>
<ul><li><strong>Hacer señales</strong> con humo (lo verás en el capítulo 7).</li><li>Su <strong>humo</strong> ayuda a alejar a los mosquitos.</li></ul>
</div>
{seguridad("<p>Todas las reglas del fuego del Libro 1 siguen valiendo: <strong>un adulto enciende y cuida el fuego</strong>, se hace en un lugar despejado y se apaga por completo (¡ahoga, remueve, ahoga!). Nunca quemes selva viva: un incendio forestal destruye el hogar de miles de animales.</p>")}
''', "c-rojo")

L.experimento("El globo que no explota", "c-rojo", "15 minutos", "media",
              ["2 globos", "1 vela en un plato", "Agua", "Fósforos (¡solo el adulto!)", "Un lugar al aire libre o junto al fregadero"],
              ["Infla un globo solo con aire y átalo.",
               "Mete un poco de agua en el otro globo (como medio vaso), luego ínflalo y átalo.",
               "El adulto enciende la vela.",
               "El adulto acerca el globo de aire a la llama. ¡PUM! Explota casi al instante.",
               "Ahora el adulto acerca el globo con agua, justo donde está el agua. ¿Qué pasa?"],
              "<p>El globo con aire explota porque la llama calienta la goma hasta que se debilita y se rompe. En el globo con agua, el calor atraviesa la goma y pasa enseguida al <strong>agua</strong>, que absorbe muchísima energía sin calentarse demasiado. La goma no llega a quemarse. Esto se llama <strong>capacidad calorífica</strong>: el agua es de las sustancias que más calor pueden «guardar». ¡Es la misma razón por la que la madera mojada cuesta tanto que arda!</p>",
              "¿Cuántos segundos aguantó cada globo?",
              seg=seguridad("<p><strong>Solo un adulto</strong> maneja la vela y los globos cerca de la llama. Ten agua cerca, el pelo recogido y los ojos alejados. Si el globo se mancha de negro por abajo, es solo hollín: se limpia con un paño.</p>"), n_lineas=2)

L.pagina(f'''
{chip("Capítulo 4 · Actividades")}
<h2>¡Enciende tu mente tropical!</h2>
<h3>1. ¿Cuál arde mejor?</h3>
<p>Numera del 1 (arde mejor) al 5 (arde peor):</p>
<table><tr><th style="width:0.7in">N.º</th><th>Material</th></tr>
<tr><td></td><td>Tronco verde recién cortado</td></tr><tr><td></td><td>Fibra seca de coco guardada en una bolsa</td></tr>
<tr><td></td><td>Rama muerta caída en un charco</td></tr><tr><td></td><td>Rama muerta que seguía colgada del árbol</td></tr><tr><td></td><td>Ramitas finas secadas junto al fuego</td></tr></table>
<h3 style="margin-top:0.2in">2. Completa las frases</h3>
<p>a) La madera mojada hace humo ____________ porque tiene mucho vapor de agua.</p>
<p>b) El agua necesita mucha ____________ para calentarse y evaporarse.</p>
<p>c) En la selva, el humo del fuego ayuda a alejar a los ____________.</p>
<p>d) Antes de beber agua del río, hay que ____________ al menos 1 minuto.</p>
<h3 style="margin-top:0.2in">3. Piensa como científico</h3>
<p>¿Por qué crees que una olla con agua puede ponerse sobre el fuego sin que se queme el fondo, pero una olla vacía se quema enseguida? Usa lo que aprendiste con el globo:</p>
{lineas(4)}
''', "c-rojo")

# ═════════════ CAP 5: ANIMALES ═════════════
L.apertura(5, "Animales de la selva", "Maestros del camuflaje, colores de advertencia y trucos increíbles.", "c-morado",
           f'<div style="margin:0 0.3in 0.1in 0">{I.svg(280, 230, I.rana(140, 150, 3.0))}</div>',
           ["Descubrir cómo se esconden los animales.", "Entender qué significan los colores brillantes.",
            "Conocer a los imitadores de la selva.", "Aprender a evitar a los animales peligrosos.", "Jugar al experimento del camuflaje."],
           "<p>Algunas ranas dardo de la selva son tan venenosas que los pueblos indígenas usaban su veneno en las puntas de sus dardos. Pero las que nacen en zoológicos <strong>no son venenosas</strong>: ¡obtienen el veneno de las hormigas y ácaros que comen en la selva!</p>")

L.pagina(f'''
{chip("Capítulo 5 · Animales")}
<h2>Esconderse o avisar</h2>
<p>En la selva hay tantos animales que todos necesitan un truco para no ser comidos. Los científicos han descubierto tres estrategias principales:</p>
<div class="cols-3">
<div class="box reto" style="margin:0"><h4>🦎 Camuflaje</h4><p class="small">Tener el color y la forma del lugar donde vives para pasar desapercibido. Ejemplos: los <strong>insectos palo</strong>, las <strong>mariposas hoja</strong>, el <strong>perezoso</strong> (¡con algas verdes en el pelo!) y las manchas del <strong>jaguar</strong> en la sombra.</p></div>
<div class="box seguridad" style="margin:0"><h4>🐸 Colores de advertencia</h4><p class="small">Algunos animales venenosos tienen colores brillantes (rojo, amarillo, azul, naranja) que dicen: <strong>«¡No me comas, soy peligroso!»</strong>. Esto se llama <strong>aposematismo</strong>. Ejemplos: las <strong>ranas dardo</strong> y muchas orugas.</p></div>
<div class="box mito" style="margin:0"><h4>🎭 Imitadores</h4><p class="small">Algunos animales inofensivos copian los colores de los peligrosos para que los dejen en paz. Esto se llama <strong>mimetismo</strong>. Ejemplo: las <strong>falsas corales</strong>, serpientes que imitan a las corales venenosas.</p></div>
</div>
{ciencia("<p>¿Cómo aparecen estos trucos? Por <strong>selección natural</strong>. Imagina insectos de muchos colores. Los pájaros ven y comen más fácilmente a los que no se parecen a las hojas. Los que se parecen sobreviven, tienen crías parecidas a ellos… y, después de muchísimas generaciones, casi todos son expertos en camuflaje. ¡Lo comprobarás con el experimento de este capítulo!</p>")}
{mito("<p><strong>«Rojo con amarillo, mata a un amigo; rojo con negro, amigo del pueblo»</strong> es un dicho para distinguir corales de falsas corales… ¡pero solo sirve en parte de Norteamérica! En Centroamérica y Sudamérica hay corales venenosas con los colores en otro orden. <strong>Regla segura: no toques ninguna serpiente.</strong></p>")}
''', "c-morado")

L.pagina(f'''
{chip("Capítulo 5 · Animales")}
<h2>Convivir con los animales de la selva</h2>
<p>Casi todos los animales de la selva <strong>prefieren huir</strong> de las personas. Los problemas suelen ocurrir cuando los pisamos, los tocamos o los sorprendemos sin querer. Estas son las reglas del explorador:</p>
<table class="small">
<tr><th style="width:1.4in">Animal</th><th>Cómo evitar problemas</th></tr>
<tr><td>🐍 <strong>Serpientes</strong></td><td>Camina por senderos despejados, mira dónde pisas y usa un palo para mover hojas. Si ves una, quédate quieto, retrocede despacio y deja que se vaya.</td></tr>
<tr><td>🐛 <strong>Orugas peludas</strong></td><td>Algunas tienen pelos con veneno que pueden causar reacciones graves. Nunca toques una oruga peluda ni te apoyes en troncos sin mirar.</td></tr>
<tr><td>🐜 <strong>Hormigas</strong></td><td>La <strong>hormiga bala</strong> tiene una de las picaduras más dolorosas del mundo. Mira antes de apoyarte en un árbol o sentarte.</td></tr>
<tr><td>🕷️ <strong>Arañas y escorpiones</strong></td><td>Les gustan los lugares oscuros: sacude botas, ropa y hamacas antes de usarlas.</td></tr>
<tr><td>🐊 <strong>Caimanes</strong></td><td>Mantente lejos de las orillas de ríos y lagunas, sobre todo de noche. Sus ojos brillan con la linterna.</td></tr>
<tr><td>🐆 <strong>Jaguares</strong></td><td>Son muy tímidos y casi nunca se dejan ver. Si ves uno: no corras, mantente de pie, hazte grande y retrocede despacio mirándolo.</td></tr>
<tr><td>🐒 <strong>Monos</strong></td><td>¡No les des comida! Se acostumbran a las personas y pueden morder para quitarte las cosas.</td></tr>
</table>
{seguridad("<p>Si te pica o te muerde cualquier animal, <strong>avisa enseguida a un adulto</strong> y quédate tranquilo y quieto. No intentes chupar ni cortar la herida (¡eso es un mito peligroso!). El adulto buscará ayuda médica.</p>")}
{sabias("<p>Los <strong>monos aulladores</strong> tienen uno de los gritos más fuertes del reino animal: ¡se oyen a kilómetros de distancia en la selva!</p>")}
''', "c-morado")

L.experimento("El juego del camuflaje", "c-morado", "30 minutos", "fácil",
              ["40 palillos o trocitos de lana: 10 verdes, 10 cafés, 10 rojos y 10 amarillos", "Un jardín o un parque con césped", "Un reloj", "Un compañero de juego (el «pájaro»)"],
              ["Mientras el «pájaro» no mira, esparce los 40 palillos sobre un pedazo de césped de unos 2 × 2 pasos.",
               "El «pájaro» tiene <strong>30 segundos</strong> para recoger todos los palillos que pueda, de uno en uno.",
               "Cuenta cuántos palillos de cada color encontró y anótalo en la tabla.",
               "Repite cambiando de papel. ¿Qué colores «sobrevivieron» más?",
               "Recoge todos los palillos al terminar. ¡No dejes rastro!"],
              "<p>Los palillos verdes y cafés se confunden con el césped y la tierra, así que el «pájaro» los encuentra menos. En la naturaleza, los animales que se esconden mejor sobreviven más y tienen más crías. Así, generación tras generación, la <strong>selección natural</strong> hace que muchos animales tengan colores parecidos a su hogar.</p>",
              "Anota tus resultados:",
              resultados='<table><tr><th>Color</th><th>Encontrados ronda 1</th><th>Encontrados ronda 2</th><th>¿Sobrevivió bien?</th></tr><tr><td>Verde</td><td></td><td></td><td></td></tr><tr><td>Café</td><td></td><td></td><td></td></tr><tr><td>Rojo</td><td></td><td></td><td></td></tr><tr><td>Amarillo</td><td></td><td></td><td></td></tr></table>',
              n_lineas=0)

L.pagina(f'''
{chip("Capítulo 5 · Actividades")}
<h2>El club de los trucos animales</h2>
<h3>1. Une cada animal con su truco</h3>
{unir(["Insecto palo", "Rana dardo azul", "Falsa coral", "Perezoso con algas", "Mono aullador"],
      ["Colores de advertencia", "Grito que se oye a kilómetros", "Camuflaje verde en el pelo", "Parece una rama", "Imita a un animal venenoso"])}
<h3 style="margin-top:0.12in">2. Inventa un animal de la selva</h3>
<p class="small">Dibuja un animal nuevo. Decide en qué piso de la selva vive y qué truco usa para sobrevivir (camuflaje, advertencia o imitación).</p>
<div class="cols">
<div class="marco" style="height:2.9in"></div>
<div><p><strong>Nombre:</strong></p>{lineas(1)}<p><strong>Piso de la selva:</strong></p>{lineas(1)}<p><strong>Su truco:</strong></p>{lineas(2)}<p><strong>¿Qué come?</strong></p>{lineas(1)}</div>
</div>
''', "c-morado")

# ═════════════ CAP 6: PLANTAS ═════════════
L.apertura(6, "Plantas de la selva", "Gigantes, trepadoras y plantas que viven en el aire.", "c-verde",
           f'<div style="margin:0 0.5in 0.3in 0">{emoji("🌿", 170)}</div>',
           ["Conocer las raíces gigantes y las plantas que viven sobre otras.", "Descubrir por qué muchas hojas tienen punta.",
            "Conocer medicinas que vienen de la selva.", "Hacer el experimento de las hojas que escurren.", "Completar tu diario de campo tropical."],
           "<p>La <strong>ceiba</strong> es uno de los árboles más altos de la selva americana: puede superar los 60 metros. ¡Es como un edificio de 20 pisos! Para los mayas era un árbol sagrado que unía la tierra con el cielo.</p>")

L.pagina(f'''
{chip("Capítulo 6 · Plantas")}
<h2>Los inventos de las plantas tropicales</h2>
<p>En la selva todas las plantas compiten por la <strong>luz</strong>. Por eso han «inventado» soluciones sorprendentes:</p>
{tarjetas([("🌳", "Raíces tabulares", "El suelo de la selva es delgado. Los árboles gigantes desarrollan enormes raíces con forma de tabla que los sostienen como las patas de una mesa."),
           ("🪢", "Lianas", "Plantas trepadoras que usan a los árboles como escalera para llegar a la luz sin gastar en un tronco grueso."),
           ("🌺", "Epífitas", "Orquídeas, bromelias y helechos que viven sobre las ramas, bien arriba, sin tocar el suelo. ¡No son parásitas: solo se apoyan!"),
           ("💧", "Puntas de goteo", "Hojas terminadas en punta para que la lluvia escurra rápido y no crezcan hongos ni musgo encima."),
           ("🍃", "Hojas gigantes", "Abajo, donde hay poca luz, las hojas enormes atrapan cada rayo de sol."),
           ("🍂", "Reciclaje veloz", "Hongos e insectos descomponen las hojas caídas en semanas. Los nutrientes vuelven enseguida a las plantas.")], 2)}
{sabias("<p>Muchas medicinas vienen de plantas de la selva. Durante siglos, la corteza del árbol de la <strong>quina</strong> (de los Andes y la Amazonía) fue el principal remedio contra la malaria. ¡Y los científicos siguen estudiando plantas de la selva en busca de medicinas nuevas!</p>")}
{seguridad("<p>La regla de oro del Libro 1 es aún más importante aquí: <strong>nunca comas ni toques plantas, frutos, hongos o savias desconocidas</strong>. En la selva hay plantas cuya savia irrita la piel o los ojos, y frutos tóxicos que se parecen a los comestibles. Solo las personas expertas del lugar saben distinguirlos.</p>")}
''', "c-verde")

L.pagina(f'''
{chip("Capítulo 6 · Plantas")}
<h2>Regalos de la selva</h2>
<p>Muchas cosas que usas cada día vienen de plantas que nacieron en selvas tropicales. ¿Las conocías?</p>
{tarjetas([("🍫", "Cacao", "El chocolate viene de las semillas del cacao, un árbol del sotobosque americano que los mayas y aztecas ya cultivaban."),
           ("🎈", "Caucho", "La goma de los globos y las pelotas se hacía con el látex del árbol del caucho, de la Amazonía."),
           ("🍌", "Plátano y bijao", "Sus hojas enormes sirven de techo, de plato y para envolver tamales y otros alimentos."),
           ("🫐", "Açaí", "Fruto de una palmera amazónica que alimenta desde hace siglos a los pueblos de la región."),
           ("🍍", "Piña", "Es pariente de las bromelias: ¡también forma una roseta de hojas!"),
           ("💊", "Medicinas", "Muchas medicinas se descubrieron estudiando plantas que usaban los pueblos indígenas.")], 2)}
{ciencia("<p>Los pueblos indígenas de la selva conocen miles de plantas y sus usos. Ese <strong>conocimiento tradicional</strong>, pasado de abuelos a nietos durante siglos, ha ayudado mucho a la ciencia moderna. Cuidar la selva también es cuidar a las personas que la conocen mejor que nadie.</p>", "🔬 Ciencia y saber tradicional")}
<h3>¿Cómo puedes ayudar a la selva desde tu casa?</h3>
<ul class="check">
<li>Usar papel por los dos lados y reciclarlo: menos árboles cortados.</li>
<li>Preferir productos con sellos de cultivo responsable (por ejemplo, en el chocolate o el café).</li>
<li>No comprar animales silvestres como mascotas: su hogar es la selva.</li>
<li>Contarle a tu familia y amigos lo que aprendiste en este libro.</li>
</ul>
''', "c-verde")

L.experimento("Hojas que escurren la lluvia", "c-verde", "25 minutos", "fácil",
              ["Papel encerado o una bolsa plástica gruesa", "Tijeras", "1 atomizador con agua", "1 reloj o cronómetro", "Palitos y plastilina para sostener las hojas"],
              ["Recorta dos hojas del mismo tamaño: una <strong>redonda</strong> y otra con una <strong>punta larga</strong> (mira el dibujo).",
               "Sujétalas con plastilina a un palito, un poco inclinadas, como si colgaran de una rama.",
               "Rocía las dos con la misma cantidad de agua (por ejemplo, 5 disparos).",
               "Espera 1 minuto. ¿Cuál tiene más gotas encima todavía?",
               "Prueba con otras formas: ¿qué forma escurre mejor?"],
              "<p>El agua forma gotas que ruedan por la hoja empujadas por la <strong>gravedad</strong>. En la hoja redonda, las gotas se quedan quietas en el centro. En la hoja con punta, las gotas se juntan y la punta las guía hacia abajo, como un pequeño canal. Una hoja que se seca rápido aprovecha mejor la luz y evita que crezcan hongos, algas y musgo encima. ¡La forma de las hojas es un diseño de ingeniería de la naturaleza!</p>",
              "¿Qué hoja se secó antes? ¿Por qué?", extra=f'<div class="fig" style="margin:0">{I.punta_goteo()}</div>', n_lineas=2)

L.pagina(f'''
{chip("Capítulo 6 · Actividades")}
<h2>Mi diario de campo tropical</h2>
<p>No hace falta ir a la Amazonía: busca plantas tropicales en un parque, un jardín botánico, un vivero o incluso en las macetas de tu casa (¡muchas plantas de interior vienen de la selva!).</p>
<div class="cols" style="gap:0.2in">
<div><p><strong>Fecha:</strong> ___________________</p><p><strong>Lugar:</strong> ___________________</p><p><strong>Nombre de la planta:</strong> ___________________</p></div>
<div><p><strong>¿Qué inventos tiene?</strong> (marca)</p><p class="small">☐ Punta de goteo &nbsp; ☐ Hojas gigantes<br>☐ Trepadora &nbsp; ☐ Vive sobre otra planta<br>☐ Raíces grandes &nbsp; ☐ Flores de colores</p></div>
</div>
<div class="cols" style="gap:0.2in;margin-top:0.1in">
<div><h4>Dibuja la planta entera</h4><div class="marco" style="height:2.8in"></div></div>
<div><h4>Dibuja una hoja de cerca</h4><div class="marco" style="height:2.8in"></div></div>
</div>
<h4 style="margin-top:0.18in">¿En qué piso de la selva crees que viviría? ¿Por qué?</h4>
{lineas(3)}
''', "c-verde")

# ═════════════ CAP 7: SEÑALES ═════════════
L.apertura(7, "Señales en la selva", "Bajo los árboles nadie te ve desde el aire. ¡Haz que te oigan y te encuentren!", "c-azul",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("📣", 170)}</div>',
           ["Saber dónde colocarte para que te vean.", "Usar el humo y el sonido como señales.",
            "Construir un teléfono de vasos y cuerda.", "Descifrar un mensaje secreto."],
           "<p>El sonido viaja por el aire a unos 340 metros por segundo, ¡pero por la madera viaja más de <strong>10 veces más rápido</strong>! Por eso golpear un tronco se oye tan lejos.</p>")

L.pagina(f'''
{chip("Capítulo 7 · Señales")}
<h2>Que te encuentren en la selva</h2>
<p>En el Libro 1 aprendiste las señales universales de auxilio: <strong>tres de cualquier cosa</strong>, SOS, la V y la X en el suelo. En la selva siguen valiendo, pero hay un problema: <strong>el dosel tapa todo</strong> y desde un avión o un helicóptero no se ve lo que hay debajo.</p>
<h3>Sal a la luz</h3>
<div class="cols small">
<div><p><strong>🏞️ Claros del bosque:</strong> donde cayó un árbol grande, se abre un hueco en el techo verde.</p><p><strong>🌊 Orillas de ríos:</strong> los ríos son «carreteras» abiertas: ahí te ven desde el aire y desde las canoas.</p></div>
<div><p><strong>🟧 Colores brillantes:</strong> extiende ropa, una lona o un chaleco de colores que no existan en la selva (naranja, rojo, blanco).</p><p><strong>🪨 Playas de arena:</strong> en las curvas de los ríos se forman playitas donde puedes hacer letras grandes.</p></div>
</div>
<h3>Humo: día y noche</h3>
<p class="small">De día, el <strong>humo blanco</strong> se ve mejor contra el verde oscuro de la selva: se consigue echando hojas verdes sobre un fuego que ya esté fuerte (siempre un adulto). De noche, lo que se ve es la <strong>luz de las llamas</strong>.</p>
<h3>Sonido: el mejor aliado bajo los árboles</h3>
<div class="cols small">
<div><p><strong>📣 Silbato:</strong> tres silbidos, pausa, y repetir. El sonido agudo atraviesa la vegetación mejor que la voz.</p></div>
<div><p><strong>🌳 Golpear raíces tabulares:</strong> en la selva se golpean las enormes raíces de tabla con un palo: ¡suenan como un tambor gigante!</p></div>
</div>
{ciencia("<p>El sonido son <strong>vibraciones</strong> que viajan de molécula en molécula. En los sólidos, las moléculas están muy juntas y pasan la vibración más rápido y con menos pérdida que en el aire. Las raíces tabulares, delgadas y anchas, vibran como la piel de un tambor y empujan mucho aire a la vez.</p>")}
''', "c-azul")

L.experimento("Teléfono de vasos", "c-azul", "20 minutos", "fácil",
              ["2 vasos de papel o de plástico", "5 a 10 metros de hilo o cordel delgado", "1 clip o palillo", "1 lápiz para hacer agujeros (con un adulto)"],
              ["Haz un agujerito en el centro del fondo de cada vaso.",
               "Pasa el hilo por el agujero de cada vaso y átalo por dentro a un trocito de palillo o clip para que no se salga.",
               "Cada persona toma un vaso y se alejan hasta que el hilo quede <strong>bien tenso</strong>.",
               "Uno habla dentro del vaso y el otro pone el vaso en la oreja. ¡Túrnense!",
               "Prueben: ¿qué pasa si el hilo está flojo? ¿Y si alguien lo pellizca con los dedos?"],
              "<p>Tu voz hace vibrar el fondo del vaso. Esa vibración viaja por el <strong>hilo tenso</strong> hasta el otro vaso, que vuelve a mover el aire y lo convierte en sonido. Si el hilo está flojo o alguien lo pellizca, la vibración se pierde y se deja de oír. Es la misma idea por la que el sonido viaja tan bien por los sólidos, como la madera de las raíces tabulares.</p>",
              "¿Hasta qué distancia pudieron oírse? ¿Qué pasó con el hilo flojo?", n_lineas=3)

clave = {ch: i + 1 for i, ch in enumerate("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")}
MENSAJE = "BUSCA UN CLARO"
codigo = " / ".join(" - ".join(str(clave[ch]) for ch in pal) for pal in MENSAJE.split())
tabla_c = "".join(f'<div style="border:1.5px solid var(--linea);border-radius:8px;padding:3px 0;text-align:center"><strong style="font-family:Fredoka">{k}</strong><br><span style="font-size:10pt">{v}</span></div>' for k, v in clave.items())
casillas = "".join('<span style="display:inline-block;width:0.3in;height:0.36in;border-bottom:2px solid var(--tinta);margin:0 2px"></span>' if ch != " " else '<span style="display:inline-block;width:0.25in"></span>' for ch in MENSAJE)
L.pagina(f'''
{chip("Capítulo 7 · Actividades")}
<h2>El código de la selva</h2>
<p>Los exploradores usan códigos secretos para enviarse mensajes. En este código, cada letra se cambia por su número de orden en el alfabeto:</p>
<div style="display:grid;grid-template-columns:repeat(9,1fr);gap:4px;margin:0.12in 0 0.18in">{tabla_c}</div>
<h3>Descifra el mensaje del guía</h3>
<p>Es el mejor consejo para que te encuentren si te pierdes en la selva:</p>
<p style="font-size:15pt;font-weight:800;text-align:center;margin:0.1in 0;font-family:Fredoka">{codigo}</p>
<p class="center" style="margin:0.15in 0">{casillas}</p>
<h3>Ahora tú: escribe un mensaje en código</h3>
{lineas(2)}
{reto("<p>Inventa tu propio código secreto con un amigo o un familiar (por ejemplo, cambiando cada letra por la siguiente del alfabeto) y envíense mensajes con el teléfono de vasos. ☐ ¡Reto completado!</p>")}
<h3>¿Qué señal usarías?</h3>
<p class="small">Escribe la mejor señal para cada caso: a) Oyes un helicóptero sobre el dosel. b) Es de noche. c) Estás junto a un río con playa de arena.</p>
{lineas(2)}
''', "c-azul")

# ═════════════ GRAN FINAL ═════════════
L.sopa(["SELVA", "DOSEL", "LIANA", "CEIBA", "JAGUAR", "LORO", "RANA", "HAMACA", "LLUVIA", "CUENCA", "RIO", "MOSQUITO", "BROMELIA", "SILBATO", "CAIMAN"], "c-verde", semilla=9)
L.crucigrama([("CAMUFLAJE", "Tener el color de tu hogar para esconderte."),
              ("CAPILARIDAD", "El agua sube por los huequitos del papel y del algodón."),
              ("MOSQUITERO", "Red para dormir sin picaduras."),
              ("EPIFITA", "Planta que vive sobre otra sin ser parásita."),
              ("PLUVIOMETRO", "Instrumento para medir la lluvia."),
              ("DOSEL", "El «techo» verde de copas de la selva."),
              ("CUENCA", "Todo el terreno que envía su agua a un mismo río."),
              ("HAMACA", "Donde duermen los exploradores, lejos del suelo."),
              ("CEIBA", "Árbol gigante, sagrado para los mayas."),
              ("QUINA", "Árbol cuya corteza curaba la malaria."),
              ("JAGUAR", "Felino tímido con manchas."),
              ("RANA", "Las de dardo avisan con colores brillantes.")], "c-naranja", "Crucigrama de la selva")
L.mochila_examen(["Silbato", "Agua segura en botella", "Mosquitero y hamaca (en la expedición)", "Repelente de insectos", "Ropa ligera de manga larga",
                  "Calcetines de repuesto en bolsa cerrada", "Sombrero o gorra", "Capa impermeable", "Brújula y mapa", "Linterna", "Botiquín pequeño",
                  "Yesca seca en bolsa cerrada", "Cinta de colores para marcar el camino", "Snacks energéticos"],
                 [("En la selva, el animal más peligroso para las personas suele ser…", ["el jaguar", "el mosquito", "el mono"]),
                  ("Si te pierdes, un buen lugar para que te encuentren es…", ["bajo el dosel", "un claro o la orilla de un río", "dentro de un tronco"]),
                  ("La humedad hace sentir más calor porque…", ["el sudor se evapora despacio", "el aire pesa más", "hay más sol"]),
                  ("Una rana de colores brillantes probablemente…", ["es venenosa", "es amigable", "está enferma"]),
                  ("La madera mojada no arde bien porque…", ["el calor se gasta en evaporar el agua", "no tiene oxígeno", "es muy dura"]),
                  ("Las puntas de goteo sirven para…", ["pinchar a los animales", "escurrir la lluvia", "atrapar insectos"]),
                  ("Para cruzar un río poco profundo con un adulto, conviene…", ["saltar", "arrastrar los pies", "correr"]),
                  ("El agua de lluvia que recoges en la selva…", ["se puede beber tal cual", "hay que hervirla", "es salada"])],
                 "En la selva, un buen explorador lleva lo justo y lo mantiene seco. Marca lo que llevas:", "c-verde")
L.soluciones([
    ("Cap. 1 · Orientación", "Mono: E3 · Loro: C5 · Rana: D7 · Refugio: H4 · Caimán: A7 · Ceiba: F2. Camino más corto de B2 a G6 sin diagonales: 5 columnas + 4 filas = 9 casillas."),
    ("Cap. 2 · Agua", "V/F: a) F, b) V, c) V, d) F, e) V, f) V. Problema: a) 80 mm; b) 80 litros; c) 1 600 litros."),
    ("Cap. 3 · Seco y sano", "a) Secar los pies y cambiarse a calcetines secos. b) Beber agua, descansar a la sombra y avisar a un adulto. c) Ponerse manga larga, repelente y entrar al mosquitero. d) Sacudirlas antes de ponérselas. Criaderos: cubeta, llanta, platito de maceta y cáscara de coco (sí); río que corre y ducha que se seca (no)."),
    ("Cap. 4 · Fuego", "Orden sugerido: 1 fibra de coco seca, 2 ramitas secadas junto al fuego, 3 rama muerta colgada del árbol, 4 tronco verde, 5 rama en el charco (4 y 5 pueden variar). Frases: a) blanco, b) energía (calor), c) mosquitos, d) hervirla. Piensa: el agua absorbe el calor del fondo de la olla y no deja que se caliente tanto como para quemarse."),
    ("Cap. 5 · Animales", "1-d, 2-a, 3-e, 4-c, 5-b."),
    ("Cap. 7 · Señales", "Mensaje: <strong>BUSCA UN CLARO</strong>. a) Ir a un claro o al río, colores brillantes, silbato. b) Luz del fuego o linterna, tres destellos. c) Letras grandes (SOS, V o X) en la arena."),
    ("Gran examen", "1-b, 2-b, 3-a, 4-a, 5-a, 6-b, 7-b, 8-b."),
    ("Para colorear", "Una hamaca con mosquitero entre dos árboles, un techo de hojas grandes, un recolector de lluvia… ¡y un adulto guía!"),
])
L.soluciones_pasatiempos()
L.glosario([("Aposematismo", "Colores brillantes que avisan que un animal es venenoso o peligroso."),
            ("Camuflaje", "Parecerse al entorno para pasar desapercibido."),
            ("Capacidad calorífica", "Cantidad de calor que puede absorber una sustancia. La del agua es muy grande."),
            ("Capilaridad", "Cuando el agua sube por espacios diminutos, como los del papel o las raíces."),
            ("Cuenca", "Territorio cuyas aguas van a parar a un mismo río."),
            ("Dosel", "Capa de copas de árboles que forma el «techo» de la selva."),
            ("Epífita", "Planta que crece sobre otra sin quitarle alimento."),
            ("Evaporación", "Cuando el agua líquida se convierte en vapor. Enfría la piel al sudar."),
            ("Humedad", "Cantidad de vapor de agua que hay en el aire."),
            ("Liana", "Planta trepadora que usa a los árboles para llegar a la luz."),
            ("Mimetismo", "Cuando un animal imita a otro, por ejemplo a uno venenoso."),
            ("Pluviómetro", "Instrumento que mide cuánta lluvia cae, en milímetros."),
            ("Raíces tabulares", "Raíces enormes con forma de tabla que sostienen a los árboles gigantes."),
            ("Ríos voladores", "Grandes corrientes de vapor de agua que salen de la selva y viajan por el aire."),
            ("Selección natural", "Proceso por el que sobreviven y tienen crías los seres mejor adaptados a su hogar."),
            ("Vibración", "Movimiento rápido de ida y vuelta. El sonido son vibraciones que viajan.")])
L.colorear(I.selva_escena(), "¿Qué necesitarías agregar a este lugar para acampar una noche seguro? Dibújalo en la escena. <em>Pista: mira el capítulo 3.</em>")
L.notas()
L.certificado("Explorador de la<br>Selva Tropical", "orientación junto a ríos, lluvia, salud en clima húmedo, fuego, animales, plantas tropicales y señales")
L.contraportada(I.selva_escena(), "¿Podrías sobrevivir en la selva?",
                ["Seguir el agua para encontrar el camino. Medir la lluvia de la selva. Descubrir por qué la humedad da más calor. Hacer que un globo no explote sobre una llama. Encontrar animales camuflados y descifrar códigos secretos.",
                 "El Libro 2 de la serie te lleva al ecosistema con más vida del planeta, con ciencia real, experimentos con materiales de casa, pasatiempos y un certificado de explorador."],
                "#1d5a36")
L.construir([("Bienvenido a la selva", "Bienvenida y lo que ya sabes", False), ("Las 8 reglas de oro de la selva", "Reglas de oro y los pisos de la selva", False),
             ("Sopa de letras del explorador", "Gran final: pasatiempos y examen", True), ("<h2>Soluciones</h2>", "Soluciones y glosario", True),
             ("CERTIFICADO OFICIAL", "Tu certificado de explorador", True)])
from mejorar import mejorar; mejorar("libro_selva.html", 2)
