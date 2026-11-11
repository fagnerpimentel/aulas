CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
RODA = "\n\\end{tikzpicture}\n\\end{document}\n"
def w(n, body): open(n + ".tex", "w").write(CAB + body.strip("\n") + RODA)


CS = ["dblue", "dgreen", "dorange", "dred"]

def boxes(items, w=3.9, h=3.0, cols=4, cap=None, capw=17, font=r"\large"):
    st = 0.6 + w
    o = [r"\tikzset{c/.style={dbox, text width=%scm, minimum height=%scm, font=%s, line width=1.4pt}}" % (w, h, font)]
    n = len(items)
    rows = (n + cols - 1) // cols
    for i, (t, x) in enumerate(items):
        r, c = divmod(i, cols)
        col = CS[i % 4]
        o.append(r"\node[c, draw=%s] at (%s,%s) {\textbf{\textcolor{%s}{%s}}\\ %s};" % (col, round(c * st, 2), round(-r * (h + 0.5), 2), col, t, x))
    if cap:
        used = min(n, cols)
        o.append(r"\node[font=\Large, text width=%scm, align=center] at (%s,%s) {%s};" % (capw, round((used - 1) * st / 2, 2), round(-(rows - 1) * (h + 0.5) - h / 2 - 1.0, 2), cap))
    return "\n".join(o)

def flow(items, w=3.5, h=3.0, cap=None, capw=17, font=r"\large"):
    st = 0.6 + w
    o = [r"\tikzset{c/.style={dbox, text width=%scm, minimum height=%scm, font=%s, line width=1.4pt}}" % (w, h, font)]
    for i, (t, x) in enumerate(items):
        col = CS[i % 4]
        o.append(r"\node[c, draw=%s] (n%d) at (%s,0) {\textbf{\textcolor{%s}{%d. %s}}\\ %s};" % (col, i, round(i * (st + 0.2), 2), col, i + 1, t, x))
    for i in range(len(items) - 1):
        o.append(r"\draw[dtrans, line width=2pt, -{Stealth[length=3mm]}] (n%d.east) -- (n%d.west);" % (i, i + 1))
    if cap:
        o.append(r"\node[font=\Large, text width=%scm, align=center] at (%s,%s) {%s};" % (capw, round((len(items) - 1) * (st + 0.2) / 2, 2), round(-h / 2 - 1.0, 2), cap))
    return "\n".join(o)
import math, random

# ---------- utilidades de grade ----------
