#!/usr/bin/env bash
# Compila os diagramas TikZ da aula 8 de IHR (Métodos de Pesquisa) para SVG em ../images/
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
    hri-componentes
    exploratoria-confirmatoria
    correlacao-causacao
    delineamento-2x2
    tipos-metodo
    entre-intra-sujeitos
    contexto-estudo
    unidades-analise
    wizard-of-oz
    medidas-diretas-indiretas
    tres-medidas
    erros-tipo
    etica-estudo
    centrado-robo-usuario
    boa-pergunta
    reeves-nass
    registrar-hipotese
    visao-geral-metodos
    qual-quanti-misto
    atribuicao-aleatoria
    ver-medir-verificar
    escalas-survey
    wer
    fontes-observacao
    pros-contras-observacao
    etnografia
    transcricao-conversa
    crowdsourcing-fluxo
    crowd-nao-serve
    estudo-de-caso
    amostra-populacao
    quantos-participantes
    efeito-organizacao
    consentimento
  )
fi

for f in "${FILES[@]}"; do
  echo ">> $f"
  pdflatex -interaction=nonstopmode -halt-on-error \
           -output-directory "$TMP" "$f.tex" > "$TMP/$f.log" 2>&1 \
    || { echo "FALHOU: veja $TMP/$f.log"; tail -n 25 "$TMP/$f.log"; exit 1; }
  dvisvgm --pdf --no-fonts --exact-bbox --output="$OUT/$f.svg" "$TMP/$f.pdf"
done
echo "OK -> $OUT"
