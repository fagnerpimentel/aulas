"""Gera descida-gradiente.tex: 3 quadros mostrando a descida do gradiente sobre o campo de distâncias."""
from collections import deque

NL, NC = 5, 7
OBS = {(r, 3) for r in range(1, 5)}          # parede na coluna 3, com passagem na linha 0
G = (3, 6)                                   # (linha, coluna)
VIZ = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    d = {G: 0}; q = deque([G])
    while q:
        r, c = q.popleft()
        for dr, dc in VIZ:
            n = (r + dr, c + dc)
            if 0 <= n[0] < NL and 0 <= n[1] < NC and n not in OBS and n not in d:
                d[n] = d[(r, c)] + 1; q.append(n)
    return d

D = bfs()

def vizinhas(p):
    return [(p[0] + dr, p[1] + dc) for dr, dc in VIZ
            if 0 <= p[0] + dr < NL and 0 <= p[1] + dc < NC and (p[0] + dr, p[1] + dc) in D]

def unico_min(p):
    v = sorted(D[n] for n in vizinhas(p))
    return len(v) == 1 or v[0] < v[1]

def descida(s):
    rota = [s]; p = s
    while D[p] > 0:
        p = min(vizinhas(p), key=lambda n: D[n]); rota.append(p)
    return rota

# escolhe um início cuja descida tenha mínimo único nos 2 primeiros passos
cands = [p for p in D if D[p] >= 8 and p[1] <= 1]
for s in sorted(cands, key=lambda p: -D[p]):
    rota = descida(s)
    if unico_min(rota[0]) and unico_min(rota[1]):
        S = s; ROTA = rota; break
print("início", S, "distância", D[S], "rota", ROTA)

CEL = 0.78
def xy(p, ox):
    return (ox + p[1] * CEL + CEL / 2, (NL - 1 - p[0]) * CEL + CEL / 2)

def quadro(ox, robo, destaca=False, caminho=None):
    out = []
    for p, d in D.items():
        x, y = xy(p, ox)
        cor = "dgreen!75" if d == 0 else "dblue!%d!white" % (6 + d * 2)
        out.append(r"\fill[%s] (%.3f,%.3f) rectangle +(%s,%s);" % (cor, x - CEL / 2, y - CEL / 2, CEL, CEL))
    for p in OBS:
        x, y = xy(p, ox)
        out.append(r"\fill[black!80] (%.3f,%.3f) rectangle +(%s,%s);" % (x - CEL / 2, y - CEL / 2, CEL, CEL))
    out.append(r"\draw[black!30, line width=0.4pt] (%s,0) grid[step=%s] (%.3f,%.3f);" % (ox, CEL, ox + NC * CEL, NL * CEL))
    out.append(r"\draw[dblue, line width=1.3pt] (%s,0) rectangle (%.3f,%.3f);" % (ox, ox + NC * CEL, NL * CEL))
    if caminho:
        pts = " -- ".join("(%.3f,%.3f)" % xy(p, ox) for p in caminho)
        out.append(r"\draw[dred, line width=2.6pt, line cap=round, line join=round] %s;" % pts)
    if destaca:
        viz = vizinhas(robo)
        mn = min(viz, key=lambda n: D[n])
        for n in viz:
            x, y = xy(n, ox)
            if n == mn: continue
            out.append(r"\draw[dorange, line width=2pt] (%.3f,%.3f) rectangle +(%s,%s);" % (x - CEL / 2 + 0.04, y - CEL / 2 + 0.04, CEL - 0.08, CEL - 0.08))
        x, y = xy(mn, ox)
        out.append(r"\draw[dgreen, line width=3.4pt] (%.3f,%.3f) rectangle +(%s,%s);" % (x - CEL / 2 + 0.04, y - CEL / 2 + 0.04, CEL - 0.08, CEL - 0.08))
        rx, ry = xy(robo, ox)
        out.append(r"\draw[dgreen, line width=2.6pt, -{Stealth[length=3mm]}] (%.3f,%.3f) -- (%.3f,%.3f);" % (rx + (x - rx) * 0.3, ry + (y - ry) * 0.3, rx + (x - rx) * 0.72, ry + (y - ry) * 0.72))
    # números (por cima, em pílulas claras quando há caminho)
    for p, d in D.items():
        x, y = xy(p, ox)
        if d == 0:
            out.append(r"\node[font=\large\bfseries, white] at (%.3f,%.3f) {0};" % (x, y))
        elif caminho:
            out.append(r"\node[font=\large, fill=white!92!dblue, inner sep=1.2pt, rounded corners=2pt] at (%.3f,%.3f) {%d};" % (x, y, d))
        else:
            out.append(r"\node[font=\large] at (%.3f,%.3f) {%d};" % (x, y, d))
    rx, ry = xy(robo, ox)
    out.append(r"\draw[dred, line width=3.2pt] (%.3f,%.3f) circle (0.3);" % (rx, ry))
    return "\n".join(out)

P = NC * CEL + 1.25
corpo = []
corpo.append(r"\useasboundingbox (-0.2,-1.3) rectangle (%.3f,%.3f);" % (2 * P + NC * CEL + 0.2, NL * CEL + 0.95))
tit = ["1. Olhe as vizinhas", "2. Vá para a menor", "3. Repita até chegar ao 0"]
for q in range(3):
    ox = q * P
    corpo.append(r"\node[font=\large\bfseries, dblue] at (%.3f,%.3f) {%s};" % (ox + NC * CEL / 2, NL * CEL + 0.5, tit[q]))
corpo.append(quadro(0, ROTA[0], destaca=True))
corpo.append(quadro(P, ROTA[1], destaca=True))
corpo.append(quadro(2 * P, ROTA[0], caminho=ROTA))
for q in range(2):
    corpo.append(r"\draw[dtrans, line width=2.2pt, -{Stealth[length=3mm]}] (%.3f,%.3f) -- (%.3f,%.3f);" % (q * P + NC * CEL + 0.15, NL * CEL / 2, (q + 1) * P - 0.15, NL * CEL / 2))
# legenda
lx = 0.2
for i, (cor_, t) in enumerate([("dred", "robô"), ("dorange", "vizinhas"), ("dgreen", "a de menor distância")]):
    x = lx + i * 4.4
    corpo.append(r"\draw[%s, line width=2.4pt] (%.2f,-0.95) rectangle +(0.38,0.38);" % (cor_, x))
    corpo.append(r"\node[font=\normalsize, anchor=west] at (%.2f,-0.76) {%s};" % (x + 0.55, t))

corpo.append(r"\fill[dgreen!75] (%.2f,-0.95) rectangle +(0.38,0.38);" % (lx + 3 * 4.4 + 1.2))
corpo.append(r"\node[font=\normalsize, anchor=west] at (%.2f,-0.76) {objetivo (distância 0)};" % (lx + 3 * 4.4 + 1.75))

CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
open("descida-gradiente.tex", "w").write(CAB + "\n".join(corpo) + "\n\\end{tikzpicture}\n\\end{document}\n")
