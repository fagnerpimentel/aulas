H = "\\documentclass[border=3pt]{standalone}\n\\input{preamble}\n\\usetikzlibrary{shapes.callouts}\n\\begin{document}\n"
T = "\n\\end{document}\n"
BAL=r"bal/.style={rectangle callout, rounded corners=7pt, draw=black!75, fill=white, line width=1pt, align=center, font=\normalsize, inner sep=5pt}"
def w(name, body, opts=""):
    open(name+".tex","w").write(H+r"\begin{tikzpicture}[x=1cm,y=1cm,"+BAL+(","+opts if opts else "")+"]\n"+body.strip("\n")+"\n"+r"\end{tikzpicture}"+T)
# robô vista de cima: círculo + seta de direção
ROBO=r"""
  \newcommand{\robo}[3]{\begin{scope}[shift={(#1,#2)}, rotate=#3]\draw[black!75, fill=dorange!65, line width=1pt] (0,0) circle (0.32); \draw[black!85, line width=2.4pt, line cap=round] (0,0) -- (0.32,0);\end{scope}}
"""
