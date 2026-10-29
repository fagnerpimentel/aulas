"""Gera amostra-populacao.tex e quantos-participantes.tex (slides 'Quem participa' e 'Quantos participantes')."""
import random
H=r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
F="\\end{tikzpicture}\n\\end{document}\n"
cores={"E":("dblue","dblue!35"),"I":("dorange","dorange!35"),"C":("dgreen","dgreen!35"),"A":("black!55","black!18")}
def dot(x,y,g,r=0.2,lw="1.2pt"):
    c,f=cores[g]; return r"  \draw[%s, fill=%s, line width=%s] (%.2f,%.2f) circle (%.2f);"%(c,f,lw,x,y,r)

# ===================== amostra =====================
random.seed(4); o=[]
o.append(r"  \useasboundingbox (-0.4,0.7) rectangle (19.6,9.4);")
o.append(r"  \node[font=\Large\bfseries, black!75] at (3.4,8.7) {população-alvo};")
o.append(r"  \draw[black!55, line width=1.4pt, rounded corners=6pt] (0,2.2) rectangle (6.8,8.1);")
for r in range(5):
    for c in range(6):
        g=random.choices(["E","I","C","A"],[0.3,0.25,0.2,0.25])[0]
        o.append(dot(0.65+c*1.1,7.35-r*1.0,g))
# conveniência (em cima)
o.append(r"  \draw[dred, line width=1.6pt, rounded corners=6pt] (8.6,5.6) rectangle (13.0,8.1);")
for i in range(6): o.append(dot(9.4+(i%3)*1.3,7.35-(i//3)*1.05,"E",r=0.24))
o.append(r"  \node[font=\large, text width=5.6cm, align=left, anchor=west] at (13.5,6.85) {\textbf{amostra de conveniência}\\ \textbf{só estudantes}: fácil de acessar\\ \textcolor{dred}{validade externa limitada}};")
# representativa (embaixo)
o.append(r"  \draw[dgreen, line width=1.6pt, rounded corners=6pt] (8.6,2.2) rectangle (13.0,4.7);")
for i,g in enumerate(["E","I","C","A","I","C"]): o.append(dot(9.4+(i%3)*1.3,3.95-(i//3)*1.05,g,r=0.24))
o.append(r"  \node[font=\large, text width=5.6cm, align=left, anchor=west] at (13.5,3.45) {\textbf{amostra representativa}\\ grande e variada\\ \textcolor{dgreen!60!black}{validade externa}: os resultados valem fora do estudo};")
o.append(r"  \draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (7.0,6.4) -- (8.45,6.85);")
o.append(r"  \draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (7.0,3.9) -- (8.45,3.45);")
for i,(g,t) in enumerate([("E","estudantes"),("I","idosos"),("C","crianças"),("A","adultos em geral")]):
    x=[0.2,3.0,5.6,8.4][i]
    o.append(dot(x+0.2,1.35,g,r=0.17)); o.append(r"  \node[font=\normalsize, anchor=west] at (%.2f,1.35) {%s};"%(x+0.5,t))
open("amostra-populacao.tex","w").write(H+"\n".join(o)+"\n"+F)

# ===================== quantos participantes =====================
random.seed(9); o=[]
o.append(r"  \useasboundingbox (-0.4,-0.9) rectangle (21.0,9.4);")
o.append(r"  \node[font=\Large\bfseries, black!75] at (3.2,8.8) {ruído e tamanho};")
def faixa(y,n,label):
    o.append(r"  \draw[daxis, line width=1.1pt] (0.2,%.2f) -- (6.4,%.2f);"%(y,y))
    for cen,cor in ((2.4,"dorange"),(3.4,"dblue")):
        pts=[min(max(random.gauss(cen,0.85),0.5),6.0) for _ in range(n)]
        for k,p in enumerate(pts): o.append(r"  \fill[%s!70] (%.2f,%.2f) circle (0.11);"%(cor,p,y+0.3+0.26*(k%4)))
        m=sum(pts)/len(pts)
        o.append(r"  \draw[%s, line width=2.4pt] (%.2f,%.2f) -- (%.2f,%.2f);"%(cor,m,y-0.1,m,y+1.5))
    o.append(r"  \node[font=\large\bfseries, anchor=west] at (0.2,%.2f) {%s};"%(y+1.95,label))
faixa(5.9,5,r"$n=5$ por grupo")
faixa(2.4,25,r"$n=25$ por grupo")
o.append(r"  \node[font=\large, dred, anchor=west] at (0.2,5.2) {efeito \textbf{difícil} de detectar};")
o.append(r"  \node[font=\large, dgreen!60!black, anchor=west] at (0.2,1.7) {efeito \textbf{mais claro}};")
o.append(r"  \fill[dorange!70] (0.3,0.4) circle (0.11); \node[font=\normalsize, anchor=west] at (0.55,0.4) {grupo A}; \fill[dblue!70] (2.2,0.4) circle (0.11); \node[font=\normalsize, anchor=west] at (2.45,0.4) {grupo B}; \node[font=\normalsize, black!65, anchor=west] at (4.1,0.4) {linha = média};")
o.append(r"  \node[font=\Large\bfseries, black!75] at (10.6,8.8) {quantos participantes?};")
o.append(r"  \tikzset{ent/.style={dbox, draw=black!55, fill=white, line width=1.3pt, text width=4.0cm, minimum height=0.95cm, font=\large, align=center}}")
o.append(r"  \node[ent] (a) at (9.1,7.4) {efeito esperado};")
o.append(r"  \node[ent] (b) at (9.1,6.2) {poder do teste};")
o.append(r"  \node[ent] (c) at (9.1,5.0) {nível de significância};")
o.append(r"  \node[dbox, draw=dblue, fill=dblue!8, line width=1.7pt, text width=2.3cm, minimum height=3.7cm, font=\large\bfseries, align=center] (g) at (12.9,6.2) {G*Power};")
for n in "abc": o.append(r"  \draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (%s.east) -- (g.west |- %s.east);"%(n,n))
o.append(r"  \node[dbox, draw=dgreen, fill=dgreen!8, line width=1.7pt, text width=4.4cm, minimum height=1.5cm, font=\large\bfseries, align=center] (t) at (10.9,3.0) {tamanho da amostra necessário};")
o.append(r"  \draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (g.south) -- ++(0,-0.55) -| (t.north);")
o.append(r"  \node[dbox, draw=dred, dashed, line width=1.4pt, text width=6.8cm, minimum height=1.9cm, font=\large, align=center] at (10.9,0.55) {\textbf{limites}: tempo, dinheiro e acesso\\ população difícil de recrutar: amostra pequena ou \textbf{casos individuais}};")
o.append(r"  \node[font=\Large\bfseries, black!75] at (17.9,8.8) {estudos qualitativos};")
o.append(r"  \draw[daxis, line width=1.2pt] (15.4,1.5) -- (20.6,1.5); \draw[daxis, line width=1.2pt] (15.4,1.5) -- (15.4,8.0);")
for i,v in enumerate([6,4,3,2,1,1,0,0,0,0]):
    x=15.7+i*0.5
    o.append(r"  \fill[%s] (%.2f,1.5) rectangle (%.2f,%.2f);"%("dorange!75" if v>0 else "black!25",x,x+0.36,1.5+max(v,0.06)*0.95))
o.append(r"  \node[font=\normalsize, rotate=90] at (15.0,4.5) {temas novos};")
o.append(r"  \node[font=\normalsize] at (17.9,1.05) {entrevistas $\rightarrow$};")
o.append(r"  \draw[dgreen, dashed, line width=1.3pt] (18.65,1.0) -- (18.65,7.2);")
o.append(r"  \node[font=\large\bfseries, dgreen!60!black, text width=2.6cm, align=center, fill=dcream, inner sep=2pt] at (19.6,6.6) {saturação:\\ só repete};")
o.append(r"  \node[font=\large, text width=5.4cm, align=center] at (17.9,-0.1) {\textbf{pare} quando os dados novos só \textbf{repetem} os temas já encontrados};")
open("quantos-participantes.tex","w").write(H+"\n".join(o)+"\n"+F)
