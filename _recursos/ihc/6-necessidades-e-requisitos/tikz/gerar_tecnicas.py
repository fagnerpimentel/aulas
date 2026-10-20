"""Gera tecnicas-icones.tex (slide 'Sete técnicas de uso frequente'): oito cartões com ícone."""
W, H, G = 4.7, 4.6, 0.3
CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
out = []


def cartao(cx, cy, cor, titulo, borda="draw=%s, line width=1.6pt"):
    out.append(r"\node[dbox, %s, minimum width=%.1fcm, minimum height=%.1fcm] at (%.2f,%.2f) {};" % (borda % cor if "%s" in borda else borda, W, H, cx, cy))
    out.append(r"\node[font=\Large\bfseries, %s, text width=%.1fcm, align=center, anchor=north] at (%.2f,%.2f) {%s};" % (cor, W - 0.4, cx, cy - 0.95, titulo))


def pessoa(x, y, cor, esc=1.0):
    out.append(r"\fill[%s!25!white, draw=%s, line width=1.4pt] (%.2f,%.2f) circle (%.2f);" % (cor, cor, x, y + 0.5 * esc, 0.3 * esc))
    out.append(r"\fill[%s!25!white, draw=%s, line width=1.4pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (cor, cor, x - 0.58 * esc, y - 0.42 * esc, x - 0.58 * esc, y + 0.1 * esc, x + 0.58 * esc, y + 0.1 * esc, x + 0.58 * esc, y - 0.42 * esc))


def balao(x, y, texto, cor):
    out.append(r"\node[draw=%s, fill=white, line width=1.3pt, rounded corners=6pt, minimum width=0.8cm, minimum height=0.55cm, font=\large\bfseries, text=%s] at (%.2f,%.2f) {%s};" % (cor, cor, x, y, texto))


CORES = ["dblue", "dblue", "dgreen", "dgreen", "dorange", "dred", "dred"]
POS = [(c, r) for r in (0, 1) for c in range(4)]       # linha 0 = em cima
def centro(i):
    c, r = POS[i]
    return c * (W + G) + W / 2, (1 - r) * (H + G) + H / 2

# 1 Entrevistas
cx, cy = centro(0); cartao(cx, cy, CORES[0], "Entrevistas"); ix, iy = cx, cy + 0.55
pessoa(ix - 0.95, iy - 0.2, "dblue"); pessoa(ix + 0.95, iy - 0.2, "dblue")
balao(ix - 0.75, iy + 0.95, "?", "dblue"); balao(ix + 0.75, iy + 0.95, "!", "dblue")

# 2 Questionários
cx, cy = centro(1); cartao(cx, cy, CORES[1], "Questionários"); ix, iy = cx, cy + 0.5
out.append(r"\draw[dblue, fill=white, line width=1.6pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.8, iy - 0.85, ix + 0.8, iy + 0.95))
for k in range(3):
    y = iy + 0.55 - 0.55 * k
    out.append(r"\draw[dblue, line width=1.2pt] (%.2f,%.2f) rectangle ++(0.28,0.28);" % (ix - 0.6, y - 0.14))
    out.append(r"\draw[black!45, line width=1.3pt] (%.2f,%.2f) -- ++(0.65,0);" % (ix - 0.15, y))
    if k < 2:
        out.append(r"\draw[dgreen, line width=2.2pt, line cap=round, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.57, y, ix - 0.5, y - 0.1, ix - 0.36, y + 0.12))

# 3 Grupos de foco
cx, cy = centro(2); cartao(cx, cy, CORES[2], "Grupos de foco"); ix, iy = cx, cy + 0.5
out.append(r"\draw[dgreen, fill=dgreen!15!white, line width=1.5pt] (%.2f,%.2f) ellipse (1.25 and 0.4);" % (ix, iy - 0.35))
for dx, dy in ((-1.15, 0.15), (0.0, 0.4), (1.15, 0.15)):
    pessoa(ix + dx, iy + dy - 0.1, "dgreen", 0.7)

# 4 Brainstorming
cx, cy = centro(3); cartao(cx, cy, CORES[3], r"\emph{Brainstorming}"); ix, iy = cx, cy + 0.5
out.append(r"\draw[dgreen, fill=dgreen!15!white, line width=1.6pt] (%.2f,%.2f) circle (0.55);" % (ix, iy + 0.4))
out.append(r"\draw[dgreen, line width=1.6pt, fill=white] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.25, iy - 0.35, ix + 0.25, iy - 0.05))
out.append(r"\draw[dgreen, line width=1.6pt] (%.2f,%.2f) -- (%.2f,%.2f) (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.22, iy - 0.05, ix - 0.3, iy + 0.1, ix + 0.22, iy - 0.05, ix + 0.3, iy + 0.1))
import math
for ang in (20, 55, 90, 125, 160):
    a = math.radians(ang)
    out.append(r"\draw[dorange, line width=1.8pt, line cap=round] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix + 0.8 * math.cos(a), iy + 0.4 + 0.8 * math.sin(a), ix + 1.1 * math.cos(a), iy + 0.4 + 1.1 * math.sin(a)))

# 5 Classificação de cartões
cx, cy = centro(4); cartao(cx, cy, CORES[4], "Classificação de cartões"); ix, iy = cx, cy + 0.45
for g, dx in enumerate((-1.2, 0.0, 1.2)):
    out.append(r"\draw[dorange, dashed, line width=1.2pt, rounded corners=4pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix + dx - 0.5, iy - 0.8, ix + dx + 0.5, iy + 0.85))
    for k in range(3 - (1 if g == 1 else 0)):
        out.append(r"\draw[dorange, fill=white, line width=1.2pt] (%.2f,%.2f) rectangle ++(0.7,0.38);" % (ix + dx - 0.35, iy + 0.35 - 0.47 * k - 0.0))

# 6 Estudos de campo
cx, cy = centro(5); cartao(cx, cy, CORES[5], "Estudos de campo"); ix, iy = cx, cy + 0.5
out.append(r"\draw[black!45, dashed, line width=1.2pt] (%.2f,%.2f) ellipse (1.2 and 0.28);" % (ix, iy - 0.8))
out.append(r"\draw[dred, fill=dred!15!white, line width=1.8pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (ix, iy - 0.75, ix - 0.2, iy - 0.35, ix - 0.7, iy - 0.05, ix - 0.7, iy + 0.45, ix - 0.7, iy + 0.95, ix + 0.7, iy + 0.95, ix + 0.7, iy + 0.45))
out.append(r"\fill[white, draw=dred, line width=1.4pt] (%.2f,%.2f) circle (0.26);" % (ix, iy + 0.45))

# 7 Investigação contextual
cx, cy = centro(6); cartao(cx, cy, CORES[6], "Investigação contextual"); ix, iy = cx, cy + 0.45
out.append(r"\draw[black!55, line width=1.6pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 1.5, iy - 0.7, ix + 1.5, iy - 0.7))
pessoa(ix - 1.0, iy - 0.25, "dred", 0.9); pessoa(ix + 1.0, iy - 0.25, "dred", 0.9)
out.append(r"\draw[black!60, fill=white, line width=1.4pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.35, iy - 0.2, ix + 0.35, iy + 0.35))
out.append(r"\draw[black!60, line width=1.4pt] (%.2f,%.2f) -- (%.2f,%.2f) (%.2f,%.2f) -- (%.2f,%.2f);" % (ix, iy - 0.2, ix, iy - 0.7, ix - 0.25, iy - 0.7, ix + 0.25, iy - 0.7))

# 8 Triangulação (cartão neutro)
cx, cy = centro(7) if False else (3 * (W + G) + W / 2, (1 - 1) * (H + G) + H / 2)
out.append(r"\node[dbox, draw=black!55, dashed, fill=white, line width=1.6pt, minimum width=%.1fcm, minimum height=%.1fcm] at (%.2f,%.2f) {};" % (W, H, cx, cy))
out.append(r"\node[font=\Large\bfseries, black!70, text width=%.1fcm, align=center, anchor=north] at (%.2f,%.2f) {Combine mais de uma};" % (W - 0.4, cx, cy - 0.95))
ix, iy = cx, cy + 0.5
pts = [(ix, iy + 0.85), (ix - 0.95, iy - 0.6), (ix + 0.95, iy - 0.6)]
out.append(r"\draw[black!55, line width=1.4pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;" % (pts[0] + pts[1] + pts[2]))
for (x, y), c in zip(pts, ("dblue", "dgreen", "dred")):
    out.append(r"\fill[%s] (%.2f,%.2f) circle (0.2);" % (c, x, y))
out.append(r"\draw[dgreen, line width=2.8pt, line cap=round, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.3, iy - 0.05, ix - 0.08, iy - 0.3, ix + 0.35, iy + 0.25))

open("tecnicas-icones.tex", "w").write(CAB + "\n".join(out) + "\n\\end{tikzpicture}\n\\end{document}\n")
