"""Gera diretrizes-icones.tex (slide 'Diretrizes para a pesquisa'): quatro cartões com ícone."""
W, H, G = 6.6, 5.5, 0.3
CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
out = []


def cartao(cx, cy, cor, titulo, frase):
    out.append(r"\node[dbox, draw=%s, line width=1.6pt, minimum width=%.1fcm, minimum height=%.1fcm] at (%.2f,%.2f) {};" % (cor, W, H, cx, cy))
    out.append(r"\node[font=\Large\bfseries, %s] at (%.2f,%.2f) {%s};" % (cor, cx, cy - 1.0, titulo))
    out.append(r"\node[font=\Large, text width=%.1fcm, align=center, anchor=north] at (%.2f,%.2f) {%s};" % (W - 0.6, cx, cy - 1.35, frase))


def pessoa(x, y, cor, esc=1.0):
    out.append(r"\fill[%s!25!white, draw=%s, line width=1.5pt] (%.2f,%.2f) circle (%.2f);" % (cor, cor, x, y + 0.55 * esc, 0.34 * esc))
    out.append(r"\fill[%s!25!white, draw=%s, line width=1.5pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (cor, cor, x - 0.66 * esc, y - 0.5 * esc, x - 0.66 * esc, y + 0.12 * esc, x + 0.66 * esc, y + 0.12 * esc, x + 0.66 * esc, y - 0.5 * esc))


X = [W / 2, W + G + W / 2]
Y = [H + G + H / 2, H / 2]

# 1 Explicar: pessoa com balão de fala (três linhas)
cx, cy = X[0], Y[0]
cartao(cx, cy, "dblue", "Explicar", r"objetivos, tempo e \textbf{como os dados serão usados}")
ix, iy = cx, cy + 0.9
pessoa(ix - 1.2, iy - 0.1, "dblue")
out.append(r"\draw[dblue, fill=white, line width=1.5pt, rounded corners=6pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.1, iy - 0.35, ix + 1.7, iy + 0.95))
out.append(r"\draw[white, line width=2.6pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.1, iy - 0.05, ix - 0.1, iy + 0.35))
out.append(r"\draw[dblue, line width=1.5pt, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.1, iy - 0.05, ix - 0.48, iy + 0.15, ix - 0.1, iy + 0.35))
for k in range(3):
    out.append(r"\draw[black!55, line width=1.4pt] (%.2f,%.2f) -- ++(%.2f,0);" % (ix + 0.2, iy + 0.7 - 0.38 * k, 1.2 if k < 2 else 0.7))

# 2 Confidencialidade: cadeado
cx, cy = X[1], Y[0]
cartao(cx, cy, "dgreen", "Confidencialidade", r"privacidade: dados brutos \textbf{só com os pesquisadores}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dgreen, line width=3pt] (%.2f,%.2f) -- (%.2f,%.2f) arc (180:0:0.45) -- (%.2f,%.2f);" % (ix - 0.45, iy + 0.1, ix - 0.45, iy + 0.45, ix + 0.45, iy + 0.1))
out.append(r"\draw[dgreen, fill=dgreen!20!white, line width=1.8pt, rounded corners=4pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.8, iy - 0.8, ix + 0.8, iy + 0.15))
out.append(r"\fill[dgreen] (%.2f,%.2f) circle (0.13);" % (ix, iy - 0.3))
out.append(r"\draw[dgreen, line width=2pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix, iy - 0.35, ix, iy - 0.62))

# 3 Anonimato: pessoa sem rosto + etiqueta de código
cx, cy = X[0], Y[1]
cartao(cx, cy, "dorange", "Anonimato", r"nada de nomes nem detalhes que \textbf{identifiquem}")
ix, iy = cx, cy + 0.9
pessoa(ix - 1.0, iy - 0.1, "dorange")
out.append(r"\node[font=\Large\bfseries, dorange] at (%.2f,%.2f) {?};" % (ix - 1.0, iy + 0.45))
out.append(r"\node[draw=dorange, fill=white, line width=1.5pt, rounded corners=3pt, font=\large\bfseries, minimum width=1.3cm, minimum height=0.65cm] at (%.2f,%.2f) {P07};" % (ix + 0.9, iy + 0.25))
out.append(r"\node[font=\normalsize, black!60] at (%.2f,%.2f) {código, não nome};" % (ix + 0.9, iy - 0.85))

# 4 Permissão para gravar: microfone com visto
cx, cy = X[1], Y[1]
cartao(cx, cy, "dred", "Permissão para gravar", r"pedir antes de gravar \textbf{voz ou imagem}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dred, fill=dred!15!white, line width=1.8pt, rounded corners=8pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.32, iy - 0.2, ix + 0.32, iy + 0.95))
out.append(r"\draw[dred, line width=1.8pt] (%.2f,%.2f) arc (180:360:0.55);" % (ix - 0.55, iy - 0.05))
out.append(r"\draw[dred, line width=1.8pt] (%.2f,%.2f) -- (%.2f,%.2f) (%.2f,%.2f) -- (%.2f,%.2f);" % (ix, iy - 0.6, ix, iy - 0.85, ix - 0.4, iy - 0.85, ix + 0.4, iy - 0.85))
out.append(r"\fill[dred] (%.2f,%.2f) circle (0.14);" % (ix + 1.1, iy + 0.85))
out.append(r"\node[font=\large\bfseries, dred, anchor=west] at (%.2f,%.2f) {REC};" % (ix + 1.28, iy + 0.85))
out.append(r"\draw[dgreen, fill=white, line width=1.5pt] (%.2f,%.2f) circle (0.32);" % (ix + 1.2, iy - 0.2))
out.append(r"\draw[dgreen, line width=2.6pt, line cap=round, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix + 1.06, iy - 0.2, ix + 1.16, iy - 0.31, ix + 1.36, iy - 0.08))

open("diretrizes-icones.tex", "w").write(CAB + "\n".join(out) + "\n\\end{tikzpicture}\n\\end{document}\n")
