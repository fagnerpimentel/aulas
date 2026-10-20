"""Gera principios-icones.tex (slide 'Os quatro princípios'): quatro cartões com ícone."""
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


def prato(x, y, cor):
    out.append(r"\draw[%s, line width=1.3pt] (%.2f,%.2f) -- (%.2f,%.2f) (%.2f,%.2f) -- (%.2f,%.2f);" % (cor, x, y, x - 0.5, y - 0.6, x, y, x + 0.5, y - 0.6))
    out.append(r"\draw[%s, line width=1.6pt, fill=%s!15!white] (%.2f,%.2f) arc (180:360:0.55 and 0.26) -- cycle;" % (cor, cor, x - 0.55, y - 0.6))


def pessoa_mini(x, y, cor):
    out.append(r"\fill[%s!30!white, draw=%s, line width=1pt] (%.2f,%.2f) circle (0.13);" % (cor, cor, x, y + 0.22))
    out.append(r"\fill[%s!30!white, draw=%s, line width=1pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (cor, cor, x - 0.24, y - 0.05, x - 0.24, y + 0.1, x + 0.24, y + 0.1, x + 0.24, y - 0.05))


X = [W / 2, W + G + W / 2]
Y = [H + G + H / 2, H / 2]

# 1 Autonomia: documento com caixa marcada e assinatura
cx, cy = X[0], Y[0]
cartao(cx, cy, "dblue", "Autonomia", r"decidir \textbf{livremente}, com informação")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dblue, fill=white, line width=1.6pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.75, iy - 0.95, ix + 0.75, iy + 1.0))
out.append(r"\draw[dblue, line width=1.3pt] (%.2f,%.2f) rectangle ++(0.3,0.3);" % (ix - 0.5, iy + 0.45))
out.append(r"\draw[dgreen, line width=2.2pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.46, iy + 0.58, ix - 0.38, iy + 0.48, ix - 0.14, iy + 0.82))
out.append(r"\draw[black!50, line width=1.1pt] (%.2f,%.2f) -- ++(0.7,0) (%.2f,%.2f) -- ++(0.55,0);" % (ix - 0.0, iy + 0.55, ix - 0.0, iy + 0.28))
out.append(r"\draw[dblue, line width=1.5pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f);" % (ix - 0.5, iy - 0.55, ix - 0.3, iy - 0.2, ix - 0.1, iy - 0.8, ix + 0.05, iy - 0.5, ix + 0.2, iy - 0.2, ix + 0.35, iy - 0.7, ix + 0.55, iy - 0.45))
out.append(r"\draw[black!50, line width=1pt] (%.2f,%.2f) -- ++(1.1,0);" % (ix - 0.55, iy - 0.7))

# 2 Beneficência: balança desequilibrada, benefícios pesam mais
cx, cy = X[1], Y[0]
cartao(cx, cy, "dgreen", "Beneficência", r"máximo de \textbf{benefício}, mínimo de risco")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dgreen, line width=2pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix, iy - 0.85, ix, iy + 0.75))
out.append(r"\draw[dgreen, line width=1.6pt, fill=dgreen!15!white] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;" % (ix - 0.45, iy - 0.85, ix + 0.45, iy - 0.85, ix, iy - 0.4))
out.append(r"\draw[dgreen, line width=2.4pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 1.4, iy + 0.45, ix + 1.4, iy + 1.0))
prato(ix - 1.4, iy + 0.45, "dgreen"); prato(ix + 1.4, iy + 1.0, "dred")
out.append(r"\node[font=\large\bfseries, dgreen] at (%.2f,%.2f) {benefícios};" % (ix - 1.75, iy - 0.75))
out.append(r"\node[font=\large\bfseries, dred] at (%.2f,%.2f) {riscos};" % (ix + 1.4, iy - 0.2))

# 3 Não maleficência: escudo com visto
cx, cy = X[0], Y[1]
cartao(cx, cy, "dorange", "Não maleficência", r"evitar danos \textbf{previsíveis}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dorange, fill=dorange!12!white, line width=1.8pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (ix - 0.8, iy + 0.95, ix + 0.8, iy + 0.95, ix + 0.8, iy + 0.1, ix + 0.8, iy - 0.55, ix + 0.25, iy - 0.9, ix, iy - 1.0, ix - 0.25, iy - 0.9, ix - 0.8, iy - 0.55, ix - 0.8, iy + 0.1))
out.append(r"\draw[dorange, line width=3pt, line cap=round, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.4, iy + 0.0, ix - 0.1, iy - 0.35, ix + 0.45, iy + 0.35))

# 4 Justiça e equidade: balança em equilíbrio com pessoas
cx, cy = X[1], Y[1]
cartao(cx, cy, "dred", "Justiça e equidade", r"benefícios e ônus \textbf{bem repartidos}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dred, line width=2pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix, iy - 0.85, ix, iy + 0.8))
out.append(r"\draw[dred, line width=1.6pt, fill=dred!15!white] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;" % (ix - 0.45, iy - 0.85, ix + 0.45, iy - 0.85, ix, iy - 0.4))
out.append(r"\draw[dred, line width=2.4pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 1.4, iy + 0.8, ix + 1.4, iy + 0.8))
prato(ix - 1.4, iy + 0.8, "dred"); prato(ix + 1.4, iy + 0.8, "dred")
pessoa_mini(ix - 1.4, iy + 0.0, "dred"); pessoa_mini(ix + 1.4, iy + 0.0, "dred")

open("principios-icones.tex", "w").write(CAB + "\n".join(out) + "\n\\end{tikzpicture}\n\\end{document}\n")
