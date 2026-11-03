"""Gera os diagramas TikZ da aula 8 de IHC (Design de IHC). Uso: python3 gerar.py && bash build.sh"""
exec(open("_helpers.py").read())

# ------------------------------------------------------------------ caminho do design
w("caminho-design", r"""
\tikzset{g/.style={dbox, fill=dshade!35, draw=black!40, line width=1.2pt, rounded corners=8pt},
        c/.style={dbox, text width=3.9cm, minimum height=1.35cm, font=\large, line width=1.5pt},
        m/.style={dbox, text width=4.2cm, minimum height=1.35cm, font=\large, line width=1.5pt}}
\node[g, minimum width=4.8cm, minimum height=6.6cm] at (2.4,4.1) {};
\node[font=\Large\bfseries, dblue, text width=4.4cm, align=center] at (2.4,7.0) {design conceitual};
\node[c, draw=dblue] at (2.4,5.4) {modelo conceitual};
\node[c, draw=dblue] at (2.4,3.5) {cenários de interação};
\node[g, minimum width=9.6cm, minimum height=6.6cm] at (10.1,4.1) {};
\node[font=\Large\bfseries, dgreen] at (10.1,7.0) {design da interação};
\node[m, draw=dgreen] at (7.8,5.4) {mapa de objetivos};
\node[m, draw=dgreen] at (12.4,5.4) {esquema de signos};
\node[m, draw=dgreen] at (7.8,3.5) {modelo de tarefas};
\node[m, draw=dgreen] at (12.4,3.5) {modelo de interação (MoLIC)};
\node[g, minimum width=3.8cm, minimum height=6.6cm] at (17.3,4.1) {};
\node[font=\Large\bfseries, dorange, text width=3.6cm, align=center] at (17.3,7.0) {interface};
\node[dbox, draw=dorange, text width=3.2cm, minimum height=1.35cm, font=\large, line width=1.5pt] at (17.3,5.4) {esboços e wireframes};
\node[dbox, draw=dorange, text width=3.2cm, minimum height=1.35cm, font=\large, line width=1.5pt] at (17.3,3.5) {protótipo};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (4.85,4.1) -- (5.25,4.1);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (14.95,4.1) -- (15.35,4.1);
\node[font=\Large, black!70, text width=18cm, align=center] at (9.7,0.3) {cada representação destaca \textbf{um aspecto} da solução e leva ao passo seguinte};
""")

# ------------------------------------------------------------------ conceitual x físico
w("conceitual-fisico", flow([
  ("Espaço do problema", "quem usa, para quê e em que contexto"),
  ("Design conceitual", r"o que o usuário \textbf{pode fazer} e que \textbf{conceitos} precisa entender"),
  ("Design físico", r"\textbf{como} a solução aparece e responde na interface")],
  w=5.2, h=3.6, cap=r"``Design é \textbf{como algo funciona}, não só o \emph{look and feel}'' (Steve Jobs)", capw=18))

# ------------------------------------------------------------------ modelos conceituais
w("modelos-conceituais", r"""
\tikzset{c/.style={dbox, text width=5.5cm, minimum height=2.9cm, font=\large, line width=1.5pt}}
\node[font=\Large\bfseries, dblue] at (6.1,8.7) {baseados em atividades};
\draw[black!40, dashed, line width=1.2pt, rounded corners=8pt] (-0.2,0.2) rectangle (12.4,8.2);
\node[c, draw=dblue] at (3.1,6.2) {\textbf{\textcolor{dblue}{Instrução}}\\ dar comandos ao sistema\\ ex.: roteador, linha de comando};
\node[c, draw=dgreen] at (9.2,6.2) {\textbf{\textcolor{dgreen}{Conversação}}\\ falar em linguagem natural\\ ex.: assistente virtual};
\node[c, draw=dorange] at (3.1,2.6) {\textbf{\textcolor{dorange}{Manipulação e navegação}}\\ agir sobre objetos na tela\\ ex.: editor de fotos, jogos};
\node[c, draw=dred] at (9.2,2.6) {\textbf{\textcolor{dred}{Exploração e pesquisa}}\\ explorar e buscar informação\\ ex.: loja virtual, biblioteca};
\node[font=\Large\bfseries, dgreen] at (16.0,8.7) {baseados em objetos};
\draw[black!40, dashed, line width=1.2pt, rounded corners=8pt] (13.2,0.2) rectangle (18.8,8.2);
\node[dbox, draw=dgreen, line width=1.5pt, text width=4.7cm, minimum height=6.6cm, font=\large, align=center] at (16.0,4.2) {transformam um \textbf{objeto do mundo real} em objeto digital\\[8pt] planilha: papel com células\\[4pt] \emph{desktop}: pasta e lixeira\\[4pt] calendário virtual\\[4pt] fichário de receitas};
""")

# ------------------------------------------------------------------ diagrama conceitual (exemplo)
w("diagrama-conceitual", r"""
\tikzset{n/.style={dstate, minimum size=2.5cm, font=\large\bfseries, line width=1.5pt, align=center},
        e/.style={-{Stealth[length=3mm]}, dblue, line width=1.7pt},
        l/.style={midway, fill=dcream, inner sep=2pt, font=\large\itshape}}
\draw[dshade!40, fill=dshade!25, line width=1pt, rounded corners=14pt] (-0.4,-0.6) rectangle (19.2,9.0);
\node[font=\large, black!60, anchor=north west] at (0.0,8.9) {\emph{background}: deslocar-se no mundo};
\node[n, draw=dblue] (p) at (2.3,4.2) {Pessoa};
\node[n, draw=dblue] (g) at (9.4,7.2) {Lugar};
\node[n, draw=dblue] (r) at (9.4,1.3) {Rota};
\node[n, draw=dblue] (m) at (16.3,3.3) {Mapa};
\node[n, draw=dblue] (a) at (16.3,7.2) {Avaliação};
\draw[e] (p) -- node[l] {busca} (g);
\draw[e, dorange, line width=3pt] (p) -- node[l, text=dorange, font=\large\bfseries\itshape] {pede} (r);
\draw[e] (r) -- node[l,pos=0.45] {leva a} (g);
\draw[e] (m) -- node[l] {desenha} (r);
\draw[e] (m) -- node[l] {marca} (g);
\draw[e] (g) -- node[l] {recebe} (a);
\node[font=\large, black!70, align=left, anchor=west] at (0.0,1.0) {\textbf{nó} = conceito\\ \textbf{conexão} = verbo};
\draw[dorange, line width=3pt, -{Stealth[length=3mm]}] (0.0,0.1) -- (1.0,0.1); \node[font=\large\bfseries, dorange, anchor=west] at (1.2,0.1) {relação principal};
""")

# ------------------------------------------------------------------ passos do diagrama
w("passos-diagrama", boxes([
  ("1. Listar elementos", "os conceitos-chave para resolver o problema do usuário"),
  ("2. Pensar as relações", "como esses elementos se relacionam entre si"),
  ("3. Eleger a relação principal", "a atividade central do usuário no sistema"),
  ("4. Desenhar nós e conexões", r"círculos para conceitos, linhas com \textbf{verbos}; o ``quê'', não o ``como''"),
  ("5. Expandir", "acrescentar as demais relações e conceitos"),
  ("6. Refinar", "manter claro e organizado; agrupar com cores e formas")],
  w=5.5, h=2.9, cols=3, cap=r"processo \textbf{iterativo}: volte a qualquer passo", capw=17))

# ------------------------------------------------------------------ cenários
w("cenarios-problema-interacao", r"""
\tikzset{c/.style={dbox, text width=5.6cm, minimum height=3.5cm, font=\large, line width=1.6pt}}
\node[c, draw=dred] (p) at (2.9,4.3) {\textbf{\textcolor{dred}{Cenário de problema}}\\ a secretária cadastra todos os projetos finais e trava no coorientador externo};
\node[c, draw=dblue] (a) at (11.4,7.0) {\textbf{\textcolor{dblue}{Cenário de interação A}}\\ o \textbf{professor} orientador cadastra os projetos dos seus alunos};
\node[c, draw=dgreen] (b) at (11.4,1.6) {\textbf{\textcolor{dgreen}{Cenário de interação B}}\\ o \textbf{próprio aluno} cadastra o seu projeto};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (p.east) -- (a.west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (p.east) -- (b.west);
\node[dbox, draw=dorange, fill=dorange!8, line width=1.6pt, text width=4.4cm, minimum height=6.4cm, font=\large, align=center] at (17.0,4.3) {\textbf{perguntas}\\ quem cadastra?\\ quando?\\ que dados?\\ quem confirma?\\[6pt] pode surgir uma \textbf{solução C}, mistura de A e B};
\node[font=\large, black!65, text width=5.4cm, align=center] at (2.9,1.2) {\textbf{sem} detalhes de interface (``lista \emph{dropdown}'')};
""")

# ------------------------------------------------------------------ conversa
w("conversa-niveis", r"""
\draw[dblue, line width=1.6pt, rounded corners=8pt, fill=dblue!6] (0,0) rectangle (9.6,8.6);
\node[font=\large\bfseries, dblue, anchor=north west] at (0.35,8.4) {conversa: tópico ``cadastrar trabalho''};
\draw[dgreen, line width=1.5pt, rounded corners=6pt, fill=dgreen!8] (0.5,0.5) rectangle (9.1,6.9);
\node[font=\large\bfseries, dgreen, anchor=north west] at (0.8,6.7) {diálogo: ``informar dados do trabalho''};
\draw[dorange, line width=1.4pt, rounded corners=5pt, fill=dorange!10] (1.0,1.0) rectangle (8.6,5.2);
\node[font=\large\bfseries, dorange, anchor=north west] at (1.3,5.0) {falas sobre \textbf{signos}};
\node[font=\large, anchor=west, align=left] at (1.4,3.0) {título\\ data de entrega\\ número de alunos\\ peso na nota};
\tikzset{u/.style={dbox, draw=dblue, fill=dblue!10, line width=1.4pt, text width=7.2cm, font=\large, align=left},
        d/.style={dbox, draw=dgreen, fill=dgreen!10, line width=1.4pt, text width=7.2cm, font=\large, align=left}}
\node[font=\large\bfseries, black!70] at (14.5,8.5) {a conversa, em turnos};
\node[u, anchor=west] at (10.6,7.2) {\textbf{U:} Preciso cadastrar um trabalho.};
\node[d, anchor=west] at (10.6,5.5) {\textbf{D:} Qual é o título e até quando deve ser entregue?};
\node[u, anchor=west] at (10.6,3.8) {\textbf{U:} Antes, quero ver os prazos do semestre.};
\node[d, anchor=west] at (10.6,2.3) {\textbf{D:} Ei-los.};
\node[font=\large, black!65, text width=8.4cm, align=center] at (14.9,0.6) {\textbf{U} = usuário $\cdot$ \textbf{D} = sistema, falando em nome do designer};
""")

# ------------------------------------------------------------------ objetivos
w("objetivos-tipos", r"""
\tikzset{c/.style={dbox, text width=6.6cm, minimum height=2.5cm, font=\large, line width=1.6pt}}
\node[c, draw=dblue, text width=5.8cm, minimum height=3.2cm] (f) at (15.5,4.4) {\textbf{\textcolor{dblue}{Objetivo final}}\\ o que leva o usuário ao sistema\\ ex.: \emph{cadastrar um projeto}};
\node[c, draw=dgreen] (d) at (4.0,7.2) {\textbf{\textcolor{dgreen}{Instrumental direto}}\\ ajuda \textbf{agora}, durante a tarefa\\ ex.: cadastrar um tipo novo de projeto enquanto cadastra};
\node[c, draw=dorange] (i) at (4.0,1.8) {\textbf{\textcolor{dorange}{Instrumental indireto}}\\ prepara o terreno para o \textbf{futuro}\\ ex.: cadastrar os tipos de projeto antes};
\draw[dgreen, line width=2.2pt, -{Stealth[length=3.4mm]}] (d.east) -- node[above, font=\large\bfseries, dgreen] {agora} (f.north west);
\draw[dorange, line width=2.2pt, dash pattern=on 8pt off 5pt, -{Stealth[length=3.4mm]}] (i.east) -- node[below, font=\large\bfseries, dorange] {depois} (f.south west);
""")

# ------------------------------------------------------------------ origem dos signos
w("signos-origem", boxes([
  ("Domínio", r"existe no mundo do usuário\\ ex.: nome e endereço de uma pessoa"),
  ("Convencional", r"já virou convenção na cultura dos usuários\\ ex.: \emph{zoom}, mapas"),
  ("Transformado", r"vem do domínio, com analogia\\ ex.: pasta, \emph{login} (assinatura)"),
  ("Aplicação", r"só faz sentido no sistema\\ ex.: \% de \emph{download}, enquadramento")],
  w=4.3, h=3.7, cols=4) + "\n" + r"""
\draw[dblue, line width=2.4pt, -{Stealth[length=4mm]}] (-2.0,-2.5) -- (16.8,-2.5);
\node[font=\large\bfseries, dgreen, anchor=north west] at (-2.0,-2.75) {pouca explicação};
\node[font=\large\bfseries, dred, anchor=north east] at (16.8,-2.75) {explicação completa};
\node[font=\large, black!70, anchor=north] at (7.4,-3.5) {quanto \textbf{mais novo} para o usuário, \textbf{mais} o designer explica};
""")

# ------------------------------------------------------------------ rupturas
w("rupturas-mecanismos", r"""
\tikzset{c/.style={dbox, text width=7.6cm, minimum height=2.3cm, font=\large, line width=1.6pt},
        sg/.style={circle, fill=white, line width=1.5pt, font=\normalsize\bfseries, inner sep=1pt, minimum size=0.95cm}}
\node[font=\Large\bfseries, dblue] at (4.4,9.3) {prevenir (antes)};
\node[font=\Large\bfseries, dorange] at (15.0,9.3) {recuperar (depois)};
\node[c, draw=dblue] (pp) at (4.4,7.3) {\textbf{\textcolor{dblue}{Prevenção passiva}}\\ explica a linguagem\\ \small ex.: dica ``(dd/mm/aaaa)''};
\node[c, draw=dgreen] (pa) at (4.4,4.6) {\textbf{\textcolor{dgreen}{Prevenção ativa}}\\ impede a fala inválida\\ \small ex.: botão desabilitado};
\node[c, draw=dred] (al) at (4.4,1.9) {\textbf{\textcolor{dred}{Alerta}}\\ pede uma decisão ao usuário\\ \small ex.: ``o arquivo já existe, sobrescrever?''};
\draw[dred, dashed, line width=2.2pt] (9.7,0.4) -- (9.7,8.8);
\node[font=\large\bfseries, dred, fill=dcream, inner sep=3pt, rotate=90] at (9.7,4.6) {ruptura};
\node[c, draw=dorange] (ra) at (15.0,6.2) {\textbf{\textcolor{dorange}{Recuperação apoiada}}\\ ajuda o usuário a corrigir\\ \small ex.: destaca o campo com erro};
\node[c, draw=dred] (ce) at (15.0,2.9) {\textbf{\textcolor{dred}{Captura de erro}}\\ orienta o que fazer fora do sistema\\ \small ex.: ``copie o arquivo de novo''};
\node[sg, draw=dblue, text=dblue] at ($(pp.north west)+(0.1,-0.1)$) {PP};
\node[sg, draw=dgreen, text=dgreen] at ($(pa.north west)+(0.1,-0.1)$) {PA};
\node[sg, draw=dred, text=dred] at ($(al.north west)+(0.1,-0.1)$) {AL};
\node[sg, draw=dorange, text=dorange] at ($(ra.north west)+(0.1,-0.1)$) {RA};
\node[sg, draw=dred, text=dred] at ($(ce.north west)+(0.1,-0.1)$) {CE};
""")

# ------------------------------------------------------------------ estruturas de tarefa
def mini(x, y, tit, kids, kind):
    o = [r"\node[font=\large\bfseries, dblue] at (%s,%s) {%s};" % (x, y + 3.1, tit)]
    o.append(r"\node[dbox, draw=black!70, rounded corners=9pt, line width=1.4pt, minimum width=3.2cm, minimum height=0.9cm, font=\normalsize] (p) at (%s,%s) {Objetivo};" % (x, y + 1.9))
    xs = [x - 1.5, x + 1.5]
    for i, (k, xx) in enumerate(zip(kids, xs)):
        sty = "draw=black!70"
        if kind == "opc" and i == 0: sty = "draw=black!70, dashed"
        o.append(r"\node[dbox, %s, line width=1.4pt, minimum width=2.7cm, minimum height=1.0cm, font=\normalsize, inner sep=3pt] (k%d) at (%s,%s) {%s};" % (sty, i, xx, y, k))
        o.append(r"\draw[black!70, line width=1.2pt] (p.south) -- (k%d.north);" % i)
    if kind == "alt":
        for i, xx in enumerate(xs): o.append(r"\draw[black!70, fill=white, line width=1.1pt] (%s,%s) circle (0.17);" % (xx + 1.2, y + 0.55))
    if kind == "iter":
        o.append(r"\node[font=\Large\bfseries, dred] at (%s,%s) {*};" % (xs[0] + 1.2, y + 0.6))
    if kind == "ubi":
        o.append(r"\fill[dred] ($(p.south)!0.55!(k1.north)$) circle (0.16);")
    return "\n".join(o)
w("tarefas-estruturas", "\n".join([
  mini(3.2, 5.6, "sequencial", ["1 Definir", "2 Efetuar"], "seq"),
  mini(9.5, 5.6, r"independente de ordem", ["1? Critério", "2? Valor"], "ind"),
  mini(15.8, 5.6, "alternativa", ["A Simples", "B Avançada"], "alt"),
  mini(3.2, 0.6, "iterativa (*)", ["Critério", "Examinar"], "iter"),
  mini(9.5, 0.6, r"ubíqua (ponto cheio)", ["Definir", "Sair"], "ubi"),
  mini(15.8, 0.6, r"opcional (tracejada)", ["Escolher tipo", "Efetuar"], "opc"),
]))

# ------------------------------------------------------------------ MoLIC: elementos
def cell(x, y, cap, body):
    return body + "\n" + r"\node[font=\large, black!75, text width=5.6cm, align=center] at (%s,%s) {%s};" % (x, y - 1.5, cap)
CENA = r"\node[dbox, draw=dblue, rounded corners=9pt, line width=1.5pt, minimum width=%scm, minimum height=0.95cm, font=\normalsize, inner sep=3pt] (%s) at (%s,%s) {%s};"
def cena(n, x, y, t, wd=2.2, extra=""): return (CENA % (wd, n, x, y, t)).replace("draw=dblue", "draw=dblue" + extra)
w("molic-elementos", "\n".join([
  cell(3.2, 7.6, r"\textbf{cena}: conversa sobre um tópico", cena("a1", 3.2, 7.6, "Consultar aviso", 3.6)),
  cell(9.5, 7.6, r"\textbf{fala do usuário} \texttt{u:} (mudança de tópico)",
       cena("b1", 8.0, 7.6, "A", 1.1) + cena("b2", 11.0, 7.6, "B", 1.1) + r"\draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (b1.east) -- node[above, font=\normalsize] {u: ver} (b2.west);"),
  cell(15.8, 7.6, r"\textbf{fala do designer} \texttt{d:} (resposta)",
       cena("c1", 14.3, 7.6, "A", 1.1) + cena("c2", 17.3, 7.6, "B", 1.1) + r"\draw[dgreen, line width=1.6pt, -{Stealth[length=2.6mm]}] (c1.east) -- node[above, font=\normalsize] {d: pronto} (c2.west);"),
  cell(3.2, 4.2, r"\textbf{processo do sistema}: caixa-preta que interpreta a fala",
       r"\fill[black] (2.7,3.9) rectangle ++(1.0,0.95);"),
  cell(9.5, 4.2, r"\textbf{acesso ubíquo}: começa uma conversa de qualquer ponto",
       r"\node[dbox, draw=black!50, fill=black!20, rounded corners=9pt, minimum width=1.3cm, minimum height=0.95cm] (u1) at (7.3,4.4) {};" + cena("u2", 11.9, 4.4, "Consultar", 2.4) + r"\draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (u1.east) -- node[above, font=\normalsize] {u: avisos} (u2.west);"),
  cell(15.8, 4.2, r"\textbf{abertura} e \textbf{encerramento} da conversa",
       r"\fill[black] (13.9,4.4) circle (0.28); \draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (14.3,4.4) -- (15.6,4.4);" + cena("v1", 16.7, 4.4, "Login", 1.8) + r"\draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (17.6,4.4) -- (18.3,4.4); \draw[black, fill=white, line width=1.2pt] (18.55,4.4) circle (0.28); \fill[black] (18.55,4.4) circle (0.14);"),
  cell(3.2, 0.8, r"\textbf{ruptura}: fala de recuperação tracejada",
       cena("r1", 1.3, 0.8, "Busca", 1.5) + cena("r2", 5.5, 0.8, "Início", 1.5) + r"\draw[dred, dash pattern=on 6pt off 4pt, line width=1.6pt, -{Stealth[length=2.6mm]}] (r1.east) -- node[above, font=\normalsize] {u: cancelar} (r2.west);"),
  cell(9.5, 0.8, r"\textbf{alerta} ou \textbf{captura de erro}: cena tracejada",
       r"\node[dbox, draw=dred, dashed, rounded corners=9pt, line width=1.5pt, minimum width=3.8cm, minimum height=0.95cm, font=\normalsize] at (9.5,0.8) {Confirmar sobreposição};"),
  cell(15.8, 0.8, r"\textbf{precondição}: só vale se a condição for verdadeira",
       cena("p1", 14.0, 0.8, "Trabalho", 1.9) + cena("p2", 17.6, 0.8, "Notas", 1.6) + r"\draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (p1.east) -- node[above, font=\small, align=center, yshift=3pt] {precond: nota\\ lançada} (p2.west);"),
]))

# ------------------------------------------------------------------ MoLIC: exemplo (busca)
w("molic-exemplo", r"""
\tikzset{s/.style={dbox, draw=dblue, rounded corners=10pt, line width=1.6pt, font=\large, inner sep=4pt},
        l/.style={font=\normalsize, fill=dcream, inner sep=1.5pt},
        a/.style={dtrans, line width=1.7pt, -{Stealth[length=3mm]}},
        r/.style={dred, dash pattern=on 7pt off 4pt, line width=1.7pt, -{Stealth[length=3mm]}}}
\node[s, minimum width=3.6cm, minimum height=1.6cm] (b) at (2.4,4.4) {Buscar material};
\node[draw=black, fill=black, minimum size=1.1cm, inner sep=0pt] (x) at (8.3,4.4) {};
\node[s, minimum width=4.2cm, minimum height=1.6cm] (l) at (14.7,4.4) {Examinar lista de material};
\node[s, minimum width=4.4cm, minimum height=1.6cm] (g) at (8.3,8.0) {Examinar progresso da busca};
\node[s, minimum width=3.6cm, minimum height=1.4cm] (e) at (14.7,0.8) {Editar material};
\draw[a] (b.east) -- node[l, pos=0.5] {u: iniciar busca} (x.west);
\draw[a] (x.east) -- node[l, pos=0.5, align=center] {d: n itens\\ encontrados} (l.west);
\draw[black!60, line width=1.5pt, -{Stealth[length=2.6mm]}] (x.north) -- node[l, align=center, pos=0.42] {d: \%n\\ concluída} (g.south);
\draw[r] (g.west) to[bend right=25] node[l, pos=0.45] {u: cancelar} (b.north);
\draw[r] (x.south) -- ++(0,-1.9) -| node[l, pos=0.25, align=center] {d: nenhum item\\ encontrado} (b.south);
\draw[a] (l.south) -- node[l] {u: editar material X} (e.north);
\node[font=\large, black!70, text width=6cm, align=left, anchor=west] at (0.1,0.5) {linha \textcolor{dred}{tracejada} = recuperação de ruptura};
""")

# ------------------------------------------------------------------ estilos de interação
def _estilo_icone(k, x, y, c):
    o = []
    if k == 0:
        o.append(r"\fill[black!80, rounded corners=3pt] (%s,%s) rectangle (%s,%s);" % (x - 1.25, y - 0.8, x + 1.25, y + 0.8))
        o.append(r"\node[white, font=\small\ttfamily, align=left, anchor=west] at (%s,%s) {>\ copy a b\\ >\_};" % (x - 1.1, y + 0.05))
    elif k == 1:
        o.append(r"\node[dbox, draw=%s, fill=%s!18, rounded corners=7pt, line width=1.2pt, minimum width=1.7cm, minimum height=0.6cm, font=\scriptsize, inner sep=2pt] at (%s,%s) {reservar sala};" % (c, c, x - 0.35, y + 0.42))
        o.append(r"\node[dbox, draw=%s, fill=white, rounded corners=7pt, line width=1.2pt, minimum width=1.7cm, minimum height=0.6cm, font=\scriptsize, inner sep=2pt] at (%s,%s) {para quando?};" % (c, x + 0.35, y - 0.4))
    elif k == 2:
        o.append(r"\node[dbox, draw=%s, fill=%s!12, rounded corners=1pt, line width=1.1pt, minimum width=1.8cm, minimum height=0.42cm, font=\scriptsize, inner sep=1pt] at (%s,%s) {Arquivo v};" % (c, c, x, y + 0.62))
        for j, (t, hi) in enumerate([("Abrir", False), ("Salvar", True), ("Sair", False)]):
            fill = "%s!30" % c if hi else "white"
            o.append(r"\node[dbox, draw=black!55, fill=%s, rounded corners=0pt, line width=0.9pt, minimum width=1.8cm, minimum height=0.4cm, font=\scriptsize, inner sep=1pt] at (%s,%s) {%s};" % (fill, x, round(y + 0.2 - j * 0.4, 2), t))
    elif k == 3:
        for j, t in enumerate(("Nome", "Data")):
            yy = y + 0.5 - j * 0.5
            o.append(r"\node[font=\scriptsize, anchor=west] at (%s,%s) {%s};" % (x - 1.25, yy, t))
            o.append(r"\draw[black!60, fill=white, line width=1pt] (%s,%s) rectangle (%s,%s);" % (x - 0.1, yy - 0.18, x + 1.2, yy + 0.18))
        o.append(r"\node[dbox, draw=%s, fill=%s!18, rounded corners=2pt, line width=1.1pt, minimum width=0.9cm, minimum height=0.4cm, font=\scriptsize, inner sep=1pt] at (%s,%s) {OK};" % (c, c, x + 0.75, y - 0.62))
    else:
        o.append(r"\draw[black!65, fill=white, line width=1.2pt] (%s,%s) rectangle (%s,%s);" % (x - 1.15, y - 0.2, x - 0.6, y + 0.65))
        o.append(r"\draw[%s, fill=%s!25, line width=1.3pt] (%s,%s) rectangle (%s,%s);" % (c, c, x + 0.35, y - 0.65, x + 1.2, y - 0.05))
        o.append(r"\draw[%s, fill=%s!25, line width=1.3pt] (%s,%s) rectangle (%s,%s);" % (c, c, x + 0.35, y - 0.05, x + 0.7, y + 0.1))
        o.append(r"\draw[black!60, dashed, line width=1.2pt, -{Stealth[length=2.4mm]}] (%s,%s) -- (%s,%s);" % (x - 0.5, y + 0.2, x + 0.3, y - 0.35))
        o.append(r"\fill[black] (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- cycle;" % (
            x - 0.62, y + 0.45, x - 0.62, y - 0.15, x - 0.5, y - 0.03, x - 0.41, y - 0.25, x - 0.33, y - 0.21, x - 0.42, y + 0.0, x - 0.25, y + 0.0))
    return "\n".join(o)
_ES = [
  ("Linguagem de comando", r"digitar comandos\\ preciso e rápido para quem sabe\\ exige memorizar"),
  ("Linguagem natural", r"falar como numa conversa\\ fácil para novatos\\ difícil resolver ambiguidades"),
  ("Menus", r"escolher entre opções\\ reconhecer em vez de lembrar"),
  ("Formulários", r"preencher campos\\ cuidado com erros de preenchimento"),
  ("Manipulação direta", r"agir sobre objetos\\ ações rápidas, incrementais e reversíveis"),
]
_o = []
for i, (t, d) in enumerate(_ES):
    x = round(i * 3.95, 2); c = CS[i % 4]
    _o.append(r"\node[dbox, draw=%s, line width=1.5pt, text width=3.35cm, minimum height=6.0cm] at (%s,0) {};" % (c, x))
    _o.append(r"\draw[%s, line width=1pt] (%s,0.55) -- (%s,0.55);" % (c, x - 1.5, x + 1.5))
    _o.append(_estilo_icone(i, x, 1.75, c))
    _o.append(r"\node[font=\normalsize, text width=3.1cm, align=center, anchor=north] at (%s,0.35) {\textbf{\textcolor{%s}{%s}}\\[3pt] %s};" % (x, c, t, d))
w("estilos-interacao", "\n".join(_o))

# ------------------------------------------------------------------ fidelidade
w("fidelidade", r"""
\tikzset{legen/.style={font=\large, black!70, text width=5.6cm, align=center}}
% ---------- baixa ----------
\node[font=\Large\bfseries, black!75] at (2.7,9.0) {baixa fidelidade};
\draw[black!60, dashed, line width=1.5pt, rounded corners=5pt] (0,1.7) rectangle (5.4,8.3);
\draw[black!55, line width=1.4pt] (0.4,7.4) -- (3.4,7.4);
\foreach \y in {6.3,5.4,4.5} {\draw[black!45, dashed, line width=1.2pt] (0.4,\y) rectangle (5.0,\y-0.6);}
\draw[black!55, dashed, line width=1.4pt] (3.3,2.7) rectangle (5.0,2.1);
\node[font=\normalsize, black!65] at (4.15,2.4) {Gravar};
% ---------- média ----------
\node[font=\Large\bfseries, dgreen] at (9.5,9.0) {média fidelidade};
\draw[black!70, line width=1.5pt, rounded corners=5pt, fill=white] (6.8,1.7) rectangle (12.2,8.3);
\fill[black!22] (6.8,7.5) rectangle (12.2,8.3); \node[font=\large\bfseries, black!80] at (9.5,7.9) {Materiais didáticos};
\foreach \y/\t in {6.7/{Aula 1 --- Introdução},5.8/{Aula 2 --- Conceitos},4.9/{Aula 3 --- Fatores}} {
  \draw[black!55, fill=black!6, line width=1.1pt] (7.2,\y) rectangle (11.8,\y-0.65);
  \node[font=\normalsize, anchor=west, black!80] at (7.4,\y-0.33) {\t};}
\draw[black!60, fill=black!15, line width=1.2pt] (10.0,2.7) rectangle (11.8,2.1); \node[font=\normalsize, black!80] at (10.9,2.4) {Gravar};
% ---------- alta ----------
\node[font=\Large\bfseries, dblue] at (16.3,9.0) {alta fidelidade};
\draw[dblue, line width=1.5pt, rounded corners=5pt, fill=white] (13.6,1.7) rectangle (19.0,8.3);
\fill[dblue] (13.6,7.5) rectangle (19.0,8.3); \node[font=\large\bfseries, white] at (16.3,7.9) {Materiais didáticos};
\foreach \y/\t in {6.7/{Aula 1 --- Introdução},5.8/{Aula 2 --- Conceitos},4.9/{Aula 3 --- Fatores}} {
  \draw[dshade, fill=dcream, line width=1.2pt] (14.0,\y) rectangle (18.6,\y-0.65);
  \node[font=\normalsize, anchor=west] at (14.2,\y-0.33) {\t};}
\draw[dblue, fill=dblue, rounded corners=3pt] (16.9,2.7) rectangle (18.6,2.1); \node[font=\normalsize\bfseries, white] at (17.75,2.4) {Gravar};
% ---------- setas ----------
\draw[dtrans, line width=2.4pt, -{Stealth[length=3.6mm]}] (5.6,5.0) -- (6.6,5.0);
\draw[dtrans, line width=2.4pt, -{Stealth[length=3.6mm]}] (12.4,5.0) -- (13.4,5.0);
""")

# ------------------------------------------------------------------ MoLIC -> interface
def mapa(rows, tl, tr, wl=7.2, wr=8.6, dy=1.3, y0=7.4):
    o = [r"\node[font=\Large\bfseries, black!75] at (3.9,%s) {%s};" % (y0 + 1.2, tl), r"\node[font=\Large\bfseries, black!75] at (14.6,%s) {%s};" % (y0 + 1.2, tr)]
    for i, (a, b) in enumerate(rows):
        y = round(y0 - i * dy, 2); col = CS[i % 4]
        o.append(r"\node[dbox, draw=%s, line width=1.5pt, text width=%scm, minimum height=1.0cm, font=\large] (l%d) at (3.9,%s) {%s};" % (col, wl, i, y, a))
        o.append(r"\node[dbox, draw=%s, line width=1.5pt, text width=%scm, minimum height=1.0cm, font=\large] (r%d) at (14.6,%s) {%s};" % (col, wr, i, y, b))
        o.append(r"\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (l%d.east) -- (r%d.west);" % (i, i))
    return "\n".join(o)
w("molic-para-interface", mapa([
  (r"\textbf{cena}", "unidade de apresentação (tela ou página)"),
  (r"\textbf{diálogo}", "quadro ou grupo de elementos"),
  (r"\textbf{signo}", r"elemento de interface (\emph{widget})"),
  (r"\textbf{fala do usuário} (\texttt{u:})", "link, botão ou item de menu"),
  (r"\textbf{precondição}", "elemento desativado ou oculto"),
  (r"\textbf{fala do designer} (\texttt{d:})", "mensagem de erro ou de status"),
  (r"\textbf{acesso ubíquo}", "barra de navegação ou menu")],
  "modelo de interação (MoLIC)", "interface"))

# ------------------------------------------------------------------ ajuda
w("ajuda-perguntas", mapa([
  (r"O que posso fazer com isto?", "objetivos: personas, cenários, mapa de objetivos"),
  (r"O que é isto? O que faz?", "conceitual (domínio) e operacional (interface)"),
  (r"Como faço isto?", "modelos de tarefas e de interação"),
  (r"O que posso fazer agora?", "cena atual e precondições satisfeitas"),
  (r"O que está acontecendo? Por quê?", "falas do sistema e \\emph{feedback}"),
  (r"Onde estou? O que fiz?", "histórico de interação do usuário"),
  (r"Por que devo usar? Como me beneficia?", "intenção de design, registrada no início")],
  "dúvida do usuário", "onde está a resposta", wl=7.6, wr=9.4))

# ------------------------------------------------------------------ adaptável x adaptativo
w("adaptavel-adaptativo", r"""
\tikzset{c/.style={dbox, text width=8.4cm, minimum height=5.6cm, font=\large, line width=1.6pt, align=left, anchor=north}}
\node[c, draw=dblue] at (4.6,7.6) {\textbf{\textcolor{dblue}{Adaptável}}: o \textbf{usuário} configura ou estende\\[6pt] $\bullet$ comunicar o que pode ser mudado\\ $\bullet$ permitir que ele faça a mudança\\ $\bullet$ explicar as consequências e ajudar a testar\\ $\bullet$ restringir o que muda, para preservar a identidade do sistema};
\node[c, draw=dgreen] at (14.4,7.6) {\textbf{\textcolor{dgreen}{Adaptativo}}: o \textbf{sistema} se ajusta sozinho\\[6pt] $\bullet$ comunicar cada mudança feita\\ $\bullet$ permitir \textbf{desfazer} a adaptação\\ $\bullet$ permitir impedir novas adaptações\\ $\bullet$ aprender com o \emph{feedback} do usuário};
\node[dbox, draw=dblue, text width=2.2cm, font=\large\bfseries, minimum height=1.0cm] (u1) at (1.8,0.4) {usuário};
\node[dbox, draw=dblue, text width=2.2cm, font=\large\bfseries, minimum height=1.0cm] (s1) at (7.4,0.4) {sistema};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (u1.east) -- (s1.west);
\node[dbox, draw=dgreen, text width=2.2cm, font=\large\bfseries, minimum height=1.0cm] (s2) at (11.6,0.4) {sistema};
\node[dbox, draw=dgreen, text width=2.2cm, font=\large\bfseries, minimum height=1.0cm] (u2) at (17.2,0.4) {usuário};
\draw[dgreen, line width=2pt, -{Stealth[length=3.2mm]}] (s2.east) -- (u2.west);
""")

# ------------------------------------------------------------------ anatomia do modelo conceitual
w("modelo-conceitual-anatomia", r"""
\tikzset{c/.style={dbox, text width=5.2cm, minimum height=2.6cm, font=\large, line width=1.6pt}}
\node[dbox, draw=dblue, fill=dblue!8, line width=2pt, text width=8cm, minimum height=1.5cm, font=\Large\bfseries] (m) at (9.5,7.4) {Modelo conceitual};
\node[c, draw=dblue] (a) at (3.5,4.0) {\textbf{\textcolor{dblue}{O que faz}}\\ o que o usuário pode fazer com o sistema};
\node[c, draw=dgreen] (b) at (9.5,4.0) {\textbf{\textcolor{dgreen}{Como se comporta}}\\ e quais conceitos ele precisa entender};
\node[c, draw=dorange] (c) at (15.5,4.0) {\textbf{\textcolor{dorange}{Com o que se parece}}\\ em termos de funcionamento, não de tela};
\draw[black!55, line width=1.5pt, -{Stealth[length=3mm]}] (m.south) -- (b.north);
\draw[black!55, line width=1.5pt, -{Stealth[length=3mm]}] (m.south west) -- (a.north);
\draw[black!55, line width=1.5pt, -{Stealth[length=3mm]}] (m.south east) -- (c.north);
\node[dbox, draw=dred, dashed, line width=1.5pt, text width=6.6cm, minimum height=1.5cm, font=\large] (n) at (4.4,0.5) {\textcolor{dred}{\textbf{não é}} esboço nem \emph{wireframes}};
\node[dbox, draw=dgreen, fill=dgreen!6, line width=1.5pt, text width=8.2cm, minimum height=1.5cm, font=\large] at (14.0,0.5) {discutido com clientes e usuários \textbf{antes} da implementação};
""")

# ------------------------------------------------------------------ quando usar cada tipo
_L = [
 ("Instrução", "precisão e controle; usuários experientes", "curva de aprendizado íngreme"),
 ("Conversação", "natural e fácil para novatos", "menos precisa; pode frustrar"),
 (r"Manipulação e navegação", r"direta e visual: jogos, edição, realidade aumentada", r"tarefas abstratas ou com muitas etapas"),
 (r"Exploração e pesquisa", "buscas e catálogos", r"exige boa estrutura da informação"),
 ("Objetos", r"familiar e fácil de aprender (planilha, calendário)", r"a metáfora pode limitar funções novas"),
]
def _icone(k, x, y, c):
    o = [r"\draw[%s, fill=white, line width=1.6pt, rounded corners=4pt] (%s,%s) rectangle ++(1.3,1.3);" % (c, x - 0.65, y - 0.65)]
    if k == 0:
        o.append(r"\fill[black!80, rounded corners=2pt] (%s,%s) rectangle (%s,%s);" % (x - 0.5, y - 0.36, x + 0.5, y + 0.36))
        o.append(r"\node[white, font=\small\ttfamily] at (%s,%s) {>\_};" % (x, y))
    elif k == 1:
        o.append(r"\draw[dgreen, fill=dgreen!22, line width=1.1pt, rounded corners=3pt] (%s,%s) rectangle (%s,%s);" % (x - 0.5, y + 0.02, x + 0.1, y + 0.4))
        o.append(r"\draw[dgreen, fill=white, line width=1.1pt, rounded corners=3pt] (%s,%s) rectangle (%s,%s);" % (x - 0.1, y - 0.42, x + 0.5, y - 0.04))
        o.append(r"\fill[dgreen] (%s,%s) circle (0.04) (%s,%s) circle (0.04) (%s,%s) circle (0.04);" % (x - 0.3, y + 0.21, x - 0.2, y + 0.21, x - 0.1, y + 0.21))
    elif k == 2:
        o.append(r"\draw[dorange, fill=dorange!25, line width=1.2pt] (%s,%s) rectangle (%s,%s);" % (x - 0.45, y - 0.3, x - 0.03, y + 0.12))
        o.append(r"\fill[black] (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- cycle;" % (
            x + 0.05, y + 0.38, x + 0.05, y - 0.22, x + 0.17, y - 0.1, x + 0.26, y - 0.32, x + 0.34, y - 0.28, x + 0.25, y - 0.07, x + 0.42, y - 0.07))
    elif k == 3:
        o.append(r"\draw[dred, fill=dred!10, line width=2pt] (%s,%s) circle (0.27);" % (x - 0.1, y + 0.1))
        o.append(r"\draw[dred, line width=3pt, line cap=round] (%s,%s) -- (%s,%s);" % (x + 0.1, y - 0.1, x + 0.38, y - 0.38))
    else:
        o.append(r"\fill[dblue!22] (%s,%s) rectangle ++(0.84,0.28);" % (x - 0.42, y + 0.14))
        o.append(r"\draw[dblue, step=0.28, line width=1pt] (%s,%s) grid ++(0.84,0.84);" % (x - 0.42, y - 0.42))
    return "\n".join(o)
_o = [r"\node[font=\Large\bfseries, dgreen] at (10.0,8.7) {bom para};", r"\node[font=\Large\bfseries, dred] at (16.3,8.7) {cuidado com};"]
for i, (t, g, r) in enumerate(_L):
    y = round(7.2 - i * 1.55, 2); c = CS[i % 4]
    _o.append(_icone(i, 0.95, y, c))
    _o.append(r"\node[dbox, draw=%s, line width=1.6pt, text width=3.4cm, minimum height=1.3cm, font=\large\bfseries] at (4.1,%s) {\textcolor{%s}{%s}};" % (c, y, c, t))
    _o.append(r"\node[dbox, draw=dgreen, fill=dgreen!6, line width=1.5pt, text width=5.4cm, minimum height=1.3cm, font=\large] at (10.0,%s) {%s};" % (y, g))
    _o.append(r"\node[dbox, draw=dred, fill=dred!6, line width=1.5pt, text width=5.4cm, minimum height=1.3cm, font=\large] at (16.3,%s) {%s};" % (y, r))
w("quando-usar-atividade", "\n".join(_o))

# ------------------------------------------------------------------ mapa de objetivos (simplificado)
w("mapa-objetivos", r"""
\tikzset{ob/.style={dbox, rounded corners=9pt, line width=1.6pt, minimum width=4.0cm, minimum height=1.2cm, font=\large},
        inst/.style={dbox, rounded corners=9pt, line width=1.6pt, minimum width=4.0cm, minimum height=1.2cm, font=\large, dashed, fill=dorange!10},
        ba/.style={circle, draw=black!60, fill=white, line width=1pt, font=\small\bfseries, inner sep=1.5pt, minimum size=0.62cm},
        ar/.style={-{Stealth[length=3mm]}, dblue, line width=1.8pt}}
\draw[black!40, dashed, line width=1.2pt, rounded corners=8pt] (-0.3,1.9) rectangle (9.2,8.3);
\node[font=\Large\bfseries, dblue] at (4.45,8.9) {entidade: material didático};
\node[ob, draw=dblue] (c1) at (4.45,6.5) {consultar material};
\node[ob, draw=dblue] (a1) at (1.9,3.0) {alterar material};
\node[ob, draw=dblue] (e1) at (7.0,3.0) {excluir material};
\draw[black!40, dashed, line width=1.2pt, rounded corners=8pt] (9.8,1.9) rectangle (20.1,8.3);
\node[font=\Large\bfseries, dgreen] at (14.95,8.9) {entidade: trabalho};
\node[ob, draw=dgreen] (c2) at (14.95,6.5) {consultar trabalho};
\node[ob, draw=dgreen] (a2) at (12.0,3.0) {alterar trabalho};
\node[inst, draw=dorange] (t2) at (17.7,3.0) {customizar tipos de trabalho};
\node[ba] at ($(c1.north west)+(0.1,0.1)$) {PA}; \node[ba] at ($(a1.north west)+(0.1,0.1)$) {P}; \node[ba] at ($(e1.north west)+(0.1,0.1)$) {P};
\node[ba] at ($(c2.north west)+(0.1,0.1)$) {PA}; \node[ba] at ($(a2.north west)+(0.1,0.1)$) {P}; \node[ba] at ($(t2.north west)+(0.1,0.1)$) {P};
\draw[ar] (c1.south) -- (a1.north);
\draw[ar] (c1.south) -- (e1.north);
\draw[ar] (c2.south) -- (a2.north);
\draw[ar, dorange, dashed] (t2.west) -- (a2.east);
\node[ob, draw=black!60, minimum width=2.4cm, minimum height=0.8cm, font=\normalsize] at (1.5,0.5) {final};
\node[inst, draw=dorange, minimum width=2.4cm, minimum height=0.8cm, font=\normalsize] at (4.4,0.5) {instrumental};
\draw[ar] (6.2,0.5) -- (8.0,0.5); \node[font=\normalsize, anchor=west] at (8.1,0.5) {instrumenta diretamente};
\node[font=\normalsize, anchor=west] at (13.0,0.5) {\textbf{P} professor $\cdot$ \textbf{A} aluno};
""")

# ------------------------------------------------------------------ esquema de signos: conteúdo (exemplo)
_E = [0, 4.6, 9.6, 12.8]
_o = [r"\node[dbox, draw=dblue, fill=dblue!12, line width=1.6pt, minimum width=12.8cm, minimum height=0.95cm, font=\large\bfseries, anchor=south west, rounded corners=3pt] at (0,7.45) {Enunciado de trabalho (E)};"]
def _lin(y, cel, cab=False, mais=False):
    o = []
    for j, t in enumerate(cel):
        x0, x1 = _E[j], _E[j + 1]
        fill = "dshade!55" if cab else "white"
        o.append(r"\draw[black!60, fill=%s, line width=1pt] (%s,%s) rectangle (%s,%s);" % (fill, x0, y - 0.45, x1, y + 0.45))
        fnt = r"\normalsize\bfseries" if (cab or (mais and j == 0)) else r"\normalsize"
        col = "dblue" if (mais and j == 0) else "black"
        o.append(r"\node[font=%s, text=%s, text width=%scm, align=center] at (%s,%s) {%s};" % (fnt, col, round(x1 - x0 - 0.3, 2), round((x0 + x1) / 2, 2), y, t))
    return "\n".join(o)
_o.append(_lin(7.0, ["signo (atributo)", "restrição de conteúdo", "valor padrão"], cab=True))
for k, (a, b, c) in enumerate([(r"+ título", "não pode ser nulo", "---"), ("data de entrega", "data futura", "---"), ("formato de entrega", "conjunto flexível", "relatório"), ("número máximo de alunos", "de 1 a 6", "1 (individual)"), ("peso", "de 0 a 1", r"1 (100\%)")]):
    _o.append(_lin(round(6.05 - k * 0.95, 2), [a, b, c], mais=a.startswith("+")))
_o.append(r"\node[font=\large, black!75, text width=12.8cm, align=center] at (6.4,1.0) {\textbf{\textcolor{dblue}{+}} identifica a entidade\\ inicial maiúscula = entidade (E); minúscula = atributo};")
_o.append(r"\node[dbox, draw=dgreen, line width=1.6pt, text width=4.0cm, minimum height=2.3cm, font=\large] (al) at (16.9,6.6) {\textbf{\textcolor{dgreen}{Aluno (A)}}\\ \textbf{+} matrícula\\ nome};")
_o.append(r"\node[dbox, draw=dorange, line width=1.6pt, text width=4.0cm, minimum height=3.4cm, font=\large] (tr) at (16.9,2.6) {\textbf{\textcolor{dorange}{Trabalho entregue (T)}}\\ \textbf{+} Enunciado (E)\\ \textbf{+} Alunos (A)\\ relatório\\ nota};")
_o.append(r"\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (al.south) -- node[right, font=\large\itshape, fill=dcream, inner sep=1.5pt] {realiza} (tr.north);")
_o.append(r"\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (12.85,2.6) -- node[above, font=\large\itshape, fill=dcream, inner sep=1.5pt] {define} (tr.west);")
w("esquema-signos-conteudo", "\n".join(_o))

# ------------------------------------------------------------------ MoLIC: visão geral
def _mini(x, y, cor):
    o = []
    for i, dx in enumerate((-1.9, 0.0, 1.9)):
        o.append(r"\node[dbox, draw=%s, rounded corners=6pt, line width=1.3pt, minimum width=1.35cm, minimum height=0.6cm, inner sep=1pt] (m%s_%d) at (%s,%s) {};" % (cor, str(x).replace('.', ''), i, x + dx, y))
    for i in range(2):
        o.append(r"\draw[%s, line width=1.3pt, -{Stealth[length=2mm]}] (m%s_%d.east) -- (m%s_%d.west);" % (cor, str(x).replace('.', ''), i, str(x).replace('.', ''), i + 1))
    return "\n".join(o)
w("molic-visao-geral", r"""
\tikzset{c/.style={dbox, line width=1.6pt, font=\large}}
\node[font=\Large\bfseries, black!70] at (2.5,9.2) {ponto de partida};
\node[font=\Large\bfseries, black!70] at (9.6,9.2) {um diagrama por papel};
\node[font=\Large\bfseries, black!70] at (16.4,9.2) {em duas etapas};
\node[c, draw=dgreen, text width=3.8cm, minimum height=3.0cm] (mo) at (2.5,4.9) {\textbf{\textcolor{dgreen}{Mapa de objetivos}}\\ o que cada papel quer alcançar};
\node[c, draw=dblue, text width=5.2cm, minimum height=2.8cm] (p) at (9.6,6.8) {\textbf{\textcolor{dblue}{MoLIC do professor}}\\[34pt] \phantom{x}};
\node[c, draw=dblue, text width=5.2cm, minimum height=2.8cm] (a) at (9.6,3.0) {\textbf{\textcolor{dblue}{MoLIC do aluno}}\\[34pt] \phantom{x}};
""" + _mini(9.6, 6.2, "dblue") + _mini(9.6, 2.4, "dblue") + r"""
\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (mo.east) -- (p.west);
\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (mo.east) -- (a.west);
\node[c, draw=dorange, text width=4.4cm, minimum height=2.8cm] (e1) at (16.4,6.8) {\textbf{\textcolor{dorange}{1. Tópicos}}\\ tópicos e mudanças de tópico: cenas e falas de transição};
\node[c, draw=dorange, text width=4.4cm, minimum height=2.8cm] (e2) at (16.4,3.0) {\textbf{\textcolor{dorange}{2. Detalhes}}\\ diálogos, falas e signos de cada cena};
\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (e1.south) -- (e2.north);
\node[font=\large\bfseries, black!70, anchor=west] at (0.0,0.6) {o designer reflete sobre:};
\node[c, draw=dred, fill=dred!6, text width=2.2cm, minimum height=0.9cm] at (7.6,0.6) {rupturas};
\node[c, draw=dred, fill=dred!6, text width=4.0cm, minimum height=0.9cm] at (11.9,0.6) {conversas alternativas};
\node[c, draw=dred, fill=dred!6, text width=4.4cm, minimum height=0.9cm] at (16.8,0.6) {relações entre objetivos};
""")

# ------------------------------------------------------------------ três "cadastros" no mesmo diagrama
w("molic-tres-cadastros", r"""
\tikzset{s/.style={dbox, draw=dblue, rounded corners=9pt, line width=1.6pt, minimum width=4.6cm, minimum height=1.2cm, font=\large},
        r/.style={dbox, draw=black!55, dashed, rounded corners=9pt, line width=1.5pt, minimum width=4.6cm, minimum height=1.2cm, font=\large},
        a/.style={dtrans, line width=1.8pt, -{Stealth[length=3mm]}},
        l/.style={font=\normalsize, fill=dcream, inner sep=1.5pt}}
\node[font=\Large\bfseries, black!75] at (3.2,9.6) {Postar aviso};
\node[font=\Large\bfseries, black!75] at (9.8,9.6) {Cadastrar material};
\node[font=\Large\bfseries, black!75] at (16.4,9.6) {Cadastrar atividade};
% 1
\node[s] (a1) at (3.2,8.0) {Postar aviso};
\node[s] (b1) at (3.2,5.2) {Cena anterior};
\draw[a] (a1.south) -- node[l, align=center] {d: aviso postado} (b1.north);
% 2
\node[s] (a2) at (9.8,8.0) {Cadastrar material};
\node[s] (c2) at (9.8,5.2) {Confirmar cadastramento};
\node[r] (b2) at (9.8,2.4) {material cadastrado};
\draw[a] (a2.south) -- node[l] {u: cadastrar} (c2.north);
\draw[a] (c2.south) -- node[l] {u: confirmar} (b2.north);
% 3
\node[s] (a3) at (16.4,8.0) {Cadastrar atividade};
\node[s] (b3) at (16.4,5.2) {Examinar atividade};
\node[s] (c3) at (16.4,2.4) {Alterar atividade};
\draw[a] (a3.south) -- node[l, align=center] {d: atividade cadastrada} (b3.north);
\draw[a] (b3.south) -- node[l] {u: alterar} (c3.north);
\node[font=\large, text width=5.8cm, align=center] at (3.2,0.5) {\textbf{grava direto}, sem confirmar};
\node[font=\large, text width=5.8cm, align=center] at (9.8,0.5) {\textbf{pede confirmação} antes de gravar};
\node[font=\large, text width=5.8cm, align=center] at (16.4,0.5) {\textbf{grava} e leva a \textbf{conferir}; dali dá para \textbf{alterar}};
""")

# ------------------------------------------------------------------ tabela de expressões dos signos
_X = [0, 4.8, 8.2, 18.6]
_R = [
 ("+ título", [("d+u", "caixa de texto", "caixa"), ("d", "rótulo", "rotulo")]),
 ("descrição", [("d+u", "caixa de texto com ferramentas de formatação", "formata"), ("d", "rótulo com várias linhas", "multi")]),
 ("data de entrega", [("d+u", "controle de calendário", "calend"), ("d", r"rótulo dd/mm/aaaa (nos avisos, + calendário)", "data")]),
 ("número máximo de alunos", [("d+u", "caixa de texto com botões de incremento e decremento", "incr"), ("d", "rótulo", "rotulo")]),
]
def _ico(k, x, y):
    o = []
    if k == "caixa":
        o.append(r"\draw[black!60, fill=white, line width=1pt] (%s,%s) rectangle (%s,%s);" % (x - 0.8, y - 0.24, x + 0.8, y + 0.24))
        o.append(r"\draw[black!70, line width=1pt] (%s,%s) -- (%s,%s);" % (x - 0.6, y - 0.14, x - 0.6, y + 0.14))
    elif k == "rotulo":
        o.append(r"\node[font=\footnotesize] at (%s,%s) {Texto};" % (x, y))
    elif k == "formata":
        o.append(r"\draw[black!60, fill=white, line width=1pt] (%s,%s) rectangle (%s,%s);" % (x - 0.8, y - 0.28, x + 0.8, y + 0.28))
        o.append(r"\fill[dshade!70] (%s,%s) rectangle (%s,%s);" % (x - 0.8, y + 0.08, x + 0.8, y + 0.28))
        o.append(r"\node[font=\tiny\bfseries] at (%s,%s) {B};\node[font=\tiny\itshape] at (%s,%s) {I};\node[font=\tiny] at (%s,%s) {\underline{U}};" % (x - 0.6, y + 0.18, x - 0.35, y + 0.18, x - 0.1, y + 0.18))
        o.append(r"\draw[black!50, line width=0.9pt] (%s,%s) -- (%s,%s);" % (x - 0.6, y - 0.08, x + 0.2, y - 0.08))
    elif k == "multi":
        for j, wd in enumerate((1.5, 1.5, 0.9)):
            o.append(r"\draw[black!50, line width=1.2pt] (%s,%s) -- (%s,%s);" % (x - 0.75, y + 0.2 - j * 0.2, x - 0.75 + wd, y + 0.2 - j * 0.2))
    elif k == "calend":
        o.append(r"\fill[dblue] (%s,%s) rectangle (%s,%s);" % (x - 0.5, y + 0.14, x + 0.5, y + 0.3))
        o.append(r"\draw[black!55, line width=0.8pt, fill=white] (%s,%s) rectangle (%s,%s);" % (x - 0.5, y - 0.3, x + 0.5, y + 0.14))
        o.append(r"\draw[black!35, step=0.2, line width=0.5pt] (%s,%s) grid (%s,%s);" % (x - 0.5, y - 0.3, x + 0.5, y + 0.14))
        o.append(r"\fill[dorange!70] (%s,%s) rectangle (%s,%s);" % (x + 0.1, y - 0.1, x + 0.3, y + 0.1))
    elif k == "data":
        o.append(r"\node[font=\footnotesize] at (%s,%s) {26/05/2026};" % (x, y))
    elif k == "incr":
        o.append(r"\draw[black!60, fill=white, line width=1pt] (%s,%s) rectangle (%s,%s);" % (x - 0.8, y - 0.24, x + 0.35, y + 0.24))
        o.append(r"\node[font=\scriptsize] at (%s,%s) {3};" % (x - 0.55, y))
        o.append(r"\draw[black!60, fill=dshade!60, line width=1pt] (%s,%s) rectangle (%s,%s);" % (x + 0.35, y, x + 0.8, y + 0.24))
        o.append(r"\draw[black!60, fill=dshade!60, line width=1pt] (%s,%s) rectangle (%s,%s);" % (x + 0.35, y - 0.24, x + 0.8, y))
        o.append(r"\node[font=\tiny] at (%s,%s) {+};\node[font=\tiny] at (%s,%s) {$-$};" % (x + 0.575, y + 0.12, x + 0.575, y - 0.12))
    return "\n".join(o)
_o = [r"\node[dbox, draw=dblue, fill=dblue!12, line width=1.6pt, minimum width=18.6cm, minimum height=0.9cm, font=\large\bfseries, anchor=south west, rounded corners=3pt] at (0,8.75) {Enunciado de trabalho (E)};"]
def _cel(j, ytop, h, txt, fill="white", bold=False, col="black", fonte=r"\normalsize"):
    x0, x1 = _X[j], _X[j + 1]
    o = [r"\draw[black!60, fill=%s, line width=1pt] (%s,%s) rectangle (%s,%s);" % (fill, x0, ytop - h, x1, ytop)]
    f = fonte + (r"\bfseries" if bold else "")
    o.append(r"\node[font=%s, text=%s, text width=%scm, align=center] at (%s,%s) {%s};" % (f, col, round(x1 - x0 - 0.3, 2), round((x0 + x1) / 2, 2), round(ytop - h / 2, 2), txt))
    return "\n".join(o)
def _cel_expr(ytop, h, txt, ico):
    x0, x1 = _X[2], _X[3]
    yc = round(ytop - h / 2, 2)
    o = [r"\draw[black!60, fill=white, line width=1pt] (%s,%s) rectangle (%s,%s);" % (x0, ytop - h, x1, ytop)]
    o.append(r"\draw[black!25, line width=0.8pt] (%s,%s) -- (%s,%s);" % (x0 + 2.3, ytop - h + 0.1, x0 + 2.3, ytop - 0.1))
    o.append(_ico(ico, round(x0 + 1.15, 2), yc))
    o.append(r"\node[font=\normalsize, anchor=west, text width=7.9cm, align=left] at (%s,%s) {%s};" % (x0 + 2.5, yc, txt))
    return "\n".join(o)
_o.append(_cel(0, 8.75, 0.8, "signo", fill="dshade!55", bold=True))
_o.append(_cel(1, 8.75, 0.8, "emissor", fill="dshade!55", bold=True))
_o.append(_cel(2, 8.75, 0.8, "expressão", fill="dshade!55", bold=True))
_y = 7.95
for nome, linhas in _R:
    _o.append(_cel(0, _y, 1.6, nome, bold=nome.startswith("+"), col="dblue" if nome.startswith("+") else "black"))
    for k, (em, ex, ic) in enumerate(linhas):
        ent = em == "d+u"
        _o.append(_cel(1, _y - 0.8 * k, 0.8, r"%s: %s" % (r"\textbf{d+u}" if ent else r"\textbf{d}", "entrada" if ent else "saída"), fill="dgreen!10" if ent else "dblue!8", col="dgreen" if ent else "dblue"))
        _o.append(_cel_expr(_y - 0.8 * k, 0.8, ex, ic))
    _y -= 1.6
_o.append(r"\node[font=\large, black!75, text width=18.6cm, align=center] at (9.3,0.7) {\textbf{d+u}: designer e usuário falam, expressão de \textbf{entrada} $\cdot$ \textbf{d}: só o designer fala, expressão de \textbf{saída}};")
w("expressao-signos", "\n".join(_o))

# ------------------------------------------------------------------ sistema de ajuda: acesso
w("ajuda-acesso", r"""
\tikzset{ch/.style={dbox, draw=dorange, fill=dorange!8, rounded corners=9pt, line width=1.5pt, text width=3.8cm, minimum height=1.0cm, font=\large},
        ly/.style={dbox, line width=1.6pt, text width=4.3cm, minimum height=1.55cm, font=\large},
        ar/.style={-{Stealth[length=3mm]}, dorange, line width=1.8pt}}
% tela
\draw[black!60, fill=white, line width=1.5pt, rounded corners=4pt] (0,1.8) rectangle (7.4,8.3);
\fill[dblue, rounded corners=0pt] (0,7.5) rectangle (7.4,8.3); \node[font=\large\bfseries, white] at (3.7,7.9) {Cadastrar trabalho};
\node[font=\normalsize, anchor=west] at (0.35,6.5) {Título};
\draw[black!60, fill=white, line width=1pt] (2.0,6.2) rectangle (6.6,6.8);
\node[font=\normalsize, anchor=west] at (0.35,5.2) {Peso};
\draw[black!60, fill=white, line width=1pt] (2.0,4.9) rectangle (5.6,5.5);
\node[font=\normalsize, anchor=west] at (0.35,3.9) {Data};
\draw[black!60, fill=white, line width=1pt] (2.0,3.6) rectangle (6.6,4.2);
\draw[dblue, fill=dblue!15, rounded corners=3pt, line width=1.2pt] (5.2,2.1) rectangle (6.9,2.7); \node[font=\normalsize] at (6.05,2.4) {Gravar};
\node[circle, draw=dorange, fill=dorange!20, line width=1.6pt, font=\large\bfseries, minimum size=0.75cm, inner sep=0pt] (q) at (6.3,5.2) {?};
% perguntas
\node[ch] (c1) at (11.2,6.9) {O que é isto?};
\node[ch] (c2) at (11.2,5.2) {Para que serve isto?};
\node[ch] (c3) at (11.2,3.5) {Como faço isto?};
\draw[ar] (q.east) -- (c1.west); \draw[ar] (q.east) -- (c2.west); \draw[ar] (q.east) -- (c3.west);
% camadas
\node[ly, draw=dgreen, fill=dgreen!8] (l1) at (16.9,6.9) {\textbf{\textcolor{dgreen}{1. Resposta curta}}\\ ``peso do trabalho na nota''};
\node[ly, draw=dblue, fill=dblue!8] (l2) at (16.9,4.7) {\textbf{\textcolor{dblue}{2. Explicação}}\\ como o peso entra na média};
\node[ly, draw=dred, fill=dred!6] (l3) at (16.9,2.5) {\textbf{\textcolor{dred}{3. Detalhes}}\\ passo a passo e manual};
\draw[ar] (c2.east) -- (l1.west);
\draw[-{Stealth[length=3mm]}, black!55, line width=1.6pt] (l1.south) -- (l2.north);
\draw[-{Stealth[length=3mm]}, black!55, line width=1.6pt] (l2.south) -- (l3.north);
\node[font=\large\bfseries, text width=6cm, align=center] at (3.7,0.7) {contextual:\\ ao lado do elemento};
\node[font=\large\bfseries, text width=6cm, align=center] at (11.2,0.7) {sob demanda:\\ o usuário pergunta};
\node[font=\large\bfseries, text width=6cm, align=center] at (16.9,0.7) {em camadas:\\ do resumo ao detalhe};
""")
