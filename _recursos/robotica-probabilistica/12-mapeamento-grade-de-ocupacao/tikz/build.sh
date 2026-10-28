#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 12 de Robótica Probabilística para SVG em ../images/
# uso: ./build.sh [nome ...]   (sem argumentos: gera os .tex com gerar.py e compila todos)
# Requer: pdflatex + dvisvgm (TeX Live) e python3
set -euo pipefail
cd "$(dirname "$0")"
OUT="../images"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  [ -f gerar.py ] && python3 gerar.py
  FILES=()
  for f in *.tex; do [ "$f" = "preamble.tex" ] || FILES+=("${f%.tex}"); done
fi
for f in "${FILES[@]}"; do
  echo ">> $f"
  pdflatex -interaction=nonstopmode -halt-on-error \
           -output-directory "$TMP" "$f.tex" > "$TMP/$f.log" 2>&1 \
    || { echo "FALHOU: veja $TMP/$f.log"; tail -n 25 "$TMP/$f.log"; exit 1; }
  dvisvgm --pdf --no-fonts --exact-bbox --output="$OUT/$f.svg" "$TMP/$f.pdf"
done
echo "OK -> $OUT (${#FILES[@]} figuras)"
