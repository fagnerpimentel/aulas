#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 2 de IHR (Design em IHR e Antropomorfização) para SVG em ../images/
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
    dentro-fora-vs-fora-dentro
    espectro-morfologia
    affordances-robo
    padroes-composicao
    prometer-entregar
    vale-estranheza
    pistas-minimas-rosto
    heider-simmel
    contingencia-olhar
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
