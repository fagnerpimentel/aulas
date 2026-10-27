CAB = r"""\documentclass[border=3pt]{standalone}
\input{preamble}
\begin{document}
\hyphenpenalty=10000 \exhyphenpenalty=10000 \tolerance=9999 \emergencystretch=3em
\begin{tikzpicture}[x=1cm,y=1cm]
"""
RODA = "\n\\end{tikzpicture}\n\\end{document}\n"
def w(n, body): open(n + ".tex", "w").write(CAB + body.strip("\n") + RODA)


CS = ["dblue", "dgreen", "dorange", "dred"]

def boxes(items, w=3.9, h=3.0, cols=4, cap=None, capw=17, font=r"\large"):
    st = 0.6 + w
    o = [r"\tikzset{c/.style={dbox, text width=%scm, minimum height=%scm, font=%s, line width=1.4pt}}" % (w, h, font)]
    n = len(items)
    rows = (n + cols - 1) // cols
    for i, (t, x) in enumerate(items):
        r, c = divmod(i, cols)
        col = CS[i % 4]
        o.append(r"\node[c, draw=%s] at (%s,%s) {\textbf{\textcolor{%s}{%s}}\\ %s};" % (col, round(c * st, 2), round(-r * (h + 0.5), 2), col, t, x))
    if cap:
        used = min(n, cols)
        o.append(r"\node[font=\Large, black!70, text width=%scm, align=center] at (%s,%s) {%s};" % (capw, round((used - 1) * st / 2, 2), round(-(rows - 1) * (h + 0.5) - h / 2 - 1.0, 2), cap))
    return "\n".join(o)

def flow(items, w=3.5, h=3.0, cap=None, capw=17, font=r"\large"):
    st = 0.6 + w
    o = [r"\tikzset{c/.style={dbox, text width=%scm, minimum height=%scm, font=%s, line width=1.4pt}}" % (w, h, font)]
    for i, (t, x) in enumerate(items):
        col = CS[i % 4]
        o.append(r"\node[c, draw=%s] (n%d) at (%s,0) {\textbf{\textcolor{%s}{%d. %s}}\\ %s};" % (col, i, round(i * (st + 0.2), 2), col, i + 1, t, x))
    for i in range(len(items) - 1):
        o.append(r"\draw[dtrans, line width=2pt, -{Stealth[length=3mm]}] (n%d.east) -- (n%d.west);" % (i, i + 1))
    if cap:
        o.append(r"\node[font=\Large, black!70, text width=%scm, align=center] at (%s,%s) {%s};" % (capw, round((len(items) - 1) * (st + 0.2) / 2, 2), round(-h / 2 - 1.0, 2), cap))
    return "\n".join(o)
w("espaco-de-problema", flow([("Dados coletados", "entrevistas, questionários, campo"), ("Perfil de usuário", "quem são e quantos"), ("Personas", "arquétipos com objetivos"), ("Cenários", "histórias de uso"), ("Tarefas", "como os objetivos são atingidos")], w=3.3, h=3.4, cap="cada representação \\textbf{organiza} e \\textbf{refina} o que foi aprendido"))

w("perfil-grupos", boxes([("Idade", "criança, jovem, adulto, terceira idade"), ("Experiência", "novato ou especialista"), ("Atitude", "tecnófilo ou tecnófobo"), ("Tarefa principal", "comprar, vender, ensinar")], cap="agrupe usuários \\textbf{semelhantes}; calcule a \\textbf{proporção} de cada perfil"))

w("perfil-quadro", r"""
  \tikzset{h/.style={font=\large\bfseries, minimum height=0.9cm, minimum width=3.4cm, align=center}, v/.style={font=\large, minimum height=0.9cm, minimum width=3.4cm, align=center}, l/.style={font=\large, anchor=east}}
  \node[h, text=dblue] at (6.0,5.6) {Perfil A};
  \node[h, text=dorange] at (9.6,5.6) {Perfil B};
  \draw[line width=1.2pt] (-0.4,5.1) -- (11.4,5.1);
  \node[l] at (3.9,4.5) {professores no perfil};  \node[v] at (6.0,4.5) {47\%}; \node[v] at (9.6,4.5) {43\%};
  \node[l] at (3.9,3.5) {faixa etária};  \node[v] at (6.0,3.5) {30 a 40}; \node[v] at (9.6,3.5) {40 a 50};
  \node[l] at (3.9,2.5) {atitude perante tecnologia};  \node[v] at (6.0,2.5) {alta}; \node[v] at (9.6,2.5) {média};
  \node[l] at (3.9,1.5) {estilo de aprendizado};  \node[v] at (6.4,1.5) {aprende fazendo}; \node[v] at (9.9,1.5) {lê o manual};
  \node[font=\large, black!70, text width=11cm, align=center] at (5.5,0.2) {valores fictícios; 10\% dos usuários podem não caber em nenhum perfil};
""")

w("persona-elementos", boxes([("Identidade", "nome, idade e foto"), ("Status", "primária, secundária ou antiusuário"), ("Objetivos", "dentro e fora do produto"), ("Habilidades", "formação e competências"), ("Tarefas", "frequência, importância e duração"), ("Relações", "com quem interage"), ("Requisitos", "do que precisa; uma citação"), ("Expectativas", "como acha que funciona")], h=2.6, cap="quanto mais \\textbf{específica}, mais útil a persona"))

w("usuario-elastico", r"""
  \tikzset{c/.style={dbox, text width=7.8cm, minimum height=4.4cm, font=\large, line width=1.5pt, align=left}}
  \node[c, draw=dred] at (0,0) {\textbf{\Large\textcolor{dred}{``O usuário''}}\\[4pt] vago e \textbf{elástico}\\ ora novato, ora especialista\\ cada designer imagina um};
  \node[c, draw=dgreen] at (8.9,0) {\textbf{\Large\textcolor{dgreen}{A persona}}\\[4pt] uma pessoa \textbf{concreta}\\ objetivos, habilidades e contexto\\ todos projetam para o mesmo alvo};
""")

w("tres-objetivos", r"""
  \tikzset{c/.style={dbox, text width=5.6cm, minimum height=4.4cm, font=\large, line width=1.5pt, align=left}}
  \node[c, draw=dblue] at (0,0) {\textbf{\Large\textcolor{dblue}{Pessoais}}\\[4pt] não se sentir estúpido\\ não errar\\ divertir-se ou não se entediar};
  \node[c, draw=dgreen] at (6.8,0) {\textbf{\Large\textcolor{dgreen}{Práticos}}\\[4pt] fazem a \textbf{ponte}\\ ex.: processar pedidos do cliente};
  \node[c, draw=dorange] at (13.6,0) {\textbf{\Large\textcolor{dorange}{Corporativos}}\\[4pt] lucro e mercado\\ mantêm o foco no quadro maior};
  \node[font=\Large, black!70, text width=18cm, align=center] at (6.8,-3.5) {os objetivos \textbf{pessoais} vêm primeiro e nunca devem ser violados};
""")

w("objetivos-tres-niveis", r"""
  \tikzset{c/.style={dbox, text width=5.6cm, minimum height=4.6cm, font=\large, line width=1.5pt, align=left}}
  \node[c, draw=dblue] at (0,0) {\textbf{\Large\textcolor{dblue}{De experiência}}\\[4pt] como quer \textbf{se sentir}\\ no controle, relaxado, focado\\ nível \textbf{visceral}};
  \node[c, draw=dgreen] at (6.8,0) {\textbf{\Large\textcolor{dgreen}{Finais}}\\[4pt] o que quer \textbf{fazer}\\ ex.: concluir a lista do dia\\ nível \textbf{comportamental}};
  \node[c, draw=dorange] at (13.6,0) {\textbf{\Large\textcolor{dorange}{De vida}}\\[4pt] quem quer \textbf{ser}\\ ex.: tornar-se especialista\\ nível \textbf{reflexivo}};
""")

w("objetivo-vs-tarefa", r"""
  \tikzset{c/.style={dbox, text width=7.8cm, minimum height=4.0cm, font=\large, line width=1.5pt, align=left}}
  \node[c, draw=dgreen] at (0,0) {\textbf{\Large\textcolor{dgreen}{Objetivo}}\\[4pt] uma condição \textbf{final}\\ bem estável no tempo\\ ex.: falar com a família};
  \node[c, draw=dorange] at (8.9,0) {\textbf{\Large\textcolor{dorange}{Tarefa}}\\[4pt] processo \textbf{intermediário}\\ muda com a tecnologia\\ ex.: escrever uma carta};
  \node[font=\Large, black!70, text width=17cm, align=center] at (4.45,-3.2) {projetar a partir dos \textbf{objetivos}, e não só das tarefas};
""")

w("falso-objetivo", r"""
  \tikzset{c/.style={dbox, text width=4.0cm, minimum height=2.4cm, font=\large, line width=1.5pt}}
  \node[c, draw=dred] (a) at (0,0) {\textbf{Falso objetivo}\\ ``rodar no navegador''};
  \node[c, draw=dorange] (b) at (5.4,0) {\textbf{Por quê?}\\ ``para acessar de qualquer lugar''};
  \node[c, draw=dgreen] (c) at (10.8,0) {\textbf{Objetivo verdadeiro}\\ acesso em qualquer lugar};
  \draw[dtrans, line width=2pt, -{Stealth[length=3mm]}] (a.east) -- (b.west);
  \draw[dtrans, line width=2pt, -{Stealth[length=3mm]}] (b.east) -- (c.west);
  \node[font=\Large, black!70, text width=14cm, align=center] at (5.4,-2.3) {pergunte ``por quê?'' até chegar a um \textbf{fim}, e não a um meio};
""")

w("cenario-elementos", boxes([("Ambiente", "contexto e situação"), ("Atores", "pessoas e suas características"), ("Objetivos", "o que motiva as ações"), ("Planejamento", "o que pensam antes de agir"), ("Ações", "comportamento observável"), ("Eventos", "reações do sistema e do ambiente"), ("Avaliação", "como interpretam o que ocorre"), ("Título", "descreve a situação em poucas palavras")], h=2.6, cap="um cenário é uma \\textbf{história} concreta, com ator e objetivo principais"))

w("cenarios-cobertura", boxes([("Ciclo de vida", "cada passo de um processo longo"), ("Públicos", "tipos de usuário"), ("Funções", "o que o produto faz"), ("Variantes", "formas de fazer uma tarefa"), ("Métodos", "diferentes caminhos para a mesma tarefa")], cols=5, w=3.2, h=3.2, font=r"\large", cap="Cooper: o \\textbf{conjunto} de cenários deve cobrir estes cinco pontos", capw=18))

w("questionamento", boxes([("Por quê?", "condições e consequências"), ("Como?", "sequência de ações detalhada"), ("O que é?", "objetos e atributos"), ("X pode ser feito de Y?", "verificação: sim ou não")], cap="divida o cenário em frases e \\textbf{pergunte} sobre cada uma"))

w("cenarios-frequencia", r"""
  \tikzset{c/.style={dbox, text width=7.8cm, minimum height=4.6cm, font=\large, line width=1.5pt, align=left}}
  \node[c, draw=dgreen] at (0,0) {\textbf{\Large\textcolor{dgreen}{Uso diário}}\\[4pt] poucas ações, muito frequentes\\ instruções \textbf{no ponto de uso}\\ atalhos e personalização};
  \node[c, draw=dorange] at (8.9,0) {\textbf{\Large\textcolor{dorange}{Uso periódico}}\\[4pt] ex.: relatório anual\\ instruções claras embutidas\\ dispensa atalhos};
  \node[font=\Large, black!70, text width=17cm, align=center] at (4.45,-3.4) {comece pelos cenários do \textbf{uso diário}; o resto vem se houver tempo};
""")

w("hta-elementos", r"""
  \tikzset{o/.style={dbox, draw=dblue, line width=1.5pt, minimum width=3.6cm, minimum height=1.4cm, font=\large}}
  \node[o] (g) at (0,3.2) {Objetivo};
  \node[o, rounded corners=14pt] (p) at (5.0,3.2) {Operação};
  \node[font=\large, black!70] at (0,1.9) {o que se quer};
  \node[font=\large, black!70] at (5.0,1.9) {ação no nível mais baixo};
  \node[font=\Large\bfseries, dblue] at (11.2,4.6) {planos};
  \node[o, minimum width=2.8cm] at (9.3,3.0) {1 > 2};
  \node[o, minimum width=2.8cm] at (12.4,3.0) {1 / 2};
  \node[o, minimum width=2.8cm] at (15.5,3.0) {1 + 2};
  \node[font=\large] at (9.3,1.9) {sequência};
  \node[font=\large] at (12.4,1.9) {seleção};
  \node[font=\large] at (15.5,1.9) {paralelo};
  \node[font=\large, black!70, text width=17cm, align=center] at (7.7,0.3) {um \textbf{plano} diz em que ordem os subobjetivos levam ao objetivo maior};
""")

w("hta-exemplo", r"""
  \tikzset{n/.style={dbox, draw=dblue, line width=1.4pt, minimum width=4.4cm, minimum height=1.5cm, font=\large}, pl/.style={font=\large\bfseries, dorange, fill=white, inner sep=2pt}}
  \node[n] (r) at (8.0,7.0) {0. Entregar trabalho};
  \node[n] (a) at (2.6,3.9) {1. Preparar arquivo};
  \node[n] (b) at (13.4,3.9) {2. Enviar no sistema};
  \node[n] (a1) at (0.0,0.6) {1.1 Exportar PDF};
  \node[n] (a2) at (5.2,0.6) {1.2 Compactar};
  \node[n] (b1) at (10.8,0.6) {2.1 Escolher turma};
  \node[n] (b2) at (16.0,0.6) {2.2 Anexar e enviar};
  \draw[line width=1.2pt] (r.south) -- (a.north);
  \draw[line width=1.2pt] (r.south) -- (b.north);
  \draw[line width=1.2pt] (a.south) -- (a1.north);
  \draw[line width=1.2pt] (a.south) -- (a2.north);
  \draw[line width=1.2pt] (b.south) -- (b1.north);
  \draw[line width=1.2pt] (b.south) -- (b2.north);
  \node[pl] at (8.0,5.0) {plano 1 > 2};
  \node[pl] at (2.6,2.2) {1 / 2};
  \node[pl] at (13.4,2.2) {1 > 2};
""")

w("hta-passos", flow([("Objetivos", "da análise"), ("Consenso", "medidas de sucesso"), ("Fontes", "como obter dados"), ("Decompor", "diagrama e tabela"), ("Validar", "com as partes interessadas")], w=3.3, h=3.2, cap="depois: operações críticas e hipóteses sobre o desempenho", capw=18))

w("criterio-pxc", r"""
  \tikzset{c/.style={dbox, text width=4.6cm, minimum height=2.8cm, font=\Large, line width=1.5pt}}
  \node[c, draw=dblue] (p) at (0,0) {\textbf{p}\\ probabilidade de falha};
  \node[font=\Huge] at (3.0,0) {$\times$};
  \node[c, draw=dorange] (c) at (6.0,0) {\textbf{c}\\ custo da falha};
  \node[font=\Huge] at (9.0,0) {$=$};
  \node[c, draw=dgreen] at (12.2,0) {\textbf{risco}\\ aceitável? pare de decompor};
  \node[font=\Large, black!70, text width=16cm, align=center] at (6.0,-2.6) {outra razão para parar: o problema já foi \textbf{identificado}};
""")

w("goms-elementos", boxes([("Goals", "objetivos: o que o usuário quer"), ("Operators", "ações: clicar, digitar, olhar"), ("Methods", "sequências conhecidas de ações"), ("Selection rules", "qual método usar em cada situação")], cap="serve para usuários que \\textbf{já dominam} a tarefa"))

w("familia-goms", boxes([("KLM", "tempos de teclas, cliques e preparação"), ("CMN-GOMS", "hierarquia de objetivos em forma de programa"), ("CPM-GOMS", "operações em \\textbf{paralelo}; caminho crítico")], w=5.2, h=3.4, cols=3, cap="do mais simples ao mais detalhado"))

w("klm-operadores", boxes([("K", "tecla: 0,12 a 0,28 s"), ("P", "apontar com o mouse: 1,10 s"), ("B", "botão do mouse: 0,10 s"), ("H", "mão do teclado ao mouse: 0,40 s"), ("M", "preparação mental: 1,20 s")], cols=5, w=3.2, h=3.0, cap="tempos médios; some os operadores para estimar a duração", capw=18))

w("klm-exemplo", r"""
  \draw[daxis, line width=1.4pt] (0,0) -- (14,0);
  \foreach \y/\t/\v/\c in {3.6/{Menu Arquivo > Salvar}/4.6/dred, 2.1/{Botão da barra}/3.1/dorange, 0.6/{Atalho Ctrl+S}/1.6/dgreen} {
    \node[font=\Large, anchor=east] at (-0.3,\y) {\t};
    \fill[\c!75] (0,\y-0.5) rectangle (\v*2.4,\y+0.5);
    \node[font=\Large\bfseries, \c, anchor=west] at (\v*2.4+0.3,\y) {\v\ s};
  }
  \node[font=\large, black!70, text width=13cm, align=center] at (6.5,-1.0) {a mesma tarefa em três métodos; estimativa pelo KLM};
""")

w("ctt-tipos", boxes([("Usuário", "realizada fora do sistema"), ("Sistema", "processamento sem interação"), ("Interativa", "diálogo usuário e sistema"), ("Abstrata", "agrupa outras tarefas")], cap="quatro tipos de tarefa no \\textbf{CTT}"))

w("ctt-relacoes", boxes([(">>", "ativação: T2 só depois de T1"), ("[]", "escolha: uma ou outra"), ("|||", "concorrência: qualquer ordem"), ("[>", "desativação: T2 interrompe T1"), ("|>", "suspensão e retomada"), ("|[]|", "concorrentes e comunicantes"), ("|=|", "independentes: uma por vez"), ("[]>>", "ativação com passagem de dados")], h=2.6, font=r"\Large", cap="operadores que ligam as tarefas no \\textbf{CTT}"))

w("ctt-exemplo", r"""
  \tikzset{n/.style={dbox, draw=dblue, line width=1.4pt, minimum width=3.9cm, minimum height=1.5cm, font=\large}, op/.style={font=\Large\bfseries, dorange, fill=white, inner sep=1pt}}
  \node[n, rounded corners=14pt] (r) at (6.0,6.2) {Pedir comida};
  \node[n, rounded corners=14pt] (a) at (0.6,3.2) {Ver o cardápio};
  \node[n] (b) at (6.0,3.2) {Montar o pedido};
  \node[n] (c) at (11.4,3.2) {Confirmar};
  \node[op] at (3.3,4.9) {>>}; \node[op] at (8.7,4.9) {>>};
  \node[n] (b1) at (3.3,0.4) {Escolher prato};
  \node[n] (b2) at (8.7,0.4) {Informar endereço};
  \node[op] at (6.0,1.8) {|||};
  \draw[line width=1.2pt] (r.south) -- (a.north);
  \draw[line width=1.2pt] (r.south) -- (b.north);
  \draw[line width=1.2pt] (r.south) -- (c.north);
  \draw[line width=1.2pt] (b.south) -- (b1.north);
  \draw[line width=1.2pt] (b.south) -- (b2.north);
""")

w("comparar-modelos", boxes([("HTA", "objetivos e subobjetivos; \\textbf{por que} e consequência"), ("GOMS", "usuário experiente; \\textbf{tempo} de execução"), ("CTT", "tarefas do usuário e do sistema; \\textbf{ordem} e interação")], w=5.2, h=3.6, cols=3, cap="modelos diferentes para perguntas diferentes"))

w("persona-conceito", r"""
  % usuarios reais: bonequinhos variados
  \foreach \x/\y/\c in {0.0/5.4/dblue, 1.5/5.9/dorange, 3.0/5.4/dgreen, 0.7/3.6/dred, 2.3/3.9/dblue, 0.0/1.8/dgreen, 1.6/2.1/dred, 3.0/1.8/dorange} {
    \draw[\c, fill=\c!20, line width=1.4pt] (\x,\y+0.55) circle (0.28);
    \draw[\c, fill=\c!20, line width=1.4pt, rounded corners=3pt] (\x-0.38,\y-0.45) rectangle (\x+0.38,\y+0.2);
  }
  \node[font=\Large\bfseries, dblue] at (1.5,0.5) {usuários reais};
  \draw[dtrans, line width=2.4pt, -{Stealth[length=4mm]}] (4.1,3.6) -- (6.4,3.6);
  \node[font=\large, black!70, text width=2.4cm, align=center] at (5.25,4.7) {pesquisa e perfis};
  % cartao de persona
  \draw[dblue, fill=dcream, line width=2pt, rounded corners=6pt] (6.6,0.6) rectangle (12.4,6.9);
  \draw[dblue, fill=dblue!20, line width=1.8pt] (8.0,5.7) circle (0.7);
  \draw[dblue, fill=dblue!35, line width=1.4pt] (8.0,5.95) circle (0.22);
  \draw[dblue, line width=1.6pt] (7.55,5.35) .. controls (7.8,5.05) and (8.2,5.05) .. (8.45,5.35);
  \node[font=\Large\bfseries, dblue, anchor=west] at (9.0,6.05) {Rita Alves};
  \node[font=\large, anchor=west] at (9.0,5.45) {aluna · 21 anos};
  \node[font=\large\itshape, black!75, text width=5.2cm, align=center] at (9.5,4.4) {``quero entregar tudo sem correria''};
  \node[font=\large\bfseries, dorange, anchor=west] at (7.0,3.3) {objetivos};
  \node[font=\large, anchor=west] at (7.0,2.7) {$\bullet$ não perder prazos};
  \node[font=\large, anchor=west] at (7.0,2.1) {$\bullet$ saber o que já entregou};
  \node[font=\large, anchor=west] at (7.0,1.5) {$\bullet$ não passar vergonha};
  \node[font=\Large\bfseries, dblue] at (9.5,-0.1) {a persona};
  \draw[dtrans, line width=2.4pt, -{Stealth[length=4mm]}] (12.6,3.6) -- (14.9,3.6);
  % equipe decide
  \tikzset{e/.style={dbox, text width=3.7cm, minimum height=1.2cm, font=\large, line width=1.4pt}}
  \node[e, draw=dgreen] at (17.0,5.8) {funcionalidades};
  \node[e, draw=dorange] at (17.0,4.0) {interface};
  \node[e, draw=dred] at (17.0,2.2) {conteúdo};
  \node[font=\Large\bfseries, dblue] at (17.0,0.5) {a equipe decide};
  \node[font=\Large, black!70, text width=9cm, align=center] at (10.0,-1.4) {todos projetam para o \textbf{mesmo alvo}};
""")

w("rita-avatar", r"""
  \definecolor{skin}{HTML}{E2AE86}
  \definecolor{hair}{HTML}{3F2A1E}
  \fill[dblue!15] (0,0) circle (3.0);
  \begin{scope}
    \clip (0,0) circle (3.0);
    % cabelo atras
    \fill[hair] (0,0.55) ellipse (1.55 and 1.75);
    \fill[hair] (-1.5,-0.7) rectangle (1.5,0.5);
    % ombros e blusa
    \fill[dblue] (0,-3.0) ellipse (2.7 and 2.1);
    \fill[skin] (-0.38,-1.35) rectangle (0.38,-0.55);
    \fill[white] (-0.55,-1.12) -- (0,-1.75) -- (0.55,-1.12) -- cycle;
    % rosto
    \fill[skin] (0,0.35) ellipse (1.12 and 1.38);
    % franja
    \fill[hair] (-1.15,0.85) .. controls (-0.7,1.9) and (0.9,1.95) .. (1.15,0.55) .. controls (0.55,1.15) and (-0.35,1.2) .. (-1.15,0.85) -- cycle;
    % olhos e sobrancelhas
    \fill[hair] (-0.43,0.38) circle (0.1); \fill[hair] (0.43,0.38) circle (0.1);
    \draw[hair, line width=1.6pt, line cap=round] (-0.7,0.68) .. controls (-0.5,0.78) and (-0.3,0.78) .. (-0.17,0.7);
    \draw[hair, line width=1.6pt, line cap=round] (0.7,0.68) .. controls (0.5,0.78) and (0.3,0.78) .. (0.17,0.7);
    % nariz e sorriso
    \draw[skin!60!hair, line width=1.3pt, line cap=round] (0,0.3) -- (-0.07,-0.02) -- (0.05,-0.04);
    \draw[dred, line width=2pt, line cap=round] (-0.42,-0.4) .. controls (-0.15,-0.68) and (0.15,-0.68) .. (0.42,-0.4);
  \end{scope}
  \draw[dblue, line width=2.4pt] (0,0) circle (3.0);
""")

w("cenario-problemas", r"""
  \tikzset{p/.style={dbox, draw=dblue, line width=1.5pt, text width=2.4cm, minimum height=2.4cm, font=\large}, r/.style={dbox, draw=dred, fill=dred!10, line width=1.5pt, font=\large\bfseries, text=dred, text width=2.6cm, minimum height=1.5cm}}
  \foreach \i/\t in {1/{23h50: termina o trabalho}, 2/{vê que só aceita PDF}, 3/{envia para o e-mail}, 4/{converte no PC do irmão}, 5/{tenta enviar de novo}, 6/{23h59: o prazo estoura}, 7/{pede desculpas ao professor}} {
    \node[p] (s\i) at (\i*3.0,0) {\t};
  }
  \foreach \i in {1,2,3,4,5,6} {
    \pgfmathtruncatemacro{\j}{\i+1}
    \draw[dtrans, line width=1.8pt, -{Stealth[length=2.6mm]}] (s\i.east) -- (s\j.west);
  }
  % problemas
  \node[r] (a) at (6.0,-3.4) {formato não aceito};
  \draw[dred, line width=1.6pt] (a.north) -- (s2.south);
  \draw[dred, line width=1.6pt] (8.0,-1.55) -- (8.0,-1.8) -- (13.0,-1.8) -- (13.0,-1.55);
  \draw[dred, line width=1.6pt] (10.5,-1.8) -- (10.5,-2.65);
  \node[r, text width=4.6cm] (b) at (10.5,-3.4) {sai do sistema para resolver};
  \node[r] (c) at (18.0,-3.4) {sem aviso de prazo};
  \draw[dred, line width=1.6pt] (c.north) -- (s6.south);
  \node[r, text width=2.6cm] (d) at (21.0,-3.4) {ajuda fora do sistema};
  \draw[dred, line width=1.6pt] (d.north) -- (s7.south);
  \node[font=\Large, black!70] at (12.0,-5.4) {cada passo problemático aponta para uma \textbf{oportunidade de design}};
""")

w("perguntas-elemento", r"""
  \tikzset{q/.style={dbox, text width=7.6cm, minimum height=2.5cm, font=\large, line width=1.5pt, align=left}}
  \node[q, draw=dblue] (o) at (-6.4,2.0) {\textbf{\textcolor{dblue}{Objetivo}}\\ por que o ator precisa dele?\\ que informações usa?};
  \node[q, draw=dgreen] (a) at (6.4,2.0) {\textbf{\textcolor{dgreen}{Ambiente}}\\ onde, quando e com que dispositivos?\\ há pressão de tempo?};
  \node[q, draw=dorange] (t) at (-6.4,-1.6) {\textbf{\textcolor{dorange}{Atores}}\\ o que os ajuda ou atrapalha?\\ de quem dependem?};
  \node[q, draw=dred] (p) at (6.4,-1.6) {\textbf{\textcolor{dred}{Planejamento}}\\ como fazem hoje?\\ como gostariam de fazer?};
  \node[circle, draw=dblue, fill=dblue!12, line width=2pt, minimum size=2.3cm, font=\Large\bfseries, text=dblue] (c) at (0,0.2) {cenário};
  \foreach \n in {o,a,t,p} {\draw[dtrans, line width=1.6pt, -{Stealth[length=2.6mm]}] (\n) -- (c);}
  \node[font=\Large, black!70, text width=20cm, align=center] at (0,-3.9) {numere as perguntas e marque no texto onde cada uma é respondida: \textbf{[1] [2] [3]}};
""")
