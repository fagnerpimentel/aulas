#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 6 de IHR (Interação Verbal) para SVG em ../images/
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
    pipeline-verbal
    robo-frustrante
    enfase-frase
    componentes-fala
    tempo-frequencia
    wer-comparativo
    limitacoes-asr
    asr-nuvem-local
    vad-deteccao
    extracao-significado-niveis
    word2vec-espaco
    llm-previsao-palavra
    gestao-dialogo-espectro
    fsm-dialogo
    chatbot-tipos
    turno-timing
    pipeline-tts
    voz-robo-percepcao
    ciclo-verbal
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
