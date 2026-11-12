"""Gera os .tex das figuras da aula 8 de Navegação (RRT), rodando o RRT de verdade (rrt_sim.py, semente fixa)."""
import math, random
from rrt_sim import *

CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
RODA = "\n\\end{tikzpicture}\n\\end{document}\n"


def grava(nome, corpo):
    open(nome + ".tex", "w").write(CAB + corpo.strip("\n") + RODA)


def X(x, s, ox): return ox + x * s
def Y(y, s, oy): return oy + y * s


def mundo(s, ox, oy, obs=OBS, w=W, h=H, S_=S, G_=G, marcas=True, fundo=True):
    o = [r"\draw[line width=1.2pt, %s] (%.2f,%.2f) rectangle (%.2f,%.2f);" % ("fill=white" if fundo else "fill=none", ox, oy, ox + w * s, oy + h * s)]
    for x0, y0, x1, y1 in obs:
        o.append(r"\draw[line width=1pt, draw=black!70, fill=dshade] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (X(x0, s, ox), Y(y0, s, oy), X(x1, s, ox), Y(y1, s, oy)))
    if marcas:
        o.append(r"\fill[dgreen] (%.2f,%.2f) circle (%.2f); \node[font=\small\bfseries, text=dgreen, anchor=south] at (%.2f,%.2f) {S};" % (X(S_[0], s, ox), Y(S_[1], s, oy), 0.16, X(S_[0], s, ox), Y(S_[1], s, oy) + 0.16))
        o.append(r"\fill[dred] (%.2f,%.2f) circle (%.2f); \node[font=\small\bfseries, text=dred, anchor=south] at (%.2f,%.2f) {G};" % (X(G_[0], s, ox), Y(G_[1], s, oy), 0.16, X(G_[0], s, ox), Y(G_[1], s, oy) + 0.16))
    return "\n".join(o)


def arvore(nos, pai, s, ox, oy, cor="dblue", lw=0.8, r=0.05, ate=None):
    n = len(nos) if ate is None else ate
    o = []
    for k in range(1, n):
        a, b = nos[pai[k]], nos[k]
        o.append(r"\draw[%s, line width=%.1fpt] (%.2f,%.2f) -- (%.2f,%.2f);" % (cor, lw, X(a[0], s, ox), Y(a[1], s, oy), X(b[0], s, ox), Y(b[1], s, oy)))
    for k in range(n):
        o.append(r"\fill[%s] (%.2f,%.2f) circle (%.2f);" % (cor, X(nos[k][0], s, ox), Y(nos[k][1], s, oy), r))
    return "\n".join(o)


def caminho_tikz(cam, s, ox, oy, cor="dorange", lw=2.6, dash=""):
    pts = " -- ".join("(%.2f,%.2f)" % (X(p[0], s, ox), Y(p[1], s, oy)) for p in cam)
    return r"\draw[%s, line width=%.1fpt%s] %s;" % (cor, lw, dash, pts)


def n_nos_ate(log, it):
    return 1 + sum(1 for e in log[:it] if e[4])


SEED = 1
NOS, PAI, LOG, ACHOU, CAM = rrt(seed=SEED)
NIT = len(LOG)
print("semente", SEED, "iterações", NIT, "nós", len(NOS), "comprimento", round(comprimento(CAM), 1))

# ----------------------------------------------------------------- 1. grade x arvore
s = 0.5
cel = 0.5
nx, ny = int(W / cel), int(H / cel)
g = [mundo(s, 0, 0)]
for i in range(1, nx):
    g.append(r"\draw[black!22, line width=0.3pt] (%.2f,0) -- (%.2f,%.2f);" % (i * cel * s, i * cel * s, H * s))
for j in range(1, ny):
    g.append(r"\draw[black!22, line width=0.3pt] (0,%.2f) -- (%.2f,%.2f);" % (j * cel * s, W * s, j * cel * s))
g.append(mundo(s, 0, 0, fundo=False))
g.append(r"\node[font=\Large\bfseries, text=dblue] at (5.0,6.9) {grade};")
g.append(r"\node[font=\large, text width=10cm, align=center] at (5.0,-0.9) {\textbf{%d células}: um valor para cada uma};" % (nx * ny))
ox2 = 11.5
g.append(mundo(s, ox2, 0))
g.append(arvore(NOS, PAI, s, ox2, 0))
g.append(caminho_tikz(CAM, s, ox2, 0))
g.append(r"\node[font=\Large\bfseries, text=dorange] at (%.2f,6.9) {RRT};" % (ox2 + 5.0))
g.append(r"\node[font=\large, text width=10cm, align=center] at (%.2f,-0.9) {\textbf{%d nós}, no espaço contínuo};" % (ox2 + 5.0, len(NOS)))
g.append(r"\node[font=\large, text width=21cm, align=center] at (10.75,-2.2) {com 6 dimensões e a mesma resolução, a grade teria $%d^6\approx 4\times10^{9}$ células};" % nx)
grava("grade-vs-arvore", "\n".join(g))

# ----------------------------------------------------------------- 2. rrt crescendo
s = 0.5
pan = [(15, 0, 7.6), (50, 10.8, 7.6), (120, 0, 0), (NIT, 10.8, 0)]
g = []
for it, ox, oy in pan:
    n = n_nos_ate(LOG, it)
    g.append(mundo(s, ox, oy))
    g.append(arvore(NOS, PAI, s, ox, oy, ate=n))
    if it == NIT:
        g.append(caminho_tikz(CAM, s, ox, oy))
    g.append(r"\node[font=\large\bfseries, anchor=north west, fill=white, inner sep=2pt] at (%.2f,%.2f) {%d iterações, %d nós};" % (ox + 0.1, oy + 6.0 - 0.1, it, n))
grava("rrt-crescendo", "\n".join(g))

# ----------------------------------------------------------------- 3. vies de Voronoi
it = 60
n = n_nos_ate(LOG, it)
nos60, pai60 = NOS[:n], PAI[:n]
rnd = random.Random(7)
cont = [0] * n
M = 20000
for _ in range(M):
    qx, qy = rnd.uniform(0, W), rnd.uniform(0, H)
    k = min(range(n), key=lambda i: (nos60[i][0] - qx) ** 2 + (nos60[i][1] - qy) ** 2)
    cont[k] += 1
prob = [c / M for c in cont]
s = 0.75
g = [mundo(s, 0, 0)]
for k in range(1, n):
    a, b = nos60[pai60[k]], nos60[k]
    g.append(r"\draw[dblue!60, line width=0.8pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (X(a[0], s, 0), Y(a[1], s, 0), X(b[0], s, 0), Y(b[1], s, 0)))
mx = max(prob)
for k in range(n):
    r_ = 0.06 + 0.42 * math.sqrt(prob[k] / mx)
    cor = "dorange" if prob[k] > 0.6 * mx else "dblue"
    g.append(r"\fill[%s, opacity=0.8] (%.2f,%.2f) circle (%.2f);" % (cor, X(nos60[k][0], s, 0), Y(nos60[k][1], s, 0), r_))
top = sorted(range(n), key=lambda i: -prob[i])[:3]
grava("voronoi-vies", "\n".join(g))
print("voronoi: top prob", [round(prob[i], 3) for i in top], "média", round(1 / n, 3))

# ----------------------------------------------------------------- 4. um passo
def painel_passo(ox, qr, titulo, legenda):
    qn_ = (3.0, 3.0)
    d = math.dist(qn_, qr)
    delta = 2.2
    qnew = estende(qn_, qr, delta)
    o = []
    o.append(r"\draw[line width=1.2pt, fill=white] (%.2f,0) rectangle (%.2f,6.4);" % (ox, ox + 9.6))
    # arvore existente
    pts = [(1.0, 1.4), (1.8, 2.3), (3.0, 3.0), (2.2, 4.2), (3.9, 1.6), (1.2, 4.6)]
    for a, b in [(0, 1), (1, 2), (2, 3), (2, 4), (3, 5)]:
        o.append(r"\draw[dblue, line width=1.2pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + pts[a][0], pts[a][1], ox + pts[b][0], pts[b][1]))
    for p in pts:
        o.append(r"\fill[dblue] (%.2f,%.2f) circle (0.09);" % (ox + p[0], p[1]))
    o.append(r"\fill[dblue] (%.2f,%.2f) circle (0.17); \node[font=\large\bfseries, text=dblue, anchor=east] at (%.2f,%.2f) {$q_{\mathrm{near}}$};" % (ox + qn_[0], qn_[1], ox + qn_[0] - 0.25, qn_[1] - 0.15))
    o.append(r"\draw[dred, line width=2.4pt] (%.2f,%.2f) -- (%.2f,%.2f) (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + qr[0] - 0.17, qr[1] - 0.17, ox + qr[0] + 0.17, qr[1] + 0.17, ox + qr[0] - 0.17, qr[1] + 0.17, ox + qr[0] + 0.17, qr[1] - 0.17))
    o.append(r"\node[font=\large\bfseries, text=dred, anchor=south west] at (%.2f,%.2f) {$q_{\mathrm{rand}}$};" % (ox + qr[0] + 0.1, qr[1] + 0.15))
    o.append(r"\draw[dred, dashed, line width=1.4pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + qn_[0], qn_[1], ox + qr[0], qr[1]))
    o.append(r"\draw[dgreen, line width=3pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + qn_[0], qn_[1], ox + qnew[0], qnew[1]))
    o.append(r"\fill[dgreen] (%.2f,%.2f) circle (0.17); \node[font=\large\bfseries, text=dgreen, anchor=north] at (%.2f,%.2f) {$q_{\mathrm{new}}$};" % (ox + qnew[0], qnew[1], ox + qnew[0], qnew[1] - 0.22))
    o.append(r"\node[font=\Large\bfseries, anchor=south] at (%.2f,6.5) {%s};" % (ox + 4.8, titulo))
    o.append(r"\node[font=\large, text width=9.4cm, align=center] at (%.2f,-0.8) {%s};" % (ox + 4.8, legenda))
    return "\n".join(o)


g = [painel_passo(0, (7.4, 5.0), "$q_{\\mathrm{rand}}$ longe", "$q_{\\mathrm{new}}$ fica a um \\textbf{passo} $\\delta$ de $q_{\\mathrm{near}}$"),
     painel_passo(11.0, (4.5, 3.9), "$q_{\\mathrm{rand}}$ perto", "se está a menos de $\\delta$, $q_{\\mathrm{new}}=q_{\\mathrm{rand}}$")]
grava("um-passo", "\n".join(g))

# ----------------------------------------------------------------- 5. colisao no segmento
def pts_seg(a, b, esp):
    d = math.dist(a, b)
    n = max(1, int(d / esp))
    return [(a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n) for i in range(n + 1)]


OB = (3.6, 0.8, 5.0, 4.4)
def dentro(p): return OB[0] <= p[0] <= OB[2] and OB[1] <= p[1] <= OB[3]
g = []
for ox, a, b, tit, leg in [(0, (1.6, 2.6), (3.0, 3.6), "segmento livre", "todos os pontos livres: \\textbf{aceita} $q_{\\mathrm{new}}$"),
                           (10.8, (1.6, 2.6), (6.6, 2.2), "segmento com colisão", "um ponto cai no obstáculo: \\textbf{rejeita} $q_{\\mathrm{new}}$")]:
    g.append(r"\draw[line width=1.2pt, fill=white] (%.2f,0) rectangle (%.2f,5.4);" % (ox, ox + 9.4))
    g.append(r"\draw[line width=1pt, draw=black!70, fill=dshade] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ox + OB[0], OB[1], ox + OB[2], OB[3]))
    pts = pts_seg(a, b, 0.5)
    prim = next((i for i, p in enumerate(pts) if dentro(p)), None)
    cor = "dgreen" if prim is None else "dred"
    g.append(r"\draw[%s, line width=2.2pt%s] (%.2f,%.2f) -- (%.2f,%.2f);" % (cor, "" if prim is None else ", dashed", ox + a[0], a[1], ox + b[0], b[1]))
    for i, p in enumerate(pts):
        if prim is not None and i == prim:
            g.append(r"\draw[dred, line width=2.6pt] (%.2f,%.2f) -- ++(0.18,0.18) (%.2f,%.2f) -- ++(0.18,-0.18) (%.2f,%.2f) -- ++(-0.18,0.18) (%.2f,%.2f) -- ++(-0.18,-0.18);" % ((ox + p[0], p[1]) * 4))
        elif prim is None or i < prim:
            g.append(r"\fill[%s] (%.2f,%.2f) circle (0.1);" % ("dgreen" if prim is None else "dblue", ox + p[0], p[1]))
        else:
            g.append(r"\draw[dblue, line width=0.8pt] (%.2f,%.2f) circle (0.09);" % (ox + p[0], p[1]))
    g.append(r"\fill[dblue] (%.2f,%.2f) circle (0.17); \node[font=\large\bfseries, text=dblue, anchor=east] at (%.2f,%.2f) {$q_{\mathrm{near}}$};" % (ox + a[0], a[1], ox + a[0] - 0.22, a[1]))
    g.append(r"\fill[%s] (%.2f,%.2f) circle (0.17); \node[font=\large\bfseries, text=%s, anchor=west] at (%.2f,%.2f) {$q_{\mathrm{new}}$};" % (cor, ox + b[0], b[1], cor, ox + b[0] + 0.22, b[1]))
    g.append(r"\node[font=\Large\bfseries, anchor=south] at (%.2f,5.5) {%s};" % (ox + 4.7, tit))
    g.append(r"\node[font=\large, text width=9.4cm, align=center] at (%.2f,-0.8) {%s};" % (ox + 4.7, leg))
g.append(r"\node[font=\large, text width=20cm, align=center] at (10.1,-2.0) {o espaçamento entre os pontos deve ser \textbf{menor que o menor obstáculo}, para a verificação não \textbf{pular} por cima dele};")
grava("colisao-segmento", "\n".join(g))

# ----------------------------------------------------------------- 6. exemplo a mao (mundo 10x6)
OBM = [(4.5, 1.5, 5.5, 6.0)]
SM, GM, DM = (1.0, 3.0), (9.0, 3.0), 1.5
QRM = [(6.0, 5.0), (3.0, 0.6), (7.0, 3.2), (6.5, 2.5), (4.0, 1.0), (6.0, 0.8), (8.0, 1.5), (9.5, 2.5), (9.0, 3.0)]
nm, pm, tabela = [SM], [None], []
for it, q in enumerate(QRM, 1):
    i = min(range(len(nm)), key=lambda k: (nm[k][0] - q[0]) ** 2 + (nm[k][1] - q[1]) ** 2)
    qn = estende(nm[i], q, DM)
    ok = livre_pt(qn, OBM) and livre_seg(nm[i], qn, OBM)
    tabela.append((it, q, i, qn, ok))
    if ok:
        nm.append(qn); pm.append(i)
    if ok and math.dist(qn, GM) <= 0.05:
        break
print("exemplo à mão:")
for t in tabela:
    print(t[0], tuple(round(v, 2) for v in t[1]), "near", t[2], tuple(round(v, 2) for v in nm[t[2]]), "new", tuple(round(v, 2) for v in t[3]), "livre" if t[4] else "colisão")
s = 1.15
g = [mundo(s, 0, 0, obs=OBM, w=10, h=6, S_=SM, G_=GM)]
idx = {}
k = 0
for it, q, i, qn, ok in tabela:
    X0, Y0 = nm[i]
    if ok:
        k += 1
        idx[it] = k
        g.append(r"\draw[dblue, line width=1.6pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (X(X0, s, 0), Y(Y0, s, 0), X(qn[0], s, 0), Y(qn[1], s, 0)))
    else:
        g.append(r"\draw[dred, line width=1.8pt, dashed] (%.2f,%.2f) -- (%.2f,%.2f);" % (X(X0, s, 0), Y(Y0, s, 0), X(qn[0], s, 0), Y(qn[1], s, 0)))
        g.append(r"\draw[dred, line width=2.6pt] (%.2f,%.2f) -- ++(0.2,0.2) (%.2f,%.2f) -- ++(0.2,-0.2) (%.2f,%.2f) -- ++(-0.2,0.2) (%.2f,%.2f) -- ++(-0.2,-0.2);" % ((X(qn[0], s, 0), Y(qn[1], s, 0)) * 4))
for kk in range(1, len(nm)):
    g.append(r"\node[circle, draw=dblue, fill=white, line width=1.2pt, inner sep=1pt, minimum size=0.5cm, font=\small\bfseries] at (%.2f,%.2f) {%d};" % (X(nm[kk][0], s, 0), Y(nm[kk][1], s, 0), kk))
g.append(r"\node[font=\large, text width=11cm, align=center] at (5.75,-0.9) {nó \textbf{numerado} = nó aceito; \textcolor{dred}{\textbf{×}} = $q_{\mathrm{new}}$ rejeitado por colisão};")
grava("exemplo-a-mao", "\n".join(g))

# ----------------------------------------------------------------- 7. estruturas de dados
g = []
g.append(r"\node[font=\Large\bfseries, text=dblue] at (4.2,8.2) {a árvore (estrutura): dois vetores};")
g.append(r"\tikzset{c/.style={draw=black!60, line width=1pt, minimum height=0.8cm, font=\large, fill=dcream}}")
cab = ["$i$", "$x$", "$y$", "pai$(i)$"]
wd = [1.2, 1.6, 1.6, 2.0]
x0 = 0.0
for j, (t, ww) in enumerate(zip(cab, wd)):
    g.append(r"\node[c, minimum width=%.1fcm, fill=dblue!15, font=\large\bfseries] at (%.2f,7.1) {%s};" % (ww, x0 + ww / 2, t))
    x0 += ww
for r in range(min(7, len(nm))):
    x0 = 0.0
    vals = [str(r), "%.1f" % nm[r][0], "%.1f" % nm[r][1], "--" if pm[r] is None else str(pm[r])]
    for ww, v in zip(wd, vals):
        g.append(r"\node[c, minimum width=%.1fcm] at (%.2f,%.2f) {%s};" % (ww, x0 + ww / 2, 6.25 - r * 0.8, v))
        x0 += ww
g.append(r"\node[font=\large, text width=7cm, align=center] at (3.2,0.3) {o nó $i$ guarda a posição e o \textbf{índice do pai}; a raiz (S) não tem pai};")
g.append(r"\node[dbox, draw=dgreen, text width=7.4cm, minimum height=2.2cm, font=\large, line width=1.6pt] at (12.9,7.4) {\textbf{\textcolor{dgreen}{Obstáculos} (estrutura)}\\ a \textbf{representação do mapa}: retângulos, círculos, polígonos ou um mapa de grade};")
g.append(r"\node[dbox, draw=dblue, text width=7.4cm, minimum height=2.2cm, font=\large, line width=1.6pt] at (12.9,4.5) {\textbf{\textcolor{dblue}{``Livre?''} (operação)}\\ diz se um \textbf{ponto} ou um \textbf{segmento} está livre, consultando os obstáculos};")
g.append(r"\node[dbox, draw=dorange, text width=7.4cm, minimum height=2.2cm, font=\large, line width=1.6pt] at (12.9,1.6) {\textbf{\textcolor{dorange}{Vizinho mais próximo} (operação)}\\ varrer \textbf{todos} os nós da árvore e guardar o de \textbf{menor distância}};")
grava("estruturas-dados", "\n".join(g))

# ----------------------------------------------------------------- 8. vies para o objetivo
s = 0.5
g = []
for ox, v, tit in [(0, 0.0, "sem viés"), (11.0, 0.10, "viés de 10\\%")]:
    nos, pai, log, ac, cam = rrt(seed=1, vies=v, maxit=200)
    g.append(mundo(s, ox, 0))
    g.append(arvore(nos, pai, s, ox, 0))
    if ac is not None:
        g.append(caminho_tikz(cam, s, ox, 0))
    g.append(r"\node[font=\Large\bfseries, anchor=south] at (%.2f,6.2) {%s};" % (ox + 5.0, tit))
    res = "chegou em %d iterações" % len(log) if ac is not None else "não chegou em 200 iterações"
    g.append(r"\node[font=\large, text width=10cm, align=center] at (%.2f,-0.9) {%d nós; \textbf{%s}};" % (ox + 5.0, len(nos), res))
    print("viés", v, "nós", len(nos), res)
grava("vies-objetivo", "\n".join(g))

# ----------------------------------------------------------------- 9. caminho pelos pais e atalhos
cs = atalhos(CAM)
s = 0.5
g = [mundo(s, 0, 0), arvore(NOS, PAI, s, 0, 0, cor="dblue!35", lw=0.6, r=0.04), caminho_tikz(CAM, s, 0, 0)]
for p in CAM:
    g.append(r"\fill[dorange] (%.2f,%.2f) circle (0.09);" % (X(p[0], s, 0), Y(p[1], s, 0)))
g.append(r"\node[font=\Large\bfseries, anchor=south] at (5.0,6.2) {seguir os pais de G até S};")
g.append(r"\node[font=\large, text width=10cm, align=center] at (5.0,-0.9) {caminho com \textbf{%d} nós e comprimento \textbf{%.1f}};" % (len(CAM), comprimento(CAM)))
ox2 = 11.0
g += [mundo(s, ox2, 0), caminho_tikz(CAM, s, ox2, 0, cor="dorange!60", lw=2.0, dash=", dashed"), caminho_tikz(cs, s, ox2, 0, cor="dgreen", lw=2.8)]
for p in cs:
    g.append(r"\fill[dgreen] (%.2f,%.2f) circle (0.1);" % (X(p[0], s, ox2), Y(p[1], s, ox2 * 0)))
g.append(r"\node[font=\Large\bfseries, anchor=south] at (%.2f,6.2) {suavização por atalhos};" % (ox2 + 5.0))
g.append(r"\node[font=\large, text width=10cm, align=center] at (%.2f,-0.9) {\textbf{%d} nós e comprimento \textbf{%.1f}};" % (ox2 + 5.0, len(cs), comprimento(cs)))
print("atalhos:", len(CAM), "->", len(cs), round(comprimento(CAM), 1), "->", round(comprimento(cs), 1))
grava("caminho-atalhos", "\n".join(g))

# ----------------------------------------------------------------- 10. parametros: passo delta
s = 0.33
g = []
for ox, d in [(0, 0.35), (7.6, 0.9), (15.2, 2.5)]:
    nos, pai, log, ac, cam = rrt(seed=1, delta=d, maxit=600)
    g.append(mundo(s, ox, 0))
    g.append(arvore(nos, pai, s, ox, 0, r=0.03, lw=0.6))
    if ac is not None:
        g.append(caminho_tikz(cam, s, ox, 0, lw=2.2))
    g.append(r"\node[font=\Large\bfseries, anchor=south] at (%.2f,4.05) {$\delta=%s$};" % (ox + 3.3, str(d).replace(".", "{,}")))
    if ac is not None:
        t = "%d iterações; %d nós; caminho %.1f" % (len(log), len(nos), comprimento(cam))
    else:
        t = "%d iterações; %d nós; \\textbf{não chegou}" % (len(log), len(nos))
    g.append(r"\node[font=\large, text width=7cm, align=center] at (%.2f,-0.8) {%s};" % (ox + 3.3, t))
g.append(r"\node[font=\large, text width=22cm, align=center] at (11.0,-2.1) {passo \textbf{pequeno}: lento; passo \textbf{grande}: rápido, mas passa mal por \textbf{espaços estreitos}};")
grava("parametros-passo", "\n".join(g))

# ----------------------------------------------------------------- 11. casos de borda (cinco casos)
s = 0.33
g = []
OY1, OY2 = 0.0, 0.0                      # uma só fileira
def titulo(ox, oy, t): return r"\node[font=\large\bfseries, anchor=south] at (%.2f,%.2f) {%s};" % (ox + 3.3, oy + 4.05, t)
def legenda(ox, oy, t): return r"\node[font=\large, text width=7cm, align=center] at (%.2f,%.2f) {%s};" % (ox + 3.3, oy - 0.8, t)
# (a) passagem estreita
OBA = [(9.5, 0.0, 10.5, 5.8), (9.5, 6.2, 10.5, 12.0)]
SA, GA = (1.5, 6.0), (18.0, 6.0)
nos, pai, log, ac, cam = rrt(seed=3, obs=OBA, s=SA, g=GA, maxit=500)
g.append(mundo(s, 0, OY1, obs=OBA, S_=SA, G_=GA)); g.append(arvore(nos, pai, s, 0, OY1, r=0.03, lw=0.6))
if ac is not None: g.append(caminho_tikz(cam, s, 0, OY1, lw=2.2))
g.append(titulo(0, OY1, "passagem estreita"))
g.append(legenda(0, OY1, "%d iterações; %s" % (len(log), "chegou" if ac is not None else "\\textbf{ainda não chegou}")))
print("passagem estreita:", len(log), ac is not None)
# (b) sem caminho: G dentro de uma caixa fechada
OBB = [(14.0, 3.0, 17.5, 3.8), (14.0, 8.2, 17.5, 9.0), (14.0, 3.0, 14.8, 9.0), (16.7, 3.0, 17.5, 9.0)]
SB, GB = (1.5, 6.0), (15.7, 6.0)
nos, pai, log, ac, cam = rrt(seed=3, obs=OBB, s=SB, g=GB, maxit=600)
ox = 7.2
g.append(mundo(s, ox, OY1, obs=OBB, S_=SB, G_=GB)); g.append(arvore(nos, pai, s, ox, OY1, r=0.03, lw=0.6))
g.append(titulo(ox, OY1, "sem caminho"))
g.append(legenda(ox, OY1, "%d iterações; nunca para \\textbf{sozinho}: use um \\textbf{limite}" % len(log)))
print("sem caminho:", len(log), ac is not None)
# (c) dois caminhos diferentes
ox = 14.4
g.append(mundo(s, ox, OY1))
for sd, cor in [(1, "dorange"), (2, "dgreen")]:
    nos_, pai_, log_, ac_, cam_ = rrt(seed=sd)
    g.append(caminho_tikz(cam_, s, ox, OY1, cor=cor, lw=2.4))
g.append(titulo(ox, OY1, "caminhos diferentes"))
g.append(legenda(ox, OY1, "sementes diferentes: \\textbf{%.1f} e \\textbf{%.1f}" % (comprimento(rrt(seed=1)[4]), comprimento(rrt(seed=2)[4]))))
# (d) obstaculo que se move
OBV_ANT = [(8.0, 0.0, 9.5, 7.0)]
OBV_NOVO = (8.0, 5.0, 9.5, 12.0)
SV, GV = (1.5, 6.0), (18.0, 6.0)
nos, pai, log, ac, camV = rrt(seed=4, obs=OBV_ANT, s=SV, g=GV, maxit=3000)
ox = 21.6
g.append(r"\draw[line width=1.2pt, fill=white] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ox, OY2, ox + W * s, OY2 + H * s))
g.append(r"\draw[line width=1pt, dashed, draw=black!60] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (X(OBV_ANT[0][0], s, ox), Y(OBV_ANT[0][1], s, OY2), X(OBV_ANT[0][2], s, ox), Y(OBV_ANT[0][3], s, OY2)))
g.append(r"\draw[line width=1pt, draw=black!70, fill=dshade] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (X(OBV_NOVO[0], s, ox), Y(OBV_NOVO[1], s, OY2), X(OBV_NOVO[2], s, ox), Y(OBV_NOVO[3], s, OY2)))
g.append(caminho_tikz(camV, s, ox, OY2, lw=2.4))
for a, b in zip(camV[:-1], camV[1:]):
    if not livre_seg(a, b, obs=[OBV_NOVO]):
        pt = next((p for p in pts_seg(a, b, 0.05) if (OBV_NOVO[0] <= p[0] <= OBV_NOVO[2] and OBV_NOVO[1] <= p[1] <= OBV_NOVO[3])), None)
        if pt:
            g.append(r"\draw[dred, line width=2.6pt] (%.2f,%.2f) -- ++(0.2,0.2) (%.2f,%.2f) -- ++(0.2,-0.2) (%.2f,%.2f) -- ++(-0.2,0.2) (%.2f,%.2f) -- ++(-0.2,-0.2);" % ((X(pt[0], s, ox), Y(pt[1], s, OY2)) * 4))
            break
g.append(r"\fill[dgreen] (%.2f,%.2f) circle (0.16); \fill[dred] (%.2f,%.2f) circle (0.16);" % (X(SV[0], s, ox), Y(SV[1], s, OY2), X(GV[0], s, ox), Y(GV[1], s, OY2)))
g.append(titulo(ox, OY2, "obstáculo que se move"))
g.append(legenda(ox, OY2, "o caminho \\textbf{deixou de valer}"))
# (e) restricao de movimento (carro)
ox = 28.8
g.append(r"\draw[line width=1.2pt, fill=white] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ox, OY2, ox + 6.6, OY2 + 4.0))
g.append(r"\draw[dred, dashed, line width=2.6pt] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + 0.6, OY2 + 0.8, ox + 4.2, OY2 + 0.8, ox + 4.2, OY2 + 3.2))
g.append(r"\draw[dgreen, line width=2.8pt] (%.2f,%.2f) -- (%.2f,%.2f) arc (-90:0:1.5) -- (%.2f,%.2f);" % (ox + 0.6, OY2 + 1.0, ox + 3.6, OY2 + 1.0, ox + 5.4 - 0.2 - 0.0, OY2 + 3.2))
g.append(r"\fill[dgreen] (%.2f,%.2f) circle (0.16); \fill[dred] (%.2f,%.2f) circle (0.16);" % (ox + 0.6, OY2 + 0.9, ox + 5.2, OY2 + 3.2))
g.append(r"\node[font=\normalsize\bfseries, text=dred, anchor=west] at (%.2f,%.2f) {curva fechada demais};" % (ox + 0.3, OY2 + 3.5))
g.append(r"\node[font=\normalsize\bfseries, text=dgreen, anchor=west] at (%.2f,%.2f) {curva suave};" % (ox + 0.3, OY2 + 2.8))
g.append(titulo(ox, OY2, "restrições de movimento"))
g.append(legenda(ox, OY2, "o passo vira uma \\textbf{simulação}"))
grava("casos-de-borda", "\n".join(g))

# ----------------------------------------------------------------- 12. variantes: RRT-Connect e RRT*
A, pA, B, pB, camC = rrt_connect(seed=1)
s = 0.5
g = [mundo(s, 0, 0), arvore(A, pA, s, 0, 0, cor="dblue", r=0.04, lw=0.7), arvore(B, pB, s, 0, 0, cor="dred", r=0.04, lw=0.7)]
if camC: g.append(caminho_tikz(camC, s, 0, 0, lw=2.8))
g.append(r"\node[font=\Large\bfseries, anchor=south] at (5.0,6.2) {RRT-Connect};")
g.append(r"\node[font=\large, text width=10cm, align=center] at (5.0,-0.9) {duas árvores, de \textcolor{dblue}{\textbf{S}} e de \textcolor{dred}{\textbf{G}}, que tentam se \textbf{encontrar}};")
print("connect:", len(A), len(B), round(comprimento(camC), 1))
# RRT*: schematic
pts = {"S": (0.0, 2.0), "a": (1.5, 3.6), "b": (1.5, 0.4), "q": (3.2, 2.0), "n1": (4.6, 3.4), "n2": (4.6, 0.6)}
cst = {"S": 0.0}
cst["a"] = math.dist(pts["S"], pts["a"]); cst["b"] = math.dist(pts["S"], pts["b"])
cst["n1"] = cst["a"] + math.dist(pts["a"], pts["n1"]); cst["n2"] = cst["b"] + math.dist(pts["b"], pts["n2"])
cq_near = cst["a"] + math.dist(pts["a"], pts["q"])
cq_star = math.dist(pts["S"], pts["q"])
n1_novo = cq_star + math.dist(pts["q"], pts["n1"]); n2_novo = cq_star + math.dist(pts["q"], pts["n2"])
print("rrt*: g(q) RRT", round(cq_near, 2), "RRT*", round(cq_star, 2), "n1", round(cst["n1"], 2), "->", round(n1_novo, 2), "n2", round(cst["n2"], 2), "->", round(n2_novo, 2))
sx, ox2 = 1.1, 11.8
def P(k, o=ox2): return (o + pts[k][0] * sx * 1.55, 0.9 + pts[k][1] * sx * 1.05)
g.append(r"\node[font=\Large\bfseries, anchor=south] at (%.2f,6.2) {RRT*: reescolhe o pai e refaz ligações};" % (ox2 + 3.2))
for k, (a, b) in enumerate([("S", "a"), ("S", "b"), ("a", "n1"), ("b", "n2")]):
    pa, pb = P(a), P(b)
    g.append(r"\draw[dblue, line width=1.8pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (pa[0], pa[1], pb[0], pb[1]))
pa, pb = P("a"), P("q")
g.append(r"\draw[dred, dashed, line width=1.8pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (pa[0], pa[1], pb[0], pb[1]))
pa = P("S")
g.append(r"\draw[dgreen, line width=2.6pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (pa[0], pa[1], pb[0], pb[1]))
for n_ in ("n1", "n2"):
    pn = P(n_)
    g.append(r"\draw[dgreen, line width=2.6pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (pb[0], pb[1], pn[0], pn[1]))
for k in pts:
    p = P(k)
    cor = "dgreen" if k == "q" else ("dgreen" if k == "S" else "dblue")
    g.append(r"\node[circle, draw=%s, fill=white, line width=1.5pt, minimum size=0.55cm, inner sep=0pt, font=\small\bfseries] at (%.2f,%.2f) {%s};" % (cor, p[0], p[1], "$q$" if k == "q" else ("S" if k == "S" else "$n_1$" if k == "n1" else "$n_2$" if k == "n2" else k)))
g.append(r"\node[font=\large, text width=9.4cm, align=center] at (%.2f,-0.9) {novo nó $q$: pai \textbf{S} (custo %.1f) em vez de $a$ (%.1f); $n_1$ e $n_2$ passam de %.1f para %.1f};" % (ox2 + 3.2, cq_star, cq_near, cst["n1"], n1_novo))
grava("variantes", "\n".join(g))

# ----------------------------------------------------------------- 13. um passo do RRT em quatro quadros
PTS = [(0.7, 0.9), (1.3, 1.7), (2.0, 2.0), (1.4, 3.0), (2.9, 1.1), (0.8, 3.4)]
ARE = [(0, 1), (1, 2), (2, 3), (2, 4), (3, 5)]
QNEAR = 2
QR = (4.1, 3.2)
DELTA_P = 1.1
QNEW = estende(PTS[QNEAR], QR, DELTA_P)
OBSP = (3.5, 0.3, 4.6, 2.0)
PW, PH, GAP = 5.0, 4.0, 1.4


def quadro(k, titulo):
    ox = k * (PW + GAP)
    o = [r"\draw[line width=1.2pt, fill=white] (%.2f,0) rectangle (%.2f,%.2f);" % (ox, ox + PW, PH)]
    o.append(r"\draw[line width=1pt, draw=black!70, fill=dshade] (%.2f,%.2f) rectangle (%.2f,%.2f);" % (ox + OBSP[0], OBSP[1], ox + OBSP[2], OBSP[3]))
    for a, b in ARE:
        o.append(r"\draw[dblue, line width=1.2pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + PTS[a][0], PTS[a][1], ox + PTS[b][0], PTS[b][1]))
    for i, p in enumerate(PTS):
        r_ = 0.2 if (i == QNEAR and k >= 1) else 0.09
        o.append(r"\fill[dblue] (%.2f,%.2f) circle (%.2f);" % (ox + p[0], p[1], r_))
    if k >= 1:
        o.append(r"\node[font=\large\bfseries, text=dblue, anchor=east] at (%.2f,%.2f) {$q_{\mathrm{near}}$};" % (ox + PTS[QNEAR][0] - 0.25, PTS[QNEAR][1] - 0.15))
    # q_rand
    o.append(r"\draw[dred, line width=2.6pt] (%.2f,%.2f) -- (%.2f,%.2f) (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + QR[0] - 0.17, QR[1] - 0.17, ox + QR[0] + 0.17, QR[1] + 0.17, ox + QR[0] - 0.17, QR[1] + 0.17, ox + QR[0] + 0.17, QR[1] - 0.17))
    o.append(r"\node[font=\large\bfseries, text=dred, anchor=south] at (%.2f,%.2f) {$q_{\mathrm{rand}}$};" % (ox + QR[0], QR[1] + 0.22))
    if k >= 1:
        o.append(r"\draw[dred, dashed, line width=1.4pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + PTS[QNEAR][0], PTS[QNEAR][1], ox + QR[0], QR[1]))
    if k >= 2:
        o.append(r"\draw[dgreen, line width=3pt] (%.2f,%.2f) -- (%.2f,%.2f);" % (ox + PTS[QNEAR][0], PTS[QNEAR][1], ox + QNEW[0], QNEW[1]))
        o.append(r"\fill[dgreen] (%.2f,%.2f) circle (0.17); \node[font=\large\bfseries, text=dgreen, anchor=north] at (%.2f,%.2f) {$q_{\mathrm{new}}$};" % (ox + QNEW[0], QNEW[1], ox + QNEW[0], QNEW[1] - 0.22))
    if k == 3:
        o.append(r"\node[font=\Large\bfseries, text=dgreen, fill=white, inner sep=2pt, anchor=south west] at (%.2f,%.2f) {livre!};" % (ox + 0.15, 0.1))
    o.append(r"\node[font=\Large\bfseries, anchor=south, text width=%.2fcm, align=center] at (%.2f,%.2f) {%s};" % (PW + 0.6, ox + PW / 2, PH + 0.15, titulo))
    return "\n".join(o)


g = [quadro(0, "1. amostrar"), quadro(1, "2. vizinho mais próximo"), quadro(2, "3. estender"), quadro(3, "4. verificar e acrescentar")]
for k in range(3):
    x0 = (k + 1) * (PW + GAP) - GAP + 0.15
    g.append(r"\draw[dtrans, line width=2.4pt, -{Stealth[length=3mm]}] (%.2f,%.2f) -- (%.2f,%.2f);" % (x0, PH / 2, x0 + GAP - 0.3, PH / 2))
# no quadro 4, a nova aresta e o novo no entram na arvore (azul)
ox = 3 * (PW + GAP)
g.append(r"\draw[dblue, line width=2.4pt] (%.2f,%.2f) -- (%.2f,%.2f); \fill[dblue] (%.2f,%.2f) circle (0.17);" % (ox + PTS[QNEAR][0], PTS[QNEAR][1], ox + QNEW[0], QNEW[1], ox + QNEW[0], QNEW[1]))
grava("passo-sequencia", "\n".join(g))
