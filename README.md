# Aulas

Materiais de aula em [Quarto](https://quarto.org): slides Reveal.js, roteiros de
laboratório e diagramas. Substitui o modelo antigo baseado em Marp
(`aulas_marp`).

## Estrutura

```
aulas/
├── _quarto.yml            # projeto Quarto (site) + formato padrão (revealjs)
├── custom.scss            # tema compartilhado por todas as disciplinas
├── index.qmd              # página inicial (lista as disciplinas)
├── .github/workflows/     # CI: renderiza e publica no GitHub Pages
├── _recursos/             # imagens e fontes de diagramas (o prefixo _ faz o Quarto ignorar a pasta)
│   └── <disciplina>/
│       └── <N-slug-da-aula>/
│           ├── images/    # SVGs/JPEGs usados nos slides (versionados)
│           └── tikz/      # fontes LaTeX dos diagramas + build.sh
└── <disciplina>/
    ├── index.qmd          # página da disciplina (lista as aulas)
    ├── teoria/            # slides das aulas teóricas
    │   └── <N-slug-da-aula>.qmd
    └── pratica/           # roteiros de aula prática (.qmd → HTML)
```

Convenção de nomes das aulas teóricas: `N-slug`, onde `N` é o número do
capítulo/tema (ex.: `2-estimacao-estado-recursiva`).

Cada `.qmd` de teoria referencia suas imagens como `images/...` e aponta para a
pasta em `_recursos/` pelo campo `resource-path` no cabeçalho YAML.

### Disciplinas

- **Robótica Probabilística** — estimação de estado, filtros bayesianos,
  localização e SLAM. Baseada em *Probabilistic Robotics* (Thrun, Burgard, Fox).

## Como renderizar

Pré-requisito: [Quarto](https://quarto.org/docs/get-started/) instalado.

```bash
quarto preview        # servidor local com hot-reload
quarto render         # gera o site completo em _site/
quarto render robotica-probabilistica/teoria/2-estimacao-estado-recursiva.qmd
```

As saídas (`_site/`, `*.html`, `*_files/`, `*.pdf`) **não** são versionadas — são
geradas a partir das fontes `.qmd`.

## Diagramas TikZ

Alguns slides usam diagramas gerados a partir de LaTeX. Para cada aula, as fontes
ficam em `_recursos/<disciplina>/<aula>/tikz/` e os SVGs resultantes ao lado, em
`.../images/` (esses SVGs **são** versionados, para o CI não precisar de LaTeX).

```bash
cd _recursos/robotica-probabilistica/2-estimacao-estado-recursiva/tikz
./build.sh                    # recompila todos os diagramas
./build.sh cadeia-markov      # recompila apenas um
```

Requer `pdflatex` + `dvisvgm` (TeX Live).

## Publicação

O workflow [`.github/workflows/publish.yml`](.github/workflows/publish.yml)
renderiza o site e publica no GitHub Pages a cada push na `main`. Para ativar:
**Settings → Pages → Source: GitHub Actions**.

## Material legado

Os arquivos PowerPoint originais (`.ppt`/`.pptx`) e SVGs grandes foram movidos
para `../_legado-aulas/` (fora deste repositório) e não fazem parte do
versionamento.
