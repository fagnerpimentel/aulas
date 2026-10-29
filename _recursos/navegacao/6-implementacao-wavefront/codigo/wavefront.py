"""Wavefront (grassfire / NF1) em Python puro: grade, distâncias e caminho."""
import heapq
import math
from collections import deque

LIVRE, OBSTACULO = 0, 1
INF = float("inf")

VIZINHOS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
VIZINHOS_8 = VIZINHOS_4 + [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def dentro(grade, lin, col):
    return 0 <= lin < len(grade) and 0 <= col < len(grade[0])


def wavefront(grade, objetivo):
    """Passos de cada célula livre até o objetivo (4 vizinhos)."""
    n_lin, n_col = len(grade), len(grade[0])
    dist = [[INF] * n_col for _ in range(n_lin)]
    lin, col = objetivo
    dist[lin][col] = 0
    fila = deque([objetivo])
    while fila:
        lin, col = fila.popleft()
        for dl, dc in VIZINHOS_4:
            l, c = lin + dl, col + dc
            if (dentro(grade, l, c) and grade[l][c] == LIVRE
                    and dist[l][c] == INF):
                dist[l][c] = dist[lin][col] + 1
                fila.append((l, c))
    return dist


def caminho(dist, inicio, vizinhos=VIZINHOS_4):
    """Descida do gradiente: sempre para a vizinha de menor distância."""
    lin, col = inicio
    if dist[lin][col] == INF:
        return None  # o objetivo é inalcançável a partir daqui
    rota = [inicio]
    while dist[lin][col] > 0:
        candidatas = [(lin + dl, col + dc) for dl, dc in vizinhos
                      if dentro(dist, lin + dl, col + dc)]
        lin, col = min(candidatas, key=lambda p: dist[p[0]][p[1]])
        rota.append((lin, col))
    return rota


def wavefront_8(grade, objetivo):
    """8 vizinhos: a diagonal custa raiz de 2 (Dijkstra com heap)."""
    n_lin, n_col = len(grade), len(grade[0])
    dist = [[INF] * n_col for _ in range(n_lin)]
    lin, col = objetivo
    dist[lin][col] = 0.0
    heap = [(0.0, lin, col)]
    while heap:
        d, lin, col = heapq.heappop(heap)
        if d > dist[lin][col]:
            continue  # entrada velha do heap
        for dl, dc in VIZINHOS_8:
            l, c = lin + dl, col + dc
            if not dentro(grade, l, c) or grade[l][c] != LIVRE:
                continue
            if dl and dc and (grade[lin + dl][col] != LIVRE
                              or grade[lin][col + dc] != LIVRE):
                continue  # não corta a quina de um obstáculo
            novo = d + (math.sqrt(2) if dl and dc else 1.0)
            if novo < dist[l][c]:
                dist[l][c] = novo
                heapq.heappush(heap, (novo, l, c))
    return dist


def inflar(grade, raio):
    """Marca como obstáculo as células a até `raio` de um obstáculo."""
    n_lin, n_col = len(grade), len(grade[0])
    saida = [linha[:] for linha in grade]
    for lin in range(n_lin):
        for col in range(n_col):
            if grade[lin][col] != OBSTACULO:
                continue
            for dl in range(-raio, raio + 1):
                for dc in range(-raio, raio + 1):
                    l, c = lin + dl, col + dc
                    if dl * dl + dc * dc <= raio * raio and dentro(grade, l, c):
                        saida[l][c] = OBSTACULO
    return saida


def astar(grade, inicio, objetivo):
    """A* (4 vizinhos, heurística de Manhattan): (rota, células expandidas)."""
    def h(p):
        return abs(p[0] - objetivo[0]) + abs(p[1] - objetivo[1])
    g = {inicio: 0}
    pai = {}
    aberta = [(h(inicio), 0, inicio)]
    expandidas = []
    while aberta:
        _, custo, atual = heapq.heappop(aberta)
        if custo > g[atual]:
            continue
        expandidas.append(atual)
        if atual == objetivo:
            rota = [atual]
            while rota[-1] in pai:
                rota.append(pai[rota[-1]])
            return rota[::-1], expandidas
        for dl, dc in VIZINHOS_4:
            viz = (atual[0] + dl, atual[1] + dc)
            if not dentro(grade, *viz) or grade[viz[0]][viz[1]] != LIVRE:
                continue
            if custo + 1 < g.get(viz, INF):
                g[viz] = custo + 1
                pai[viz] = atual
                heapq.heappush(aberta, (custo + 1 + h(viz), custo + 1, viz))
    return None, expandidas


# --- ligação com mapas do ROS 2 (nav_msgs/OccupancyGrid) -------------------
def ocupacao_para_grade(dados, largura, altura, limiar=50):
    """OccupancyGrid.data (linha a linha; -1 = desconhecido) -> grade."""
    grade = []
    for lin in range(altura):
        linha = dados[lin * largura:(lin + 1) * largura]
        grade.append([OBSTACULO if v >= limiar or v < 0 else LIVRE
                      for v in linha])
    return grade


def mundo_para_celula(x, y, origem_x, origem_y, resolucao):
    lin = int((y - origem_y) // resolucao)
    col = int((x - origem_x) // resolucao)
    return lin, col


def celula_para_mundo(lin, col, origem_x, origem_y, resolucao):
    x = origem_x + (col + 0.5) * resolucao   # centro da célula
    y = origem_y + (lin + 0.5) * resolucao
    return x, y
