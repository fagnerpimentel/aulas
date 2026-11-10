"""Gera os diagramas TikZ da aula 9 de IHC (Princípios e Diretrizes). Uso: python3 gerar.py && bash build.sh"""
exec(open("_helpers.py").read())

# ------------------------------------------------------------------ tres niveis
w("tres-niveis", r"""
\tikzset{k/.style={dbox, text width=7.6cm, minimum height=2.0cm, font=\large, line width=1.7pt, align=left},
        t/.style={dbox, text width=3.4cm, minimum height=2.0cm, font=\Large\bfseries, line width=1.7pt}}
\node[t, draw=dblue] at (2.0,6.6) {\textcolor{dblue}{Princípio}};
\node[k, draw=dblue] at (8.6,6.6) {objetivo \textbf{geral}, de \textbf{alto nível}\\ {\normalsize ex.: consistência}};
\node[t, draw=dgreen] at (2.0,3.9) {\textcolor{dgreen}{Diretriz}};
\node[k, draw=dgreen] at (8.6,3.9) {\textbf{regra geral} comum na prática\\ {\normalsize ex.: ações semelhantes funcionam da mesma forma}};
\node[t, draw=dorange] at (2.0,1.2) {\textcolor{dorange}{Padrão}};
\node[k, draw=dorange] at (8.6,1.2) {\textbf{solução específica} a um contexto delimitado\\ {\normalsize ex.: o padrão Acordeão}};
\draw[dtrans, line width=2.6pt, -{Stealth[length=4mm]}] (13.6,7.4) -- (13.6,0.4);
\node[font=\large\bfseries, dblue, anchor=west] at (14.0,6.9) {geral};
\node[font=\large\bfseries, dorange, anchor=west] at (14.0,0.7) {específico};
""")

# ------------------------------------------------------------------ nove familias
w("nove-familias", boxes([
  ("1. Expectativas", "correspondência com as expectativas do usuário"),
  ("2. Simplicidade", "simplicidade na estrutura das tarefas"),
  ("3. Controle", "equilíbrio entre controle e liberdade"),
  ("4. Consistência", "consistência e padronização"),
  ("5. Eficiência", "promover a eficiência do usuário"),
  ("6. Antecipação", "antecipar as necessidades"),
  ("7. Visibilidade", "visibilidade e reconhecimento"),
  ("8. Conteúdo", "conteúdo relevante e expressão adequada"),
  ("9. Erros", "projeto para erros")], w=5.4, h=2.6, cols=3))

# ------------------------------------------------------------------ identificacao na compra
w("identificacao-compra", r"""
\tikzset{s/.style={dbox, text width=2.6cm, minimum height=1.4cm, font=\normalsize, line width=1.5pt, rounded corners=8pt},
        a/.style={dtrans, line width=1.8pt, -{Stealth[length=3mm]}}}
\node[font=\large\bfseries, dgreen, anchor=west] at (0,8.6) {(a) identificar só no fim, como na loja física};
\node[s, draw=dblue] (a1) at (1.5,7.3) {buscar produto};
\node[s, draw=dblue] (a2) at (5.0,7.3) {selecionar produto};
\node[s, draw=dgreen, line width=2.4pt] (a3) at (8.5,7.3) {efetuar login};
\node[s, draw=dgreen] (a4) at (12.0,7.3) {finalizar compra};
\draw[a] (a1) -- (a2); \draw[a] (a2) -- (a3); \draw[a] (a3) -- (a4);
\node[font=\large\bfseries, dred, anchor=west] at (0,5.7) {(b) identificar antes de tudo};
\node[s, draw=dred, line width=2.4pt] (b1) at (1.5,4.4) {efetuar login};
\node[s, draw=dblue] (b2) at (5.0,4.4) {buscar produto};
\node[s, draw=dblue] (b3) at (8.5,4.4) {selecionar produto};
\node[s, draw=dgreen] (b4) at (12.0,4.4) {finalizar compra};
\draw[a] (b1) -- (b2); \draw[a] (b2) -- (b3); \draw[a] (b3) -- (b4);
\node[font=\large\bfseries, dgreen, anchor=west] at (0,2.8) {(c) opcional, a qualquer momento antes do \emph{checkout}};
\node[s, draw=dblue] (c1) at (1.5,1.5) {buscar produto};
\node[s, draw=dblue] (c2) at (5.0,1.5) {selecionar produto};
\node[s, draw=dgreen] (c4) at (12.0,1.5) {finalizar compra};
\node[s, draw=dgreen, dashed, line width=2.4pt] (c3) at (8.5,1.5) {efetuar login};
\draw[a] (c1) -- (c2); \draw[a] (c2) -- (c3); \draw[a] (c3) -- (c4);
\draw[a, dashed] (c2.south) to[bend right=25] (c4.south);
\node[dbox, draw=dgreen, text width=5.0cm, minimum height=1.4cm, font=\large, line width=1.6pt] at (16.8,1.5) {não exclui clientes ainda não cadastrados};
\node[dbox, draw=dred, text width=5.0cm, minimum height=1.4cm, font=\large, line width=1.6pt] at (16.8,4.4) {exigir cedo demais pode afastar quem só quer ver os produtos};
""")

# ------------------------------------------------------------------ quatro abordagens (simplificar)
w("quatro-abordagens", boxes([
  ("Mais apoio", r"$\bullet$ lembretes de prazo no calendário\\[2pt] $\bullet$ assistentes passo a passo\\[2pt] $\bullet$ ajuda contextual ao lado do campo"),
  ("Tornar visível", r"$\bullet$ barra de progresso do \emph{download}\\[2pt] $\bullet$ indicador de bateria\\[2pt] $\bullet$ ``digitando\ldots'' nos aplicativos de mensagem"),
  ("Automatizar", r"$\bullet$ sincronização automática de arquivos\\[2pt] $\bullet$ correção ortográfica\\[2pt] $\bullet$ endereço preenchido a partir do CEP"),
  ("Mudar a natureza", r"$\bullet$ pagar por aproximação, sem digitar senha\\[2pt] $\bullet$ planilha no lugar da conta em papel\\[2pt] $\bullet$ reunião por videochamada, sem viagem")], w=4.2, h=5.0, cols=4, font=r"\large"))

# ------------------------------------------------------------------ controle x liberdade
w("controle-liberdade", r"""
\tikzset{k/.style={dbox, text width=6.2cm, minimum height=2.6cm, font=\large, line width=1.7pt}}
\node[k, draw=dgreen] (a) at (3.2,3.4) {\textbf{\textcolor{dgreen}{usuário inexperiente}}\\ mais \textbf{assistência}\\ menos alternativas};
\node[k, draw=dorange] (b) at (16.2,3.4) {\textbf{\textcolor{dorange}{usuário experiente}}\\ mais \textbf{liberdade}\\ comanda como quiser};
\draw[dtrans, line width=2.6pt, {Stealth[length=4mm]}-{Stealth[length=4mm]}] (a.east) -- (b.west);
\node[dbox, draw=dblue, fill=white, line width=1.7pt, text width=5.4cm, minimum height=1.6cm, font=\large] at (9.7,3.4) {\textbf{equilíbrio}\\ depende do perfil};
\node[font=\large, text width=17cm, align=center] at (9.7,0.4) {sempre uma \textbf{saída clara}, mas \textbf{mais fácil ficar} no caminho do que sair dele por engano};
""")

# ------------------------------------------------------------------ assistente com botao primario
w("assistente-botoes", r"""
\draw[line width=1.8pt, draw=black!70, fill=white, rounded corners=3pt] (0,0) rectangle (13,7.6);
\draw[line width=1.8pt, draw=black!70, fill=dshade!50] (0,6.6) rectangle (13,7.6);
\node[font=\Large\bfseries, anchor=west] at (0.4,7.1) {Assistente de consulta};
\draw[line width=1.6pt, draw=black!60] (0.6,1.9) rectangle (12.4,6.2);
\draw[line width=1.2pt, draw=black!40] (0.6,1.9) -- (12.4,6.2); \draw[line width=1.2pt, draw=black!40] (0.6,6.2) -- (12.4,1.9);
\node[font=\large, text=black, anchor=west] at (0.7,0.9) {\underline{$<$ Voltar}};
\node[font=\large, text=black, anchor=west] at (3.4,0.9) {\underline{Cancelar}};
\node[font=\large, text=black, anchor=east] at (8.6,0.9) {\underline{Concluir}};
\draw[line width=2.6pt, draw=black, fill=dblue!15, rounded corners=2pt] (9.3,0.3) rectangle (12.4,1.5);
\node[font=\large\bfseries] at (10.85,0.9) {Avançar $>$};
\draw[dred, line width=2pt, -{Stealth[length=3.2mm]}] (14.4,0.9) -- (12.6,0.9);
\node[font=\large\bfseries, dred, anchor=west, text width=4.8cm] at (14.6,1.5) {botão primário claramente indicado};
\node[font=\large, anchor=west, text width=4.8cm] at (14.6,-0.3) {\textbf{\textcolor{dgreen}{sair é possível}}, mas \textbf{ficar é mais fácil}};
""")

# ------------------------------------------------------------------ progresso sem e com cancelar
w("progresso-cancelar", r"""
\tikzset{d/.style={draw=black!70, line width=1.6pt, fill=white, rounded corners=2pt}}
\draw[d] (0,0) rectangle (8,5); \draw[d, fill=dshade!50] (0,4.1) rectangle (8,5);
\node[font=\large\bfseries, anchor=west] at (0.3,4.55) {Realizando busca};
\draw[line width=1.6pt, draw=black!60, fill=dshade!60] (0.5,2.3) rectangle (6.4,3.3);
\node[font=\large\bfseries] at (3.4,2.8) {50\%};
\node[font=\large, anchor=north] at (4.0,-0.2) {\textbf{\textcolor{dred}{sem saída}}: só esperar};
\draw[d] (10.5,0) rectangle (18.5,5); \draw[d, fill=dshade!50] (10.5,4.1) rectangle (18.5,5);
\node[font=\large\bfseries, anchor=west] at (10.8,4.55) {Realizando busca};
\draw[line width=1.6pt, draw=black!60, fill=dshade!60] (11.0,2.9) rectangle (16.9,3.9);
\node[font=\large\bfseries] at (13.9,3.4) {50\%};
\draw[line width=2.2pt, draw=black, fill=white, rounded corners=2pt] (14.4,0.6) rectangle (17.0,1.7);
\node[font=\large\bfseries] at (15.7,1.15) {Cancelar};
\node[font=\large, anchor=north] at (14.5,-0.2) {\textbf{\textcolor{dgreen}{com saída}}: o usuário pode cancelar};
""")

# ------------------------------------------------------------------ confirmacao
w("confirmacao", r"""
\tikzset{d/.style={draw=black!70, line width=1.6pt, fill=white, rounded corners=2pt},
        b/.style={draw=black, line width=1.8pt, fill=white, rounded corners=2pt, minimum width=2.0cm, minimum height=0.9cm, font=\large\bfseries}}
\draw[d] (0,0) rectangle (9,6.4); \draw[d, fill=dshade!50] (0,5.5) rectangle (9,6.4);
\node[font=\large\bfseries, anchor=west] at (0.3,5.95) {Confirma formatação};
\node[font=\large, text width=7.6cm, align=left, anchor=north west] at (0.7,5.1) {\textbf{Todos os arquivos do disco D: serão apagados permanentemente!}\\[6pt] Deseja continuar?};
\node[b] at (2.8,0.9) {Sim}; \node[b] at (5.8,0.9) {Não};
\node[font=\large, anchor=north, text width=8.6cm, align=center] at (4.5,-0.3) {basta apertar \emph{Sim}, quase sem ler: \textbf{\textcolor{dred}{menos seguro}}};
\draw[d] (10.4,0) rectangle (19.4,6.4); \draw[d, fill=dshade!50] (10.4,5.5) rectangle (19.4,6.4);
\node[font=\large\bfseries, anchor=west] at (10.7,5.95) {Confirma formatação};
\node[font=\large, text width=8.0cm, align=left, anchor=north west] at (10.8,5.1) {\textbf{Todos os arquivos do disco D: serão apagados permanentemente!}\\[6pt] Para confirmar, digite a \emph{palavra-secreta}:};
\draw[line width=1.6pt, draw=black!60] (10.8,1.9) rectangle (19.0,2.6);
\node[b, text=black!40, draw=black!40] at (12.6,0.9) {Formatar}; \node[b] at (15.6,0.9) {Cancelar};
\node[font=\large, anchor=north, text width=8.6cm, align=center] at (14.9,-0.3) {exige \textbf{atenção}: \textbf{\textcolor{dgreen}{mais seguro}}};
""")

# ------------------------------------------------------------------ consistencia
w("consistencia", r"""
\tikzset{k/.style={dbox, text width=8.6cm, minimum height=2.6cm, font=\large, line width=1.7pt}}
\node[k, draw=dgreen] at (4.5,6.0) {\textbf{\textcolor{dgreen}{mesma coisa, mesmo nome}}\\ não alternar \emph{Salvar} e \emph{Gravar} no mesmo sistema};
\node[k, draw=dgreen] at (14.2,6.0) {\textbf{\textcolor{dgreen}{mesma situação, mesma ação}}\\ o botão \emph{Fechar} não cancela aqui e confirma ali};
\node[k, draw=dorange] at (4.5,2.8) {\textbf{\textcolor{dorange}{comportamento diferente, aparência diferente}}\\ selecionar uma opção $\neq$ disparar uma ação};
\node[k, draw=dblue] at (14.2,2.8) {\textbf{\textcolor{dblue}{o que se faz sem pensar}}\\ teclas de atalho e roda do mouse: iguais em todo o sistema};
\node[dbox, draw=dred, dashed, fill=dred!6, line width=1.6pt, text width=18.4cm, minimum height=1.3cm, font=\large] at (9.35,0.2) {exceção: \textbf{inconsistência proposital}, para o usuário não agir no automático (\emph{Sim}/\emph{Não} trocados por rótulos que dizem o efeito)};
""")

# ------------------------------------------------------------------ novato x experiente (eficiencia)
w("aceleradores", r"""
\tikzset{k/.style={dbox, text width=5.6cm, minimum height=2.6cm, font=\large, line width=1.7pt}}
\node[k, draw=dgreen] (a) at (3.0,3.6) {\textbf{\textcolor{dgreen}{uso ocasional}}\\ menus e botões\\ ajuda à mão};
\node[k, draw=dorange] (b) at (16.4,3.6) {\textbf{\textcolor{dorange}{uso frequente}}\\ \textbf{teclas de atalho} (Ctrl+S)\\ \textbf{macros} e \textbf{perfis}};
\draw[dtrans, line width=2.8pt, -{Stealth[length=4.5mm]}] (6.2,3.6) -- (13.2,3.6);
\node[font=\large\bfseries, dblue] at (9.7,4.4) {mais uso};
\node[font=\large, text width=6cm, align=center] at (9.7,2.7) {mais vontade de \textbf{reduzir os passos}};
\node[font=\large, text width=17cm, align=center] at (9.7,0.4) {os \textbf{aceleradores} não atrapalham o novato: ficam como \textbf{atalhos opcionais}};
""")

# ------------------------------------------------------------------ defaults (newsletter)
def _card(x, tit, rot, cor, txt, sel=False, obrig=False):
    q = r"\textbf{Quer receber a \emph{newsletter}?}" + (" *" if obrig else "")
    o = r"\draw[draw=black!70, line width=1.6pt, fill=white, rounded corners=3pt] (%s,3.2) rectangle (%s,7.2);" % (x, x + 5.9)
    o += r"\node[font=\large, anchor=north west, text width=5.5cm] at (%s,7.1) {%s};" % (x + 0.2, q)
    o += r"\draw[black, line width=1.6pt] (%s,4.9) circle (0.22); \node[font=\large, anchor=west] at (%s,4.9) {sim};" % (x + 0.6, x + 1.0)
    o += r"\draw[black, line width=1.6pt] (%s,3.9) circle (0.22); \node[font=\large, anchor=west] at (%s,3.9) {não};" % (x + 0.6, x + 1.0)
    if sel: o += r"\fill[black] (%s,4.9) circle (0.12);" % (x + 0.6)
    o += r"\node[font=\large\bfseries, anchor=north] at (%s,2.8) {\textcolor{%s}{%s}};" % (x + 2.95, cor, tit)
    o += r"\node[font=\large, anchor=north, text width=5.6cm, align=center] at (%s,2.1) {%s};" % (x + 2.95, txt)
    return o
w("defaults", "\n".join([
  _card(0.0, "pré-selecionado", None, "dred", r"a maioria aceita: \textbf{induz} à opção", sel=True),
  _card(6.6, "sem seleção", None, "dgreen", r"\textbf{neutro}, mas pede uma escolha"),
  _card(13.2, "campo obrigatório", None, "dorange", r"\textbf{exige} a resposta (* indica obrigatório)", obrig=True),
  r"\node[font=\Large\bfseries] at (9.6,8.3) {Cada alternativa é eficiente? neutra? induz?};"]))

# ------------------------------------------------------------------ tempos de feedback
w("feedback-tempos", r"""
\tikzset{k/.style={dbox, text width=4.2cm, minimum height=3.9cm, font=\large, line width=1.7pt}}
\draw[line width=3pt, draw=black!80, -{Stealth[length=4mm]}] (0,2.6) -- (19.2,2.6);
\foreach \x/\t in {1.9/{50 ms}, 6.9/{0,5 a 2 s}, 11.9/{mais de 2 s}, 16.9/{mais de 10 s}} {\fill[black] (\x,2.6) circle (0.17); \node[font=\Large\bfseries, anchor=north] at (\x,2.2) {\t};}
\node[k, draw=dgreen, text width=3.9cm] at (1.9,5.4) {\textbf{\textcolor{dgreen}{imediato}}\\ \emph{feedback} no botão, visual ou sonoro};
\node[k, draw=dblue, text width=3.9cm] at (6.9,5.4) {\textbf{\textcolor{dblue}{ocupado}}\\ sinalizar que não travou (ampulheta animada)};
\node[k, draw=dorange, text width=3.9cm] at (11.9,5.4) {\textbf{\textcolor{dorange}{progresso}}\\ tempo estimado, barra e opção de cancelar ou suspender};
\node[k, draw=dred, text width=3.9cm] at (16.9,5.4) {\textbf{\textcolor{dred}{conclusão}}\\ som e sinal visual destacado ao terminar};
\foreach \x in {1.9,6.9,11.9,16.9} {\draw[line width=1.2pt, black] (\x,3.4) -- (\x,2.8);}
\node[font=\large, text width=18cm, align=center] at (9.6,0.5) {tempo desde o clique, sem resposta do sistema};
""")

# ------------------------------------------------------------------ feedback sutil x destacado
w("feedback-sutil-destacado", r"""
\tikzset{d/.style={draw=black!70, line width=1.6pt, fill=white, rounded corners=3pt}}
\node[font=\Large\bfseries, dgreen] at (4.8,7.6) {sutil};
\draw[d] (0,3.4) rectangle (9.6,6.9); 
\draw[line width=1.6pt, draw=dgreen, fill=dgreen!12] (0,5.3) rectangle (9.6,6.9);
\node[font=\large, anchor=west, text width=9cm] at (0.3,6.1) {\textbf{\textcolor{dgreen}{ok}}\ Material incluído com sucesso};
\node[font=\large, anchor=west, text width=9cm] at (0.4,4.4) {Disciplina INF9999: lista de materiais};
\node[font=\large, text width=9.6cm, align=center, anchor=north] at (4.8,3.0) {ação \textbf{frequente} e com resultado \textbf{esperado}};
\node[font=\Large\bfseries, dred] at (14.4,7.6) {destacado};
\draw[d] (9.8,2.0) rectangle (19.2,6.9); \draw[d, fill=dshade!50] (9.8,6.0) rectangle (19.2,6.9);
\node[font=\large\bfseries, anchor=west] at (10.1,6.45) {Problema no \emph{upload} do arquivo};
\draw[line width=2.2pt, draw=dred] (11.1,3.6) circle (0.5); \node[font=\large\bfseries, dred] at (11.1,3.6) {x};
\node[font=\large, anchor=west, text width=6.6cm] at (12.0,4.4) {Houve um problema no envio, talvez por falha de conexão.};
\node[font=\large\bfseries, anchor=west, draw=black, line width=1.8pt, rounded corners=2pt, minimum height=0.9cm] at (12.0,2.9) {Tentar novamente};
\node[font=\large, text width=9.4cm, align=center, anchor=north] at (14.5,1.6) {ação \textbf{infrequente} ou de \textbf{grande consequência}};
""")

# ------------------------------------------------------------------ maximas de Grice
w("maximas-grice", boxes([
  ("Qualidade", "não dizer o que se sabe falso ou sem evidência"),
  ("Quantidade", "só a informação necessária: \\emph{menos é mais}"),
  ("Relação", "tudo o que se diz deve ser relevante ao objetivo"),
  ("Modo", "evitar prolixidade e ambiguidade; ser claro e ordenado")], w=4.1, h=3.4, cols=4,
  cap=r"a interação polida segue as \textbf{máximas da conversa cooperativa} (Grice, 1975)", capw=18))

# ------------------------------------------------------------------ rotulos de menu
w("rotulos-menu", r"""
\tikzset{m/.style={draw=black!70, line width=1.6pt, fill=white, text width=7.0cm, minimum height=0.95cm, font=\large, anchor=west, inner sep=8pt}}
\node[font=\Large\bfseries, dred] at (4.4,6.4) {verbos variados};
\node[m] at (0.9,5.1) {Inserir Quebra de Página};
\node[m] at (0.9,4.15) {Acrescentar Nota de Rodapé};
\node[m] at (0.9,3.2) {Construir Tabela};
\node[font=\large, text width=8.4cm, align=center, anchor=north] at (4.4,2.4) {mais \textbf{precisos}, mas cada verbo exige \textbf{decodificação}};
\node[font=\Large\bfseries, dgreen] at (14.6,6.4) {mesmo verbo, varredura rápida};
\node[m] at (11.1,5.1) {Inserir Quebra de Página};
\node[m] at (11.1,4.15) {Inserir Nota de Rodapé};
\node[m] at (11.1,3.2) {Inserir Tabela};
\node[font=\large, text width=8.4cm, align=center, anchor=north] at (14.6,2.4) {o usuário \textbf{varre} as opções \textbf{mais rápido}};
""")

# ------------------------------------------------------------------ cor com dica secundaria
w("cor-dica-secundaria", r"""
\tikzset{k/.style={dbox, text width=5.6cm, minimum height=4.9cm, font=\large, line width=1.7pt}}
\node[k, draw=dred] at (3.0,4.0) {\textbf{\textcolor{dred}{só a cor}}\\[10pt] \tikz{\fill[dred!70] (0,0) circle (0.45); \fill[dgreen!70] (1.4,0) circle (0.45);}\\[10pt] quem não distingue as cores perde a informação};
\node[k, draw=dgreen] at (9.9,4.0) {\textbf{\textcolor{dgreen}{cor + dica secundária}}\\[6pt] \tikz{\fill[dred!70] (0,0) circle (0.45); \node[font=\large\bfseries, white] at (0,0) {x}; \fill[dgreen!70] (1.9,0) circle (0.45); \node[font=\large\bfseries, white] at (1.9,0) {ok};}\\[6pt] ícone, rótulo ou tom de cinza diferente};
\node[k, draw=dorange, text width=4.8cm] at (16.7,4.0) {\textbf{\textcolor{dorange}{por quê?}}\\[8pt] daltonismo: cerca de \textbf{10\%} dos homens\\[4pt] e limitações do dispositivo};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (6.1,4.0) -- (6.8,4.0);
""")

# ------------------------------------------------------------------ erros: evitar, detectar, recuperar
w("erros-etapas", flow([
  ("Evitar", "projetar para que o erro não ocorra: ações perigosas difíceis, desfazer fácil"),
  ("Detectar", "o sistema reconhece o erro e avisa em linguagem simples"),
  ("Recuperar", "indicar o problema e sugerir uma solução construtiva")],
  w=5.2, h=3.8, cap=r"assuma que \textbf{qualquer erro possível será cometido}", capw=18))

# ------------------------------------------------------------------ botoes perigosos
w("botoes-perigosos", r"""
\tikzset{d/.style={draw=black!70, line width=1.6pt, fill=white, rounded corners=2pt},
        b/.style={draw=black, line width=1.8pt, fill=white, rounded corners=2pt, minimum height=0.95cm, font=\normalsize\bfseries, inner sep=6pt}}
\draw[d] (0,0.4) rectangle (9.2,5.8); \draw[d, fill=dshade!50] (0,4.9) rectangle (9.2,5.8);
\node[font=\large\bfseries, anchor=west] at (0.3,5.35) {Status da conexão};
\node[font=\large, anchor=west] at (0.5,4.2) {Duração: 1:52:37};
\node[font=\large, anchor=west] at (0.5,3.4) {Velocidade: 100 Mbps};
\node[b, anchor=west] at (0.3,1.4) {Propriedades...}; \node[b, anchor=west, draw=dred, line width=2.6pt] at (3.9,1.4) {Desabilitar}; \node[b, anchor=east] at (8.8,1.4) {Fechar};
\node[font=\large, text width=9cm, align=center, anchor=north] at (4.6,0.1) {uso \textbf{frequente} colado a uma ação de \textbf{consequência grave}};
\draw[d] (10.3,0.4) rectangle (19.5,5.8); \draw[d, fill=dshade!50] (10.3,4.9) rectangle (19.5,5.8);
\node[font=\large\bfseries, anchor=west] at (10.6,5.35) {Status da conexão};
\node[font=\large, anchor=west] at (10.8,4.2) {Duração: 1:52:37};
\node[font=\large, anchor=west] at (10.8,3.4) {Velocidade: 100 Mbps};
\node[b, anchor=west] at (10.7,1.4) {Propriedades...}; \node[b, anchor=east] at (19.1,1.4) {Fechar};
\node[b, anchor=west, draw=dgreen, line width=2.6pt] at (10.7,2.45) {Desabilitar};
\node[font=\large, text width=9cm, align=center, anchor=north] at (14.9,0.1) {ação perigosa \textbf{afastada} dos controles de uso frequente};
""")

# ------------------------------------------------------------------ mensagem de erro
w("mensagem-erro", r"""
\tikzset{d/.style={draw=black!70, line width=1.6pt, fill=white, rounded corners=2pt, text width=8.6cm, minimum height=4.3cm, anchor=north west, inner sep=0pt},
        b/.style={draw=black, line width=1.8pt, fill=white, rounded corners=2pt, minimum height=0.95cm, font=\large\bfseries, inner sep=7pt}}
\draw[d] (0,5.6) rectangle (9.2,0.6) ; \draw[d, fill=dshade!50] (0,4.7) rectangle (9.2,5.6);
\node[font=\large\bfseries, anchor=west] at (0.3,5.15) {Problema no \emph{upload}};
\draw[line width=2.2pt, draw=dred] (1.0,3.4) circle (0.5); \node[font=\large\bfseries, dred] at (1.0,3.4) {x};
\node[font=\large, anchor=west, text width=6.8cm] at (1.9,3.5) {Houve um problema no envio, talvez por falha de conexão.};
\node[b] at (7.6,1.4) {OK};
\node[font=\large, text width=9cm, align=center, anchor=north] at (4.6,0.3) {\textbf{\textcolor{dred}{sem saída}}: só fechar o aviso};
\draw[d] (10.3,5.6) rectangle (19.5,0.6); \draw[d, fill=dshade!50] (10.3,4.7) rectangle (19.5,5.6);
\node[font=\large\bfseries, anchor=west] at (10.6,5.15) {Problema no \emph{upload}};
\draw[line width=2.2pt, draw=dred] (11.3,3.4) circle (0.5); \node[font=\large\bfseries, dred] at (11.3,3.4) {x};
\node[font=\large, anchor=west, text width=6.8cm] at (12.2,3.5) {Houve um problema no envio, talvez por falha de conexão.};
\node[b, anchor=west] at (10.6,1.4) {Tentar novamente}; \node[font=\normalsize, anchor=west, text width=3.4cm, align=left] at (15.5,1.4) {\underline{$<$ Voltar à edição}};
\node[font=\large, text width=9cm, align=center, anchor=north] at (14.9,0.3) {\textbf{\textcolor{dgreen}{com recuperação}}: retoma o caminho produtivo};
""")

# ------------------------------------------------------------------ descricao de padroes
w("descricao-padroes", boxes([
  ("Título", "nome curto, fácil de lembrar (ex.: painéis colapsáveis)"),
  ("O que", "a solução resumida em um parágrafo curto"),
  ("Quando usar", "as situações em que o padrão se aplica e as forças em jogo"),
  ("Por quê", "dados que justificam o padrão na situação"),
  ("Como", "a solução em detalhe e como implementá-la"),
  ("Exemplos", "diagramas e imagens de interfaces concretas")], w=5.4, h=2.6, cols=3))

# ------------------------------------------------------------------ acordeao
w("acordeao", r"""
\tikzset{p/.style={draw=black!70, line width=1.6pt, fill=dshade!55, minimum width=7.0cm, minimum height=0.95cm, font=\large\bfseries, anchor=west, inner sep=8pt}}
\node[p] at (0,6.8) {> Páginas mestres};
\node[p, fill=dblue!22] at (0,5.85) {v Layouts};
\draw[draw=black!70, line width=1.6pt, fill=white] (0,3.0) rectangle (7.0,5.4);
\foreach \x in {0.4,2.6,4.8} {\foreach \y in {4.2,3.3} {\draw[black!55, line width=1.4pt, fill=dcream] (\x,\y) rectangle (\x+1.8,\y+0.7);}}
\node[p] at (0,2.5) {> Modelos de tabela};
\node[p] at (0,1.55) {> Animação personalizada};
\node[dbox, draw=dgreen, text width=5.2cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (11.0,5.6) {\textbf{\textcolor{dgreen}{vantagem}}\\ comprime muitos itens em pouco espaço};
\node[dbox, draw=dred, text width=5.2cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (11.0,2.9) {\textbf{\textcolor{dred}{desvantagem}}\\ os itens dos outros painéis ficam ocultos};
\node[dbox, draw=dblue, text width=5.2cm, minimum height=1.6cm, font=\large, line width=1.7pt] at (16.9,4.3) {\textbf{um painel} aberto de cada vez};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (7.2,5.85) -- (8.2,5.6);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (7.2,5.0) -- (8.2,3.4);
""")

# ------------------------------------------------------------------ persuasivo x coercivo
w("persuasivo-coercivo", r"""
\tikzset{k/.style={dbox, text width=7.2cm, minimum height=3.0cm, font=\large, line width=1.7pt}}
\node[k, draw=dgreen] (a) at (3.8,3.4) {\textbf{\textcolor{dgreen}{persuasivo}}\\ influencia decisões\\ e ações, em geral a favor do \textbf{usuário}};
\node[k, draw=dred] (b) at (15.4,3.4) {\textbf{\textcolor{dred}{\emph{deceptive pattern}}}\\ princípios de persuasão levados ao \textbf{exagero}: \textbf{coercivo}, em detrimento do usuário};
\draw[dtrans, line width=2.6pt, -{Stealth[length=4mm]}] (a.east) -- (b.west);
\node[font=\large\bfseries] at (9.6,4.1) {exagero};
\node[font=\large, text width=17cm, align=center] at (9.6,0.5) {persuasão não é antiética por natureza: depende da \textbf{intenção} de quem projeta e da \textbf{forma} de uso};
""")

# ------------------------------------------------------------------ taxonomia de Gray
w("gray-taxonomia", boxes([
  ("Incômodo repetitivo", "\\emph{Nagging}: pedidos insistentes e repetidos"),
  ("Obstrução", "\\emph{Obstruction}: obstáculos que desencorajam uma ação"),
  ("Ação sorrateira", "\\emph{Sneaking}: ocultar, disfarçar ou atrasar informações"),
  ("Interferência na interface", "\\emph{Interface Interference}: privilegiar certas ações"),
  ("Ação forçada", "\\emph{Forced Action}: exigir uma ação desnecessária")], w=5.2, h=3.2, cols=3,
  cap=r"Gray et al. (2018), a partir dos exemplos do site de Brignull", capw=17))

# ------------------------------------------------------------------ exemplo: incomodo repetitivo
w("dp-incomodo", r"""
\draw[draw=black!70, line width=1.8pt, fill=white, rounded corners=6pt] (0,0) rectangle (6.8,8.4);
\node[font=\large\bfseries, anchor=west] at (0.4,8.0) {23:00};
\foreach \i/\d in {0/{15/04}, 1/{14/04}, 2/{13/04}, 3/{12/04}, 4/{11/04}} {
  \draw[draw=black!50, line width=1.3pt, fill=dshade!55] (0.3,{6.4-\i*1.4}) rectangle (6.5,{7.5-\i*1.4});
  \node[font=\normalsize\bfseries, anchor=west] at (0.5,{7.22-\i*1.4}) {Loja Express \d};
  \node[font=\normalsize, anchor=west] at (0.5,{6.72-\i*1.4}) {Hoje é sua última oportunidade!};}
\draw[decorate, decoration={brace, amplitude=8pt, mirror}, line width=2pt, dred] (6.8,0.3) -- (6.8,7.6);
\node[font=\large, anchor=west, text width=9cm] at (8.0,5.8) {a \textbf{mesma mensagem} todos os dias: \textbf{\textcolor{dred}{todo dia é o dia da ``última oportunidade''}}};
\node[font=\large, anchor=west, text width=9cm] at (8.0,3.2) {o sistema tenta convencer o usuário \textbf{por exaustão}, na esperança de que o incômodo pare};
\node[font=\large, anchor=west, text width=9cm] at (8.0,1.0) {também em \emph{e-mails} e \emph{pop-ups}};
""")

# ------------------------------------------------------------------ exemplo: obstrucao
w("dp-obstrucao", r"""
\tikzset{f/.style={draw=black!60, line width=1.4pt, fill=white, minimum width=8.4cm, minimum height=0.8cm, anchor=west}}
\node[font=\Large\bfseries, dgreen] at (4.2,8.6) {assinar: 1 passo};
\draw[draw=black!70, line width=1.8pt, fill=white, rounded corners=3pt] (0,5.4) rectangle (8.8,8.0);
\node[font=\large\bfseries, anchor=west] at (0.4,7.4) {Boletim Bem Estar};
\node[font=\large, anchor=west, draw=black, line width=1.8pt, fill=dblue!15, rounded corners=2pt, minimum height=1.0cm] at (0.4,6.1) {Assinar};
\node[font=\Large\bfseries, dred] at (14.0,8.6) {descadastrar: vários passos};
\draw[draw=black!70, line width=1.8pt, fill=white, rounded corners=3pt] (9.6,0) rectangle (18.9,8.0);
\node[font=\large\bfseries, anchor=west] at (10.0,7.4) {Boletim Bem Estar};
\node[font=\normalsize, anchor=west] at (10.0,6.7) {Para se descadastrar, preencha o formulário:};
\node[f] at (10.0,5.8) {}; \node[font=\normalsize, anchor=west] at (10.2,5.8) {Nome *};
\node[f] at (10.0,4.8) {}; \node[font=\normalsize, anchor=west] at (10.2,4.8) {E-mail *};
\draw[draw=black!60, line width=1.4pt, fill=white] (10.0,2.8) rectangle (18.4,4.3); \node[font=\normalsize, anchor=north west] at (10.2,4.2) {Razões para se descadastrar *};
\draw[draw=black!60, line width=1.4pt, fill=white] (10.0,1.0) rectangle (18.4,2.5); \node[font=\normalsize, anchor=north west] at (10.2,2.4) {Como falaria de nós para conhecidos? *};
\node[font=\large, text width=8.8cm, align=center, anchor=north] at (4.4,4.6) {\textbf{\textcolor{dred}{sair} custa mais do que entrar}:\\ campos obrigatórios desnecessários \emph{(descadastrar não depende desses dados)}};
""")

# ------------------------------------------------------------------ exemplo: acao sorrateira
w("dp-sorrateira", r"""
\tikzset{d/.style={draw=black!70, line width=1.6pt, fill=white, rounded corners=3pt}}
\draw[d] (0,0) rectangle (10.4,6.8);
\node[font=\Large\bfseries, anchor=west] at (0.4,6.2) {Resumo da reserva};
\node[font=\large, anchor=west] at (0.4,5.1) {Assento regular \hfill R\$ 100,00};
\node[font=\large, anchor=west] at (0.4,4.3) {Assento regular \hfill R\$ 100,00};
\node[font=\large\bfseries, anchor=west, text=dred] at (0.4,3.5) {Seleção de assentos \quad R\$ 25,00};
\node[font=\large\bfseries, anchor=west] at (0.4,2.6) {Subtotal: R\$ 225,00};
\node[font=\large\bfseries, draw=black, line width=2.0pt, fill=dblue!15, rounded corners=2pt, minimum width=9.4cm, minimum height=1.1cm] at (5.2,1.5) {Confirmar};
\node[font=\tiny, anchor=north] at (5.2,0.8) {\underline{Avançar sem seleção de assentos}};
\node[dbox, draw=dred, text width=7.6cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (15.4,4.8) {\textbf{custo extra} pré-selecionado: parece um passo \textbf{obrigatório}};
\node[dbox, draw=dorange, text width=7.6cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (15.4,1.7) {a opção de \textbf{avançar sem isso} é um \textbf{link minúsculo}};
\draw[dred, line width=2pt, -{Stealth[length=3.2mm]}] (11.6,4.8) -- (10.6,3.5);
\draw[dorange, line width=2pt, -{Stealth[length=3.2mm]}] (11.6,1.7) -- (8.6,0.8);
""")

# ------------------------------------------------------------------ exemplo: interferencia
w("dp-interferencia", r"""
\draw[draw=black!70, line width=1.8pt, fill=white, rounded corners=3pt] (0,0) rectangle (10.8,7.6);
\node[font=\Large\bfseries] at (5.4,6.8) {Clube da Barganha};
\node[font=\normalsize, text width=9.4cm, align=center] at (5.4,5.5) {Junte-se a nós! Receba vantagens e benefícios instalando um \emph{plugin}.};
\node[font=\Large\bfseries, draw=black, line width=2.2pt, fill=dblue!20, rounded corners=3pt, minimum width=8.2cm, minimum height=1.5cm] at (5.4,3.5) {Quero benefícios!};
\node[font=\tiny, text width=9.4cm, align=center] at (5.4,1.4) {\underline{Não gosto de benefícios e prefiro pagar preços mais caros pelos mesmos produtos}};
\node[dbox, draw=dred, text width=6.8cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (15.6,5.4) {botão \textbf{grande} e atraente \emph{versus} texto \textbf{pequeno}, sem aparência de link};
\node[dbox, draw=dorange, text width=6.8cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (15.6,2.2) {a linguagem \textbf{constrange} o usuário a aceitar: \textbf{emocionalmente abusiva}};
\draw[dred, line width=2pt, -{Stealth[length=3.2mm]}] (12.1,5.0) -- (8.8,3.6);
\draw[dorange, line width=2pt, -{Stealth[length=3.2mm]}] (12.1,2.0) -- (10.2,1.4);
""")

# ------------------------------------------------------------------ exemplo: acao forcada
w("dp-forcada", r"""
\draw[draw=black!70, line width=1.8pt, fill=white, rounded corners=3pt] (0,0) rectangle (10.8,7.6);
\node[font=\Large\bfseries, anchor=west] at (0.4,6.9) {Trilhos de Ouro};
\node[font=\Large\bfseries] at (5.4,5.3) {Seu agendamento está confirmado.};
\node[font=\Large\bfseries, draw=black, line width=2.2pt, fill=dblue!20, rounded corners=3pt, minimum width=4.6cm, minimum height=1.3cm] at (5.4,3.8) {Continuar};
\draw[draw=black!50, line width=1.3pt, fill=dshade!50] (0,0) rectangle (10.8,1.9);
\node[font=\normalsize, anchor=west] at (0.4,1.4) {Você vai para São Paulo!};
\node[font=\LARGE\bfseries, anchor=west] at (0.4,0.6) {XYKZ987};
\node[dbox, draw=dred, text width=6.8cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (15.6,5.3) {\textbf{Continuar} parece o próximo passo, mas leva a um \textbf{cadastro em outro sistema}};
\node[dbox, draw=dgreen, text width=6.8cm, minimum height=2.0cm, font=\large, line width=1.7pt] at (15.6,1.9) {a compra \textbf{já foi concluída}: o código de confirmação está na parte de baixo};
\draw[dred, line width=2pt, -{Stealth[length=3.2mm]}] (12.1,5.0) -- (8.0,3.9);
\draw[dgreen, line width=2pt, -{Stealth[length=3.2mm]}] (12.1,1.9) -- (8.0,0.8);
""")

# ------------------------------------------------------------------ taxonomia de Mathur
w("mathur-taxonomia", boxes([
  ("Assimetria de informação", "\\emph{Asymmetric}: impor preferência por certas escolhas"),
  ("Ocultação de efeitos", "\\emph{Covert}: esconder como as decisões afetam o usuário"),
  ("Enganação", "\\emph{Deceptive}: levar o usuário a acreditar em falsidades"),
  ("Ocultação de informações", "\\emph{Hides Information}: obscurecer ou atrasar o que é relevante"),
  ("Restrição de ações", "\\emph{Restrictive}: limitar as escolhas disponíveis")], w=5.2, h=3.2, cols=3,
  cap=r"Mathur et al. (2019)", capw=17))

# ------------------------------------------------------------------ gray x mathur (cruzamento)
w("gray-mathur", r"""
\tikzset{k/.style={dbox, text width=6.4cm, minimum height=2.6cm, font=\large, line width=1.7pt}}
\node[font=\Large\bfseries, dblue] at (3.6,7.2) {mecanismo};
\node[font=\large, anchor=north] at (3.6,6.8) {Gray et al. (2018)};
\node[k, draw=dblue] (a) at (3.6,4.8) {\textbf{\textcolor{dblue}{Ação sorrateira}}\\ assentos pré-selecionados, com custo extra};
\node[font=\Large\bfseries, dgreen] at (15.6,7.2) {fim almejado};
\node[font=\large, anchor=north] at (15.6,6.8) {Mathur et al. (2019)};
\node[k, draw=dgreen] (b) at (15.6,4.8) {\textbf{\textcolor{dgreen}{Enganação}}\\ o usuário acredita que a marcação é obrigatória};
\draw[dtrans, line width=2.4pt, -{Stealth[length=4mm]}] (a.east) -- (b.west) node[midway, above, font=\large\bfseries, text=black] {leva a};
\node[dbox, draw=dorange, text width=16.4cm, minimum height=2.2cm, font=\large, line width=1.7pt] at (9.6,1.2) {as classificações são \textbf{complementares}: uma olha os \textbf{mecanismos}, a outra os \textbf{fins}. Juntas mostram \textbf{que informação oculta} leva à falsidade e \textbf{que parte da solução} rever};
""")

# ------------------------------------------------------------------ consequencias dos dark patterns
w("dark-consequencias", flow([
  ("Interesse do criador", "o benefício do sistema vem antes do usuário"),
  ("Vieses cognitivos", "tendências de decisão exploradas para induzir ações"),
  ("Prejuízo", "gastos desnecessários, dados cedidos, ansiedade e distração")],
  w=5.2, h=3.2, cap=r"ao usar \emph{deceptive patterns}, o criador assume uma postura \textbf{antiética}", capw=18) + r"""
\node[dbox, draw=dgreen, dashed, fill=dgreen!6, line width=1.7pt, text width=16.4cm, minimum height=1.6cm, font=\large] at (6.3,-4.2) {\textbf{LGPD}: transparência no uso dos dados, controle do usuário e \emph{privacy by design}; induzir o usuário a compartilhar dados pode violar a lei, com multas};
""")

# ------------------------------------------------------------------ escopos do guia de estilo
w("escopos-guia", boxes([
  ("Plataforma", "dispositivo e sistema operacional"),
  ("Corporativo", "padronização entre os produtos de uma empresa"),
  ("Família de produtos", "consistência entre produtos relacionados"),
  ("Produto específico", "decisões de um único produto")], w=4.2, h=3.0, cols=4,
  cap=r"o guia registra as \textbf{decisões de design} para que não se percam", capw=18))

# ------------------------------------------------------------------ elementos de Marcus
w("marcus-elementos", boxes([
  ("Layout", "proporção, \\emph{grids}, metáforas espaciais"),
  ("Tipografia", "uso em diálogos, formulários e relatórios"),
  ("Simbolismo", "clareza e consistência dos ícones"),
  ("Cores", "regras de uso de cores"),
  ("Visualização", "gráficos, diagramas e mapas"),
  ("Telas e \\emph{widgets}", "design de telas e elementos de interface")], w=5.4, h=2.6, cols=3))

# ------------------------------------------------------------------ estrutura do guia
w("estrutura-guia", boxes([
  ("1. Introdução", "objetivo, público, como usar e manter"),
  ("2. Análise", "ambiente de trabalho do usuário"),
  ("3. Elementos de interface", "grid, janelas, tipografia, símbolos, cores, animações"),
  ("4. Elementos de interação", "estilos de interação e aceleradores"),
  ("5. Elementos de ação", "preencher campos, selecionar, ativar"),
  ("6. Vocabulário e padrões", "terminologia, tipos de tela, sequências de diálogos")], w=5.4, h=2.8, cols=3))

# ------------------------------------------------------------------ usar bem o guia
w("guia-usar-bem", boxes([
  ("Comunicar", "divulgar a existência e a importância do guia"),
  ("Treinar", "oferecer treinamento à equipe"),
  ("Facilitar", "acesso ao guia todo ou a um tópico"),
  ("Mudar a cultura", "de design e desenvolvimento da equipe")], w=4.2, h=3.0, cols=4,
  cap=r"o guia é parte de um \textbf{processo reflexivo de design}, não um conjunto de regras prontas", capw=18))

# ------------------------------------------------------------------ padroes: vantagens e cuidados
w("padroes-vantagens-cuidados", r"""
\tikzset{k/.style={dbox, text width=5.2cm, minimum height=1.9cm, font=\large, line width=1.7pt}}
\node[font=\Large\bfseries, dgreen, anchor=west] at (0.0,8.0) {o que um padrão oferece};
\node[k, draw=dgreen] at (2.9,6.2) {\textbf{sabedoria coletiva} de designers experientes};
\node[k, draw=dgreen] at (9.7,6.2) {\textbf{vocabulário comum} para a equipe};
\node[k, draw=dgreen] at (16.5,6.2) {\textbf{divulgação} de boas soluções};
\node[font=\Large\bfseries, dred, anchor=west] at (0.0,4.3) {o que um padrão não é};
\node[k, draw=dred, dashed] at (2.9,2.5) {\textbf{solução pronta} para copiar};
\node[k, draw=dred, dashed] at (9.7,2.5) {\textbf{regra} ou \textbf{heurística}};
\node[k, draw=dred, dashed] at (16.5,2.5) {\textbf{receita} do projeto inteiro};
\node[dbox, draw=dblue, fill=dblue!6, line width=1.8pt, text width=18.6cm, minimum height=1.4cm, font=\large] at (9.7,0.0) {um \textbf{recurso} para problemas pontuais, em um processo de design \textbf{reflexivo}; \textbf{não garante} a qualidade};
""")

# ------------------------------------------------------------------ linguagem de padroes (rede em torno do Acordeao)
w("linguagem-padroes", r"""
\tikzset{n/.style={dbox, text width=4.2cm, minimum height=1.5cm, font=\large\bfseries, line width=1.7pt},
        e/.style={dtrans, line width=1.8pt, -{Stealth[length=3mm]}},
        l/.style={midway, fill=dcream, inner sep=2pt, font=\normalsize, text=black, text width=3.6cm, align=center}}
\draw[draw=dblue, dashed, line width=1.8pt, rounded corners=14pt, fill=dblue!4] (-0.6,-2.2) rectangle (20.0,9.8);
\node[font=\Large\bfseries, dblue, anchor=north west] at (-0.2,9.6) {linguagem de padrões};
\node[n, draw=dorange, line width=2.6pt, fill=white] (a) at (9.7,4.4) {Acordeão};
\node[n, draw=dgreen] (g) at (2.9,7.8) {Guias};
\node[n, draw=dgreen] (t) at (16.5,7.8) {Árvores de navegação};
\node[n, draw=dgreen] (p) at (2.9,0.8) {Painéis colapsáveis};
\node[n, draw=dgreen] (f) at (16.5,0.8) {Perguntas frequentes (FAQ)};
\node[n, draw=dred, dashed] (s) at (9.7,-1.0) {Assistente};
\draw[e] (a) -- (g) node[l] {equivalente conceitualmente};
\draw[e] (a) -- (t) node[l] {solução alternativa};
\draw[e] (a) -- (p) node[l] {se mais de um painel pode ficar aberto};
\draw[e] (a) -- (f) node[l] {bom uso: uma pergunta aberta por vez};
\draw[e] (a) -- (s) node[l, pos=0.45, text width=3.0cm] {uso não recomendado};
""")

# ------------------------------------------------------------------ linguagem de padroes de navegacao (em camadas)
w("linguagem-padroes-camadas", r"""
\tikzset{n/.style={dbox, text width=3.7cm, minimum height=1.6cm, font=\large\bfseries, line width=1.8pt},
        e/.style={dtrans, line width=2pt, -{Stealth[length=3.2mm]}}}
\fill[dblue!8, rounded corners=8pt] (-0.4,7.2) rectangle (23.0,9.6);
\fill[dgreen!8, rounded corners=8pt] (-0.4,3.6) rectangle (23.0,6.8);
\fill[dorange!8, rounded corners=8pt] (-0.4,0.0) rectangle (23.0,3.2);
\node[font=\large\bfseries, dblue, anchor=west, text width=3.0cm] at (0.0,8.4) {padrões maiores};
\node[font=\large\bfseries, dgreen, anchor=west, text width=3.0cm] at (0.0,5.2) {padrões intermediários};
\node[font=\large\bfseries, dorange, anchor=west, text width=3.0cm] at (0.0,1.6) {padrões menores};
\node[n, draw=dblue, text width=4.4cm] (nav) at (9.4,8.4) {Navegação do site};
\node[n, draw=dblue, text width=4.4cm] (faq) at (18.9,8.4) {Seção de perguntas frequentes};
\node[n, draw=dgreen] (g) at (6.2,5.2) {Guias};
\node[n, draw=dgreen] (t) at (10.8,5.2) {Árvores de navegação};
\node[n, draw=dgreen] (a) at (15.4,5.2) {Acordeão};
\node[n, draw=dred, dashed] (w) at (20.6,5.2) {Assistente};
\node[n, draw=dorange] (b) at (10.8,1.6) {Trilha de navegação};
\node[n, draw=dorange] (p) at (15.4,1.6) {Painéis colapsáveis};
\draw[e] (nav) -- (g); \draw[e] (nav) -- (t); \draw[e] (nav) -- (a);
\draw[e] (faq) -- (a);
\draw[e] (t) -- (b);
\draw[e] (a) -- (p);
\draw[dred, line width=2pt, dashed, -{Stealth[length=3.2mm]}] (w.west) -- (a.east);
\node[font=\large, anchor=west, text width=21cm] at (0.0,-0.9) {\textbf{seta}: o padrão maior usa o menor \quad\quad \textbf{tracejado vermelho}: Acordeão dentro de um Assistente não é recomendado};
""")

# ------------------------------------------------------------------ sequencia: tres linguagens/catalogos de padroes
def _painel(cx, cor, titulo, sub, itens, rodape):
    o = []
    o.append(r"\draw[draw=%s, line width=2.2pt, fill=%s!6, rounded corners=10pt] (%s,-0.4) rectangle (%s,9.2);" % (cor, cor, cx - 3.4, cx + 3.4))
    o.append(r"\node[font=\Large\bfseries, text=%s] at (%s,8.4) {%s};" % (cor, cx, titulo))
    o.append(r"\node[font=\large, text width=6.2cm, align=center] at (%s,7.6) {%s};" % (cx, sub))
    ys = [6.0, 4.0, 2.0]
    for y, t in zip(ys, itens):
        o.append(r"\node[dbox, draw=%s, text width=5.5cm, minimum height=1.6cm, font=\large, line width=1.6pt, fill=white] (%s%d) at (%s,%s) {%s};" % (cor, cor[1:], int(y), cx, y, t))
    o.append(r"\node[font=\large\bfseries, text width=6.2cm, align=center] at (%s,0.5) {%s};" % (cx, rodape))
    return "\n".join(o)

w("padroes-sequencia", "\n".join([
  _painel(3.4, "dblue", "Alexander (anos 1970)", "arquitetura e urbanismo: \\textbf{253 padrões}, do maior ao menor",
          [r"\textbf{região}: \emph{Independent Regions}", r"\textbf{cidade}: \emph{Web of Public Transportation}", r"\textbf{cômodo}: \emph{Window Place}"],
          "uma \\textbf{linguagem}: cada padrão cita os maiores e os menores"),
  _painel(11.4, "dgreen", "Gamma et al. (1994)", "engenharia de software: \\textbf{23 padrões} em três famílias",
          [r"\textbf{criação}: \emph{Singleton}, \emph{Factory Method}", r"\textbf{estrutura}: \emph{Adapter}, \emph{Decorator}", r"\textbf{comportamento}: \emph{Observer}, \emph{Strategy}"],
          "um \\textbf{catálogo}, organizado por família"),
  _painel(19.4, "dorange", "Tidwell (2011)", "interfaces de usuário: padrões agrupados por \\textbf{tema}",
          [r"\textbf{organizar o conteúdo}: \emph{Wizard}, \emph{Escape Hatch}", r"\textbf{navegar}: \emph{Global Navigation}, \emph{Breadcrumbs}", r"\textbf{organizar a página}: \emph{Accordion}, \emph{Collapsible Panels}"],
          "um \\textbf{mapa temático} de padrões de IHC"),
  r"\draw[dtrans, line width=3pt, -{Stealth[length=4.2mm]}] (6.9,4.4) -- (7.9,4.4);",
  r"\draw[dtrans, line width=3pt, -{Stealth[length=4.2mm]}] (14.9,4.4) -- (15.9,4.4);"]))

# ------------------------------------------------------------------ padrao Acordeao descrito pelos seis elementos
def _carta(cx, cy, cor, titulo, texto):
    return (r"\node[dbox, draw=%s, text width=5.9cm, minimum height=3.9cm, font=\large, line width=1.7pt] at (%s,%s) {\textbf{\Large\textcolor{%s}{%s}}\\[5pt] %s};" % (cor, cx, cy, cor, titulo, texto))

w("padrao-acordeao", "\n".join([
  _carta(3.4, 5.0, "dblue", "Título", r"{\Huge\bfseries Acordeão}"),
  _carta(10.6, 5.0, "dgreen", "O que", r"para encontrar um item entre as opções de navegação: empilhar painéis, abrindo \textbf{um por vez} e colapsando os demais"),
  _carta(17.8, 5.0, "dorange", "Quando usar", r"\textbf{navegação} (equivale a \emph{Guias}), \textbf{perguntas frequentes} ou \textbf{preferências}; em geral \textbf{menos de dez painéis}"),
  _carta(3.4, 0.5, "dred", "Por quê", r"comprime muitos elementos em \textbf{pouco espaço}; \textbf{desvantagem}: os itens dos outros painéis ficam ocultos"),
  _carta(10.6, 0.5, "dblue", "Como", r"\textbf{animar} a abertura (\emph{feedback} sutil, até \textbf{250 ms}); \textbf{setas do teclado}; \textbf{destacar} o painel atual; tamanho total variável"),
  r"""
\node[dbox, draw=dgreen, text width=5.9cm, minimum height=3.9cm, line width=1.7pt] at (17.8,0.5) {};
\node[font=\Large\bfseries, text=dgreen] at (17.8,2.0) {Exemplos};
\node[font=\normalsize] at (17.8,1.5) {painel de tarefas de um editor};
\tikzset{p/.style={draw=black!70, line width=1.4pt, fill=dshade!55, minimum width=4.8cm, minimum height=0.6cm, font=\normalsize\bfseries, anchor=west, inner sep=4pt}}
\node[p] at (15.4,0.9) {> Páginas mestres};
\node[p, fill=dblue!22] at (15.4,0.3) {v Layouts};
\draw[draw=black!70, line width=1.4pt, fill=white] (15.4,-0.7) rectangle (20.2,0.0);
\foreach \x in {15.6,17.2,18.8} {\draw[black!55, line width=1.2pt, fill=dcream] (\x,-0.6) rectangle (\x+1.2,-0.1);}
\node[p] at (15.4,-1.0) {> Modelos de tabela};
"""]))

# ------------------------------------------------------------------ linha do tempo: origem dos deceptive patterns
w("origem-conceito", r"""
\tikzset{k/.style={dbox, text width=4.4cm, minimum height=3.4cm, font=\large, line width=1.8pt}}
\draw[line width=3pt, draw=black!80, -{Stealth[length=4mm]}] (0,2.3) -- (21.0,2.3);
\foreach \x/\a in {2.5/2003, 8.0/2010, 13.5/2018, 18.5/2019} {
  \fill[black] (\x,2.3) circle (0.2);
  \node[font=\Large\bfseries, anchor=north] at (\x,1.8) {\a};
  \draw[line width=1.4pt, black] (\x,2.5) -- (\x,3.1);}
\node[k, draw=dblue, anchor=south] at (2.5,3.1) {\textbf{\textcolor{dblue}{Fogg et al.}}\\[4pt] a persuasão \textbf{exacerbada} deixa de ser persuasiva e se torna \textbf{coerciva}};
\node[k, draw=dgreen, anchor=south] at (8.0,3.1) {\textbf{\textcolor{dgreen}{Brignull}}\\[4pt] estabelece o conceito ao analisar \textbf{sites de compra e venda} e cataloga casos};
\node[k, draw=dorange, anchor=south] at (13.5,3.1) {\textbf{\textcolor{dorange}{Gray et al.}}\\[4pt] \textbf{taxonomia} a partir dos exemplos de Brignull};
\node[k, draw=dred, dashed, anchor=south, text width=3.9cm] at (18.5,3.1) {\textbf{\textcolor{dred}{Mathur et al.}}\\[4pt] taxonomia complementar: classifica pelo \textbf{fim almejado}, em 5 categorias};
""")
