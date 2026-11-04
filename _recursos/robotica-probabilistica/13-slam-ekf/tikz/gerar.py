"""Gera os diagramas TikZ da aula 13 (SLAM com EKF). Uso: python3 gerar.py && bash build.sh"""
exec(open("_helpers.py").read())

# ------------------------------------------------------------ entradas e saídas do SLAM
w("slam-entradas-saidas", r"""
\tikzset{c/.style={dbox, text width=4.6cm, minimum height=1.9cm, font=\large, line width=1.6pt}}
\node[font=\Large\bfseries, black!70] at (2.9,8.3) {o que o robô tem};
\node[font=\Large\bfseries, black!70] at (16.4,8.3) {o que quer descobrir};
\node[c, draw=dblue] (a) at (2.9,6.2) {\textbf{\textcolor{dblue}{Medições}}\\ o que os sensores veem};
\node[c, draw=dblue] (b) at (2.9,3.5) {\textbf{\textcolor{dblue}{Controles}}\\ o que o robô mandou fazer};
\node[dbox, draw=dgreen, fill=dgreen!10, line width=2.2pt, text width=3.6cm, minimum height=2.8cm, font=\Huge\bfseries] (s) at (9.5,4.9) {SLAM};
\node[c, draw=dorange] (m) at (16.4,6.2) {\textbf{\textcolor{dorange}{Mapa}}\\ onde estão os marcos};
\node[c, draw=dorange] (p) at (16.4,3.5) {\textbf{\textcolor{dorange}{Pose}}\\ onde o robô está};
\foreach \n in {a,b} {\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (\n.east) -- (s.west);}
\foreach \n in {m,p} {\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (s.east) -- (\n.west);}
\node[dbox, draw=dred, dashed, line width=1.5pt, text width=12.4cm, minimum height=1.2cm, font=\large] at (9.5,0.9) {o robô \textbf{não conhece} nem o mapa nem as próprias poses: precisa estimar \textbf{os dois ao mesmo tempo}};
""")

# ------------------------------------------------------------ online x full
w("online-vs-full", r"""
\tikzset{p/.style={circle, draw=dblue, fill=dblue!15, line width=1.6pt, minimum size=1.1cm, font=\large},
        f/.style={circle, draw=black!40, dashed, fill=white, line width=1.3pt, minimum size=1.1cm, font=\large, text=black!50},
        mp/.style={dbox, draw=dgreen, fill=dgreen!10, line width=1.6pt, text width=4.2cm, minimum height=1.2cm, font=\large\bfseries}}
\node[font=\Large\bfseries, dblue] at (4.4,8.6) {SLAM online};
\node[font=\Large\bfseries, dorange] at (14.6,8.6) {SLAM completo (\emph{full})};
\foreach \i in {1,2,3,4,5} {
  \node[f] (a\i) at ({0.9+(\i-1)*1.75},6.4) {$x_\i$};
  \node[p, draw=dorange, fill=dorange!15] (b\i) at ({11.1+(\i-1)*1.75-1.0},6.4) {$x_\i$};
}
\node[p] (a5) at (7.9,6.4) {$x_5$};
\foreach \i/\j in {1/2,2/3,3/4,4/5} {
  \draw[black!40, dashed, line width=1.2pt, -{Stealth[length=2.4mm]}] (a\i) -- (a\j);
  \draw[dorange, line width=1.4pt, -{Stealth[length=2.4mm]}] (b\i) -- (b\j);
}
\node[mp] (ma) at (4.4,3.0) {mapa};
\node[mp] (mb) at (14.6,3.0) {mapa};
\draw[dblue, line width=1.8pt, -{Stealth[length=3mm]}] (a5.south) -- (ma.north east);
\foreach \i in {1,2,3,4,5} {\draw[dorange, line width=1.2pt, -{Stealth[length=2.4mm]}] (b\i.south) -- (mb.north);}
\node[font=\large, text width=8.4cm, align=center] at (4.4,1.5) {só a \textbf{pose atual} e o mapa;\\ as poses passadas são \textbf{integradas} e descartadas};
\node[font=\large, text width=8.4cm, align=center] at (14.6,1.5) {o \textbf{caminho inteiro} e o mapa};
\node[font=\large, black!70] at (4.4,0.4) {$p(x_t,\, m \mid z_{1:t},\, u_{1:t})$};
\node[font=\large, black!70] at (14.6,0.4) {$p(x_{1:t},\, m \mid z_{1:t},\, u_{1:t})$};
""")

# ------------------------------------------------------------ contínuo e discreto
w("continuo-discreto", r"""
\tikzset{c/.style={dbox, text width=8.4cm, minimum height=7.2cm, line width=1.6pt, font=\large, anchor=north}}
\node[c, draw=dblue] at (4.6,7.9) {};
\node[font=\Large\bfseries, dblue] at (4.6,7.2) {parte contínua};
\draw[daxis, line width=1.1pt] (0.8,2.1) -- (8.2,2.1); \draw[daxis, line width=1.1pt] (0.8,2.1) -- (0.8,6.4);
\draw[dorange, fill=dorange!15, line width=1.5pt] (3.0,3.4) -- (3.9,3.6) -- (3.0,3.9) -- cycle;
\fill[dgreen] (5.6,5.5) circle (0.16); \draw[dgreen, line width=1.2pt] (5.6,5.5) ellipse (0.55 and 0.4);
\fill[dgreen] (7.0,3.2) circle (0.16); \draw[dgreen, line width=1.2pt] (7.0,3.2) ellipse (0.4 and 0.55);
\node[font=\large] at (4.6,1.0) {\textbf{onde estão} o robô e os marcos};
\node[c, draw=dorange] at (14.4,7.9) {};
\node[font=\Large\bfseries, dorange] at (14.4,7.2) {parte discreta};
\draw[dorange, fill=dorange!15, line width=1.5pt] (11.5,5.35) -- (12.4,5.55) -- (11.5,5.85) -- cycle;
\node[font=\large\bfseries, dorange] at (11.95,4.85) {robô};
\draw[black!70, line width=1.5pt, -{Stealth[length=2.8mm]}] (12.5,5.6) -- (14.2,5.8);
\fill[black] (14.4,5.8) circle (0.13); \node[font=\large, anchor=west] at (14.6,5.8) {medição};
\fill[dgreen] (13.0,3.2) circle (0.16); \node[font=\large] at (13.0,2.6) {marco A};
\fill[dgreen] (16.0,3.2) circle (0.16); \node[font=\large] at (16.0,2.6) {marco B};
\draw[black!60, dashed, line width=1.3pt, -{Stealth[length=2.6mm]}] (14.3,5.6) -- (13.1,3.45);
\draw[black!60, dashed, line width=1.3pt, -{Stealth[length=2.6mm]}] (14.5,5.6) -- (15.9,3.45);
\node[font=\Large\bfseries, dred] at (14.4,4.3) {?};
\node[font=\large] at (14.4,1.0) {é o \textbf{mesmo marco} de antes? \textbf{sim} ou \textbf{não}};
""")

# ------------------------------------------------------------ vetor de estado combinado
w("estado-combinado", r"""
\tikzset{k/.style={draw=black!70, line width=1.2pt, minimum width=1.25cm, minimum height=1.1cm, font=\large, inner sep=1pt, fill=white}}
\foreach \c/\t in {0/$x$,1/$y$,2/$\theta$} {\node[k, fill=dorange!15] (r\c) at ({0.7+\c*1.25},4.2) {\t};}
\foreach \c/\t in {0/$m_{1,x}$,1/$m_{1,y}$,2/$s_1$} {\node[k, fill=dblue!12] (u\c) at ({5.0+\c*1.25},4.2) {\t};}
\foreach \c/\t in {0/$m_{2,x}$,1/$m_{2,y}$,2/$s_2$} {\node[k, fill=dblue!12] (v\c) at ({9.4+\c*1.25},4.2) {\t};}
\node[font=\Huge] at (13.6,4.2) {$\cdots$};
\foreach \c/\t in {0/$m_{N,x}$,1/$m_{N,y}$,2/$s_N$} {\node[k, fill=dblue!12] (w\c) at ({15.0+\c*1.25},4.2) {\t};}
\draw[decorate, decoration={brace, amplitude=7pt, mirror}, dorange, line width=1.5pt] (0.0,3.5) -- (3.2,3.5);
\node[font=\large\bfseries, dorange] at (1.6,2.5) {robô (3)};
\draw[decorate, decoration={brace, amplitude=7pt, mirror}, dblue, line width=1.5pt] (4.3,3.5) -- (7.5,3.5);
\node[font=\large\bfseries, dblue] at (5.9,2.5) {marco 1 (3)};
\draw[decorate, decoration={brace, amplitude=7pt, mirror}, dblue, line width=1.5pt] (8.7,3.5) -- (11.9,3.5);
\node[font=\large\bfseries, dblue] at (10.3,2.5) {marco 2 (3)};
\draw[decorate, decoration={brace, amplitude=7pt, mirror}, dblue, line width=1.5pt] (14.3,3.5) -- (17.5,3.5);
\node[font=\large\bfseries, dblue] at (15.9,2.5) {marco $N$ (3)};
\draw[decorate, decoration={brace, amplitude=9pt}, black!60, line width=1.5pt] (0.0,5.0) -- (17.5,5.0);
\node[font=\Large\bfseries, black!75] at (8.75,6.3) {estado combinado: $3N + 3$ números};
\node[font=\large, black!70, text width=18cm, align=center] at (8.75,0.9) {$s$ é a \textbf{assinatura} do marco; cada novo marco \textbf{aumenta} o vetor};
""")

# ------------------------------------------------------------ covariância em blocos
_n = 4
_lab = ["robô", "marco 1", "marco 2", "marco 3"]
_cor = {"d": "dorange", "m": "dgreen", "x": "dblue", "c": "dred"}
_o = []
_s = 1.55
for i in range(_n):
    _o.append(r"\node[font=\normalsize\bfseries, anchor=east] at (-0.2,%s) {%s};" % (round(-i * _s - _s / 2 + 6.2, 2), _lab[i]))
    _o.append(r"\node[font=\normalsize\bfseries, rotate=0] at (%s,6.55) {%s};" % (round(i * _s + _s / 2 + 0.2 - 0.2 + 0.0, 2), _lab[i]))
for i in range(_n):
    for j in range(_n):
        if i == j and i == 0: k, t = "d", "robô\\\\$\\times$ robô"
        elif i == j: k, t = "m", "mesmo\\\\marco"
        elif i == 0 or j == 0: k, t = "x", "robô\\\\$\\times$ marco"
        else: k, t = "c", "marcos\\\\diferentes"
        c = _cor[k]
        _o.append(r"\draw[%s, fill=%s!18, line width=1.3pt] (%s,%s) rectangle (%s,%s);" % (c, c, round(j * _s, 2), round(6.2 - i * _s, 2), round(j * _s + _s, 2), round(6.2 - i * _s - _s, 2)))
        _o.append(r"\node[font=\scriptsize, align=center, text=%s] at (%s,%s) {%s};" % (c, round(j * _s + _s / 2, 2), round(6.2 - i * _s - _s / 2, 2), t))
_o.append(r"\node[dbox, draw=dred, line width=1.5pt, text width=8.0cm, minimum height=2.0cm, font=\large, align=left, anchor=west] at (7.4,5.0) {\textbf{\textcolor{dred}{blocos fora da diagonal}}\\ ligam as incertezas: saber mais sobre um marco muda o que se sabe sobre os outros};")
_o.append(r"\node[dbox, draw=dgreen, line width=1.5pt, text width=8.0cm, minimum height=1.6cm, font=\large, align=left, anchor=west] at (7.4,2.4) {\textbf{\textcolor{dgreen}{matriz cheia}}: tamanho $(3N+3)\times(3N+3)$, quase sempre sem zeros};")
_o.append(r"\node[dbox, draw=black!55, fill=white, line width=1.5pt, text width=8.0cm, minimum height=1.6cm, font=\large, align=left, anchor=west] at (7.4,0.3) {\textbf{cada quadrado é um bloco $3\times 3$}: o robô e cada marco têm 3 números; aqui, $N=3$ marcos, ou seja, $12\times 12$ números};")
w("covariancia-blocos", "\n".join(_o))

# ------------------------------------------------------------ ciclo do EKF SLAM
w("ciclo-ekf-slam", r"""
\tikzset{c/.style={dbox, text width=5.3cm, minimum height=3.7cm, font=\large, line width=1.6pt}}
\node[c, draw=dblue] (a) at (3.0,5.2) {\textbf{\textcolor{dblue}{1. Mover}}\\ prevê a nova pose\\ os marcos ficam parados\\ a incerteza da pose \textbf{cresce}};
\node[c, draw=dgreen] (b) at (9.5,5.2) {\textbf{\textcolor{dgreen}{2. Observar}}\\ para cada marco visto, compara o \textbf{esperado} com o \textbf{medido}};
\node[c, draw=dorange] (c) at (16.0,5.2) {\textbf{\textcolor{dorange}{3. Corrigir}}\\ o ganho atualiza a \textbf{pose} \textbf{e o mapa inteiro}};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a.east) -- (b.west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b.east) -- (c.west);
\node[dbox, draw=dred, fill=dred!6, line width=1.5pt, text width=5.6cm, minimum height=1.5cm, font=\large] (n) at (9.5,1.5) {\textbf{marco novo}: inicia na posição \textbf{medida}};
\draw[dred, line width=1.5pt, -{Stealth[length=3mm]}] (n.north) -- (b.south);
\draw[black!55, line width=1.3pt, -{Stealth[length=3mm]}, rounded corners=8pt] (c.north) -- ++(0,1.5) -| (a.north);
\node[font=\large, black!70, fill=dcream, inner sep=2pt] at (9.5,8.2) {a cada passo de tempo};
""")

# ------------------------------------------------------------ fechar o ciclo (4 painéis)
def _painel(ox, titulo, pos, ang, marcos, rob, mrad, ult):
    o = [r"\draw[black!35, line width=1pt, rounded corners=4pt] (%s,0) rectangle (%s,5.6);" % (ox, ox + 4.4)]
    P = [(1.0, 1.2), (3.4, 1.2), (3.4, 3.6), (1.0, 3.6), (1.0, 1.3)]
    L = [(0.35, 2.4), (2.2, 0.4), (4.05, 2.4), (2.2, 4.4)]
    for k in range(len(pos)):
        a = P[pos[k]]; b = P[pos[k + 1]] if k + 1 < len(pos) else None
        if b: o.append(r"\draw[black!55, dotted, line width=1.6pt] (%s,%s) -- (%s,%s);" % (ox + a[0], a[1], ox + b[0], b[1]))
    cur = P[pos[-1]]
    for idx, r in zip(marcos, mrad):
        x, y = L[idx]
        o.append(r"\draw[dblue, fill=dblue!12, line width=1.3pt] (%s,%s) ellipse (%s and %s);" % (ox + x, y, round(r * 1.2, 2), round(r, 2)))
        o.append(r"\fill[dblue] (%s,%s) circle (0.08);" % (ox + x, y))
    o.append(r"\draw[dorange, fill=dorange!20, line width=1.5pt] (%s,%s) ellipse (%s and %s);" % (ox + cur[0], cur[1], round(rob * 1.2, 2), rob))
    o.append(r"\fill[dorange] (%s,%s) circle (0.09);" % (ox + cur[0], cur[1]))
    o.append(r"\node[font=\large\bfseries, text width=4.3cm, align=center] at (%s,-0.9) {%s};" % (ox + 2.2, titulo))
    return "\n".join(o)
w("fechar-ciclo", "\n".join([
  _painel(0.0, "a. primeiro marco", [0, 1], 0, [0, 1], 0.25, [0.18, 0.25], 1),
  _painel(4.9, r"b. a incerteza cresce", [0, 1, 2], 0, [0, 1, 2], 0.4, [0.2, 0.3, 0.4], 2),
  _painel(9.8, r"c. máxima incerteza", [0, 1, 2, 3], 0, [0, 1, 2, 3], 0.55, [0.22, 0.32, 0.42, 0.55], 3),
  _painel(14.7, r"d. revê o 1º marco: \textbf{tudo melhora}", [0, 1, 2, 3, 4], 0, [0, 1, 2, 3], 0.12, [0.1, 0.2, 0.26, 0.34], 4),
  r"\node[font=\large, dorange] at (3.6,7.0) {$\bigcirc$ pose do robô};",
  r"\node[font=\large, dblue] at (9.4,7.0) {$\bigcirc$ marcos};",
  r"\node[font=\large, black!70] at (15.2,7.0) {elipse = incerteza};",
]))

# ------------------------------------------------------------ marco novo: inicialização
w("marco-novo", r"""
\draw[black!45, dashed, line width=1.3pt] (2.5,1.6) -- ({2.5+3.2*cos(20)},{1.6+3.2*sin(20)});
\node[font=\large, black!60, anchor=west] at ({2.5+3.2*cos(20)+0.1},{1.6+3.2*sin(20)}) {direção do robô};
\draw[dorange, fill=dorange!20, line width=1.6pt] (2.5,1.6) circle (0.38);
\draw[dorange, line width=2.2pt, -{Stealth[length=3mm]}] (2.5,1.6) -- ({2.5+0.7*cos(20)},{1.6+0.7*sin(20)});
\node[font=\large\bfseries, dorange, anchor=north] at (2.5,1.1) {robô};
\draw[dblue, line width=2.2pt, -{Stealth[length=3.4mm]}] (2.5,1.6) -- ({2.5+5.6*cos(60)},{1.6+5.6*sin(60)});
\fill[dgreen] ({2.5+5.6*cos(60)},{1.6+5.6*sin(60)}) circle (0.2);
\draw[dgreen, line width=1.5pt] ({2.5+5.6*cos(60)},{1.6+5.6*sin(60)}) circle (0.5);
\node[font=\large\bfseries, dgreen, anchor=west] at ({2.5+5.6*cos(60)+0.7},{1.6+5.6*sin(60)}) {marco novo};
\draw[black!70, line width=1.4pt, -{Stealth[length=2.4mm]}] ({2.5+2.2*cos(20)},{1.6+2.2*sin(20)}) arc (20:60:2.2);
\node[font=\large, black!80] at (5.3,3.55) {ângulo};
\node[font=\large\bfseries, dblue, rotate=60] at ({2.5+2.9*cos(60)-0.4},{1.6+2.9*sin(60)+0.25}) {alcance};
\node[dbox, draw=dgreen, fill=dgreen!8, line width=1.6pt, text width=7.6cm, minimum height=2.6cm, font=\large, align=left, anchor=west] at (10.6,6.0) {\textbf{\textcolor{dgreen}{posição do marco}}\\ = pose do robô + o alcance, na direção do ângulo medido};
\node[dbox, draw=dorange, fill=dorange!8, line width=1.6pt, text width=7.6cm, minimum height=2.6cm, font=\large, align=left, anchor=west] at (10.6,2.6) {\textbf{\textcolor{dorange}{por que importa}}\\ dá ao EKF um \textbf{bom ponto de partida} para linearizar; começar do zero daria um erro enorme};
""")

# ------------------------------------------------------------ decisão: mesmo marco ou novo?
w("mahalanobis-decisao", r"""
\tikzset{e/.style={dblue, fill=dblue!10, line width=1.5pt}}
\draw[e] (3.4,4.6) ellipse (1.9 and 1.3); \fill[dblue] (3.4,4.6) circle (0.1); \node[font=\large, dblue] at (3.4,3.0) {marco 1};
\draw[e] (8.8,5.2) ellipse (1.7 and 1.5); \fill[dblue] (8.8,5.2) circle (0.1); \node[font=\large, dblue] at (8.8,3.4) {marco 2};
\draw[e] (13.2,4.0) ellipse (1.8 and 1.2); \fill[dblue] (13.2,4.0) circle (0.1); \node[font=\large, dblue] at (13.2,2.5) {marco 3};
\fill[dgreen] (9.4,5.7) circle (0.17); \node[font=\large\bfseries, dgreen, anchor=west] at (9.7,5.4) {medição A};
\fill[dred] (16.9,6.3) circle (0.17); \node[font=\large\bfseries, dred, anchor=north] at (16.9,6.0) {medição B};
\node[dbox, draw=dgreen, fill=dgreen!8, line width=1.5pt, text width=5.4cm, minimum height=1.6cm, font=\large] at (4.2,7.9) {\textbf{dentro} da elipse do marco 2: é o \textbf{mesmo marco}};
\node[dbox, draw=dred, fill=dred!6, line width=1.5pt, text width=5.6cm, minimum height=1.6cm, font=\large] at (14.3,8.0) {\textbf{fora} de todas as elipses: \textbf{marco novo}};
\draw[dgreen, line width=1.4pt, -{Stealth[length=2.6mm]}] (7.0,7.5) -- (9.25,5.85);
\draw[dred, line width=1.4pt, -{Stealth[length=2.6mm]}] (15.8,7.3) -- (16.85,6.5);
\node[font=\large, black!75, text width=17cm, align=center] at (9.5,0.8) {a elipse é a \textbf{distância de Mahalanobis} até o limiar $\alpha$: a distância medida em \textbf{desvios-padrão}};
""")

# ------------------------------------------------------------ lista provisória
w("lista-provisoria", r"""
\tikzset{c/.style={dbox, text width=4.4cm, minimum height=2.2cm, font=\large, line width=1.6pt},
        q/.style={dbox, draw=dblue, text width=4.6cm, minimum height=2.2cm, font=\large, line width=1.6pt},
        a/.style={dtrans, line width=1.9pt, -{Stealth[length=3mm]}},
        l/.style={font=\large\bfseries, fill=dcream, inner sep=2pt}}
\node[c, draw=dred] (n) at (2.4,4.6) {\textbf{\textcolor{dred}{Observação nova}}\\ longe de todos os marcos};
\node[c, draw=dorange, fill=dorange!8] (p) at (8.2,4.6) {\textbf{\textcolor{dorange}{Lista provisória}}\\ \textbf{não} corrige a pose};
\node[q] (d) at (14.2,4.6) {vista \textbf{de novo} e a incerteza \textbf{encolheu}?};
\node[c, draw=dgreen, fill=dgreen!8] (m) at (14.2,1.2) {\textbf{\textcolor{dgreen}{Entra no mapa}}};
\node[c, draw=black!55, dashed] (x) at (14.2,8.0) {\textbf{descartada}\\ era ruído};
\draw[a] (n.east) -- (p.west);
\draw[a] (p.east) -- (d.west);
\draw[a, dgreen] (d.south) -- node[l, text=dgreen] {sim} (m.north);
\draw[a, dred] (d.north) -- node[l, text=dred] {não} (x.south);
""")

# ------------------------------------------------------------ evidência de existência do marco
w("evidencia-marco", r"""
\draw[daxis, line width=1.2pt] (1.2,1.6) -- (17.8,1.6) node[right, font=\large] {tempo};
\draw[daxis, line width=1.2pt] (1.2,1.6) -- (1.2,7.8) node[above, font=\large] {evidência $o_j$};
\draw[dred, dashed, line width=1.6pt] (1.2,3.0) -- (17.4,3.0);
\node[font=\large\bfseries, dred, anchor=west] at (1.5,2.6) {limiar: remover o marco};
\foreach \i/\v in {0/5.2,1/6.0,2/6.8,3/6.0,4/6.8,5/6.0,6/5.2,7/4.4,8/3.6,9/2.8} {
  \fill[black!70] ({2.2+\i*1.6},\v) circle (0.12);
}
\draw[dblue, line width=2pt] (2.2,5.2) -- (3.8,6.0) -- (5.4,6.8) -- (7.0,6.0) -- (8.6,6.8) -- (10.2,6.0) -- (11.8,5.2) -- (13.4,4.4) -- (15.0,3.6) -- (16.6,2.8);
\foreach \i/\t/\c in {1/{+}/dgreen,2/{+}/dgreen,3/{$-$}/dred,4/{+}/dgreen,5/{$-$}/dred,6/{$-$}/dred,7/{$-$}/dred,8/{$-$}/dred,9/{$-$}/dred} {
  \node[font=\Large\bfseries, text=\c] at ({2.2+\i*1.6},1.1) {\t};
}
\node[font=\large, dgreen, text width=5cm, align=center] at (6.0,0.2) {marco \textbf{observado}: sobe};
\node[font=\large, dred, text width=7cm, align=center] at (13.2,0.2) {deveria ser visto e \textbf{não foi}: desce};
\fill[dred] (16.6,2.8) circle (0.2); \node[font=\large\bfseries, dred, anchor=west] at (16.95,2.8) {removido};
""")

# ------------------------------------------------------------ confusão de marcos
w("confusao-marcos", r"""
\tikzset{c/.style={dbox, text width=8.4cm, minimum height=7.0cm, line width=1.6pt, font=\large, anchor=north},
        e/.style={dblue, fill=dblue!10, line width=1.4pt}}
\node[c, draw=dred] at (4.6,8.2) {};
\node[font=\Large\bfseries, dred] at (4.6,7.5) {marcos muito próximos};
\draw[e] (3.5,4.4) ellipse (1.7 and 1.3); \fill[dblue] (3.5,4.4) circle (0.1);
\draw[e] (5.6,4.4) ellipse (1.7 and 1.3); \fill[dblue] (5.6,4.4) circle (0.1);
\fill[dred] (4.55,4.4) circle (0.15); \node[font=\Huge\bfseries, dred] at (4.55,5.9) {?};
\node[font=\large, text width=7.4cm, align=center] at (4.6,2.0) {as elipses \textbf{se sobrepõem}: a medição serve para os \textbf{dois}};
\node[c, draw=dgreen] at (14.4,8.2) {};
\node[font=\Large\bfseries, dgreen] at (14.4,7.5) {marcos distantes e distintos};
\draw[e] (12.1,4.4) ellipse (1.3 and 1.2); \fill[dblue] (12.1,4.4) circle (0.1);
\draw[e] (16.7,4.4) ellipse (1.3 and 1.2); \fill[dblue] (16.7,4.4) circle (0.1);
\fill[dgreen] (12.5,4.7) circle (0.15);
\node[font=\large\bfseries, dorange] at (12.1,3.0) {porta vermelha};
\node[font=\large\bfseries, dblue] at (16.7,3.0) {porta azul};
\node[font=\large, text width=7.4cm, align=center] at (14.4,2.0) {\textbf{espaço} e \textbf{assinaturas} diferentes: sem confusão};
""")

# ------------------------------------------------------------ complexidade quadrática
w("complexidade-n", r"""
\draw[daxis, line width=1.2pt] (1.2,1.4) -- (14.2,1.4) node[right, font=\large] {$N$ marcos};
\draw[daxis, line width=1.2pt] (1.2,1.4) -- (1.2,8.2) node[above, font=\large] {tempo e memória};
\draw[dblue, line width=2.6pt, domain=0:6.4, samples=40] plot (\x+1.2, {1.4+0.16*\x*\x});
\draw[dred, dashed, line width=1.5pt] (7.0,1.4) -- (7.0,8.0);
\node[font=\large\bfseries, dred, anchor=east, text width=5.2cm, align=right] at (6.85,7.4) {$\approx$ 1.000 marcos:\\ limite prático do EKF SLAM};
\node[font=\large\bfseries, dblue] at (3.0,6.2) {$\propto N^2$};
\node[dbox, draw=dorange, fill=dorange!8, line width=1.6pt, text width=4.4cm, minimum height=2.2cm, font=\large] at (16.6,4.0) {mapas desejados: $10^6$ marcos ou mais};
""")

# ------------------------------------------------------------ o dilema do EKF SLAM
w("dilema-ekf", r"""
\tikzset{c/.style={dbox, text width=7.6cm, minimum height=3.6cm, font=\large, line width=1.7pt}}
\node[c, draw=dgreen] (a) at (4.2,5.2) {\textbf{\textcolor{dgreen}{Associação por máxima verossimilhança}}\\ funciona bem em mapas \textbf{densos}, com muitos marcos};
\node[c, draw=dred] (b) at (14.8,5.2) {\textbf{\textcolor{dred}{EKF}}\\ só aguenta mapas \textbf{esparsos}: o custo cresce com $N^2$};
\draw[dred, line width=2.4pt, {Stealth[length=3.4mm]}-{Stealth[length=3.4mm]}] (a.east) -- node[above, font=\Large\bfseries, dred] {dilema} (b.west);
\node[dbox, draw=dblue, fill=dblue!8, line width=1.7pt, text width=15.6cm, minimum height=1.8cm, font=\large] at (9.5,1.3) {\textbf{próximos capítulos}: algoritmos que aguentam \textbf{mapas bem maiores} e associação de dados \textbf{mais robusta}};
\draw[dblue, line width=1.8pt, -{Stealth[length=3mm]}] (9.5,3.2) -- (9.5,2.3);
""")

# ------------------------------------------------------------ correlação entre marcos ao longo do tempo
def _grade_corr(ox, nivel):
    o = []
    n = 6; s = 0.62
    for i in range(n):
        for j in range(n):
            if i == j: v = 85
            elif nivel == 0: v = 0
            elif nivel == 1: v = 40 if abs(i - j) == 1 else (18 if abs(i - j) == 2 else 0)
            else: v = 62
            o.append(r"\fill[black!%d] (%s,%s) rectangle (%s,%s);" % (v, round(ox + j * s, 2), round(5.0 - i * s - s, 2), round(ox + j * s + s, 2), round(5.0 - i * s, 2)))
    o.append(r"\draw[black!60, line width=1pt] (%s,%s) rectangle (%s,%s);" % (ox, round(5.0 - n * s, 2), round(ox + n * s, 2), 5.0))
    return "\n".join(o)
w("correlacao-mapa", "\n".join([
  _grade_corr(0.0, 0), _grade_corr(6.4, 1), _grade_corr(12.8, 2),
  r"\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (4.1,3.2) -- (6.1,3.2);",
  r"\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (10.5,3.2) -- (12.5,3.2);",
  r"\node[font=\large\bfseries, text width=4.2cm, align=center] at (1.86,0.0) {início: estimativas \textbf{independentes}};",
  r"\node[font=\large\bfseries, text width=4.2cm, align=center] at (8.26,0.0) {com o tempo: \textbf{vão se ligando}};",
  r"\node[font=\large\bfseries, text width=4.2cm, align=center] at (14.66,0.0) {no fim: \textbf{tudo correlacionado}};",
  r"\node[font=\large, black!70, text width=18cm, align=center] at (9.5,6.4) {cada quadradinho é a \textbf{correlação} entre duas variáveis (robô e marcos); quanto mais escuro, mais ligadas};",
]))

# ------------------------------------------------------------ as três hipóteses do EKF SLAM
w("tres-limitacoes", r"""
\tikzset{c/.style={draw=black!45, line width=1.4pt, rounded corners=6pt, fill=dcream}}
\draw[c] (0.2,0.2) rectangle (6.2,8.6); \draw[c] (6.6,0.2) rectangle (12.6,8.6); \draw[c] (13.0,0.2) rectangle (19.0,8.6);
\node[font=\Large\bfseries, dblue, text width=5.6cm, align=center] at (3.2,7.6) {1. Marcos pontuais};
\node[font=\Large\bfseries, dgreen, text width=5.6cm, align=center] at (9.6,7.6) {2. Ruído gaussiano};
\node[font=\Large\bfseries, dorange, text width=5.6cm, align=center] at (16.0,7.6) {3. Só positivas};
% 1: poucos pontos
\foreach \x/\y in {1.3/5.4,2.4/3.6,3.5/5.0,4.6/3.3,5.2/5.6,1.8/4.5,4.0/4.2} {
  \fill[dblue] (\x,\y) circle (0.14); \draw[dblue, line width=1.1pt] (\x,\y) circle (0.34);}
\node[font=\large, text width=5.4cm, align=center] at (3.2,1.9) {cada marco é um \textbf{ponto}\\ em geral, \textbf{menos de 1.000}};
% 2: gaussianas
\draw[black!40, line width=1pt] (7.0,3.3) -- (12.2,3.3);
\draw[dgreen, line width=2.4pt, domain=6.9:8.3, samples=40] plot (\x, {3.3+2.4*exp(-((\x-7.6)^2)/(2*0.09))});
\draw[dred, line width=2.4pt, domain=8.7:12.1, samples=40] plot (\x, {3.3+2.4*exp(-((\x-10.4)^2)/(2*0.6))});
\node[font=\large\bfseries, dgreen, text width=2.2cm, align=center] at (7.6,2.7) {incerteza\\ pequena};
\node[font=\large\bfseries, dred, text width=3cm, align=center] at (10.4,2.7) {incerteza\\ grande};
\node[font=\large, text width=5.4cm, align=center] at (9.6,1.5) {se for grande, a \textbf{linearização falha}};
% 3: só o que foi visto
\draw[dorange, fill=dorange!20, line width=1.5pt] (13.5,4.3) -- (14.5,4.55) -- (13.5,4.85) -- cycle;
\draw[black!45, dashed, line width=1.1pt] (14.5,4.55) -- (18.3,6.1); \draw[black!45, dashed, line width=1.1pt] (14.5,4.55) -- (18.3,3.0);
\fill[dgreen] (17.0,5.2) circle (0.17); \node[font=\large\bfseries, dgreen, anchor=north] at (17.0,4.95) {visto: usado};
\draw[black!55, dashed, line width=1.4pt, fill=white] (17.0,3.7) circle (0.17); \node[font=\large\bfseries, black!60, anchor=north, text width=4cm, align=center] at (16.0,3.35) {não visto: ignorado};
\node[font=\large, text width=5.4cm, align=center] at (16.0,1.5) {a \textbf{ausência} de um marco não entra no filtro};
""")

# ------------------------------------------------------------ ponto de partida: pose na origem, marcos desconhecidos
_o = []
_o.append(r"\node[font=\Large\bfseries, black!75] at (4.6,8.6) {o mundo no início};")
_o.append(r"\draw[daxis, line width=1.2pt] (1.0,2.0) -- (8.6,2.0); \draw[daxis, line width=1.2pt] (1.0,2.0) -- (1.0,7.8);")
_o.append(r"\draw[dorange, fill=dorange!25, line width=1.6pt] (0.7,1.7) -- (1.7,2.0) -- (0.7,2.3) -- cycle;")
_o.append(r"\node[font=\large\bfseries, dorange, anchor=west] at (1.1,1.0) {pose inicial = origem $(0,\,0,\,0)$};")
for x, y, r in [(4.2, 6.4, 1.1), (6.9, 4.6, 1.3), (3.6, 3.8, 0.95)]:
    _o.append(r"\draw[dred, dashed, fill=dred!6, line width=1.5pt] (%s,%s) circle (%s);" % (x, y, r))
    _o.append(r"\node[font=\Huge\bfseries, dred] at (%s,%s) {?};" % (x, y))
_o.append(r"\node[font=\large, dred, text width=4.2cm, align=center] at (6.9,7.4) {$N$ marcos: posição \textbf{desconhecida}};")
# matriz inicial
_s = 1.45; _ox = 11.6; _top = 7.3
_L = ["robô", "marco 1", "marco 2", "marco 3"]
_o.append(r"\node[font=\Large\bfseries, black!75] at (%s,8.6) {covariância inicial};" % round(_ox + 2 * _s, 2))
for i in range(4):
    _o.append(r"\node[font=\normalsize\bfseries, anchor=east] at (%s,%s) {%s};" % (round(_ox - 0.15, 2), round(_top - i * _s - _s / 2, 2), _L[i]))
    _o.append(r"\node[font=\footnotesize\bfseries] at (%s,%s) {%s};" % (round(_ox + i * _s + _s / 2, 2), round(_top + 0.35, 2), _L[i]))
    for j in range(4):
        zero = (i == 0 and j == 0)
        c = "dgreen" if zero else "dred"
        t = r"\textbf{0}" if zero else r"$\boldsymbol{\infty}$"
        _o.append(r"\draw[%s, fill=%s!%d, line width=1.3pt] (%s,%s) rectangle (%s,%s);" % (c, c, 18 if zero else 8, round(_ox + j * _s, 2), round(_top - i * _s, 2), round(_ox + j * _s + _s, 2), round(_top - i * _s - _s, 2)))
        _o.append(r"\node[font=\Large, text=%s] at (%s,%s) {%s};" % (c, round(_ox + j * _s + _s / 2, 2), round(_top - i * _s - _s / 2, 2), t))
_o.append(r"\node[font=\large, dgreen, text width=7.6cm, align=center] at (%s,0.95) {\textbf{0}: a pose é a origem, \textbf{sem incerteza}};" % round(_ox + 2 * _s, 2))
_o.append(r"\node[font=\large, dred, text width=7.6cm, align=center] at (%s,0.2) {$\boldsymbol{\infty}$: posição dos $N$ marcos \textbf{desconhecida}};" % round(_ox + 2 * _s, 2))
w("ponto-de-partida", "\n".join(_o))

# ------------------------------------------------------------ passos do algoritmo (inclui a inicialização)
w("passos-ekf-slam", r"""
\tikzset{c/.style={dbox, text width=3.7cm, minimum height=4.0cm, font=\large, line width=1.7pt},
        a/.style={dtrans, line width=2pt, -{Stealth[length=3.2mm]}}}
\node[c, draw=dblue, fill=dblue!8] (p0) at (2.5,4.3) {\textbf{\textcolor{dblue}{Passo 0}}\\ \textbf{Ponto de partida}\\[4pt] pose na origem\\ marcos com incerteza $\infty$};
\node[font=\large\bfseries, dblue] at (2.5,1.6) {uma única vez};
\draw[dorange, dashed, line width=1.6pt, rounded corners=10pt] (5.0,1.3) rectangle (19.0,7.9);
\node[font=\large\bfseries, dorange, fill=dcream, inner sep=3pt] at (12.0,7.9) {a cada passo de tempo (repete)};
\node[c, draw=dblue] (p1) at (7.2,4.3) {\textbf{\textcolor{dblue}{Passo 1}}\\ \textbf{Mover}\\[4pt] prevê a pose\\ a incerteza da pose \textbf{cresce}};
\node[c, draw=dgreen] (p2) at (12.0,4.3) {\textbf{\textcolor{dgreen}{Passo 2}}\\ \textbf{Observar}\\[4pt] compara o \textbf{esperado} com o \textbf{medido}; marco novo: inicia na medida};
\node[c, draw=dorange] (p3) at (16.8,4.3) {\textbf{\textcolor{dorange}{Passo 3}}\\ \textbf{Corrigir}\\[4pt] atualiza a \textbf{pose} e o \textbf{mapa inteiro}};
\draw[a] (p0.east) -- (p1.west);
\draw[a] (p1.east) -- (p2.west);
\draw[a] (p2.east) -- (p3.west);
\draw[black!55, line width=1.5pt, -{Stealth[length=3mm]}, rounded corners=8pt] (p3.south) -- ++(0,-1.0) -| (p1.south);
""")

# ------------------------------------------------------------ passo 1: mover (só a pose muda)
_o = []
_o.append(r"\node[font=\Large\bfseries, black!75] at (4.4,8.4) {no mapa};")
_o.append(r"\draw[dorange, fill=dorange!15, line width=1.5pt] (1.6,3.0) ellipse (0.35 and 0.28); \fill[dorange] (1.6,3.0) circle (0.09);")
_o.append(r"\draw[dorange, dotted, line width=1.8pt, -{Stealth[length=3mm]}] (2.1,3.0) -- (5.0,3.0);")
_o.append(r"\node[font=\large\bfseries, dorange] at (3.3,2.4) {controle $u$};")
_o.append(r"\draw[dorange, fill=dorange!15, line width=1.5pt] (6.1,3.0) ellipse (1.0 and 0.65); \fill[dorange] (6.1,3.0) circle (0.09);")
_o.append(r"\node[font=\large\bfseries, dorange, text width=4cm, align=center] at (6.1,1.6) {a incerteza da pose \textbf{cresce}};")
for x, y in [(2.2, 6.0), (6.8, 6.2)]:
    _o.append(r"\draw[dblue, fill=dblue!12, line width=1.4pt] (%s,%s) ellipse (0.55 and 0.45); \fill[dblue] (%s,%s) circle (0.08);" % (x, y, x, y))
_o.append(r"\node[font=\large\bfseries, dblue, text width=5cm, align=center] at (4.5,7.0) {marcos: \textbf{parados}};")
# vetor de estado
_o.append(r"\node[font=\Large\bfseries, black!75] at (14.6,8.4) {no estado e na covariância};")
for i in range(9):
    pose = i < 3
    _o.append(r"\draw[%s, fill=%s!%d, line width=1.2pt] (%s,6.6) rectangle (%s,7.5);" % ("dorange" if pose else "black!45", "dorange" if pose else "black", 18 if pose else 8, round(10.2 + i * 0.9, 2), round(11.1 + i * 0.9, 2)))
_o.append(r"\node[font=\large\bfseries, dorange, text width=3cm, align=center] at (11.55,6.0) {robô: \textbf{muda}};")
_o.append(r"\node[font=\large\bfseries, black!65, text width=5cm, align=center] at (16.3,6.0) {marcos: \textbf{iguais}};")
_s = 1.3
for i in range(3):
    for j in range(3):
        ch = (i == 0 and j == 0)
        _o.append(r"\draw[%s, fill=%s!%d, line width=1.3pt] (%s,%s) rectangle (%s,%s);" % ("dorange" if ch else "black!45", "dorange" if ch else "black", 22 if ch else 8, round(11.6 + j * _s, 2), round(4.6 - i * _s, 2), round(11.6 + j * _s + _s, 2), round(4.6 - i * _s - _s, 2)))
_o.append(r"\node[font=\normalsize\bfseries, dorange] at (12.25,3.95) {muda};")
_o.append(r"\node[font=\large, black!65, anchor=west, text width=3cm] at (15.7,3.0) {o resto: \textbf{não muda}};")
_o.append(r"\node[font=\large, text width=4.6cm, align=right, anchor=east] at (11.3,3.3) {covariância};")
w("passo-mover", "\n".join(_o))

# ------------------------------------------------------------ passo 2: observar (esperado x medido)
w("passo-observar", r"""
\draw[dorange, fill=dorange!20, line width=1.6pt] (1.5,1.6) -- (2.6,1.9) -- (1.5,2.3) -- cycle;
\node[font=\large\bfseries, dorange] at (1.6,0.9) {robô};
\draw[dorange, dashed, line width=2pt, -{Stealth[length=3.2mm]}] (2.6,1.95) -- (6.6,5.2);
\draw[dblue, fill=dblue!10, line width=1.4pt] (7.0,5.5) ellipse (0.8 and 0.6); \fill[dorange] (7.0,5.5) circle (0.13);
\node[font=\large\bfseries, dorange, anchor=east, text width=3cm, align=right] at (4.3,4.6) {esperado};
\draw[black, line width=2.2pt, -{Stealth[length=3.4mm]}] (2.6,1.85) -- (7.7,4.35);
\fill[black] (7.9,4.45) circle (0.14);
\node[font=\large\bfseries, black, anchor=west] at (8.1,4.1) {medido};
\draw[dred, line width=2.4pt, -{Stealth[length=3mm]}] (7.25,5.2) -- (7.8,4.65);
\node[font=\large\bfseries, dred, anchor=west] at (8.4,5.3) {diferença};
\node[font=\large\bfseries, dblue] at (7.0,6.5) {marco no mapa};
\tikzset{b/.style={dbox, text width=7.4cm, minimum height=1.9cm, font=\large, line width=1.6pt, anchor=west}}
\node[b, draw=black] at (11.3,6.7) {\textbf{Medição}\\ alcance, ângulo e assinatura de um marco};
\node[b, draw=dorange] at (11.3,4.2) {\textbf{\textcolor{dorange}{Esperado}}\\ calculado a partir do estado atual};
\node[b, draw=dred] at (11.3,1.7) {\textbf{\textcolor{dred}{Diferença}}\\ é a correção a ser aplicada};
""")

# ------------------------------------------------------------ passo 3: corrigir (antes e depois)
def _cen(ox, antes):
    o = []
    R = (1.8, 2.6); M = [(3.2, 5.8), (5.4, 3.4), (6.4, 6.0)]
    rr = (0.8, 0.58) if antes else (0.3, 0.22)
    mm = [(0.75, 0.6), (0.7, 0.55), (0.8, 0.62)] if antes else [(0.4, 0.3), (0.45, 0.35), (0.5, 0.4)]
    o.append(r"\draw[black!35, line width=1pt, rounded corners=6pt] (%s,0.9) rectangle (%s,7.6);" % (ox, ox + 7.7))
    o.append(r"\node[font=\Large\bfseries, black!75] at (%s,8.2) {%s};" % (ox + 3.85, "antes" if antes else "depois"))
    for (x, y), (a, b) in zip(M, mm):
        o.append(r"\draw[dblue, fill=dblue!12, line width=1.4pt] (%s,%s) ellipse (%s and %s); \fill[dblue] (%s,%s) circle (0.08);" % (ox + x, y, a, b, ox + x, y))
    o.append(r"\draw[dorange, fill=dorange!20, line width=1.5pt] (%s,%s) ellipse (%s and %s); \fill[dorange] (%s,%s) circle (0.09);" % (ox + R[0], R[1], rr[0], rr[1], ox + R[0], R[1]))
    return "\n".join(o)
w("passo-corrigir", "\n".join([
  _cen(0.0, True), _cen(11.6, False),
  r"\draw[dgreen, line width=2.2pt, -{Stealth[length=3.2mm]}] (2.5,3.0) -- (3.0,5.1);",
  r"\node[font=\large\bfseries, dgreen, anchor=west, text width=2.6cm] at (3.6,4.5) {observa \textbf{um} marco};",
  r"\node[font=\large\bfseries, dorange, anchor=north] at (1.8,1.8) {robô};",
  r"\node[font=\large\bfseries, dblue, anchor=north, text width=3cm, align=center] at (5.4,2.55) {outros marcos};",
  r"\node[font=\large\bfseries, dorange, text width=2.4cm, align=center] at (13.4,1.5) {melhora \textbf{muito}};",
  r"\node[font=\large\bfseries, dblue, text width=4.2cm, align=center] at (16.0,4.9) {\textbf{todos} melhoram};",
  r"\node[font=\large\bfseries, text width=3.2cm, align=center] at (9.65,7.4) {ganho de Kalman};",
  r"\draw[dtrans, line width=2.2pt, -{Stealth[length=3.4mm]}] (7.9,4.3) -- (8.7,4.3);",
  r"\draw[dtrans, line width=2.2pt, -{Stealth[length=3.4mm]}] (10.6,4.3) -- (11.4,4.3);",
] + [r"\draw[dred, fill=dred!%d, line width=1pt] (%s,%s) rectangle (%s,%s);" % (22 if i == j else 12, round(8.75 + j * 0.45, 2), round(5.9 - i * 0.45, 2), round(9.2 + j * 0.45, 2), round(5.45 - i * 0.45, 2)) for i in range(4) for j in range(4)] + [
  r"\node[font=\large, dred, text width=3.4cm, align=center] at (9.65,3.0) {matriz \textbf{cheia}: a correção chega a tudo};",
]))

# ------------------------------------------------------------ os quatro limites do EKF SLAM
import random as _rd
_rd.seed(5)
_o = []
_cards = [(0.0, 4.6, 9.3, 9.0), (9.7, 4.6, 19.0, 9.0), (0.0, 0.0, 9.3, 4.4), (9.7, 0.0, 19.0, 4.4)]
_tit = ["1. Descarta quase todos os dados", "2. Custo quadrático", "3. Associação sem volta", "4. Só serve ao SLAM online"]
_cor = ["dblue", "dgreen", "dred", "dorange"]
for (x0, y0, x1, y1), t, c in zip(_cards, _tit, _cor):
    _o.append(r"\draw[black!40, line width=1.3pt, rounded corners=6pt, fill=dcream] (%s,%s) rectangle (%s,%s);" % (x0, y0, x1, y1))
    _o.append(r"\node[font=\large\bfseries, text=%s] at (%s,%s) {%s};" % (c, round((x0 + x1) / 2, 2), round(y1 - 0.45, 2), t))
# 1: muitos pontos, poucos marcos
for k in range(34):
    px, py = _rd.uniform(0.6, 5.2), _rd.uniform(5.3, 7.7)
    if k < 3: continue
    _o.append(r"\fill[black!35] (%s,%s) circle (0.08);" % (round(px, 2), round(py, 2)))
for px, py in [(1.2, 6.9), (3.0, 5.7), (4.7, 7.2)]:
    _o.append(r"\fill[dblue] (%s,%s) circle (0.13); \draw[dblue, line width=1.5pt] (%s,%s) circle (0.36);" % (px, py, px, py))
_o.append(r"\node[font=\large, text width=3.3cm, align=left, anchor=west] at (5.7,6.5) {\textbf{3 marcos} escolhidos; o \textbf{resto} dos pontos é descartado};")
# 2: quadrados crescendo
_x = 10.4
for lado, lab, custo in [(0.6, "$N$", "1$\\times$"), (1.2, "$2N$", "4$\\times$"), (1.8, "$3N$", "9$\\times$")]:
    _o.append(r"\draw[dgreen, fill=dgreen!15, line width=1.4pt] (%s,5.4) rectangle (%s,%s);" % (_x, round(_x + lado, 2), round(5.4 + lado, 2)))
    _o.append(r"\node[font=\large\bfseries, dgreen] at (%s,%s) {%s};" % (round(_x + lado / 2, 2), round(5.4 + lado + 0.35, 2), custo))
    _o.append(r"\node[font=\normalsize] at (%s,5.1) {%s marcos};" % (round(_x + lado / 2, 2), lab))
    _x += lado + 0.9
_o.append(r"\node[font=\large, text width=2.8cm, align=left, anchor=west] at (16.15,6.3) {\textbf{dobrar} os marcos: \textbf{4$\times$} o custo};")
# 3: linha do tempo com erro
for i, (ok, tx) in enumerate([(True, "t1"), (True, "t2"), (False, "t3"), (True, "t4")]):
    xx = 1.3 + i * 2.1
    _o.append(r"\node[circle, draw=%s, fill=%s!15, line width=1.5pt, minimum size=0.95cm, font=\large\bfseries] (q%d) at (%s,2.5) {%s};" % ("dgreen" if ok else "dred", "dgreen" if ok else "dred", i, xx, tx))
for i in range(3):
    _o.append(r"\draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (q%d.east) -- (q%d.west);" % (i, i + 1))
_o.append(r"\node[font=\normalsize\bfseries, dred] at (5.5,3.35) {errada};")
_o.append(r"\draw[dred, dashed, line width=1.5pt, -{Stealth[length=2.6mm]}] (q3.south) to[bend left=35] node[below, font=\normalsize\bfseries, dred] {não volta atrás} (q2.south);")
_o.append(r"\node[font=\large, text width=7.6cm, align=center] at (4.65,0.45) {o \textbf{erro fica} no mapa};")
# 4: online fixo x completo cresce
_o.append(r"\node[font=\large\bfseries, dorange] at (12.0,3.4) {online: fixo};")
_o.append(r"\node[font=\large\bfseries, dred] at (16.6,3.4) {completo: cresce};")
for k, (a, b) in enumerate([(1.8, 1.8), (1.8, 2.7), (1.8, 3.6)]):
    yy = 2.65 - k * 0.62
    _o.append(r"\draw[dorange, fill=dorange!18, line width=1.2pt] (10.8,%s) rectangle (%s,%s);" % (round(yy - 0.2, 2), round(10.8 + a, 2), round(yy + 0.2, 2)))
    _o.append(r"\draw[dred, fill=dred!12, line width=1.2pt] (14.6,%s) rectangle (%s,%s);" % (round(yy - 0.2, 2), round(14.6 + b, 2), round(yy + 0.2, 2)))
_o.append(r"\node[font=\large, text width=8.4cm, align=center] at (14.35,0.45) {a cada pose nova, estado e covariância \textbf{crescem sem limite}};")
w("limites-ekf", "\n".join(_o))
