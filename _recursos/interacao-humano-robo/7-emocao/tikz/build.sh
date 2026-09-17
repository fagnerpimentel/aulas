#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 7 de IHR (Emoção) para SVG em ../images/
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
    afeto-emocao-humor
    emocao-preparacao
    emocao-canal-comunicacao
    emocoes-basicas-secundarias
    circumplex-russell
    retroalimentacao-facial
    quando-da-errado
    robo-agencia-social
    estrategia-mimica
    gerenciamento-expectativa
    percepcao-artificial-emocao
    facs-unidades-acao
    robos-expressivos
    occ-modelo-simplificado
    pad-modelo-3d
    desafios-leitura-emocao
    atores-exagero
    ciclo-emocao-robo
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
