"""Gera fontes-informacao.tex (slide 'Como achar as fontes de informação')."""
W, GAP, H = 6.3, 0.4, 3.1
X = [W / 2, W + GAP + W / 2]
TOT = 2 * W + GAP


def cell(cx, cy, cor, icone, texto):
    s = r"\node[dbox, draw=%s, line width=1.4pt, minimum width=%.1fcm, minimum height=%.1fcm] at (%.2f,%.2f) {};" % (cor, W, H, cx, cy)
    s += "\n" + icone
    s += "\n" + r"\node[font=\Large, text width=%.1fcm, align=center] at (%.2f,%.2f) {%s};" % (W - 0.6, cx, cy - 0.85, texto)
    return s


def pessoa(x, y, c):
    return (r"\fill[%s!25!white, draw=%s, line width=1.4pt] (%.2f,%.2f) circle (0.3);" % (c, c, x, y + 0.5) + "\n" +
            r"\fill[%s!25!white, draw=%s, line width=1.4pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f) -- cycle;" % (c, c, x - 0.58, y - 0.45, x - 0.58, y + 0.1, x + 0.58, y + 0.1, x + 0.58, y - 0.45))


def rosto(x, y, c, feliz):
    s = r"\draw[%s, line width=1.3pt, fill=%s!15!white] (%.2f,%.2f) circle (0.3);" % (c, c, x, y)
    s += "\n" + r"\fill[%s] (%.2f,%.2f) circle (0.04) (%.2f,%.2f) circle (0.04);" % (c, x - 0.1, y + 0.07, x + 0.1, y + 0.07)
    y0, y1 = (-0.08, -0.2) if feliz else (-0.17, -0.05)
    s += "\n" + r"\draw[%s, line width=1.1pt] (%.2f,%.2f) .. controls (%.2f,%.2f) and (%.2f,%.2f) .. (%.2f,%.2f);" % (c, x - 0.14, y + y0, x - 0.06, y + y1, x + 0.06, y + y1, x + 0.14, y + y0)
    return s


def sec(y, cor, titulo):
    return (r"\node[font=\Large\bfseries, %s] at (%.2f,%.2f) {%s};" % (cor, TOT / 2, y, titulo) + "\n" +
            r"\draw[%s, line width=1.4pt] (0,%.2f) -- (%.2f,%.2f);" % (cor, y - 0.5, TOT, y - 0.5))


R1, R2, R3 = 9.6, 6.3, 1.9
ty = [sec(12.0, "dblue", "Sistema novo"),
      cell(X[0], R1, "dblue", pessoa(X[0], R1 + 0.5, "dblue"), r"quem \textbf{usará}"),
      cell(X[1], R1, "dblue", r"\draw[dblue, dashed, line width=1.2pt] (%.2f,%.2f) circle (0.85);" % (X[1], R1 + 0.58) + "\n" + pessoa(X[1], R1 + 0.5, "dblue"), r"quem será \textbf{afetado}"),
      cell(X[0], R2, "dblue", pessoa(X[0], R2 + 0.5, "dblue") + "\n" + r"\node[font=\huge, dorange] at (%.2f,%.2f) {$\star$};" % (X[0] + 0.95, R2 + 0.85), r"quem \textbf{decide}")]
proc = "\n".join([r"\draw[dblue, fill=dblue!15!white, line width=1.1pt] (%.2f,%.2f) rectangle ++(0.56,0.5);" % (X[1] + dx - 0.28, R2 + 0.3) for dx in (-0.95, 0, 0.95)] +
                 [r"\draw[dblue, -{Stealth[length=1.8mm]}, line width=1.1pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (X[1] - 0.62, R2 + 0.55, X[1] - 0.35, R2 + 0.55),
                  r"\draw[dblue, -{Stealth[length=1.8mm]}, line width=1.1pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (X[1] + 0.33, R2 + 0.55, X[1] + 0.6, R2 + 0.55)])
ty += [cell(X[1], R2, "dblue", proc, r"quem definiu os \textbf{processos}"),
       sec(4.2, "dgreen", "Sistema existente"),
       cell(X[0], R3, "dgreen", pessoa(X[0] - 0.7, R3 + 0.5, "dgreen") + "\n" + rosto(X[0] + 0.75, R3 + 0.85, "dgreen", True) + "\n" + rosto(X[0] + 0.75, R3 + 0.15, "dred", False), r"quem \textbf{usa hoje}")]
fone = (pessoa(X[1], R3 + 0.5, "dgreen") + "\n" + r"\draw[dgreen, line width=1.6pt] (%.2f,%.2f) arc (180:0:0.4);" % (X[1] - 0.4, R3 + 0.98) + "\n" +
        r"\fill[dgreen] (%.2f,%.2f) rectangle ++(0.14,0.3) (%.2f,%.2f) rectangle ++(0.14,0.3);" % (X[1] - 0.47, R3 + 0.8, X[1] + 0.33, R3 + 0.8))
ty.append(cell(X[1], R3, "dgreen", fone, r"\textbf{suporte}, \textbf{treino} e \textbf{manutenção}"))
CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
open("fontes-informacao.tex", "w").write(CAB + "\n".join(ty) + "\n\\end{tikzpicture}\n\\end{document}\n")
