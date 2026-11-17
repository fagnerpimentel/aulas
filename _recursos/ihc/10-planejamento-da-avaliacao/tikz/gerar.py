"""Gera os diagramas TikZ da aula 10 de IHC (Planejamento da Avaliação). Uso: python3 gerar.py && bash build.sh"""
exec(open("_helpers.py").read())

# ------------------------------------------------------------------ duas perspectivas de qualidade
w("duas-perspectivas", r"""
\tikzset{k/.style={dbox, text width=7.6cm, minimum height=2.0cm, font=\large, line width=1.6pt}}
\draw[draw=dblue, line width=2pt, fill=dblue!6, rounded corners=10pt] (0,0.2) rectangle (9.0,7.8);
\node[font=\Large\bfseries, dblue] at (4.5,7.2) {quem constrói};
\node[k, draw=dblue] at (4.5,5.4) {o sistema \textbf{funciona conforme a especificação}?};
\node[k, draw=dblue] at (4.5,3.2) {foco \textbf{dentro} do sistema: entrada, processamento e saída};
\node[font=\large, text width=8cm, align=center] at (4.5,1.2) {testes de unidade, integração, sistema e operação};
\draw[draw=dgreen, line width=2pt, fill=dgreen!6, rounded corners=10pt] (10.4,0.2) rectangle (19.4,7.8);
\node[font=\Large\bfseries, dgreen] at (14.9,7.2) {quem projeta e quem usa};
\node[k, draw=dgreen] at (14.9,5.4) {o sistema \textbf{apoia o usuário} a atingir seus objetivos?};
\node[k, draw=dgreen] at (14.9,3.2) {foco \textbf{da interface para fora}: a experiência vivida};
\node[font=\large, text width=8cm, align=center] at (14.9,1.2) {usabilidade, UX, acessibilidade e comunicabilidade};
""")

# ------------------------------------------------------------------ razoes para avaliar (Tognazzini)
w("razoes-avaliar", boxes([
  ("Corrigir cedo", "problemas de IHC corrigidos antes, e não depois, do lançamento"),
  ("Foco em problemas reais", "em vez de debater gostos e preferências da equipe"),
  ("Advogado do usuário", "engenheiros sabem construir, mas não defender a qualidade de uso"),
  ("Menos tempo até o mercado", "problemas corrigidos desde o início, com menos esforço"),
  ("Produto mais robusto", "a versão corretiva não precisa começar no lançamento")], w=5.4, h=3.0, cols=3,
  cap=r"razões apontadas por Tognazzini (2000)", capw=17))

# ------------------------------------------------------------------ custo x beneficio
w("custo-beneficio", r"""
\tikzset{k/.style={dbox, text width=7.8cm, minimum height=2.4cm, font=\large, line width=1.7pt}}
\node[font=\Large\bfseries, dgreen] at (4.9,8.4) {a curto prazo};
\node[k, draw=dgreen] at (4.9,6.3) {\textbf{mais produtividade} dos usuários};
\node[k, draw=dgreen] at (4.9,3.6) {\textbf{menos erros}, em número e em gravidade};
\node[k, draw=dgreen] at (4.9,0.9) {\textbf{mais satisfação} dos usuários};
\node[font=\Large\bfseries, dblue] at (14.5,8.4) {a médio e longo prazo};
\node[k, draw=dblue] at (14.5,6.3) {\textbf{menos custo} de treinamento e suporte};
\node[k, draw=dblue] at (14.5,3.6) {\textbf{versões futuras} melhor planejadas};
\node[k, draw=dblue] at (14.5,0.9) {partes do sistema que \textbf{podem ser mais exploradas}};
""")

# ------------------------------------------------------------------ planejar: perguntas
w("planejar-perguntas", boxes([
  ("O que avaliar?", "os objetivos e os aspectos relacionados ao uso"),
  ("Quando avaliar?", "durante o design (formativa) ou ao final (somativa)"),
  ("Onde coletar dados?", "em contexto real de uso ou em laboratório"),
  ("Que dados coletar?", "e que dados produzir, para responder às perguntas"),
  ("Qual método?", "investigação, observação ou inspeção"),
  ("Como avaliar?", "preparar, coletar, interpretar, consolidar e relatar")], w=5.4, h=2.6, cols=3))

# ------------------------------------------------------------------ stakeholders e objetivos
w("stakeholders-objetivos", r"""
\tikzset{s/.style={dbox, text width=3.6cm, minimum height=1.5cm, font=\large\bfseries, line width=1.6pt},
        o/.style={dbox, text width=10.6cm, minimum height=1.5cm, font=\large, line width=1.6pt}}
\foreach \y/\n/\t/\cor in {7.2/Usuários/{demonstram \textbf{desinteresse} ou fazem \textbf{reclamações}}/dblue, 5.5/Designers/{querem \textbf{comparar alternativas} de design}/dgreen, 3.8/Cliente/{quer saber se a \textbf{qualidade de uso} é um diferencial do produto}/dorange, 2.1/Desenvolvedores/{querem saber se a \textbf{nova tecnologia} da interface agrada}/dred, 0.4/Marketing/{quer lançar um produto que atenda \textbf{necessidades ainda não exploradas}}/dblue} {
  \node[s, draw=\cor] (a) at (2.4,\y) {\textcolor{\cor}{\n}};
  \node[o, draw=\cor] (b) at (11.9,\y) {\t};
  \draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a.east) -- (b.west);}
\node[font=\Large\bfseries] at (2.4,8.6) {stakeholder};
\node[font=\Large\bfseries] at (11.9,8.6) {objetivo da avaliação};
""")

# ------------------------------------------------------------------ quatro aspectos
w("quatro-aspectos", boxes([
  ("Apropriação de tecnologia", "como os usuários incorporam o sistema e a tecnologia no cotidiano"),
  ("Ideias e alternativas de design", "comparar soluções por critérios de uso e de construção"),
  ("Conformidade com um padrão", "acessibilidade (W3C), ambientes, domínio e normas da organização"),
  ("Problemas na interação e na interface", "o que prejudica a qualidade de uso")], w=4.2, h=3.8, cols=4,
  cap=r"o objetivo da avaliação define \textbf{quais aspectos do uso} serão investigados", capw=18))

# ------------------------------------------------------------------ formativa x somativa
w("formativa-somativa", r"""
\tikzset{k/.style={dbox, text width=7.6cm, minimum height=2.8cm, font=\large, line width=1.7pt}}
\draw[line width=3pt, draw=black!80, -{Stealth[length=4mm]}] (0,3.4) -- (19.4,3.4);
\node[font=\Large\bfseries, anchor=north] at (3.0,3.0) {início do design};
\node[font=\Large\bfseries, anchor=north] at (16.2,3.0) {solução pronta};
\draw[draw=dgreen, line width=2.2pt, fill=dgreen!8] (0.4,4.0) rectangle (12.4,5.2);
\node[font=\Large\bfseries, dgreen] at (6.4,4.6) {avaliação formativa (construtiva)};
\draw[draw=dorange, line width=2.2pt, fill=dorange!8] (12.9,4.0) rectangle (19.2,5.2);
\node[font=\Large\bfseries, dorange] at (16.05,4.6) {avaliação somativa};
\node[k, draw=dgreen, text width=11.2cm] at (6.4,7.4) {\textbf{durante} a elaboração: compara ideias e alternativas, acha problemas \textbf{cedo}, com custo de correção baixo\\ {\normalsize cenários, esboços, \emph{storyboards}, modelos e protótipos}};
\node[k, draw=dorange, text width=5.8cm] at (16.05,7.4) {\textbf{depois}: julga a solução e busca evidências de que as \textbf{metas} foram atingidas};
\node[font=\large, anchor=north, text width=7cm, align=center] at (16.05,1.9) {protótipo de média ou alta fidelidade, ou o sistema implementado};
\node[font=\large, anchor=north, text width=11cm, align=center] at (6.4,1.9) {\textbf{(re)design} e avaliação em ciclos};
""")

# ------------------------------------------------------------------ contexto x laboratorio
w("contexto-laboratorio", r"""
\tikzset{k/.style={dbox, text width=8.4cm, minimum height=1.7cm, font=\large, line width=1.6pt}}
\node[font=\Large\bfseries, dgreen] at (4.7,8.7) {em contexto real de uso};
\node[k, draw=dgreen] at (4.7,7.0) {\textbf{diversidade} de situações de uso e dados de situações típicas};
\node[k, draw=dgreen] at (4.7,5.1) {mostra como os usuários \textbf{se apropriam} da tecnologia no cotidiano};
\node[k, draw=dred, dashed] at (4.7,3.2) {\textbf{difícil controlar} a execução e os aspectos analisados};
\node[font=\Large\bfseries, dblue] at (14.7,8.7) {em laboratório};
\node[k, draw=dblue] at (14.7,7.0) {\textbf{controle} sobre as interferências do ambiente};
\node[k, draw=dblue] at (14.7,5.1) {facilita o \textbf{registro} dos dados e \textbf{comparar} experiências};
\node[k, draw=dred, dashed] at (14.7,3.2) {ambiente \textbf{artificial}: deve ser confortável para o participante};
\node[font=\large, text width=9cm, align=center] at (4.7,1.3) {estudo de campo};
\node[font=\large, text width=9cm, align=center] at (14.7,1.3) {sala de reunião, teste de usabilidade, avaliação de comunicabilidade};
""")

# ------------------------------------------------------------------ laboratorio de observacao
w("laboratorio-observacao", r"""
\draw[draw=black!70, line width=2.4pt] (0,0) rectangle (19.0,9.0);
\draw[draw=black!70, line width=4pt] (9.5,0) -- (9.5,9.0);
\node[font=\Large\bfseries, dblue] at (4.7,8.3) {sala de uso};
\node[font=\Large\bfseries, dgreen] at (14.2,8.3) {sala de observação};
\draw[draw=dblue, line width=1.7pt, fill=dblue!10, rounded corners=3pt] (1.5,5.0) rectangle (7.9,7.2);
\node[font=\large\bfseries] at (4.7,6.1) {participante + computador};
\draw[draw=dblue, line width=1.7pt, fill=white, rounded corners=3pt] (1.5,1.2) rectangle (5.0,2.8);
\node[font=\large, text width=3.2cm, align=center] at (3.25,2.0) {avaliador de apoio};
\draw[draw=dgreen, line width=1.7pt, fill=dgreen!10, rounded corners=3pt] (11.0,4.8) rectangle (17.4,7.2);
\node[font=\large\bfseries, text width=6cm, align=center] at (14.2,6.0) {monitor clone: reproduz o que o participante vê};
\draw[draw=dgreen, line width=1.7pt, fill=white, rounded corners=3pt] (11.0,1.2) rectangle (17.4,2.8);
\node[font=\large\bfseries, text width=6cm, align=center] at (14.2,2.0) {avaliador: anota e acompanha};
\node[font=\large\bfseries, text=white, fill=black!70, rounded corners=2pt, inner sep=3pt] at (9.5,4.5) {vidro espelhado};

""")

# ------------------------------------------------------------------ objetivos e perguntas (Tabela 11.1)
w("objetivo-perguntas", r"""
\tikzset{h/.style={dbox, text width=4.1cm, minimum height=2.2cm, font=\large\bfseries, line width=1.8pt},
        q/.style={dbox, text width=4.1cm, minimum height=1.9cm, font=\normalsize, line width=1.4pt}}
\node[h, draw=dblue] at (2.2,7.0) {\textcolor{dblue}{apropriação da tecnologia}};
\node[q, draw=dblue] at (2.2,4.6) {Como os usuários usam o sistema? Em que difere do planejado?};
\node[q, draw=dblue] at (2.2,2.4) {Que variação houve em erros, tempo e satisfação?};
\node[q, draw=dblue] at (2.2,0.2) {Por que não incorporaram o sistema?};
\node[h, draw=dgreen] at (7.1,7.0) {\textcolor{dgreen}{alternativas de design}};
\node[q, draw=dgreen] at (7.1,4.6) {Qual é a mais eficiente? Mais fácil de aprender?};
\node[q, draw=dgreen] at (7.1,2.4) {Qual pode ser construída em menos tempo?};
\node[q, draw=dgreen] at (7.1,0.2) {Qual os usuários preferem? Por quê?};
\node[h, draw=dorange] at (12.0,7.0) {\textcolor{dorange}{conformidade com um padrão}};
\node[q, draw=dorange] at (12.0,4.6) {Está de acordo com os padrões de acessibilidade do W3C?};
\node[q, draw=dorange] at (12.0,2.4) {Segue o padrão do sistema operacional? E o da empresa?};
\node[q, draw=dorange] at (12.0,0.2) {Os termos seguem as convenções do domínio?};
\node[h, draw=dred] at (16.9,7.0) {\textcolor{dred}{problemas na interação}};
\node[q, draw=dred] at (16.9,4.6) {O usuário consegue operar o sistema? Atinge o objetivo, com quanta eficiência?};
\node[q, draw=dred] at (16.9,2.4) {Que parte da interface o deixa insatisfeito?};
\node[q, draw=dred] at (16.9,0.2) {Ele entende o que significa cada elemento?};
""")

# ------------------------------------------------------------------ dados por objetivo
w("dados-por-objetivo", r"""
\tikzset{k/.style={dbox, text width=8.4cm, minimum height=1.5cm, font=\large, line width=1.6pt}}
\node[dbox, draw=dblue, text width=8.6cm, minimum height=1.9cm, font=\large\bfseries, line width=2pt, fill=dblue!8] at (4.7,8.4) {objetivo: verificar se o protótipo \textbf{satisfaz as necessidades} dos usuários};
\node[k, draw=dblue] at (4.7,6.4) {grau de \textbf{satisfação} com o sistema};
\node[k, draw=dblue] at (4.7,4.7) {necessidade de usar \textbf{outros sistemas} ou artefatos};
\node[k, draw=dblue] at (4.7,3.0) {\textbf{pontos fortes e fracos} do sistema};
\node[k, draw=dblue] at (4.7,1.3) {o que gostariam que fosse \textbf{melhorado}};
\node[dbox, draw=dred, text width=8.6cm, minimum height=1.9cm, font=\large\bfseries, line width=2pt, fill=dred!8] at (14.7,8.4) {objetivo: \textbf{identificar problemas} na interação e na interface};
\node[k, draw=dred] at (14.7,6.4) {quantos usuários \textbf{concluíram} as tarefas};
\node[k, draw=dred] at (14.7,4.7) {\textbf{quanto tempo} cada tarefa levou};
\node[k, draw=dred] at (14.7,3.0) {\textbf{erros}: quais, onde e com que frequência};
\node[k, draw=dred] at (14.7,1.3) {consultas a \textbf{material de apoio}, e quando};
""")

# ------------------------------------------------------------------ tres classificacoes
w("tres-classificacoes", r"""
\tikzset{h/.style={dbox, text width=5.8cm, minimum height=1.7cm, font=\Large\bfseries, line width=1.8pt},
        k/.style={dbox, text width=5.8cm, minimum height=1.4cm, font=\large, line width=1.5pt}}
\node[h, draw=dblue] at (3.2,6.8) {\textcolor{dblue}{pela escala}};
\node[k, draw=dblue] at (3.2,4.9) {nominais};
\node[k, draw=dblue] at (3.2,3.4) {ordinais};
\node[k, draw=dblue] at (3.2,1.9) {de intervalo};
\node[k, draw=dblue] at (3.2,0.4) {de razão};
\node[h, draw=dgreen] at (9.7,6.8) {\textcolor{dgreen}{pela natureza}};
\node[k, draw=dgreen] at (9.7,4.9) {qualitativos};
\node[k, draw=dgreen] at (9.7,3.4) {quantitativos};
\node[h, draw=dorange] at (16.2,6.8) {\textcolor{dorange}{pela origem}};
\node[k, draw=dorange] at (16.2,4.9) {objetivos};
\node[k, draw=dorange] at (16.2,3.4) {subjetivos};
\node[font=\large, text width=17cm, align=center] at (9.7,-1.0) {cada método de avaliação privilegia \textbf{dados e resultados de diferentes tipos}};
""")

# ------------------------------------------------------------------ escalas de medida
w("escalas-medida", r"""
\tikzset{c/.style={dbox, text width=4.0cm, minimum height=3.8cm, font=\large, line width=1.7pt}}
\node[c, draw=dblue] (a) at (2.3,3.4) {\textbf{\textcolor{dblue}{Nominal}}\\ rótulos ou categorias\\[4pt] {\normalsize ex.: atividades, idiomas, problemas}};
\node[c, draw=dgreen] (b) at (7.4,3.4) {\textbf{\textcolor{dgreen}{Ordinal}}\\ ranqueamento\\[4pt] {\normalsize ex.: sites mais usados}};
\node[c, draw=dorange] (d) at (12.5,3.4) {\textbf{\textcolor{dorange}{Intervalo}}\\ diferença de igual magnitude\\[4pt] {\normalsize ex.: temperatura em Celsius}};
\node[c, draw=dred] (e) at (17.6,3.4) {\textbf{\textcolor{dred}{Razão}}\\ zero verdadeiro\\[4pt] {\normalsize ex.: tempo da tarefa, erros}};
\foreach \p/\q in {a/b, b/d, d/e} {\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (\p.east) -- (\q.west);}
\node[font=\large, text width=4.3cm, align=center] at (2.3,0.4) {igual ou diferente};
\node[font=\large, text width=4.3cm, align=center] at (7.4,0.4) {maior ou menor, mas \textbf{não quanto}};
\node[font=\large, text width=4.3cm, align=center] at (12.5,0.4) {\textbf{quanto} a mais, mas não a proporção};
\node[font=\large, text width=4.3cm, align=center] at (17.6,0.4) {também a \textbf{proporção} (o triplo)};
\node[font=\large\bfseries] at (9.95,6.5) {o que se pode afirmar cresce da esquerda para a direita};
""")

# ------------------------------------------------------------------ exemplo quantitativo (61/23/16 x 82/13/5)
w("exemplo-quantitativo", r"""
\def\u{0.16}
\node[font=\Large\bfseries, anchor=east] at (2.2,4.6) {Solução A};
\node[font=\Large\bfseries, anchor=east] at (2.2,2.0) {Solução B};
\draw[draw=black!70, line width=1.4pt, fill=dgreen!55] (2.6,4.0) rectangle (2.6+61*\u,5.2); \node[font=\large\bfseries, text=white] at (2.6+30.5*\u,4.6) {61\%};
\draw[draw=black!70, line width=1.4pt, fill=dorange!65] (2.6+61*\u,4.0) rectangle (2.6+84*\u,5.2); \node[font=\large\bfseries, text=white] at (2.6+72.5*\u,4.6) {23\%};
\draw[draw=black!70, line width=1.4pt, fill=dred!65] (2.6+84*\u,4.0) rectangle (2.6+100*\u,5.2); \node[font=\large\bfseries, text=white] at (2.6+92*\u,4.6) {16\%};
\draw[draw=black!70, line width=1.4pt, fill=dgreen!55] (2.6,1.4) rectangle (2.6+82*\u,2.6); \node[font=\large\bfseries, text=white] at (2.6+41*\u,2.0) {82\%};
\draw[draw=black!70, line width=1.4pt, fill=dorange!65] (2.6+82*\u,1.4) rectangle (2.6+95*\u,2.6); \node[font=\large\bfseries, text=white] at (2.6+88.5*\u,2.0) {13\%};
\draw[draw=black!70, line width=1.4pt, fill=dred!65] (2.6+95*\u,1.4) rectangle (2.6+100*\u,2.6); \node[font=\small\bfseries, text=white] at (2.6+97.5*\u,2.0) {5\%};
\draw[fill=dgreen!55, draw=black!70, line width=1.2pt] (3.0,0.2) rectangle (3.6,0.8); \node[font=\large, anchor=west] at (3.8,0.5) {concluíram todas as tarefas};
\draw[fill=dorange!65, draw=black!70, line width=1.2pt] (10.6,0.2) rectangle (11.2,0.8); \node[font=\large, anchor=west] at (11.4,0.5) {concluíram metade};
\draw[fill=dred!65, draw=black!70, line width=1.2pt] (15.6,0.2) rectangle (16.2,0.8); \node[font=\large, anchor=west] at (16.4,0.5) {nem metade};
\node[font=\large, anchor=north west, text width=16cm] at (2.6,-0.3) {os números mostram \textbf{quanto}, mas \textbf{não explicam por quê}: só comprovam a hipótese se forem estatisticamente significativos};
""")

# ------------------------------------------------------------------ objetivo x subjetivo
w("objetivo-subjetivo", r"""
\tikzset{k/.style={dbox, text width=7.6cm, minimum height=2.6cm, font=\large, line width=1.7pt}}
\node[font=\Large\bfseries, dgreen] at (6.0,8.6) {qualitativo};
\node[font=\Large\bfseries, dblue] at (15.2,8.6) {quantitativo};
\node[font=\Large\bfseries, anchor=east] at (-0.6,6.2) {objetivo};
\node[font=\Large\bfseries, anchor=east] at (-0.6,2.6) {subjetivo};
\node[k, draw=dgreen] at (6.0,6.2) {termos usados em uma \textbf{busca};\\ músicas mais ouvidas no último mês};
\node[k, draw=dblue] at (15.2,6.2) {\textbf{tempo} para realizar a tarefa em uma sessão de teste};
\node[k, draw=dgreen] at (6.0,2.6) {opiniões expressas em \textbf{texto} em linguagem natural};
\node[k, draw=dblue] at (15.2,2.6) {opiniões em uma \textbf{escala numérica}, em questionários};
\node[font=\large, text width=17cm, align=center] at (10.6,0.3) {\textbf{objetivos}: medidos por instrumentos ou software; \textbf{subjetivos}: expressos pelos participantes};
""")

# ------------------------------------------------------------------ tres metodos
w("tres-metodos", r"""
\tikzset{k/.style={dbox, text width=5.6cm, minimum height=6.4cm, font=\large, line width=1.9pt, align=left}}
\node[k, draw=dblue] at (3.2,4.2) {\textbf{\Large\textcolor{dblue}{Investigação}}\\[6pt] \emph{inquiry}\\[6pt] questionários, entrevistas, grupos de foco, estudos de campo\\[6pt] usuários \textbf{relatam} concepções, opiniões e expectativas};
\node[k, draw=dgreen] at (9.7,4.2) {\textbf{\Large\textcolor{dgreen}{Observação}}\\[6pt] dados sobre \textbf{situações reais} de uso\\[6pt] em contexto ou em laboratório\\[6pt] métodos \textbf{empíricos}: \textbf{identificam problemas reais}};
\node[k, draw=dorange] at (16.2,4.2) {\textbf{\Large\textcolor{dorange}{Inspeção}}\\[6pt] o avaliador \textbf{antevê} as consequências das decisões de design\\[6pt] em geral \textbf{sem usuários}: experiências \textbf{potenciais}\\[6pt] métodos \textbf{analíticos}};
""")

# ------------------------------------------------------------------ escolha do metodo
w("escolha-metodo", r"""
\tikzset{o/.style={dbox, text width=7.2cm, minimum height=1.8cm, font=\large, line width=1.7pt},
        m/.style={dbox, text width=8.4cm, minimum height=1.8cm, font=\large, line width=1.7pt}}
\node[o, draw=dred] (a) at (3.8,6.6) {\textbf{problemas} na interação e na interface};
\node[m, draw=dorange] (a2) at (14.8,6.6) {\textbf{inspeção} para cobrir (quase) toda a interface + \textbf{observação ou investigação} nas partes importantes};
\node[o, draw=dblue] (b) at (3.8,4.0) {\textbf{apropriação} da tecnologia};
\node[m, draw=dgreen] (b2) at (14.8,4.0) {\textbf{investigação} ou \textbf{observação}, com a participação dos usuários};
\node[o, draw=dgreen] (c) at (3.8,1.4) {\textbf{conformidade} com um padrão};
\node[m, draw=dorange] (c2) at (14.8,1.4) {\textbf{inspeção}: a participação dos usuários é desnecessária};
\foreach \p/\q in {a/a2, b/b2, c/c2} {\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (\p.east) -- (\q.west);}
\node[font=\Large\bfseries] at (3.8,8.1) {objetivo};
\node[font=\Large\bfseries] at (14.8,8.1) {método mais adequado};
""")

# ------------------------------------------------------------------ atividades de uma avaliacao
w("atividades-avaliacao", flow([
  ("Preparação", "objetivos, escopo, método, participantes, material e piloto"),
  ("Coleta de dados", "seguir o método e registrar as experiências de uso"),
  ("Interpretação", "dar significado aos dados de cada participante"),
  ("Consolidação e relato", "analisar em conjunto e relatar os resultados")],
  w=3.6, h=3.6, cap=r"se houver problemas ou oportunidades, planeja-se também o \textbf{reprojeto} do sistema", capw=18))

# ------------------------------------------------------------------ numero de participantes
w("numero-participantes", r"""
\tikzset{k/.style={dbox, text width=5.6cm, minimum height=4.2cm, font=\large, line width=1.8pt}}
\node[k, draw=dblue] at (3.2,3.2) {\textbf{\textcolor{dblue}{Dumas e Redish (1999)}}\\[8pt] {\Huge\bfseries 5 a 12}\\[8pt] usuários em uma avaliação, em geral};
\node[k, draw=dgreen] at (9.7,3.2) {\textbf{\textcolor{dgreen}{Nielsen (2000)}}\\[8pt] {\Huge\bfseries 5}\\[8pt] bastam para achar \textbf{cerca de 85\%} dos problemas};
\node[k, draw=dorange] at (16.2,3.2) {\textbf{\textcolor{dorange}{Significância estatística}}\\[8pt] amostra \textbf{grande} e \textbf{representativa}\\[8pt] custo alto de coleta e análise};
\node[font=\large, text width=18cm, align=center] at (9.7,0.0) {mesmo sem significância, os resultados dão \textbf{indícios} úteis para o reprojeto};
""")

# ------------------------------------------------------------------ material de apoio
w("material-apoio", boxes([
  ("TCLE", "termo de consentimento livre e esclarecido"),
  ("Questionário pré-teste", "ou roteiro de entrevista estruturada: perfil e experiência"),
  ("Entrevista pós-teste", "opiniões e sentimentos sobre a experiência de uso"),
  ("Instruções e cenários", "orientam os participantes nas tarefas"),
  ("Roteiro de observação", "facilita a captura de dados e anotações")], w=5.4, h=2.8, cols=3,
  cap=r"todos os participantes recebem o \textbf{mesmo material} e as \textbf{mesmas orientações}", capw=17))

# ------------------------------------------------------------------ passos da sessao
w("sessao-passos", flow([
  ("Receber", "quebra-gelo e apresentação do ambiente"),
  ("Explicar", "objetivos, procedimento e TCLE em duas vias"),
  ("Pré-teste", "questionário ou entrevista estruturada"),
  ("Explorar", "exploração livre do sistema, se for o 1º contato"),
  ("Tarefas", "instruções e cenários; observação e anotações"),
  ("Pós-teste", "entrevista sobre a experiência vivida")],
  w=2.6, h=4.4, font=r"\normalsize"))

# ------------------------------------------------------------------ DECIDE
w("decide", r"""
\tikzset{l/.style={circle, minimum size=1.6cm, font=\Huge\bfseries, line width=2pt, fill=white},
        k/.style={dbox, text width=7.0cm, minimum height=1.9cm, font=\large, line width=1.6pt, align=left}}
\foreach \y/\ch/\col/\tit/\txt in {
  7.6/D/dblue/{Determinar os objetivos}/{o que se avalia, por quê e para quem},
  5.5/E/dgreen/{Explorar as perguntas}/{perguntas específicas para cada objetivo},
  3.4/C/dorange/{Escolher os métodos}/{prazo, orçamento, equipamentos e experiência dos avaliadores},
  1.3/I/dred/{Identificar as questões práticas}/{recrutamento, equipamentos, prazos, pessoal}} {
  \node[l, draw=\col, text=\col] at (1.0,\y) {\ch};
  \node[k, draw=\col] at (5.4,\y) {\textbf{\textcolor{\col}{\tit}}\\ \txt};}
\foreach \y/\ch/\col/\tit/\txt in {
  7.6/D/dblue/{Decidir as questões éticas}/{respeitar e não prejudicar os participantes},
  5.5/E/dgreen/{Avaliar os dados}/{interpretar e apresentar, atento à confiabilidade e à validade}} {
  \node[l, draw=\col, text=\col] at (11.4,\y) {\ch};
  \node[k, draw=\col] at (15.8,\y) {\textbf{\textcolor{\col}{\tit}}\\ \txt};}
\node[dbox, draw=dorange, dashed, fill=dorange!6, line width=1.7pt, text width=8.2cm, minimum height=2.8cm, font=\large] at (15.2,2.3) {as atividades são \textbf{interligadas} e feitas de forma \textbf{iterativa}: sem permissão para visitar o ambiente de uso, os \textbf{objetivos} precisam ser revistos};
""")

# ------------------------------------------------------------------ validades
w("validades", boxes([
  ("Confiabilidade", "mesmos resultados ao repetir o método nas mesmas circunstâncias"),
  ("Validade interna", "o método mede o que deveria medir, com rigor e sem distorções"),
  ("Validade externa", "até que ponto os resultados podem ser generalizados para outro contexto"),
  ("Validade ecológica", "o quanto materiais, métodos e ambiente se parecem com a situação real")], w=4.2, h=4.0, cols=4,
  cap=r"cuidados antes de tirar conclusões e divulgar os resultados", capw=18))

# ------------------------------------------------------------------ o usuário não é o designer
w("usuario-nao-e-designer", r"""
\tikzset{k/.style={dbox, text width=5.0cm, minimum height=3.4cm, font=\large, line width=1.8pt}}
\node[k, draw=dblue] (d) at (2.7,5.4) {\textbf{\Large\textcolor{dblue}{Designer}}\\[3pt] decide com base na \textbf{sua interpretação}, no seu conhecimento e na sua criatividade};
\node[k, draw=dorange] (s) at (10.0,5.4) {\textbf{\Large\textcolor{dorange}{Sistema}}\\[3pt] a interação segue a \textbf{lógica do designer}};
\node[k, draw=dgreen] (u) at (17.3,5.4) {\textbf{\Large\textcolor{dgreen}{Usuário}}\\[3pt] \textbf{outra} cultura, costumes, gostos e objetivos};
\draw[->, line width=2.4pt, dblue] (d.east) -- node[above, font=\large] {projeta} (s.west);
\draw[->, line width=2.4pt, dorange] (s.east) -- node[above, font=\large] {usa} (u.west);
\node[draw=dred, dashed, line width=1.6pt, rounded corners=4pt, fill=dred!6, text width=4.6cm, align=center, font=\large, inner sep=7pt] (q) at (13.2,2.3) {pode \textbf{não compreender} ou \textbf{não concordar} com essa lógica};
\draw[dashed, line width=1.6pt, dred] (q.north) -- (13.2,5.35);
\node[dbox, draw=dred, text width=11.4cm, minimum height=2.2cm, font=\large, line width=1.8pt] (a) at (8.0,-0.3) {\textbf{\Large\textcolor{dred}{Avaliador}}: uma espécie de \textbf{advogado do usuário}\\[2pt] de preferência, quem \textbf{não participou da concepção}};
\draw[->, line width=2.4pt, dred] (a.east) -| (16.0,3.7);
\node[anchor=west, font=\large, text width=3.6cm, align=left] at (16.25,1.4) {defende o ponto de vista do usuário};
""")

# ------------------------------------------------------------------ a qualidade de uso sempre será avaliada
w("qualidade-sempre-avaliada", r"""
\tikzset{k/.style={dbox, text width=4.6cm, minimum height=2.1cm, font=\large, line width=1.7pt},
        u/.style={dbox, text width=7.6cm, minimum height=2.1cm, font=\large, line width=1.7pt}}
\draw[dashed, line width=1.8pt, dblue] (10.9,-0.3) -- (10.9,7.5);
\node[font=\Large\bfseries, dblue, fill=white, inner sep=3pt] at (10.9,7.95) {entrega ao usuário};
\node[font=\Large\bfseries, dgreen, anchor=west] at (0.0,7.1) {a equipe avalia antes};
\node[k, draw=dgreen] (a1) at (2.5,5.2) {\textbf{avalia} a qualidade de uso};
\node[k, draw=dgreen] (a2) at (8.0,5.2) {\textbf{corrige} os problemas};
\node[u, draw=dgreen] (a3) at (15.6,5.2) {\textbf{usuário avalia} e forma sua opinião: o sistema \textbf{já foi corrigido}};
\draw[->, line width=2.2pt, dgreen] (a1.east) -- (a2.west);
\draw[->, line width=2.2pt, dgreen] (a2.east) -- (a3.west);
\node[font=\Large\bfseries, dred, anchor=west] at (0.0,3.2) {a equipe não avalia};
\node[k, draw=dred, dashed] (b1) at (8.0,1.3) {\textbf{sem} avaliação prévia};
\node[u, draw=dred] (b3) at (15.6,1.3) {\textbf{usuário avalia} e forma sua opinião: \textbf{encontra os problemas}};
\draw[->, line width=2.2pt, dred] (b1.east) -- (b3.west);
\node[font=\large, text width=19cm, align=center] at (10.0,-1.2) {o usuário final \textbf{sempre avalia}; à equipe cabe avaliar \textbf{antes}, principalmente em um sistema \textbf{inovador}};
""")
