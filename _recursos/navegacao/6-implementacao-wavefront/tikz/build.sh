#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 6 de Navegação (Implementação do Wavefront) para SVG em ../images/
# Requer: pdflatex + dvisvgm (TeX Live)
set -euo pipefail
cd "$(dirname "$0")"
python3 gerar_figuras.py > /dev/null
python3 gerar_descida.py > /dev/null
OUT="../images"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [ "$#" -gt 0 ]; then
  FILES=("$@")
else
  FILES=(
    grade-entrada
    vizinhancas
    wavefront-etapas
    wavefront-resultado
    comparacao-4-8
    inflar-obstaculos
    wavefront-astar
    ocupacao-ros
    pipeline-ros
    descida-gradiente
    fila-em-acao
    caminho-em-acao
    executando-a-mao
    executando-a-mao-lateral
    executando-a-mao-coluna
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
