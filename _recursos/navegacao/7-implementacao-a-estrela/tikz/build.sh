#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 7 de Navegação (Implementação do A*) para SVG em ../images/
# uso: ./build.sh [nome ...]   (sem argumentos: regera os .tex e compila todos)
# Requer: pdflatex + dvisvgm (TeX Live) e python3
set -euo pipefail
cd "$(dirname "$0")"
python3 gerar_figuras.py > /dev/null
OUT="../images"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  FILES=(wavefront-vs-astar g-h-f heuristica-manhattan lista-aberta astar-etapas astar-caminho estruturas-dados casos-de-borda)
fi
for f in "${FILES[@]}"; do
  echo ">> $f"
  pdflatex -interaction=nonstopmode -halt-on-error \
           -output-directory "$TMP" "$f.tex" > "$TMP/$f.log" 2>&1 \
    || { echo "FALHOU: veja $TMP/$f.log"; tail -n 25 "$TMP/$f.log"; exit 1; }
  dvisvgm --pdf --no-fonts --exact-bbox --output="$OUT/$f.svg" "$TMP/$f.pdf"
done
echo "OK -> $OUT (${#FILES[@]} figuras)"
