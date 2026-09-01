#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 3 de IHC (Fatores Humanos) para SVG em ../images/
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
    gestalt-principios
    gestalt-adicoes
    tons-de-cinza
    pre-atencional
    percepcao-cor
    sistema1-sistema2
    vieses-cognitivos
    metafora-metonimia
    ancora-vinhos
    reconhecimento-ordem
    afeto-cascata
    circumplexo
    shiv-fedorikhin
    niveis-design-emocional
    piramide-hedonomia
    abordagens-afeto
    computacao-afetiva-ciclo
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
