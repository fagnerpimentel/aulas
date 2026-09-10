#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 4 de IHR (Interação Espacial) para SVG em ../images/
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
    espaco-recurso
    zonas-hall
    grupo-orientacao
    nao-atravessar-conversa
    mapas-humanos
    fatores-distancia
    adaptar-distancia
    direcao-aproximacao
    aproximacao-fases
    f-formation-espacos
    f-formation-arranjos
    robo-entra-formacao
    robo-guia-museu
    braco-espaco-pessoal
    aprender-aproximacao
    carros-polidez
    navegacao-social-requisitos
    pre-requisitos
    informar-intencao
    custo-espaco-pessoal
    passar-lado
    prever-trajetoria
    dinamica-espacial
    guiar-seguir
    ciclo-espacial
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
