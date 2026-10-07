#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 5 de IHC (Processos de Design de IHC) para SVG em ../images/
# Requer: pdflatex + dvisvgm (TeX Live)
set -euo pipefail
cd "$(dirname "$0")"
OUT="../images"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  FILES=(
    visao-geral
    situacao-intervencao
    sequencia-generica
    problema-vs-solucao
    modelo-simples
    ciclo-estrela
    nielsen-dez-passos
    faixas-usabilidade
    prototipo-horizontal-vertical
    mayhew
    design-contextual
    cenarios
    objetivo-tarefa
    objetivos-fases
    comunicacao
    sistema-vs-uso
    comparacao-processos
    lista-processos
    artefatos-intervencao
    analise-elementos
    metas-design
    stakeholders
    avaliacao-momentos
    iteracao-esforco
    gould-lewis
    coevolucao
    analise-competitiva
    design-paralelo
    diretrizes-niveis
    wizard-of-oz
    fidelidade-prototipos
    tres-cenarios
    mediana-vs-criativa
    usuario-maquina
    integracao-abordagens
    principios-gulliksen
    equipes-multi
    metacomunicacao-design
    linha-tempo-processos
  )
fi

for f in "${FILES[@]}"; do
  echo ">> $f"
  pdflatex -interaction=nonstopmode -halt-on-error \
           -output-directory "$TMP" "$f.tex" > "$TMP/$f.log" 2>&1 \
    || { echo "FALHOU: veja $TMP/$f.log"; tail -n 25 "$TMP/$f.log"; exit 1; }
  dvisvgm --pdf --no-fonts --exact-bbox --output="$OUT/$f.svg" "$TMP/$f.pdf"
done
echo "OK -> $OUT/{$(IFS=,; echo "${FILES[*]}")}.svg"
