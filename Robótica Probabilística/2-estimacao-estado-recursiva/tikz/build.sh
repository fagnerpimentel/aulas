#!/usr/bin/env bash
# Compila os diagramas TikZ do slide 7 para SVG em ../images/
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
    variaveis-robo-pose
    variaveis-robo-atuadores
    variaveis-ambiente-marco
    variaveis-ambiente-movimento
    variaveis-ambiente-outras
    crenca-inicial
    dados-medicao-controle
    distribuicao-crenca
    duas-probabilidades
    filtro-bayes-passos
    matriz-sensor
    modelo-hmm
    passo1-crenca
    passo2-crenca
    resultado-final-porta
    transicao-porta
    transicao-porta-empurrar
    transicao-porta-nada
    interacao-robo-ambiente
    estado-tipos
    cadeia-markov
    estado-incompleto
    linha-tempo
    percepcao-vs-movimento
    hipoteses-probabilidade
    familia-filtros
    exato-vs-aproximado
    tradeoffs
    sensores-para-crenca
    predicao-correcao
    estado-exemplo
  )
fi

for f in "${FILES[@]}"; do
  echo ">> $f"
  pdflatex -interaction=nonstopmode -halt-on-error \
           -output-directory "$TMP" "$f.tex" > "$TMP/$f.log" 2>&1 \
    || { echo "FALHOU: veja $TMP/$f.log"; cat "$TMP/$f.log"; exit 1; }
  # PDF -> SVG, texto convertido em curvas (--no-fonts) para renderizar em qualquer lugar
  dvisvgm --pdf --no-fonts --exact-bbox --output="$OUT/$f.svg" "$TMP/$f.pdf"
done

echo "OK -> $OUT/{$(IFS=,; echo "${FILES[*]}")}.svg"
