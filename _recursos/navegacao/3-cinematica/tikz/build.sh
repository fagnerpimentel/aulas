#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 3 de Navegação (Cinemática de Robôs Móveis) para SVG em ../images/
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
    manipulador-vs-movel
    cinematica-vs-dinamica
    frames
    rotacao
    diff-drive-forward
    contribuicoes-rodas
    exemplo-movimento
    exemplo-trajetoria
    exemplo-omni-movimento
    restricoes-conceito
    roda-fixa
    roda-orientavel
    roda-castor
    roda-sueca
    roda-esferica
    rodas-tipos-icones
    tipos-rodas-restricoes
    icr
    mobilidade-formulas
    cinco-tipos
    holonomia
    ddof-exemplo
    synchro-drive
    path-vs-trajectory
    controle-malha-aberta
    controle-realimentado
    lei-controle
    tb3-primitivas
    tb3-malha-aberta
    tb3-malha-fechada
    tb3-convergencia
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
