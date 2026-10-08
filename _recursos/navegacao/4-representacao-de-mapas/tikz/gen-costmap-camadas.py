# Gera costmap-camadas.tex: camadas do costmap_2d (estático, obstáculos, inflação) -> costmap final
import math
H = "\\documentclass[border=3pt]{standalone}\n\\input{preamble}\n\\begin{document}\n"
T = "\n\\end{document}\n"
NX,NY=18,12; C=0.24
static=set()
for i in range(NX):
    static.add((i,0)); static.add((i,NY-1))
for j in range(NY):
    static.add((0,j)); static.add((NX-1,j))
for j in range(0,7): static.add((9,j))            # parede interna com passagem em cima
obst={(4,8),(4,7),(13,3),(14,3),(13,4)}
occ=static|obst
def cost(i,j):
    if (i,j) in occ: return None
    d=min(math.hypot(i-a,j-b) for a,b in occ)
    return max(0,100-(d-1)*30)
def cell(i,j,fill,thin=True):
    return r"\fill[%s, draw=black!18, line width=0.2pt] (%.3f,%.3f) rectangle ++(%.3f,%.3f);"%(fill,i*C,j*C,C,C)+"\n"
def red(lv): return "red!%d!white"%int(lv*0.7)
def panel(kind):
    s=""
    for i in range(NX):
        for j in range(NY):
            if kind=="static": f="black!85" if (i,j) in static else "white"
            elif kind=="obst": f="black!85" if (i,j) in obst else "white"
            elif kind=="infl":
                c=cost(i,j); f="white" if c is None else red(c)
            else:
                c=cost(i,j); f="black!85" if c is None else red(c)
            s+=cell(i,j,f)
    s+=r"\draw[black!80, line width=1pt] (0,0) rectangle (%.3f,%.3f);"%(NX*C,NY*C)+"\n"
    return s
W=NX*C; gap=1.25
items=[("static","Mapa estático","\\texttt{static\\_layer}","paredes do mapa salvo"),
       ("obst","Obstáculos detectados","\\texttt{obstacle\\_layer}","leituras do laser em tempo real"),
       ("infl","Inflação","\\texttt{inflation\\_layer}","custo decrescente ao redor"),
       ("final","Costmap final","\\texttt{master costmap}","usado pelo planejador")]
b=r"\begin{tikzpicture}[x=1cm,y=1cm]"+"\n"
for k,(kind,t,code,desc) in enumerate(items):
    ox=k*(W+gap)
    b+=r"\begin{scope}[shift={(%.3f,0)}]"%ox+"\n"+panel(kind)
    col="dred" if kind=="final" else "dblue"
    b+=r"\node[font=\bfseries\large, text=%s] at (%.3f,%.3f) {%s};"%(col,W/2,NY*C+0.5,t)+"\n"
    b+=r"\node[font=\normalsize] at (%.3f,-0.45) {%s};"%(W/2,code)+"\n"
    b+=r"\node[dsub, font=\normalsize, align=center] at (%.3f,-1.1) {%s};"%(W/2,desc)+"\n"
    b+=r"\end{scope}"+"\n"
for k,sym in enumerate(["+","+","="]):
    x=(k+1)*(W+gap)-gap/2
    b+=r"\node[font=\Huge\bfseries, black!60] at (%.3f,%.3f) {%s};"%(x,NY*C/2,sym)+"\n"
b+=r"\end{tikzpicture}"
open("costmap-camadas.tex","w").write(H+b+T)
