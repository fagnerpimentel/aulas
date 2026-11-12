"""Simulação do RRT usada pelas figuras da aula 8 de Navegação (semente fixa, para reproduzir os números)."""
import math, random

W, H = 20.0, 12.0
OBS = [(5.5, 0.0, 7.5, 7.5), (10.5, 4.5, 12.5, 12.0), (15.0, 0.0, 16.5, 6.5)]   # retângulos (x0,y0,x1,y1)
S, G = (1.5, 6.0), (18.0, 8.5)


def livre_pt(p, obs=OBS):
    return all(not (x0 <= p[0] <= x1 and y0 <= p[1] <= y1) for x0, y0, x1, y1 in obs)


def livre_seg(a, b, obs=OBS, passo=0.05):
    d = math.dist(a, b)
    n = max(1, int(d / passo))
    for i in range(n + 1):
        t = i / n
        if not livre_pt((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])), obs):
            return False
    return True


def estende(qn, qr, delta):
    d = math.dist(qn, qr)
    if d <= delta:
        return qr
    return (qn[0] + delta * (qr[0] - qn[0]) / d, qn[1] + delta * (qr[1] - qn[1]) / d)


def rrt(seed=1, delta=0.9, vies=0.05, tol=0.9, maxit=4000, obs=OBS, s=S, g=G, parar_ao_achar=True):
    rnd = random.Random(seed)
    nos = [s]
    pai = [None]
    log = []                      # (it, qrand, idx_near, qnew|None, ok)
    achou = None
    for it in range(1, maxit + 1):
        qr = g if rnd.random() < vies else (rnd.uniform(0, W), rnd.uniform(0, H))
        i = min(range(len(nos)), key=lambda k: (nos[k][0] - qr[0]) ** 2 + (nos[k][1] - qr[1]) ** 2)
        qn = estende(nos[i], qr, delta)
        ok = livre_pt(qn, obs) and livre_seg(nos[i], qn, obs)
        log.append((it, qr, i, qn, ok))
        if ok:
            nos.append(qn)
            pai.append(i)
            if math.dist(qn, g) <= tol and achou is None:
                achou = len(nos) - 1
                if parar_ao_achar:
                    break
    caminho = []
    k = achou
    while k is not None:
        caminho.append(nos[k])
        k = pai[k]
    caminho.reverse()
    return nos, pai, log, achou, caminho


def comprimento(c):
    return sum(math.dist(c[i], c[i + 1]) for i in range(len(c) - 1))


def atalhos(caminho, obs=OBS):
    """suavização: tenta ligar cada nó ao mais distante visível"""
    res = [caminho[0]]
    i = 0
    while i < len(caminho) - 1:
        j = len(caminho) - 1
        while j > i + 1 and not livre_seg(caminho[i], caminho[j], obs):
            j -= 1
        res.append(caminho[j])
        i = j
    return res


if __name__ == "__main__":
    for seed in range(1, 12):
        nos, pai, log, achou, cam = rrt(seed=seed)
        print(seed, "iters", len(log), "nós", len(nos), "achou", achou is not None, "comp", round(comprimento(cam), 1) if achou else None)


def rrt_connect(seed=1, delta=0.9, maxit=3000, obs=OBS, s=S, g=G):
    """RRT-Connect (duas árvores): devolve (A, paiA, B, paiB, caminho) com A enraizada em S e B em G."""
    rnd = random.Random(seed)
    A, pA, B, pB = [s], [None], [g], [None]
    troca = False
    for _ in range(maxit):
        T1, P1, T2, P2 = (B, pB, A, pA) if troca else (A, pA, B, pB)
        qr = (rnd.uniform(0, W), rnd.uniform(0, H))
        i = min(range(len(T1)), key=lambda k: (T1[k][0] - qr[0]) ** 2 + (T1[k][1] - qr[1]) ** 2)
        qn = estende(T1[i], qr, delta)
        if livre_pt(qn, obs) and livre_seg(T1[i], qn, obs):
            T1.append(qn); P1.append(i)
            # tenta conectar a outra árvore até qn
            j = min(range(len(T2)), key=lambda k: (T2[k][0] - qn[0]) ** 2 + (T2[k][1] - qn[1]) ** 2)
            cur = j
            while True:
                nx = estende(T2[cur], qn, delta)
                if not (livre_pt(nx, obs) and livre_seg(T2[cur], nx, obs)):
                    break
                T2.append(nx); P2.append(cur); cur = len(T2) - 1
                if math.dist(nx, qn) < 1e-9:
                    # conectado: monta o caminho
                    def sobe(T, P, k):
                        c = []
                        while k is not None:
                            c.append(T[k]); k = P[k]
                        return c[::-1]
                    ca = sobe(T1, P1, len(T1) - 1)
                    cb = sobe(T2, P2, len(T2) - 1)
                    cam = ca + cb[::-1][1:] if not troca else sobe(T2, P2, len(T2) - 1) + sobe(T1, P1, len(T1) - 1)[::-1][1:]
                    return A, pA, B, pB, cam
        troca = not troca
    return A, pA, B, pB, None
