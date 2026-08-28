# Exercício: Filtro de Bayes para Localização de Robôs

**Disciplina:** Robótica Probabilística / Percepção e Estimação de Estado
**Tema:** Filtro de Bayes discreto (recursivo)
**Duração estimada:** 2 horas

---

## Objetivos de aprendizagem

Ao final deste exercício, o aluno deve ser capaz de:

- Explicar o papel das etapas de **predição** (motion update) e **correção** (measurement update) no filtro de Bayes.
- Justificar a hipótese de Markov usada na derivação do filtro.
- Calcular manualmente a evolução de uma distribuição de crença (*belief*) discreta.
- Implementar um filtro de Bayes discreto em Python para localização 1D de um robô.

---

## Parte 1 — Fundamentação teórica (sem calculadora)

1. Escreva a expressão recursiva do filtro de Bayes para a crença `bel(x_t)`, separando explicitamente a etapa de predição (usando o modelo de movimento `p(x_t | u_t, x_{t-1})`) e a etapa de correção (usando o modelo de sensor `p(z_t | x_t)`).

2. A derivação do filtro de Bayes depende da **hipótese de Markov**. Enuncie essa hipótese em suas próprias palavras e dê um exemplo de situação em robótica real na qual ela é violada (ou seja, o estado atual não resume toda a informação relevante do passado).

3. Explique por que a etapa de correção é uma aplicação direta do Teorema de Bayes, mas a etapa de predição **não** é — ela é uma aplicação do Teorema da Probabilidade Total.

4. O termo de normalização `η` (eta) aparece na etapa de correção. Qual é o seu papel? O que aconteceria com a crença se ele fosse omitido?

5. Cite duas limitações do filtro de Bayes **discreto** (grid-based) em comparação com o Filtro de Kalman ou o Filtro de Partículas, especialmente em relação a custo computacional e dimensionalidade do espaço de estados.

---

## Parte 2 — Cálculo manual: robô em corredor 1D

Considere um robô que se move em um corredor discretizado em **5 posições** (células 1 a 5, dispostas em linha). O robô não sabe onde está inicialmente, então sua crença inicial é uniforme:

```
bel(x_0) = [0.2, 0.2, 0.2, 0.2, 0.2]   (células 1, 2, 3, 4, 5)
```

Há uma porta apenas na **célula 3**. O sensor do robô detecta "porta" ou "não-porta" com o seguinte modelo de observação:

- `p(z=porta | x=célula 3) = 0.8`
- `p(z=porta | x≠célula 3) = 0.2`

**Passo 1 — Correção (measurement update):**
O robô lê o sensor pela primeira vez e observa `z_1 = porta`.
Calcule `bel(x_1)` aplicando o Teorema de Bayes célula a célula e normalizando o resultado. Mostre os valores não normalizados e o valor de `η`.

**Passo 2 — Predição (motion update):**
O robô então executa o comando "mover uma célula para a direita". O modelo de movimento não é perfeito:

- `p(x_t = i+1 | u=direita, x_{t-1}=i) = 0.8`
- `p(x_t = i | u=direita, x_{t-1}=i) = 0.2` (o robô às vezes não se move)
- Nas bordas do corredor, assuma que a massa de probabilidade que "sairia" do corredor permanece na célula extrema.

Calcule a crença predita `bel_bar(x_2)` a partir de `bel(x_1)`.

**Passo 3 — Correção novamente:**
O robô lê o sensor de novo e observa `z_2 = não-porta`. Calcule `bel(x_2)` final.

**Pergunta de reflexão:** Após esses três passos, em qual célula o robô está mais confiante de que se encontra? Esse resultado faz sentido dado o histórico de observações e o movimento executado?

---

## Parte 3 — Implementação em Python

Implemente um filtro de Bayes discreto genérico para o cenário do corredor de **N células** (não apenas 5), com as seguintes funções:

```python
def predict(bel, motion_model, u):
    """
    bel: lista de probabilidades (crença atual)
    motion_model: dict ou função p(x_t | u, x_t-1)
    u: comando de controle ('direita' ou 'esquerda')
    Retorna: bel_bar (crença predita)
    """
    # TODO

def correct(bel_bar, sensor_model, z):
    """
    bel_bar: crença predita
    sensor_model: p(z | x) para cada célula
    z: observação ('porta' ou 'nao_porta')
    Retorna: bel (crença corrigida e normalizada)
    """
    # TODO
```

**Tarefas:**

1. Implemente `predict` e `correct` de forma genérica (não hard-code os valores da Parte 2).
2. Valide sua implementação reproduzindo numericamente os resultados da Parte 2 (os valores devem bater até a 3ª casa decimal).
3. Simule um corredor com **10 células**, com portas nas células 3 e 7, e uma sequência de 6 movimentos/observações à sua escolha. Plote a evolução de `bel(x_t)` a cada passo (um gráfico de barras por iteração, ou um heatmap tempo × posição).
4. **Desafio (opcional):** o que acontece com a crença se as duas portas estiverem posicionadas simetricamente e as observações forem ambíguas? O filtro consegue convergir para uma única hipótese? Discuta o problema de *multimodalidade* e por que ele é relevante para a escolha entre filtro de Bayes discreto, EKF e filtro de partículas.

---

## Entregáveis

- Respostas escritas da Parte 1 e Parte 2 (pode ser à mão ou digitado, com os cálculos intermediários visíveis).
- Código Python da Parte 3 + gráfico(s) da simulação de 10 células.
- Um parágrafo curto respondendo ao desafio opcional (se realizado).
