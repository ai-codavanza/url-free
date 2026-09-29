# Serie Pequeños Exploradores — Ciencia y supervivencia en la naturaleza

Tres libros de actividades imprimibles para niños de 8 a 12 años (48 páginas cada uno, tamaño Carta 8.5" × 11").

| Libro | PDF listo para imprimir | Script |
|---|---|---|
| 1. ¡Sobrevive en el Bosque! | `Sobrevive-en-el-Bosque_Carta.pdf` | `build.py` |
| 2. ¡Sobrevive en la Selva! | `Sobrevive-en-la-Selva_Carta.pdf` | `build_selva.py` |
| 3. ¡Sobrevive en la Isla! | `Sobrevive-en-la-Isla_Carta.pdf` | `build_isla.py` |

**Libro 2 — Selva:** orientarse siguiendo ríos, lluvia y pluviómetro, calor húmedo e insectos, fuego con humedad, camuflaje y colores de advertencia, plantas tropicales, señales bajo el dosel. Experimentos: maqueta de cuenca, pluviómetro, capilaridad, globo que no explota, juego del camuflaje, hojas con punta de goteo, teléfono de vasos.

**Libro 3 — Isla:** sol y rayos UV, agua dulce y ósmosis, mareas y corrientes de resaca, refugio y fuego en la playa, navegación polinesia y flotación, vida en la costa, señales. Experimentos: colores y calor, destilación solar, papa en agua salada, huevo que flota, arena contra agua (brisa marina), barco de aluminio, cristales de sal, alcance del silbato.

## Contenido del Libro 1
- Portada, ficha del explorador, índice, cómo usar el libro
- Reglas de oro de seguridad, la regla de los 3 y el método S.T.O.P.
- 7 capítulos: Orientación · Agua · Fuego · Refugio · Cuerdas y nudos · Plantas y animales · Clima y señales
- 6 experimentos científicos (brújula casera, filtro de agua, transpiración, vela y oxígeno, aislantes, cromatografía de hojas…) y retos
- Pasatiempos: laberinto, rosa de los vientos, código Morse, sopa de letras, crucigrama, examen final
- Diario de campo, página para colorear, notas, soluciones, glosario y certificado

## Regenerar el PDF
```bash
python3 build.py            # genera libro.html (Libro 1)
python3 build_selva.py      # genera libro_selva.html (Libro 2)
python3 build_isla.py       # genera libro_isla.html (Libro 3)
# Luego imprime cada .html a PDF con Chrome/Chromium (tamaño Carta, márgenes: ninguno, gráficos de fondo activados)
```
El diseño v2 (cabeceras, portada con sellos, aperturas de capítulo, certificado) se aplica al final de cada `build*.py` con `mejorar.py`. El texto está en `build*.py`, las piezas comunes de la serie en `comun.py`, las ilustraciones SVG en `ilustraciones.py`, los pasatiempos en `pasatiempos.py` y el diseño en `estilos.css`.
Fuentes: Fredoka, Nunito y Patrick Hand (Google Fonts, licencia SIL OFL).
