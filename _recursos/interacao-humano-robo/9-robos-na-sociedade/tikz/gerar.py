"""Gera os diagramas TikZ da aula 9 de IHR (Robôs na Sociedade). Uso: python3 gerar.py && bash build.sh"""
import math
exec(open("_helpers.py").read())

# ------------------------------------------------------------ 1. lacuna entre ficção e realidade
w("lacuna-expectativas", r"""
\fill[dorange!70] (1.6,1.0) rectangle (4.6,7.2);
\fill[dblue!75] (6.4,1.0) rectangle (9.4,2.6);
\node[font=\large\bfseries, dorange, text width=4.4cm, align=center] at (3.1,7.9) {expectativa\\ (ficção)};
\node[font=\large\bfseries, dblue, text width=4.4cm, align=center] at (7.9,3.5) {capacidade\\ real};
\draw[dred, line width=2.4pt, {Stealth[length=3.4mm]}-{Stealth[length=3.4mm]}] (11.0,2.7) -- (11.0,7.0);
\node[font=\Large\bfseries, dred, anchor=west] at (11.4,5.3) {lacuna};
\node[font=\large, dred, anchor=west, text width=4.6cm] at (11.4,4.3) {leva à \textbf{decepção} ao interagir com um robô de verdade};
\node[dbox, draw=black!50, fill=white, line width=1.4pt, text width=5.4cm, minimum height=1.5cm, font=\large] at (15.9,1.4) {o \textbf{primeiro contato} com robôs é, quase sempre, \textbf{na tela}};
""")

# ------------------------------------------------------------ 2. ficção e IA ao longo do tempo
w("ficcao-x-ia", r"""
\tikzset{n/.style={circle, fill=white, line width=2pt, minimum size=0.5cm, inner sep=0pt},
        t/.style={font=\large, text width=4.2cm, align=center}}
\node[font=\Large\bfseries, dorange, anchor=west] at (0.0,8.4) {na ficção};
\draw[dorange, line width=2.4pt, -{Stealth[length=3.4mm]}] (0.2,6.8) -- (18.9,6.8);
\foreach \x/\a/\b in {2.3/{folclore}/{\textbf{Golem}: ser artificial, há centenas de anos}, 6.9/{1921}/{\textbf{R.U.R.} (Čapek): nasce a palavra \emph{robô}}, 11.5/{Asimov}/{cria os termos \emph{robótica} e \emph{robopsicologia}}, 16.1/{pós-guerra}/{\textbf{Astro Boy} (Tezuka): o robô amigo}} {
  \node[n, draw=dorange] at (\x,6.8) {};
  \node[font=\large\bfseries, dorange] at (\x,7.6) {\a};
  \node[t] at (\x,5.6) {\b};
}
\node[font=\Large\bfseries, dblue, anchor=west] at (0.0,3.8) {na inteligência artificial};
\draw[dblue, line width=2.4pt, -{Stealth[length=3.4mm]}] (0.2,2.4) -- (18.9,2.4);
\foreach \x/\a/\b in {3.5/{1997}/{\textbf{Deep Blue} vence o campeão mundial de xadrez}, 9.5/{2011}/{\textbf{Watson} vence no \emph{Jeopardy}}, 15.5/{2017}/{\textbf{AlphaGo} vence o número 1 do Go}} {
  \node[n, draw=dblue] at (\x,2.4) {};
  \node[font=\large\bfseries, dblue] at (\x,3.2) {\a};
  \node[t] at (\x,1.2) {\b};
}
""")

# ------------------------------------------------------------ 3. quatro narrativas
w("quatro-narrativas", boxes([
  ("Querem ser humanos", r"\emph{Bicentennial Man}\\ \emph{Blade Runner}\\ \emph{A.I.}\\ \emph{Star Trek} (Mr. Data)"),
  ("Ameaça à humanidade", r"\emph{O Exterminador do Futuro}\\ \emph{Matrix}\\ \emph{Eu, Robô}\\ \emph{R.U.R.}"),
  ("Superiores e bons", r"R. Daneel Olivaw (Asimov)\\ \emph{Astro Boy}\\ \emph{Doraemon}"),
  ("Iguais ou diferentes?", r"Mr. Data\\ Johnny Five\\ \emph{Ex Machina}")],
  w=4.3, h=4.3, cols=4, cap=r"quatro arquétipos que \textbf{moldam} o que esperamos dos robôs", capw=18))

# ------------------------------------------------------------ 4. corpo x mente (tabela 12.1)
w("corpo-mente-2x2", r"""
\tikzset{c/.style={dbox, text width=5.2cm, minimum height=3.0cm, font=\large, line width=1.6pt}}
\node[font=\Large\bfseries, black!75] at (11.0,8.3) {mente};
\node[font=\large\bfseries, black!75] at (8.2,7.4) {semelhante};
\node[font=\large\bfseries, black!75] at (14.0,7.4) {diferente};
\node[font=\Large\bfseries, black!75, rotate=90] at (0.7,4.0) {corpo};
\node[font=\large\bfseries, black!75, anchor=east] at (2.4,5.4) {semelhante};
\node[font=\large\bfseries, black!75, anchor=east] at (2.4,2.1) {diferente};
\node[c, draw=dblue] at (8.2,5.4) {\textbf{\textcolor{dblue}{Tipo I}}\\ corpo e mente \textbf{iguais}\\ \emph{orquestra de robôs} (Raes)};
\node[c, draw=dgreen] at (14.0,5.4) {\textbf{\textcolor{dgreen}{Tipo II}}\\ corpo igual, mente \textbf{diferente}\\ Mr. Data, o androide David};
\node[c, draw=dorange] at (8.2,2.1) {\textbf{\textcolor{dorange}{Tipo III}}\\ corpo \textbf{diferente}, mente igual\\ Johnny Five};
\node[c, draw=dred] at (14.0,2.1) {\textbf{\textcolor{dred}{Tipo IV}}\\ corpo e mente \textbf{diferentes}};
""")

# ------------------------------------------------------------ 5. narrativas da mídia sobre ciência
w("narrativas-ciencia", r"""
\tikzset{c/.style={dbox, text width=8.6cm, minimum height=4.0cm, font=\large, line width=1.7pt}}
\node[c, draw=dred] at (4.7,5.2) {\textbf{\textcolor{dred}{História de alarme}}\\ \emph{science-scare}\\[6pt] ``\textbf{Quando os robôs vão dominar o mundo?}''\\ explora o medo e a fascinação};
\node[c, draw=dorange] at (14.7,5.2) {\textbf{\textcolor{dorange}{Ciência maluca}}\\ \emph{wacky science}\\[6pt] mais rara; \textbf{entretém} em vez de relatar o progresso científico};
\node[dbox, draw=black!50, dashed, fill=white, line width=1.6pt, text width=14cm, minimum height=1.7cm, font=\large] at (9.7,1.2) {manchete \textbf{improvável}: ``Robôs são inofensivos e quase inúteis'', mas é o que a maioria dos projetos de HRI mostra hoje};
""")

# ------------------------------------------------------------ 6. as três leis (e a lei zero)
leis = [
 ("0", "dred", r"Um robô não pode causar mal à \textbf{humanidade} nem, por omissão, permitir que ela sofra dano"),
 ("1", "dorange", r"Um robô não pode ferir um \textbf{ser humano} nem, por omissão, permitir que ele sofra dano"),
 ("2", "dgreen", r"Um robô deve \textbf{obedecer} às ordens dos humanos, exceto se conflitarem com a Primeira Lei"),
 ("3", "dblue", r"Um robô deve \textbf{proteger a própria existência}, desde que não conflite com a Primeira ou a Segunda Lei"),
]
_o = [r"\draw[black!55, line width=2.2pt, -{Stealth[length=3.4mm]}] (0.3,8.0) -- (0.3,0.5);",
      r"\node[font=\large\bfseries, rotate=90] at (-0.35,4.3) {prioridade};"]
for i, (n, c, t) in enumerate(leis):
    y = 7.3 - i * 2.05
    _o.append(r"\node[circle, draw=%s, fill=%s!15, line width=1.8pt, minimum size=1.1cm, font=\Large\bfseries] at (1.5,%s) {%s};" % (c, c, y, n))
    _o.append(r"\node[dbox, draw=%s, line width=1.7pt, text width=15.2cm, minimum height=1.5cm, font=\large, anchor=west] at (2.4,%s) {%s};" % (c, y, t))
w("tres-leis", "\n".join(_o))

# ------------------------------------------------------------ 7. mapa dos temas éticos
temas = [("Robôs na\\\\ pesquisa", "dblue"), ("Necessidades\\\\ emocionais", "dgreen"), ("Persuasão", "dorange"), ("Abuso de\\\\ robôs", "dred"),
         ("Trabalho", "dblue"), ("Atitudes\\\\ ambivalentes", "dgreen"), ("Diversidade\\\\ e inclusão", "dorange")]
_o = [r"\node[circle, draw=black!70, fill=dshade!60, line width=2.4pt, minimum size=3.2cm, font=\Large\bfseries, align=center] (c) at (9.7,4.3) {Ética\\ em HRI};"]
for i, (t, c) in enumerate(temas):
    ang = 90 - i * 360 / len(temas)
    x, y = 9.7 + 6.6 * math.cos(math.radians(ang)), 4.3 + 3.5 * math.sin(math.radians(ang))
    _o.append(r"\node[dbox, draw=%s, fill=%s!8, line width=1.7pt, text width=3.0cm, minimum height=1.4cm, font=\large\bfseries, text=%s] (t%d) at (%.2f,%.2f) {%s};" % (c, c, c, i, x, y, t))
    _o.append(r"\draw[black!45, line width=1.4pt] (c) -- (t%d);" % i)
w("temas-eticos", "\n".join(_o))

# ------------------------------------------------------------ 8. a avó e o robô devolvido
w("cuidado-devolvido", r"""
\draw[daxis, line width=1.2pt] (0.8,1.6) -- (18.6,1.6) node[right, font=\large] {tempo};
\draw[daxis, line width=1.2pt] (0.8,1.6) -- (0.8,7.4) node[above, font=\large] {solidão};
\draw[black!35, dashed, line width=1.1pt] (6.4,1.6) -- (6.4,7.0);
\draw[black!35, dashed, line width=1.1pt] (13.6,1.6) -- (13.6,7.0);
\draw[dred, line width=3.2pt, line join=round] (1.2,4.4) -- (6.4,4.4) -- (7.0,2.4) -- (13.6,2.4) -- (14.2,6.4) -- (18.2,6.4);
\node[font=\large\bfseries, black!70, text width=5cm, align=center] at (3.8,7.5) {rotina do asilo};
\node[font=\large\bfseries, dgreen, text width=7cm, align=center] at (10.0,7.5) {3 semanas com o robô};
\node[font=\large\bfseries, dred, text width=4.4cm, align=center] at (16.2,7.5) {robô devolvido};
\node[font=\large, dgreen, text width=6.4cm, align=center] at (10.0,3.5) {companhia, jogos de memória, nunca discute};
\node[font=\large, dred, text width=4.4cm, align=center] at (16.2,5.4) {\textbf{ainda mais} sozinha do que antes};
\node[font=\large, text width=18cm, align=center] at (9.7,0.5) {o apego se forma rápido; \textbf{retirar} o robô ao fim do estudo tem consequências emocionais};
""")

# ------------------------------------------------------------ 9. três tipos de relação e o argumento de Sparrow
w("relacoes-cuidado", r"""
\tikzset{c/.style={dbox, text width=4.9cm, minimum height=2.5cm, font=\large, line width=1.7pt},
        a/.style={dtrans, line width=2pt, -{Stealth[length=3.2mm]}}}
\node[c, draw=dblue] (a) at (3.0,6.2) {\textbf{\textcolor{dblue}{Ferramenta}}\\ só um instrumento};
\node[c, draw=dgreen] (b) at (9.7,6.2) {\textbf{\textcolor{dgreen}{Ferramenta social}}\\ com capacidades sociais};
\node[c, draw=dorange] (d) at (16.4,6.2) {\textbf{\textcolor{dorange}{Parceiro}}\\ uma relação, de fato};
\draw[a] (a.east) -- (b.west); \draw[a] (b.east) -- (d.west);
\node[font=\large\bfseries] at (9.7,8.1) {quanto mais \textbf{vínculo emocional} $\rightarrow$};
\node[dbox, draw=dred, fill=dred!6, line width=1.7pt, text width=17.4cm, minimum height=2.8cm, font=\large] at (9.7,2.0) {\textbf{O argumento de Sparrow e Sparrow (2006)}\\ mesmo um cuidador robótico perfeito seria antiético: uma relação só é significativa entre quem pode sentir \textbf{afeto e preocupação recíprocos}; \textbf{imitar} o cuidado nunca substitui o real};
""")

# ------------------------------------------------------------ 10. persuasão pela repetição de palavras
w("mera-exposicao", r"""
\draw[daxis, line width=1.2pt] (0.8,1.8) -- (8.4,1.8) node[right, font=\normalsize] {tempo};
\draw[daxis, line width=1.2pt] (0.8,1.8) -- (0.8,6.8) node[above, font=\normalsize] {atitude positiva};
\draw[dgreen, line width=3pt, domain=0:7, samples=40] plot (\x+1.0, {1.9+3.9*(1-exp(-0.45*\x))});
\node[font=\large\bfseries, dgreen, text width=7cm, align=center] at (4.6,7.7) {efeito de mera exposição};
\node[font=\large, text width=7.4cm, align=center] at (4.6,0.6) {quanto mais se ouve uma palavra, mais \textbf{positiva} ela soa};
\tikzset{c/.style={dbox, text width=7.6cm, minimum height=1.6cm, font=\large, line width=1.6pt}}
\node[c, draw=dblue] (a) at (14.2,7.0) {o robô de compras sugere ``\textbf{Pepsi}'' em vez de ``\textbf{Coca-Cola}''};
\node[c, draw=dorange] (b) at (14.2,4.5) {milhares de robôs \textbf{sincronizam} o vocabulário pela internet, \textbf{em segundos}};
\node[c, draw=dred, fill=dred!6] (d) at (14.2,2.0) {\textbf{quem decide} as palavras que os robôs usam?};
\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (a.south) -- (b.north);
\draw[dtrans, line width=1.8pt, -{Stealth[length=3mm]}] (b.south) -- (d.north);
""")

# ------------------------------------------------------------ 11. abuso e generalização
w("abuso-generalizacao", r"""
\tikzset{c/.style={dbox, text width=5.4cm, minimum height=2.6cm, font=\large, line width=1.7pt},
        a/.style={dtrans, line width=2pt, -{Stealth[length=3.2mm]}}}
\node[c, draw=dred] (a) at (3.0,4.6) {\textbf{\textcolor{dred}{Comportamento abusivo}}\\ chutar, bater, insultar, não sair da frente do robô};
\node[c, draw=black!55, fill=white] (b) at (3.0,0.9) {o robô \textbf{não sente dor}; o humano é quem pode se machucar};
\node[c, draw=dorange] (d) at (9.7,4.6) {\textbf{\textcolor{dorange}{Ofensa moral?}}\\ violência é errada mesmo sem vítima (Whitby, 2008)};
\node[c, draw=dgreen, fill=dgreen!6] (e) at (16.4,4.6) {\textbf{\textcolor{dgreen}{Generalização?}}\\ pode se estender a animais e a pessoas};
\draw[a] (a.east) -- (d.west); \draw[a] (d.east) -- (e.west);
\draw[black!50, dashed, line width=1.4pt] (a.south) -- (b.north);
\node[font=\large, text width=7cm, align=center] at (13.3,1.4) {transferência já discutida em jogos violentos; \textbf{faltam estudos}};
""")

# ------------------------------------------------------------ 12. robôs e emprego
w("emprego-robos", r"""
\tikzset{c/.style={dbox, text width=8.6cm, minimum height=3.4cm, font=\large, line width=1.7pt}}
\node[c, draw=dred] at (4.7,6.0) {\textbf{\textcolor{dred}{Substituem}}\\ certos empregos, como a máquina fez desde a Revolução Industrial};
\node[c, draw=dgreen] at (14.7,6.0) {\textbf{\textcolor{dgreen}{Criam}}\\ novos empregos, sobretudo para \textbf{profissionais bem treinados}};
\node[dbox, draw=dorange, fill=dorange!8, line width=1.7pt, text width=18.6cm, minimum height=1.7cm, font=\large] at (9.7,3.0) {\textbf{o desafio}: quem perde o emprego precisa de \textbf{requalificação}, que pode ser inviável por limites financeiros ou intelectuais};
\node[dbox, draw=dblue, fill=dblue!8, line width=1.7pt, text width=18.6cm, minimum height=1.9cm, font=\large] at (9.7,0.9) {\textbf{na escola}: robô \textbf{assistente}, sim; \textbf{professor principal}, não; quem já gosta de tecnologia aceita melhor (Reich-Stiebert e Eyssel, 2015)};
""")

# ------------------------------------------------------------ 13. ambivalência x neutralidade
w("ambivalencia-2x2", r"""
\tikzset{c/.style={dbox, text width=5.3cm, minimum height=2.9cm, font=\large, line width=1.7pt}}
\draw[daxis, line width=1.4pt] (1.6,0.6) -- (13.6,0.6) node[right, font=\large] {avaliação \textbf{positiva}};
\draw[daxis, line width=1.4pt] (1.6,0.6) -- (1.6,8.2) node[above, font=\large] {avaliação \textbf{negativa}};
\node[c, draw=black!55] at (4.9,2.3) {\textbf{Indiferença}\\ pouco positivo, pouco negativo};
\node[c, draw=dgreen] at (10.9,2.3) {\textbf{\textcolor{dgreen}{Atitude positiva}}\\ muito positivo, pouco negativo};
\node[c, draw=dred] at (4.9,5.9) {\textbf{\textcolor{dred}{Atitude negativa}}\\ pouco positivo, muito negativo};
\node[c, draw=dorange, fill=dorange!10, line width=2.4pt] at (10.9,5.9) {\textbf{\textcolor{dorange}{Ambivalência}}\\ \textbf{os dois ao mesmo tempo}: conflito interno};
\node[dbox, draw=dblue, fill=dblue!8, line width=1.6pt, text width=4.6cm, minimum height=5.0cm, font=\large] at (16.9,4.1) {atitudes aparentemente \textbf{neutras} podem ser, na verdade, \textbf{ambivalentes} (Stapels e Eyssel, 2021, 2022)};
""")

# ------------------------------------------------------------ 14. WEIRD e eixos de diversidade
_o = []
for i, (l, t) in enumerate([("W", "ocidentais"), ("E", "educados"), ("I", "industrializados"), ("R", "ricos"), ("D", "democráticos")]):
    y = 7.2 - i * 1.4
    _o.append(r"\node[circle, draw=dorange, fill=dorange!12, line width=1.6pt, minimum size=1.0cm, font=\Large\bfseries] at (1.0,%s) {%s};" % (y, l))
    _o.append(r"\node[font=\large, anchor=west] at (1.8,%s) {%s};" % (y, t))
_o.append(r"\node[font=\Large\bfseries, dorange] at (3.0,8.4) {WEIRD};")
_o.append(r"\node[dbox, draw=black!55, fill=white, line width=1.5pt, text width=4.6cm, minimum height=1.1cm, font=\normalsize] at (3.2,0.3) {a maior parte dos estudos de HRI vem destas populações};")
_o.append(r"\node[font=\Large\bfseries, dgreen] at (12.0,8.4) {eixos de diversidade pouco considerados};")
eixos = ["sexo e gênero", "raça e etnia", "idade", "sexualidade e família", "deficiência", "tipo de corpo", "ideologia", "expertise no domínio"]
for i, e in enumerate(eixos):
    col, lin = i % 2, i // 2
    _o.append(r"\node[dbox, draw=dgreen, fill=dgreen!8, line width=1.5pt, text width=4.2cm, minimum height=1.1cm, font=\large] at (%s,%s) {%s};" % (9.9 + col * 4.8, 7.3 - lin * 1.55, e))
_o.append(r"\node[font=\large, dgreen, text width=10cm, align=center] at (12.3,0.7) {em quem \textbf{pesquisa}, em quem \textbf{participa} e nos \textbf{contextos} de uso};")
w("weird-diversidade", "\n".join(_o))

# ------------------------------------------------------------ 15. viés de grupo com robôs
w("vies-grupos", r"""
\newcommand{\rob}[3]{% x, y, fill
  \draw[black!75, fill=#3, line width=1.6pt, rounded corners=4pt] (#1-0.9,#2-0.8) rectangle (#1+0.9,#2+0.9);
  \fill[white] (#1-0.4,#2+0.25) circle (0.19); \fill[white] (#1+0.4,#2+0.25) circle (0.19);
  \draw[black!75, line width=1.6pt] (#1,#2+0.9) -- (#1,#2+1.35); \fill[black!75] (#1,#2+1.45) circle (0.1);
  \draw[black!75, fill=#3, line width=1.6pt, rounded corners=4pt] (#1-1.1,#2-2.1) rectangle (#1+1.1,#2-1.0);}
\rob{2.6}{5.6}{black!10}
\rob{8.2}{5.6}{black!70}
\node[font=\large\bfseries, black!80, text width=4cm, align=center] at (2.6,2.6) {robô do \textbf{endogrupo}\\ (parece do mesmo grupo)};
\node[font=\large\bfseries, black!80, text width=4cm, align=center] at (8.2,2.6) {robô do \textbf{exogrupo}\\ (parece de outro grupo)};
\node[font=\Large\bfseries, black!75] at (14.7,8.0) {``mente'' atribuída};
\fill[dgreen!70] (12.6,1.6) rectangle (13.9,6.8);
\fill[dred!70] (15.3,1.6) rectangle (16.6,4.4);
\node[font=\large\bfseries, dgreen] at (13.25,7.3) {mais};
\node[font=\large\bfseries, dred] at (15.95,5.0) {menos};
\node[font=\large, text width=7cm, align=center] at (14.75,0.7) {sobretudo em participantes com alto \textbf{preconceito} (esquemático)};
""")

# ------------------------------------------------------------ 16. caminhos para um HRI mais inclusivo
w("caminhos-inclusivos", boxes([
  ("Moral proativa", r"identificar e \textbf{corrigir} o viés antes de o robô ser usado (Howard e Borenstein, 2018)"),
  ("Equidade e comunidade", r"considerar \textbf{uso ético e equidade}; \emph{Black in Robotics} (Howard e Kennedy III, 2020)"),
  ("Olhar feminista", r"\textbf{questionar o poder} entre pesquisadores, participantes e quem decide (Winkle et al., 2023)"),
  ("Design participativo", r"\textbf{empoderar} quem vai usar os robôs a decidir sobre o seu uso")],
  w=4.3, h=4.6, cols=4, cap=r"incluir mais vozes \textbf{durante} o desenvolvimento, e não só depois", capw=18))

# ------------------------------------------------------------ falando com a imprensa (antes, durante, depois)
w("falando-imprensa", r"""
\tikzset{c/.style={dbox, text width=5.2cm, minimum height=4.6cm, font=\large, line width=1.7pt, align=left}}
\node[dbox, draw=dred, dashed, fill=dred!6, line width=1.6pt, text width=16.4cm, minimum height=1.3cm, font=\large] at (9.7,7.9) {\textbf{oportunidade}, mas com \textbf{risco}: o repórter pode querer uma \textbf{história de alarme} sem dizer};
\node[c, draw=dblue] (a) at (3.2,4.0) {\textbf{\textcolor{dblue}{Antes}}\\[4pt] $\bullet$ \textbf{treinamento de mídia}\\ $\bullet$ \textbf{esclarecer as perguntas} que serão feitas};
\node[c, draw=dgreen] (b) at (9.7,4.0) {\textbf{\textcolor{dgreen}{Durante}}\\[4pt] $\bullet$ ficar na \textbf{pesquisa que foi feita}\\ $\bullet$ \textbf{não especular} sobre o que o estudo não cobriu};
\node[c, draw=dorange] (d) at (16.2,4.0) {\textbf{\textcolor{dorange}{Depois}}\\[4pt] $\bullet$ pedir para \textbf{ver o rascunho} do texto\\ $\bullet$ \textbf{corrigir} erros antes de publicar};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a.east) -- (b.west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b.east) -- (d.west);
""")

# ------------------------------------------------------------ expectativas de quem participa
w("expectativas-participante", r"""
\tikzset{s/.style={dbox, text width=4.4cm, minimum height=1.5cm, font=\large, line width=1.6pt}}
\node[s, draw=dorange] (a) at (2.6,6.6) {\textbf{filmes}, séries e livros};
\node[s, draw=dred] (b) at (2.6,4.4) {\textbf{notícias} enviesadas};
\node[s, draw=dgreen, dashed] (c) at (2.6,2.2) {\textbf{pesquisa} científica};
\node[ellipse, draw=black!60, fill=white, line width=1.8pt, text width=4.2cm, minimum height=3.2cm, font=\large, align=center, inner sep=4pt] (e) at (9.4,4.4) {\textbf{expectativas}\\ sobre o que o robô pode e não pode fazer};
\draw[dorange, line width=4pt, -{Stealth[length=3.6mm]}] (a.east) -- (e.north west);
\draw[dred, line width=4pt, -{Stealth[length=3.6mm]}] (b.east) -- (e.west);
\draw[dgreen, dashed, line width=1.2pt, -{Stealth[length=2.6mm]}] (c.east) -- (e.south west);
\draw[dblue, fill=dblue!15, line width=1.6pt] (14.2,5.4) circle (0.5);
\draw[dblue, fill=dblue!15, line width=1.6pt, rounded corners=5pt] (13.5,3.6) rectangle (14.9,4.9);
\node[font=\large\bfseries, dblue] at (14.2,3.0) {participante};
\draw[dgreen, fill=dgreen!15, line width=1.6pt, rounded corners=3pt] (16.9,4.0) rectangle (18.5,5.4);
\fill[dgreen] (17.3,4.9) circle (0.12); \fill[dgreen] (18.1,4.9) circle (0.12);
\draw[dgreen, line width=1.6pt] (17.7,5.4) -- (17.7,5.8); \fill[dgreen] (17.7,5.9) circle (0.08);
\draw[dgreen, fill=dgreen!15, line width=1.6pt, rounded corners=3pt] (16.7,2.9) rectangle (18.7,3.9);
\node[font=\large\bfseries, dgreen] at (17.7,2.4) {robô};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (11.8,4.4) -- (13.2,4.4);
\draw[dtrans, line width=2pt, dashed, -{Stealth[length=3.2mm]}] (15.2,4.3) -- (16.5,4.3);
\node[font=\large, text width=14cm, align=center] at (9.7,0.7) {as expectativas vêm \textbf{mais da ficção} e da mídia do que da \textbf{ciência}};
""")

# ------------------------------------------------------------ robos na pesquisa (Mago de Oz e persuasao)
w("robos-pesquisa", r"""
\tikzset{k/.style={dbox, text width=4.6cm, minimum height=1.9cm, font=\large, line width=1.6pt}}
\node[font=\large\bfseries, dorange, anchor=west] at (0.2,8.3) {Mágico de Oz};
\node[k, draw=dblue, dashed] (a) at (2.9,6.6) {\textbf{operador} escondido comanda o robô};
\node[k, draw=dorange] (b) at (9.7,6.6) {o robô \textbf{parece autônomo}};
\node[k, draw=dred] (c) at (16.5,6.6) {\textbf{expectativas infladas}: a tecnologia parece mais avançada};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a.east) -- (b.west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b.east) -- (c.west);
\node[font=\large\bfseries, dblue, anchor=west] at (0.2,4.3) {Persuasão};
\node[k, draw=dblue] (d) at (2.9,2.6) {robô \textbf{persuasivo}\\ {\normalsize (ex.: hábitos de saúde)}};
\node[k, draw=dgreen] (e) at (9.7,2.6) {muda \textbf{atitudes} e \textbf{comportamentos}};
\node[k, draw=dred, dashed] (f) at (16.5,2.6) {\textbf{explora o vínculo social} sem \textbf{consentimento} nem consciência?};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (d.east) -- (e.west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (e.east) -- (f.west);
""")

# ------------------------------------------------------------ escola e casa
w("escola-casa", r"""
\tikzset{k/.style={dbox, text width=5.6cm, minimum height=1.7cm, font=\large, line width=1.6pt}}
\node[font=\large\bfseries, dblue, anchor=west] at (0.2,8.4) {Na sala de aula};
\node[k, draw=dgreen] (a) at (3.2,6.8) {robô como \textbf{assistente}\\ {\normalsize \textbf{preferido}}};
\node[k, draw=dred, dashed] (b) at (9.7,6.8) {robô como \textbf{professor principal}\\ {\normalsize \textbf{não} preferido}};
\node[k, draw=dorange, text width=5.9cm] (c) at (16.3,6.8) {\textbf{temores} dos professores: \textbf{manutenção}, perda de \textbf{tempo e atenção}};
\node[font=\large\bfseries, dblue, anchor=west] at (0.2,4.7) {O que prevê a aceitação};
\node[k, draw=dblue] (d) at (4.6,3.0) {\textbf{comprometimento} com a tecnologia\\ {\normalsize (escola)}};
\node[k, draw=dblue] (e) at (4.6,0.9) {\textbf{abertura} à tecnologia\\ {\normalsize (robôs assistivos em casa)}};
\node[k, draw=dgreen, text width=6.2cm, minimum height=3.7cm] (f) at (14.6,1.95) {\textbf{atitudes positivas}\\ e \textbf{aceitação} do robô};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (d.east) -- (f.north west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (e.east) -- (f.south west);
""")

# ------------------------------------------------------------ quem participa e quem constroi
w("participa-constroi", r"""
\tikzset{k/.style={dbox, text width=7.4cm, minimum height=2.6cm, font=\large, line width=1.6pt}}
\node[font=\large\bfseries, dblue] at (4.4,8.4) {Quem participa dos estudos};
\node[font=\large\bfseries, dorange] at (15.0,8.4) {Quem constrói os robôs};
\node[k, draw=dblue] (a) at (4.4,6.5) {\textbf{homens sobrerrepresentados} entre os participantes\\ {\normalsize (estudos de HRI, 2006--2021)}};
\node[k, draw=dblue] (b) at (4.4,3.4) {gênero tratado como \textbf{binário}};
\node[k, draw=dorange] (c) at (15.0,6.5) {\textbf{poucos} desenvolvedores de países em desenvolvimento};
\node[k, draw=dorange] (d) at (15.0,3.4) {\textbf{poucas} soluções para ambientes com \textbf{poucos recursos}};
\node[dbox, draw=dred, dashed, fill=dred!6, line width=1.8pt, text width=9.6cm, minimum height=1.7cm, font=\large] (e) at (9.7,0.4) {a falta de diversidade pode \textbf{agravar o viés} no design dos robôs};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b.south) -- (b.south |- e.north) -- (e.north west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (d.south) -- (d.south |- e.north) -- (e.north east);
""")

# ------------------------------------------------------------ categorias sociais e robos
w("categorias-robos", r"""
\tikzset{k/.style={dbox, text width=4.6cm, minimum height=1.5cm, font=\large, line width=1.6pt}}
% robo
\draw[dgreen, fill=dgreen!15, line width=1.6pt, rounded corners=3pt] (0.2,2.4) rectangle (2.2,3.9);
\fill[dgreen] (0.75,3.3) circle (0.14); \fill[dgreen] (1.65,3.3) circle (0.14);
\draw[dgreen, line width=1.6pt] (1.2,3.9) -- (1.2,4.35); \fill[dgreen] (1.2,4.4) circle (0.09);
\draw[dgreen, fill=dgreen!15, line width=1.6pt, rounded corners=3pt] (0.0,1.2) rectangle (2.4,2.3);
\node[k, draw=dorange, text width=3.9cm] (a) at (5.3,4.4) {\textbf{pistas visuais}\\ {\normalsize (idade, etnia, gênero)}};
\node[k, draw=dorange, text width=3.9cm] (b) at (5.3,2.2) {só o \textbf{nome} do robô};
\node[k, draw=dblue, text width=4.4cm] (c) at (11.3,3.3) {\textbf{categoria social} inferida};
\node[k, draw=dred, text width=4.4cm] (d) at (17.0,3.3) {impressão \textbf{rápida} e \textbf{automática}};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a.east) -- (c.north west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b.east) -- (c.south west);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (c.east) -- (d.west);
\node[dbox, draw=dred, dashed, fill=dred!6, line width=1.6pt, text width=16cm, minimum height=1.2cm, font=\large] at (10.0,0.2) {mesmo robôs \textbf{neutros em gênero} ativam \textbf{vieses}: as pessoas trazem suas experiências e suposições};
""")

# ------------------------------------------------------------ nome e pais de origem
w("nome-pais", r"""
\tikzset{k/.style={dbox, text width=5.8cm, minimum height=1.7cm, font=\large, line width=1.6pt}}
\draw[dgreen, fill=dgreen!15, line width=1.6pt, rounded corners=3pt] (8.7,3.0) rectangle (10.7,4.3);
\fill[dgreen] (9.25,3.8) circle (0.14); \fill[dgreen] (10.15,3.8) circle (0.14);
\draw[dgreen, line width=1.6pt] (9.7,4.3) -- (9.7,4.6);
\draw[dgreen, fill=dgreen!15, line width=1.6pt, rounded corners=3pt] (8.5,2.0) rectangle (10.9,2.9);
\node[font=\large\bfseries, dgreen] at (9.7,5.0) {a mesma imagem do robô};
\node[k, draw=dblue] (a) at (3.2,3.3) {\textbf{nome} e \textbf{país de produção} do \textbf{endogrupo}};
\node[k, draw=dorange] (b) at (16.2,3.3) {\textbf{nome} e \textbf{país de produção} do \textbf{exogrupo}};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a.east) -- (8.3,3.3);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b.west) -- (11.1,3.3);
\node[k, draw=dgreen, line width=1.8pt] (c) at (3.2,0.6) {\textbf{preferido}, até na \textbf{avaliação do design}};
\node[k, draw=dred, dashed, line width=1.8pt] (d) at (16.2,0.6) {\textbf{menos preferido}};
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (a.south) -- (c.north);
\draw[dtrans, line width=2pt, -{Stealth[length=3.2mm]}] (b.south) -- (d.north);
""")
