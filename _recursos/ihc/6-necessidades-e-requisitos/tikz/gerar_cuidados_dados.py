"""Gera cuidados-dados.tex (slide 'Cuidados com os dados'): quatro cartões com ícone."""
W, H, G = 6.6, 5.5, 0.3
CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
out = []


def cartao(cx, cy, cor, titulo, frase, fonte=r"\Large"):
    out.append(r"\node[dbox, draw=%s, line width=1.6pt, minimum width=%.1fcm, minimum height=%.1fcm] at (%.2f,%.2f) {};" % (cor, W, H, cx, cy))
    out.append(r"\node[font=\Large\bfseries, %s] at (%.2f,%.2f) {%s};" % (cor, cx, cy - 1.0, titulo))
    out.append(r"\node[font=%s, text width=%.1fcm, align=center, anchor=north] at (%.2f,%.2f) {%s};" % (fonte, W - 0.6, cx, cy - 1.35, frase))


X = [W / 2, W + G + W / 2]
Y = [H + G + H / 2, H / 2]

# 1 Válidos e confiáveis: gráfico de barras com visto
cx, cy = X[0], Y[0]
cartao(cx, cy, "dblue", "Válidos e confiáveis", r"dados distorcidos levam a \textbf{decisões ruins}")
ix, iy = cx, cy + 0.9
out.append(r"\draw[black!55, line width=1.4pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 1.3, iy + 0.95, ix - 1.3, iy - 0.8, ix + 0.4, iy - 0.8))
for k, h in enumerate((0.8, 1.35, 1.0)):
    out.append(r"\draw[dblue, fill=dblue!25!white, line width=1.5pt] (%.2f,%.2f) rectangle ++(0.42,%.2f);" % (ix - 1.1 + 0.55 * k, iy - 0.8, h))
out.append(r"\draw[dgreen, fill=white, line width=1.6pt] (%.2f,%.2f) circle (0.55);" % (ix + 0.95, iy + 0.2))
out.append(r"\draw[dgreen, line width=3.2pt, line cap=round, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix + 0.68, iy + 0.2, ix + 0.88, iy - 0.02, ix + 1.25, iy + 0.45))

# 2 Tendenciosidade: pergunta que induz
cx, cy = X[1], Y[0]
cartao(cx, cy, "dgreen", "Sem tendenciosidade", r"perguntas e reações podem \textbf{influenciar as respostas}")
ix, iy = cx, cy + 0.9
out.append(r"\fill[dgreen!25!white, draw=dgreen, line width=1.5pt] (%.2f,%.2f) circle (0.32);" % (ix - 1.35, iy + 0.45))
out.append(r"\fill[dgreen!25!white, draw=dgreen, line width=1.5pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (ix - 1.95, iy - 0.5, ix - 1.95, iy + 0.1, ix - 0.75, iy + 0.1, ix - 0.75, iy - 0.5))
out.append(r"\draw[dgreen, fill=white, line width=1.5pt, rounded corners=7pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 0.45, iy - 0.2, ix + 2.35, iy + 1.0))
out.append(r"\draw[white, line width=2.6pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.45, iy + 0.15, ix - 0.45, iy + 0.5))
out.append(r"\draw[dgreen, line width=1.5pt, line join=round] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ix - 0.45, iy + 0.15, ix - 0.72, iy + 0.3, ix - 0.45, iy + 0.5))
out.append(r"\node[font=\Large, black!75] at (%.2f,%.2f) {\textbf{Ótimo}, né?};" % (ix + 0.95, iy + 0.4))
out.append(r"\draw[dred, line width=2pt, -{Stealth[length=3mm]}] (%.2f,%.2f) -- (%.2f,%.2f);" % (ix + 0.0, iy - 0.55, ix + 1.7, iy - 0.55))
out.append(r"\node[font=\normalsize, dred, anchor=north] at (%.2f,%.2f) {resposta empurrada};" % (ix + 0.85, iy - 0.62))

# 3 Dados inválidos: linha descartada
cx, cy = X[0], Y[1]
cartao(cx, cy, "dorange", "Dados inválidos", r"\textbf{descartar} e informar as \textbf{limitações}")
ix, iy = cx, cy + 0.9
for k in range(4):
    y = iy + 0.75 - 0.5 * k
    ruim = (k == 2)
    out.append(r"\draw[%s, fill=%s, line width=1.3pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % ("dred" if ruim else "black!45", "dred!12!white" if ruim else "white", ix - 1.25, y - 0.22, ix + 1.25, y + 0.22))
    out.append(r"\fill[%s] (%.2f,%.2f) circle (0.08);" % ("dred" if ruim else "black!55", ix - 1.0, y))
    out.append(r"\draw[%s, line width=1.6pt] (%.2f,%.2f) -- ++(%.2f,0);" % ("dred" if ruim else "black!40", ix - 0.75, y, 1.5 if k != 1 else 1.0))
out.append(r"\draw[dred, line width=3pt, line cap=round] (%.2f,%.2f) -- (%.2f,%.2f) (%.2f,%.2f) -- (%.2f,%.2f);" % (ix + 0.78, iy - 0.13, ix + 1.08, iy - 0.37, ix + 0.78, iy - 0.37, ix + 1.08, iy - 0.13))

# 4 Reter e proteger: calendário + cadeado
cx, cy = X[1], Y[1]
cartao(cx, cy, "dred", "Reter e proteger", r"só enquanto relevantes; às vezes, \textbf{acordo de confidencialidade}", r"\large")
ix, iy = cx, cy + 0.9
out.append(r"\draw[dred, fill=white, line width=1.6pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 1.5, iy - 0.7, ix - 0.1, iy + 0.85))
out.append(r"\fill[dred] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix - 1.5, iy + 0.45, ix - 0.1, iy + 0.85))
for r in range(3):
    for c in range(3):
        out.append(r"\fill[black!45] (%.2f,%.2f) rectangle ++(0.2,0.14);" % (ix - 1.35 + 0.4 * c, iy + 0.12 - 0.3 * r))
out.append(r"\draw[dred, line width=3pt] (%.2f,%.2f) -- (%.2f,%.2f) arc (180:0:0.38) -- (%.2f,%.2f);" % (ix + 0.55, iy + 0.0, ix + 0.55, iy + 0.25, ix + 1.31, iy + 0.0))
out.append(r"\draw[dred, fill=dred!20!white, line width=1.8pt, rounded corners=4pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ix + 0.25, iy - 0.7, ix + 1.61, iy + 0.05))
out.append(r"\fill[dred] (%.2f,%.2f) circle (0.11);" % (ix + 0.93, iy - 0.3))

open("cuidados-dados.tex", "w").write(CAB + "\n".join(out) + "\n\\end{tikzpicture}\n\\end{document}\n")
