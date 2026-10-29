"""Gera os .tex das figuras da aula 6 de Navegação a partir do código da própria aula."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
from wavefront import *  # noqa

TEXTO = ["........."
         , "....#...."
         , "....#.##."
         , ".G..#..#."
         , "....#..#S"
         , "........."]
GRADE = [[OBSTACULO if ch == "#" else LIVRE for ch in linha] for linha in TEXTO]
G, S = (3, 1), (4, 8)
R, C = len(GRADE), len(GRADE[0])

CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
RODAPE = "\\end{tikzpicture}\n\\end{document}\n"


def xy(lin, col, s, ox=0, oy=0, rows=R):
    return ox + (col + 0.5) * s, oy + (rows - 1 - lin + 0.5) * s


def painel(grade, ox, oy, s, celula=None, rota=None, marcas=True, titulo=None, fonte=r"\Large"):
    """celula(lin,col) -> (preenchimento ou None, texto ou None)."""
    rows, cols = len(grade), len(grade[0])
    out = []
    nums = []
    for lin in range(rows):
        for col in range(cols):
            x0 = ox + col * s
            y0 = oy + (rows - 1 - lin) * s
            fill, txt = (None, None)
            if grade[lin][col] == OBSTACULO:
                fill = "black!80"
            elif celula:
                fill, txt = celula(lin, col)
            f = "fill=%s, " % fill if fill else "fill=white, "
            out.append(r"\draw[%sdraw=black!30, line width=0.4pt] (%.3f,%.3f) rectangle ++(%.3f,%.3f);" % (f, x0, y0, s, s))
            if txt is not None and grade[lin][col] == LIVRE:
                x, y = xy(lin, col, s, ox, oy, rows)
                nums.append(r"\node[font=%s, black!80] at (%.3f,%.3f) {%s};" % (fonte, x, y, txt))
    out.append(r"\draw[black!80, line width=1.2pt] (%.3f,%.3f) rectangle (%.3f,%.3f);" % (ox, oy, ox + cols * s, oy + rows * s))
    if rota:
        pts = " -- ".join("(%.3f,%.3f)" % xy(l, c, s, ox, oy, rows) for l, c in rota)
        out.append(r"\draw[dorange, line width=2.6pt, line cap=round, line join=round, -{Stealth[length=3mm]}] %s;" % pts)
    out.extend(nums)
    if marcas:
        for (l, c), nome, cor in ((S, "S", "dgreen"), (G, "G", "dred")):
            x, y = xy(l, c, s, ox, oy, rows)
            out.append(r"\node[circle, fill=%s, text=white, font=\bfseries%s, inner sep=1.5pt, minimum size=%.2fcm] at (%.3f,%.3f) {%s};" % (cor, fonte, s * 0.72, x, y, nome))
    if titulo:
        out.append(r"\node[font=\Large\bfseries, black!75] at (%.3f,%.3f) {%s};" % (ox + cols * s / 2, oy + rows * s + 0.55, titulo))
    return "\n".join(out)


def azul(v, vmax):
    return "dblue!%d!white" % int(10 + 55 * v / max(vmax, 1))


def grava(nome, corpo):
    with open(nome + ".tex", "w") as f:
        f.write(CAB + corpo + "\n" + RODAPE)


dist = wavefront(GRADE, G)
vmax = max(v for lin in dist for v in lin if v != INF)
rota4 = caminho(dist, S)

# 1. grade de entrada
grava("grade-entrada", painel(GRADE, 0, 0, 1.15) + "\n" +
      r"\node[font=\Large, black!70, anchor=west] at (11.0,4.6) {branco: \textbf{livre}};" + "\n" +
      r"\node[font=\Large, black!70, anchor=west] at (11.0,3.7) {preto: \textbf{obstáculo}};" + "\n" +
      r"\node[font=\Large, black!70, anchor=west] at (11.0,2.8) {\textbf{S} início};" + "\n" +
      r"\node[font=\Large, black!70, anchor=west] at (11.0,1.9) {\textbf{G} objetivo};")

# 2. etapas da onda
paineis = []
for i, k in enumerate((1, 4, 8, vmax)):
    def cel(l, c, k=k):
        v = dist[l][c]
        if v == INF or v > k:
            return None, None
        if v == k and k != vmax:
            return "dorange!45!white", str(int(v))
        return azul(v, vmax), str(int(v))
    tit = "onda %d" % k if k != vmax else "onda %d (completa)" % k
    paineis.append(painel(GRADE, i * 7.8, 0, 0.8, celula=cel, titulo=tit))
paineis.append(r"\draw[fill=dorange!45!white, draw=black!30, line width=0.4pt] (0.4,-1.15) rectangle ++(0.6,0.6);")
paineis.append(r"\node[font=\Large, black!75, anchor=west] at (1.25,-0.85) {laranja = \textbf{fronteira da onda}: células alcançadas nesta rodada};")
paineis.append(r"\draw[fill=dblue!20!white, draw=black!30, line width=0.4pt] (16.2,-1.15) rectangle ++(0.6,0.6);")
paineis.append(r"\draw[fill=dblue!60!white, draw=black!30, line width=0.4pt] (16.8,-1.15) rectangle ++(0.6,0.6);")
paineis.append(r"\node[font=\Large, black!75, anchor=west] at (17.65,-0.85) {azul = \textbf{já visitadas} (mais escuro = mais longe)};")
grava("wavefront-etapas", "\n".join(paineis))

# 3. resultado + caminho
grava("wavefront-resultado", painel(GRADE, 0, 0, 1.4, celula=lambda l, c: (azul(dist[l][c], vmax), str(int(dist[l][c])) if dist[l][c] != INF else None), rota=rota4))

# 4. 4 x 8 vizinhos (ícones)
viz = []
for ox, nome, vs in ((0, "4 vizinhos", VIZINHOS_4), (9, "8 vizinhos", VIZINHOS_8)):
    viz.append(r"\node[font=\Large\bfseries, black!75] at (%.2f,4.9) {%s};" % (ox + 2.1, nome))
    for dl in (-1, 0, 1):
        for dc in (-1, 0, 1):
            x, y = ox + 0.7 + (dc + 1) * 1.4, 0.7 + (1 - dl) * 1.4 - 0.0
            y = 0.7 + (-dl + 1) * 1.4
            centro = dl == 0 and dc == 0
            ativo = centro or (dl, dc) in vs
            fill = "dblue!25!white" if centro else ("dcream" if ativo else "white")
            out = r"\draw[fill=%s, draw=black!%d, line width=0.6pt] (%.2f,%.2f) rectangle ++(1.4,1.4);" % (fill, 60 if ativo else 20, x - 0.7, y - 0.7)
            viz.append(out)
            if ativo and not centro:
                viz.append(r"\node[font=\Large, black!80] at (%.2f,%.2f) {%s};" % (x, y, r"$\sqrt{2}$" if dl and dc else "1"))
            if centro:
                viz.append(r"\node[font=\Large\bfseries, dblue] at (%.2f,%.2f) {célula};" % (x, y))
grava("vizinhancas", "\n".join(viz))

# 5. caminhos 4 x 8
d8 = wavefront_8(GRADE, G)
rota8 = caminho(d8, S, VIZINHOS_8)
custo8 = d8[S[0]][S[1]]
grava("comparacao-4-8",
      painel(GRADE, 0, 0, 1.15, celula=lambda l, c: (None, None), rota=rota4, titulo="4 vizinhos: custo %d" % dist[S[0]][S[1]]) + "\n" +
      painel(GRADE, 11.4, 0, 1.15, celula=lambda l, c: (None, None), rota=rota8, titulo="8 vizinhos: custo %s" % ("%.2f" % custo8).replace(".", ",")))

# 6. inflação
TEXTO2 = ["....#......"
          , "....#......"
          , "..........."
          , "....#......"
          , "....#......"
          , "..........."
          , "..........."]
G2 = [[OBSTACULO if ch == "#" else LIVRE for ch in linha] for linha in TEXTO2]
I2 = inflar(G2, 1)
g2, s2 = (2, 0), (2, 10)
r_sem = caminho(wavefront(G2, g2), s2)
r_com = caminho(wavefront(I2, g2), s2)
assert r_sem and r_com and len(r_com) > len(r_sem)
def inf_cel(l, c):
    return ("dshade" if I2[l][c] == OBSTACULO and G2[l][c] == LIVRE else None), None
S0, G0 = S, G
S, G = s2, g2
corpo = painel(G2, 0, 0, 0.95, celula=lambda l, c: (None, None), rota=r_sem, titulo="sem margem: passa rente à parede") + "\n" + \
        painel(G2, 12.4, 0, 0.95, celula=inf_cel, rota=r_com, titulo="com margem: a passagem estreita fecha")
grava("inflar-obstaculos", corpo)
S, G = S0, G0

# 7. wavefront x A*
TEXTO3 = ["............."
          , "............."
          , "....#........"
          , "....#........"
          , "....#..####.."
          , "....#........"
          , "............."]
G3 = [[OBSTACULO if ch == "#" else LIVRE for ch in linha] for linha in TEXTO3]
g3, s3 = (3, 1), (3, 11)
d3 = wavefront(G3, g3)
rota3 = caminho(d3, s3)
_, exp3 = astar(G3, s3, g3)
alc = sum(1 for lin in d3 for v in lin if v != INF)
S, G = s3, g3
fa = lambda l, c: ("dblue!25!white" if (l, c) in set(exp3) else None, None)
fw = lambda l, c: ("dblue!25!white" if d3[l][c] != INF else None, None)
corpo = painel(G3, 0, 0, 0.9, celula=fw, rota=rota3, titulo="wavefront: %d células" % alc) + "\n" + \
        painel(G3, 13.0, 0, 0.9, celula=fa, rota=rota3, titulo="A*: %d células" % len(set(exp3)))
grava("wavefront-astar", corpo)
S, G = S0, G0
print("OK", vmax, len(rota4) - 1, "%.2f" % custo8, len(rota8) - 1, "wf", alc, "A*", len(set(exp3)),
      "sem", len(r_sem) - 1, "com", len(r_com) - 1)

# 8. OccupancyGrid -> índices (desenhado à mão)
oc = []
s = 1.5
for lin in range(4):
    for col in range(5):
        oc.append(r"\draw[fill=%s, draw=black!35] (%.2f,%.2f) rectangle ++(%.2f,%.2f);" % ("black!75" if (lin, col) in ((1, 2), (2, 2)) else "white", col * s, lin * s, s, s))
        idx = lin * 5 + col
        if (lin, col) not in ((1, 2), (2, 2)):
            oc.append(r"\node[font=\large, black!60] at (%.2f,%.2f) {%d};" % ((col + 0.5) * s, (lin + 0.5) * s, idx))
oc.append(r"\draw[black!80, line width=1.2pt] (0,0) rectangle (%.2f,%.2f);" % (5 * s, 4 * s))
oc.append(r"\node[circle, fill=dorange, inner sep=2pt] at (0,0) {};")
oc.append(r"\node[font=\Large\bfseries, dorange, anchor=north east] at (-0.15,-0.1) {origem $(o_x, o_y)$};")
oc.append(r"\draw[daxis, line width=1.2pt, ->] (-0.3,-0.9) -- (3.2,-0.9) node[right, font=\Large] {$x$};")
oc.append(r"\draw[daxis, line width=1.2pt, ->] (-0.9,-0.3) -- (-0.9,2.6) node[above, font=\Large] {$y$};")
for col in range(5):
    oc.append(r"\node[font=\Large\bfseries, dblue] at (%.2f,-0.55) {%d};" % ((col + 0.5) * s, col)) if False else None
for col in range(5):
    oc.append(r"\node[font=\Large, dblue] at (%.2f,%.2f) {col %d};" % ((col + 0.5) * s, 4 * s + 0.45, col))
for lin in range(4):
    oc.append(r"\node[font=\Large, dblue, anchor=west] at (%.2f,%.2f) {linha %d};" % (5 * s + 0.2, (lin + 0.5) * s, lin))
oc.append(r"\node[font=\Large, black!75, anchor=west, text width=9.5cm, align=left] at (12.2,4.6) {\textbf{resolução} $r$: metros por célula\\[4pt] \textbf{largura} $w$ e \textbf{altura} $h$, em células\\[4pt] \texttt{data} é uma lista só, \textbf{linha a linha}, de baixo para cima\\[8pt] \texttt{índice} $=$ \texttt{linha}$\cdot w +$ \texttt{coluna}\\[4pt] \texttt{coluna} $=\lfloor (x-o_x)/r \rfloor$\\[4pt] \texttt{linha} $=\lfloor (y-o_y)/r \rfloor$};")
grava("ocupacao-ros", "\n".join(oc))

# 9. pipeline
pl = []
nomes = ["mapa\\\\\\texttt{/map}", "binarizar", "inflar", "wavefront", "caminho", "mensagem\\\\\\texttt{Path}", "controlador"]
cores = ["dblue", "dgreen", "dgreen", "dorange", "dorange", "dblue", "dred"]
for i, (n, cor) in enumerate(zip(nomes, cores)):
    x = i * 3.55
    pl.append(r"\node[dbox, draw=%s, line width=1.5pt, text width=2.7cm, minimum height=2.6cm, font=\Large] (b%d) at (%.2f,0) {%s};" % (cor, i, x, n))
    if i:
        pl.append(r"\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (b%d.east) -- (b%d.west);" % (i - 1, i))
grava("pipeline-ros", "\n".join(pl))


# 4. a fila em ação (mesma grade da aula, 4 vizinhos: cima, baixo, esquerda, direita)
from collections import deque as _dq
def _snapshots(n_passos=3):
    d = {G: 0}
    f = _dq([G])
    popped = set()
    snaps = [("início", None, list(f), dict(d), set(popped))]
    for k in range(1, n_passos + 1):
        sai = f.popleft()
        popped.add(sai)
        for dl, dc in VIZINHOS_4:
            l, c = sai[0] + dl, sai[1] + dc
            if 0 <= l < R and 0 <= c < C and GRADE[l][c] == LIVRE and (l, c) not in d:
                d[(l, c)] = d[sai] + 1
                f.append((l, c))
        snaps.append(("passo %d" % k, sai, list(f), dict(d), set(popped)))
    return snaps

_snaps = _snapshots()
_cor = {0: "dgreen!45", 1: "dorange!40", 2: "dblue!35"}
_out = []
_PITCH, _W, _H, _X0 = 1.65, 1.5, 1.45, 4.3
_CAP = 8
_xend = _X0 + _CAP * _PITCH
_MS = 0.34                                  # tamanho das células do mini-mapa
_RP = 2.2                                   # passo vertical entre linhas
_MX = _xend + 0.95                          # origem x dos mini-mapas
_xfim = _MX + C * _MS
_out.append(r"\useasboundingbox (-0.2,-9.9) rectangle (%.2f,2.35);" % (_xfim + 0.3))
_out.append(r"\node[font=\large\bfseries, dred, anchor=west] at (%.2f,1.65) {$\leftarrow$ sai (início da fila)};" % (_X0 - 0.1))
_out.append(r"\node[font=\large\bfseries, dgreen!60!black, anchor=east] at (%.2f,1.65) {entra (fim da fila) $\leftarrow$};" % (_xend + 0.1))
_out.append(r"\node[font=\large\bfseries, dblue] at (%.2f,1.65) {mapa};" % (_MX + C * _MS / 2))
for i, (nome, sai, fila, dist_, saiu) in enumerate(_snaps):
    y = -i * _RP
    _out.append(r"\draw[black!55, line width=1.1pt, rounded corners=5pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (_X0 - 0.15, y - 0.88, _xend + 0.05, y + 0.88))
    rot = r"\textbf{%s}" % nome if sai is None else r"\textbf{%s}\\ sai \texttt{(%d,%d)}" % (nome, sai[0], sai[1])
    _out.append(r"\node[font=\large, anchor=west, text width=3.5cm, align=left] at (0,%.2f) {%s};" % (y, rot))
    for j, (l, c) in enumerate(fila):
        cx = _X0 + j * _PITCH + _W / 2
        d = dist_[(l, c)]
        _out.append(r"\draw[fill=%s, draw=black!45, line width=0.6pt, rounded corners=2pt] (%.2f,%.2f) rectangle ++(%s,%s);" % (_cor.get(d, "black!15"), cx - _W / 2, y - _H / 2, _W, _H))
        _out.append(r"\node[font=\normalsize, black!75] at (%.2f,%.2f) {(%d,%d)};" % (cx, y + 0.36, l, c))
        _out.append(r"\node[font=\Large\bfseries] at (%.2f,%.2f) {%d};" % (cx, y - 0.28, d))
    # mini-mapa
    oy = y - R * _MS / 2
    for l in range(R):
        for c in range(C):
            x0 = _MX + c * _MS
            y0 = oy + (R - 1 - l) * _MS
            if GRADE[l][c] == OBSTACULO:
                cor_ = "black!80"
            elif (l, c) in dist_:
                cor_ = _cor.get(dist_[(l, c)], "black!15")
            else:
                cor_ = "white"
            _out.append(r"\draw[fill=%s, draw=black!30, line width=0.3pt] (%.3f,%.3f) rectangle ++(%s,%s);" % (cor_, x0, y0, _MS, _MS))
            if (l, c) in saiu:
                _out.append(r"\fill[black!75] (%.3f,%.3f) circle (0.07);" % (x0 + _MS / 2, y0 + _MS / 2))
    _out.append(r"\draw[dblue, line width=1pt] (%.3f,%.3f) rectangle (%.3f,%.3f);" % (_MX, oy, _xfim, oy + R * _MS))
_yb = -len(_snaps) * _RP + 0.55
for k, (cor_, txt) in enumerate([("dgreen!45", "distância 0"), ("dorange!40", "distância 1"), ("dblue!35", "distância 2")]):
    x = 4.3 + k * 4.2
    _out.append(r"\draw[fill=%s, draw=black!45, line width=0.6pt] (%.2f,%.2f) rectangle ++(0.5,0.5);" % (cor_, x, _yb - 0.55))
    _out.append(r"\node[font=\large, anchor=west] at (%.2f,%.2f) {%s};" % (x + 0.65, _yb - 0.3, txt))
_out.append(r"\fill[black!75] (%.2f,%.2f) circle (0.09);" % (4.3 + 3 * 4.2 + 0.25, _yb - 0.3))
_out.append(r"\node[font=\large, anchor=west] at (%.2f,%.2f) {já saiu da fila};" % (4.3 + 3 * 4.2 + 0.65, _yb - 0.3))
_out.append(r"\node[font=\large, black!75] at (%.2f,%.2f) {as de distância 1 saem \textbf{antes} das de distância 2: a fila as mantém \textbf{em ordem}};" % ((_X0 + _xend) / 2 - 0.4, _yb - 1.15))
grava("fila-em-acao", "\n".join(_out))


# 5. construindo o caminho (descida do gradiente, depois que a onda terminou)
_rota = rota4
_n = len(_rota)
_P, _Wb, _Hb, _X0c, _RPc, _MSc = 1.2, 1.1, 1.45, 4.3, 2.2, 0.34
_xendc = _X0c + _n * _P
_MXc = _xendc + 0.95
_xfimc = _MXc + C * _MSc
_snapc = [("início", None, 1), ("passo 1", _rota[1], 2), ("passo 2", _rota[2], 3), ("passo %d" % (_n - 1), _rota[-1], _n)]
_o = []
_o.append(r"\useasboundingbox (-0.2,-9.9) rectangle (%.2f,2.35);" % (_xfimc + 0.3))
_o.append(r"\node[font=\large\bfseries, dgreen!60!black, anchor=west] at (%.2f,1.65) {início do caminho (S)};" % (_X0c - 0.1))
_o.append(r"\node[font=\large\bfseries, dred, anchor=east] at (%.2f,1.65) {entra (fim do caminho) $\leftarrow$};" % (_xendc + 0.1))
_o.append(r"\node[font=\large\bfseries, dblue] at (%.2f,1.65) {mapa};" % (_MXc + C * _MSc / 2))
for i, (nome, novo, k) in enumerate(_snapc):
    y = -i * _RPc
    _o.append(r"\draw[black!55, line width=1.1pt, rounded corners=5pt] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (_X0c - 0.15, y - 0.88, _xendc + 0.05, y + 0.88))
    rot = r"\textbf{%s}" % nome if novo is None else r"\textbf{%s}\\ vai para \texttt{(%d,%d)}" % (nome, novo[0], novo[1])
    _o.append(r"\node[font=\large, anchor=west, text width=3.5cm, align=left] at (0,%.2f) {%s};" % (y, rot))
    for j in range(k):
        l, c = _rota[j]
        d = int(dist[l][c])
        cx = _X0c + j * _P + _Wb / 2
        cor_ = "dgreen!45" if d == 0 else azul(d, vmax)
        borda = "dorange, line width=2.4pt" if (j == k - 1 and novo is not None) else "black!45, line width=0.6pt"
        _o.append(r"\draw[fill=%s, draw=%s, rounded corners=2pt] (%.2f,%.2f) rectangle ++(%s,%s);" % (cor_, borda, cx - _Wb / 2, y - _Hb / 2, _Wb, _Hb))
        _o.append(r"\node[font=\small, black!75] at (%.2f,%.2f) {(%d,%d)};" % (cx, y + 0.36, l, c))
        _o.append(r"\node[font=\Large\bfseries] at (%.2f,%.2f) {%d};" % (cx, y - 0.28, d))
    # mini-mapa: campo de distâncias + caminho até aqui
    oy = y - R * _MSc / 2
    feitas = set(_rota[:k])
    for l in range(R):
        for c in range(C):
            x0 = _MXc + c * _MSc
            y0 = oy + (R - 1 - l) * _MSc
            if GRADE[l][c] == OBSTACULO:
                cor_ = "black!80"
            elif (l, c) in feitas:
                cor_ = "dorange!65"
            else:
                cor_ = azul(dist[l][c], vmax)
            _o.append(r"\draw[fill=%s, draw=black!30, line width=0.3pt] (%.3f,%.3f) rectangle ++(%s,%s);" % (cor_, x0, y0, _MSc, _MSc))
    rl, rc = _rota[k - 1]
    _o.append(r"\draw[dred, line width=1.8pt] (%.3f,%.3f) circle (0.15);" % (_MXc + (rc + 0.5) * _MSc, oy + (R - 1 - rl + 0.5) * _MSc))
    _o.append(r"\draw[dblue, line width=1pt] (%.3f,%.3f) rectangle (%.3f,%.3f);" % (_MXc, oy, _xfimc, oy + R * _MSc))
    if i == 2:
        _o.append(r"\node[font=\Large, black!55] at (%.2f,%.2f) {$\vdots$};" % ((_X0c + _xendc) / 2, y - _RPc / 2 - 0.02))
_ybc = -len(_snapc) * _RPc + 0.55
_o.append(r"\draw[fill=dorange!65, draw=black!45, line width=0.6pt] (%.2f,%.2f) rectangle ++(0.5,0.5);" % (4.3, _ybc - 0.55))
_o.append(r"\node[font=\large, anchor=west] at (%.2f,%.2f) {caminho já montado};" % (4.95, _ybc - 0.3))
_o.append(r"\draw[fill=dblue!45!white, draw=black!45, line width=0.6pt] (%.2f,%.2f) rectangle ++(0.5,0.5);" % (9.9, _ybc - 0.55))
_o.append(r"\node[font=\large, anchor=west] at (%.2f,%.2f) {campo de distâncias};" % (10.55, _ybc - 0.3))
_o.append(r"\draw[dred, line width=1.8pt] (%.2f,%.2f) circle (0.2);" % (15.25, _ybc - 0.3))
_o.append(r"\node[font=\large, anchor=west] at (%.2f,%.2f) {posição do robô};" % (15.65, _ybc - 0.3))
_o.append(r"\node[font=\large, black!75] at (%.2f,%.2f) {a cada passo: vá para a vizinha de \textbf{menor distância}; a distância cai \textbf{1} por passo até o \textbf{0}};" % ((_X0c + _xendc) / 2 - 0.6, _ybc - 1.15))
grava("caminho-em-acao", "\n".join(_o))


# 6. executando à mão: um quadro de mapa por iteração (mesma tabela do slide)
def _iteracoes(n=4):
    d = {G: 0}
    f = _dq([G])
    its = []
    for k in range(1, n + 1):
        antes = dict(d)
        sai = f.popleft()
        novas = []
        for dl, dc in VIZINHOS_4:
            l, c = sai[0] + dl, sai[1] + dc
            if 0 <= l < R and 0 <= c < C and GRADE[l][c] == LIVRE and (l, c) not in d:
                d[(l, c)] = d[sai] + 1
                f.append((l, c))
                novas.append((l, c))
        its.append((k, sai, novas, antes, dict(d), len(f)))
    return its

_S6 = 0.8
_W6 = C * _S6
_P6 = _W6 + 0.7
_o6 = []
_o6.append(r"\useasboundingbox (-0.2,-2.9) rectangle (%.2f,%.2f);" % (4 * _P6 - 0.5 + 0.2, R * _S6 + 1.0))
for k, sai, novas, antes, depois, tam in _iteracoes():
    ox = (k - 1) * _P6
    def cel6(l, c, antes=antes, depois=depois, novas=novas):
        if (l, c) in novas:
            return "dorange!45!white", str(depois[(l, c)])
        if (l, c) in antes:
            return azul(antes[(l, c)], 2), str(antes[(l, c)])
        return None, None
    _o6.append(painel(GRADE, ox, 0, _S6, celula=cel6, marcas=False, titulo="iteração %d" % k))
    x0 = ox + sai[1] * _S6
    y0 = (R - 1 - sai[0]) * _S6
    _o6.append(r"\draw[dred, line width=3pt] (%.3f,%.3f) rectangle ++(%s,%s);" % (x0 + 0.03, y0 + 0.03, _S6 - 0.06, _S6 - 0.06))
    nov = "entram %d" % len(novas) if novas else "nenhuma entra"
    _o6.append(r"\node[font=\large, black!80] at (%.3f,-0.5) {sai \texttt{(%d,%d)} $\cdot$ %s};" % (ox + _W6 / 2, sai[0], sai[1], nov))
    _o6.append(r"\node[font=\large\bfseries, black!80] at (%.3f,-1.2) {fila: %d};" % (ox + _W6 / 2, tam))
_lx = 2.0
_o6.append(r"\draw[fill=dorange!45!white, draw=black!45, line width=0.6pt] (%.2f,-2.55) rectangle ++(0.5,0.5);" % _lx)
_o6.append(r"\node[font=\large, anchor=west] at (%.2f,-2.3) {recebem distância nesta iteração};" % (_lx + 0.65))
_o6.append(r"\draw[fill=dblue!50!white, draw=black!45, line width=0.6pt] (%.2f,-2.55) rectangle ++(0.5,0.5);" % (_lx + 9.6))
_o6.append(r"\node[font=\large, anchor=west] at (%.2f,-2.3) {já alcançadas antes};" % (_lx + 10.25))
_o6.append(r"\draw[dred, line width=3pt] (%.2f,-2.55) rectangle ++(0.5,0.5);" % (_lx + 16.0))
_o6.append(r"\node[font=\large, anchor=west] at (%.2f,-2.3) {sai da fila};" % (_lx + 16.65))
grava("executando-a-mao", "\n".join(_o6))


# 6b. executando à mão: versão lateral (grade 2x2)
_S7 = 0.8
_W7 = C * _S7
_PX = _W7 + 0.7
_PY = R * _S7 + 2.0                       # passo vertical entre as duas linhas de quadros
_o7 = []
_o7.append(r"\useasboundingbox (-0.2,-9.5) rectangle (%.2f,%.2f);" % (2 * _PX - 0.5 + 0.2, R * _S7 + 1.0))
for k, sai, novas, antes, depois, tam in _iteracoes():
    ox = ((k - 1) % 2) * _PX
    oy = -((k - 1) // 2) * _PY
    def cel7(l, c, antes=antes, depois=depois, novas=novas):
        if (l, c) in novas:
            return "dorange!45!white", str(depois[(l, c)])
        if (l, c) in antes:
            return azul(antes[(l, c)], 2), str(antes[(l, c)])
        return None, None
    _o7.append(painel(GRADE, ox, oy, _S7, celula=cel7, marcas=False, titulo="iteração %d" % k))
    x0 = ox + sai[1] * _S7
    y0 = oy + (R - 1 - sai[0]) * _S7
    _o7.append(r"\draw[dred, line width=3pt] (%.3f,%.3f) rectangle ++(%s,%s);" % (x0 + 0.03, y0 + 0.03, _S7 - 0.06, _S7 - 0.06))
    nov = "entram %d" % len(novas) if novas else "nenhuma entra"
    _o7.append(r"\node[font=\large, black!80] at (%.3f,%.3f) {sai \texttt{(%d,%d)} $\cdot$ %s $\cdot$ \textbf{fila: %d}};" % (ox + _W7 / 2, oy - 0.55, sai[0], sai[1], nov, tam))
_yl = -_PY - 1.3
_o7.append(r"\draw[fill=dorange!45!white, draw=black!45, line width=0.6pt] (0.2,%.2f) rectangle ++(0.45,0.45);" % (_yl - 0.5))
_o7.append(r"\node[font=\large, anchor=west] at (0.8,%.2f) {recebem distância nesta iteração};" % (_yl - 0.28))
_o7.append(r"\draw[fill=dblue!50!white, draw=black!45, line width=0.6pt] (9.4,%.2f) rectangle ++(0.45,0.45);" % (_yl - 0.5))
_o7.append(r"\node[font=\large, anchor=west] at (10.0,%.2f) {já alcançadas antes};" % (_yl - 0.28))
_o7.append(r"\draw[dred, line width=3pt] (0.2,%.2f) rectangle ++(0.45,0.45);" % (_yl - 1.2))
_o7.append(r"\node[font=\large, anchor=west] at (0.8,%.2f) {sai da fila};" % (_yl - 0.98))
grava("executando-a-mao-lateral", "\n".join(_o7))


# 6c. executando à mão: versão em coluna (quadros um embaixo do outro)
_S8 = 0.7
_W8 = C * _S8
_H8 = R * _S8
_RP8 = _H8 + 0.45
_o8 = []
_o8.append(r"\useasboundingbox (-0.15,%.2f) rectangle (%.2f,%.2f);" % (-(3 * _RP8) - 1.55, _W8 + 5.3, _H8 + 0.15))
for k, sai, novas, antes, depois, tam in _iteracoes():
    oy = -(k - 1) * _RP8
    def cel8(l, c, antes=antes, depois=depois, novas=novas):
        if (l, c) in novas:
            return "dorange!45!white", str(depois[(l, c)])
        if (l, c) in antes:
            return azul(antes[(l, c)], 2), str(antes[(l, c)])
        return None, None
    _o8.append(painel(GRADE, 0, oy, _S8, celula=cel8, marcas=False, fonte=r"\large"))
    x0 = sai[1] * _S8
    y0 = oy + (R - 1 - sai[0]) * _S8
    _o8.append(r"\draw[dred, line width=2.6pt] (%.3f,%.3f) rectangle ++(%s,%s);" % (x0 + 0.03, y0 + 0.03, _S8 - 0.06, _S8 - 0.06))
    nov = "entram %d" % len(novas) if novas else "nenhuma entra"
    _o8.append(r"\node[font=\large, anchor=west, align=left, text width=4.9cm] at (%.2f,%.2f) {\textbf{iteração %d}\\ sai \texttt{(%d,%d)}\\ %s\\ \textbf{fila: %d}};" % (_W8 + 0.4, oy + _H8 / 2, k, sai[0], sai[1], nov, tam))
_yl = -(3 * _RP8) - 0.55
for i, (cor_, txt) in enumerate([("dorange!45!white", "recebem distância"), ("dblue!50!white", "já alcançadas")]):
    x = 0.1 + i * 5.6
    _o8.append(r"\draw[fill=%s, draw=black!45, line width=0.6pt] (%.2f,%.2f) rectangle ++(0.4,0.4);" % (cor_, x, _yl - 0.45))
    _o8.append(r"\node[font=\large, anchor=west] at (%.2f,%.2f) {%s};" % (x + 0.55, _yl - 0.25, txt))
_o8.append(r"\draw[dred, line width=2.6pt] (0.1,%.2f) rectangle ++(0.4,0.4);" % (_yl - 1.05))
_o8.append(r"\node[font=\large, anchor=west] at (0.65,%.2f) {sai da fila};" % (_yl - 0.85))
grava("executando-a-mao-coluna", "\n".join(_o8))
