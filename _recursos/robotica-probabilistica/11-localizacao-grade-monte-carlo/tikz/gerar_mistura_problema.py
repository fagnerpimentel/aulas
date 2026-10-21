"""Gera mistura-problema.tex: sensor ruidoso x sensor muito preciso (palpites do movimento)."""
import math, random
random.seed(7)
N = 70
pts = [(random.gauss(3.2, 1.05), random.gauss(2.6, 0.85)) for _ in range(N)]
pts = [(x, y) for x, y in pts if 0.35 < x < 6.65 and 0.35 < y < 4.65]
# centro da região aceita: dentro da nuvem, mas sem nenhum palpite a menos de 0.30 (caso preciso)
best = None
for cx in [i * 0.05 for i in range(60, 130)]:
    for cy in [j * 0.05 for j in range(40, 90)]:
        dmin = min(math.hypot(cx - x, cy - y) for x, y in pts)
        dentro_a = sum(1 for x, y in pts if ((x - cx) / 1.25) ** 2 + ((y - cy) / 0.95) ** 2 <= 1)
        if dmin > 0.34 and dentro_a >= 7:
            sc = dentro_a - 0.5 * math.hypot(cx - 3.2, cy - 2.6)
            if best is None or sc > best[0]:
                best = (sc, cx, cy, dmin, dentro_a)
_, cx, cy, dmin, dentro_a = best
print("centro", cx, cy, "dmin", round(dmin, 2), "dentro(a)", dentro_a)

CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
out = []
PW, PH, GAP = 7.0, 5.0, 1.2

def painel(ox, preciso):
    cor = "dred" if preciso else "dgreen"
    titulo = "sensor muito preciso" if preciso else "sensor ruidoso"
    out.append(r"\node[font=\Large\bfseries, %s] at (%.2f,%.2f) {%s};" % (cor, ox + PW / 2, PH + 0.6, titulo))
    out.append(r"\draw[black!70, fill=white, line width=1.2pt] (%.2f,0) rectangle (%.2f,%.2f);" % (ox, ox + PW, PH))
    # região aceita pelo sensor
    if preciso:
        out.append(r"\draw[dorange, fill=dorange!45!white, line width=1.6pt] (%.2f,%.2f) circle (0.2);" % (ox + cx, cy))
    else:
        out.append(r"\draw[dorange, fill=dorange!22!white, line width=1.6pt] (%.2f,%.2f) ellipse (1.25 and 0.95);" % (ox + cx, cy))
    # palpites do movimento
    for x, y in pts:
        dentro = (not preciso) and ((x - cx) / 1.25) ** 2 + ((y - cy) / 0.95) ** 2 <= 1
        c = "dgreen" if dentro else "dblue!55!white"
        r = 0.13 if dentro else 0.10
        out.append(r"\fill[%s, draw=%s!80!black, line width=0.3pt] (%.2f,%.2f) circle (%.2f);" % (c, "dgreen" if dentro else "dblue", ox + x, y, r))
    out.append(r"\node[font=\large, dorange, anchor=south west, fill=white, inner sep=1pt] at (%.2f,%.2f) {poses que o sensor aceita};" % (ox + (cx + 0.45 if preciso else cx + 0.2), cy + (0.1 if preciso else 1.0)) if False else "")
    legenda = r"\textbf{nenhum} palpite cai na região: notas $\approx 0$" if preciso else r"\textbf{muitos} palpites caem na região: boas notas"
    out.append(r"\node[font=\Large, text width=%.1fcm, align=center] at (%.2f,%.2f) {%s};" % (PW, ox + PW / 2, -0.95, legenda))

painel(0, False)
painel(PW + GAP, True)
# rótulo da região aceita (um só, no painel da direita) e legenda das cores
ox = PW + GAP
out.append(r"\draw[dorange, line width=1.3pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + cx + 0.18, cy + 0.12, ox + cx + 1.0, cy + 1.2))
out.append(r"\node[font=\large, dorange, anchor=west, fill=white, inner sep=1pt] at (%.2f,%.2f) {região aceita};" % (ox + cx + 0.95, cy + 1.3))
out.append(r"\draw[dorange, line width=1.3pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (cx + 0.9, cy + 0.45, cx + 1.4, cy + 1.45))
out.append(r"\node[font=\large, dorange, anchor=south, fill=white, inner sep=1pt] at (%.2f,%.2f) {região aceita};" % (cx + 1.4, cy + 1.45))
out.append(r"\fill[dblue!55!white, draw=dblue, line width=0.3pt] (0.2,%.2f) circle (0.1); \node[font=\large, anchor=west] at (0.4,%.2f) {palpite do movimento};" % (-1.9, -1.9))
out.append(r"\fill[dgreen, draw=dgreen!80!black, line width=0.3pt] (6.2,%.2f) circle (0.13); \node[font=\large, anchor=west] at (6.45,%.2f) {palpite com boa nota};" % (-1.9, -1.9))
out.append(r"\fill[dorange!35!white, draw=dorange, line width=1.2pt] (11.0,%.2f) circle (0.14); \node[font=\large, anchor=west] at (11.3,%.2f) {poses que a medição aceita};" % (-1.9, -1.9))
open("mistura-problema.tex", "w").write(CAB + "\n".join(o for o in out if o) + "\n\\end{tikzpicture}\n\\end{document}\n")
