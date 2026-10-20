"""Gera quanti-quali.tex (slide 'Quantitativo e qualitativo')."""
W, H, G = 6.5, 5.9, 0.3
CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
out = []
FB = 2.1                         # altura da faixa inferior
CY = FB + G + H / 2              # centro dos cartões
TOT = 2 * W + G


def cartao(cx, cor, titulo, sub):
    out.append(r"\node[dbox, draw=%s, line width=1.6pt, minimum width=%.1fcm, minimum height=%.1fcm] at (%.2f,%.2f) {};" % (cor, W, H, cx, CY))
    out.append(r"\node[font=\Large\bfseries, %s] at (%.2f,%.2f) {%s};" % (cor, cx, CY + 2.45, titulo))
    out.append(r"\node[font=\large, black!70] at (%.2f,%.2f) {%s};" % (cx, CY + 1.95, sub))


# quantitativos
cx = W / 2
cartao(cx, "dblue", "Quantitativos", "viram \\textbf{número} (escala Likert)")
for k, h in enumerate((0.7, 1.3, 1.0, 1.5)):
    out.append(r"\draw[dblue, fill=dblue!25!white, line width=1.4pt] (%.2f,%.2f) rectangle ++(0.5,%.2f);" % (cx - 1.5 + 0.7 * k, CY - 0.1, h))
out.append(r"\draw[black!55, line width=1.3pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (cx - 1.75, CY + 1.45, cx - 1.75, CY - 0.1, cx + 1.45, CY - 0.1))
out.append(r"\node[font=\large, black!65, anchor=east] at (%.2f,%.2f) {};" % (cx - 1.9, CY))
for k, v in enumerate(("4", "5", "3", "5")):
    out.append(r"\node[draw=dblue, fill=white, line width=1.2pt, minimum width=0.75cm, minimum height=0.65cm, font=\Large] at (%.2f,%.2f) {%s};" % (cx - 1.2 + 0.8 * k, CY - 0.85, v))
out.append(r"\node[font=\large, text width=%.1fcm, align=center] at (%.2f,%.2f) {\textbf{quais, quando, onde e quem}};" % (W - 0.4, cx, CY - 1.85))

# qualitativos
cx = W + G + W / 2
cartao(cx, "dgreen", "Qualitativos", "\\textbf{textos} e multimídia")
for dx, dy, w in ((-0.9, 0.95, 2.6), (0.55, 0.0, 2.6)):
    out.append(r"\draw[dgreen, fill=white, line width=1.4pt, rounded corners=6pt] (%.2f,%.2f) rectangle ++(%.2f,0.75);" % (cx + dx - 1.0, CY + dy - 0.1, w))
    out.append(r"\draw[black!45, line width=1.3pt] (%.2f,%.2f) -- ++(1.5,0) (%.2f,%.2f) -- ++(0.9,0);" % (cx + dx - 0.8, CY + dy + 0.45, cx + dx - 0.8, CY + dy + 0.18))
    out.append(r"\fill[dorange!55!white] (%.2f,%.2f) rectangle ++(0.6,0.14);" % (cx + dx + 0.75, CY + dy + 0.38))
out.append(r"\node[draw=dgreen, fill=white, line width=1.2pt, rounded corners=3pt, font=\large, minimum height=0.65cm, minimum width=1.2cm] (a) at (%.2f,%.2f) {Ana};" % (cx - 1.5, CY - 0.85))
out.append(r"\node[draw=dgreen, fill=dgreen!12!white, line width=1.2pt, rounded corners=3pt, font=\large\bfseries, minimum height=0.65cm, minimum width=1.2cm] (b) at (%.2f,%.2f) {P07};" % (cx - 0.1, CY - 0.85))
out.append(r"\draw[dgreen, line width=1.6pt, -{Stealth[length=2.6mm]}] (a) -- (b);")
out.append(r"\node[font=\large, dgreen, anchor=west] at (%.2f,%.2f) {anonimizar};" % (cx + 0.65, CY - 0.85))
out.append(r"\node[font=\large, text width=%.1fcm, align=center] at (%.2f,%.2f) {\textbf{o quê, como e por quê}};" % (W - 0.4, cx, CY - 1.85))

# faixa inferior: ordem de análise
fy = FB / 2
bw, gap = 3.75, 0.7
for i, (cor, t) in enumerate((("dblue", r"1º \textbf{quantitativo}"), ("dgreen", r"2º \textbf{qualitativo}"), ("dorange", r"\textbf{cruzar} os dois"))):
    x = bw / 2 + i * (bw + gap) + (TOT - (3 * bw + 2 * gap)) / 2
    out.append(r"\node[dbox, draw=%s, line width=1.6pt, minimum width=%.2fcm, minimum height=1.5cm, font=\Large] (f%d) at (%.2f,%.2f) {%s};" % (cor, bw, i, x, fy, t))
    if i:
        out.append(r"\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (f%d.east) -- (f%d.west);" % (i - 1, i))

open("quanti-quali.tex", "w").write(CAB + "\n".join(out) + "\n\\end{tikzpicture}\n\\end{document}\n")
