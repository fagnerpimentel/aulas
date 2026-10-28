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
        o.append(r"\node[font=\Large, black!70, text width=%scm, align=center] at (%s,%s) {%s};" % (capw, round((used - 1) * st / 2, 2), round(-(rows - 1) * (h + 0.5) - h / 2 - 1.0, 2), cap))
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
        o.append(r"\node[font=\Large, black!70, text width=%scm, align=center] at (%s,%s) {%s};" % (capw, round((len(items) - 1) * (st + 0.2) / 2, 2), round(-h / 2 - 1.0, 2), cap))
    return "\n".join(o)
import math, random

# ---------- utilidades de grade ----------
def planta(W=20, H=12):
    m = [['?'] * W for _ in range(H)]
    for y in range(2, 10):
        for x in range(2, 18):
            m[y][x] = '.'
    for x in range(2, 18):
        m[2][x] = '#'; m[9][x] = '#'
    for y in range(2, 10):
        m[y][2] = '#'; m[y][17] = '#'
        m[y][9] = '#'
    m[5][9] = '.'; m[6][9] = '.'
    for (x, y) in [(5, 4), (5, 5), (13, 7), (14, 7), (14, 4)]:
        m[y][x] = '#'
    return m

def grade(m, ox, oy, s=0.42, cores=None):
    cores = cores or {'#': 'black!85', '.': 'white', '?': 'black!18'}
    H = len(m); out = []
    for y, row in enumerate(m):
        for x, c in enumerate(row):
            out.append(r"\fill[%s] (%s,%s) rectangle +(%s,%s);" % (cores[c], round(ox + x * s, 3), round(oy + (H - 1 - y) * s, 3), s, s))
    W = len(m[0])
    out.append(r"\draw[black!35, line width=0.3pt] (%s,%s) grid[step=%s] (%s,%s);" % (ox, oy, s, round(ox + W * s, 3), round(oy + H * s, 3)))
    out.append(r"\draw[dblue, line width=1.4pt] (%s,%s) rectangle (%s,%s);" % (ox, oy, round(ox + W * s, 3), round(oy + H * s, 3)))
    return "\n  ".join(out)

# ---------- figuras ----------
w("dificuldades-mapeamento", boxes([("Tamanho", "ambiente grande em relação ao alcance dos sensores"), ("Ruído", "sensores e atuadores imperfeitos"), ("Ambiguidade", "lugares diferentes que parecem iguais"), ("Ciclos", "voltar por outro caminho acumula erro de odometria")], h=3.2, cap="quanto maior cada fator, mais difícil é aprender o mapa"))

w("galinha-e-ovo", r"""
  \node[dstate, minimum size=3.0cm, font=\Large] (p) at (0,0) {pose $x_t$};
  \node[dstate, minimum size=3.0cm, font=\Large] (m) at (9,0) {mapa $m$};
  \draw[dtrans, line width=2pt, -{Stealth[length=3.4mm]}, bend left=28] (p) to node[above, font=\large, text width=5cm, align=center] {para mapear preciso da pose} (m);
  \draw[dmeas, line width=2pt, -{Stealth[length=3.4mm]}, bend left=28] (m) to node[below, font=\large, text width=5.4cm, align=center] {para me localizar preciso do mapa} (p);
  \node[font=\Large, black!70] at (4.5,-3.1) {é o problema \textbf{SLAM}; nesta aula a pose é conhecida};
""")

w("ciclo-odometria", r"""
  \draw[dgreen, line width=2.4pt] (0,0) -- (6,0) -- (6,4) -- (0,4) -- cycle;
  \node[font=\large, dgreen] at (3.0,5.2) {caminho verdadeiro (sólido)};
  \draw[dred, dashed, line width=2.4pt] (0,0) -- (6,0) -- (6.5,3.8) -- (0.7,4.5) -- (1.5,0.9);
  \node[font=\large, dred] at (3.4,-0.7) {estimado pela odometria (tracejado)};
  \draw[dorange, <->, line width=1.8pt] (1.5,0.9) -- (0.08,0.08);
  \node[font=\large\bfseries, dorange, anchor=west] at (7.2,2.4) {erro ao fechar o ciclo};
  \draw[dorange, line width=1.2pt] (7.1,2.3) -- (4.0,1.5) -- (0.85,0.55);
""")

w("grade-celulas", r"""
  \tikzset{c0/.style={fill=white, draw=black!60, line width=0.8pt}, c1/.style={fill=black!85, draw=black!60, line width=0.8pt}, cx/.style={fill=black!18, draw=black!60, line width=0.8pt}}
  \foreach \x in {0,...,7} {\foreach \y in {0,...,4} {\draw[cx] (\x*1.1,\y*1.1) rectangle +(1.1,1.1);}}
  \foreach \x/\y in {1/4, 2/4, 3/4, 4/4, 5/4, 6/4, 1/0, 2/0, 3/0, 4/0, 5/0, 6/0, 1/1, 1/2, 1/3, 6/1, 6/2, 6/3} {\draw[c1] (\x*1.1,\y*1.1) rectangle +(1.1,1.1);}
  \foreach \x/\y in {2/1, 3/1, 4/1, 5/1, 2/2, 3/2, 4/2, 5/2, 2/3, 3/3, 4/3, 5/3} {\draw[c0] (\x*1.1,\y*1.1) rectangle +(1.1,1.1);}
  \node[font=\Large] at (3.85,2.75) {livre};
  \node[font=\large, white, rotate=90] at (1.65,2.75) {$m_i=1$};
  \node[font=\large, white, rotate=90] at (7.15,2.2) {ocupada};
""")

w("sigmoide-logodds", r"""
  \draw[daxis, line width=1.2pt] (-7,0) -- (7.4,0) node[right, font=\large] {$l$};
  \draw[daxis, line width=1.2pt] (0,-0.3) -- (0,5.0) node[above, font=\large] {$p$};
  \draw[dblue, line width=2.6pt, domain=-6.5:6.5, samples=80, smooth, variable=\x] plot ({\x},{4.4/(1+exp(-\x))});
  \draw[dguide] (-7,4.4) -- (7,4.4); \node[font=\large, anchor=east] at (-7.1,4.4) {1};
  \draw[dguide] (-7,2.2) -- (0,2.2); \node[font=\large, anchor=east] at (-7.1,2.2) {0,5};
  \node[font=\large, anchor=east] at (-7.1,0) {0};
  \fill[dorange] (0,2.2) circle (0.16); \node[font=\large, dorange, anchor=west] at (0.3,1.7) {$l_0=0$ (prior 0,5)};
  \node[font=\large, dgreen, anchor=north] at (5.4,3.6) {$l\to+\infty$: ocupada};
  \node[font=\large, dred, anchor=south] at (-5.2,1.0) {$l\to-\infty$: livre};
""")

w("cone-sensor", r"""
  \def\bw{16}
  \fill[dgreen!18] (0,0) -- (-\bw:5.6) arc(-\bw:\bw:5.6) -- cycle;
  \fill[dred!55] (-\bw:5.6) arc(-\bw:\bw:5.6) -- (\bw:6.6) arc(\bw:-\bw:6.6) -- cycle;
  \fill[black!15] (-\bw:6.6) arc(-\bw:\bw:6.6) -- (\bw:9.0) arc(\bw:-\bw:9.0) -- cycle;
  \draw[black!70, line width=1.2pt] (0,0) -- (-\bw:9.0) arc(-\bw:\bw:9.0) -- cycle;
  \draw[black!55, dashed, line width=0.8pt] (-\bw:5.6) arc(-\bw:\bw:5.6);
  \draw[black!55, dashed, line width=0.8pt] (-\bw:6.6) arc(-\bw:\bw:6.6);
  \fill[dblue] (0,0) circle (0.18); \node[font=\large, anchor=east] at (-0.3,0) {robô};
  \node[font=\large, dgreen] at (3.9,0) {\textbf{livre} ($l_{free}$)};
  \node[font=\large, white] at (6.1,0) {\bf occ.};
  \node[font=\large, black!70] at (7.9,0) {\textbf{?} ($l_0$)};
  \draw[<->, line width=1.2pt] (5.6,-3.2) -- (6.6,-3.2); \node[font=\large] at (6.1,-3.8) {$\alpha$ (espessura)};
  \draw[line width=1.2pt] (-\bw:1.8) arc(-\bw:\bw:1.8);
  \node[font=\large] at (2.15,0) {$\beta$};
  \draw[-{Stealth}, line width=1pt] (6.1,3.6) node[above, font=\large] {leitura $z_t^k$} -- (6.1,2.1);
""")

w("celula-no-tempo", r"""
  \pgfmathsetmacro{\lo}{0.85}\pgfmathsetmacro{\lf}{-0.4}
  \draw[daxis, line width=1.2pt] (0,0) -- (13.4,0); \draw[daxis, line width=1.2pt] (0,0) -- (0,5.2) node[above, font=\large] {$p(m_i)$};
  \draw[dguide] (0,2.5) -- (13.0,2.5); \node[font=\large, anchor=east] at (-0.2,2.5) {0,5}; \node[font=\large, anchor=east] at (-0.2,5.0) {1}; \node[font=\large, anchor=east] at (-0.2,0) {0};
  \fill[dred!70] (1.0,0) rectangle (2.1,3.503);
  \node[font=\large\bfseries] at (1.55,3.853) {0.70};
  \node[font=\large, dred] at (1.55,-0.5) {ocup.};
  \fill[dred!70] (2.55,0) rectangle (3.65,4.228);
  \node[font=\large\bfseries] at (3.1,4.578) {0.85};
  \node[font=\large, dred] at (3.1,-0.5) {ocup.};
  \fill[dgreen!70] (4.1,0) rectangle (5.2,3.929);
  \node[font=\large\bfseries] at (4.65,4.279) {0.79};
  \node[font=\large, dgreen] at (4.65,-0.5) {livre};
  \fill[dred!70] (5.65,0) rectangle (6.75,4.478);
  \node[font=\large\bfseries] at (6.2,4.828) {0.90};
  \node[font=\large, dred] at (6.2,-0.5) {ocup.};
  \fill[dred!70] (7.2,0) rectangle (8.3,4.763);
  \node[font=\large\bfseries] at (7.75,5.113) {0.95};
  \node[font=\large, dred] at (7.75,-0.5) {ocup.};
  \fill[dred!70] (8.75,0) rectangle (9.85,4.896);
  \node[font=\large\bfseries] at (9.3,5.246) {0.98};
  \node[font=\large, dred] at (9.3,-0.5) {ocup.};
  \fill[dgreen!70] (10.3,0) rectangle (11.4,4.846);
  \node[font=\large\bfseries] at (10.85,5.196) {0.97};
  \node[font=\large, dgreen] at (10.85,-0.5) {livre};
  \fill[dred!70] (11.85,0) rectangle (12.95,4.933);
  \node[font=\large\bfseries] at (12.4,5.283) {0.99};
  \node[font=\large, dred] at (12.4,-0.5) {ocup.};
  \node[font=\Large, black!70, text width=13cm, align=center] at (6.5,-1.9) {a célula converge para \textbf{perto de 1} com poucas leituras (sequência fictícia)};
""".replace("PYEOF_BARS", ""))

# ---------- mapas ----------
M = planta()
w("mapa-exemplo", r"""
  %s
  \node[font=\Large\bfseries, dblue] at (4.2,5.6) {mapa de ocupação};
  \node[font=\large, black!70, anchor=west, text width=6.4cm] at (9.0,3.9) {preto: ocupado\\ branco: livre\\ cinza: prior (ainda sem informação)};
  \node[font=\large, black!70, anchor=west, text width=6.4cm] at (9.0,1.6) {as células tendem a \textbf{convergir} para perto de 0 ou de 1};
""" % grade(M, 0, 0, 0.42))

random.seed(7)
pts = []
def seg(x0, y0, x1, y1, n):
    for i in range(n):
        t = i / (n - 1)
        pts.append((x0 + (x1 - x0) * t + random.uniform(-0.05, 0.05), y0 + (y1 - y0) * t + random.uniform(-0.05, 0.05)))
seg(0.0, 0.0, 6.4, 0.0, 28); seg(0.0, 3.2, 6.4, 3.2, 28); seg(0.0, 0.0, 0.0, 3.2, 14); seg(6.4, 0.0, 6.4, 3.2, 14)
seg(3.2, 0.0, 3.2, 1.0, 5); seg(3.2, 2.0, 3.2, 3.2, 5)
ppl = [(1.6, 1.4), (1.8, 1.6), (4.6, 2.2), (4.8, 1.0), (5.0, 1.2), (2.4, 2.4)]
dots = "\n  ".join(r"\fill[black] (%s,%s) circle (0.045);" % (round(x, 3), round(y, 3)) for x, y in pts)
pdots = "\n  ".join(r"\fill[dred] (%s,%s) circle (0.06);" % (x, y) for x, y in ppl)
Mmini = [['.' for _ in range(16)] for _ in range(8)]
for x in range(16):
    Mmini[0][x] = '#'; Mmini[7][x] = '#'
for y in range(8):
    Mmini[y][0] = '#'; Mmini[y][15] = '#'
for y in range(8):
    if y not in (3, 4): Mmini[y][8] = '#'
w("pontos-vs-grade", r"""
  \node[font=\Large\bfseries, dblue] at (3.2,4.1) {pontos brutos do laser};
  \draw[dblue, line width=1.2pt] (-0.3,-0.3) rectangle (6.7,3.5);
  %s
  %s
  \node[font=\large, dred] at (3.2,-0.8) {pontos vermelhos: pessoas};
  \draw[dtrans, line width=2.4pt, -{Stealth[length=3.4mm]}] (7.2,1.6) -- (8.6,1.6);
  \node[font=\Large\bfseries, dblue] at (13.0,4.1) {mapa de ocupação};
  %s
  \node[font=\large, dgreen] at (13.0,-0.8) {as pessoas \textbf{somem}: o espaço livre vence};
""" % (dots, pdots, grade(Mmini, 9.8, -0.2, 0.4, {'#': 'black!85', '.': 'white', '?': 'black!18'})))

def minimapa(pontos, n=7):
    mm = [['.' for _ in range(n)] for _ in range(n)]
    for (x, y) in pontos: mm[y][x] = '#'
    return mm
A = minimapa([(1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (5, 5), (5, 4)])
B = minimapa([(5, 5), (5, 4), (4, 2), (5, 2), (3, 5), (2, 5)])
C = [[('#' if (A[y][x] == '#' or B[y][x] == '#') else '.') for x in range(7)] for y in range(7)]
w("fusao-sensores", r"""
  \node[font=\Large\bfseries, dblue] at (1.5,3.7) {mapa do sonar};
  %s
  \node[font=\Huge] at (3.5,1.5) {$\&$};
  \node[font=\Large\bfseries, dorange] at (6.4,3.7) {mapa do laser};
  %s
  \draw[dtrans, line width=2.4pt, -{Stealth[length=3.4mm]}] (9.0,1.5) -- (10.3,1.5);
  \node[font=\large, black!70] at (9.65,2.0) {max};
  \node[font=\Large\bfseries, dgreen] at (13.0,3.7) {mapa combinado};
  %s
  \node[font=\Large, black!70, text width=17cm, align=center] at (7.0,-0.9) {o mapa mais \textbf{pessimista}: se qualquer sensor vê ocupado, fica ocupado};
""" % (grade(A, 0, 0, 0.43), grade(B, 4.9, 0, 0.43), grade(C, 11.5, 0, 0.43)))

# ---------- modelos inversos ----------
w("direto-vs-inverso", r"""
  \tikzset{b/.style={dbox, minimum width=3.4cm, minimum height=1.7cm, font=\large, line width=1.5pt}}
  \node[font=\Large\bfseries, dblue, anchor=west] at (0,5.4) {modelo de medição (direto): causa $\to$ efeito};
  \node[b, draw=dblue] (a) at (1.8,3.9) {mapa $m$\\ pose $x$};
  \node[b, draw=dgreen] (b) at (8.4,3.9) {medição $z$};
  \draw[dtrans, line width=2pt, -{Stealth[length=3mm]}] (a) -- node[above, font=\large] {$p(z\mid x,m)$} (b);
  \node[font=\Large\bfseries, dorange, anchor=west] at (0,1.9) {modelo inverso: efeito $\to$ causa};
  \node[b, draw=dgreen] (c) at (1.8,0.4) {medição $z$\\ pose $x$};
  \node[b, draw=dorange] (d) at (8.4,0.4) {ocupação $m_i$};
  \draw[dmeas, line width=2pt, -{Stealth[length=3mm]}] (c) -- node[above, font=\large] {$p(m_i\mid x,z)$} (d);
""")

w("amostragem-modelo", flow([("Mapa", "sorteie $m^{[k]}\\sim p(m)$"), ("Pose", "sorteie $x_t^{[k]}$ no mapa"), ("Medição", "simule $z_t^{[k]}\\sim p(z\\mid x,m)$"), ("Rótulo", "leia $m_i$ no mapa verdadeiro")], w=4.1, h=3.2, cap="repita muitas vezes: cada amostra vira um par entrada $\\to$ ocupação", capw=16))

w("invariancias", boxes([("Só o que está no alcance", "células fora do cone não dependem da leitura"), ("Coordenadas relativas", "só importa a posição da célula em relação ao robô"), ("Células vizinhas", "interpretação parecida: uma função para todas"), ("Sensores iguais", "o mesmo modelo vale para cada feixe")], h=3.4, cap="essas invariâncias reduzem muito o conjunto de treinamento"))

# ---------- MAP ----------
w("arco-vs-ponto", r"""
  \def\bw{14}
  \begin{scope}
    \fill[dgreen!18] (0,0) -- (-\bw:5.0) arc(-\bw:\bw:5.0) -- cycle;
    \fill[dred!55] (-\bw:5.0) arc(-\bw:\bw:5.0) -- (\bw:5.9) arc(\bw:-\bw:5.9) -- cycle;
    \draw[black!70, line width=1.2pt] (0,0) -- (-\bw:5.9) arc(-\bw:\bw:5.9) -- cycle;
    \fill[dblue] (0,0) circle (0.16);
    \node[font=\Large\bfseries, dred] at (3.0,-3.0) {modelo inverso por célula};
    \node[font=\large, text width=6.6cm, align=center] at (3.0,-3.9) {marca o \textbf{arco inteiro} como ocupado};
  \end{scope}
  \begin{scope}[shift={(9.4,0)}]
    \fill[dgreen!18] (0,0) -- (-\bw:5.0) arc(-\bw:\bw:5.0) -- cycle;
    \draw[black!70, line width=1.2pt] (0,0) -- (-\bw:5.9) arc(-\bw:\bw:5.9) -- cycle;
    \fill[black!85] (5.35,0.45) rectangle +(0.45,0.45);
    \fill[dblue] (0,0) circle (0.16);
    \node[font=\Large\bfseries, dgreen] at (3.0,-3.0) {mapa MAP};
    \node[font=\large, text width=6.6cm, align=center] at (3.0,-3.9) {\textbf{um} obstáculo no cone já explica a leitura};
  \end{scope}
""")

w("porta-aberta", r"""
  \tikzset{wall/.style={line width=3pt, black!85}}
  \foreach \ox/\tt in {0/{leituras}, 7.2/{mapa padrão}, 14.4/{mapa MAP}} {
    \node[font=\Large\bfseries, dblue] at (\ox+3.0,5.3) {\tt};
    \draw[dblue, line width=1pt] (\ox-0.3,-0.9) rectangle (\ox+6.3,4.7);
  }
  % leituras
  \draw[wall] (0,3.2) -- (2.4,3.2); \draw[wall] (3.6,3.2) -- (6,3.2);
  \draw[wall] (2.4,3.2) -- (2.4,3.6); \draw[wall] (3.6,3.2) -- (3.6,3.6);
  \foreach \x in {0.5,1.1,1.7,4.3,4.9,5.5} {\fill[dblue] (\x,0) circle (0.07); \draw[dblue!70, line width=0.8pt] (\x,0) -- (\x,3.1);}
  \foreach \x in {2.65,3.0,3.35} {\fill[dblue] (\x,0) circle (0.07); \draw[dblue!70, line width=0.8pt] (\x,0) -- (\x,4.4); \fill[dorange] (\x,4.4) circle (0.06);}
  \node[font=\large, black!70] at (3.0,-0.5) {robô passa pela porta};
  % mapa padrao: porta fechada
  \draw[wall] (7.2,3.2) -- (13.2,3.2);
  \draw[black!30, dashed, line width=1pt] (9.6,3.2) -- (10.8,3.2);
  \node[font=\large, dred] at (10.2,-0.5) {a abertura \textbf{não} aparece};
  % MAP: porta aberta
  \draw[wall] (14.4,3.2) -- (16.8,3.2); \draw[wall] (18.0,3.2) -- (20.4,3.2);
  \draw[wall] (16.8,3.2) -- (16.8,3.6); \draw[wall] (18.0,3.2) -- (18.0,3.6);
  \node[font=\large, dgreen] at (17.4,-0.5) {a porta aparece};
""")

w("hill-climbing", flow([("Começa", "mapa todo \\textbf{livre}"), ("Testa", "inverta o valor de uma célula $m_i$"), ("Decide", "mantenha se a verossimilhança \\textbf{aumenta}"), ("Repete", "para todas as células até convergir")], w=4.1, h=3.4, cap="escalada de colina: acha um máximo \\textbf{local}", capw=16))

w("limites-map", boxes([("Sem incerteza", "devolve só a moda do posterior"), ("Em lote", "precisa de todos os dados na memória"), ("Máximo local", "na prática há poucos, ou nenhum"), ("Acelerar", "comece pelo mapa padrão e atualize só as medições afetadas")], h=3.4, cap="sensibilidade por célula aproxima a incerteza, mas é otimista demais"))

# ---------- figuras para simplificar a aula ----------
def cor(l):
    if l == 0: return "black!14"
    if l < 0: return "dgreen!%d" % min(75, 22 + int(abs(l) * 45))
    return "dred!%d" % min(85, 35 + int(l * 28))

def prob(l): return 1 - 1 / (1 + math.exp(l))

def linha(y, valores, mostra_p=False, feixe=None):
    out = []
    for i, l in enumerate(valores):
        x = 1.9 + i * 1.6
        out.append(r"\draw[black!60, line width=0.9pt, fill=%s] (%s,%s) rectangle +(1.6,1.3);" % (cor(l), x, y))
        txt = ("%+.2f" % l).replace(".", ",") if l != 0 else "0"
        out.append(r"\node[font=\large\bfseries] at (%s,%s) {%s};" % (round(x + 0.8, 2), round(y + 0.65, 2), txt))
        if mostra_p:
            out.append(r"\node[font=\normalsize, black!70] at (%s,%s) {%d\%%};" % (round(x + 0.8, 2), round(y - 0.3, 2), round(prob(l) * 100)))
    if feixe is not None:
        a, b = feixe
        xa = 1.9 + a * 1.6 + 0.1
        xb = 1.9 + b * 1.6 + 0.8
        out.append(r"\draw[dblue, line width=2pt, <->, >={Stealth[length=2.4mm]}] (%s,%s) -- (%s,%s);" % (round(xa, 2), round(y + 1.7, 2), round(xb, 2), round(y + 1.7, 2)))
        out.append(r"\node[font=\large, dblue, fill=white, inner sep=1pt] at (%s,%s) {feixe do robô};" % (round((xa + xb) / 2, 2), round(y + 1.7, 2)))
    return "\n  ".join(out)

v0 = [0] * 8
v1 = [-0.4] * 5 + [0.85, 0, 0]
v2 = [-0.4, -0.4, -0.8, -0.8, -0.8, 1.7, 0, 0]
w("corredor-1d", r"""
  \node[font=\Large\bfseries, dblue, anchor=west] at (0,10.3) {1. Antes de medir: log-odds 0 em todas as células};
  %s
  \node[font=\Large\bfseries, dblue, anchor=west] at (0,7.3) {2. Leitura 1: o feixe vai da célula 1 até um obstáculo na 6};
  %s
  \node[font=\Large\bfseries, dblue, anchor=west] at (0,3.6) {3. Leitura 2: o feixe vai da célula 3 ao mesmo obstáculo};
  %s
  \node[font=\large, black!70, anchor=west] at (1.9,-1.3) {verde = tende a livre; vermelho = tende a ocupada; cinza = sem informação};
""" % (linha(8.4, v0), linha(5.1, v1, feixe=(0, 5)), linha(1.4, v2, mostra_p=True, feixe=(2, 5))))

w("escala-logodds", r"""
  \fill[dgreen!75!white] (0.0,0) rectangle (0.5,1.4);
  \fill[dgreen!69!white] (0.5,0) rectangle (1.0,1.4);
  \fill[dgreen!63!white] (1.0,0) rectangle (1.5,1.4);
  \fill[dgreen!58!white] (1.5,0) rectangle (2.0,1.4);
  \fill[dgreen!52!white] (2.0,0) rectangle (2.5,1.4);
  \fill[dgreen!47!white] (2.5,0) rectangle (3.0,1.4);
  \fill[dgreen!41!white] (3.0,0) rectangle (3.5,1.4);
  \fill[dgreen!36!white] (3.5,0) rectangle (4.0,1.4);
  \fill[dgreen!30!white] (4.0,0) rectangle (4.5,1.4);
  \fill[dgreen!25!white] (4.5,0) rectangle (5.0,1.4);
  \fill[dgreen!19!white] (5.0,0) rectangle (5.5,1.4);
  \fill[dgreen!13!white] (5.5,0) rectangle (6.0,1.4);
  \fill[dgreen!8!white] (6.0,0) rectangle (6.5,1.4);
  \fill[dgreen!2!white] (6.5,0) rectangle (7.0,1.4);
  \fill[dred!2!white] (7.0,0) rectangle (7.5,1.4);
  \fill[dred!8!white] (7.5,0) rectangle (8.0,1.4);
  \fill[dred!13!white] (8.0,0) rectangle (8.5,1.4);
  \fill[dred!19!white] (8.5,0) rectangle (9.0,1.4);
  \fill[dred!24!white] (9.0,0) rectangle (9.5,1.4);
  \fill[dred!30!white] (9.5,0) rectangle (10.0,1.4);
  \fill[dred!36!white] (10.0,0) rectangle (10.5,1.4);
  \fill[dred!41!white] (10.5,0) rectangle (11.0,1.4);
  \fill[dred!47!white] (11.0,0) rectangle (11.5,1.4);
  \fill[dred!52!white] (11.5,0) rectangle (12.0,1.4);
  \fill[dred!58!white] (12.0,0) rectangle (12.5,1.4);
  \fill[dred!63!white] (12.5,0) rectangle (13.0,1.4);
  \fill[dred!69!white] (13.0,0) rectangle (13.5,1.4);
  \fill[dred!75!white] (13.5,0) rectangle (14.0,1.4);
  \draw[black!70, line width=1.4pt] (0,0) rectangle (14,1.4);
  \draw[black!80, line width=2pt] (7,-0.2) -- (7,1.6);
  \node[font=\Large\bfseries] at (7,2.2) {0 = 50\%};
  \node[font=\Large\bfseries, dgreen] at (1.6,2.2) {livre};
  \node[font=\Large\bfseries, dred] at (12.4,2.2) {ocupada};
  \draw[dred, -{Stealth[length=3.4mm]}, line width=2.4pt] (7.3,-1.3) -- (10.3,-1.3);
  \node[font=\large, dred, anchor=west] at (10.5,-1.3) {leitura ``ocupado'': $+0{,}85$};
  \draw[dgreen, -{Stealth[length=3.4mm]}, line width=2.4pt] (6.7,-2.5) -- (3.7,-2.5);
  \node[font=\large, dgreen, anchor=east] at (3.5,-2.5) {leitura ``livre'': $-0{,}4$};
""")

w("ciclo-atualizacao", flow([("Chega uma medição", "e a pose do robô"), ("Quais células?", "só as que o feixe cobre"), ("Modelo inverso", "livre, ocupada ou sem informação"), ("Soma ao log-odds", "as outras células ficam como estão")], w=4.1, h=3.4, cap="isso se repete a cada nova medição", capw=16))

w("visao-geral", flow([("Pose conhecida", "vem da odometria ou de um SLAM"), ("Medição", "sonar ou laser"), ("Modelo inverso", "diz o que a leitura sugere em cada célula"), ("Mapa de ocupação", "um log-odds por célula")], w=4.1, h=3.4, cap="nesta aula o robô \\textbf{sabe onde está} e aprende o mapa", capw=16))

w("planta-vs-realidade", r"""
  \tikzset{wall/.style={line width=3.2pt, black!85, line cap=round}, mov/.style={draw=dorange, fill=dorange!25, line width=1.4pt, rounded corners=2pt}}
  % ---- planta do arquiteto ----
  \node[font=\Large\bfseries, dblue] at (3.6,6.2) {planta do arquiteto};
  \draw[wall] (0,0) rectangle (7.2,5.2);
  \draw[wall] (3.8,0) -- (3.8,2.0); \draw[wall] (3.8,3.2) -- (3.8,5.2);
  \node[font=\large, black!60] at (1.9,2.6) {sala};
  \node[font=\large, black!60] at (5.5,2.6) {sala};
  \node[font=\large, black!60] at (3.8,-0.6) {paredes e portas, nada mais};
  % ---- seta ----
  \draw[dtrans, line width=2.6pt, -{Stealth[length=3.6mm]}] (8.0,2.6) -- (9.4,2.6);
  % ---- ambiente real ----
  \begin{scope}[shift={(10.2,0)}]
    \node[font=\Large\bfseries, dred] at (3.6,6.2) {ambiente real};
    \draw[wall] (0,0) rectangle (7.2,5.2);
    \draw[wall] (4.6,0) -- (4.6,1.6); \draw[wall] (4.6,2.8) -- (4.6,5.2);
    \draw[wall, dred] (4.6,4.2) -- (6.2,4.2);
    \draw[mov] (0.4,3.7) rectangle (2.4,4.7);
    \draw[mov] (0.4,0.4) rectangle (1.2,2.0);
    \draw[mov] (2.2,1.4) rectangle (3.6,2.4);
    \foreach \x in {0.75,1.55} {\draw[mov] (\x+1.9,0.4) circle (0.28);}
    \draw[mov] (5.2,0.4) rectangle (6.8,1.2);
    \draw[mov] (5.3,2.3) rectangle (6.0,3.0);
    \draw[mov] (6.2,2.3) rectangle (6.8,3.0);
    \node[font=\large, dorange, anchor=east] at (-0.1,6.2) {};
    \node[font=\large, black!60] at (3.6,-0.6) {móveis, divisória nova, caixas...};
  \end{scope}
  \node[font=\large\bfseries, dorange, text width=4cm, align=center] at (14.0,-1.6) {itens que a planta \textbf{não mostra}};
  \node[font=\large\bfseries, dred, text width=4cm, align=center] at (17.2,6.9) {parede que \textbf{não existe} na planta};
  \draw[dred, line width=1.4pt, -{Stealth[length=2.6mm]}] (16.9,6.5) -- (16.6,4.5);
""")

# ---------- ciclo de atualização ilustrado com um robô de sensor circular ----------
def ciclo_robo():
    N = 13; S = 0.45; C = 6                      # grade NxN, célula S cm, robô na célula central
    paredes = set()
    for i in range(1, 12):
        for (x, y) in [(i, 1), (i, 11), (1, i), (11, i)]:
            paredes.add((x, y))
    paredes |= {(8, 3), (9, 3), (9, 4), (3, 9), (4, 9), (3, 8), (6, 9)}
    paredes -= {(6, 11), (6, 1)} if False else set()
    ang = [k * 45 for k in range(8)]
    meia = 11.0                                   # meia abertura do feixe (graus)
    # lançamento de raios a partir do centro do robô
    hits = {}
    for a in ang:
        r = 0.0; hit = None
        while r < 9.0:
            r += 0.02
            x = C + 0.5 + r * math.cos(math.radians(a)); y = C + 0.5 + r * math.sin(math.radians(a))
            cel = (int(math.floor(x)), int(math.floor(y)))
            if cel in paredes: hit = (r, cel); break
        hits[a] = hit
    # classificação das células
    cls = {}
    for x in range(N):
        for y in range(N):
            if (x, y) == (C, C): continue
            dx = x + 0.5 - (C + 0.5); dy = y + 0.5 - (C + 0.5)
            r = math.hypot(dx, dy); phi = math.degrees(math.atan2(dy, dx)) % 360
            melhor = None
            for a in ang:
                d = min(abs(phi - a), 360 - abs(phi - a))
                if d <= meia and hits[a] is not None:
                    melhor = a; break
            if melhor is None: continue
            rh = hits[melhor][0]
            if r < rh - 0.6: cls[(x, y)] = "livre"
            elif r <= rh + 0.6 and (x, y) in paredes: cls[(x, y)] = "ocupada"
            elif r > rh: cls[(x, y)] = "alem"
            else: cls[(x, y)] = "livre"
    for a_ in ang:                                # a célula onde cada feixe bate é sempre ocupada
        cls[hits[a_][1]] = "ocupada"
    P = 6.4                                       # passo horizontal entre quadros
    out = []
    def cel(ox, x, y, cor):
        out.append(r"\fill[%s] (%s,%s) rectangle +(%s,%s);" % (cor, round(ox + x * S, 3), round(y * S, 3), S, S))
    def grade(ox):
        out.append(r"\draw[black!22, line width=0.3pt] (%s,0) grid[step=%s] (%s,%s);" % (ox, S, round(ox + N * S, 3), round(N * S, 3)))
        out.append(r"\draw[dblue, line width=1.3pt] (%s,0) rectangle (%s,%s);" % (ox, round(ox + N * S, 3), round(N * S, 3)))
    def robo(ox):
        cx = ox + (C + 0.5) * S; cy = (C + 0.5) * S
        out.append(r"\fill[dblue] (%s,%s) circle (0.3);" % (round(cx, 3), round(cy, 3)))
        for a in ang:
            out.append(r"\fill[white] (%s,%s) circle (0.05);" % (round(cx + 0.19 * math.cos(math.radians(a)), 3), round(cy + 0.19 * math.sin(math.radians(a)), 3)))
    def feixes(ox, cor="dorange", pontos=True):
        cx = ox + (C + 0.5) * S; cy = (C + 0.5) * S
        for a in ang:
            r = hits[a][0]
            ex = cx + r * S * math.cos(math.radians(a)); ey = cy + r * S * math.sin(math.radians(a))
            out.append(r"\draw[%s, line width=1.1pt] (%s,%s) -- (%s,%s);" % (cor, round(cx, 3), round(cy, 3), round(ex, 3), round(ey, 3)))
            if pontos: out.append(r"\fill[dred] (%s,%s) circle (0.07);" % (round(ex, 3), round(ey, 3)))
    def cones(ox):
        cx = ox + (C + 0.5) * S; cy = (C + 0.5) * S
        out.append(r"\begin{scope}")
        out.append(r"\clip (%s,0) rectangle (%s,%s);" % (ox, round(ox + N * S, 3), round(N * S, 3)))
        for a in ang:
            for da in (-meia, meia):
                t = math.radians(a + da); R = 9.0
                out.append(r"\draw[dblue, dashed, line width=0.7pt] (%s,%s) -- (%s,%s);" % (round(cx, 3), round(cy, 3), round(cx + R * math.cos(t), 3), round(cy + R * math.sin(t), 3)))
        out.append(r"\end{scope}")
    titulos = ["1. Chega uma medição", "2. Quais células?", "3. Modelo inverso", "4. Soma ao log-odds"]
    legs = ["pose $x_t$ e leituras $z_t$\\\\ do anel de sensores", "só as dentro do cone\\\\ de algum feixe (tracejado)", "livre, ocupada\\\\ ou sem informação", "as outras células\\\\ ficam como estão"]
    for q in range(4):
        ox = q * P
        out.append(r"\node[font=\large\bfseries, dblue, text width=5.8cm, align=center] at (%s,%s) {%s};" % (round(ox + N * S / 2, 3), round(N * S + 0.55, 3), titulos[q]))
        out.append(r"\node[font=\normalsize, black!75, text width=5.8cm, align=center] at (%s,-0.85) {%s};" % (round(ox + N * S / 2, 3), legs[q]))
        # fundo por quadro
        if q == 0:
            for (x, y) in paredes: cel(ox, x, y, "black!32")
        if q == 1:
            for (x, y) in paredes: cel(ox, x, y, "black!15")
            for (x, y), c in cls.items(): cel(ox, x, y, "dblue!22")
        if q == 2:
            for (x, y), c in cls.items():
                cel(ox, x, y, {"livre": "dgreen!38", "ocupada": "dred!60", "alem": "black!14"}[c])
        if q == 3:
            for x in range(N):
                for y in range(N):
                    cel(ox, x, y, "black!14")
            for (x, y), c in cls.items():
                if c == "livre": cel(ox, x, y, "dgreen!38")
                if c == "ocupada": cel(ox, x, y, "dred!60")
        grade(ox)
        if q == 1: cones(ox)
        if q in (0, 1): feixes(ox)
        robo(ox)
        if q < 3:
            out.append(r"\draw[dtrans, line width=2.2pt, -{Stealth[length=3mm]}] (%s,%s) -- (%s,%s);" % (round(ox + N * S + 0.12, 3), round(N * S / 2, 3), round(ox + P - 0.12, 3), round(N * S / 2, 3)))
    # legendas de cor no quadro 3 e 4
    itens = [("dgreen!38", "livre ($l_{free}$)"), ("dred!60", "ocupada ($l_{occ}$)"), ("black!14", "sem informação ($l_0$)")]
    x0 = 4 * P / 2 - 6.4
    for i, (c, t) in enumerate(itens):
        x = x0 + i * 4.6
        out.append(r"\fill[%s] (%s,-2.25) rectangle +(0.35,0.35);" % (c, round(x, 2)))
        out.append(r"\draw[black!45, line width=0.5pt] (%s,-2.25) rectangle +(0.35,0.35);" % round(x, 2))
        out.append(r"\node[font=\normalsize, anchor=west] at (%s,-2.07) {%s};" % (round(x + 0.5, 2), t))
    out.append(r"\node[font=\large, black!70] at (%s,-3.1) {isso se repete a cada nova medição};" % round(4 * P / 2 - 0.6, 2))
    return "\n  ".join(out)

w("ciclo-atualizacao-robo", ciclo_robo())

# ---------- sonar x laser ----------
def sonar_laser():
    out = []
    bw = 14.0                                   # meia abertura do cone do sonar (graus, exagerada)
    obx, oby, obs = 5.75, 0.95, 0.5             # bloco (obstáculo) dentro do cone
    rb = math.hypot(obx, oby + obs / 2)         # distância medida pelo sonar (aprox.)
    # ---------------- sonar ----------------
    out.append(r"\node[font=\Large\bfseries, dblue] at (4.2,3.7) {Sonar};")
    out.append(r"\fill[dgreen!22] (0,0) -- (-%s:%s) arc(-%s:%s:%s) -- cycle;" % (bw, round(rb - 0.55, 2), bw, bw, round(rb - 0.55, 2)))
    out.append(r"\fill[dred!55] (-%s:%s) arc(-%s:%s:%s) -- (%s:%s) arc(%s:-%s:%s) -- cycle;" % (bw, round(rb - 0.55, 2), bw, bw, round(rb - 0.55, 2), bw, round(rb + 0.55, 2), bw, bw, round(rb + 0.55, 2)))
    out.append(r"\fill[black!12] (-%s:%s) arc(-%s:%s:%s) -- (%s:7.6) arc(%s:-%s:7.6) -- cycle;" % (bw, round(rb + 0.55, 2), bw, bw, round(rb + 0.55, 2), bw, bw, bw))
    out.append(r"\draw[black!60, line width=1pt] (0,0) -- (-%s:7.6) arc(-%s:%s:7.6) -- cycle;" % (bw, bw, bw))
    out.append(r"\fill[black!85] (%s,%s) rectangle +(%s,%s);" % (obx, oby, obs, obs))
    out.append(r"\fill[dblue] (0,0) circle (0.17);")
    # ---------------- laser ----------------
    ox = 11.0
    out.append(r"\begin{scope}[shift={(%s,0)}]" % ox)
    out.append(r"\node[font=\Large\bfseries, dblue] at (4.2,3.7) {Laser};")
    out.append(r"\fill[black!85] (%s,%s) rectangle +(%s,%s);" % (obx, oby, obs, obs))
    for k in range(9):
        a = -bw + k * (2 * bw / 8)
        ra = math.radians(a)
        # alcance: se o feixe cruza o bloco, para na face esquerda
        x = obx
        y = math.tan(ra) * x
        if oby <= y <= oby + obs:
            r = x / math.cos(ra)
            out.append(r"\draw[dgreen, line width=1.2pt] (0,0) -- (%s,%s);" % (round(r * math.cos(ra), 3), round(r * math.sin(ra), 3)))
            out.append(r"\fill[dred!70] (%s,%s) circle (0.13);" % (round(r * math.cos(ra), 3), round(r * math.sin(ra), 3)))
        else:
            r = 7.6
            out.append(r"\draw[dgreen, line width=1.2pt] (0,0) -- (%s,%s);" % (round(r * math.cos(ra), 3), round(r * math.sin(ra), 3)))
            out.append(r"\fill[black!30] (%s,%s) circle (0.07);" % (round(r * math.cos(ra), 3), round(r * math.sin(ra), 3)))
    out.append(r"\fill[dblue] (0,0) circle (0.17);")
    out.append(r"\end{scope}")
    # ---------------- textos ----------------
    out.append(r"\node[font=\large, text width=7.8cm, align=left, anchor=north west] at (-0.4,-2.2) {\textbf{feixe largo} ($\approx 15^\circ$)\\ o obstáculo pode estar em \textbf{qualquer ponto do arco}\\ marca o \textbf{arco inteiro} como ocupado\\ leitura \textbf{menos confiável}};")
    out.append(r"\node[font=\large, text width=7.8cm, align=left, anchor=north west] at (%s,-2.2) {\textbf{feixe muito estreito}\\ \textbf{muitos feixes} por varredura\\ o obstáculo aparece \textbf{onde está}\\ leitura \textbf{mais precisa}};" % (ox - 0.4))
    # legenda
    for i, (c, t) in enumerate([("dgreen!22", "livre"), ("dred!55", "ocupada"), ("black!12", "sem informação"), ("black!85", "obstáculo real")]):
        x = 1.0 + i * 4.6
        out.append(r"\fill[%s] (%s,-6.1) rectangle +(0.35,0.35);" % (c, x))
        out.append(r"\draw[black!45, line width=0.5pt] (%s,-6.1) rectangle +(0.35,0.35);" % x)
        out.append(r"\node[font=\normalsize, anchor=west] at (%s,-5.92) {%s};" % (round(x + 0.5, 2), t))
    return "\n  ".join(out)

w("sonar-vs-laser", sonar_laser())

# ---------- exemplo numérico: treino em 1D (valores obtidos por simulação) ----------
def treino_1d():
    vals = [0.00, 0.00, 0.00, 0.13, 0.81, 0.26, 0.20, 0.20, 0.20]
    out = []
    H = 5.0
    out.append(r"\draw[daxis, line width=1.2pt] (0,0) -- (12.4,0) node[right, font=\large] {célula $r$};")
    out.append(r"\draw[daxis, line width=1.2pt] (0,0) -- (0,%s) node[above, font=\large] {$p(\text{ocupada})$};" % (H + 0.4))
    for v, lab in [(0, "0"), (0.5, "0,5"), (1.0, "1")]:
        out.append(r"\draw[black!30, line width=0.4pt] (0,%s) -- (12.0,%s);" % (v * H, v * H))
        out.append(r"\node[font=\large, anchor=east] at (-0.15,%s) {%s};" % (v * H, lab))
    out.append(r"\draw[dorange, dashed, line width=1.6pt] (0,%s) -- (12.0,%s);" % (0.2 * H, 0.2 * H))
    out.append(r"\node[font=\large, dorange, anchor=west] at (12.15,%s) {prior $0{,}2$};" % round(0.2 * H, 2))
    for i, v in enumerate(vals):
        r = i + 1
        x = 0.4 + i * 1.3
        c = "dgreen!55" if r <= 3 else ("dred!70" if r == 5 else ("dblue!35" if r == 4 else "black!22"))
        if r == 6: c = "black!22"
        out.append(r"\fill[%s] (%s,0) rectangle (%s,%s);" % (c, x, round(x + 0.95, 2), round(max(v * H, 0.04), 3)))
        out.append(r"\node[font=\large\bfseries, fill=white, inner sep=1.5pt] at (%s,%s) {%s};" % (round(x + 0.475, 3), round(v * H + 0.38, 3), ("%.2f" % v).replace(".", ",")))
        out.append(r"\node[font=\large] at (%s,-0.5) {%d};" % (round(x + 0.475, 3), r))
    out.append(r"\node[font=\large\bfseries, dgreen, text width=4cm, align=center] at (2.2,-1.5) {antes da leitura: \textbf{livre}};")
    out.append(r"\node[font=\large\bfseries, dred, text width=4cm, align=center] at (6.5,-1.5) {na leitura: \textbf{ocupada}};")
    out.append(r"\node[font=\large\bfseries, black!60, text width=5cm, align=center] at (10.3,-1.5) {depois: volta ao \textbf{prior}};")
    out.append(r"\node[font=\Large\bfseries, dblue] at (6.0,%s) {leitura $z \approx 5$};" % (H + 1.2))
    return "\n  ".join(out)

w("treino-1d", treino_1d())

# ---------- o espaço do próprio robô ----------
def espaco_robo():
    NR, NCc, S = 7, 9, 0.62
    cr, cc = 3, 4                      # célula central (linha, coluna) do robô
    cores = {'W': 'black!85', 'f': 'dgreen!20', '?': 'black!18', 'o': 'dred!60', 'F': 'dgreen!75'}
    def base():
        m = [['f'] * NCc for _ in range(NR)]
        for c in range(NCc): m[0][c] = 'W'; m[NR - 1][c] = 'W'
        return m
    foot = [(r, c) for r in range(cr - 1, cr + 2) for c in range(cc - 1, cc + 2)]
    m1 = base()
    for r, c in foot: m1[r][c] = '?'
    m1[cr - 1][cc + 1] = 'o'; m1[cr + 1][cc - 1] = 'o'
    m2 = base()
    for p in range(1, cc + 1):                      # trilha: poses anteriores ao longo da linha central
        for r in range(cr - 1, cr + 2):
            for c in range(p - 1, p + 2):
                if 0 <= c < NCc: m2[r][c] = 'F'
    P = NCc * S + 1.4
    out = []
    out.append(r"\useasboundingbox (-0.2,-3.0) rectangle (%.2f,%.2f);" % (2 * P + 1.0, NR * S + 1.0))
    out.append(r"\node[font=\Large\bfseries, dblue] at (%.2f,%.2f) {só com as medições};" % (NCc * S / 2, NR * S + 0.5))
    out.append(r"\node[font=\Large\bfseries, dgreen!60!black] at (%.2f,%.2f) {somando o espaço do robô};" % (P + NCc * S / 2, NR * S + 0.5))
    out.append(grade(m1, 0, 0, S, cores))
    out.append(grade(m2, P, 0, S, cores))
    for ox in (0, P):
        cx = ox + (cc + 0.5) * S; cy = (NR - 1 - cr + 0.5) * S
        out.append(r"\draw[dblue, line width=2.4pt] (%.3f,%.3f) circle (%.3f);" % (cx, cy, 1.45 * S))
        out.append(r"\fill[dblue] (%.3f,%.3f) circle (0.14);" % (cx, cy))
    cy = (NR - 1 - cr + 0.5) * S
    for p in range(1, cc):
        out.append(r"\fill[dblue!60] (%.3f,%.3f) circle (0.08);" % (P + (p + 0.5) * S, cy))
    out.append(r"\draw[dblue, -{Stealth[length=2.6mm]}, line width=1.3pt] (%.3f,%.3f) -- (%.3f,%.3f);" % (P + 0.55 * S, cy, P + (cc + 0.5) * S - 0.5, cy))
    # rótulos
    out.append(r"\node[font=\large, dred, text width=3.6cm, align=center] at (%.2f,-0.75) {leituras erradas dentro do robô};" % (NCc * S / 2))
    out.append(r"\node[font=\large, dgreen!60!black, text width=4.5cm, align=center] at (%.2f,-0.75) {$l$ muito negativo: \textbf{trilha livre}};" % (P + NCc * S / 2))
    # legenda
    itens = [("dgreen!75", "livre (muito negativo)"), ("dgreen!20", "livre"), ("dred!60", "ocupada"), ("black!18", "sem informação")]
    x = 0.0
    for c, t in itens:
        out.append(r"\fill[%s] (%.2f,-2.05) rectangle ++(0.4,0.4);" % (c, x))
        out.append(r"\draw[black!45, line width=0.5pt] (%.2f,-2.05) rectangle ++(0.4,0.4);" % x)
        out.append(r"\node[font=\normalsize, anchor=west] at (%.2f,-1.85) {%s};" % (x + 0.5, t))
        x += 0.5 + 0.17 * len(t) + 0.5
    out.append(r"\node[font=\Large, black!75] at (%.2f,-2.75) {onde o robô esteve, \textbf{é livre}};" % (P - 0.55))
    return "\n  ".join(out)

w("espaco-do-robo", espaco_robo())

# ---------- filtro único: o mesmo vidro, dois mapas ----------
w("filtro-unico-conflito", r"""
  \useasboundingbox (-3.6,-3.9) rectangle (22.4,5.6);
  % ---- cena (vista de cima) ----
  \node[font=\Large\bfseries, dblue] at (4.3,4.7) {o mesmo vidro};
  \draw[black!85, line width=5pt] (8.6,-2.4) -- (8.6,3.6);
  \node[font=\large, black!70] at (9.4,-2.9) {parede};
  \draw[dblue!45, line width=7pt, line cap=butt] (5.7,-2.4) -- (5.7,3.6);
  \node[font=\large\bfseries, dblue!70!black] at (5.7,4.15) {vidro};
  % sonar (A): cone largo que para no vidro
  \fill[dred!18] (0,0) -- (-15:5.5) arc(-15:15:5.5) -- cycle;
  \draw[black!55, line width=0.9pt] (0,0) -- (-15:5.5) arc(-15:15:5.5) -- cycle;
  \fill[dred!60] (5.45,-1.4) rectangle (5.95,1.4);
  % laser (B): feixes finos que atravessam o vidro
  \foreach \a in {-8,-4,0,4,8} {\draw[dgreen, line width=1.1pt] (0,0) -- (\a:8.55);}
  \foreach \a in {-8,-4,0,4,8} {\fill[dgreen] (\a:8.55) circle (0.09);}
  \fill[dblue] (0,0) circle (0.2);
  \node[font=\large\bfseries, dred, anchor=east] at (-0.35,2.1) {A: sonar};
  \node[font=\large, dred, anchor=east] at (-0.35,1.55) {vê o vidro};
  \node[font=\large\bfseries, dgreen!60!black, anchor=east] at (-0.35,-1.55) {B: laser};
  \node[font=\large, dgreen!60!black, anchor=east] at (-0.35,-2.1) {atravessa};
  % ---- dois cenários para a mesma célula ----
  \node[font=\Large\bfseries, dblue] at (16.6,4.7) {log-odds da célula do vidro};
  \tikzset{c/.style={dbox, text width=9.2cm, minimum height=2.6cm, font=\large, line width=1.5pt, align=center}}
  \node[c, draw=dgreen] at (16.6,2.2) {sonar mede \textbf{1 vez} e laser \textbf{5 vezes}\\[3pt] $0{,}85 - 5 \times 0{,}4 = \mathbf{-1{,}15}$\\ \textbf{\textcolor{dgreen!60!black}{o mapa diz: livre}}};
  \node[c, draw=dred] at (16.6,-1.3) {sonar mede \textbf{5 vezes} e laser \textbf{1 vez}\\[3pt] $5 \times 0{,}85 - 0{,}4 = \mathbf{+3{,}85}$\\ \textbf{\textcolor{dred}{o mapa diz: ocupada}}};
  \node[font=\Large, black!75] at (11.0,-3.5) {o resultado depende de \textbf{quantas vezes} cada sensor mede};
""")
