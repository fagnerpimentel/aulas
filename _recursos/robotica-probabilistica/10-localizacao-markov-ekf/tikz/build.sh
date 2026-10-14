#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 10 (Localização de Markov e Gaussiana) para SVG em ../images/
# Requer: pdflatex + dvisvgm (TeX Live). Sem argumentos: compila todos os .tex (exceto o preâmbulo).
set -euo pipefail
cd "$(dirname "$0")"
OUT="../images"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  FILES=()
  for t in *.tex; do [ "$t" = preamble.tex ] || FILES+=("${t%.tex}"); done
fi

for f in "${FILES[@]}"; do
  echo ">> $f"
  pdflatex -interaction=nonstopmode -halt-on-error \
           -output-directory "$TMP" "$f.tex" > "$TMP/$f.log" 2>&1 \
    || { echo "FALHOU: veja $TMP/$f.log"; grep -m3 -A3 "^!" "$TMP/$f.log"; exit 1; }
  dvisvgm --pdf --no-fonts --exact-bbox --output="$OUT/$f.svg" "$TMP/$f.pdf" > /dev/null 2>&1
done
echo "OK -> $OUT ($(echo "${FILES[@]}" | wc -w) arquivos)"
