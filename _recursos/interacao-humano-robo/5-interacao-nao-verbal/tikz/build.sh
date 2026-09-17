#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 5 de IHR (Interação Não Verbal) para SVG em ../images/
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
    canais-nao-verbais
    falar-sem-palavras
    camada-nao-verbal
    atencao-conjunta
    funcoes-olhar
    pupila-dilatacao
    papeis-conversacionais
    tipos-gestos
    congruencia-gestos
    mimica-neuronios
    efeito-camaleao
    imitacao-robo
    espectro-toque
    toque-afetivo-funcional
    postura-sinais
    micro-movimentos
    alternancia-turnos-timing
    ritmo-sincronia
    percepcao-geracao-ciclo
    keyframes-interpolacao
    arquitetura-cognitiva
    ciclo-nao-verbal
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
