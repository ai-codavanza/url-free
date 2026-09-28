# ¡Sobrevive en el Bosque! — Ciencia y supervivencia en la naturaleza

Libro de actividades imprimible para niños de 8 a 12 años (48 páginas, tamaño Carta 8.5" × 11").

**Archivo listo para imprimir:** `Sobrevive-en-el-Bosque_Carta.pdf`

## Contenido
- Portada, ficha del explorador, índice, cómo usar el libro
- Reglas de oro de seguridad, la regla de los 3 y el método S.T.O.P.
- 7 capítulos: Orientación · Agua · Fuego · Refugio · Cuerdas y nudos · Plantas y animales · Clima y señales
- 7 experimentos científicos (brújula casera, filtro de agua, transpiración, vela y oxígeno, aislantes, cromatografía de hojas…) y retos
- Pasatiempos: laberinto, rosa de los vientos, código Morse, sopa de letras, crucigrama, examen final
- Diario de campo, página para colorear, notas, soluciones, glosario y certificado

## Regenerar el PDF
```bash
python3 build.py            # genera libro.html
# Luego imprime libro.html a PDF con Chrome/Chromium (tamaño Carta, márgenes: ninguno, gráficos de fondo activados)
```
El texto está en `build.py`, las ilustraciones SVG en `ilustraciones.py`, los pasatiempos en `pasatiempos.py` y el diseño en `estilos.css`.
Fuentes: Fredoka, Nunito y Patrick Hand (Google Fonts, licencia SIL OFL).
