"""Libro 3 de la serie: ¡Sobrevive en la Isla! Ejecuta: python3 build_isla.py"""
import ilustraciones as I
from comun import (Libro, lineas, caja, ciencia, seguridad, sabias, reto, mito, chip, emoji, pasos, tarjetas,
                   vf_tabla, unir)

ALAMBIQUE = I.alambique_bol().replace('width="460" height="250"', 'width="330" height="179"', 1)
RESACA = I.corriente_resaca().replace('width="560" height="280"', 'width="440" height="220"', 1)
L = Libro(3, "¡Sobrevive en la Isla!", "Ciencia y supervivencia en la costa y el mar", "libro_isla.html")

# ─────────────── INICIO ───────────────
L.portada(I.isla_escena(), "☀️ Sol · 💧 Agua · 🌊 Mareas · 🏖️ Refugio · ⛵ Navegar · 🦀 Vida marina · 🆘 Señales",
          fondo_cielo="linear-gradient(#a9dcf5,#dff2fb)", color_titulo="#135a86")
L.propiedad(emoji("🏝️", 120))
L.reservar_indice()

L.pagina(f'''
{chip("Antes de empezar")}
<h2>Bienvenido a la isla</h2>
<p>¡Hola otra vez, explorador o exploradora! Ya sobreviviste al bosque (Libro 1) y a la selva (Libro 2). Ahora llegamos a la última aventura de la serie: una <strong>isla rodeada de mar</strong>. Hay agua por todas partes… ¡pero no se puede beber! Hay sol de sobra… ¡y puede ser peligroso!</p>
<p>En esta isla vas a descubrir la ciencia del mar: por qué es salado, por qué sube y baja, cómo se orientaban los navegantes sin brújula y cómo lograr que te vean desde un barco.</p>
<h3>Lo que ya sabes (de los Libros 1 y 2)</h3>
{tarjetas([("🛑", "S.T.O.P.", "Detente, piensa, observa y planea."),
           ("💧", "Agua segura", "El agua natural se hierve; ahora aprenderás a quitarle la sal."),
           ("🔥", "Fuego responsable", "Un adulto lo enciende, lo cuida y lo apaga por completo."),
           ("🦟", "Protégete", "De insectos, del calor y de la deshidratación."),
           ("📣", "Tres = auxilio", "Tres silbidos, tres destellos, tres fuegos."),
           ("🔢", "Coordenadas y códigos", "¡Los usarás para encontrar un tesoro!")])}
<p>Como siempre, busca: 🔬 <strong>La ciencia detrás</strong>, 🧪 <strong>Experimento</strong>, ⚠️ <strong>Seguridad</strong>, 💡 <strong>¿Sabías que…?</strong>, 🤔 <strong>¿Mito o realidad?</strong> y 🏅 <strong>Reto de explorador</strong>.</p>
{caja("sabias", "👨‍👩‍👧 Nota para madres, padres y docentes", "<p>Este libro enseña ciencia del mar y la costa a través de la supervivencia, para leer y practicar <strong>en familia</strong>. Las actividades en la playa o en el agua requieren siempre la supervisión de un adulto y el respeto de las indicaciones de los socorristas. Las soluciones están al final.</p>")}
''', "c-azul")

L.pagina(f'''
{chip("Lo más importante")}
<h2>Las 8 reglas de oro de la costa</h2>
{pasos(["<strong>Nunca entres al mar sin un adulto</strong> que te esté mirando, y báñate solo en playas con socorristas y banderas.",
        "<strong>Respeta las banderas:</strong> verde = se puede nadar con precaución, amarilla = mucho cuidado, roja = prohibido bañarse.",
        "<strong>Protégete del sol:</strong> sombrero, camiseta, gafas de sol y protector solar, que se renueva a menudo.",
        "<strong>Bebe agua dulce con frecuencia.</strong> Nunca bebas agua de mar.",
        "<strong>Usa calzado</strong> al caminar sobre rocas, arrecifes y en el agua: hay erizos, conchas cortantes y corales.",
        "<strong>Mira, pero no toques</strong> animales marinos: medusas, erizos, corales y peces pueden picar o lastimarse.",
        "<strong>Vigila la marea:</strong> el mar sube y puede dejarte aislado en una roca o un banco de arena.",
        "<strong>No dejes rastro:</strong> llévate tu basura. El plástico en el mar dura cientos de años."], "var(--rojo)")}
{seguridad("<p>Si ves a alguien en apuros en el agua, <strong>no te lances a rescatarlo</strong>: grita pidiendo ayuda a un adulto o a un socorrista y lánzale algo que flote (una pelota, una tabla, una nevera vacía). ¡Así ayudas sin ponerte en peligro!</p>", "⚠️ Recuerda")}
''', "c-rojo")

isla_zonas = [("🌊", "El mar", "Agua salada, olas y corrientes. Alimento, pero también peligros."),
              ("〰️", "Línea de marea alta", "La marca de algas y conchas secas: hasta ahí llega el agua. ¡Acampa más arriba!"),
              ("🏖️", "La playa", "Arena caliente de día y fresca de noche. Buen lugar para hacer señales."),
              ("🌴", "Palmeras y matorral", "Sombra, hojas para techos y cocos… ¡cuidado al sentarte debajo!"),
              ("🪨", "Rocas y pozas", "Cuando baja la marea aparecen pozas llenas de vida."),
              ("⛰️", "Colina", "Un buen mirador para vigilar barcos y hacer señales de fuego.")]
L.pagina(f'''
{chip("Conoce la isla")}
<h2>Llegaste a una isla: ¿qué hago primero?</h2>
<p>Recuerda la <strong>regla de los 3</strong> del Libro 1. En una isla tropical, el orden de prioridades suele ser:</p>
<div class="cols-4 center" style="margin:0.1in 0 0.18in">
<div style="background:var(--naranja-claro);border-radius:14px;padding:0.12in"><div style="font-size:28px">⛱️</div><strong>1. Sombra</strong><p class="tiny" style="margin:0">El sol es el peligro más rápido.</p></div>
<div style="background:var(--azul-claro);border-radius:14px;padding:0.12in"><div style="font-size:28px">💧</div><strong>2. Agua dulce</strong><p class="tiny" style="margin:0">Con calor, se necesita mucha.</p></div>
<div style="background:var(--verde-claro);border-radius:14px;padding:0.12in"><div style="font-size:28px">🆘</div><strong>3. Señales</strong><p class="tiny" style="margin:0">Que te vean desde el mar y el aire.</p></div>
<div style="background:#f1e6da;border-radius:14px;padding:0.12in"><div style="font-size:28px">🥥</div><strong>4. Comida</strong><p class="tiny" style="margin:0">Puede esperar más de lo que crees.</p></div>
</div>
<h3>Las zonas de una isla</h3>
{tarjetas(isla_zonas, 2)}
{sabias("<p>Hay más de <strong>100 000 islas</strong> en el mundo. Algunas son volcanes que salieron del fondo del mar, como las Galápagos o Hawái; otras las construyeron los <strong>corales</strong> durante miles de años, ¡como muchas islas del Caribe!</p>")}
''', "c-azul")

# ═════════════ CAP 1: SOL Y CALOR ═════════════
L.apertura(1, "Sol y calor", "En la playa, el sol es tu amigo… y tu mayor peligro.", "c-naranja",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("☀️", 170)}</div>',
           ["Descubrir la luz invisible del sol: los rayos ultravioleta.", "Entender por qué la arena y el agua aumentan las quemaduras.",
            "Reconocer las señales de alarma del calor.", "Comprobar qué colores se calientan más.", "Diseñar tu kit anti-sol."],
           "<p>La luz del sol tarda unos <strong>8 minutos</strong> en llegar a la Tierra. ¡La luz que ves ahora salió del sol cuando empezaste a leer esta página!</p>")

L.pagina(f'''
{chip("Capítulo 1 · Sol")}
<h2>La luz que no se ve</h2>
<p>La luz del sol parece blanca, pero está formada por muchos tipos de luz. Algunos los vemos (los colores del arcoíris) y otros son <strong>invisibles</strong>:</p>
{tarjetas([("🌡️", "Infrarroja", "No la vemos, pero la sentimos como calor en la piel."),
           ("🌈", "Visible", "Los colores del arcoíris: rojo, naranja, amarillo, verde, azul y violeta."),
           ("🟣", "Ultravioleta (UV)", "Invisible y con mucha energía. Es la que quema la piel y daña los ojos.")])}
{ciencia("<p>Los rayos <strong>ultravioleta</strong> tienen tanta energía que pueden dañar las células de la piel. La piel se defiende fabricando más <strong>melanina</strong>, un pigmento oscuro (por eso nos bronceamos), pero si recibe demasiado UV, se quema. En la playa hay aún más UV porque <strong>la arena, el agua y la espuma lo reflejan</strong> hacia ti. ¡Por eso puedes quemarte incluso bajo una sombrilla!</p>")}
<h3>¿Cuándo es más fuerte el sol?</h3>
<p>Aproximadamente entre las <strong>10 de la mañana y las 4 de la tarde</strong>, cuando el sol está alto. Truco del explorador: <strong>la regla de la sombra</strong>. Si tu sombra es <strong>más corta que tú</strong>, el sol está alto y los rayos UV son muy fuertes: ¡busca sombra!</p>
{mito("<p><strong>«Si está nublado, no me quemo».</strong> ¡Falso! Muchos rayos UV atraviesan las nubes. En días nublados de playa la gente se quema a menudo porque no siente tanto calor y se confía.</p>")}
{mito("<p><strong>«Con protector solar puedo estar todo el día al sol».</strong> ¡Tampoco! El protector se va con el agua y el sudor: hay que <strong>volver a ponerlo cada 2 horas</strong> y después de bañarse, y usarlo junto con sombrero, camiseta y sombra.</p>")}
''', "c-naranja")

L.pagina(f'''
{chip("Capítulo 1 · Calor")}
<h2>Cuando el cuerpo se calienta demasiado</h2>
<p>Tu cuerpo funciona bien a unos 37 °C. En la playa, entre el sol, la arena caliente y el ejercicio, puede calentarse demasiado. Aprende a reconocer las señales de alarma:</p>
<table>
<tr><th style="width:1.8in">Señal</th><th>Qué hacer</th></tr>
<tr><td>😓 Mucha sed, cansancio, dolor de cabeza</td><td>Ir a la sombra, beber agua a sorbos y descansar.</td></tr>
<tr><td>🥵 Mareo, náuseas, piel fría y pegajosa, calambres</td><td><strong>Avisar a un adulto.</strong> Acostarse a la sombra con los pies elevados, refrescar la piel con agua y beber a sorbitos.</td></tr>
<tr><td>🚨 Confusión, piel muy caliente, desmayo</td><td><strong>¡Emergencia!</strong> Un adulto debe pedir ayuda médica de inmediato y enfriar a la persona con agua.</td></tr>
</table>
<h3 style="margin-top:0.15in">Cómo se protegen los exploradores de costa</h3>
<div class="cols small">
<ul><li><strong>Sombra primero:</strong> palmeras, rocas, una lona o ropa colgada entre dos palos.</li>
<li><strong>Moverse temprano y tarde:</strong> las tareas pesadas, cuando el sol está bajo.</li>
<li><strong>Ropa amplia y clara</strong> que cubra brazos y piernas.</li></ul>
<ul><li><strong>Sombrero de ala ancha</strong> y gafas de sol: protegen cara, cuello y ojos.</li>
<li><strong>Mojar la ropa</strong> con agua de mar refresca al evaporarse (¡el enfriamiento por evaporación del Libro 2!).</li>
<li><strong>Nunca camines descalzo</strong> por arena muy caliente: puede quemar las plantas de los pies.</li></ul>
</div>
{sabias("<p>Los animales del desierto y de la playa también buscan la sombra: los <strong>cangrejos</strong> se esconden en sus cuevas en la arena en las horas de más calor y salen al atardecer. ¡Imítalos!</p>")}
''', "c-naranja")

L.experimento("¿Qué color se calienta más?", "c-naranja", "40 minutos", "fácil",
              ["2 vasos o frascos iguales", "Papel negro y papel blanco (o tela)", "Cinta adhesiva y ligas", "Agua a la misma temperatura", "1 termómetro (o tu dedo)", "Un lugar soleado"],
              ["Forra un vaso con papel negro y el otro con papel blanco.",
               "Llénalos con la misma cantidad de agua del grifo.",
               "Ponlos al sol, uno al lado del otro, durante 30 minutos.",
               "Mide la temperatura del agua de cada uno (o tócala con el dedo).",
               "Anota los resultados. ¿Qué color de camiseta te pondrías en la playa?"],
              "<p>Los colores oscuros <strong>absorben</strong> casi toda la luz que les llega y la convierten en calor. Los colores claros <strong>reflejan</strong> gran parte de la luz, así que se calientan menos. Los científicos llaman <strong>albedo</strong> a la capacidad de reflejar la luz: la nieve y la arena blanca tienen mucho albedo; el asfalto y el mar oscuro, poco.</p>",
              "Anota tus resultados:",
              resultados='<table><tr><th>Vaso</th><th>Temperatura al inicio</th><th>Temperatura a los 30 min</th></tr><tr><td style="height:0.36in">Negro</td><td></td><td></td></tr><tr><td style="height:0.36in">Blanco</td><td></td><td></td></tr></table>',
              n_lineas=1)

L.pagina(f'''
{chip("Capítulo 1 · Actividades")}
<h2>Tu kit anti-sol</h2>
<h3>1. ¿Verdadero o falso?</h3>
{vf_tabla(["Los rayos ultravioleta no se ven, pero pueden quemar la piel.",
           "En días nublados no hace falta protegerse del sol.",
           "La arena y el agua reflejan los rayos UV hacia nosotros.",
           "Si tu sombra es más corta que tú, el sol está muy fuerte.",
           "El protector solar dura todo el día, aunque te bañes.",
           "La ropa oscura se calienta más al sol que la clara."])}
<h3 style="margin-top:0.18in">2. Viste al explorador de playa</h3>
<p class="small">Dibuja a un explorador bien protegido del sol. Señala con flechas: sombrero, gafas, camiseta, protector solar, calzado y botella de agua.</p>
<div class="marco" style="height:3.4in"></div>
<h3 style="margin-top:0.15in">3. Mide tu sombra</h3>
<p class="small">Un día soleado, con un adulto, mide tu sombra a tres horas distintas (con pasos o con cinta métrica):</p>
<p>9:00 → ________ &nbsp;&nbsp; 12:00 → ________ &nbsp;&nbsp; 17:00 → ________ &nbsp;&nbsp; ¿A qué hora fue más corta? ________</p>
''', "c-naranja")

# ═════════════ CAP 2: AGUA DULCE ═════════════
L.apertura(2, "Agua dulce", "Agua, agua por todas partes… y ni una gota para beber.", "c-azul",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("🥥", 170)}</div>',
           ["Descubrir por qué el mar es salado.", "Entender por qué el agua de mar da más sed.",
            "Quitarle la sal al agua con la energía del sol.", "Ver la ósmosis con una papa.", "Conocer las fuentes de agua dulce de una isla."],
           "<p>Si se evaporara toda el agua de los océanos, la sal que queda cubriría todos los continentes con una capa de más de <strong>100 metros de alto</strong>. ¡Como un edificio de 30 pisos de sal!</p>")

L.pagina(f'''
{chip("Capítulo 2 · Agua dulce")}
<h2>¿Por qué no se puede beber el agua del mar?</h2>
<p>El agua de mar tiene unos <strong>35 gramos de sal por cada litro</strong>: es como disolver 7 cucharaditas de sal en una botella de agua. ¿De dónde sale tanta sal? Durante millones de años, la lluvia y los ríos han ido disolviendo minerales de las rocas y llevándolos al mar. El agua se evapora, pero la sal se queda… y se va acumulando.</p>
{ciencia("<p>Tus <strong>riñones</strong> limpian la sangre y eliminan lo que sobra en la orina. Pero no pueden fabricar una orina tan salada como el agua de mar. Para deshacerse de la sal de un vaso de agua de mar, ¡necesitan usar <strong>más agua</strong> de la que ese vaso te dio! Así que beber agua de mar te <strong>deshidrata</strong> más rápido. Por eso los náufragos dicen que es lo peor que se puede hacer.</p>")}
<h3>Fuentes de agua dulce en una isla</h3>
{tarjetas([("🌧️", "Lluvia", "La mejor fuente. Se recoge con lonas, hojas de palma o conchas grandes."),
           ("🥥", "Cocos verdes", "Tienen un agua dulce y limpia en su interior. Un adulto los abre con cuidado."),
           ("☀️", "Destilación solar", "El sol puede separar el agua de la sal. ¡Lo harás en el experimento!"),
           ("💦", "Rocío", "Al amanecer se condensa sobre hojas, lonas y rocas: se recoge con un paño."),
           ("⛰️", "Arroyos y manantiales", "Algunas islas grandes tienen agua dulce en el interior (hay que hervirla)."),
           ("🕳️", "Pozos tras la duna", "En algunas islas, el agua de lluvia flota sobre la salada bajo la arena. Solo los expertos saben dónde cavar.")], 2)}
{seguridad("<p>El agua de coco es un buen recurso, pero no hay que abusar: tomada en grandes cantidades puede dar dolor de estómago. Y recuerda: los cocos deben abrirlos los adultos, porque se usan herramientas cortantes.</p>")}
''', "c-azul")

L.experimento("Quítale la sal al agua", "c-azul", "3 a 6 horas al sol", "media",
              ["1 bol grande", "1 vaso pequeño y pesado (más bajo que el bol)", "Agua del grifo y 2 cucharadas de sal", "Film plástico para cocina", "1 piedrita o moneda", "Un día de sol"],
              ["Disuelve la sal en agua y viértela en el bol hasta unos 3 cm de altura.",
               "Coloca el vaso vacío en el centro del bol. El agua salada no debe entrar en él.",
               "Tapa el bol con el film, bien estirado y sin agujeros.",
               "Pon la piedrita encima del film, justo sobre el vaso, para que el plástico forme una «V».",
               "Deja el bol al sol varias horas. Luego quita el film con cuidado y prueba una gota del agua del vaso."],
              "<p>El sol calienta el agua salada y una parte se <strong>evapora</strong>. Pero la sal no se evapora: se queda en el bol. El vapor sube, choca con el plástico más fresco, se <strong>condensa</strong> en gotitas y, gracias a la piedra, escurre hasta el vaso. ¡Obtienes agua sin sal! Es la <strong>destilación</strong>: el ciclo del agua del Libro 1 en miniatura.</p>",
              "¿Cómo sabía el agua del vaso? ¿Cuánta obtuviste?", extra=f'<div class="fig" style="margin:0">{ALAMBIQUE}</div>',
              seg=seguridad("<p>Prueba solo una gota, y solo si usaste agua del grifo y recipientes limpios de tu cocina.</p>"), n_lineas=1)

L.experimento("La papa sedienta", "c-azul", "40 minutos", "fácil",
              ["1 papa (patata) cruda", "2 vasos", "Agua del grifo", "3 cucharadas de sal", "1 cuchillo (¡solo el adulto!)"],
              ["El adulto corta dos rodajas de papa del mismo grosor.",
               "Llena los dos vasos con agua. En uno, disuelve la sal.",
               "Pon una rodaja en cada vaso y espera 30 minutos.",
               "Saca las rodajas y dóblalas con cuidado. ¿Cuál está firme? ¿Cuál está blanda y flexible?"],
              "<p>Las células de la papa tienen agua dentro y están rodeadas por una capa muy fina, la <strong>membrana</strong>, que deja pasar el agua. El agua siempre tiende a moverse hacia donde hay <strong>más sal</strong> para igualar las concentraciones. Esto se llama <strong>ósmosis</strong>. En el vaso salado, el agua sale de las células de la papa y la rodaja queda blanda. ¡Algo parecido pasaría en tu cuerpo si bebieras agua de mar: tus células perderían agua!</p>",
              "Dibuja cómo quedaron las dos rodajas:",
              resultados='<div class="cols"><div class="marco" style="height:1.5in;padding:6px" ><span class="small">Agua dulce</span></div><div class="marco" style="height:1.5in;padding:6px"><span class="small">Agua salada</span></div></div>',
              n_lineas=0)

L.pagina(f'''
{chip("Capítulo 2 · Actividades")}
<h2>¡Pon a prueba tu sed de saber!</h2>
<h3>1. Ordena la destilación solar</h3>
<p>Numera del 1 al 4:</p>
<div class="cols-4 center" style="margin-bottom:0.2in">
<div class="marco" style="padding:0.12in">☐<br>El vapor se condensa en el plástico</div><div class="marco" style="padding:0.12in">☐<br>El sol calienta el agua salada</div>
<div class="marco" style="padding:0.12in">☐<br>Las gotas escurren al vaso</div><div class="marco" style="padding:0.12in">☐<br>El agua se evapora y la sal se queda</div>
</div>
<h3>2. Cálculos salados</h3>
<p>El agua de mar tiene unos 35 gramos de sal por litro.</p>
<p>a) ¿Cuánta sal hay en 2 litros de agua de mar? ______ g</p>
<p>b) ¿Y en un balde de 10 litros? ______ g</p>
<p>c) Si evaporas medio litro, ¿cuánta sal queda en el fondo? ______ g</p>
<h3 style="margin-top:0.18in">3. ¿Qué harías?</h3>
<p>Estás en una isla, tienes mucha sed y solo ves el mar, algunas palmeras con cocos, una lona y un día muy soleado. Escribe tu plan para conseguir agua dulce, paso a paso:</p>
{lineas(5)}
{sabias("<p>Los <strong>albatros</strong> y otras aves marinas sí pueden beber agua de mar: tienen unas glándulas especiales encima de los ojos que eliminan la sal. ¡Por eso a veces parece que les gotea la nariz!</p>")}
''', "c-azul")

# ═════════════ CAP 3: MAREAS Y OLAS ═════════════
L.apertura(3, "Mareas y olas", "El mar respira: sube y baja dos veces al día.", "c-turquesa",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("🌊", 170)}</div>',
           ["Descubrir cómo la Luna mueve el mar.", "Leer una tabla de mareas.",
            "Reconocer y escapar de una corriente de resaca.", "Hacer flotar un huevo con ciencia."],
           "<p>En la <strong>bahía de Fundy</strong>, en Canadá, la diferencia entre la marea alta y la baja puede superar los <strong>15 metros</strong>: ¡la altura de un edificio de 5 pisos!</p>")

L.pagina(f'''
{chip("Capítulo 3 · Mareas")}
<h2>La Luna tira del mar</h2>
<div class="fig">{I.mareas()}</div>
{ciencia("<p>La <strong>gravedad</strong> de la Luna atrae a toda la Tierra, pero el agua, que puede moverse, se estira hacia ella formando un «bulto». Del lado contrario se forma otro bulto. Mientras la Tierra gira, cada playa pasa por los dos bultos (<strong>marea alta</strong>) y por las zonas entre ellos (<strong>marea baja</strong>). Por eso en la mayoría de las costas hay dos mareas altas y dos bajas cada día, y cada día llegan unos <strong>50 minutos más tarde</strong>. El Sol también ayuda: con luna llena y luna nueva, las mareas son más grandes (<strong>mareas vivas</strong>).</p>")}
<h2 style="margin-top:0.1in">Corrientes de resaca: cómo escapar</h2>
<div class="fig">{RESACA}</div>
<div class="cols small">
<p>Una <strong>corriente de resaca</strong> es un «río» de agua que vuelve de la playa hacia mar adentro. Se reconoce porque ahí <strong>no rompen olas</strong>, el agua se ve más oscura o arrastra espuma y arena.</p>
<p><strong>Si te atrapa:</strong> ¡no nades contra ella! 1) Mantén la calma y <strong>flota</strong>. 2) Nada <strong>paralelo a la orilla</strong> hasta salir de la corriente. 3) Luego nada hacia la playa. 4) Si no puedes, flota y levanta el brazo para pedir ayuda.</p>
</div>
''', "c-turquesa")

L.experimento("El huevo que flota", "c-turquesa", "15 minutos", "fácil",
              ["1 huevo crudo", "1 vaso alto o un frasco", "Agua del grifo", "Sal (unas 6 cucharadas)", "1 cuchara"],
              ["Llena el vaso con agua hasta la mitad y mete el huevo con cuidado. ¿Flota o se hunde?",
               "Saca el huevo. Añade sal cucharada a cucharada, removiendo hasta que se disuelva.",
               "Vuelve a meter el huevo después de cada 2 cucharadas. ¿Cuándo empieza a flotar?",
               "Reto: añade con mucho cuidado agua sin sal por encima, despacio por la cuchara. ¡Puedes lograr que el huevo quede flotando en medio del vaso!"],
              "<p>Un objeto flota si es menos <strong>denso</strong> que el líquido que lo rodea. La densidad es cuánta materia hay en un espacio. Al disolver sal, el agua se vuelve más densa y empuja con más fuerza hacia arriba. ¡Por eso flotamos más fácil en el mar que en una piscina! En el <strong>mar Muerto</strong>, que es casi diez veces más salado que el océano, las personas flotan como corchos.</p>",
              "¿Cuántas cucharadas de sal hicieron falta?", n_lineas=2)

L.pagina(f'''
{chip("Capítulo 3 · Actividades")}
<h2>Lee la tabla de mareas</h2>
<p>Los pescadores y los exploradores de costa consultan una <strong>tabla de mareas</strong> antes de salir. Esta es la de hoy en tu isla:</p>
<table style="width:auto;margin:0.1in auto 0.2in;font-size:12pt">
<tr><th>Marea</th><th>Hora</th><th>Altura del agua</th></tr>
<tr><td>🌊 Alta</td><td>05:10</td><td>1,8 m</td></tr><tr><td>🏖️ Baja</td><td>11:20</td><td>0,3 m</td></tr>
<tr><td>🌊 Alta</td><td>17:30</td><td>1,9 m</td></tr><tr><td>🏖️ Baja</td><td>23:40</td><td>0,2 m</td></tr>
</table>
<p>a) ¿Cuál es la mejor hora para explorar las pozas de las rocas? ________</p>
<p>b) ¿A qué hora de la tarde estará el mar más alto? ________</p>
<p>c) ¿Cuántos metros sube el agua entre las 11:20 y las 17:30? ________</p>
<p>d) Mañana, ¿a qué hora aproximada será la primera marea alta? (Pista: unos 50 minutos más tarde) ________</p>
<p>e) Son las 15:00 y quieres dejar tu mochila en la arena, cerca del agua. ¿Es buena idea? ¿Por qué?</p>
{lineas(2)}
<h3>¿Verdadero o falso?</h3>
{vf_tabla(["Si te atrapa una corriente de resaca, hay que nadar con fuerza directo a la orilla.",
           "Donde hay una corriente de resaca, a veces no rompen las olas.",
           "La Luna es la principal responsable de las mareas.",
           "En el agua salada es más fácil flotar que en el agua dulce."])}
''', "c-turquesa")

# ═════════════ CAP 4: REFUGIO Y FUEGO ═════════════
L.apertura(4, "Refugio y fuego en la playa", "Un techo contra el sol y la lluvia, y un fuego que se vea desde el mar.", "c-cafe",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("⛺", 170)}</div>',
           ["Elegir un lugar seguro para acampar en la costa.", "Construir un refugio con hojas de palma.",
            "Encender fuego con materiales de playa.", "Descubrir por qué sopla la brisa del mar."],
           "<p>Las hojas de palma se han usado durante siglos para techar casas en el Caribe, Centroamérica y el Pacífico. Bien colocadas en capas, ¡pueden aguantar lluvias tropicales durante años!</p>")

L.pagina(f'''
{chip("Capítulo 4 · Refugio")}
<h2>Tu refugio en la costa</h2>
<h3>¿Dónde acampar?</h3>
<div class="cols small">
<div><p><strong style="color:var(--verde)">✔ Sí:</strong></p><ul>
<li><strong>Por encima de la línea de marea alta</strong> (la franja de algas secas y conchas).</li>
<li>Al borde de la vegetación: sombra y protección del viento.</li>
<li>Cerca de un lugar despejado para hacer señales.</li>
<li>En un terreno un poco elevado, por si llueve.</li></ul></div>
<div><p><strong style="color:var(--rojo)">✘ No:</strong></p><ul>
<li><strong>Debajo de palmeras con cocos</strong>: un coco que cae desde 20 metros es muy peligroso.</li>
<li>Bajo el <strong>manzanillo</strong> (Libro 1): su savia quema la piel.</li>
<li>En hondonadas donde se junta el agua de lluvia.</li>
<li>Junto a nidos de tortugas o de aves marinas.</li></ul></div>
</div>
<h3>El refugio de hojas de palma</h3>
{pasos(["Busca dos árboles o clava dos palos fuertes con horqueta y apoya una rama larga entre ellos (la viga, como en el cobertizo del Libro 1).",
        "Apoya varias ramas inclinadas sobre la viga, del lado de donde viene el viento.",
        "Coloca las hojas de palma <strong>de abajo hacia arriba</strong>, cada fila cubriendo la anterior, como las tejas de un techo. Así la lluvia escurre por fuera.",
        "Cubre el suelo con hojas secas de palma o hierba para no dormir sobre la arena húmeda.",
        "Deja los lados abiertos si hace calor: el aire que circula te refresca."], "var(--cafe)")}
{ciencia("<p>¿Por qué el techo en capas no deja pasar el agua? La <strong>gravedad</strong> hace que la gota resbale por la hoja inclinada; al llegar al borde, cae sobre la hoja de abajo, y así hasta el suelo. Nunca llega a pasar entre las hojas. ¡Es el mismo principio de las tejas, las escamas de los peces y las plumas de las aves!</p>")}
''', "c-cafe")

L.pagina(f'''
{chip("Capítulo 4 · Fuego")}
<h2>Fuego con lo que trae el mar</h2>
<p>El fuego en la playa sirve para hervir agua, cocinar, dar luz y, sobre todo, <strong>hacer señales</strong>. Recuerda el triángulo del fuego y ve de lo fino a lo grueso:</p>
{tarjetas([("🥥", "Yesca: fibra de coco", "La fibra seca de la cáscara del coco, deshilachada, prende muy bien."),
           ("🌴", "Astillas: hojas y ramitas secas", "Hojas secas de palma y ramitas del matorral de la playa."),
           ("🪵", "Leña: madera de deriva", "Troncos que trae el mar. Los que están arriba de la marea alta suelen estar más secos."),
           ("🔍", "Chispa o lupa", "Un adulto puede usar fósforos, un encendedor o concentrar el sol con una lupa.")], 2)}
{seguridad("<p>Enciende el fuego <strong>sobre la arena, lejos de la vegetación seca</strong>, y nunca cerca de nidos. No quemes plásticos ni basura del mar: sueltan humo tóxico. Un adulto enciende y cuida el fuego, y al terminar se apaga con agua (¡la arena sola no siempre basta: las brasas enterradas siguen calientes durante horas y pueden quemar a quien pise ahí!).</p>")}
<h2 style="margin-top:0.1in">La brisa del mar</h2>
<div class="fig">{I.brisa_marina()}</div>
<p class="small">De día, en la costa suele soplar una brisa <strong>desde el mar hacia la tierra</strong>; de noche, al revés. Por eso el humo de tu fogata cambia de dirección y conviene hacer la fogata <strong>a un lado</strong> del refugio, no delante. ¿Por qué pasa? ¡Descúbrelo en el experimento!</p>
''', "c-cafe")

L.experimento("La arena contra el agua", "c-cafe", "1 hora", "fácil",
              ["2 recipientes iguales", "Arena (o tierra seca)", "Agua", "1 termómetro", "Un lugar soleado (o una lámpara, con un adulto)", "Un reloj"],
              ["Llena un recipiente con arena y el otro con agua, a la misma altura. Déjalos a la sombra 15 minutos y mide su temperatura.",
               "Ponlos al sol durante 30 minutos.",
               "Mide la temperatura de la arena (a 1 cm de profundidad) y la del agua.",
               "Llévalos otra vez a la sombra y mide cada 10 minutos. ¿Cuál se enfría más rápido?"],
              "<p>La arena se calienta y se enfría <strong>mucho más rápido</strong> que el agua, porque el agua necesita muchísima energía para cambiar de temperatura (su gran <strong>capacidad calorífica</strong>, la del globo del Libro 2). De día, la tierra está más caliente que el mar: el aire sobre la arena se calienta, se vuelve más ligero y <strong>sube</strong>, y el aire fresco del mar corre a ocupar su lugar: ¡es la <strong>brisa marina</strong>! De noche, la tierra se enfría antes que el mar y la brisa sopla al revés.</p>",
              "Anota tus resultados:",
              resultados='<table><tr><th>Momento</th><th>Arena (°C)</th><th>Agua (°C)</th></tr><tr><td>Al inicio</td><td></td><td></td></tr><tr><td>30 min al sol</td><td></td><td></td></tr><tr><td>10 min a la sombra</td><td></td><td></td></tr><tr><td>20 min a la sombra</td><td></td><td></td></tr></table>',
              n_lineas=0)

L.pagina(f'''
{chip("Capítulo 4 · Actividades")}
<h2>El campamento perfecto</h2>
<p>Dibuja tu campamento en la isla. Incluye: la línea de marea alta, tu refugio de palma, la fogata, el lugar para las señales, tu recolector de lluvia y de dónde viene la brisa de día.</p>
<div class="marco" style="height:4.3in"></div>
<h3 style="margin-top:0.18in">Une cada problema con su solución</h3>
{unir(["Los cocos pueden caer", "La marea sube de noche", "Llueve con fuerza", "Hace mucho calor al mediodía", "Brasas bajo la arena"],
      ["Colocar las hojas del techo en capas", "Apagar el fuego con agua", "No acampar bajo palmeras con cocos", "Acampar arriba de la línea de algas secas", "Dejar abiertos los lados del refugio"])}
''', "c-cafe")

# ═════════════ CAP 5: NAVEGACIÓN ═════════════
L.apertura(5, "Navegar sin brújula", "Estrellas, nubes, olas y aves: los secretos de los grandes navegantes.", "c-morado",
           f'<div style="margin:0 0.3in 0.1in 0">{I.svg(280, 230, I.barco(140, 150, 1.6))}</div>',
           ["Conocer a los navegantes polinesios.", "Descubrir cómo delatan una isla las nubes y las aves.",
            "Entender por qué flotan los barcos.", "Construir un barco de papel de aluminio.", "Encontrar un tesoro con coordenadas y rumbos."],
           "<p>En 1976, la canoa polinesia <strong>Hōkūle‘a</strong> navegó de Hawái a Tahití —¡unos 4 000 km!— sin brújula ni instrumentos modernos, guiándose solo por las estrellas, el sol, las olas y las aves.</p>")

L.pagina(f'''
{chip("Capítulo 5 · Navegación")}
<h2>Los maestros del océano</h2>
<p>Hace más de mil años, los navegantes de la <strong>Polinesia</strong> cruzaron el océano Pacífico en canoas dobles y descubrieron islas diminutas separadas por miles de kilómetros de agua. No tenían brújula ni mapas de papel: tenían la <strong>ciencia de la observación</strong>.</p>
{tarjetas([("⭐", "Estrellas", "Memorizaban por dónde salía y se ponía cada estrella en el horizonte: una brújula en el cielo."),
           ("🌊", "El oleaje", "Sentían con el cuerpo la dirección de las olas largas del océano y cómo cambiaban al acercarse a tierra."),
           ("☁️", "Nubes quietas", "Sobre una isla se forman nubes que no se mueven con las demás. ¡A veces su base se ve verdosa por el reflejo de la laguna!"),
           ("🐦", "Aves marinas", "Algunas aves salen a pescar al amanecer y regresan a tierra al atardecer: seguirlas lleva a una isla."),
           ("🌿", "Restos flotantes", "Hojas, ramas o cocos flotando indican que hay tierra cerca."),
           ("☀️", "El sol", "Sale por el este y se pone por el oeste, como aprendiste en el Libro 1.")], 2)}
{ciencia("<p>¿Por qué se forman nubes sobre las islas? De día, la tierra de la isla se calienta más que el mar (¡como la arena del experimento anterior!). El aire caliente sube, se enfría al subir y su vapor se <strong>condensa</strong> formando una nube que se queda «anclada» encima de la isla.</p>")}
''', "c-morado")

L.pagina(f'''
{chip("Capítulo 5 · Flotar")}
<h2>¿Por qué flota un barco de hierro?</h2>
<p>Un clavo de hierro se hunde, pero un barco de hierro enorme flota. ¿Cómo es posible? Hace más de 2 000 años, un sabio griego llamado <strong>Arquímedes</strong> lo descubrió (según la leyenda, ¡mientras se bañaba!).</p>
{ciencia("<p>Cuando algo se mete en el agua, <strong>aparta</strong> (desplaza) una cantidad de agua. El agua empuja hacia arriba con una fuerza igual al peso del agua apartada: es el <strong>empuje</strong> o <strong>principio de Arquímedes</strong>. Un clavo aparta muy poca agua y se hunde. Un barco tiene forma de cuenco lleno de aire: aparta muchísima agua, y el empuje es suficiente para sostenerlo. ¡La forma importa tanto como el material!</p>", "🔬 El principio de Arquímedes")}
<h3>Balsas de supervivencia</h3>
<p>Para cruzar una laguna o llevar cosas por el agua, los náufragos y los pueblos costeros han usado:</p>
<div class="cols small">
<ul><li><strong>Troncos atados</strong> con lianas o cuerdas: la madera es menos densa que el agua.</li>
<li><strong>Bambú</strong>: sus tallos huecos están llenos de aire.</li></ul>
<ul><li><strong>Totora</strong>: en el lago Titicaca se construyen barcas e islas enteras con este junco.</li>
<li><strong>Botellas cerradas</strong>: el aire atrapado las hace flotar muy bien.</li></ul>
</div>
{seguridad("<p>Una balsa es para aprender y para emergencias reales con adultos. <strong>Nunca intentes salir al mar en una balsa</strong>: las corrientes y el viento pueden alejarte de la costa muy rápido. En una isla, lo más seguro es quedarse en tierra y hacer señales.</p>")}
{sabias("<p>Las balsas de los <strong>uros</strong>, en el lago Titicaca (Perú y Bolivia), son de totora, igual que las islas flotantes donde viven. ¡Tienen que añadir capas nuevas de junco cada pocas semanas porque las de abajo se pudren!</p>")}
''', "c-morado")

L.experimento("El barco de aluminio", "c-morado", "30 minutos", "fácil",
              ["Papel de aluminio (2 cuadrados de 20 × 20 cm)", "1 recipiente grande con agua", "Monedas iguales (o canicas)", "1 regla"],
              ["Con un cuadrado de aluminio, haz una bola bien apretada y ponla en el agua. ¿Flota o se hunde?",
               "Con el otro cuadrado, construye un barco con fondo plano y bordes levantados.",
               "Ponlo en el agua y añade monedas una a una, repartidas por el fondo.",
               "Cuenta cuántas monedas aguanta antes de hundirse.",
               "Prueba a rediseñarlo: ¿más ancho? ¿bordes más altos? ¿Cuál es tu récord?"],
              "<p>La bola y el barco pesan lo mismo, pero el barco <strong>aparta mucha más agua</strong>, así que recibe un empuje mayor. Cuantas más monedas pones, más se hunde el barco y más agua aparta… hasta que el agua llega al borde y entra. Un barco ancho y con bordes altos puede apartar más agua antes de hundirse: por eso aguanta más carga.</p>",
              "Mi récord de monedas:",
              resultados='<table><tr><th>Diseño</th><th>Descripción</th><th>Monedas</th></tr><tr><td style="height:0.36in">1</td><td></td><td></td></tr><tr><td style="height:0.36in">2</td><td></td><td></td></tr><tr><td style="height:0.36in">3</td><td></td><td></td></tr></table>',
              n_lineas=0)

tesoro = {(2, 4): "🌴", (5, 4): "🦀", (1, 1): "🐢", (7, 0): "⛵", (4, 2): "🗿", (6, 3): "🪨", (0, 5): "🐚"}
mar = {(c, r) for c in range(8) for r in range(6) if c in (0, 7) or r in (0, 5)}
colsT = "ABCDEFGH"
filasT = '<tr><th></th>' + "".join(f'<th class="center">{c}</th>' for c in colsT) + "</tr>"
for r in range(6):
    filasT += f'<tr><th class="center">{r + 1}</th>'
    for c in range(8):
        bg = "#bfe6fa" if (c, r) in mar else "#f6e4b8"
        filasT += f'<td class="center" style="height:0.5in;width:0.55in;font-size:22px;background:{bg}">{tesoro.get((c, r), "")}</td>'
    filasT += "</tr>"
L.pagina(f'''
{chip("Capítulo 5 · Actividades")}
<h2>El mapa del tesoro</h2>
<p>Un viejo pirata dejó estas instrucciones. El <strong>Norte</strong> está arriba del mapa. Cada paso es una casilla.</p>
<div style="display:flex;gap:0.25in;align-items:flex-start">
<table style="width:auto">{filasT}</table>
<div class="small" style="flex:1">
<div class="box sabias" style="margin-top:0"><h4>📜 Instrucciones del pirata</h4>
<p class="mano" style="font-size:13pt;line-height:1.4">1. Empieza en la palmera 🌴.<br>2. Camina 2 pasos al Este.<br>3. Camina 3 pasos al Norte.<br>4. Camina 1 paso al Oeste.<br>5. ¡Cava ahí!</p></div>
<p>🔢 El tesoro está en la casilla: ______</p>
<p>🌴 La palmera está en: ______</p>
<p>🐢 La tortuga está en: ______</p>
</div></div>
<h3 style="margin-top:0.15in">Preguntas de navegante</h3>
<p>a) Desde el tesoro, ¿en qué dirección está el barco ⛵? (N, S, E, O, NE, NO, SE, SO) ________</p>
<p>b) ¿Qué objeto está justo al Este de la palmera, a 3 pasos? ________</p>
<p>c) ¿En qué fila y columna está el barco? ________</p>
<h3>Ahora tú: esconde un tesoro</h3>
<p class="small">Elige una casilla secreta y escribe instrucciones para que alguien de tu familia lo encuentre:</p>
{lineas(3)}
''', "c-morado")

# ═════════════ CAP 6: VIDA EN LA COSTA ═════════════
L.apertura(6, "Vida en la costa", "Pozas, cangrejos, corales y tortugas: un mundo entre dos mareas.", "c-verde",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("🦀", 170)}</div>',
           ["Explorar las pozas de marea.", "Conocer a los animales que debes mirar sin tocar.",
            "Descubrir por qué los corales son animales.", "Hacer crecer cristales de sal.", "Ayudar a cuidar el mar."],
           "<p>Los <strong>arrecifes de coral</strong> ocupan una parte diminuta del océano, pero en ellos vive cerca de <strong>una de cada cuatro especies marinas</strong>. ¡Son como las selvas tropicales del mar!</p>")

L.pagina(f'''
{chip("Capítulo 6 · Vida marina")}
<h2>Un mundo entre dos mareas</h2>
<p>Cuando baja la marea, entre las rocas quedan <strong>pozas</strong> llenas de vida. Los seres que viven ahí son campeones de supervivencia: aguantan el sol, las olas, el agua dulce de la lluvia y quedarse fuera del agua durante horas.</p>
{tarjetas([("🦀", "Cangrejos", "Tienen el esqueleto por fuera (exoesqueleto) y lo cambian para crecer."),
           ("⭐", "Estrellas de mar", "¡Pueden regenerar un brazo perdido! Si la tocas, puedes dañarla: solo mírala."),
           ("🐚", "Caracoles y lapas", "Se pegan fuerte a la roca para no secarse ni ser arrastrados."),
           ("🪸", "Corales", "Parecen plantas o rocas, pero son colonias de animalitos llamados pólipos."),
           ("🐢", "Tortugas marinas", "Vuelven a desovar a la playa donde nacieron. ¡Viajan miles de kilómetros!"),
           ("🐟", "Peces de poza", "Algunos se quedan en las pozas hasta que vuelve la marea.")])}
<h3>Mira, pero no toques</h3>
<table class="small">
<tr><th style="width:1.5in">Animal</th><th>Por qué y qué hacer</th></tr>
<tr><td>🎐 <strong>Medusas</strong></td><td>Sus tentáculos pican, incluso si la medusa está muerta en la arena. Si te pica, sal del agua, avisa a un adulto y enjuaga con <strong>agua de mar</strong> (no dulce), sin frotar.</td></tr>
<tr><td>⚫ <strong>Erizos</strong></td><td>Sus púas se clavan en los pies. Por eso se usa calzado en las rocas.</td></tr>
<tr><td>🟤 <strong>Rayas</strong></td><td>Se entierran en la arena de la orilla. Camina en el agua <strong>arrastrando los pies</strong>, igual que en los ríos del Libro 2.</td></tr>
<tr><td>🪸 <strong>Corales</strong></td><td>Cortan la piel y se mueren si los tocas o los pisas. Admíralos de lejos.</td></tr>
</table>
{sabias("<p>Las tortuguitas recién nacidas encuentran el mar guiándose por el brillo del horizonte sobre el agua. Las luces de casas y hoteles las confunden y caminan hacia tierra. Por eso en las playas de anidación se apagan las luces de noche.</p>")}
''', "c-verde")

L.experimento("Cristales de sal", "c-verde", "15 minutos + 3 a 7 días de espera", "fácil",
              ["1 taza de agua caliente (con un adulto)", "Sal de mesa (o sal gruesa)", "1 frasco", "1 plato oscuro o un trozo de cartulina negra", "1 lupa", "1 cuchara"],
              ["Un adulto calienta el agua. Añade sal cucharada a cucharada y remueve hasta que ya <strong>no se disuelva más</strong> (quedará un poco en el fondo).",
               "Deja reposar unos minutos y vierte el agua transparente en el plato oscuro, sin la sal del fondo.",
               "Coloca el plato en un lugar tranquilo, soleado o cálido, donde nadie lo mueva.",
               "Obsérvalo cada día con la lupa. ¿Qué forma tienen los cristales?"],
              "<p>El agua caliente puede disolver más sal que la fría. Cuando el agua se <strong>evapora</strong>, ya no puede mantener toda la sal disuelta, y las partículas de sal se ordenan unas junto a otras formando <strong>cristales</strong>. La sal de mesa forma cristales con forma de <strong>cubo</strong> porque sus partículas se colocan en una red ordenada, como bloques de construcción. ¡Así se obtiene la sal en las <strong>salinas</strong> junto al mar!</p>",
              "Dibuja los cristales que viste con la lupa:",
              resultados='<div class="marco" style="height:1.5in"></div>', n_lineas=0)

L.pagina(f'''
{chip("Capítulo 6 · Actividades")}
<h2>Guardianes del mar</h2>
<h3>1. ¿Cuánto tarda en desaparecer?</h3>
<p>Une cada residuo que llega a la playa con el tiempo aproximado que tarda en descomponerse en el mar:</p>
{unir(["Toalla de papel", "Periódico", "Lata de refresco", "Botella de plástico", "Sedal (hilo) de pesca"],
      ["Unas 6 semanas", "Unos 600 años", "Unas 2 a 4 semanas", "Unos 200 años", "Unos 450 años"])}
<p class="tiny">Los tiempos son aproximados: dependen del sol, el agua y la temperatura.</p>
<h3 style="margin-top:0.15in">2. Mi diario de la costa</h3>
<div class="cols" style="gap:0.2in">
<div><p><strong>Fecha y lugar:</strong> _______________</p><p><strong>Marea:</strong> ☐ alta ☐ baja ☐ subiendo ☐ bajando</p><p><strong>Animales que vi:</strong></p>{lineas(2)}</div>
<div><h4>Dibuja tu mejor hallazgo</h4><div class="marco" style="height:1.9in"></div></div>
</div>
{reto("<p>Con tu familia, dedica 15 minutos a recoger basura en una playa, un río o un parque. Cuenta cuántos objetos de plástico encontraste: ______. ¡Cada pieza que recoges es una que no llegará al estómago de una tortuga! ☐ ¡Reto completado!</p>")}
''', "c-verde")

# ═════════════ CAP 7: SEÑALES ═════════════
L.apertura(7, "Señales desde la isla", "¡Barco a la vista! Aprende a que te vean desde el mar y desde el aire.", "c-azul",
           f'<div style="margin:0 0.5in 0.4in 0">{emoji("🆘", 170)}</div>',
           ["Hacer señales gigantes en la arena.", "Usar el fuego, el humo y los espejos.",
            "Comprobar hasta dónde llega un silbato.", "Descifrar el código del náufrago."],
           "<p>En 2018, en una playa de Australia, una familia encontró un <strong>mensaje en una botella</strong> lanzado desde un barco alemán en 1886. ¡Había estado 132 años escondido en la arena!</p>")

L.pagina(f'''
{chip("Capítulo 7 · Señales")}
<h2>Que te vean desde lejos</h2>
<p>En una isla, la ventaja es que <strong>la playa es un lugar abierto</strong>: desde un barco o un avión se ve muy bien. Solo hay que llamar su atención. Repasa las señales del Libro 1 y añade estas:</p>
{tarjetas([("🆘", "Letras gigantes", "Escribe SOS en la arena <strong>por encima de la marea alta</strong>, con letras de al menos 3 pasos. Rellena los surcos con algas, piedras o ramas para que hagan sombra y contraste."),
           ("🔥", "Tres fuegos", "Tres fogatas en triángulo es una señal internacional de auxilio. De día, hojas verdes encima dan humo blanco."),
           ("🪞", "Espejo o lata brillante", "Un reflejo del sol se ve a kilómetros desde un barco. Apunta con los dedos en «V»."),
           ("🚩", "Bandera", "Tela de color brillante atada a un palo alto en el punto más visible de la playa."),
           ("🔦", "Linterna", "De noche: tres destellos largos o el SOS en Morse (··· ——— ···)."),
           ("📣", "Silbato", "El sonido viaja bien sobre el agua. Tres silbidos, pausa, y repetir.")], 2)}
{ciencia("<p>Desde lejos, los ojos distinguen mejor el <strong>contraste</strong> (oscuro sobre claro, o claro sobre oscuro) y el <strong>movimiento</strong> que los detalles. Por eso una letra rellena de algas oscuras sobre arena blanca, un destello que parpadea o una bandera que ondea llaman mucho la atención. Además, las formas rectas y los ángulos (como una X o una V) casi no existen en la naturaleza: ¡el cerebro de quien mira sabe enseguida que las hizo una persona!</p>")}
{seguridad("<p>Las señales de auxilio son solo para emergencias reales. Y nunca apuntes un reflejo a los ojos de una persona o de un piloto.</p>")}
''', "c-azul")

L.experimento("¿Hasta dónde llega tu voz?", "c-azul", "30 minutos", "fácil",
              ["1 silbato", "1 compañero", "Un parque o una playa amplia y tranquila", "1 adulto que acompañe", "Papel y lápiz"],
              ["Tu compañero se queda en un punto fijo con el adulto. Tú te alejas contando tus pasos.",
               "Cada 20 pasos, di una palabra con voz normal. Tu compañero levanta la mano si la oye.",
               "Anota a cuántos pasos dejó de oírte.",
               "Repite con un grito (sin forzar la garganta) y luego con el silbato.",
               "Compara las tres distancias. ¿Cuál llegó más lejos? ¿Cuál te cansó más?"],
              "<p>El sonido son vibraciones que se van debilitando a medida que se alejan, porque la energía se reparte en un espacio cada vez mayor. El silbato produce un sonido muy <strong>agudo</strong> (de alta frecuencia) y potente, fácil de distinguir entre el ruido de las olas y el viento. Además, silbar no cansa ni daña la voz: ¡puedes pedir ayuda durante horas!</p>",
              "Anota tus resultados:",
              resultados='<table><tr><th>Sonido</th><th>Pasos hasta dejar de oírse</th><th>¿Te cansó?</th></tr><tr><td style="height:0.36in">Voz normal</td><td></td><td></td></tr><tr><td style="height:0.36in">Grito</td><td></td><td></td></tr><tr><td style="height:0.36in">Silbato</td><td></td><td></td></tr></table>',
              n_lineas=0)

cuadro = ["ABCDE", "FGHIK", "LMNOP", "QRSTU", "VWXYZ"]
pos = {ch: f"{r + 1}{c + 1}" for r, fila in enumerate(cuadro) for c, ch in enumerate(fila)}
pos["J"] = pos["I"]
MENSAJE = "SOS EN LA ARENA"
codigo = " / ".join(" ".join(pos[ch] for ch in pal) for pal in MENSAJE.split())
tabla_p = '<tr><th></th>' + "".join(f'<th class="center">{i}</th>' for i in range(1, 6)) + "</tr>"
for r, fila in enumerate(cuadro):
    tabla_p += f'<tr><th class="center">{r + 1}</th>' + "".join(f'<td class="center" style="font-family:Fredoka;font-weight:600;font-size:15pt;width:0.5in;height:0.42in">{"I/J" if ch == "I" else ch}</td>' for ch in fila) + "</tr>"
casillas = "".join('<span style="display:inline-block;width:0.3in;height:0.36in;border-bottom:2px solid var(--tinta);margin:0 2px"></span>' if ch != " " else '<span style="display:inline-block;width:0.25in"></span>' for ch in MENSAJE)
L.pagina(f'''
{chip("Capítulo 7 · Actividades")}
<h2>El código del náufrago</h2>
<p>Este código tiene más de 2 000 años: se llama <strong>cuadrado de Polibio</strong>, por un sabio griego. Cada letra se escribe con dos números: primero la <strong>fila</strong> y luego la <strong>columna</strong>. Por ejemplo, la <strong>B</strong> es <strong>12</strong> y la <strong>M</strong> es <strong>32</strong>. (La I y la J comparten casilla, y la Ñ se escribe como N).</p>
<div style="display:flex;gap:0.3in;align-items:center">
<table style="width:auto">{tabla_p}</table>
<div class="box sabias" style="flex:1"><h4>💡 ¿Por qué con números?</h4><p class="small">Porque los números se pueden enviar con cualquier cosa: golpes, destellos de linterna, piedras en fila… Por ejemplo, 3-2 serían tres destellos, pausa, dos destellos.</p></div>
</div>
<h3 style="margin-top:0.15in">Descifra el mensaje de la botella</h3>
<p style="font-size:15pt;font-weight:800;text-align:center;margin:0.1in 0;font-family:Fredoka">{codigo}</p>
<p class="center" style="margin:0.15in 0">{casillas}</p>
<h3>Escribe tu propio mensaje en una botella</h3>
<p class="small">¿Qué escribirías si estuvieras en una isla? Escríbelo primero en letras y luego en código de Polibio.</p>
{lineas(4)}
''', "c-azul")

# ═════════════ GRAN FINAL ═════════════
L.sopa(["ISLA", "MAREA", "OLA", "CORAL", "PALMERA", "COCO", "CANGREJO", "TORTUGA", "MEDUSA", "BRISA", "BALSA", "SAL", "SOMBRA", "PLAYA", "ESTRELLA"], "c-azul", semilla=11)
L.crucigrama([("DESTILACION", "Separar el agua de la sal evaporándola y condensándola."),
              ("ULTRAVIOLETA", "Luz invisible del sol que quema la piel."),
              ("ARQUIMEDES", "Sabio griego que explicó por qué flotan los barcos."),
              ("RESACA", "Corriente que te lleva mar adentro: se escapa nadando paralelo a la orilla."),
              ("OSMOSIS", "El agua pasa hacia donde hay más sal, como en la papa."),
              ("ALBEDO", "Capacidad de una superficie para reflejar la luz."),
              ("MAREA", "Subida y bajada del mar causada por la Luna."),
              ("CORAL", "Animal que forma arrecifes."),
              ("LUNA", "Su gravedad provoca las mareas."),
              ("BRISA", "Viento suave que de día sopla desde el mar."),
              ("COCO", "Fruto de palmera con agua dulce dentro."),
              ("POLIBIO", "Sabio griego que inventó un código con números.")], "c-naranja", "Crucigrama de la isla")
L.mochila_examen(["Agua dulce (¡mucha!)", "Sombrero de ala ancha", "Protector solar", "Gafas de sol", "Camiseta de manga larga", "Calzado para el agua",
                  "Silbato", "Espejo pequeño de señales", "Linterna", "Botiquín pequeño", "Tabla de mareas del día", "Bolsa para recoger basura",
                  "Snacks y fruta", "Toalla o pareo para dar sombra"],
                 [("En una isla tropical, lo primero suele ser buscar…", ["comida", "sombra", "conchas"]),
                  ("Beber agua de mar…", ["quita la sed", "deshidrata", "es sano"]),
                  ("La luz que quema la piel es la…", ["ultravioleta", "infrarroja", "verde"]),
                  ("Si te atrapa una corriente de resaca, nadas…", ["contra la corriente", "paralelo a la orilla", "hacia el fondo"]),
                  ("Las mareas las causa sobre todo…", ["el viento", "la Luna", "los peces"]),
                  ("Para acampar en la playa, te pones…", ["bajo las palmeras con cocos", "junto al agua", "arriba de la línea de marea alta"]),
                  ("Un barco de hierro flota porque…", ["aparta mucha agua", "el hierro flota", "tiene motor"]),
                  ("Si te pica una medusa, se enjuaga con…", ["agua dulce", "agua de mar sin frotar", "arena"])],
                 "En la costa, el sol y el agua son los protagonistas. Marca lo que llevas:", "c-azul")
L.soluciones([
    ("Cap. 1 · Sol y calor", "V/F: a) V, b) F, c) V, d) V, e) F, f) V. La sombra más corta es cerca del mediodía."),
    ("Cap. 2 · Agua dulce", "Orden: 1 el sol calienta, 2 el agua se evapora y la sal se queda, 3 el vapor se condensa, 4 las gotas escurren al vaso. Cálculos: a) 70 g, b) 350 g, c) 17,5 g. Plan: abrir cocos verdes con un adulto, montar una destilación solar, recoger lluvia y rocío con la lona."),
    ("Cap. 3 · Mareas", "a) Hacia las 11:20 (marea baja), con un adulto. b) 17:30. c) 1,6 m. d) Hacia las 06:00. e) No: la marea está subiendo y a las 17:30 el agua llegará mucho más arriba. V/F: a) F, b) V, c) V, d) V."),
    ("Cap. 4 · Refugio", "1-c, 2-d, 3-a, 4-e, 5-b."),
    ("Cap. 5 · Navegación", "Tesoro: <strong>D2</strong> (palmera C5 → E5 → E2 → D2). Palmera: C5 · Tortuga: B2. a) Noreste. b) El cangrejo (F5). c) H1."),
    ("Cap. 6 · Vida marina", "1-c (toalla de papel: 2 a 4 semanas), 2-a (periódico: unas 6 semanas), 3-d (lata: unos 200 años), 4-e (botella: unos 450 años), 5-b (sedal: unos 600 años)."),
    ("Cap. 7 · Señales", "Mensaje: <strong>SOS EN LA ARENA</strong>."),
    ("Gran examen", "1-b, 2-b, 3-a, 4-b, 5-b, 6-c, 7-a, 8-b."),
    ("Para colorear", "La fogata no tiene agua cerca ni un adulto cuidándola, ¡y falta un SOS gigante en la arena!"),
])
L.soluciones_pasatiempos()
L.glosario([("Albedo", "Capacidad de una superficie para reflejar la luz. Los colores claros tienen mucho."),
            ("Brisa marina", "Viento que de día sopla desde el mar hacia la tierra."),
            ("Condensación", "Cuando el vapor se enfría y se convierte en gotitas de agua."),
            ("Contraste", "Diferencia de color o brillo que hace que algo destaque."),
            ("Coral", "Colonia de animalitos (pólipos) que construye arrecifes."),
            ("Corriente de resaca", "Corriente que se lleva el agua desde la orilla hacia mar adentro."),
            ("Cristal", "Sólido cuyas partículas están ordenadas en una red, como la sal."),
            ("Densidad", "Cuánta materia hay en un espacio. Lo menos denso flota sobre lo más denso."),
            ("Destilación", "Separar el agua de la sal evaporándola y volviéndola a condensar."),
            ("Empuje", "Fuerza hacia arriba que hace el agua sobre lo que se mete en ella."),
            ("Marea", "Subida y bajada del nivel del mar causada por la Luna y el Sol."),
            ("Ósmosis", "Paso del agua a través de una membrana hacia donde hay más sal."),
            ("Pozas de marea", "Charcos entre las rocas que quedan cuando baja la marea."),
            ("Ultravioleta (UV)", "Luz invisible del sol con mucha energía, que quema la piel.")])
L.colorear(I.isla_escena(), "¿Qué le falta a este campamento de isla para que los rescaten y sea seguro? <em>Pista: mira los capítulos 4 y 7.</em>")
L.notas()
L.certificado("Explorador de<br>Islas y Mares", "sol y calor, agua dulce, mareas, refugio y fuego en la playa, navegación, vida marina y señales")
L.contraportada(I.isla_escena(), "¿Podrías sobrevivir en una isla?",
                ["Quitarle la sal al agua con el sol. Descubrir por qué la Luna mueve el mar. Escapar de una corriente de resaca. Hacer flotar un huevo y construir un barco que aguante monedas. Encontrar un tesoro con coordenadas y descifrar el mensaje de una botella.",
                 "El Libro 3 cierra la serie con la ciencia del mar y la costa: experimentos con materiales de casa, pasatiempos, diario de la costa y un certificado de explorador."],
                "#135a86")
L.construir([("Bienvenido a la isla", "Bienvenida y lo que ya sabes", False), ("Las 8 reglas de oro de la costa", "Reglas de oro y las zonas de la isla", False),
             ("Sopa de letras del explorador", "Gran final: pasatiempos y examen", True), ("<h2>Soluciones</h2>", "Soluciones y glosario", True),
             ("CERTIFICADO OFICIAL", "Tu certificado de explorador", True)])
