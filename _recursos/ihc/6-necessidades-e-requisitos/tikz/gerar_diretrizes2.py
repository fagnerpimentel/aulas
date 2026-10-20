"""Gera diretrizes2-icones.tex (slide 'Diretrizes para a pesquisa (continuação)')."""
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


X = [W / 2, W + G + W / 2]
Y = [H + G + H / 2, H / 2]

# 1 Consentimento: termo com duas assinaturas
cx, cy = X[0], Y[0]
cartao(cx, cy, "dblue", "Consentimento", r"termo assinado; menores: \textbf{o responsável}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dblue, fill=white, line width=1.6pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.85, iy - 0.95, ix + 0.85, iy + 1.0))
for k in range(2):
    out.append(r"\draw[black!45, line width=1.2pt] (%.2f,%.2f) -- ++(%.2f,0);" % (ix - 0.55, iy + 0.65 - 0.3 * k, 1.1 if k == 0 else 0.8))
for k, dy in enumerate((0.0, -0.55)):
    y0 = iy - 0.1 + dy
    out.append(r"\draw[dblue, line width=1.5pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f);" % (ix - 0.55, y0, ix - 0.4, y0 + 0.28, ix - 0.25, y0 - 0.2, ix - 0.1, y0 + 0.05, ix + 0.05, y0 + 0.25, ix + 0.2, y0 - 0.2, ix + 0.5, y0 + 0.05))
    out.append(r"\draw[black!45, line width=1pt] (%.2f,%.2f) -- ++(1.1,0);" % (ix - 0.55, y0 - 0.2))

# 2 Conforto: xícara com vapor
cx, cy = X[1], Y[0]
cartao(cx, cy, "dgreen", "Conforto", r"pausas e respeito; avalia-se \textbf{o produto, não a pessoa}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dgreen, fill=dgreen!15!white, line width=1.8pt, rounded corners=5pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.7, iy - 0.7, ix + 0.4, iy + 0.25))
out.append(r"\draw[dgreen, line width=1.8pt] (%.2f,%.2f) arc (90:-90:0.3 and 0.28);" % (ix + 0.4, iy + 0.05))
out.append(r"\draw[dgreen, line width=1.8pt, line cap=round] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 1.0, iy - 0.82, ix + 0.7, iy - 0.82))
for dx in (-0.45, -0.15, 0.15):
    out.append(r"\draw[dgreen, line width=1.4pt, line cap=round] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f);" % (ix + dx, iy + 0.4, ix + dx - 0.15, iy + 0.62, ix + dx + 0.15, iy + 0.8, ix + dx, iy + 1.02))

# 3 Liberdade de desistir: porta aberta com seta de saída
cx, cy = X[0], Y[1]
cartao(cx, cy, "dorange", "Liberdade de desistir", r"a qualquer momento, \textbf{sem penalidade}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dorange, fill=white, line width=1.8pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.8, iy - 0.9, ix + 0.0, iy + 0.95))
out.append(r"\draw[dorange, fill=dorange!20!white, line width=1.6pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;" % (ix - 0.8, iy - 0.9, ix - 0.35, iy - 0.7, ix - 0.35, iy + 0.75, ix - 0.8, iy + 0.95))
out.append(r"\draw[dgreen, line width=3pt, -{Stealth[length=4mm]}] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.1, iy - 0.05, ix + 1.45, iy - 0.05))

# 4 Incentivos: ônibus (ressarcir) e moeda riscada (não pagar)
cx, cy = X[1], Y[1]
cartao(cx, cy, "dred", "Incentivos", r"só \textbf{ressarcir despesas} (transporte, alimentação)")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dred, fill=dred!12!white, line width=1.8pt, rounded corners=5pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 1.45, iy - 0.5, ix - 0.15, iy + 0.5))
for k in range(2):
    out.append(r"\draw[dred, fill=white, line width=1.2pt] (%.2f,%.2f) rectangle ++(0.4,0.32);" % (ix - 1.3 + 0.55 * k, iy + 0.1))
out.append(r"\fill[dred] (%.2f,%.2f) circle (0.14) (%.2f,%.2f) circle (0.14);" % (ix - 1.1, iy - 0.5, ix - 0.5, iy - 0.5))
out.append(r"\draw[dgreen, line width=2.6pt, line cap=round, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 1.0, iy + 0.78, ix - 0.88, iy + 0.66, ix - 0.62, iy + 0.98))
out.append(r"\draw[black!70, fill=white, line width=1.6pt] (%.2f,%.2f) circle (0.55);" % (ix + 0.95, iy))
out.append(r"\node[font=\large\bfseries, black!70] at (%.2f,%.2f) {R\$};" % (ix + 0.95, iy))
out.append(r"\draw[dred, line width=3pt, line cap=round] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix + 0.5, iy - 0.6, ix + 1.4, iy + 0.6))

open("diretrizes2-icones.tex", "w").write(CAB + "\n".join(out) + "\n\\end{tikzpicture}\n\\end{document}\n")
