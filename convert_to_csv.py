import csv

def processar_entrada(texto):
    # Separar as linhas e remover espaços desnecessários
    linhas = [linha.strip() for linha in texto.strip().split('\n') if linha.strip()]
    
    # Agrupar as linhas em pares (inglês, português)
    pares = [(linhas[i], linhas[i + 1]) for i in range(0, len(linhas), 2)]
    
    return pares

def criar_csv(pares, nome_arquivo):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Inglês", "Português"])  # Cabeçalho
        writer.writerows(pares)

if __name__ == "__main__":
    # Dados de entrada
    texto = """
I promise that, from now on, I’ll always tell you the truth.
Eu prometo que, de agora em diante, eu sempre lhe direi a verdade.

From now on, every student must switch off their phones before coming to my class.
De agora em diante, todos os alunos deverão desligar os seus celulares antes de vir para a minha aula.

The teacher made it known that from now on, she will not tolerate any lateness to class.
A professora divulgou que, de agora em diante, ela não tolerará quaisquer atrasos para a aula.

From now on, I will stop fending for anyone other than myself as it is now every man for himself.
De agora em diante, eu irei parar de defender a qualquer um além de mim mesmo, já que agora é cada um por si.

Mary told us that from now on, she wouldn’t be eating any meat or fish as she is starting a vegetarian diet.
A Mary nos disse que, de agora em diante, ela não comerá nenhuma carne ou peixe, já que está começando uma dieta vegetariana.

After her wedding to Paul yesterday, Alice told us that from now on, we are to refer to her married name.
Depois do seu casamento com o Paul ontem, a Alice nos disse que, de agora em diante, nós deveremos chamá-la pelo seu nome de casada.

From now on you can wear casual clothes to work every Friday.
De agora em diante, você poderá usar roupas casuais no trabalho toda sexta-feira.

From here on out, I’m making all the decisions.
De agora em diante, eu tomarei todas as decisões.

We need to follow the map from here on out — otherwise, we’re liable to get lost.
Nós precisamos seguir o mapa de agora em diante — caso contrário, nós poderemos nos perder.

I was lucky to escape from the accident with just a few minor injuries, so from now on I’m going to be much more careful when I drive.
Eu tive sorte de escapar do acidente com apenas alguns ferimentos leves, então, de agora em diante, eu tomarei muito mais cuidado quando dirigir.

From now on the gates will be locked at midnight.
De agora em diante, os portões serão trancados à meia-noite.

I’m sorry, I’ll take my responsibilities more seriously from now on.
Desculpe, eu levarei as minhas responsabilidades mais a sério de agora em diante.

We stayed up all night talking.
Nós passamos a noite acordados, conversando.

Kate stayed up all night by his bedside.
A Kate passou a noite acordada ao lado da cama dele.

The kids were allowed to stay up all night on New Year’s Eve.
As crianças tinham permissão para passar a noite acordadas na véspera de Ano Novo.

We stayed up all night, chatting about old times.
Nós passamos a noite acordados, conversando sobre os velhos tempos.

I stayed up all night, watching the Olympics on television.
Eu passei a noite acordado, assistindo às Olimpíadas na televisão.

They stay up all night and then they don’t do their job properly.
Eles passam a noite acordados e depois eles não fazem o seu trabalho adequadamente.

I was up all night yesterday because I had drunk so much coffee.
Eu passei a noite acordado ontem porque eu havia bebido café demais.

She had been up all night studying.
Ela havia passado a noite acordada, estudando.

The cafe filled up with students who had been up all night.
A cafeteria encheu de estudantes que haviam passado a noite acordados.

We were up all night trying to figure out what to do.
Nós passamos a noite acordados tentando resolver o que fazer.

Our son was up all night long with a headache, so everyone is feeling pretty tired today.
O nosso filho passou a noite acordado com dor de cabeça, então todos estão se sentindo bem cansados hoje.

The book was so interesting that I sat up all night reading it.
O livro estava tão interessante que eu passei a noite acordado, lendo-o.

The nurse sat up all night by her side.
A enfermeira passou a noite acordada ao lado dela.

My parents sat up all night waiting for me to come home.
Meus pais passaram a noite acordados, esperando eu voltar para casa.

I’ve found a witness willing to name names.
Eu encontrei uma testemunha disposta a dar nome aos bois.

I hate to name names, but Brian and Mitch were the ones who did the graffiti. I saw it myself.
Eu detesto dar nome aos bois, mas foram o Brian e o Mitch que fizeram a pichação. Eu vi com os meus próprios olhos.

I’m not going to name names, but several of you have been coming in late and going home early. This needs to stop.
Eu não irei dar nome aos bois, mas vários de vocês têm chegado tarde e ido para casa cedo. Isso precisa parar.

More than one person was involved in the robbery, and his lawyer said he would get a shorter sentence if he named names.
Mais de uma pessoa estava envolvida no assalto, e o advogado dele disse que ele receberia uma sentença menor se desse nome aos bois.

Some of our neighbors disobey the town’s leash law, but I’m naming no names.
Alguns dos nossos vizinhos desobedecem a lei da cidade que exige o uso de coleira em animais, mas eu não darei nome aos bois.

He was under pressure from the police to name names.
Ele estava sendo pressionado pela polícia para dar nome aos bois.

If the newspapers really know the people responsible for these terrible crimes, then they should name names.
Se os jornais realmente conhecem as pessoas responsáveis por esses crimes terríveis, então eles deveriam dar nome aos bois.

I won’t name names, but there are some people in this room who have broken several of the club’s rules.
Eu não irei dar nome aos bois, mas há certas pessoas nessa sala que quebraram várias regras do clube.

She said she would never name names, even if she were offered money.
Ela disse que jamais daria nome aos bois, mesmo que lhe oferecessem dinheiro.

If you’re convinced my staff is part of this operation, then name names.
Se você está convencido de que os meus funcionários são parte dessa operação, então dê nome aos bois.

Nobody was prepared to risk prosecution by actually naming names.
Ninguém estava preparado para arriscar um processo por de fato dar nome aos bois.

We’ve been affiliated to Hostelling International for more than 15 years.
Nós somos afiliados à Hostelling International há mais de 15 anos.

I’ve been maintaining strong international partnerships for more than 25 years.
Eu mantenho fortes parcerias internacionais há mais de 25 anos.

We have been providing innovative manufacturing technology for more than fifteen years.
Nós fornecemos tecnologias de fabricação inovadoras há mais de quinze anos.

This library has existed for more than four hundred years.
Esta biblioteca existe há mais de quatrocentos anos.

The brand has been making history in the naval industry for more than 75 years.
A marca vem fazendo história na indústria naval há mais de 75 anos.

I’m starting to get worried. He’s been gone for over an hour.
Eu estou começando a ficar preocupado. Ele foi embora há mais de uma hora.

We’ve known each other for over a decade.
Nós nos conhecemos há mais de uma década.

She’s been an outspoken feminist for over twenty years.
Ela tem sido uma feminista ferrenha há mais de vinte anos.

I’ve been smoking for over ten years, and I can’t stop.
Eu fumo há mais de dez anos e não consigo parar.

Bentley has been providing solutions to highway agencies for over three decades.
A Bentley fornece soluções para concessionárias de rodovias há mais de três décadas.

Sefar has served the chemical and mining industries for over 50 years.
A Sefar atende as indústrias química e de mineração há mais de 50 anos.

He was a huge yes-man.
Ele era uma baita vaquinha de presépio.

To be sure, this skepticism of the yes-man mentality has advantages.
Com certeza, esse ceticismo da mentalidade de vaquinha de presépio tem vantagens.

Becoming a dull yes-man seemed too big a price to pay.
Tornar-se uma vaquinha de presépio sem graça parecia um preço grande demais a pagar.

“I totally agree,” the yes-man said with a smile.
“Eu concordo totalmente”, a vaquinha de presépio disse com um sorriso.

They are all a bunch of yes-men.
Eles são todos um bando de vaquinhas de presépio.

A country of yes-men is a country marked for destruction.
Um país de vaquinhas de presépio é um país fadado à destruição.

That can happen to rich guys, particularly those who prefer to surround themselves with yes-men.
Isso pode acontecer com caras ricos, especialmente aqueles que preferem se cercar de vaquinhas de presépio.

This is making the policemen seem like subservient yes-men.
Isso está fazendo os policiais parecerem vaquinhas de presépio subservientes.

He accused the president of surrounding himself with yes-men, rewarding only sycophancy and punishing dissent.
Ele acusou o presidente de cercar-se de vaquinhas de presépio, recompensando apenas a bajulação e punindo a dissensão.

None of those yes-men that you call advisors will ever tell you what you need to hear.
Nenhuma daquelas vaquinhas de presépio que você chama de conselheiros jamais lhe dirá o que você precisa ouvir.

Have you met Christina’s fiancé?
Você já conheceu o noivo da Christina?

Let me introduce my fiancé.
Permita-me apresentar o meu noivo.

She couldn’t wait to show off her fiancé to all of her relatives.
Ela mal podia esperar para exibir o seu noivo a todos os seus parentes.

My fiancé just bought me this. Isn’t it gorgeous?
Meu noivo acabou de me comprar isso. Não é lindo?

Does anyone know where the groom is?
Alguém sabe onde o noivo está?

The bride and groom walked down the aisle together.
A noiva e o noivo caminharam até o altar juntos.

The expression on the groom’s face when he saw the bride was priceless.
A expressão facial do noivo quando ele viu a noiva foi inestimável.

Now, if you’d all please raise your glasses, I’d like to propose a toast to the bride and groom.
Agora, se todos puderem, por favor, erguer as suas taças, eu gostaria de propor um brinde à noiva e ao noivo.

His fiancée is insisting on an elaborate wedding.
A noiva dele está insistindo em um casamento elaborado.

It would be unfair to marry your fiancée without being honest with her.
Seria injusto casar com a sua noiva sem ser honesto com ela.

I even bought a pearl necklace for my fiancée, but she married somebody else instead.
Eu até mesmo comprei um colar de pérolas para a minha noiva, mas ela se casou com outra pessoa em vez de comigo.

If a relative announces his engagement, you must at once go to see his fiancée.
Se um parente anuncia seu noivado, você precisa imediatamente ir ver a noiva dele.

After the ceremony, the bride lifted up her veil to kiss her husband.
Após a cerimônia, a noiva ergueu o seu véu para beijar o seu marido.

In some countries, it is traditional for a bride to wear white.
Em alguns países, é tradição a noiva usar branco.

The bride and groom posed for pictures outside the church.
A noiva e o noivo posaram para fotos do lado de fora da igreja.

As the mother of the bride, I feel obliged to wear something really spectacular.
Como mãe da noiva, eu me sinto obrigada a vestir algo muito espetacular.

Good thing I’m an early riser or else I’d probably miss the beginning of school.
Ainda bem que eu sou madrugador, caso contrário provavelmente perderia o começo das aulas. (Note que a palavra school, “escola”, pode ser usada no sentido de “aulas”.)

I was surprised to see him asleep at 10:00, as he’s normally such an early riser.
Eu me surpreendi de vê-lo dormindo às 10 da manhã, já que normalmente ele é tão madrugador. (Note que “madrugador” é um adjetivo, mas early riser é um substantivo. Por isso, para dizer “tão early riser”, você precisa usar o artigo a, ou no caso an: such an early riser. Um outro exemplo: “Ele é uma pessoa tão boa”, He’s such a good person.)

My wife and I are early risers, usually up by 6.00.
A minha esposa e eu somos madrugadores, geralmente de pé às 6.

Maybe he was always such an early riser because he grew up on a farm.
Talvez ele tenha sempre sido tão madrugador porque cresceu em uma fazenda.

He’d always been an early riser, so getting up for a morning run wasn’t a great chore.
Ele sempre havia sido madrugador, de forma que não era grande tarefa ter de se levantar para uma corrida matinal.

He was always an early bird.
Ele sempre foi madrugador.

I’m usually an early bird: I enjoy the fresh morning air, the first rays of sun, the quiet.
Geralmente sou madrugador: gosto do ar fresco da manhã, dos primeiros raios de sol, do silêncio.

Being an early bird allowed me to get a lot of work done while everyone else was sleeping and there no distractions.
Ser madrugador me permitia realizar bastante trabalho enquanto todos os outros estavam dormindo e não havia distrações.

It is the early bird who gets the bargains, apparently.
É quem chega antes que consegue as pechinchas, aparentemente.

Everyone wanted to be an early bird and cash in on the sale.
Todo o mundo queria chegar adiantado e lucrar com a venda.

The early bird gets the worm.
Quem chega antes sai ganhando.

Are you more of a lark or an owl?
Você é mais madrugador ou mais coruja?

I’m definitely a lark – already as a child I enjoyed getting up early in the morning.
Eu sou certamente madrugador – já quando era criança eu gostava de me levantar cedo de manhã.

You’re not much of a lark, are you? Getting up at 11am every day.
Você não é muito madrugador, é? Levantando-se às 11 da manhã todo dia.

He’s not really a morning person – he doesn’t even talk before about eleven o’clock!
Ele não é mesmo madrugador – ele nem sequer fala antes das onze da manhã!

Try not to schedule yourself for 8 am classes unless you’re truly a morning person.
Tente não se inscrever para aulas das 8 da manhã a menos que você realmente seja madrugador.

I’m a morning person and like to get most of my work done before midday.
Eu sou madrugador e gosto de realizar a maior parte do meu trabalho antes do meio-dia.

He married his childhood sweetheart last July.
Ele se casou com o seu amor de infância no último mês de julho.

She was my very first childhood sweetheart.
Ela foi o meu primeiro amor de infância.

How cute! Mattie drew his childhood sweetheart.
Que fofo! O Mattie desenhou o seu amor de infância.

The football player ended the 18-year relationship with his childhood sweetheart, saying he no longer loved her.
O jogador de futebol terminou o seu relacionamento de 18 anos com o seu amor de infância, dizendo que não a amava mais.

On December 20, 1769, Garrard married his childhood sweetheart, Elizabeth Mountjoy.
Em 20 de dezembro de 1769, Garrard se casou com o seu amor de infância, Elizabeth Mountjoy.

Riise was married to his childhood sweetheart, the Norwegian model Guri Havnevik, from 2003 until they divorced in 2004.
Riise foi casado com o seu amor de infância, a modelo norueguesa Guri Havnevik, de 2003 até se divorciarem em 2004.

It’s been one year, 22 weeks and four days since he got married to his childhood sweetheart.
Faz um ano, 22 semanas e quatro dias que ele se casou com o seu amor de infância.

They came home proud war heroes and married their childhood sweethearts.
Eles voltaram para casa orgulhosos heróis de guerra e se casaram com os seus amores de infância.

They were childhood sweethearts and had been together for 11 years.
Eles eram namorados de infância e haviam estado juntos por 11 anos.

He and I are in our thirties but we were childhood sweethearts and have been married for 15 years.
Ele e eu estamos na casa dos trinta, mas nós éramos namorados de infância e estamos casados há 15 anos.

She and Fred were childhood sweethearts, but she refuses to admit that.
Ela e o Fred eram namorados de infância, mas ela se recusa a admitir isso.

Carole married her high school sweetheart after a 10-year relationship!
A Carole se casou com o seu namorado da escola após um relacionamento de 10 anos!

She married her high school sweetheart when she was very young and stayed at home to raise their four children.
Ela se casou com o seu namorado da escola quando era muito nova e ficou em casa para criar os seus quatro filhos.

He married his high school sweetheart in 1969, and in 1970 their first son was born.
Ele se casou com a sua namorada da escola em 1969, e, em 1970, seu primeiro filho nasceu.

She married her high school sweetheart and gave birth to a son; but the marriage ended a few years later.
Ela se casou com o seu namorado da escola e deu à luz um filho; mas o casamento acabou alguns anos mais tarde.

Don likes hockey, but he plays dirty.
O Don gosta de hóquei, mas ele joga sujo.

The opposition had started to play dirty.
A oposição havia começado a jogar sujo.

I’d watch out for that prosecutor. I heard he isn’t afraid to play dirty if it helps him win a case.
Eu ficaria de olho naquele promotor. Eu ouvi que ele não tem medo de jogar sujo se isso o ajudar a vencer um caso.

Of course, even when somebody plays dirty, losing is losing and it’s not long before nobody cares about the details.
Claro, mesmo quando alguém joga sujo, perder é perder e não demora muito até que ninguém ligue para os detalhes.

During the next election campaign, don’t be surprised when Labour Party plays dirty.
Durante a próxima campanha eleitoral, não fique surpreso quando o Partido Trabalhista jogar sujo.

"There is no way I would devalue the honour of playing for my country by playing dirty,” Harrison said.
“De jeito nenhum eu desvalorizaria a honra de jogar para o meu país por jogar sujo”, disse Harrison.

You can win, without even resorting to playing dirty.
Você pode vencer, sem nem mesmo recorrer a jogar sujo.

The bad news is that they are doing what they always do: playing dirty.
A má notícia é que eles estão fazendo o que sempre fazem: jogando sujo.

They could play big; they could not play at all; and they may turn up to find their opponents playing dirty.
Eles poderiam jogar muito, eles poderiam nem jogar; e eles poderiam acabar descobrindo que seus oponentes jogam sujo.

He stars as the infamous Rankin Fitch, a jury selection specialist not afraid to play dirty if it gets the results his clients pay him big bucks for.
Ele estrela como o infame Rankin Fitch, um especialista em seleção de júri sem medo de jogar sujo se isso lhe render os resultados pelos quais os seus clientes lhe pagam muito dinheiro.

Their team started playing dirty as soon as they fell behind, throwing sand into other players’ eyes or stepping on their toes when the ref wasn’t looking.
O time deles começou a jogar sujo assim que ficou para trás, jogando areia nos olhos dos outros jogadores ou pisando nos seus dedões quando o árbitro não estava olhando.

– It’s cold in here. – You can say that again!
– Está frio aqui. – Pode crer!

– It’s hot! – You can say that again.
– Está quente! – Pode crer.

– She’s in a bad mood. – You can say that again.
– Ela está de mau humor. – Pode crer.

– This is so boring! – You can say that again!
– Isso é tão chato! – Pode crer.

Brother, you can say that again!
Pode crer, irmão.

– Wow, that exam was brutally difficult. – You can say that again! It was the hardest test I’ve ever taken.
– Nossa, essa prova foi brutalmente difícil. – Pode crer! Foi a prova mais difícil que já fiz.

– What a relief that Brian didn’t get hurt. – You can say that again!
– Que alívio que o Brian não se machucou. – Pode crer!

– That was a pretty selfish thing for him to do. – You said it.
– Isso foi uma coisa bem egoísta de ele fazer. – Pode crer.

– How stupid of me to lend him that money! – You said it!
– Como foi estúpido da minha parte emprestar aquele dinheiro para ele! – Pode crer.

– I’ve made a terrible mess of this. – You said it.
– Fiz uma confusão terrível disso. – Pode crer.

– Let’s grab something to eat. – You said it. I’m starving.
– Vamos pegar algo para comer. – Pode crer, estou morrendo de fome.

– This cake is yummy! – You said it!
– Esse bolo é delicioso! – Pode crer!

They decided to get engaged.
Eles decidiram ficar noivos.

Debbie and Jake have just got engaged.
A Debbie e o Jake acabaram de ficar noivos.

We got engaged about this time last year.
Nós ficamos noivos por volta dessa época no ano passado.

He asked her to sign a prenuptial agreement when they got engaged.
Ele pediu para ela assinar um acordo pré-nupcial quando eles ficaram noivos.

We got engaged on my eighteenth birthday.
Nós ficamos noivos no meu aniversário de dezoito anos.

Alicia sported a gorgeous diamond ring after getting engaged to Ed.
A Alicia ostentava um maravilhoso anel de diamantes após ficar noiva do Ed.

She got engaged to her childhood sweetheart as soon as she left school.
Ela ficou noiva do seu amor de infância assim que saiu da escola.

I can’t believe we are engaged! I’m so happy!
Eu não acredito que estamos noivos! Eu estou tão feliz!

She was engaged to some guy in the army.
Ela estava noiva de um cara do exército.

How long have you been engaged?
Há quanto tempo vocês estão noivos?

She’s engaged to someone she met at work.
Ela está noiva de alguém que conheceu no trabalho.

You know Kelly’s engaged to Chris, so stop flirting with her!
Você sabe que a Kelly está noiva do Chris, então pare de flertar com ela!

This photo was taken when we were engaged.
Esta foto foi tirada quando estávamos noivos.

Of course she’s oblivious to the growing homeless population in our city — she can’t see beyond the end of her nose.
É claro que ela está alheia à crescente população sem-teto da nossa cidade ─ ela não vê um palmo à frente do nariz.

Thomas hasn’t hired an orchestra for the Christmas concert; he just can’t see beyond the end of his nose.
O Thomas não contratou uma orquestra para o concerto de Natal; ele simplesmente não vê um palmo à frente do nariz.

When it comes to the environment, sadly, this government can’t see beyond the end of its nose.
Quando se trata do meio ambiente, infelizmente, esse governo não vê um palmo à frente do nariz.

You’re too busy thinking about you and about everything to do with you that you don’t see beyond the end of your nose.
Você está tão ocupado pensando em si mesmo e em tudo relacionado a você, que não vê um palmo à frente do nariz.

He probably thought she was an overprotective, neurotic mother who couldn’t see beyond the end of her nose.
Ele provavelmente achava que ela era uma mãe superprotetora e neurótica, que não via um palmo à frente do nariz.

He explained his vision for the company and I believe he can’t see beyond the end of his nose.
Ele explicou a visão dele para a empresa e eu acho que ele não vê um palmo à frente do nariz.

If I asked her opinion, she likely would declare that you can’t see beyond the end of your nose.
Se eu perguntasse a opinião dela, ela provavelmente declararia que você não vê um palmo à frente do nariz.

“Why didn’t you tell me that she can’t see beyond the end of her nose?” she asked.
“Por que você não me disse que ela não vê um palmo à frente do nariz?”, ela perguntou.

He couldn’t save money or make plans for the future; he just never saw beyond the end of his nose.
Ele não conseguia economizar dinheiro ou fazer planos para o futuro; ele simplesmente nunca viu um palmo à frente do nariz.

People who always complain about school taxes would stop it if they could see beyond their noses and understand the importance of first-class schools.
As pessoas que sempre reclamam dos impostos escolares parariam com isso se conseguissem ver um palmo à frente do nariz e entendessem a importância das escolas de qualidade.

In financial planning, you need to see beyond the end of your nose.
No planejamento financeiro, você precisa ver um palmo à frente do nariz.

She was gazing out the window, rocking rhythmically to and fro.
Ela estava olhando pela janela, balançando-se ritmicamente para cá e para lá.

Outside my door I could hear people walking to and fro.
Do lado de fora da porta, eu podia ouvir pessoas andando para cá e para lá.

Not only do people move to and fro across international space, their personal relationships change.
Às pessoas não só se movem para cá e para lá no espaço internacional, mas também seus relacionamentos pessoais mudam.

She stood up and began to pace to and fro.
Ela levantou-se e começou a andar de um lado para o outro.

The boat was rocking gently to and fro in the water.
O barco estava balançando levemente para cá e para lá na água.

She rocked the baby to and fro.
Ela balançava o bebê para cá e para lá.

The ducks were toing and froing.
Os patos estavam indo de cá para lá.

There is a lot of toing and froing and complex weekend arrangements.
Há um monte de vaivéns e arranjos complexos de final de semana.

The wasps are still out there, toing and froing.
As vespas ainda está lá fora, indo de cá para lá.

We stood there among the busy to-and-fro of the holiday shoppers.
Ficamos ali, entre o vaivém atarefado dos compradores de fim de ano. (Note que holiday pode se referir a um feriado qualquer, mas geralmente é usado em relação ao período de “festas” de dezembro.)

We are following the to and fro in Britain.
Estamos seguindo o vaivém na Grã-Bretanha.

The endless to and fro between ministers and fishermen is getting us nowhere.
O vaivém infindo entre ministros e pescadores não está nos levando a lugar nenhum.

Who? That girl with the glasses and the ponytail?
Quem? Aquela garota de óculos e rabo de cavalo?

Will a young man with a ponytail have to cut it off?
Um rapaz com rabo de cavalo precisará cortá-lo?

She usually wears her hair pulled back in a ponytail.
Ela geralmente usa o cabelo puxado para trás em um rabo de cavalo.

Simply tie up your hair with a decorative scrunchie and your messy ponytail is instantly elevated.
Simplesmente amarre o seu cabelo com um elástico decorativo e seu rabo de cavalo bagunçado melhorará instantaneamente.

Her long hair was swept back in a ponytail.
O cabelo comprido dela estava puxado para trás em um rabo de cavalo.

Gloves are a good idea and be sure to tie long hair back into a ponytail.
Luvas são uma boa ideia, e certifique-se de amarrar cabelos compridos para trás em um rabo de cavalo.

Who is that girl with pigtails?
Quem é aquela garota de maria-chiquinha?

She had straight dark brown hair in pigtails.
Ela tinha um cabelo castanho-escuro liso (preso) em maria-chiquinha.

That’s just some random woman who wears her hair in pigtails the way Michelle used to.
Aquela é só uma mulher qualquer que prende o cabelo em maria-chiquinha da forma como a Michelle costumava prender.

A little girl in pigtails presented the bouquet.
Uma menininha de maria-chiquinha entregou o buquê.

The April issue of the magazine featured a pop star in pigtails.
A edição de abril da revista apresentava uma estrela do pop de maria-chiquinha.

He currently holds the position of technical manager.
Ele atualmente ocupa o cargo de gerente técnico.

Jeff holds the position of managing editor.
O Jeff ocupa o cargo de editor-chefe.

No one could imagine he would hold the position for 21 years.
Ninguém poderia imaginar que ele ocuparia o cargo por 21 anos.

Do you really think he’s capable of holding such a responsible position?
Você realmente acha que ele é capaz de ocupar um cargo de tamanha responsabilidade?

As chairman of the association, he held office for over 20 years.
Como presidente da associação, ele ocupou o cargo por mais de 20 anos.

She was the first woman to hold the office of prime minister.
Ela foi a primeira mulher a ocupar o cargo de primeira-ministra.

Whoever is elected will hold office for four years.
Quem quer que seja eleito ocupará o cargo por quatro anos.

The Coordinator is appointed for only six months at a time, but now he is to hold office for a year.
O Coordenador é nomeado para apenas seis meses por vez, mas agora ele ocupará o cargo por um ano.

She’s held the post for 13 years.
Ela ocupou o cargo por 13 anos.

The governor had held the post since 1989.
O governador havia ocupado o cargo desde 1989.

He will hold the post for three or four months.
Ele ocupará o cargo por três ou quatro meses.

In 1947, she was appointed as the Sheriff, first woman to hold the post.
Em 1947, ela foi designada como xerife, a primeira mulher a ocupar o cargo.

He’s been unemployed for over a year.
Ele está desempregado há mais de um ano.

Being unemployed entitles you to free medical treatment.
Estar desempregado lhe dá o direito a tratamento médico gratuito.

With Dave unemployed, we haven’t got much money coming in at the moment.
Com o David desempregado, nós não temos muito dinheiro entrando no momento.

His financial problems escalated after he became unemployed.
Os problemas financeiros dele aumentaram depois de ele ficar desempregado.

The gunman in Wednesday’s attack has been identified as Lee Giggs, an unemployed truck driver.
O atirador do ataque de quarta-feira foi identificado como Lee Giggs, um motorista de caminhão desempregado.

The government publishes figures every six months showing how many people are unemployed.
O governo divulga dados a cada seis meses mostrando quantas pessoas estão desempregadas.

Have you been unemployed for over six months?
Você está desempregado há mais de seis meses?

My father was out of work at the time, so we struggled, obviously.
Meu pai estava desempregado na época, então nós passamos dificuldade, obviamente.

I’ve been out of work for the past ten months.
Eu estou desempregado há dez meses.

The plant closed in November 2010, leaving 400 people out of work.
A fábrica fechou em novembro de 2010, deixando 400 pessoas desempregadas.

Joe was out of work for nearly eight months after the financial crisis.
O Joe ficou desempregado por quase oito meses depois da crise econômica.

You’ll be out of work if you ever pull a stunt like that again, do you understand?
Você ficará desempregado se você fizer uma coisa dessas de novo, você entendeu?

Whether a person is between jobs or wants to change career, volunteering can be one way of seeing what’s available.
Quer a pessoa esteja desempregada, quer deseje mudar de carreira, fazer serviço voluntário pode ser uma forma de ver o que está disponível.

Just tell the recruiter that you’re between jobs. She doesn’t need to know that you got fired!
Só diga à recrutadora que você está desempregado. Ela não precisa saber que você foi demitido!

“Tell me about your current position.” “I’m between jobs right now.”
“Conte-me sobre o seu cargo atual.” “Eu estou desempregado no momento.”

When Jill was between jobs, she took a computer class at the community college.
Quando a Jill estava desempregada, fez um curso de informática na faculdade comunitária.

Come here right now and say you’re sorry!
Venha aqui agora mesmo e peça desculpas!

The next morning she came into my room and said she was sorry.
Na manhã seguinte, ela veio ao meu quarto e pediu desculpas.

I’ve said I’m sorry a thousand times. What else can I do?
Eu já pedi desculpas mil vezes. O que mais posso fazer?

He said he was sorry he had upset me.
Ele pediu desculpas por ter me chateado.

“Then say you’re sorry,” I requested, unfolding my arms.
“Então peça desculpas”, eu pedi, descruzando os braços.

Apologize to significa “pedir desculpas para” ou “pedir desculpas a” e é seguido pela pessoa que receberá o pedido de perdão;
Apologize for significa “pedir desculpas por” ou “pedir desculpas pelo(a)” e é seguido pelo motivo de tal pedido.

If I offended you, I apologize.
Se eu te ofendi, peço desculpas.

There’s no need to apologize.
Não é preciso pedir desculpas.

I tried to apologize, but he refused to listen.
Eu tentei pedir desculpas, mas ele se recusou a escutar.

Imagine the humiliation of having to apologize.
Imagine a humilhação de ter que pedir desculpas.

The allegations were false and the newspaper apologized unreservedly.
As alegações eram falsas e o jornal pediu desculpas abertamente.

I must apologize to Isabel for my lateness.
Eu preciso pedir desculpas para a Isabel pelo meu atraso.

He apologized to the people who had been affected.
Ele pediu desculpas às pessoas que foram afetadas.

I would like to apologize to everybody.
Eu gostaria de pedir desculpas a todos.

He apologized for his mistake.
Ele pediu desculpas por seu erro.

She apologized for her husband’s rudeness.
Ela pediu desculpas pela grosseria do seu marido.

I apologize for taking so long to reply.
Eu peço desculpas por levar tanto tempo para responder.

She apologized profusely for having to leave at 3.30 p.m.
Ela pediu desculpas profusamente por ter que ir embora às 15:30.

Trains may be subject to delay – we apologize for any inconvenience caused.
Os trens podem estar sujeitos a atrasos – nós pedimos desculpas por qualquer inconveniência causada.

She apologized to us for losing her temper.
Ela pediu desculpas para nós por ter perdido a calma. (Lose one’s temper também pode ser traduzido como Chutar o Balde)

You should apologize to your customers for your behavior.
Você deveria pedir desculpas aos seus clientes pelo seu comportamento.

He’ll inherit his grandma’s car if she ever dies and that thing is a junker.
Ele herdará o carro da sua avó se ela morrer algum dia e aquilo é uma lata velha.

I’ve been driving this old junker around for so long because I just can’t part with it!
Eu dirijo essa lata velha há muito tempo porque não consigo me desfazer dela!

She has made a business out of buying junkers for cheap, fixing them up, and selling them off for a big profit.
Ela criou um negócio de comprar latas velhas por pouco dinheiro, consertá-las e vendê-las com muito lucro.

The Beverly Hills cops drive pristine cars; he drives an old, dilapidated junker.
Os policiais de Beverly Hills dirigem carros impecáveis; ele dirige uma lata velha decadente.

The choices you make now will help determine whether you end up owning a muscle car or a rusted-out old junker.
As escolhas que você faz agora ajudarão a determinar se você acabará tendo um muscle car ou uma lata velha enferrujada.

My first car was an old clunker that kept breaking down.
O meu primeiro carro era uma lata velha que vivia quebrando.

I think it’s time for me to get a new car — this one has turned out to be a real clunker.
Eu acho que está na hora de eu comprar um carro novo ─ esse aqui se mostrou ser uma lata velha.

He drives an old clunker and doesn’t have any insurance.
Ele dirige uma lata velha e não tem nenhum seguro.

I had to drive my mom’s clunker for a few weeks.
Eu tive que dirigir a lata velha da minha mãe por algumas semanas.

He worked long hours to keep his gas-guzzling clunker on the road.
Ele trabalhava muitas horas para manter a sua lata velha beberrona na estrada.

I can’t sell this old bucket of bolts!
Eu não consigo vender essa lata velha!

My old bucket of bolts wouldn’t start this morning.
Minha lata velha não queria pegar essa manhã.

I don’t want that bucket of bolts. I want a used car that is in good shape.
Eu não quero aquela lata velha. Eu quero um carro que esteja funcionando bem.

Elliott accused me of being selfish. Talk about the pot calling the kettle black!
Elliott me acusou de ser egoísta. Isso sim é que é o roto falando do esfarrapado.

Sean called me a liar – that’s the pot calling the kettle black!
Sean me chamou de mentiroso – isso é o roto falando do esfarrapado!

To be fair, my own criticism is an example of the pot calling the kettle black.
Para ser justo, a minha própria crítica é um exemplo do roto falando do esfarrapado.

At this point I was sitting in my chair thinking, man, this guy’s really the pot calling the kettle black, isn’t he?
Nesta altura, eu estava sentado na minha cadeira pensando: “Gente, esse cara realmente é o roto falando do esfarrapado, não é?”

This was a classic case of the pot calling the kettle black.
Era um caso clássico do roto falando do esfarrapado.

She said my brother never wanted to help, which was exactly like the pot calling the kettle black.
Ela disse que o meu irmão nunca queria ajudar, o que era exatamente como o roto falando do esfarrapado.

Forgive me for mentioning it, but isn’t it a case of the pot calling the kettle black?
Perdoe-me por mencionar isso, mas não é um caso do roto falando do esfarrapado?

It was a bit like the pot calling the kettle black.
Era um pouco como o roto falando do esfarrapado.

You think I’m lazy? That’s like the pot calling the kettle black.
Você acha que eu sou preguiçoso? Isso é como o roto falando do esfarrapado.

It’s very easy to say that, but in your case it’s like the pot calling the kettle black.
É muito fácil dizer isto, mas no seu caso é como o roto falando do esfarrapado.

The political party have just elected a new leader.
O partido político acabou de eleger um novo líder.

There are signs of dissension within the ruling political party.
Há sinais de dissensão dentro do partido político no poder.

A publicly disunited political party stands little chance of winning the election.
Um partido político publicamente desunido tem pouca chance de ganhar a eleição.

The political party that was elected to power has no experience of government.
O partido político que foi eleito ao poder não tem experiência de governo.

There are two political parties in the US – the Democratic Party and the Republican Party.
Existem dois partidos políticos nos EUA – o Partido Democrata e o Partido Republicano.

The committee’s job is to ensure fair play between all the political parties and candidates during the election.
A função do comitê é garantir um jogo limpo entre todos os partidos políticos e candidatos durante a eleição.

The 20th century saw the spread of political parties throughout the entire world.
O século 20 viu a propagação de partidos políticos no mundo inteiro.

Many political parties in developing countries are partly political, partly military.
Muitos partidos políticos de países em desenvolvimento são em parte políticos, em parte militares.

Most political parties have an ideological core.
A maioria dos partidos políticos possuem um núcleo ideológico.

All other political parties there have been completely banned.
Todos os outros partidos políticos lá foram totalmente banidos.

Many countries have several significant political parties but some nations have one-party systems, such as China and Cuba.
Muitos países têm vários partidos políticos importantes, mas algumas nações têm sistemas de partido único, como a China e Cuba.

He opened the book at random.
Ele abriu o livro ao acaso.

We received several answers, and we picked one at random.
Recebemos várias respostas e escolhemos uma ao acaso.

Three people were killed by shots fired at random from a minibus.
Três pessoas foram mortas por tiros disparados ao acaso de um micro-ônibus.

They picked names out of the telephone book at random.
Eles escolheram nomes de uma agenda telefônica ao acaso.

The winning entry will be the first correct answer drawn at random.
A entrada vitoriosa será a primeira resposta correta tirada ao acaso.

By way of comparison, I went to the book shelf and picked out three Ian Fleming books at random.
Para comparar, andei até a prateleira e tirei três livros de Ian Fleming ao acaso.

Study participants were selected at random.
Os participantes do estudo foram selecionados ao acaso.

We wandered aimlessly around Venice.
Vagamos sem rumo por Veneza.

While she waited, she walked aimlessly around the car park.
Enquanto esperava, ela caminhava sem rumo ao redor do estacionamento.

She drove aimlessly for hours.
Ela dirigiu sem rumo por horas.

I’m going out tonight to get drunk.
Eu vou sair hoje à noite e ficar bêbado.

I got completely drunk at my sister’s wedding.
Eu fiquei completamente bêbado no casamento da minha irmã.

They’re not here to party and get drunk.
Eles não estão aqui para festejarem e ficarem bêbados.

If you want to forget about her, just get drunk.
Se você quiser esquecê-la, simplesmente fique bêbado.

Here’s 20 bucks. Take this in case I get drunk and need a cab later.
Aqui estão 20 pratas. Pegue, para o caso de eu ficar bêbado e precisar de um táxi mais tarde.

Tonight, I want to go out and just get wasted.
Hoje à noite, eu quero sair e simplesmente ficar bêbado.

I cannot wait until I’m old enough to get wasted.
Eu mal posso esperar até ter idade suficiente para ficar bêbado.

He got too wasted and couldn’t drive.
Ele ficou bêbado demais e não conseguiu dirigir.

Paula got completely wasted after only one drink.
A Paula ficou completamente bêbada depois de apenas uma bebida.

It’s not a good idea to get hammered at brunch.
Não é uma boa ideia ficar bêbado no brunch.

Man, old Fred got really hammered last night.
Cara, o velho Fred ficou muito bêbado ontem à noite.

I’d rather just hang out at home and get hammered while I watch the game.
Eu preferiria simplesmente ficar em casa e ficar bêbado enquanto assisto ao jogo.

I’m only going to have a beer or two — I don’t want to get plastered.
Eu só vou tomar uma ou duas cervejas ─ eu não quero ficar bêbado.

We got so plastered we had to leave the bar.
Nós ficamos tão bêbados que tivemos que ir embora do bar.

My plan is to deal with this situation by getting plastered.
O meu plano é lidar com essa situação ficando bêbado.

I’ve never seen my dad get plastered. He says he hates getting out of control because of alcohol.
Eu nunca vi o meu pai ficar bêbado. Ele diz que odeia sair do controle por causa do álcool.

He got stoned at the party.
Ele ficou bêbado na festa.

They got stoned and knocked this guy out.
Eles ficaram bêbados e nocautearam esse cara.

Once I got stoned and stared into a mirror for two hours… until I saw someone who looked Chinese.
Uma vez, eu fiquei bêbado e encarei o espelho por duas horas… até que eu vi alguém que parecia chinês.

The driver seemed to be really stepping on it as the bus gained speed very fast.
O motorista parecia estar realmente pisando na tábua, já que o ônibus ganhou velocidade muito rápido.

If we are to get there in time, you better step on it!
Se queremos chegar lá a tempo, é melhor pisar na tábua!

Could you step on it? I’m late.
Você pode pisar na tábua? Estou atrasado.

Take me to the airport, and step on it!
Leve-me para o aeroporto e pise na tábua!

We’ll need to step on it if we’re going to get to the movie on time.
Vamos precisar pisar na tábua se quisermos pegar o filme a tempo.

Step on it or we are going to be late.
Pise na tábua ou então vamos nos atrasar.

You’ll be late if you don’t step on it.
Você vai se atrasar se não pisar na tábua.

We’re late. Come on! Step on it!
Estamos atrasados. Vamos lá! Pé na tábua!

We’ve only got thirty-five minutes so step on it.
Só temos trinta e cinco minutos, então pé na tábua.

If he didn’t drive faster, we were going to be late, so I told him to step on it.
Se ele não dirigisse mais rápido, íamos nos atrasar, então eu disse a ele para pisar na tábua.

Step on the gas, they’re getting away!
Pé na tábua, eles estão escapando!

Step on the gas, will you? We’re going to be late!
Pise na tábua, pode ser? Vamos nos atrasar!

If you don’t step on the gas a bit, we’re going to keep getting passed.
Se você não pisar na tábua um pouco, vamos continuar sendo ultrapassados.

Let’s step on it, or else we’ll never get there in time.
Vamos pisar na tábua, se não nunca vamos chegar lá a tempo.

We need to step on the gas in the second half to keep up with them.
Precisamos pisar na tábua no segundo tempo para não ficar para trás deles. (Como você pode ver aqui, keep up significa “acompanhar”, mas também pode ser traduzido de forma negativa, como acima: “não ficar para trás”.)

I think it’s time to step on the gas with this initiative and really scale it up.
Está na hora de pisar na tábua com essa iniciativa e expandi-la de verdade.

On impulse, Bob decided to buy a car.
Por impulso, o Bob decidiu comprar um carro.

I didn’t need a cell phone. I just bought it on impulse.
Eu não precisava de um celular. Eu simplesmente o comprei por impulso.

I bought this expensive sweater on impulse.
Eu comprei esse suéter caro por impulso.

“I didn’t know you were looking for some new shoes.” “Oh, I wasn’t — I just bought them on impulse.”
“Eu não sabia que você estava procurando sapatos novos.” “Ah, eu não estava – eu apenas os comprei por impulso.”

I understand that you’re dissatisfied with your job, but don’t just quit it on impulse — sleep on it for a few days.
Eu compreendo que você esteja insatisfeito com o seu emprego, mas não peça demissão por impulso ─ pense bem no assunto por alguns dias.

I had always wanted a classic muscle car, so after getting the payout from my insurers I decided to buy one on impulse.
Eu sempre quis ter um muscle car clássico, então, após receber o pagamento da minha seguradora, eu decidi comprar um por impulso.

We booked the trip on a whim.
Nós reservamos a viagem por impulso.

He quit his job on a whim.
Ele pediu demissão do emprego por impulso.

On a whim, we drove to the beach for the weekend.
Por impulso, nós dirigimos até a praia para passar o fim de semana.

Major governmental policies cannot be decided on a whim; they have to be carefully and rationally thought through.
Grandes políticas governamentais não podem ser decididas por impulso; elas precisam ser cuidadosamente e racionalmente ponderadas.

We decided, more or less on a whim, to sail to Morocco.
Nós decidimos, mais ou menos por impulso, velejar ao Marrocos.

You can’t get married on a whim!
Você não pode se casar por impulso!

Profits this year will not meet expectations because of a slowdown in the worldwide economic recovery.
O retorno este ano não atenderá às expectativas devido à desaceleração na recuperação econômica mundial.

Why do projects fail regularly to meet expectations?
Por que projetos regularmente deixam de atender às expectativas? (Note fail to, “deixar de”.)

He did not meet the expectations of his family.
Ele não atendeu às expectativas da sua família.

We’d heard so many good things about the new restaurant, but the food didn’t meet our expectations at all.
Havíamos ouvido tantas coisas boas sobre o novo restaurante, mas a comida não atendeu às nossas expectativas nem um pouco.

I’m so excited for the latest movie in the series — I hope it meets my expectations!
Estou tão empolgado para o último filme da série – espero que atenda às minhas expectativas!

The company failed to match our expectations.
A economia não correspondeu às nossas expectativas.

They’ve placed their hopes on him, but he’s afraid of not being able to meet their expectations.
Eles depositaram suas esperanças nele, mas ele está com medo de não conseguir atender às expectativas deles.

Their trip more than lived up to their expectations.
A viagem deles mais do que esteve à altura das expectativas.

Does the hotel live up to your expectations?
O hotel está à altura das suas expectativas?

The movie failed to live up to my expectations.
O filme não ficou à altura das minhas expectativas.

He’s got a headache and a slight fever.
Ele está com dor de cabeça e um pouco de febre.

It’s an extremely effective cure for a headache.
É uma cura extremamente eficaz para a dor de cabeça.

She didn’t want to go out, so she faked a headache.
Ela não queria sair, então fingiu uma dor de cabeça.

I tried taking tablets for the headache but they didn’t have any effect.
Eu tentei tomar comprimidos para a dor de cabeça, mas eles não fizeram efeito algum.

I had a terrible headache, but even so I went to the concert.
Eu estava com uma dor de cabeça terrível, mas, mesmo assim, fui ao concerto.

I’ve got a splitting headache.
Eu estou com uma dor de cabeça lancinante.

I have had a terrible headache for the last two days.
Eu estive com uma dor de cabeça terrível nos últimos dois dias.

In our sample, a much smaller proportion of men than women reported headaches.
Em nossa amostragem, uma proporção bem menor de homens do que de mulheres relataram dores de cabeça.

This is a real headache for us.
Isso é uma verdadeira dor de cabeça para nós.

Finding a babysitter for Saturday evening will be a major headache.
Encontrar uma babá para sábado à noite será uma grande dor de cabeça.

The airline’s biggest headache is the increase in the price of aviation fuel.
A maior dor de cabeça da companhia aérea é o aumento no preço do combustível de aviação.

Do you suffer from migraines?
Você sofre de enxaqueca?

Considering the amount of stress she’s under, it’s not surprising she keeps getting migraines.
Considerando a quantidade de estresse que ela enfrenta, não surpreende que ela sempre tenha enxaqueca.

Migraine affects three times as many women as men.
A enxaqueca afeta três vezes mais mulheres do que homens.

Her mother suffered from migraines.
A mãe dela sofria de enxaqueca.

I’m meeting her parents tonight, and I have a bad case of butterflies in my stomach.
Vou conhecer os pais dela hoje à noite e estou com um sério frio na barriga. (A bad case of é um jeito de dizer que uma doença ou sensação, geralmente nervosismo ou ansiedade, é séria. Em português, creio que soa um pouco esquisito dizer “um caso de”, então a tradução muda um pouco.)

I had terrible butterflies before I gave that talk in Venice.
Eu estava com um frio terrível na barriga antes de fazer aquela fala em Veneza. (Às vezes, como você vê, pode-se dizer to have butterflies, sem mencionar in one’s stomach.)

The butterflies in my stomach almost kept me from going on stage and performing.
O frio na barriga quase me impediu de subir ao palco e apresentar.

Whenever I have to speak in public, I get butterflies in my stomach.
Sempre que tenho de falar em público, fico com um frio na barriga.

She always has butterflies in her stomach before a test.
Ela sempre fica com um frio na barriga antes de uma prova.

It was not frightening enough to give me butterflies in my stomach, but it made me a little apprehensive.
Não era assustador o suficiente para me dar um frio na barriga, mas me deixou um pouco apreensivo.

I always get butterflies in my stomach before making a speech.
Eu sempre fico com um frio na barriga antes de fazer um discurso.

I’m starting to feel the butterflies in my stomach already.
Já estou começando a sentir um frio na barriga.

An exam, or even an exciting social event may produce butterflies in the stomach.
Uma prova, ou mesmo um evento social empolgante, pode gerar um frio na barriga.

He had butterflies in his stomach on the morning of his wedding.
Ele estava com um frio na barriga na manhã do seu casamento.

Kevin had butterflies in his stomach every time he saw her.
Kevin sentia um frio na barriga toda vez que a via.

Everytime I look at her I get butterflies in my stomach.
Toda vez que olho para ela, sinto um frio no estômago.

She felt butterflies in her stomach whenever he was around.
Ela sentia um frio no estômago sempre que ele estava por perto.

– I just heard that Janet broke up with you. That’s hard luck, buddy.
– Acabei de ouvir que a Janet terminou com você. Que azar, cara.

– Failed again, I’m afraid. – Oh, hard luck.
– Falhei uma vez mais, infelizmente. – Ah, que azar.

– I failed my driving test. – Oh, hard luck!
– Não passei no meu teste de direção. – Ah, que azar!

Hard luck, chaps. But that happens, don’t despair too much.
Que azar, camaradas. Mas isto acontece, não se desesperem demais.

– We lost again. – Oh, hard luck!
– Perdemos de novo. – Ah, que azar!

You lost your job? Oh, tough luck.
Você perdeu seu emprego? Ah, que azar.

– They lost a lot of money on their investment. – Tough luck – they should have been more careful.
– Eles perderam muito dinheiro no investimento. – Que azar – mas eles deviam ter sido mais cuidadosos.

You didn’t get the job? Oh, tough luck!
Você não conseguiu o emprego? Ah, que azar!

– I think I’ve damaged my back. – Oh, bad luck!
– Acho que prejudiquei as costas. – Ah, que azar.

– I was up two pawns and had a winning advantage, but blundered it all in one move. – Tough luck!
– Eu estava com dois peões a mais e tinha uma vantagem decisiva, mas pus tudo a perder em um lance. – Que azar!

She wrote dull articles for the local newspaper.
Ela escrevia artigos sem graça para o jornal local.

He’s a pleasant man, but deadly dull.
Ele é um homem agradável, mas extremamente sem graça.

I find his art rather dull and conventional.
Eu acho a arte dele bem sem graça e convencional.

For years, he’s plodded away at the same dull job.
Por anos, ele labutou no mesmo trabalho sem graça.

Those books seem rather dull beside this one.
Aqueles livros parecem muito sem graça perto desse.

The ponderous reporting style makes the evening news dull viewing.
O enfadonho estilo de reportagem faz o noticiário da noite ficar sem graça de assistir.

I felt she found me boring and dull.
Eu senti que ela me achou tedioso e sem graça.

The documentary lasts for more than two and a half hours, and there is scarcely a dull minute.
O documentário dura mais de duas horas e meia e mal contém um minuto sem graça.

She felt embarrassed about undressing in front of the doctor.
Ela se sentiu sem graça de tirar a roupa na frente do médico.

I was too embarrassed to admit that I was scared.
Eu estava sem graça demais para admitir que estava com medo.

You have no idea how embarrassed I was.
Você não faz ideia do quanto eu estava sem graça.

He was so embarrassed – his face went brick-red.
Ele ficou tão sem graça – seu rosto ficou vermelho.

She looked a bit embarrassed by all the praise.
Ela parecia um pouco sem graça com todos os elogios.

I was too embarrassed to admit that I’d forgotten.
Eu estava sem graça demais para admitir que eu havia esquecido.

I’ve never been so embarrassed in my life.
Eu nunca fiquei tão sem graça na minha vida.

She was too embarrassed to ask for help.
Ela estava sem graça demais para pedir ajuda.

As a rule, I stay in on Friday nights.
Por via de regra, eu fico em casa nas noites de sexta-feira.

As a rule, Irene does not eat meat.
Por via de regra, a Irene não come carne.

As a rule, however, such attacks have been aimed at causing damage rather than taking life.
Por via de regra, entretanto, tais ataques visavam mais causar danos do que tirar a vida.

My mother always makes extra food for family dinners, as a rule.
A minha mãe sempre faz comida extra para os jantares de família, por via de regra.

As a rule, things tend to get less busy after supper time.
Por via de regra, as coisas costumam ficar menos agitadas depois da hora do jantar.

As a rule, men should wear tuxedos at formal dinners.
Por via de regra, os homens devem usar ternos em jantares formais.

As a rule, the bus picks me up at 7:30 every morning.
Por via de regra, o ônibus me pega às 7:30 toda manhã.

It’s lucky for you that I’m still awake. As a rule, I’m in bed by eleven.
Sorte sua que eu ainda estou acordado. Por via de regra, eu estou na cama às onze.

As a rule, we take the bus.
Por via de regra, nós vamos de ônibus.

As a general rule, I don’t read detective novels.
Por via de regra, eu não leio romances policiais.

As a general rule, we don’t allow children in here.
Por via de regra, nós não permitimos crianças aqui.

As a general rule, I won’t sit in the window seat on an airplane. I get too anxious watching the ground below disappear!
Por via de regra, eu não me sento no assento da janela em um avião. Eu fico muito ansioso assistindo ao chão abaixo desaparecer!

He can be found in his office, as a general rule.
Ele pode ser encontrado em seu escritório, por via de regra.

As a general rule, Jane plays golf on Wednesdays.
Por via de regra, a Jane joga golfe às quartas-feiras.

To tell the truth, I couldn’t hear a word he said.
Para dizer a verdade, não consegui ouvir uma palavra do que ele disse.

I didn’t really like the movie, to tell the truth.
Eu não gostei muito do filme, para dizer a verdade.

I don’t really want to go out, to tell the truth.
Não quero muito sair, para falar a verdade.

To tell you the truth, I’m completely bored.
Para falar a verdade, estou totalmente entediada.

To tell you the truth, I was afraid to see him.
Para dizer a verdade, eu estava com medo de vê-lo.

Truth to tell, John did not want Veronica at his wedding.
A bem dizer, John não queria a Veronica no casamento dele.

Truth be told, the food was pretty bad.
Verdade seja dita, a comida era bem ruim.

Truth be told, even though I majored in English literature, I’ve never read anything by Hemingway!
Verdade seja dita, embora eu tenha me especializado em literatura inglesa, eu nunca li nada de Hemingway!

I know I said I wanted to go out to the bars tonight, but if the truth be told, I’d rather just stay home and watch a movie.
Eu sei que eu disse que queria ir para os bares hoje à noite, mas para dizer a verdade eu preferia só ficar em casa e assistir a um filme.

I’m not sure if I can do this, truth be told.
Não tenho certeza se posso fazer isso, para dizer a verdade.

Actually, truth be told, I just don’t like you.
Na realidade, verdade seja dita, eu simplesmente não gosto de você.

If truth be told, I’ve never really liked David’s wife.
Verdade seja dita, eu nunca gostei muito da esposa do David.

I personally would have loved it.
Eu, pessoalmente, teria amado isso.

I personally think it’s too cold to go out.
Eu, pessoalmente, acho que está frio demais para sair.

I personally prefer pizza to burgers.
Eu, pessoalmente, prefiro pizza do que hambúrguer.

I personally think their marriage won’t last.
Eu, pessoalmente, acho que o casamento deles não vai durar.

I personally think we should stick with our original plan.
Eu, pessoalmente, acho que nós deveríamos manter o nosso plano original.

She’s a very talented young singer, and I personally think she’s going places!
Ela é uma jovem cantora muito talentosa e eu, pessoalmente, acho que ela vai longe!

The rest of you may disagree, but I, for one, think we should go ahead with the project.
O resto de vocês pode discordar, mas eu, pessoalmente, acho que nós deveríamos prosseguir com o projeto.

I, for one, hope you don’t get the job.
Eu, pessoalmente, espero que você não consiga o emprego.

He doesn’t like their behavior, and I for one agree with him.
Ele não gosta do comportamento deles e eu, pessoalmente, concordo com ele.

I for one do not like the idea of trying to sell second-rate goods.
Eu, pessoalmente, não gosto da ideia de tentar vender mercadorias de segunda categoria.

It’s getting late and I, for one, must be going.
Está ficando tarde e eu, pessoalmente, preciso ir embora.

Nothing has been proved yet, and I for one believe that he is innocent.
Nada foi aprovado ainda, e eu, pessoalmente, acredito que ele seja inocente.

I can tell you that I for one am really happy about the changes to the tax law they’ve introduced.
Eu posso lhe dizer que eu, pessoalmente, estou muito feliz com as mudanças na legislação fiscal que eles introduziram.

I am studying English, as always! (I am studying English, as usual!)
Eu estou estudando inglês, como sempre!

As always, dinner was delicious.
Como sempre, o jantar estava delicioso.

Your children, as always, were very well-behaved.
Os seus filhos, como sempre, foram muito bem-comportados.

As always, her father was there to meet her.
Como sempre, o pai dela estava lá para se encontrar com ela.

As always, I think that consumers are looking for a product that tastes good.
Como sempre, eu acho que os consumidores estão procurando um produto que seja saboroso.

We’ll give you the facts, as always.
Nós lhe apresentaremos os fatos, como sempre.

The truth, as always, is more complicated.
A verdade, como sempre, é mais complicada.

As always, Deborah was the last to arrive.
Como sempre, a Deborah foi a última a chegar.

As usual, she was wearing jeans.
Como sempre, ela estava usando jeans.

Dan got there late, as usual.
O Dan chegou lá atrasado, como sempre.

As usual, there will be the local and regional elections on June the twelfth.
Como sempre, as eleições locais e regionais ocorrerão em doze de junho.

The headlines are, as usual, a mixture of domestic and foreign news.
As manchetes são, como sempre, uma mistura de notícias nacionais e internacionais.

When somebody died, everything went on as usual, as if it had never happened.
Quando alguém morria, tudo continuava como sempre, como se aquilo nunca tivesse acontecido.

Sam is ignoring me, as usual. I wonder if he’ll ever forgive me.
O Sam está me ignorando, como sempre. Eu me pergunto se ele me perdoará algum dia.

The writers’ group is meeting at the coffee shop on Saturday morning, as usual.
O grupo de escritores se reunirá na cafeteria no sábado de manhã, como sempre.

She’d been late for work every morning and I thought I’d better have it out with her.
Ela havia se atrasado para o trabalho toda manhã e eu achei que era melhor tirar satisfações com ela.

I had to have it out with my roommate because he never does his share of cleaning in the house.
Eu tive de tirar satisfações com o meu companheiro de quarto, porque ele nunca faz a parte dele na limpeza da casa.

John has been mad at Mary for a week. He finally had it out with her today.
O John esteve furioso com a Mary por uma semana. Ele finalmente tirou satisfações com ela hoje.

You must stop ignoring Fred because of what he said, and have it out with him once and for all.
Você precisa parar de ignorar o Fred por causa do que ele disse e tirar satisfações com ele de uma vez por todas.

Give her the chance of a night’s rest before you have it out with her.
Dê a ela a chance de descansar uma noite antes de você tirar satisfações com ela.

Why not have it out with your critic, discuss the whole thing face to face?
Por que não tirar satisfações com os seus críticos, discutir a coisa toda cara a cara?

He decided to have it out with Rose there and then.
Ele decidiu tirar satisfações com a Rose ali mesmo.

I’m going round to his house to have it out with him.
Vou até a casa dele para tirar satisfações com ele.

I think it’s about time we have it out with him.
Acho que está na hora de tirarmos satisfações com eles.

Tom and his girlfriend are always having it out.
O Tom e sua namorada estão sempre discutindo.

By giving out printed sheets of facts and theories, the teachers spoon-fed us with what we needed for the exam.
Distribuindo folhas impressas com os fatos e teorias, os professores nos deram mastigado aquilo de que precisávamos para a prova. 

Some students are unwilling to really work. They want to be spoon-fed.
Alguns alunos não querem se esforçar de verdade. Eles querem receber tudo mastigado.

They’ve been spoon-fed, provided with a house, servants, bank balance.
Eles receberam tudo mastigado, foram providenciados com casa, servos, saldo bancário.

Her students are lazy because she always spoon-feeds them the answers.
Os alunos dela são preguiçosos, porque ela sempre dá as respostas mastigadas para eles.

You mustn’t spoon-feed the new recruits by telling them what to do all the time. They must use their initiative.
Você não deve dar tudo mastigado para os novos recrutas, dizendo a eles o que fazer o tempo todo. Eles precisam usar a própria iniciativa.

I don’t believe in spoon-feeding students.
Eu não acredito em dar tudo mastigado para os alunos.

Certain people enjoy finding out things for themselves; others prefer being spoon-fed.
Certas pessoas gostam de descobrir as coisas por conta própria; outras, preferem receber tudo mastigado.

Teachers should avoid spoon-feeding facts to students.
Os professores deveriam evitar dar os fatos mastigados para os alunos.

I prefer to learn by myself, and not have everything spoon-fed to me.
Eu prefiro aprender por mim mesmo, e não ter tudo dado mastigadinho.

The problem with having information spoon-fed to you is that it kills creativity and the ability to think by oneself.
O problema de ter a informação dada mastigadinha para você é que isso mata a criatividade e a capacidade de pensar por conta própria.

He had the press eating out of his hand.
Ele tinha a imprensa comendo na palma da sua mão.

She usually has the guys eating out of her hand.
Ela geralmente tem os caras comendo na palma da sua mão.

I’ve got her eating out of my hand. She’ll do anything I ask.
Eu tenho ela comendo na palma da minha mão. Ela fará qualquer coisa que eu pedir.

He will be eating out of your hand before you are finished with him.
Ele estará comendo na palma da sua mão antes de você ter terminado com ele.

You can tell the candidate has his followers eating out of his hand — they’ll believe anything he says.
Dá pra notar que o candidato tem os seus partidários comendo na palma da sua mão ─ eles acreditarão em qualquer coisa que ele disser.

Within two minutes of walking into the classroom, she had the kids eating out of her hand.
Dentro de dois minutos após entrar na sala de aula, ela tinha as crianças comendo na palma da sua mão.

He soon had the client eating out of his hand.
Ele logo tinha o cliente comendo na palma da sua mão.

He’s brilliant in job interviews ─ he always manages to get the interviewer eating out of his hand.
Ele é brilhante em entrevistas de emprego ─ ele sempre consegue ter o entrevistador comendo na palma da sua mão.

I introduced him to my mother, and within minutes she had him eating out of her hand.
Eu o apresentei para a minha mãe e, em questão de minutos, ela tinha ele comendo na palma da sua mão.

Most women have their husbands eating out of their hands.
A maioria das mulheres têm os seus maridos comendo na palma das suas mãos.

The guys have the crowd eating out of their hand right away making a few jokes.
Os caras têm a multidão comendo na palma das suas mãos imediatamente, fazendo algumas piadas.

We don’t have any flour left, as far as I remember, but you can check in the closet.
Não temos mais farinha, que eu me lembre, mas você pode verificar no armário.

As far as I remember, we need this part of the project done by Wednesday.
Que eu me lembre, precisamos que esta parte do projeto seja completada até a quarta-feira.

As far as I can remember, their wedding was in 1983, but maybe it was a little earlier.
Que eu me lembre, o casamento deles foi em 1983, mas talvez tenha sido um pouco antes.

As far as I recall, she has never explicitly stated that she wants to become Prime Minister.
Que eu me lembre, ela nunca declarou expressamente que quer ser primeira ministra.

– Have you seen this place before? – No, not as far as I recall.
– Você já viu esse lugar antes? – Não, não que eu me lembre.

That’s not what they said, as far as I recall.
Não foi isso o que eles disseram, pelo que eu me lembro.

To the best of my recollection, she drives a Mercedes.
Que eu me lembre, ela dirige uma Mercedes.

To the best of my recollection no one ever had a bad word to say about him.
Que eu me lembre, ninguém nunca teve algo ruim a dizer sobre ele.

To the best of my recollection I have never seen her before.
Que eu me lembre, eu nunca a vi antes.

He knows the history of the matter, and he has given the facts, to the best of my recollection, with complete accuracy.
Ele sabe a história da questão e ele deu os fatos, pelo que me lembro, com total precisão.

No one, to my recollection, gave a second thought to the risks involved.
Ninguém, pelo que me lembro, pensou duas vezes sobre os riscos envolvidos.

He was shot for breaking the curfew.
Ele foi baleado por violar o toque de recolher.

We do not keep records of the length of previous curfews.
Nós não mantemos registros da duração de toques de recolher anteriores.

The village was placed under curfew.
A aldeia foi colocada sob toque de recolher.

Crowds of people defied the curfew to celebrate on the streets.
Multidões de pessoas desafiaram o toque de recolher para comemorar nas ruas.

He was also given a suspended jail sentence and night curfew.
Ele também recebeu uma pena suspensa e um toque de recolher noturno.

He is free to come and go during the day but has to observe a curfew at night.
Ele é livre para ir e vir durante o dia, mas precisa obedecer a um toque de recolher à noite.

The crowd begins slowly to disperse under the impatient eyes of police officers imposing a city curfew.
A multidão começa lentamente a se dispersar sob o olhar impaciente dos policiais que impunham um toque de recolher na cidade.

The city ordered a curfew to prevent further rioting.
A cidade decretou toque de recolher para evitar mais tumultos.

The authorities declared a state of emergency and imposed a curfew.
As autoridades declararam estado de emergência e impuseram um toque de recolher.

The accused is under a curfew from 8 pm till 6 am.
O acusado está sob um toque de recolher das 8 da noite até as 6 da manhã.

The curfew was lifted on May 6th.
O toque de recolher foi revogado em 6 de maio.

Anyone found in the streets after curfew was shot.
Qualquer um encontrado nas ruas após o toque de recolher era baleado.

I wish you well in your new job.
Eu lhe desejo tudo de bom no seu novo emprego.

The crowd wished them well as they left for their honeymoon.
A multidão lhes desejou tudo de bom enquanto eles partiam para a sua lua-de-mel.

The breakup was hard, but there was no animosity on either side; I genuinely wish him well.
O término foi difícil, mas não havia hostilidade de nenhum dos lados; eu genuinamente desejo tudo de bom para ele.

On behalf of everyone here, let me say that we wish you well in your adventure to Japan.
Em nome de todos aqui, permita-me dizer que nós lhe desejamos tudo de bom em sua aventura ao Japão.

We wish you all the best in your new job in Europe.
Nós lhe desejamos tudo de bom em seu novo emprego na Europa.

Wish him all the best, and tell him we miss him.
Deseje-lhe tudo de bom, e diga-lhe que nós estamos com saudade dele.

We’d just like to wish him all the best in his new job.
Gostaríamos apenas de desejar a ele tudo de bom em seu novo trabalho.

I wish you all the best for the coming year.
Eu lhe desejo tudo de bom no ano vindouro.

I wish all the best in your future endeavours.
Eu lhe desejo tudo de bom em seus futuros empreendimentos.

We’re sorry that you’re leaving, and we wish you the best of luck in your new job.
Nós lamentamos que você esteja indo embora e lhe desejamos tudo de bom em seu novo emprego.

He kissed her on the cheek. “I wish you the best of luck!”
Ele a beijou na bochecha. “Eu lhe desejo tudo de bom!”

I wish you the best of luck in your new endeavor — we’ll miss you around the office.
Eu lhe desejo tudo de bom em seu novo empreendimento ─ nós sentiremos sua falta no escritório.

The British upper class is no longer very rich.
A classe alta britânica não é muito rica mais.

The upper classes usually send their children to expensive private schools.
As classes altas geralmente mandam seus filhos para escolas particulares caras.

Those goods were specifically designed to appeal to the tastes of the upper class.
Aquelas mercadorias foram especificamente projetadas para agradar aos gostos da classe alta.

She comes from an upper-class family.
Ela vem de uma família de classe alta.

He grew up in an upper-class neighborhood in Cairo.
Ele cresceu em um bairro de classe alta em Cairo.

The country’s economic problems have affected the middle class most strongly.
Os problemas econômicos do país afetaram a classe média mais fortemente.

I’m studying the expansion of the middle class in the late 19th century.
Eu estou estudando a expansão da classe média no final do século 19.

The President may have secured some support from the middle classes.
O presidente pode ter adquirido algum apoio das classes médias.

Middle-class children have more advantages.
Crianças de classe média têm mais vantagens.

They shop at a middle-class supermarket that sells dozens of different varieties of olives and fresh pasta.
Eles compram em um supermercado de classe média que vende dezenas de variedades diferentes de azeitonas e massas frescas.

He’s a member of the lower class.
Ele é membro da classe baixa.

Education now offers the lower classes access to job opportunities.
A educação agora oferece às classes baixas acesso a oportunidades de trabalho.

Horse-racing was once considered vulgar and lower-class in Japan.
As corridas de cavalo já foram consideradas vulgares e de classe baixa no Japão.

They provided lower-class women with dignified employment.
Eles forneciam às mulheres de classe baixa trabalho digno.

He claims his flat-tax proposal would help middle-class and lower-class Americans.
Ele alega que a sua proposta de imposto único ajudaria os americanos de classe média e de classe baixa.

She described the brutal realities of lower-class life during the Depression.
Ela descreveu as realidades cruéis da vida de classe baixa durante a Depressão.

The long-term unemployed now constitute a kind of underclass.
Os desempregados há muito tempo constituem agora um tipo de classe baixa.

Letting guest workers into America doesn’t create an underclass.
Deixar trabalhadores estrangeiros entrar na América não cria uma classe baixa.

The nation needs to reduce the vast gap between the wealthy and the jobless underclass.
A nação precisa reduzir o enorme abismo entre os ricos e a classe baixa desempregada.

Johnson belongs to a new and growing underclass who work inside some of the world’s wealthiest companies.
O Johnson pertence a uma nova e crescente classe baixa que trabalha dentro de algumas das empresas mais ricas do mundo.

The basic problems of the inner-city underclass are inadequate housing and lack of jobs.
Os problemas básicos da classe baixa urbana são moradia inadequada e falta de empregos.

You can fundraise for any charitable cause.
Você pode arrecadar fundos para qualquer causa beneficente.

Those communities fundraised to help their own members after the tragedy.
Aquelas comunidades arrecadaram fundos para ajudar os seus próprios membros após a tragédia.

During his recovery, he decided to fundraise for a cancer charity.
Durante a sua recuperação, ele decidiu arrecadar fundos para uma instituição de caridade para o câncer.

Candidates from both political parties will continue to fundraise regardless of outside events.
Candidatos de ambos os partidos políticos continuarão a arrecadar fundos independentemente de eventos externos.

I’d fundraised in my private life, so it seemed obvious to do it professionally.
Eu havia arrecadado fundos na minha vida privada, então pareceu óbvio fazer isso profissionalmente.

After his retirement, he continued to fundraise for the Democratic Party.
Depois da sua aposentadoria, ele continuou a arrecadar fundos para o Partido Democrático.

His bucket list included some really funny and imaginative ways to fundraise.
A sua lista de coisas a fazer antes de morrer incluía algumas maneiras bem engraçadas e criativas de arrecadar fundos.

We managed to raise money through sponsored events.
Nós conseguimos arrecadar fundos através de eventos patrocinados.

We need your help to raise money for urgent medical research.
Nós precisamos da sua ajuda para arrecadar fundos para pesquisas médicas urgentes.

I want to start my own business if I can raise enough money.
Eu quero começar o meu próprio negócio, se eu conseguir arrecadar fundos suficientes.

We will raise funds for reconstruction by disposing of assets.
Nós iremos arrecadar fundos para a reconstrução nos desfazendo de ativos.

The coffee company aims to raise funds from investors eager to invest in ethical concerns.
A empresa de café visa arrecadar fundos de investidores ansiosos para investir em questões éticas.

All funds raised will be used by Children With Leukaemia.
Todos os fundos arrecadados serão usados pela Crianças Com Leucemia.

Her brother definitely has a screw loose – I don’t really trust him.
Com certeza, o irmão dela tem um parafuso a menos – eu não confio muito nele.

My sister looked at me as if I had a screw loose.
A minha irmã olhou para mim como se eu tivesse um parafuso a menos.

That guy on the corner must have a screw loose or something, because he’s been standing out there yelling obscenities at passersby all morning.
Aquele sujeito na esquina deve ter um parafuso a menos ou algo assim, porque ele tem estado ali gritando obscenidades para os transeuntes a manhã toda.

My old uncle Pete has a few screws loose, but he’s a really nice guy.
Meu velho tio Pete tem alguns parafusos a menos, mas é um cara muito legal.

What’s the matter with you? Do you have a screw loose, or what?
Qual é o problema com você? Você tem um parafuso a menos ou o quê?

He’s sort of strange. I think he’s got a loose screw.
Ele é um tanto estranho. Acho que ele tem um parafuso a menos.

He must have a screw loose, spending that sort of money on a holiday!
Ele deve ter um parafuso a menos, gastando tanto dinheiro em um feriado! (That sort of money é um jeito de se referir a “muito dinheiro”.)

He dresses his cats up in little coats for the winter. Sometimes I think he must have a screw loose.
Ele veste seus gatos com pequenos casacos no inverno. Às vezes, acho que falta um parafuso a ele.

Yes, he has a screw loose somewhere. He wears a heavy jacket in the middle of summer.
Sim, ele tem um parafuso a menos em algum lugar. Ele usa uma jaqueta pesada no meio do verão.

Under no circumstances are you to go out.
Sob hipótese alguma você pode sair.

Under no circumstances will I let you go out.
Sob hipótese alguma eu deixarei você sair.

Under no circumstances will I allow you to go to a party on a school night.
Sob hipótese alguma eu te deixarei ir a uma festa tendo aula no dia seguinte.

“Under no circumstances will I ever go back there again!” “Why? What happened?”
“Sob hipótese alguma eu jamais voltarei lá novamente!” “Por quê? O que aconteceu?”

Under no circumstances should you lend Paul any money.
Sob hipótese alguma você deve emprestar dinheiro ao Paul.

The proceedings can be reported but under no circumstances may any child involved in the proceedings be identified.
As medidas judiciais podem ser relatadas, mas sob hipótese alguma qualquer criança envolvida nas medidas judiciais pode ser identificada.

Under no circumstances must I mention to anyone that I have turned down that invitation.
Sob hipótese alguma eu devo mencionar a qualquer um que eu recusei aquele convite.

Under no circumstances should you see them again.
Sob hipótese alguma você deve vê-los novamente.

Tears must not be allowed to fill their eyes and under no circumstances run down their cheeks.
Não se deve permitir que lágrimas encham os seus olhos e, sob hipótese alguma, que escorram em suas bochechas.

In no circumstances are you allowed to drive home after you’ve had more than one drink!
Sob hipótese alguma você tem permissão de dirigir para casa após ter tomado mais de uma bebida!

I’m sorry for my sudden resignation, but in no circumstances will I work for some sexist manager like him.
Sinto muito pelo meu pedido de demissão repentino, mas sob hipótese alguma eu trabalharei para um gerente sexista como ele.

In no circumstances should I be responsible for your reckless driving of my vehicle.
Sob hipótese alguma eu devo ser responsável por sua condução imprudente do meu veículo.

“Can I talk you into serving as a referee again?” “Heavens, no! In any circumstances!”
“Eu consigo te convencer a servir como árbitro novamente?” “Céus, não! Sob hipótese alguma!”

Do not, under any circumstances, eat that cake. It’s for tomorrow’s party.
Não coma, sob hipótese alguma, aquele bolo. É para a festa de amanhã.

And you may not, under any circumstances, administer medications.
E você não pode, sob hipótese alguma, administrar medicamentos.

Don’t open the door to strangers under any circumstances.
Não abra a porta para estranhos sob hipótese alguma.

    """

    # Nome do arquivo CSV
    nome_arquivo = "frases_traducao.csv"

    # Processar a entrada para obter os pares
    pares = processar_entrada(texto)

    # Criar o arquivo CSV
    criar_csv(pares, nome_arquivo)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")