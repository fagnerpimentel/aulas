import math
from wavefront import *

TEXTO = [
    ".........",
    "....#....",
    "....#.##.",
    ".G..#..#.",
    "....#..#S",
    ".........",
]
grade = [[OBSTACULO if ch == "#" else LIVRE for ch in linha] for linha in TEXTO]
G, S = (3, 1), (4, 8)

d = wavefront(grade, G)
assert d[G[0]][G[1]] == 0
rota = caminho(d, S)
assert rota[0] == S and rota[-1] == G
assert len(rota) - 1 == d[S[0]][S[1]]
assert all(grade[l][c] == LIVRE for l, c in rota)
assert all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rota, rota[1:]))
print("distância S->G (4 viz.):", d[S[0]][S[1]])

r, exp = astar(grade, S, G)
assert len(r) - 1 == d[S[0]][S[1]]  # A* também é ótimo
print("A* expandiu", len(exp), "de", sum(v != INF for lin in d for v in lin), "células alcançáveis")

d8 = wavefront_8(grade, G)
r8 = caminho(d8, S, VIZINHOS_8)
assert d8[S[0]][S[1]] <= d[S[0]][S[1]] + 1e-9
print("custo S->G (8 viz.): %.3f, passos: %d" % (d8[S[0]][S[1]], len(r8) - 1))

# inalcançável
fechada = [[LIVRE]*5 for _ in range(5)]
for i in range(5): fechada[2][i] = OBSTACULO
df = wavefront(fechada, (0, 0))
assert caminho(df, (4, 4)) is None and df[4][4] == INF

# inflar
g2 = [[LIVRE]*7 for _ in range(7)]; g2[3][3] = OBSTACULO
gi = inflar(g2, 1)
assert gi[3][4] == OBSTACULO and gi[2][3] == OBSTACULO and gi[2][2] == LIVRE and gi[4][4] == LIVRE

# ROS
dados = [0, 100, -1, 0, 0, 0]
assert ocupacao_para_grade(dados, 3, 2) == [[0, 1, 1], [0, 0, 0]]
assert mundo_para_celula(0.37, 0.12, -0.5, -0.5, 0.25) == (2, 3)
x, y = celula_para_mundo(2, 3, -0.5, -0.5, 0.25)
assert abs(x - 0.375) < 1e-9 and abs(y - 0.125) < 1e-9
print("todos os testes passaram")
