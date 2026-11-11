"""Gera os diagramas TikZ da aula 14 de Robótica Probabilística (SLAM com EIF). Uso: python3 gerar.py && bash build.sh"""
exec(open("_helpers.py").read())

# ------------------------------------------------------------------ momentos x informacao
w("momentos-informacao", r"""
\tikzset{k/.style={dbox, text width=7.4cm, minimum height=3.2cm, font=\large, line width=1.8pt}}
\node[k, draw=dblue] (a) at (3.9,4.0) {\textbf{\Large\textcolor{dblue}{Forma de momentos}}\\[6pt] média $\mu$ e covariância $\Sigma$\\[6pt] usada pelo \textbf{EKF SLAM}};
\node[k, draw=dorange] (b) at (15.5,4.0) {\textbf{\Large\textcolor{dorange}{Forma de informação}}\\[6pt] vetor $\xi$ e matriz $\Omega$\\[6pt] usada pelo \textbf{EIF SLAM}};
\draw[dtrans, line width=2.4pt, {Stealth[length=3.6mm]}-{Stealth[length=3.6mm]}] (a.east) -- (b.west);
\node[font=\large, fill=white, inner sep=3pt, text width=3.4cm, align=center] at (9.7,5.2) {a \textbf{mesma} informação};
\node[font=\Large] at (9.7,3.4) {$\Omega=\Sigma^{-1}$};
\node[font=\Large] at (9.7,2.5) {$\xi=\Sigma^{-1}\mu$};
\node[dbox, draw=dgreen, fill=dgreen!8, line width=1.8pt, text width=17cm, minimum height=1.4cm, font=\large] at (9.7,0.0) {a \textbf{informação é aditiva}: integrar uma medição é \textbf{somar} parcelas a $\Omega$ e $\xi$};
""")

# ------------------------------------------------------------------ vantagens do EIF SLAM
w("vantagens-eif", boxes([
  ("Linearização melhor", "usa todos os dados, e não só os até o instante $t$"),
  ("Correspondência melhor", "também usa todos os dados para decidir quem é quem"),
  ("Refinamento iterativo", "refaz o mapa, as correspondências e os modelos"),
  ("Mais robusto", "menos frágil a associação errada e a incerteza rotacional alta"),
  ("Mapas bem maiores", "ordens de grandeza acima do que o EKF aguenta")], w=5.4, h=2.9, cols=3,
  cap=r"o preço: \textbf{não é incremental}, e os dados ficam na memória até o mapa ser construído", capw=17))

# ------------------------------------------------------------------ grafo de molas
w("grafo-molas", r"""
\tikzset{p/.style={circle, draw=dblue, fill=dblue!12, line width=1.8pt, minimum size=1.3cm, font=\large},
        m/.style={circle, draw=dgreen, fill=dgreen!12, line width=1.8pt, minimum size=1.3cm, font=\large},
        sp/.style={decorate, decoration={zigzag, segment length=3.2mm, amplitude=1.4mm}, line width=1.5pt}}
\foreach \i in {0,1,2,3,4} {\node[p] (x\i) at ({1.4+\i*3.4},6.0) {$x_{\i}$};}
\foreach \i/\j in {0/1,1/2,2/3,3/4} {\draw[sp, draw=dblue] (x\i) -- (x\j);}
\foreach \i/\j in {0/1,1/2,2/3,3/4} {\node[font=\large, text=dblue, fill=white, inner sep=1pt] at ({1.4+\i*3.4+1.7},6.75) {$u_{\j}$};}
\node[m] (m1) at (3.1,1.8) {$m_1$};
\node[m] (m2) at (8.2,1.8) {$m_2$};
\node[m] (m3) at (13.3,1.8) {$m_3$};
\draw[sp, draw=dorange] (x0) -- (m1); \draw[sp, draw=dorange] (x1) -- (m1);
\draw[sp, draw=dorange] (x1) -- (m2); \draw[sp, draw=dorange] (x2) -- (m2); \draw[sp, draw=dorange] (x3) -- (m2);
\draw[sp, draw=dorange] (x3) -- (m3); \draw[sp, draw=dorange] (x4) -- (m3);
\node[font=\large, anchor=west] at (15.5,2.8) {\textcolor{dblue}{\textbf{controle}}: mola entre poses};
\node[font=\large, anchor=west] at (15.5,2.0) {\textcolor{dorange}{\textbf{medição}}: mola entre pose e marco};
\node[font=\large, anchor=west] at (15.5,1.2) {marcos \textbf{não} se ligam entre si};
""")

# ------------------------------------------------------------------ matriz de informacao esparsa
w("matriz-omega", r"""
\def\cw{1.15}
\foreach \i in {0,...,7} {
  \foreach \j in {0,...,7} {\draw[black!25, line width=0.4pt] ({\j*\cw},{-\i*\cw}) rectangle ({(\j+1)*\cw},{-(\i+1)*\cw});}}
% diagonal e vizinhas: poses x0..x4 (indices 0..4)
\foreach \i in {0,...,4} {\fill[dblue!70] ({\i*\cw+0.04},{-\i*\cw-0.04}) rectangle ({(\i+1)*\cw-0.04},{-(\i+1)*\cw+0.04});}
\foreach \i in {0,...,3} {\pgfmathtruncatemacro{\k}{\i+1}
  \fill[dblue!40] ({\k*\cw+0.04},{-\i*\cw-0.04}) rectangle ({(\k+1)*\cw-0.04},{-(\i+1)*\cw+0.04});
  \fill[dblue!40] ({\i*\cw+0.04},{-\k*\cw-0.04}) rectangle ({(\i+1)*\cw-0.04},{-(\k+1)*\cw+0.04});}
% marcos m1,m2,m3 = indices 5,6,7 : diagonal
\foreach \i in {5,6,7} {\fill[dgreen!70] ({\i*\cw+0.04},{-\i*\cw-0.04}) rectangle ({(\i+1)*\cw-0.04},{-(\i+1)*\cw+0.04});}
% pose-marco
\foreach \p/\mm in {0/5,1/5,1/6,2/6,3/6,3/7,4/7} {
  \fill[dorange!75] ({\mm*\cw+0.04},{-\p*\cw-0.04}) rectangle ({(\mm+1)*\cw-0.04},{-(\p+1)*\cw+0.04});
  \fill[dorange!75] ({\p*\cw+0.04},{-\mm*\cw-0.04}) rectangle ({(\p+1)*\cw-0.04},{-(\mm+1)*\cw+0.04});}
\foreach \i/\t in {0/{$x_0$},1/{$x_1$},2/{$x_2$},3/{$x_3$},4/{$x_4$},5/{$m_1$},6/{$m_2$},7/{$m_3$}} {
  \node[font=\large] at ({\i*\cw+0.575},0.5) {\t};
  \node[font=\large] at (-0.55,{-\i*\cw-0.575}) {\t};}
\draw[line width=1.6pt] (0,0) rectangle (9.2,-9.2);
\def\lx{10.6}
\fill[dblue!70] (\lx,-1.0) rectangle (\lx+0.7,-1.7); \node[font=\large, anchor=west] at (\lx+1.0,-1.35) {pose com ela mesma};
\fill[dblue!40] (\lx,-2.3) rectangle (\lx+0.7,-3.0); \node[font=\large, anchor=west] at (\lx+1.0,-2.65) {poses consecutivas (controle)};
\fill[dorange!75] (\lx,-3.6) rectangle (\lx+0.7,-4.3); \node[font=\large, anchor=west] at (\lx+1.0,-3.95) {pose e marco observado};
\fill[dgreen!70] (\lx,-4.9) rectangle (\lx+0.7,-5.6); \node[font=\large, anchor=west] at (\lx+1.0,-5.25) {marco com ele mesmo};
\draw[black!40, line width=0.8pt] (\lx,-6.2) rectangle (\lx+0.7,-6.9); \node[font=\large, anchor=west] at (\lx+1.0,-6.55) {\textbf{zero}: sem ligação};
\node[font=\large, anchor=west, text width=8.2cm] at (\lx,-8.2) {\textbf{esparsa}: quase tudo é zero};
""")

# ------------------------------------------------------------------ adicao local a Omega
w("adicao-local", r"""
\def\cw{1.5}
\tikzset{g/.style={draw=black!35, line width=0.5pt}}
\foreach \o/\tit/\a/\b/\col/\leg in {0/{cada \textbf{controle} $u_t$}/0/1/dblue/{liga $x_{t-1}$ e $x_t$}, 11/{cada \textbf{medição} $z_t^i$}/1/2/dorange/{liga $x_t$ e $m_j$}} {
  \node[font=\Large, anchor=west] at (\o,1.6) {\tit};
  \foreach \i in {0,1,2} {\foreach \j in {0,1,2} {\draw[g] ({\o+\j*\cw},{-\i*\cw}) rectangle ({\o+(\j+1)*\cw},{-(\i+1)*\cw});}}
  \foreach \p in {\a,\b} {\foreach \q in {\a,\b} {\fill[\col!70] ({\o+\q*\cw+0.05},{-\p*\cw-0.05}) rectangle ({\o+(\q+1)*\cw-0.05},{-(\p+1)*\cw+0.05});}}
  \draw[line width=1.6pt] (\o,0) rectangle ({\o+3*\cw},{-3*\cw});
  \node[font=\large] at ({\o+0.75},0.5) {$x_{t-1}$}; \node[font=\large] at ({\o+2.25},0.5) {$x_t$}; \node[font=\large] at ({\o+3.75},0.5) {$m_j$};
  \node[font=\large, anchor=north, text width=7cm, align=center] at ({\o+2.25},-4.8) {\leg};}
\node[font=\Large\bfseries] at (7.0,-2.25) {\Huge $+$};
\node[font=\large, text width=18cm, align=center] at (10.0,-6.4) {a atualização é uma \textbf{soma local}: só as linhas e colunas das variáveis envolvidas mudam};
""")

# ------------------------------------------------------------------ topologia: sem ciclo x com ciclo (grafo e matriz)
w("topologia-ciclos", r"""
\tikzset{p/.style={circle, draw=dblue, fill=dblue!12, line width=1.5pt, minimum size=0.75cm},
        m/.style={circle, draw=dgreen, fill=dgreen!12, line width=1.5pt, minimum size=0.75cm}}
\node[font=\Large\bfseries, text=dgreen] at (5.2,8.4) {cada marco é visto uma vez};
\node[p] (ap0) at (0.5,5.6) {};
\node[p] (ap1) at (1.65,5.6) {};
\node[p] (ap2) at (2.8,5.6) {};
\node[p] (ap3) at (3.9499999999999997,5.6) {};
\node[p] (ap4) at (5.1,5.6) {};
\node[p] (ap5) at (6.25,5.6) {};
\draw[dblue, line width=1.6pt] (ap0) -- (ap1);
\draw[dblue, line width=1.6pt] (ap1) -- (ap2);
\draw[dblue, line width=1.6pt] (ap2) -- (ap3);
\draw[dblue, line width=1.6pt] (ap3) -- (ap4);
\draw[dblue, line width=1.6pt] (ap4) -- (ap5);
\node[m] (am1) at (1.65,3.6) {};
\draw[dorange, line width=1.4pt] (ap1) -- (am1); \draw[dorange, line width=1.4pt] (ap2) -- (am1);
\node[m] (am3) at (3.95,3.6) {};
\draw[dorange, line width=1.4pt] (ap3) -- (am3); \draw[dorange, line width=1.4pt] (ap4) -- (am3);
\fill[dblue!70] (6.9,4.4) rectangle (7.4,4.9);
\fill[dblue!35] (7.4,4.4) rectangle (7.9,4.9);
\fill[dblue!35] (7.9,4.4) rectangle (8.4,4.9);
\fill[dblue!35] (6.9,3.9) rectangle (7.4,4.4);
\fill[dblue!70] (7.4,3.9) rectangle (7.9,4.4);
\fill[dblue!35] (7.9,3.9) rectangle (8.4,4.4);
\fill[dblue!35] (8.4,3.9) rectangle (8.9,4.4);
\fill[dblue!35] (6.9,3.4) rectangle (7.4,3.9);
\fill[dblue!35] (7.4,3.4) rectangle (7.9,3.9);
\fill[dblue!70] (7.9,3.4) rectangle (8.4,3.9);
\fill[dblue!35] (8.4,3.4) rectangle (8.9,3.9);
\fill[dblue!35] (8.9,3.4) rectangle (9.4,3.9);
\fill[dblue!35] (7.4,2.9) rectangle (7.9,3.4);
\fill[dblue!35] (7.9,2.9) rectangle (8.4,3.4);
\fill[dblue!70] (8.4,2.9) rectangle (8.9,3.4);
\fill[dblue!35] (8.9,2.9) rectangle (9.4,3.4);
\fill[dblue!35] (9.4,2.9) rectangle (9.9,3.4);
\fill[dblue!35] (7.9,2.4) rectangle (8.4,2.9);
\fill[dblue!35] (8.4,2.4) rectangle (8.9,2.9);
\fill[dblue!70] (8.9,2.4) rectangle (9.4,2.9);
\fill[dblue!35] (9.4,2.4) rectangle (9.9,2.9);
\fill[dblue!35] (9.9,2.4) rectangle (10.4,2.9);
\fill[dblue!35] (8.4,1.9) rectangle (8.9,2.4);
\fill[dblue!35] (8.9,1.9) rectangle (9.4,2.4);
\fill[dblue!70] (9.4,1.9) rectangle (9.9,2.4);
\fill[dblue!35] (9.9,1.9) rectangle (10.4,2.4);
\fill[dblue!35] (10.4,1.9) rectangle (10.9,2.4);
\fill[dblue!35] (8.9,1.4) rectangle (9.4,1.9);
\fill[dblue!35] (9.4,1.4) rectangle (9.9,1.9);
\fill[dblue!70] (9.9,1.4) rectangle (10.4,1.9);
\fill[dblue!35] (10.4,1.4) rectangle (10.9,1.9);
\fill[dblue!35] (9.4,0.9) rectangle (9.9,1.4);
\fill[dblue!35] (9.9,0.9) rectangle (10.4,1.4);
\fill[dblue!70] (10.4,0.9) rectangle (10.9,1.4);
\draw[black!30, line width=0.5pt] (6.9,0.9) grid[step=0.5] (10.9,4.9);
\draw[line width=1.6pt] (6.9,0.9) rectangle (10.9,4.9);
\node[font=\large, text width=4.2cm, align=center] at (9.1,-0.1) {\textbf{banda}: não nulos perto da diagonal};
\node[font=\large, text width=6.4cm, align=center] at (3.2,1.2) {o grafo é uma \textbf{cadeia}: inversão em \textbf{tempo linear}};
\node[font=\Large\bfseries, text=dred] at (17.0,8.4) {marcos revistos depois de muito tempo};
\node[p] (bp0) at (12.3,5.6) {};
\node[p] (bp1) at (13.450000000000001,5.6) {};
\node[p] (bp2) at (14.600000000000001,5.6) {};
\node[p] (bp3) at (15.75,5.6) {};
\node[p] (bp4) at (16.9,5.6) {};
\node[p] (bp5) at (18.05,5.6) {};
\draw[dblue, line width=1.6pt] (bp0) -- (bp1);
\draw[dblue, line width=1.6pt] (bp1) -- (bp2);
\draw[dblue, line width=1.6pt] (bp2) -- (bp3);
\draw[dblue, line width=1.6pt] (bp3) -- (bp4);
\draw[dblue, line width=1.6pt] (bp4) -- (bp5);
\node[m] (bm) at (15.100000000000001,3.6) {};
\draw[dorange, line width=1.4pt] (bp1) -- (bm); \draw[dorange, line width=1.4pt] (bp2) -- (bm); \draw[dorange, line width=2.6pt, dashed] (bp5) -- (bm);
\draw[dred, line width=2.2pt, dashed] (bp1) to[bend left=38] (bp5);
\fill[dblue!70] (18.700000000000003,4.4) rectangle (19.200000000000003,4.9);
\fill[dblue!35] (19.200000000000003,4.4) rectangle (19.700000000000003,4.9);
\fill[dblue!35] (19.700000000000003,4.4) rectangle (20.200000000000003,4.9);
\fill[dblue!35] (18.700000000000003,3.9) rectangle (19.200000000000003,4.4);
\fill[dblue!70] (19.200000000000003,3.9) rectangle (19.700000000000003,4.4);
\fill[dblue!35] (19.700000000000003,3.9) rectangle (20.200000000000003,4.4);
\fill[dblue!35] (20.200000000000003,3.9) rectangle (20.700000000000003,4.4);
\fill[dred!80] (21.700000000000003,3.9) rectangle (22.200000000000003,4.4);
\fill[dblue!35] (18.700000000000003,3.4) rectangle (19.200000000000003,3.9);
\fill[dblue!35] (19.200000000000003,3.4) rectangle (19.700000000000003,3.9);
\fill[dblue!70] (19.700000000000003,3.4) rectangle (20.200000000000003,3.9);
\fill[dblue!35] (20.200000000000003,3.4) rectangle (20.700000000000003,3.9);
\fill[dblue!35] (20.700000000000003,3.4) rectangle (21.200000000000003,3.9);
\fill[dblue!35] (19.200000000000003,2.9) rectangle (19.700000000000003,3.4);
\fill[dblue!35] (19.700000000000003,2.9) rectangle (20.200000000000003,3.4);
\fill[dblue!70] (20.200000000000003,2.9) rectangle (20.700000000000003,3.4);
\fill[dblue!35] (20.700000000000003,2.9) rectangle (21.200000000000003,3.4);
\fill[dblue!35] (21.200000000000003,2.9) rectangle (21.700000000000003,3.4);
\fill[dblue!35] (19.700000000000003,2.4) rectangle (20.200000000000003,2.9);
\fill[dblue!35] (20.200000000000003,2.4) rectangle (20.700000000000003,2.9);
\fill[dblue!70] (20.700000000000003,2.4) rectangle (21.200000000000003,2.9);
\fill[dblue!35] (21.200000000000003,2.4) rectangle (21.700000000000003,2.9);
\fill[dblue!35] (21.700000000000003,2.4) rectangle (22.200000000000003,2.9);
\fill[dblue!35] (20.200000000000003,1.9) rectangle (20.700000000000003,2.4);
\fill[dblue!35] (20.700000000000003,1.9) rectangle (21.200000000000003,2.4);
\fill[dblue!70] (21.200000000000003,1.9) rectangle (21.700000000000003,2.4);
\fill[dblue!35] (21.700000000000003,1.9) rectangle (22.200000000000003,2.4);
\fill[dblue!35] (22.200000000000003,1.9) rectangle (22.700000000000003,2.4);
\fill[dred!80] (19.200000000000003,1.4) rectangle (19.700000000000003,1.9);
\fill[dblue!35] (20.700000000000003,1.4) rectangle (21.200000000000003,1.9);
\fill[dblue!35] (21.200000000000003,1.4) rectangle (21.700000000000003,1.9);
\fill[dblue!70] (21.700000000000003,1.4) rectangle (22.200000000000003,1.9);
\fill[dblue!35] (22.200000000000003,1.4) rectangle (22.700000000000003,1.9);
\fill[dblue!35] (21.200000000000003,0.9) rectangle (21.700000000000003,1.4);
\fill[dblue!35] (21.700000000000003,0.9) rectangle (22.200000000000003,1.4);
\fill[dblue!70] (22.200000000000003,0.9) rectangle (22.700000000000003,1.4);
\draw[black!30, line width=0.5pt] (18.700000000000003,0.9) grid[step=0.5] (22.700000000000003,4.9);
\draw[line width=1.6pt] (18.700000000000003,0.9) rectangle (22.700000000000003,4.9);
\node[font=\large, text width=4.4cm, align=center] at (20.9,-0.1) {\textbf{elemento longe da diagonal}};
\node[font=\large, text width=6.4cm, align=center] at (15.0,1.2) {surge um \textbf{ciclo}: a inversão fica \textbf{mais cara}};
""")

# ------------------------------------------------------------------ eliminar um marco
w("eliminar-marco", r"""
\tikzset{p/.style={circle, draw=dblue, fill=dblue!12, line width=1.8pt, minimum size=1.3cm, font=\large},
        m/.style={circle, draw=dgreen, fill=dgreen!12, line width=1.8pt, minimum size=1.3cm, font=\large},
        sp/.style={decorate, decoration={zigzag, segment length=3.2mm, amplitude=1.4mm}, line width=1.5pt}}
\node[font=\Large\bfseries] at (4.3,8.6) {antes};
\node[p] (a1) at (1.2,6.0) {$x_a$}; \node[p] (a2) at (4.3,6.0) {$x_b$}; \node[p] (a3) at (7.4,6.0) {$x_c$};
\draw[sp, draw=dblue] (a1) -- (a2); \draw[sp, draw=dblue] (a2) -- (a3);
\node[m] (am) at (4.3,2.4) {$m_j$};
\draw[sp, draw=dorange] (a1) -- (am); \draw[sp, draw=dorange] (a2) -- (am); \draw[sp, draw=dorange] (a3) -- (am);
\node[font=\large, text width=8.6cm, align=center] at (4.3,0.6) {$m_j$ ligado às poses $\tau(j)$ em que foi \textbf{observado}};
\draw[dtrans, line width=3pt, -{Stealth[length=4.5mm]}] (9.0,4.2) -- (10.6,4.2);
\node[font=\Large\bfseries] at (15.2,8.6) {depois};
\node[p] (b1) at (12.1,6.0) {$x_a$}; \node[p] (b2) at (15.2,6.0) {$x_b$}; \node[p] (b3) at (18.3,6.0) {$x_c$};
\draw[sp, draw=dblue] (b1) -- (b2); \draw[sp, draw=dblue] (b2) -- (b3);
\draw[sp, draw=dred] (b1) to[bend left=55] (b2); \draw[sp, draw=dred] (b2) to[bend left=55] (b3); \draw[sp, draw=dred] (b1) to[bend left=62] (b3);
\node[font=\large, text width=8.6cm, align=center] at (15.2,3.5) {$m_j$ \textbf{removido}; molas \textbf{novas} ligam as poses de $\tau(j)$ entre si};
\node[font=\large, text width=8.6cm, align=center] at (15.2,1.5) {a informação total é a \textbf{mesma}: só $m_j$ foi desconectado};
\draw[sp, draw=dblue] (0.3,-0.9) -- (1.4,-0.9); \node[font=\large, anchor=west] at (1.6,-0.9) {controle (já existia)};
\draw[sp, draw=dorange] (7.3,-0.9) -- (8.4,-0.9); \node[font=\large, anchor=west] at (8.6,-0.9) {medição de $m_j$};
\draw[sp, draw=dred] (13.3,-0.9) -- (14.4,-0.9); \node[font=\large, anchor=west] at (14.6,-0.9) {mola nova};
""")

# ------------------------------------------------------------------ tres passos do EIF SLAM
w("tres-passos-eif", flow([
  ("Construir", r"$\Omega$ e $\xi$ sobre poses e marcos: matriz \textbf{grande e esparsa}"),
  ("Reduzir", r"eliminar os marcos: $\tilde\Omega$ e $\tilde\xi$ \textbf{só sobre as poses}"),
  ("Resolver", r"inverter $\tilde\Omega$ para o \textbf{caminho}; depois, \textbf{um marco por vez}")],
  w=5.6, h=3.6, cap=r"em cada passo, o custo é \textbf{linear}, exceto a inversão de $\tilde\Omega$ quando há \textbf{ciclos}", capw=18))

# ------------------------------------------------------------------ reducao em blocos
w("reducao-blocos", r"""
\def\u{1.0}
\tikzset{bl/.style={draw=black!70, line width=1.4pt}}
\node[font=\Large\bfseries] at (3.4,7.6) {antes: $\Omega$};
\fill[dblue!60] (0,6.6) rectangle (4.4,2.2); \node[font=\large\bfseries, text=white] at (2.2,4.4) {poses};
\fill[dgreen!60] (4.4,2.2) rectangle (6.8,-0.2); \node[font=\large\bfseries, text=white] at (5.6,1.0) {marcos};
\fill[dorange!65] (4.4,6.6) rectangle (6.8,2.2); \node[font=\large\bfseries, text=white] at (5.6,4.4) {liga};
\fill[dorange!65] (0,2.2) rectangle (4.4,-0.2); \node[font=\large\bfseries, text=white] at (2.2,1.0) {liga};
\draw[line width=1.8pt] (0,6.6) rectangle (6.8,-0.2);
\node[font=\large, text width=7cm, align=center] at (3.4,-1.1) {$\Omega_{mm}$ é \textbf{bloco-diagonal}: fácil de inverter};
\draw[dtrans, line width=3pt, -{Stealth[length=4.5mm]}] (7.6,3.2) -- (9.4,3.2);
\node[font=\Large\bfseries] at (13.2,7.6) {depois: $\tilde\Omega$};
\fill[dblue!60] (10.2,6.6) rectangle (14.6,2.2); \node[font=\large\bfseries, text=white, text width=4cm, align=center] at (12.4,4.4) {poses, com novas ligações};
\draw[line width=1.8pt] (10.2,6.6) rectangle (14.6,2.2);
\node[font=\Large, anchor=west] at (15.2,5.2) {$\tilde\Omega=\Omega_{pp}-\Omega_{pm}\,\Omega_{mm}^{-1}\,\Omega_{mp}$};
\node[font=\Large, anchor=west] at (15.2,3.6) {$\tilde\xi=\xi_{p}-\Omega_{pm}\,\Omega_{mm}^{-1}\,\xi_{m}$};
\node[font=\large, anchor=west, text width=5.6cm] at (15.2,2.0) {os marcos \textbf{somem}, e a informação deles vai para as \textbf{poses}};
""")

# ------------------------------------------------------------------ iteracao
w("eif-iteracao", r"""
\tikzset{k/.style={dbox, text width=3.3cm, minimum height=2.4cm, font=\large, line width=1.7pt}}
\node[k, draw=black] (z) at (1.8,4.0) {\textbf{dados completos coletados}\\ $u_{1:t},\ z_{1:t}$};
\node[k, draw=dred] (a) at (6.4,4.0) {$\mu_{0:t}$ \textbf{inicial}\\ pela odometria};
\node[k, draw=dblue] (b) at (11.0,4.0) {\textbf{construir}\\ $\Omega,\ \xi$};
\node[k, draw=dgreen] (c) at (15.6,4.0) {\textbf{reduzir}\\ $\tilde\Omega,\ \tilde\xi$};
\node[k, draw=dorange] (d) at (20.2,4.0) {\textbf{resolver}\\ $\mu,\ \Sigma_{0:t}$};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (z) -- (a);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a) -- (b);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b) -- (c);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (c) -- (d);
\draw[dred, line width=2.2pt, -{Stealth[length=3.4mm]}] (d.south) -- ++(0,-1.4) -| node[pos=0.25, above, font=\large\bfseries, text=black, fill=white, inner sep=2pt] {$\mu$ melhor: repetir 2 ou 3 vezes} (b.south);
\node[font=\large, text width=20cm, align=center] at (10.6,0.4) {tudo roda \textbf{depois da coleta}: cada passada reestima o \textbf{caminho inteiro} e o mapa de uma vez, e só é preciso repetir se o erro inicial de orientação for grande (mais de $20^\circ$)};
""")

# ------------------------------------------------------------------ teste de correspondencia
w("teste-correspondencia", r"""
\foreach \o/\mu/\col/\tit/\res in {0/0.7/dgreen/{$\Delta_{j,k}$ perto de zero}/{\textbf{provavelmente o mesmo marco}: unir}, 10.8/3.1/dred/{$\Delta_{j,k}$ longe de zero}/{\textbf{provavelmente marcos diferentes}: manter}} {
  \node[font=\Large\bfseries, text=\col] at ({\o+4.2},5.4) {\tit};
  \draw[line width=1.6pt, ->] ({\o-0.4},0) -- ({\o+9.2},0);
  \draw[line width=1.6pt, ->] ({\o+4.2},0) -- ({\o+4.2},4.4);
  \node[font=\large, anchor=north] at ({\o+8.6},-0.1) {$\Delta_{j,k}=m_j-m_k$};
  \draw[domain=-4.0:6.2, samples=90, smooth, line width=2.4pt, draw=\col] plot ({\o+4.2+\x*0.8},{2.6*exp(-0.5*((\x-\mu)/1.0)^2)});
  \fill[\col] ({\o+4.2},{2.6*exp(-0.5*(\mu)^2)}) circle (0.2);
  \draw[->, line width=1.2pt] ({\o+4.9},3.6) -- ({\o+4.3},{2.6*exp(-0.5*(\mu)^2)+0.25});
  \node[font=\large\bfseries, anchor=south west] at ({\o+4.7},3.6) {$\pi$ = densidade em 0};
  \node[font=\large, text width=9cm, align=center] at ({\o+4.2},-1.5) {\res};}
\node[font=\large, text width=19cm, align=center] at (10.0,-3.0) {se \mbox{$\pi>\chi$} (o limiar), os marcos $m_j$ e $m_k$ são \textbf{unificados}};
""")


# ------------------------------------------------------------------ melhorias de eficiencia
w("melhorias-eficiencia", boxes([
  ("Mapas locais", r"unir cedo o que é óbvio e inferir \textbf{entre mapas locais}: reduz a complexidade em ordens de grandeza"),
  ("Vetores de medições", r"medições do \textbf{mesmo instante} nunca são o mesmo marco: testar o vetor inteiro de uma vez"),
  ("Desfazer associações", r"fácil de desfazer, difícil saber \textbf{quando}: o algoritmo do capítulo não faz"),
  ("Informação negativa", r"\textbf{não ver} um marco também informa, mas exige modelo de oclusão")], w=4.6, h=4.6, cols=4, font=r"\normalsize",
  cap=r"o algoritmo básico testa \textbf{todos os pares} de marcos e refaz o mapa a cada união", capw=19))

# ------------------------------------------------------------------ associacao iterativa (corredor com deriva)
w("associacao-iterativa", r"""
\tikzset{d/.style={circle, fill=dblue, inner sep=1.4pt}}
\node[font=\Large\bfseries] at (3.0,5.5) {1. deriva};
\draw[dblue, line width=2.2pt] (0.5,0.5) -- (0.5,4.5) -- (4.5,4.5) -- (4.5,0.5) -- (1.6,0.5) -- (1.6,3.6);
\foreach \y in {0.5,1.5,2.5,3.5} {\fill[dblue] (0.5,\y) circle (0.12); \fill[dred] (1.6,\y) circle (0.12);}
\node[font=\large, text width=6.6cm, align=center] at (3.0,-0.8) {o corredor aparece \textbf{duas vezes}};
\node[font=\Large\bfseries] at (10.6,5.5) {2. restrições};
\draw[dblue, line width=2.2pt] (8.1,0.5) -- (8.1,4.5) -- (12.1,4.5) -- (12.1,0.5) -- (9.2,0.5) -- (9.2,3.6);
\foreach \y in {0.5,1.5,2.5,3.5} {\fill[dblue] (8.1,\y) circle (0.12); \fill[dred] (9.2,\y) circle (0.12); \draw[dorange, dashed, line width=1.8pt] (8.1,\y) -- (9.2,\y);}
\node[font=\large, text width=6.6cm, align=center] at (10.6,-0.8) {pares de poses \textbf{provavelmente iguais} viram restrições};
\node[font=\Large\bfseries] at (18.2,5.5) {3. mapa consistente};
\draw[dgreen, line width=2.6pt] (15.7,0.5) -- (15.7,4.5) -- (19.7,4.5) -- (19.7,0.5) -- (15.7,0.5);
\foreach \y in {0.5,1.5,2.5,3.5} {\fill[dgreen] (15.7,\y) circle (0.14);}
\node[font=\large, text width=6.6cm, align=center] at (17.7,-0.8) {o caminho se \textbf{fecha}; um só corredor};
\draw[dtrans, line width=2.4pt, -{Stealth[length=3.6mm]}] (6.0,3.0) -- (7.0,3.0);
\draw[dtrans, line width=2.4pt, -{Stealth[length=3.6mm]}] (13.6,3.0) -- (14.6,3.0);
""")

# ------------------------------------------------------------------ comparacao EKF x EIF
def _linha(y, rot, a, b):
    return (r"\node[dbox, draw=black!60, text width=3.4cm, minimum height=1.25cm, font=\large\bfseries, line width=1.2pt, fill=dshade!40] at (1.9,%s) {%s};" % (y, rot)
            + r"\node[dbox, draw=dblue, text width=7.6cm, minimum height=1.25cm, font=\large, line width=1.4pt] at (8.8,%s) {%s};" % (y, a)
            + r"\node[dbox, draw=dorange, text width=7.6cm, minimum height=1.25cm, font=\large, line width=1.4pt] at (17.2,%s) {%s};" % (y, b))
w("comparacao-ekf-eif", "\n".join([
  r"\node[font=\Large\bfseries, text=dblue] at (8.8,9.9) {EKF SLAM};",
  r"\node[font=\Large\bfseries, text=dorange] at (17.2,9.9) {EIF SLAM};",
  _linha(8.4, "Problema", "SLAM \\textbf{online}", "SLAM \\textbf{completo}"),
  _linha(6.9, "Posterior", r"pose atual e mapa: $p(x_t,m\mid\cdot)$", r"caminho todo e mapa: $p(x_{0:t},m\mid\cdot)$"),
  _linha(5.4, "Representação", r"média $\mu$ e covariância $\Sigma$ (\textbf{cheia})", r"vetor $\xi$ e matriz $\Omega$ (\textbf{esparsa})"),
  _linha(3.9, "Execução", r"\textbf{incremental}: atualiza para sempre", r"em \textbf{lote}: todos os dados na memória"),
  _linha(2.4, "Linearização", r"com os dados até o instante $t$", r"com \textbf{todos} os dados, \textbf{refeita}"),
  _linha(0.9, "Correspondência", r"máxima verossimilhança, \textbf{sem desfazer}", r"busca gananciosa sobre \textbf{pares de marcos}"),
  _linha(-0.6, "Mapa", r"esparso: menos de \textbf{1.000} marcos", r"\textbf{muito maior}")]))

# ------------------------------------------------------------------ robo Groundhog (esquema)
w("groundhog", r"""
\tikzset{t/.style={font=\large, fill=white, inner sep=2pt, text width=4.2cm, align=center},
        ar/.style={line width=1.6pt, -{Stealth[length=3mm]}}}
% chassi, cabine e rodas
\draw[line width=2.2pt, draw=dblue, fill=dblue!12, rounded corners=6pt] (4.0,3.0) rectangle (12.6,5.0);
\draw[line width=2.2pt, draw=dblue, fill=white, rounded corners=4pt] (5.0,5.0) rectangle (9.4,6.8);
\foreach \x in {5.2,11.4} {\fill[black!85] (\x,2.9) circle (1.15); \draw[fill=dorange!55, draw=black, line width=1.6pt] (\x,2.9) circle (0.55);}
% laser na frente
\draw[line width=1.8pt, fill=dred!55, draw=black] (12.0,5.0) rectangle (12.9,5.8);
\draw[dred, line width=2.2pt] (12.9,5.4) ++(-55:1.0) arc (-55:55:1.0);
\draw[dred, line width=2.2pt] (12.9,5.4) ++(-55:1.6) arc (-55:55:1.6);
% camera
\draw[line width=1.8pt, fill=dgreen!50, draw=black] (5.2,6.8) rectangle (6.0,7.4);
% sensores de gas e afundamento (frente, embaixo)
\fill[dorange!80] (12.6,3.6) circle (0.28); \fill[dorange!80] (12.6,4.3) circle (0.28);
% computador de bordo
\draw[line width=1.6pt, fill=dblue!25, draw=dblue] (6.6,5.4) rectangle (8.8,6.4); \node[font=\normalsize\bfseries] at (7.7,5.9) {PC};
% legendas
\node[t] at (16.2,7.6) {\textbf{laser}\\ varredura do ambiente};
\draw[ar, dred] (15.0,7.2) -- (13.5,6.0);
\node[t] at (2.2,8.2) {\textbf{câmeras} de vídeo};
\draw[ar, dgreen] (3.5,7.9) -- (5.2,7.3);
\node[t] at (9.4,8.6) {\textbf{computador} de bordo};
\draw[ar, dblue] (8.6,8.1) -- (7.9,6.5);
\node[t] at (16.2,1.8) {\textbf{sensores de gás} e de \textbf{afundamento}};
\draw[ar, dorange] (15.0,2.4) -- (12.9,3.7);
\node[font=\Large, text width=17cm, align=center] at (9.0,0.0) {cerca de \textbf{680 kg} (1.500 libras), construído para \textbf{mapear minas abandonadas}};
""")

# ------------------------------------------------------------------ casamento de varreduras aos pares: deriva acumulada
w("casamento-varreduras", r"""
\def\n{10}
\foreach \k in {0,...,\n} {
  \pgfmathsetmacro{\ang}{90-\k*33}
  \pgfmathsetmacro{\r}{0.10+\k*0.07}
  \coordinate (s\k) at ({6.0+4.6*cos(\ang)},{4.4+3.0*sin(\ang)});
  \draw[dorange, line width=1.6pt, fill=dorange!12, fill opacity=0.5] (s\k) circle (\r+0.25);
}
\foreach \k in {0,...,9} {\pgfmathtruncatemacro{\j}{\k+1}\draw[dblue, line width=2.2pt, -{Stealth[length=3mm]}] (s\k) -- (s\j);}
\foreach \k in {0,...,\n} {\fill[dblue] (s\k) circle (0.14);}
\draw[dred, line width=2.6pt, dashed, {Stealth[length=3.4mm]}-{Stealth[length=3.4mm]}] (s0) -- (s10);
\node[font=\large\bfseries, text=dred, fill=white, inner sep=2pt] at (6.0,8.4) {sem ligação: o mesmo lugar, visto como lugares distintos};
\node[font=\large, text width=7.0cm, align=center] at (6.0,4.4) {cada varredura casa só com a \textbf{anterior}; o erro \textbf{se acumula} (círculos crescentes)};
\node[font=\Large\bfseries, anchor=west] at (12.4,6.6) {resultado};
\node[font=\large, anchor=west, text width=6.0cm] at (12.4,5.3) {mapa \textbf{inconsistente}: vários corredores aparecem \textbf{mais de uma vez}};
\node[font=\large, anchor=west, text width=6.0cm] at (12.4,3.2) {falta \textbf{fechar o ciclo}};
""")

# ------------------------------------------------------------------ submapas como nos de pose
w("submapas-nos", r"""
\tikzset{sub/.style={draw=dblue, dashed, line width=1.5pt, fill=dblue!7, rounded corners=6pt},
        sp/.style={decorate, decoration={zigzag, segment length=2.8mm, amplitude=1.2mm}, line width=1.4pt, draw=dorange}}
\foreach \px/\py in {1.2/1.8,1.2/3.8,1.2/5.8,8.4/5.8,8.4/3.8,8.4/1.8} {\draw[sub] ({\px-0.75},{\py-0.95}) rectangle ({\px+0.75},{\py+0.95});}
\foreach \px/\py in {2.8/7.2,4.8/7.2,6.8/7.2} {\draw[sub] ({\px-0.95},{\py-0.75}) rectangle ({\px+0.95},{\py+0.75});}
\draw[sub] (0.45,6.0) rectangle (1.95,7.95);
\draw[dblue, line width=2.6pt] (1.2,1.0) -- (1.2,7.2) -- (8.4,7.2) -- (8.4,1.0);
\coordinate (n1) at (1.2,1.8); \coordinate (n2) at (1.2,3.8); \coordinate (n3) at (1.2,5.8); \coordinate (n4) at (2.8,7.2); \coordinate (n5) at (4.8,7.2); \coordinate (n6) at (6.8,7.2); \coordinate (n7) at (8.4,5.8); \coordinate (n8) at (8.4,3.8); \coordinate (n9) at (8.4,1.8);
\foreach \a/\b in {n1/n2,n2/n3,n3/n4,n4/n5,n5/n6,n6/n7,n7/n8,n8/n9} {\draw[sp] (\a) -- (\b);}
\foreach \k in {n1,n2,n3,n4,n5,n6,n7,n8,n9} {\fill[dblue] (\k) circle (0.2);}
\draw[line width=1.4pt, {Stealth[length=2.6mm]}-{Stealth[length=2.6mm]}] (-0.7,2.8) -- (-0.7,4.8); \node[font=\large\bfseries, rotate=90] at (-1.15,3.8) {5 m};
\fill[dblue] (11.0,6.6) circle (0.2); \node[font=\large, anchor=west] at (11.5,6.6) {nó de pose (coordenadas do submapa)};
\draw[sub] (10.8,4.9) rectangle (11.4,5.6); \node[font=\large, anchor=west] at (11.7,5.25) {submapa a cada \textbf{5 m} percorridos};
\draw[sp] (10.8,3.6) -- (11.8,3.6); \node[font=\large, anchor=west] at (12.0,3.6) {restrição de movimento};
\node[font=\large, anchor=west, text width=7.0cm] at (11.0,1.8) {dentro dos 5 m, a deriva é \textbf{pequena}, e o casamento de varreduras funciona \textbf{bem}};
""")

# ------------------------------------------------------------------ inicializacao pelos controles
w("inicializacao-controles", r"""
\tikzset{p/.style={circle, draw=dblue, fill=dblue!12, line width=1.6pt, minimum size=0.55cm}}
\draw[dgreen, dashed, line width=2.2pt, smooth] plot coordinates {(0.90,1.50) (2.79,1.74) (4.63,2.21) (6.39,2.90) (8.06,3.81) (9.60,4.93) (10.99,6.22) (12.21,7.68) (13.24,9.28)}; \fill[dgreen] (13.24,9.28) circle (0.22);
\draw[dblue, line width=2.0pt, smooth] plot coordinates {(0.90,1.50) (2.79,1.69) (4.65,2.07) (6.47,2.63) (8.22,3.37) (9.89,4.28) (11.45,5.35) (12.91,6.58) (14.23,7.94)};
\node[p] (e0) at (0.90,1.50) {}; \draw[->, line width=1.6pt, draw=dblue] (e0) -- ++(0.0:0.7);
\node[p] (e1) at (2.79,1.69) {}; \draw[->, line width=1.6pt, draw=dblue] (e1) -- ++(5.7:0.7);
\node[p] (e2) at (4.65,2.07) {}; \draw[->, line width=1.6pt, draw=dblue] (e2) -- ++(11.5:0.7);
\node[p] (e3) at (6.47,2.63) {}; \draw[->, line width=1.6pt, draw=dblue] (e3) -- ++(17.2:0.7);
\node[p] (e4) at (8.22,3.37) {}; \draw[->, line width=1.6pt, draw=dblue] (e4) -- ++(22.9:0.7);
\node[p] (e5) at (9.89,4.28) {}; \draw[->, line width=1.6pt, draw=dblue] (e5) -- ++(28.6:0.7);
\node[p] (e6) at (11.45,5.35) {}; \draw[->, line width=1.6pt, draw=dblue] (e6) -- ++(34.4:0.7);
\node[p] (e7) at (12.91,6.58) {}; \draw[->, line width=1.6pt, draw=dblue] (e7) -- ++(40.1:0.7);
\node[p] (e8) at (14.23,7.94) {}; \draw[->, line width=1.6pt, draw=dblue] (e8) -- ++(45.8:0.7);

\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (1.85,0.99) {$u_{1}$};
\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (3.72,1.28) {$u_{2}$};
\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (5.56,1.75) {$u_{3}$};
\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (7.34,2.40) {$u_{4}$};
\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (9.05,3.22) {$u_{5}$};
\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (10.67,4.22) {$u_{6}$};
\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (12.18,5.36) {$u_{7}$};
\node[font=\normalsize, text=dblue, fill=white, inner sep=1pt] at (13.57,6.66) {$u_{8}$};

\node[font=\large\bfseries, anchor=east] at (0.5,1.5) {$\mu_0=(0\ 0\ 0)^{\top}$};
\node[font=\large, anchor=west, text width=6.4cm] at (16.2,5.6) {\textcolor{dblue}{\textbf{estimativa} $\mu_{0:t}$}: encadeia o modelo de movimento com os controles $u_t$};
\node[font=\large, anchor=west, text width=6.4cm] at (16.2,3.6) {\textcolor{dgreen}{\textbf{caminho real}} (desconhecido): a estimativa \textbf{deriva}};
\node[font=\large, anchor=west, text width=6.4cm] at (16.2,1.8) {só a parte \textbf{determinística}, \textbf{sem medições}};
""")

# ------------------------------------------------------------------ ancora e controles em Omega
w("ancora-controles", r"""
\def\cw{1.6}
\tikzset{p/.style={circle, draw=dblue, fill=dblue!12, line width=1.8pt, minimum size=1.1cm, font=\large},
        sp/.style={decorate, decoration={zigzag, segment length=3mm, amplitude=1.3mm}, line width=1.5pt, draw=dblue}}
\foreach \i in {0,1,2,3} {\node[p] (q\i) at ({1.0+\i*2.6},6.6) {$x_\i$};}
\foreach \i/\j in {0/1,1/2,2/3} {\draw[sp] (q\i) -- (q\j);}
\draw[line width=3pt, draw=dred] (-0.25,5.6) -- (-0.25,7.6); \draw[line width=1.6pt, draw=dred] (-0.25,5.9) -- (-0.7,5.45); \draw[line width=1.6pt, draw=dred] (-0.25,6.5) -- (-0.7,6.05); \draw[line width=1.6pt, draw=dred] (-0.25,7.1) -- (-0.7,6.65);
\node[font=\large\bfseries, text=dred, anchor=west] at (9.0,7.8) {âncora: $x_0$ fixo na origem};
\foreach \i in {0,...,3} {\foreach \j in {0,...,3} {\draw[black!30, line width=0.5pt] ({11.0+\j*\cw},{3.8-\i*\cw+1.6}) rectangle ({11.0+(\j+1)*\cw},{3.8-(\i+1)*\cw+1.6});}}
\fill[dred!75] (11.04,5.36) rectangle (12.56,3.84); \node[font=\Large\bfseries, text=white] at (11.8,4.6) {$\infty$};
\foreach \i in {0,...,3} {\foreach \j in {0,...,3} {\pgfmathtruncatemacro{\d}{abs(\i-\j)} \ifnum\d=1 \fill[dblue!45] ({11.0+\j*\cw+0.04},{5.4-\i*\cw-0.04}) rectangle ({11.0+(\j+1)*\cw-0.04},{5.4-(\i+1)*\cw+0.04}); \fi}}
\foreach \i in {1,2,3} {\fill[dblue!70] ({11.0+\i*\cw+0.04},{5.4-\i*\cw-0.04}) rectangle ({11.0+(\i+1)*\cw-0.04},{5.4-(\i+1)*\cw+0.04});}
\draw[line width=1.8pt] (11.0,5.4) rectangle (17.4,-1.0);
\foreach \i in {0,...,3} {\node[font=\large] at ({11.8+\i*\cw},5.8) {$x_\i$}; \node[font=\large] at (10.55,{4.6-\i*\cw}) {$x_\i$};}
\node[font=\large, anchor=west, text width=8.6cm] at (0.0,3.6) {\textcolor{dred}{\textbf{âncora}}: valor infinito em $x_0$; sem ela, $\Omega$ seria \textbf{singular} (só há informação relativa)};
\node[font=\large, anchor=west, text width=8.6cm] at (0.0,1.4) {\textcolor{dblue}{\textbf{cada controle}} $u_t$ soma um bloco que liga $x_{t-1}$ e $x_t$: a matriz fica em \textbf{blocos tridiagonais}};
""")

# ------------------------------------------------------------------ medicao: geometria e blocos 5x5
w("medicao-blocos", r"""
\tikzset{p/.style={circle, draw=dblue, fill=dblue!12, line width=1.8pt, minimum size=1.0cm},
        m/.style={circle, draw=dgreen, fill=dgreen!12, line width=1.8pt, minimum size=1.0cm}}
\node[p] (r) at (1.8,2.0) {}; \draw[->, line width=2pt, draw=dblue] (r) -- ++(25:1.0);
\node[font=\large, anchor=north] at (1.8,1.3) {$x_t$};
\node[m] (l) at (7.4,5.4) {}; \node[font=\large, anchor=south] at (7.4,6.0) {$m_j$};
\draw[dorange, line width=2.6pt] (r) -- (l); \node[font=\large\bfseries, text=dorange, fill=white, inner sep=2pt] at (4.5,3.9) {$z_t^i$ medido};
\draw[dred, dashed, line width=2.4pt] (r) -- (7.0,4.4); \node[font=\large\bfseries, text=dred, fill=white, inner sep=2pt, anchor=west] at (4.2,2.4) {$\hat z_t^i$ esperado};
\draw[<->, line width=1.6pt] (7.0,4.4) -- (7.35,5.0); \node[font=\large, anchor=west] at (7.7,4.5) {$z-\hat z$};
\def\cw{0.9}
\foreach \i in {0,...,4} {\foreach \j in {0,...,4} {\draw[black!30, line width=0.5pt] ({11.6+\j*\cw},{5.0-\i*\cw}) rectangle ({11.6+(\j+1)*\cw},{5.0-(\i+1)*\cw});}}
\fill[dblue!70] (11.64,4.96) rectangle (14.26,2.34);
\fill[dgreen!70] (14.34,2.26) rectangle (16.06,0.54);
\fill[dorange!75] (14.34,4.96) rectangle (16.06,2.34); \fill[dorange!75] (11.64,2.26) rectangle (14.26,0.54);
\draw[line width=1.8pt] (11.6,5.0) rectangle (16.1,0.5);
\node[font=\large\bfseries, text=white] at (12.95,3.65) {$3\times3$};
\node[font=\large\bfseries, text=white] at (15.2,1.4) {$2\times2$};
\node[font=\large\bfseries, text=white] at (15.2,3.65) {$3\times2$}; \node[font=\large\bfseries, text=white] at (12.95,1.4) {$2\times3$};
\node[font=\large] at (12.95,5.4) {$x_t$}; \node[font=\large] at (15.2,5.4) {$m_j$};
\node[font=\large, text width=10cm, align=center] at (13.8,-0.6) {a parcela $H^\top Q^{-1}H$ é $5\times5$: \textbf{pose}, \textbf{marco} e duas de \textbf{ligação}};
""")

# ------------------------------------------------------------------ resolver: caminho e depois marcos um a um
w("resolver-etapas", r"""
\tikzset{p/.style={circle, draw=dblue, fill=dblue!30, line width=1.8pt, minimum size=1.1cm, font=\large},
        m/.style={circle, draw=dgreen, fill=dgreen!12, line width=1.8pt, minimum size=1.1cm, font=\large}}
\node[font=\Large\bfseries, text=dblue, anchor=west] at (0.0,8.4) {1. caminho: $\Sigma_{0:t}=\tilde\Omega^{-1}$, $\mu_{0:t}=\Sigma_{0:t}\tilde\xi$};
\foreach \i in {0,...,5} {\node[p] (x\i) at ({1.0+\i*2.2},6.6) {$x_\i$};}
\foreach \i/\j in {0/1,1/2,2/3,3/4,4/5} {\draw[dblue, line width=1.8pt] (x\i) -- (x\j);}
\node[font=\large, anchor=west, text width=6.4cm] at (13.6,6.6) {\textbf{todas as poses} de uma vez};
\node[font=\Large\bfseries, text=dgreen, anchor=west, text width=6.4cm] at (13.6,4.4) {2. marcos, \textbf{um a um}, com as poses de $\tau(j)$ \textbf{fixas}};
\node[m] (m1) at (2.1,1.6) {$m_1$}; \node[m] (m2) at (6.5,1.6) {$m_2$}; \node[m] (m3) at (10.9,1.6) {$m_3$};
\foreach \p/\q in {x0/m1,x1/m1,x1/m2,x2/m2,x3/m2,x3/m3,x4/m3} {\draw[->, dorange, line width=1.6pt, -{Stealth[length=2.8mm]}] (\p) -- (\q);}
\node[font=\large, anchor=west, text width=6.4cm] at (13.6,2.0) {$\mu_j=\Omega_{j,j}^{-1}(\xi_j-\Omega_{j,\tau(j)}\tilde\mu_{\tau(j)})$};
\node[font=\large, text width=19cm, align=center] at (9.5,-0.2) {devolve a \textbf{média} de tudo, mas só a \textbf{covariância do caminho}};
""")

# ------------------------------------------------------------------ iterar: relinearizar em um ponto melhor
w("iterar-linearizacao", r"""
\def\tc{1.35}
\foreach \o/\a/\col/\tit/\res/\am/\bm in {0/0.3/dred/{1ª passada: ponto inicial ruim}/{erro \textbf{grande}}/north east/north west, 11.0/1.2/dgreen/{2ª passada: ponto melhorado}/{erro \textbf{pequeno}}/north east/north west} {
  \node[font=\Large\bfseries, text=\col] at ({\o+4.6},6.2) {\tit};
  \draw[line width=1.4pt, ->] ({\o-0.3},0) -- ({\o+9.6},0); \draw[line width=1.4pt, ->] ({\o},-0.3) -- ({\o},4.8);
  \draw[domain=0:3.14, samples=70, smooth, line width=2.6pt, draw=dblue] plot ({\o+\x*2.7},{3.6*sin(\x r)});
  \begin{scope}\clip ({\o-0.2},-0.2) rectangle ({\o+9.6},4.7);
  \draw[domain=\a-0.3:\a+1.8, samples=2, line width=2.2pt, draw=\col] plot ({\o+\x*2.7},{3.6*(sin(\a r)+cos(\a r)*(\x-\a))});
  \end{scope}
  \fill[\col] ({\o+\a*2.7},{3.6*sin(\a r)}) circle (0.2);
  \draw[dashed, line width=1.2pt] ({\o+\tc*2.7},0) -- ({\o+\tc*2.7},{3.6*sin(\tc r)});
  \fill[dblue] ({\o+\tc*2.7},{3.6*sin(\tc r)}) circle (0.2);
  \node[font=\large, anchor=\bm] at ({\o+\tc*2.7},-0.1) {$\theta$ real};
  \node[font=\large, anchor=\am] at ({\o+\a*2.7},-0.1) {$\mu_\theta$};
  \node[font=\large, text width=9cm, align=center] at ({\o+4.6},-1.6) {\res};}
\node[font=\large, text width=21cm, align=center] at (10.6,-3.0) {ilustração com o seno: a \textbf{orientação} entra por senos e cossenos, então a reta tangente só serve \textbf{perto} do ponto de linearização};
""")


# ------------------------------------------------------------------ o que o EIF pode na correspondencia
w("eif-pode", r"""
\tikzset{m/.style={circle, draw=dgreen, fill=dgreen!12, line width=1.6pt, minimum size=0.9cm, font=\normalsize},
        s/.style={circle, draw=dorange, fill=dorange!30, line width=2.2pt, minimum size=0.9cm, font=\normalsize},
        k/.style={dbox, text width=3.6cm, minimum height=1.3cm, font=\large, line width=1.6pt}}
% painel 1
\draw[draw=dblue, line width=2pt, fill=dblue!5, rounded corners=10pt] (0,-0.6) rectangle (7.2,8.6);
\node[font=\Large\bfseries, text=dblue, text width=6.6cm, align=center] at (3.6,7.7) {1. qualquer conjunto de marcos};
\node[m] (a1) at (1.2,5.0) {$m_1$}; \node[s] (a2) at (2.9,6.2) {$m_2$}; \node[m] (a3) at (1.9,3.1) {$m_3$}; \node[m] (a4) at (4.0,1.9) {$m_4$};
\node[s] (a5) at (5.6,6.0) {$m_5$}; \node[s] (a6) at (5.8,2.9) {$m_6$};
\draw[dorange, dashed, line width=2pt] (a2) -- (a5) -- (a6) -- (a2);
\node[font=\large, text width=6.6cm, align=center] at (3.6,0.8) {testar \textbf{qualquer grupo}, e não só os vistos \textbf{em sequência}};
% painel 2
\draw[draw=dgreen, line width=2pt, fill=dgreen!5, rounded corners=10pt] (8.0,-0.6) rectangle (15.2,8.6);
\node[font=\Large\bfseries, text=dgreen, text width=6.6cm, align=center] at (11.6,7.7) {2. busca e mapa intercalados};
\node[k, draw=dorange] (h) at (11.6,5.9) {hipótese: $m_j=m_k$};
\node[k, draw=dblue] (r) at (11.6,2.9) {refazer o mapa};
\draw[dtrans, line width=2.2pt, -{Stealth[length=3.2mm]}] (h.south west) ++(0.4,0) -- ([xshift=0.4cm]r.north west);
\draw[dtrans, line width=2.2pt, -{Stealth[length=3.2mm]}] ([xshift=-0.4cm]r.north east) -- ([xshift=-0.4cm]h.south east);
\node[font=\large, text width=6.6cm, align=center] at (11.6,0.8) {outras hipóteses ficam \textbf{mais} ou \textbf{menos} prováveis};
% painel 3
\draw[draw=dred, dashed, line width=2pt, fill=dred!4, rounded corners=10pt] (16.0,-0.6) rectangle (23.2,8.6);
\node[font=\Large\bfseries, text=dred, text width=6.6cm, align=center] at (19.6,7.7) {3. desfazer decisões};
\node[m, minimum size=1.3cm] (u1) at (17.6,5.0) {}; \node[m, minimum size=1.3cm] (u2) at (18.3,5.0) {};
\node[font=\large, text width=3cm, align=center] at (17.95,3.7) {unidos};
\draw[dred, line width=2.2pt, -{Stealth[length=3.2mm]}] (18.9,5.4) -- (20.4,5.4); \node[font=\large\bfseries, text=dred] at (19.65,5.9) {desfazer};
\node[m, minimum size=1.3cm] (v1) at (21.0,5.0) {}; \node[m, minimum size=1.3cm] (v2) at (22.4,5.0) {};
\node[font=\large, text width=3cm, align=center] at (21.7,3.7) {separados};
\node[font=\large, text width=6.6cm, align=center] at (19.6,1.4) {possível \textbf{em princípio};\\ o algoritmo do capítulo \textbf{não} faz};
""")
