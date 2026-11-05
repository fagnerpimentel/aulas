"""Gera os .tex das figuras da aula 7 de Navegação (A*), rodando o A* de verdade na grade do exemplo."""
import heapq
import itertools
from collections import deque

TEXTO = [".........", "....#....", "....#.##.", ".G..#..#.", "....#..#S", "........."]
R, C = len(TEXTO), len(TEXTO[0])
OBS = {(r, c) for r in range(R) for c in range(C) if TEXTO[r][c] == "#"}
G, S = (3, 1), (4, 8)
V = [(-1, 0), (1, 0), (0, -1), (0, 1)]          # cima, baixo, esquerda, direita


def h(p):
    return abs(p[0] - G[0]) + abs(p[1] - G[1])


def astar(hf):
    cnt = itertools.count()
    g, pai = {S: 0}, {S: None}
    aberta = [(hf(S), hf(S), next(cnt), S)]
    fechada, log = [], []
    while aberta:
        f, hh, _, n = heapq.heappop(aberta)
        if n in fechada:
            continue
        fechada.append(n)
        novos = []
        if n == G:
            log.append((n, f, novos))
            break
        for dr, dc in V:
            m = (n[0] + dr, n[1] + dc)
            if not (0 <= m[0] < R and 0 <= m[1] < C) or m in OBS:
                continue
            ng = g[n] + 1
            if m not in g or ng < g[m]:
                g[m], pai[m] = ng, n
                heapq.heappush(aberta, (ng + hf(m), hf(m), next(cnt), m))
                novos.append((m, ng, hf(m)))
        log.append((n, f, novos))
    rota, x = [], G
    while x is not None:
        rota.append(x)
        x = pai.get(x)
    return fechada, g, pai, log, rota[::-1]


FE, GG, PAI, LOG, ROTA = astar(h)
FE0, _, _, _, _ = astar(lambda q: 0)


def bfs():
    d, q, ex = {S: 0}, deque([S]), []
    while q:
        n = q.popleft()
        ex.append(n)
        if n == G:
            break
        for dr, dc in V:
            m = (n[0] + dr, n[1] + dc)
            if 0 <= m[0] < R and 0 <= m[1] < C and m not in OBS and m not in d:
                d[m] = d[n] + 1
                q.append(m)
    return ex


EX = bfs()


def descobertas(k):
    """células descobertas (com g definido) após k expansões"""
    desc = {S}
    for n, f, novos in LOG[:k]:
        for m, gg, hh in novos:
            desc.add(m)
    return desc


CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
RODAPE = "\\end{tikzpicture}\n\\end{document}\n"


def xy(lin, col, s, ox=0, oy=0):
    return ox + (col + 0.5) * s, oy + (R - 1 - lin + 0.5) * s


def painel(ox, oy, s, celula=None, rota=None, marcas=True, titulo=None, fonte=r"\Large", rotulos=True):
    out, nums = [], []
    for lin in range(R):
        for col in range(C):
            x0, y0 = ox + col * s, oy + (R - 1 - lin) * s
            fill, txt = (None, None)
            if (lin, col) in OBS:
                fill = "black!80"
            elif celula:
                fill, txt = celula(lin, col)
            f = "fill=%s, " % fill if fill else "fill=white, "
            out.append(r"\draw[%sdraw=black!30, line width=0.4pt] (%.3f,%.3f) rectangle ++(%.3f,%.3f);" % (f, x0, y0, s, s))
            if txt is not None and (lin, col) not in OBS:
                x, y = xy(lin, col, s, ox, oy)
                nums.append(r"\node[font=%s, black!80] at (%.3f,%.3f) {%s};" % (fonte, x, y, txt))
    out.append(r"\draw[black!80, line width=1.2pt] (%.3f,%.3f) rectangle (%.3f,%.3f);" % (ox, oy, ox + C * s, oy + R * s))
    if rota:
        pts = " -- ".join("(%.3f,%.3f)" % xy(l, c, s, ox, oy) for l, c in rota)
        out.append(r"\draw[dorange, line width=%.1fpt, line cap=round, line join=round, -{Stealth[length=%.1fmm]}] %s;" % (2.6 if s > 0.8 else 1.8, 3 if s > 0.8 else 2, pts))
    out.extend(nums)
    if marcas:
        for (l, c), nome, cor in ((S, "S", "dgreen"), (G, "G", "dred")):
            x, y = xy(l, c, s, ox, oy)
            out.append(r"\node[circle, fill=%s, text=white, font=\bfseries%s, inner sep=1pt, minimum size=%.2fcm] at (%.3f,%.3f) {%s};" % (cor, fonte, s * 0.72, x, y, nome))
    if titulo:
        out.append(r"\node[font=\Large\bfseries, black!75, text width=%.1fcm, align=center] at (%.3f,%.3f) {%s};" % (C * s + 1, ox + C * s / 2, oy + R * s + 0.6, titulo))
    return "\n".join(out)


def grava(nome, corpo):
    with open(nome + ".tex", "w") as f:
        f.write(CAB + corpo + "\n" + RODAPE)


AZ, LA = "dblue!28!white", "dorange!35!white"

# ---------------------------------------------------------------- 1. quantas células cada busca explora
ex_set, fe_set = set(EX), set(FE)
grava("wavefront-vs-astar",
      painel(0, 0, 1.0, lambda l, c: (AZ if (l, c) in ex_set else None, None), ROTA, titulo=r"Wavefront / Dijkstra: %d células" % len(EX)) + "\n" +
      painel(10.4, 0, 1.0, lambda l, c: (AZ if (l, c) in fe_set else None, None), ROTA, titulo=r"A*: %d células" % len(FE)) + "\n" +
      r"\fill[%s] (0.2,-1.0) rectangle ++(0.55,0.4); \node[font=\large, anchor=west] at (0.9,-0.8) {célula \textbf{expandida} até alcançar G};" % AZ + "\n" +
      r"\draw[dorange, line width=2.4pt, -{Stealth[length=2.6mm]}] (10.6,-0.8) -- ++(0.7,0); \node[font=\large, anchor=west] at (11.5,-0.8) {caminho encontrado (10 passos nos dois)};")

# ---------------------------------------------------------------- 2. g, h e f de uma célula
gg_, hh_ = GG[(5, 5)], h((5, 5))
grava("g-h-f", r"""
\node[circle, fill=dgreen, text=white, font=\Large\bfseries, minimum size=1.1cm] (s) at (1.5,3.4) {S};
\node[circle, draw=dblue, fill=dblue!15, line width=1.8pt, font=\Large\bfseries, minimum size=1.5cm] (n) at (9.0,3.4) {$N$};
\node[circle, fill=dred, text=white, font=\Large\bfseries, minimum size=1.1cm] (g) at (16.5,3.4) {G};
\draw[dorange, line width=3pt, -{Stealth[length=3.4mm]}] (s) -- (n);
\draw[dblue, dashed, line width=3pt, -{Stealth[length=3.4mm]}] (n) -- (g);
\draw[decorate, decoration={brace, amplitude=9pt}, dorange, line width=1.6pt] (1.0,4.2) -- (8.5,4.2);
\node[font=\Large\bfseries, dorange, text width=8cm, align=center] at (4.75,5.5) {g = %d};
\node[font=\large, dorange, text width=8cm, align=center] at (4.75,4.85) {custo \textbf{já percorrido} (real)};
\draw[decorate, decoration={brace, amplitude=9pt, mirror}, dblue, line width=1.6pt] (9.5,2.6) -- (16.0,2.6);
\node[font=\Large\bfseries, dblue, text width=7cm, align=center] at (12.75,1.3) {h = %d};
\node[font=\large, dblue, text width=7cm, align=center] at (12.75,0.65) {\textbf{estimativa} do que falta};
\node[dbox, draw=black!70, fill=white, line width=1.8pt, text width=7.2cm, minimum height=1.6cm, font=\Huge\bfseries] at (4.75,1.2) {f = g + h = %d};
\node[font=\large, black!70] at (4.75,0.1) {custo total \textbf{estimado} do caminho por $N$};
""" % (gg_, hh_, gg_ + hh_))

# ---------------------------------------------------------------- 3. heurística: distância de Manhattan
def cel_h(l, c):
    v = h((l, c))
    return "dblue!%d!white" % int(8 + 50 * v / 14), v
rx = " -- ".join("(%.3f,%.3f)" % p for p in (xy(S[0], S[1], 1.15), xy(S[0], G[1], 1.15), xy(G[0], G[1], 1.15)))
grava("heuristica-manhattan",
      painel(0, 0, 1.15, cel_h, None) + "\n" +
      r"\node[font=\Large, anchor=west, text width=7.4cm] at (11.0,5.6) {\textbf{h} = distância de Manhattan até G, contando \textbf{linhas e colunas} e \textbf{ignorando as paredes}};" + "\n" +
      r"\node[font=\Large, dgreen, anchor=west, text width=7.4cm] at (11.0,3.0) {em S: \textbf{h = %d}, mas o caminho real tem \textbf{%d} passos};" % (h(S), len(ROTA) - 1) + "\n" +
      r"\node[font=\Large\bfseries, dgreen, anchor=west, text width=7.4cm] at (11.0,1.3) {h nunca passa do custo real};")

# ---------------------------------------------------------------- 4. fila x lista aberta (após 7 expansões)
K = 7
abertas = [(m, GG[m], h(m)) for m in descobertas(K) if m not in FE[:K]]
ordem_chegada = []
for n, f, novos in LOG[:K]:
    for m, gg, hh in novos:
        if m not in ordem_chegada and m in [a[0] for a in abertas]:
            ordem_chegada.append(m)
ordem_chegada = [m for m in ordem_chegada if m in [a[0] for a in abertas]]
tabela = {a[0]: a for a in abertas}
seq = {m: i for i, m in enumerate(ordem_chegada)}
por_f = sorted(abertas, key=lambda a: (a[1] + a[2], a[2], seq[a[0]]))
def cartao(x, y, cor, linha1, linha2, forte=False):
    st = "line width=2.4pt" if forte else "line width=1.4pt"
    return r"\node[dbox, draw=%s, fill=%s!%d, %s, text width=5.6cm, minimum height=1.3cm, font=\large] at (%.2f,%.2f) {%s\\ %s};" % (cor, cor, 14 if forte else 6, st, x, y, linha1, linha2)
corpo = [r"\node[font=\Large\bfseries, black!75] at (9.5,8.6) {depois de %d expansões};" % K,
         r"\node[font=\Large\bfseries, dblue] at (3.4,7.7) {fila (wavefront)};",
         r"\node[font=\Large\bfseries, dorange] at (15.6,7.7) {lista aberta (A*)};"]
for i, m in enumerate(ordem_chegada):
    a = tabela[m]
    corpo.append(cartao(3.4, 6.5 - i * 1.5, "dblue", r"\textbf{(%d,%d)}" % m, "chegou %dª" % (i + 1), i == 0))
for i, a in enumerate(por_f):
    corpo.append(cartao(15.6, 6.5 - i * 1.5, "dorange", r"\textbf{(%d,%d)}" % a[0], r"$f=%d$ \quad ($g=%d$, $h=%d$)" % (a[1] + a[2], a[1], a[2]), i == 0))
corpo.append(r"\node[font=\large\bfseries, dblue, anchor=west, text width=2.4cm, align=left] at (6.6,6.5) {$\leftarrow$ sai a mais antiga};")
corpo.append(r"\node[font=\large\bfseries, dorange, anchor=east, text width=2.4cm, align=right] at (12.4,6.5) {sai a de menor $f$ $\rightarrow$};")
grava("lista-aberta", "\n".join(corpo))

# ---------------------------------------------------------------- 5. etapas da busca A*
paineis = []
for i, k in enumerate((3, 7, 12, len(FE))):
    fe_k = set(FE[:k])
    ab = descobertas(k) - fe_k
    atual = FE[k - 1]
    def cel(l, c, fe_k=fe_k, ab=ab):
        if (l, c) in fe_k: return AZ, None
        if (l, c) in ab: return LA, None
        return None, None
    ox = i * 5.3
    paineis.append(painel(ox, 0, 0.5, cel, ROTA if k == len(FE) else None, titulo=r"após %d expansões" % k, fonte=r"\normalsize"))
    x0 = ox + atual[1] * 0.5; y0 = (R - 1 - atual[0]) * 0.5
    paineis.append(r"\draw[black, line width=2.2pt] (%.3f,%.3f) rectangle ++(0.5,0.5);" % (x0, y0))
paineis.append(r"\fill[%s] (0.0,-0.9) rectangle ++(0.45,0.35); \node[font=\large, anchor=west] at (0.55,-0.72) {lista fechada};" % AZ)
paineis.append(r"\fill[%s] (4.2,-0.9) rectangle ++(0.45,0.35); \node[font=\large, anchor=west] at (4.75,-0.72) {lista aberta};" % LA)
paineis.append(r"\draw[black, line width=2.2pt] (9.0,-0.9) rectangle ++(0.45,0.35); \node[font=\large, anchor=west] at (9.55,-0.72) {última expandida};")
grava("astar-etapas", "\n".join(paineis))

# ---------------------------------------------------------------- 6. pais e caminho
setas = []
for n in FE:
    p = PAI.get(n)
    if p is None: continue
    x1, y1 = xy(n[0], n[1], 1.15); x2, y2 = xy(p[0], p[1], 1.15)
    dx, dy = x2 - x1, y2 - y1
    setas.append(r"\draw[black!55, line width=1.6pt, -{Stealth[length=2.4mm]}] (%.3f,%.3f) -- (%.3f,%.3f);" % (x1 + 0.18 * dx, y1 + 0.18 * dy, x1 + 0.78 * dx, y1 + 0.78 * dy))
grava("astar-caminho",
      painel(0, 0, 1.15, lambda l, c: (AZ if (l, c) in fe_set else None, None), ROTA, fonte=r"\normalsize") + "\n" + "\n".join(setas) + "\n" +
      r"\node[font=\Large, anchor=west, text width=7.4cm] at (11.0,5.4) {\textbf{seta cinza}: aponta para o \textbf{pai} da célula (de onde veio o menor $g$)};" + "\n" +
      r"\node[font=\Large, dorange, anchor=west, text width=7.4cm] at (11.0,3.0) {\textbf{laranja}: seguindo os pais de \textbf{G} até \textbf{S} e invertendo};")


# ---------------------------------------------------------------- 7. as três estruturas, depois de 7 expansões
K7 = 7
gk, paik = {S: 0}, {S: None}
for n, f, novos in LOG[:K7]:
    for m, gg, hh in novos:
        gk[m], paik[m] = gg, n
fe7 = set(FE[:K7])
ab7 = [(m, gk[m], h(m)) for m in gk if m not in fe7]
ab7.sort(key=lambda a: (a[1] + a[2], a[2]))
SC = 0.5
cart = []
# (x0, largura, título, cor, legenda)
CARDS = [(0.0, 4.4, "Lista aberta", "dorange", r"ordenada por $f$"),
         (4.8, 5.6, "Lista fechada", "dblue", "células já expandidas"),
         (10.8, 8.4, "Árvore de busca", "dgreen", r"cada célula guarda o \textbf{pai} e $g$, $h$, $f$")]
for x0, wd, t, cor, lg in CARDS:
    cart.append(r"\draw[%s, line width=1.6pt, rounded corners=6pt, fill=dcream] (%.2f,0.6) rectangle (%.2f,6.6);" % (cor, x0, x0 + wd))
    cart.append(r"\node[font=\Large\bfseries, %s] at (%.2f,7.2) {%s};" % (cor, x0 + wd / 2, t))
    cart.append(r"\node[font=\normalsize, text width=%.1fcm, align=center] at (%.2f,1.25) {%s};" % (wd - 0.4, x0 + wd / 2, lg))
# 1: lista aberta
linhas = r"\\[6pt] ".join(r"\textbf{(%d,%d)} \ $f=%d$" % (m[0], m[1], g_ + h_) for m, g_, h_ in ab7)
cart.append(r"\node[font=\large, text width=3.8cm, align=center] at (2.2,3.8) {%s};" % linhas)
# 2: lista fechada
ox2, oy = 4.8 + (5.6 - C * SC) / 2, 2.2
cart.append(painel(ox2, oy, SC, lambda l, c: (AZ if (l, c) in fe7 else None, None), fonte=r"\scriptsize"))
# 3: árvore de busca (g na grade + setas para o pai) e um nó ampliado
ox3 = 11.1
cart.append(painel(ox3, oy, SC, lambda l, c: (AZ if (l, c) in fe7 else (LA if (l, c) in gk else None), None), fonte=r"\scriptsize"))
for m, p in paik.items():
    if p is None: continue
    x1, y1 = xy(m[0], m[1], SC, ox3, oy); x2, y2 = xy(p[0], p[1], SC, ox3, oy)
    dx, dy = x2 - x1, y2 - y1
    cart.append(r"\draw[black!70, line width=1.3pt, -{Stealth[length=1.6mm]}] (%.3f,%.3f) -- (%.3f,%.3f);" % (x1 + 0.2 * dx, y1 + 0.2 * dy, x1 + 0.85 * dx, y1 + 0.85 * dy))
NO = (1, 8)
xn, yn = xy(NO[0], NO[1], SC, ox3, oy)
cart.append(r"\draw[dgreen, line width=2.2pt] (%.3f,%.3f) rectangle ++(%.2f,%.2f);" % (xn - SC / 2, yn - SC / 2, SC, SC))
cart.append(r"\node[dbox, draw=dgreen, fill=white, line width=1.8pt, text width=2.7cm, minimum height=3.1cm, font=\large, align=left] (no) at (17.65,%.3f) {\textbf{\textcolor{dgreen}{nó (%d,%d)}}\\[4pt] pai: (%d,%d)\\ $g=%d$\\ $h=%d$\\ $f=g+h=%d$};" % (yn, NO[0], NO[1], paik[NO][0], paik[NO][1], gk[NO], h(NO), gk[NO] + h(NO)))
cart.append(r"\draw[dgreen, line width=1.8pt, -{Stealth[length=2.8mm]}] (%.3f,%.3f) -- (no.west);" % (xn + SC / 2, yn))
cart.append(r"\node[font=\large, black!75] at (9.6,-0.2) {depois de %d expansões do exemplo: \colorbox{dblue!28!white}{ lista fechada } \ \colorbox{dorange!35!white}{ lista aberta }};" % K7)
grava("estruturas-dados", "\n".join(cart))


# ---------------------------------------------------------------- 8. os seis casos de borda (uma linha)
def mini(ox, oy, s, rows, cols, obst=(), fills=None, marcas=()):
    out = []
    fills = fills or {}
    for r in range(rows):
        for c in range(cols):
            f = "black!80" if (r, c) in obst else fills.get((r, c), "white")
            out.append(r"\draw[fill=%s, draw=black!30, line width=0.4pt] (%.3f,%.3f) rectangle ++(%.3f,%.3f);" % (f, ox + c * s, oy + (rows - 1 - r) * s, s, s))
    out.append(r"\draw[black!80, line width=1pt] (%.3f,%.3f) rectangle (%.3f,%.3f);" % (ox, oy, ox + cols * s, oy + rows * s))
    for (r, c), nome, cor in marcas:
        out.append(r"\node[circle, fill=%s, text=white, font=\bfseries\normalsize, inner sep=1pt, minimum size=%.2fcm] at (%.3f,%.3f) {%s};" % (cor, s * 0.8, ox + (c + 0.5) * s, oy + (rows - 1 - r + 0.5) * s, nome))
    return "\n".join(out)

CW_, CH_, ESP_ = 3.55, 4.9, 3.75
def cartao(i, titulo, cor):
    x0 = i * ESP_
    return x0, 0.0, [
        r"\draw[%s, line width=1.6pt, rounded corners=6pt, fill=dcream] (%.2f,0) rectangle (%.2f,%.2f);" % (cor, x0, x0 + CW_, CH_),
        r"\node[font=\normalsize\bfseries, %s, text width=3.2cm, align=center] at (%.2f,%.2f) {%s};" % (cor, x0 + CW_ / 2, CH_ - 0.8, titulo)]

corpo = []
SC8 = 0.4
GX = 0.25                      # margem esquerda da grade dentro do cartão
GY = 0.9
# 1 sem caminho
x0, y0, c = cartao(0, "Sem caminho", "dred")
corpo += c
corpo.append(mini(x0 + GX, y0 + 1.4, SC8, 4, 8, obst={(0, 5), (1, 5), (2, 5), (3, 5), (1, 6), (2, 6)}, fills={(1, 7): "dblue!28!white", (2, 7): "dblue!28!white", (0, 7): "dblue!28!white", (3, 7): "dblue!28!white", (0, 6): "dblue!28!white", (3, 6): "dblue!28!white"}, marcas=[((1, 1), "G", "dred"), ((3, 7), "S", "dgreen")]))
corpo.append(r"\node[font=\footnotesize, text width=3.2cm, align=center] at (%.2f,0.85) {lista aberta \textbf{vazia}: \textbf{falhou}};" % (x0 + CW_ / 2))
# 2 obstáculo
x0, y0, c = cartao(1, "Início ou objetivo em obstáculo", "dorange")
corpo += c
corpo.append(mini(x0 + GX, y0 + 1.4, SC8, 4, 8, obst={(1, 2), (1, 3), (2, 3), (2, 4), (1, 4)}, marcas=[((1, 3), "G", "dred"), ((3, 7), "S", "dgreen")]))
gx, gy = x0 + GX + 3.5 * SC8, y0 + 1.4 + (4 - 1 - 1 + 0.5) * SC8
for _lw, _cor in ((6, "white"), (3.5, "dred")):
    corpo.append(r"\draw[%s, line width=%spt, line cap=round] (%.3f,%.3f) -- ++(0.4,0.4) (%.3f,%.3f) -- ++(0.4,-0.4);" % (_cor, _lw, gx + 0.12, gy + 0.03, gx + 0.12, gy + 0.43))
corpo.append(r"\node[font=\footnotesize, text width=3.2cm, align=center] at (%.2f,0.85) {\textbf{verifique} antes};" % (x0 + CW_ / 2))
# 3 empates
x0, y0, c = cartao(2, r"Empates em $f$", "dblue")
corpo += c
corpo.append(r"\node[dbox, draw=dblue, fill=dblue!14, line width=2.2pt, text width=2.8cm, minimum height=1.1cm, font=\normalsize] at (%.2f,2.9) {\textbf{(3,6)}: $f=10$\\ $h=5$ \ $\leftarrow$ \textbf{sai}};" % (x0 + CW_ / 2))
corpo.append(r"\node[dbox, draw=dblue, fill=white, line width=1.4pt, text width=2.8cm, minimum height=1.1cm, font=\normalsize] at (%.2f,1.5) {\textbf{(5,5)}: $f=10$\\ $h=6$};" % (x0 + CW_ / 2))
# 4 heurística que superestima
x0, y0, c = cartao(3, "Heurística que superestima", "dred")
corpo += c
corpo.append(r"\node[circle, fill=dgreen, text=white, font=\bfseries\normalsize, minimum size=0.65cm] (sa) at (%.2f,2.5) {S};" % (x0 + 0.65))
corpo.append(r"\node[circle, fill=dred, text=white, font=\bfseries\normalsize, minimum size=0.65cm] (ga) at (%.2f,2.5) {G};" % (x0 + 2.9))
corpo.append(r"\draw[black!55, dashed, line width=1.8pt, -{Stealth[length=2.2mm]}] (sa) to[bend left=32] node[above, font=\footnotesize, black, pos=0.5, yshift=1pt] {6 (ótimo)} (ga);")
corpo.append(r"\draw[dorange, line width=2.6pt, -{Stealth[length=2.6mm]}] (sa) to[bend right=32] node[below, font=\footnotesize\bfseries, dorange, pos=0.5] {8 (escolhido)} (ga);")
# 5 oito vizinhos
x0, y0, c = cartao(4, "8 vizinhos", "dgreen")
corpo += c
corpo.append(mini(x0 + GX, y0 + 1.4, SC8, 4, 8, marcas=[((3, 1), "S", "dgreen"), ((0, 6), "G", "dred")]))
pts = " -- ".join("(%.3f,%.3f)" % (x0 + GX + (cc + 0.5) * SC8, y0 + 1.4 + (4 - 1 - rr + 0.5) * SC8) for rr, cc in [(3, 1), (2, 2), (1, 3), (0, 4), (0, 5), (0, 6)])
corpo.append(r"\draw[dorange, line width=2.2pt, line cap=round, line join=round, -{Stealth[length=2.2mm]}] %s;" % pts)
corpo.append(r"\node[font=\footnotesize, text width=3.2cm, align=center] at (%.2f,0.85) {diagonal custa $\sqrt{2}$};" % (x0 + CW_ / 2))
# 6 custos diferentes
x0, y0, c = cartao(5, "Terrenos de custos diferentes", "dorange")
corpo += c
terr = [("S", "white", ""), ("asfalto", "black!15", "1"), ("asfalto", "black!15", "1"), ("areia", "dorange!25!white", "3"), ("G", "white", "1")]
gg_ = 0
for i, (nome, cor, custo) in enumerate(terr):
    gg_ += int(custo) if custo else 0
    xx = x0 + 0.2 + i * 0.63
    corpo.append(r"\draw[fill=%s, draw=black!45, line width=0.8pt] (%.2f,2.0) rectangle ++(0.62,0.62);" % (cor, xx))
    if nome in ("S", "G"):
        corpo.append(r"\node[circle, fill=%s, text=white, font=\bfseries\small, minimum size=0.5cm, inner sep=0.5pt] at (%.2f,2.31) {%s};" % ("dgreen" if nome == "S" else "dred", xx + 0.31, nome))
    corpo.append(r"\node[font=\small\bfseries, dorange] at (%.2f,2.95) {%s};" % (xx + 0.31, ("+" + custo) if custo else ""))
    corpo.append(r"\node[font=\footnotesize, dblue] at (%.2f,1.65) {$g{=}%d$};" % (xx + 0.31, gg_))
corpo.append(r"\node[font=\scriptsize] at (%.2f,1.15) {\colorbox{black!15}{ asfalto } \ \colorbox{dorange!25!white}{ areia }};" % (x0 + CW_ / 2))
corpo.append(r"\node[font=\footnotesize, text width=3.2cm, align=center] at (%.2f,0.55) {$g$ soma os \textbf{custos reais}};" % (x0 + CW_ / 2))
grava("casos-de-borda", "\n".join(corpo))

print("expandidas:", len(FE), "bfs:", len(EX), "caminho:", len(ROTA) - 1, "aberta@7:", por_f)
