"""Gera outras-fontes.tex (slide 'Outras fontes de informação'): quatro faixas empilhadas."""
W, H, PASSO = 7.6, 3.6, 3.85
CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
out = []
CX = W / 2
U0 = 0.15              # início da área do desenho (ocupa a largura do cartão)


def faixa(cy, cor, titulo, legenda):
    out.append(r"\node[dbox, draw=%s, line width=1.5pt, minimum width=%.1fcm, minimum height=%.2fcm] at (%.2f,%.2f) {};" % (cor, W, H, CX, cy))
    out.append(r"\node[font=\Large\bfseries, %s] at (%.2f,%.2f) {%s};" % (cor, CX, cy + 1.45, titulo))
    out.append(r"\node[font=\Large, text width=%.1fcm, align=center] at (%.2f,%.2f) {%s};" % (W - 0.4, CX, cy - 1.5, legenda))


# A: suporte
cy = 3 * PASSO + H / 2
faixa(cy, "dblue", "Suporte aos usuários", r"problemas \textbf{mais comuns}")
x, y = U0 + 1.0, cy
out.append(r"\fill[dblue!25!white, draw=dblue, line width=1.4pt] (%.2f,%.2f) circle (0.36);" % (x, y + 0.45))
out.append(r"\fill[dblue!25!white, draw=dblue, line width=1.4pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (x - 0.7, y - 0.65, x - 0.7, y + 0.0, x + 0.7, y + 0.0, x + 0.7, y - 0.65))
out.append(r"\draw[dblue, line width=1.8pt] (%.2f,%.2f) arc (180:0:0.44);" % (x - 0.44, y + 0.55))
out.append(r"\fill[dblue] (%.2f,%.2f) rectangle ++(0.16,0.32) (%.2f,%.2f) rectangle ++(0.16,0.32);" % (x - 0.52, y + 0.35, x + 0.36, y + 0.35))
for i, t in enumerate(("erro", "dúvida", "pedido")):
    out.append(r"\node[draw=dblue, rounded corners=8pt, fill=white, line width=1.2pt, minimum width=2.6cm, minimum height=0.55cm, font=\large] at (%.2f,%.2f) {%s};" % (U0 + 4.4, cy + 0.65 - i * 0.65, t))

# B: logs
cy = 2 * PASSO + H / 2
faixa(cy, "dgreen", "Logs de uso", r"o \textbf{quê}, não o \textbf{porquê}")
x0, ya = U0 + 0.3, cy - 0.3
out.append(r"\draw[black!60, line width=1.2pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (x0 - 0.1, ya, U0 + 6.9, ya))
vals = [1, 2, 2, 3, 3, 4, 18]
seen = {}
for v in vals:
    k = seen.get(v, 0); seen[v] = k + 1
    out.append(r"\fill[dgreen] (%.2f,%.2f) circle (0.13);" % (x0 + 0.3 * v, ya + 0.2 + 0.28 * k))
med, mean = 3, sum(vals) / len(vals)
out.append(r"\draw[dgreen, line width=2pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (x0 + 0.3 * med, ya - 0.1, x0 + 0.3 * med, ya + 0.85))
out.append(r"\node[font=\large\bfseries, dgreen, anchor=south] at (%.2f,%.2f) {mediana};" % (x0 + 0.3 * med, ya + 0.85))
out.append(r"\fill[dred] (%.2f,%.2f) -- ++(-0.14,-0.28) -- ++(0.28,0) -- cycle;" % (x0 + 0.3 * mean, ya - 0.03))
out.append(r"\node[font=\large\bfseries, dred, anchor=north] at (%.2f,%.2f) {média};" % (x0 + 0.3 * mean + 0.3, ya - 0.33))
out.append(r"\node[font=\large, black!65, anchor=south] at (%.2f,%.2f) {valor extremo};" % (x0 + 0.3 * 18 - 0.2, ya + 0.4))

# C: análise competitiva
cy = 1 * PASSO + H / 2
faixa(cy, "dorange", "Análise competitiva", r"a \textbf{experiência do usuário}")
out.append(r"\node[dbox, draw=dorange, fill=dorange!12!white, line width=1.6pt, minimum width=2.5cm, minimum height=0.8cm, font=\large] (n) at (%.2f,%.2f) {nosso produto};" % (U0 + 3.65, cy + 0.3))
for dx, dy, t in ((-2.7, 0.3, "concorrente"), (2.7, 0.3, "substituto"), (0.0, -0.7, "complementar")):
    nm = t[:3]
    out.append(r"\node[dbox, draw=black!60, line width=1.2pt, minimum width=1.9cm, minimum height=0.7cm, font=\normalsize, inner sep=3pt] (%s) at (%.2f,%.2f) {%s};" % (nm, U0 + 3.65 + dx, cy + dy, t))
    out.append(r"\draw[black!55, line width=1.2pt] (n) -- (%s);" % nm)

# D: documentação e uso
cy = H / 2
faixa(cy, "dred", "Normas e uso", r"o que \textbf{limita} e o que se \textbf{sente}")
x, y = U0 + 1.5, cy + 0.2
out.append(r"\draw[dred, fill=white, line width=1.4pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;" % (x - 0.5, y - 0.65, x - 0.5, y + 0.8, x + 0.2, y + 0.8, x + 0.5, y + 0.5, x + 0.5, y - 0.65))
out.append(r"\draw[dred, line width=1pt] (%.2f,%.2f) -- ++(0,-0.3) -- ++(0.3,0);" % (x + 0.2, y + 0.8))
for k in range(4):
    out.append(r"\draw[black!50, line width=1pt] (%.2f,%.2f) -- ++(%.2f,0);" % (x - 0.32, y + 0.3 - 0.24 * k, 0.64 if k < 3 else 0.36))
out.append(r"\node[font=\large, anchor=north] at (%.2f,%.2f) {normas};" % (x, y - 0.7))
x = U0 + 5.3
out.append(r"\draw[dred, fill=dred!15!white, line width=1.4pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;" % (x - 0.3, y + 0.8, x - 0.3, y - 0.45, x - 0.04, y - 0.2, x + 0.18, y - 0.72, x + 0.4, y - 0.62, x + 0.18, y - 0.1, x + 0.52, y - 0.1))
out.append(r"\node[font=\large, anchor=north] at (%.2f,%.2f) {usar você mesmo};" % (x, y - 0.75))

open("outras-fontes.tex", "w").write(CAB + "\n".join(out) + "\n\\end{tikzpicture}\n\\end{document}\n")
