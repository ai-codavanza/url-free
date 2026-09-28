"""Generadores de pasatiempos: sopa de letras, crucigrama y laberinto (con soluciones)."""
import random

LETRAS = "ABCDEFGHIJLMNOPRSTUVYZ"


def sopa_de_letras(palabras, n=14, semilla=7):
    rnd = random.Random(semilla)
    dirs = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (1, -1)]
    for _ in range(500):
        grid = [[None] * n for _ in range(n)]
        colocadas = {}
        ok = True
        for p in sorted(palabras, key=len, reverse=True):
            opciones = []
            for dr, dc in dirs:
                for r in range(n):
                    for c in range(n):
                        er, ec = r + dr * (len(p) - 1), c + dc * (len(p) - 1)
                        if not (0 <= er < n and 0 <= ec < n):
                            continue
                        cruces = 0
                        valido = True
                        for i, ch in enumerate(p):
                            g = grid[r + dr * i][c + dc * i]
                            if g is not None and g != ch:
                                valido = False
                                break
                            if g == ch:
                                cruces += 1
                        if valido:
                            opciones.append((cruces, rnd.random(), r, c, dr, dc))
            if not opciones:
                ok = False
                break
            opciones.sort(reverse=True)
            top = [o for o in opciones if o[0] == opciones[0][0]]
            _, _, r, c, dr, dc = rnd.choice(top[: max(1, len(top))]) if rnd.random() < 0.5 else rnd.choice(opciones[: max(1, len(opciones) // 3)])
            celdas = []
            for i, ch in enumerate(p):
                grid[r + dr * i][c + dc * i] = ch
                celdas.append((r + dr * i, c + dc * i))
            colocadas[p] = celdas
        if ok:
            sol = [[grid[r][c] is not None for c in range(n)] for r in range(n)]
            for r in range(n):
                for c in range(n):
                    if grid[r][c] is None:
                        grid[r][c] = rnd.choice(LETRAS)
            # comprobación: cada palabra aparece exactamente donde se colocó
            for p, celdas in colocadas.items():
                assert "".join(grid[r][c] for r, c in celdas) == p
            return grid, sol, colocadas
    raise RuntimeError("No se pudo generar la sopa de letras")


def crucigrama(entradas, tam=25):
    """entradas: lista de (PALABRA, pista). Coloca las palabras cruzándolas."""
    palabras = sorted(entradas, key=lambda e: -len(e[0]))
    grid = {}
    dirs_celda = {}
    colocadas = []

    def puede(p, r, c, d):
        dr, dc = (0, 1) if d == "H" else (1, 0)
        antes = (r - dr, c - dc)
        despues = (r + dr * len(p), c + dc * len(p))
        if antes in grid or despues in grid:
            return -1
        cruces = 0
        for i, ch in enumerate(p):
            rr, cc = r + dr * i, c + dc * i
            if (rr, cc) in grid:
                if grid[(rr, cc)] != ch or d in dirs_celda[(rr, cc)]:
                    return -1
                cruces += 1
            else:
                vecinos = [(rr + dc, cc + dr), (rr - dc, cc - dr)]
                if any(v in grid for v in vecinos):
                    return -1
        return cruces

    def poner(p, r, c, d, pista):
        dr, dc = (0, 1) if d == "H" else (1, 0)
        for i, ch in enumerate(p):
            grid[(r + dr * i, c + dc * i)] = ch
            dirs_celda.setdefault((r + dr * i, c + dc * i), set()).add(d)
        colocadas.append((p, r, c, d, pista))

    primera, pista0 = palabras[0]
    poner(primera, 0, 0, "H", pista0)
    pendientes = palabras[1:]
    for _ in range(3):
        resto = []
        for p, pista in pendientes:
            mejor = None
            for (gr, gc), ch in list(grid.items()):
                for i, pc in enumerate(p):
                    if pc != ch:
                        continue
                    for d in ("H", "V"):
                        r, c = (gr, gc - i) if d == "H" else (gr - i, gc)
                        k = puede(p, r, c, d)
                        if k >= 1:
                            rs = [rr for rr, _ in grid] + [r, r + (len(p) if d == "V" else 1)]
                            cs = [cc for _, cc in grid] + [c, c + (len(p) if d == "H" else 1)]
                            area = (max(rs) - min(rs)) * (max(cs) - min(cs))
                            score = (k, -area)
                            if mejor is None or score > mejor[0]:
                                mejor = (score, r, c, d)
            if mejor:
                _, r, c, d = mejor
                poner(p, r, c, d, pista)
            else:
                resto.append((p, pista))
        pendientes = resto
        if not pendientes:
            break
    if pendientes:
        raise RuntimeError(f"No se colocaron: {pendientes}")
    r0 = min(r for r, _ in grid)
    c0 = min(c for _, c in grid)
    filas = max(r for r, _ in grid) - r0 + 1
    cols = max(c for _, c in grid) - c0 + 1
    celdas = {(r - r0, c - c0): ch for (r, c), ch in grid.items()}
    # numeración
    inicios = {}
    for p, r, c, d, pista in colocadas:
        inicios.setdefault((r - r0, c - c0), []).append((d, p, pista))
    numeros = {}
    n = 1
    for pos in sorted(inicios):
        numeros[pos] = n
        n += 1
    horiz = sorted([(numeros[pos], p, pista) for pos, l in inicios.items() for d, p, pista in l if d == "H"])
    vert = sorted([(numeros[pos], p, pista) for pos, l in inicios.items() for d, p, pista in l if d == "V"])
    return filas, cols, celdas, numeros, horiz, vert


def laberinto(w, h, semilla=11):
    rnd = random.Random(semilla)
    # paredes: para cada celda, conjunto de direcciones abiertas
    abiertas = {(x, y): set() for x in range(w) for y in range(h)}
    visit = {(0, 0)}
    pila = [(0, 0)]
    mov = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "O": (-1, 0)}
    op = {"N": "S", "S": "N", "E": "O", "O": "E"}
    while pila:
        x, y = pila[-1]
        vecinos = [(d, x + dx, y + dy) for d, (dx, dy) in mov.items() if (x + dx, y + dy) in abiertas and (x + dx, y + dy) not in visit]
        if not vecinos:
            pila.pop()
            continue
        d, nx, ny = rnd.choice(vecinos)
        abiertas[(x, y)].add(d)
        abiertas[(nx, ny)].add(op[d])
        visit.add((nx, ny))
        pila.append((nx, ny))
    # solución BFS
    from collections import deque
    prev = {(0, 0): None}
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for d in abiertas[(x, y)]:
            dx, dy = mov[d]
            n = (x + dx, y + dy)
            if n not in prev:
                prev[n] = (x, y)
                q.append(n)
    camino = []
    cur = (w - 1, h - 1)
    while cur:
        camino.append(cur)
        cur = prev[cur]
    camino.reverse()
    return abiertas, camino


def laberinto_svg(w, h, abiertas, camino=None, cel=34, color="#26302a"):
    m = 20
    W, H = w * cel + 2 * m, h * cel + 2 * m
    lineas = []
    for (x, y), ab in abiertas.items():
        x0, y0 = m + x * cel, m + y * cel
        if "N" not in ab and not (x == 0 and y == 0):
            lineas.append((x0, y0, x0 + cel, y0))
        if "O" not in ab:
            lineas.append((x0, y0, x0, y0 + cel))
        if y == h - 1 and "S" not in ab and not (x == w - 1):
            lineas.append((x0, y0 + cel, x0 + cel, y0 + cel))
        if x == w - 1 and "E" not in ab:
            lineas.append((x0 + cel, y0, x0 + cel, y0 + cel))
    b = "".join(f'<line x1="{a}" y1="{b_}" x2="{c}" y2="{d}"/>' for a, b_, c, d in lineas)
    out = f'<g stroke="{color}" stroke-width="3.5" stroke-linecap="round">{b}</g>'
    if camino:
        pts = " ".join(f"{m + x * cel + cel / 2},{m + y * cel + cel / 2}" for x, y in camino)
        out += f'<polyline points="{m + cel / 2},{m - 10} {pts} {m + (w - 1) * cel + cel / 2},{m + h * cel + 10}" fill="none" stroke="#e0702a" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{out}</svg>'
