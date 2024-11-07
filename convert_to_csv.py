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
I’ll go see if I can persuade the committee — they hold me in high regard.
Vou ver se consigo persuadir o comitê – eles me têm em alta conta.

I’ve always held my father in high regard for his hard work to provide for us.
Sempre tive meu pai em alta conta pelo duro esforço em prover para nós.

All of us hold the vice president in high regard.
Todos nós temos o vice-presidente em alta conta.

We hold these policies in high regard.
Temos estas políticas em alta conta.

I hold you in the highest regard.
Eu o tenho na maior estima.

The students have a high regard for their teacher.
Os alunos têm um grande apreço pelo professor.

I have a very high regard for him and what he has achieved.
Eu tenho um grande apreço por ele e por aquilo que ele alcançou.

There were armed people about, people with little regard for human life.
Havia pessoas armadas por ali, pessoas com pouca consideração pela vida humana.

The Party ruled the country without regard for the people’s views.
O Partido governava o país sem consideração pelos pontos de vista das pessoas.

I have no regard for his opinions.
Eu não tenho respeito pelas opiniões dele.

Sending money the old-fashioned way means it can get lost in the mail.
Enviar dinheiro à moda antiga significa que ele pode ser extraviado.

These sweets are still made in the old-fashioned way.
Esses doces ainda são feitos à moda antiga.

The job was done the old-fashioned way, with teamwork, better quality and new models that appeal to customers.
O serviço foi feito à moda antiga, com trabalho de equipe, melhor qualidade e modelos novos que atraem os consumidores.

They beat the other team the old-fashioned way.
Eles derrotaram o outro time à moda antiga.

We should get the truth out of him the old-fashioned way.
Nós deveríamos arrancar a verdade dele à moda antiga.

The doctors took care of her the old-fashioned way.
Os médicos cuidaram dela à moda antiga.

Maybe we should try to do this the old-fashioned way.
Talvez nós devêssemos tentar fazer isso à moda antiga.

I believe that procreation should happen the old-fashioned way.
Eu acredito que a procriação deveria acontecer à moda antiga.

I guess I could just seduce her the old-fashioned way.
Acho que eu poderia simplesmente seduzi-la à moda antiga.

If she doesn’t call us after 5 minutes, we’ll do it the old-fashioned way.
Se ela não nos ligar em 5 minutos, nós faremos isso à moda antiga.

Either we maintain our command structure or else we settle our differences the old-fashioned way.
Ou nós mantemos a nossa estrutura de comando, ou então nós resolvemos as nossas diferenças à moda antiga.

Good old John: you can always count on him to help.
O bom e velho John: você sempre pode contar com ele para ajudar.

I don’t need fancy shoes. I prefer good old sneakers.
Eu não preciso de sapatos chiques. Eu prefiro os bons e velhos tênis.

There is nothing wrong with good old cauliflower cheese.
Não há nada de errado com uma boa e velha couve-flor gratinada.

Good old Margaret, she’s always there when you need her.
A boa e velha Margaret, ela está sempre lá quando você precisa dela.

Good old Harry. Reliable to the end.
O bom e velho Harry. Confiável até o fim.

If you need excitement and a good old dose of adrenalin, then the Ducati is a top option.
Se você precisa de emoção e de uma boa e velha dose de adrenalina, então a Ducati é a melhor opção.

Our only hope is a good old winter storm over the Christmas holiday.
A nossa única esperança é uma boa e velha tempestade de inverno durante o Natal.

I wish my grandma would stop going on about the good old days.
Eu queria que a minha vó parasse de falar sobre os bons e velhos tempos.

They were talking about the good old days.
Eles estavam conversando sobre os bons e velhos tempos.

In the 1960s, everything seemed possible. Those were the good old days.
Nos anos 60, tudo parecia possível. Aqueles eram os bons e velhos tempos.

They loved to sit and chat about the good old days.
Eles amavam sentar e conversar sobre os bons e velhos tempos.

I married my soulmate, you don’t get much luckier than that.
Casei-me com minha alma gêmea, é difícil ter mais sorte do que isso!

Later that year she met Adam and she knew instantly that they were soulmates.
Mais tarde naquele ano ela encontrou Adam, e percebeu instantaneamente que eles eram almas gêmeas.

They are a husband and wife who are perfect soulmates.
Eles são um homem e mulher que são almas gêmeas perfeitas.

They are ideological soulmates.
Ideologicamente, eles são almas gêmeas.

Steve and I became soulmates, near-constant companions.
Steve e eu viramos almas gêmeas, companheiros quase que constantes.

When it comes to chess, we are soulmates. We like the same openings, we play the same attacking style.
No que se refere ao xadrez, somos almas gêmeas. Gostamos das mesmas aberturas, jogamos o mesmo estilo de ataque.

I longed to find a kindred spirit.
Eu ansiava encontrar uma alma gêmea.

How could I recognise a kindred spirit, a possible friend?
Como eu podia reconhecer uma alma gêmea, um possível amigo?

When I saw his work for the first time, I recognized a kindred spirit.
Quando vi a obra dele pela primeira vez, reconheci uma alma gêmea.

He told her they were kindred spirits and were fated to fall in love.
Ele disse a ela que eles eram almas gêmeas e destinados a se apaixonar.

We are kindred spirits.
Somos almas gêmeas.

We recognized each other as kindred spirits as soon as we met.
Reconhecemo-nos como almas gêmeas assim que nos conhecemos.

It was just as well I didn’t know at the time.
Ainda bem que eu não sabia na época.

It’s just as well she didn’t get that job, since she will now be closer to home.
Ainda bem que ela não conseguiu aquele emprego, já que agora ela vai ficar mais perto de casa.

I really didn’t want to stay home this weekend, but it’s just as well. I have a lot to do.
Eu realmente não queria ficar em casa esse final de semana, mas ainda bem. Tenho um monte de coisa para fazer.

It’s beginning to rain – it’s just as well that we brought our umbrellas.
Está começando a chover – ainda bem que trouxemos nossos guarda-chuvas.

It’s a good thing we brought some food with us.
Ainda bem que trouxemos comida conosco.

It’s a good thing this happened now, before it’s too late.
Ainda bem que isto aconteceu agora, antes que seja tarde demais.

Good thing they didn’t go camping last weekend – the weather was terrible.
Ainda bem que eles não foram acampar no final de semana passada – o tempo estava terrível.

It’s a good thing you called – Mom was starting to get worried.
Ainda bem que você ligou – a mãe estava começando a ficar preocupada.

It’s a good job I remembered to bring an umbrella.
Ainda bem que eu lembrei de trazer um guarda-chuva.

It’s a good job you aren’t married.
Ainda bem que você não está casado.

It’s a good job it happened here rather than on the open road.
Ainda bem que isso aconteceu aqui, e não na estrada aberta.

All right… you’re the boss.
Está bem… você é quem manda.

– Let’s continue working on this tomorrow. Time to go home now.
– OK, you’re the boss.

– Vamos continuar trabalhando nisso amanhã. Agora está na hora de ir para casa.
– OK, você é quem manda.

Well, if you say so, let’s do it. You’re the boss!
Bem, se é assim vamos em frente. Você é quem manda.

I think that if we’re going to do this we should make sure we get official permission, but you’re the boss.
Acho que, se formos fazer isso, deveríamos garantir que temos uma permissão oficial, mas você é quem manda.

Well, you’re the boss, I suppose… just don’t blame me if this doesn’t go down well.
Bem, é você quem manda, imagino… só não me culpe se isso não der certo.

Well, you’re the boss. Let’s get down to business, then.
Bem, é você quem manda. Vamos direto ao que importa, então.

Well, you’re the boss — whatever you say goes.
Bem, é você quem manda – o que você disser vale.

Are you sure you want to do this? Yes? Well, you’re the boss. Let’s do it.
Tem certeza de que você quer fazer isso? Sim? Bem, você é quem manda. Vamos lá.

If you really want to do this, let’s go ahead and do it. You’re the boss.
Se você realmente quer fazer isso, vamos em frente. É você quem manda.

Whatever you say – you’re the boss.
O que você disser – é você quem manda.

No offense, but I think you are mistaken.
Sem ofensas, mas eu acho que você está enganado.

Dad, you need a bath. No offence.
Pai, você precisa de um banho. Sem ofensas.

I’m not sure you’re the best person for the job. No offense, Charlie.
Eu não tenho certeza de que você é a melhor pessoa para o serviço. Sem ofensas, Charlie.

No offence, but I think it may be time you cleaned up your kitchen.
Sem ofensas, mas eu acho que talvez esteja na hora de você arrumar a sua cozinha.

All I’m saying is that I think we could use some more help with the renovation. No offense, John, you’ve been a big help.
Só estou dizendo que eu acho que precisamos de mais ajuda com a reforma. Sem ofensas, John, você tem ajudado muito.

No offense, but I’d really like to be on my own.
Sem ofensas, mas eu realmente gostaria de ficar sozinho.

No offense, but this cheese tastes like rubber.
Sem ofensas, mas este queijo tem gosto de borracha.

No offense, but I find your sister a little rude.
Sem ofensas, mas eu acho a sua irmã um pouco rude.

If you don’t mind, I’d rather go on my own ‒ no offense, but I think it would be better.
Se você não se importar, eu preferiria ir sozinho ‒ sem ofensas, mas eu acho que seria melhor.

No disrespect to the team, but it wasn’t their best performance.
Sem ofensas ao time, mas não foi o melhor desempenho deles.

No disrespect to John Beck, but the club has been happier since he left.
Sem ofensas ao John Beck, mas o clube tem estado mais feliz desde que ele saiu.

Jerry, no disrespect, but you really need to connect more with your family.
Jerry, sem ofensas, mas você realmente precisa se relacionar mais com a sua família.

I’m sorry, I meant no offense.
Desculpe, eu não quis ofender.

I mean no offense, but isn’t there someone more qualified for the job?
Eu não quero ofender, mas não há alguém mais qualificado para o serviço?

I mean no offence by what I’m about to say, but you look very tired.
Eu não quero ofender com o que estou prestes a dizer, mas você parece muito cansado.

Any one of your tenants, Sir John, and I mean no offence, could be the assassin.
Qualquer um dos seus inquilinos, Sir John, e eu não quero ofender, poderia ser o assassino.

“No offense, but your bedroom is a mess.” “No worries, none taken. I’ve been meaning to clean it all week.”
“Sem ofensas, mas o seu quarto está uma bagunça.” “Sem problemas, não me ofendi. Eu venho querendo limpá-lo a semana inteira.”

“I don’t think the work you’ve done so far will be enough — no offense.” “None taken. If you need more done, just say the word.”
“Eu acho que o trabalho que você fez até agora não será o suficiente — sem ofensas.” “Não me ofendi. Se você precisar que mais seja feito, é só falar.”

“No offense but your hair is pretty messy, Claire.” “None taken, I woke up like this, to be honest.”
“Sem ofensas, mas seu cabelo está bem bagunçado, Claire.” “Não me ofendi, eu acordei assim, para ser sincera.”

There was no malice in her, on the contrary, she was very kind.
Não havia malícia nela, pelo contrário, ela era muito bondosa.

It wasn’t a good thing, on the contrary it was a huge mistake.
Isso não era uma boa coisa, pelo contrário, era um grande erro.

The crime problem has not disappeared. On the contrary, it seems to be becoming worse again.
O problema da criminalidade não desapareceu. Pelo contrário, parece estar piorando novamente.

– Did I fail the test? – On the contrary, you passed with flying colors!
– Eu não passei na prova? – Pelo contrário, você passou com louvor!

The risk of infection hasn’t diminished – on the contrary, it has increased.
O risco de infecção não diminuiu – pelo contrário, aumentou.

It is not an idea around which the Community can unite. On the contrary, I see it as one that will divide us.
Esta não é uma ideia em torno da qual a comunidade pode se unir. Pelo contrário, eu a vejo como uma ideia que nos dividirá.

– I thought you said the film was exciting? – On the contrary, I nearly fell asleep halfway through it!
– Achei que você disse que o filme era empolgante.  – Pelo contrário, eu quase peguei no sono na metade dele!

– People just don’t do things like that. – On the contrary, they do them all the time.
– As pessoas simplesmente não fazem coisas assim. – Pelo contrário, fazem o tempo todo.

– I suppose your wife doesn’t understand you. – On the contrary, she understands me very well.
– Imagino que a sua esposa não o entenda. – Pelo contrário, ela me entende muito bem.

And quite the contrary, we have increased oil production.
E muito pelo contrário, aumentamos a produção de petróleo.

That is not to say that the film is bad, quite the contrary.
Isto não quer dizer que o filme seja ruim, muito pelo contrário.

There is nothing disreputable or sinister in this, quite the contrary.
Não há nada desconceituado ou sinistro nisto, muito pelo contrário.

A liberal secular constitution does not mean intolerance for religious beliefs – quite the contrary.
Uma constituição liberal secular não significa intolerância por crenças religiosas – muito pelo contrário.

Your needs do not decrease on retirement, quite the contrary.
As suas necessidades não diminuem após a aposentadoria, muito pelo contrário.

– Are they happy? – No, no, quite the contrary.
– Eles estão felizes? – Não, não, muito pelo contrário.

– Was he angry? – No, quite the opposite – he invited me to have dinner with him.
– Ele ficou bravo? – Não, muito pelo contrário – ele me convidou para jantar com ele.

I didn’t feel sleepy at all – just the opposite, in fact.
Eu não estava nem um pouco com sono – muito pelo contrário, na verdade.

I’m not a feminist, quite the opposite.
Eu não sou feminista, muito pelo contrário.

Brian said he had been in various parts of Britain but did not go into details.
O Brian disse que ele esteve em várias partes da Grã-Bretanha, mas não entrou em detalhes.

He doesn’t wish to go into detail about all the events of those days.
Ele não deseja entrar em detalhes sobre todos os eventos daqueles dias.

I did not go into detail on the phone but stressed the importance of what we needed to talk about.
Eu não entrei em detalhes pelo telefone, mas frisei a importância do que precisávamos conversar.

Mr. Shaw refused to go into detail about the discussions.
O senhor Shaw se recusou a entrar em detalhes sobre os debates.

I don’t want to go into details, but there were a few legal issues that prevented us from participating.
Eu não quero entrar em detalhes, mas houveram algumas questões legais que nos impediram de participar.

The clerk went into detail about the product with the customer.
O funcionário entrou em detalhes sobre o produto com o cliente.

I can’t go into details now, it would take too long.
Eu não posso entrar em detalhes agora, levaria muito tempo.

I just want a simple answer. Don’t go into details.
Eu só quero uma resposta simples. Não entre em detalhes.

I don’t think your essay goes into detail enough about how the three books relate to one another.
Eu acho que a sua redação não entra em detalhes o suficiente sobre como os três livros se relacionam uns com os outros.

The newspaper reports went into great detail about his political background.
As reportagens do jornal entraram em muitos detalhes sobre os antecedentes políticos dele.

I will try to tell the story without going into too much detail.
Eu tentarei contar a história sem entrar em muitos detalhes.

It’s time to pour oil on troubled waters.
É hora de colocar panos quentes.

My husband’s always arguing with my father, and I’m the one who has to pour oil on troubled waters.
Meu marido está sempre discutindo com meu pai, e sou eu que tenho que colocar panos quentes.

If those two are arguing again, send Mom in to talk to them — she’s great at pouring oil on troubled waters.
Se aqueles dois estiverem discutindo novamente, mande a mãe para falar com eles — ela é ótima em colocar panos quentes.

You’ve got what it takes to pour oil on troubled waters right now.
Você tem o necessário para colocar panos quentes neste momento.

The twins are quarreling so I’d best go pour oil on troubled waters.
Os gêmeos estão brigando, então é melhor eu ir colocar panos quentes.

His ideas caused real dissension within the party at first, but he poured oil on troubled waters in last night’s speech.
As ideias dele causaram uma verdadeira discórdia na festa a princípio, mas ele colocou panos quentes no discurso de ontem à noite.

I remember him taking umbrage when he thought I was doubting his grandmother’s skills so quickly poured oil on troubled waters.
Eu me lembro de ele ficar ofendido quando achou que eu estava duvidando da habilidade de sua avó, então eu rapidamente coloquei panos quentes.

He is an extremely experienced politician, who some diplomats believe may be able to pour oil on troubled waters.
Ele é um político extremamente experiente, o qual alguns diplomatas acreditam que talvez consiga colocar panos quentes.

Friends are a blessing — they pour oil on troubled waters, drag you to parties and make you feel loved.
Amigos são uma benção — eles colocam panos quentes, arrastam você para festas e fazem você se sentir amado.

Mama got into some frightful fuss with the staff at the store and Papa’s having to pour oil on troubled waters.
A mamãe se meteu em uma confusão medonha com os funcionários da loja e o papai está tendo que colocar panos quentes.

Mankind needs hope more than ever.
A humanidade precisa de esperança mais do que nunca.

Sister, I need your wisdom more than ever.
Irmã, eu preciso da sua sabedoria mais do que nunca.

More than ever, marketers require data to better understand their customers.
Mais do que nunca, os comerciantes precisam de dados para melhor entender os seus clientes.

Your adventure stories make me want to travel more than ever.
Suas histórias de aventura me fazem querer viajar mais do que nunca.

After spending the weekend with him, I like him more than ever.
Depois de passar o fim de semana com ele, eu gosto dele mais do que nunca.

We are spending more than ever on education.
Nós estamos gastando mais do que nunca com educação.

It is obvious that, more than ever, we need a strong European Union.
É óbvio que, mais do que nunca, nós precisamos de uma União Europeia forte.

Don’t let her down! She needs you more than ever.
Não a decepcione! Ela precisa de você mais do que nunca.

Now that I’ve proposed, Simone wants me more than ever.
Agora que eu a pedi em casamento, a Simone me quer mais do que nunca.

I am, more than ever, conscious of my shortcomings.
Eu estou, mais do que nunca, consciente dos meus defeitos.

Now that she’s with him, I want her more than ever.
Agora que ela está com ele, eu a quero mais do que nunca.

I screwed up and now they hate me more than ever.
Eu estraguei tudo e agora eles me odeiam mais do que nunca.

I really hope that my band will keep on being honest and playing the good music instead of turning into rats running after the rockstar lifestyle.
Espero de verdade que minha banda continue sendo honesta e tocando a boa música em vez de virar ratos correndo atrás do estilo de vida de estrelas do roque.

She has spent her life running after fame and fortune.
Ela passou a vida correndo atrás de fama e fortuna.

They’ve spent years running after that market.
Eles passaram anos correndo a trás desse mercado.

Run after excellence, and success will follow you.
Corra atrás da excelência e o sucesso o seguirá.

In today’s fast-paced world, where everyone is running after success and money, the one thing that often gets looked over is our health.
No mundo apressado de hoje em dia, onde todos estão correndo atrás de sucesso e dinheiro, a coisa que com frequência passa despercebida é a nossa saúde.          

It’s depressing how many people there are chasing so few jobs.
É deprimente quantas pessoas há correndo atrás de tão poucos empregos.

After years of chasing her dreams, she finally got a part in a film.
Após anos correndo atrás de seus sonhos, ela finalmente conseguiu o papel em um filme.

She is chasing her fourth championship title.
Ela está correndo atrás de seu quarto título de campeonato.

I don’t want to spend my whole life chasing after material possessions.
Não quero passar a vida toda correndo atrás de posses materiais.

People who spend their lives always chasing after pleasure have a good chance of attaining it.
Pessoas que passam suas vidas sempre correndo atrás do prazer têm uma boa chance de o conseguir.

All I do is pay attention to my body.
Tudo que eu faço é prestar atenção ao meu corpo.

I hope you’re paying attention, because you’ll be tested later.
Eu espero que você esteja prestando atenção, porque você será testado depois.

I’m sorry, I wasn’t paying attention to what you were saying.
Perdão, eu não estava prestando atenção ao que você estava dizendo.

Pay attention, Mark — there will be a quiz on this material at the end of the week!
Preste atenção, Mark — haverá uma prova baseada neste material no fim da semana!

Pay particular attention to the warnings printed on the label.
Preste atenção especial aos avisos impressos no rótulo.

Pay close attention to what she says.
Preste muita atenção ao que ela diz.

I don’t think she was paying any attention to what I was saying.
Eu acho que ela não estava prestando atenção nenhuma ao que eu estava dizendo.

My father never paid attention to the financial burden his gambling was creating until it was too late.
Meu pai nunca prestou atenção ao ônus financeiro que a sua jogatina estava criando até que fosse tarde demais.

You need to start paying attention to your kids, or you won’t have a relationship with them when they’re grown up.
Você precisa começar a prestar atenção aos seus filhos ou não terá um relacionamento com eles quando eles forem adultos.

Max always pays careful attention to what is being told to him.
O Max sempre presta atenção especial ao que lhe está sendo dito.

Organizations in this environment must pay attention to flexibility, quality and asset utilization to remain competitive.
As organizações neste meio devem prestar atenção à flexibilidade, qualidade e utilização de ativos para permanecerem competitivas.

However, the candidate’s response can be very revealing and interviewers should pay attention to it.
Entretanto, a resposta do candidato pode ser muito reveladora e os entrevistadores devem prestar atenção a ela.

– How are things going? – I can’t complain.
– Como vão as coisas? – Não dá pra reclamar.

– How have you been? – I can’t complain.
– Como você tem estado? – Não dá pra reclamar.

– How is work? – Well, I make a good living. I can’t complain.
– Como está o trabalho? – Bem, eu ganho bem. Não dá pra reclamar.

– How are you feeling? – I can’t complain.
– Como está se sentindo? – Não posso reclamar.

– Hi, Fred! How are you doing? – Nothing to complain about.
– Oi, Fred! Como você está? – Não dá pra reclamar.

– How are things at work? – Nothing to complain about.
– Como estão as coisas no trabalho? – Nada de que reclamar.

She asked me how I was and I answered there was nothing to complain about.
Ela me perguntou como eu estava e eu respondi que não dava para reclamar.

–  How did you sleep? – Oh, not too bad. Mustn’t grumble.
– Como você dormiu? – Ah, não muito mal. Não devo reclamar. (Note que not too bad é outro eufemismo que geralmente significa, isso sim, “bem” ou “muito bem”.)

– How’s it going then, Mike? – Oh, not too bad. Mustn’t grumble.
– E como vão as coisas então, Mike? – Ah, nada de mais. Não dá pra reclamar.

– How are you today? – Mustn’t grumble.
– Como você está hoje? – Não posso reclamar.

Please don’t be hard on Tessa — she’s such a sensitive kid.
Por favor, não pegue pesado com a Tessa — ela é uma criança tão sensível.

You mustn’t be hard on him. Take it easy, ok?
Você não pode pegar pesado com ele. Vá com calma, tá?

You’re right. Perhaps I’m too hard on her.
Você tem razão. Talvez eu pegue pesado demais com ela.

Don’t be hard on the boy. He didn’t mean it.
Não pegue pesado com o menino. Ele não teve a intenção.

I know I didn’t do well on the exam, but I didn’t expect my dad to be so hard on me about it — he grounded me for a month!
Eu sei que não fui bem na prova, mas eu não esperava que meu pai pegaria tão pesado comigo por causa disso — ele me deixou de castigo por um mês!

Don’t be so rough on them for making a mistake.
Não pegue tão pesado com eles por terem cometido um erro.

Aren’t you being a little rough on him? He is only a child.
Você não está pegando pesado demais com ele? Ele é só uma criança.

You know, I kind of expect her to be rough on me. I really screwed up this time.
Sabe, eu meio que espero que ela pegue pesado comigo. Eu realmente estraguei tudo dessa vez.

Why are you being so rough on him? You’re not perfect either.
Por que você está pegando tão pesado com ele? Você também não é perfeito.

You’re not rough on him like you should and I think that’s the problem.
Você não pega pesado com ele como deveria e eu acho que esse é o problema.

Be sure to ring and let us know you’ve got back safely.
Não deixe de nos ligar e avisar que você voltou bem.

Be sure to read all the directions carefully.
Não deixe de ler todas as instruções com cuidado. (Note que directions se refere especificamente a “instruções de como chegar” a algum lugar.)

Be sure to help your mom around the house.
Não deixe de ajudar sua mãe com as tarefas de casa.

Be sure to fasten your seat belt.
Não deixe de apertar seu cinto de segurança.

Be sure to pick up a shovel before this weekend’s snow storm.
Não deixe de comprar uma pá antes da tempestade de neve desse final de semana. (Note que pick up não só significa “pegar”, mas também “comprar”.)

Be sure to double-check that the door is locked.
Não deixe de se certificar duas vezes de que a porta esteja trancada.

Be sure to give your family my regards.
Não deixe de transmitir meus cumprimentos à sua família.

Be sure to call me tomorrow.
Não deixe de me ligar amanhã.

Be sure to read The Lord of the Rings before you kick the bucket!
Não deixe de ler O senhor dos anéis antes de bater as botas!

Be sure to see if she needs any help before you start playing your games.
Não deixe de ver se ela precisa de ajuda antes de começar a jogar seus jogos.

To some degree, we’ll have to compromise.
Até certo ponto, nós precisaremos ceder.

These statements are, to some degree, all correct.
Estas declarações estão, até certo ponto, todas corretas.

To some degree, I think that’s right, but there are other factors which affect the situation.
Até certo ponto, eu acho que isso está certo, mas há outros fatores que afetam a situação.

Your essay would be improved to some degree by tidying up your paragraphs.
A sua redação ficaria melhor, até certo ponto, dando uns retoques finais nos parágrafos.

The administration is willing to negotiate to some degree, but it is not ready to make any significant changes to the legislation.
A administração está disposta a negociar até certo ponto, mas não está pronta para fazer nenhuma mudança significativa na legislação.

To a certain extent, he’s right.
Até certo ponto, ele está certo.

If the composition of the family changes, the house can be adjusted, and to a certain extent enlarged.
Se a composição da família mudar, a casa pode ser ajustada e, até certo ponto, ampliada.

To a certain extent, this was anticipated before the study was undertaken.
Até certo ponto, isso foi previsto antes de o estudo ser realizado.

Even I believe that it is true to a certain extent.
Até eu acredito que é verdade, até certo ponto.

We are all to a certain extent affected by our surroundings.
Nós todos somos, até certo ponto, afetados por nosso ambiente.

“Was she good?” “Mmm… Up to a point.”
“Ela foi boa?” “Hum… Até certo ponto.”

Of course there is some truth in all this, but only up to a point.
É claro que há alguma verdade em tudo isso, mas somente até certo ponto.

The new traffic system worked up to a point, but it had its problems.
O novo sistema de tráfego funcionou até certo ponto, mas teve seus problemas.

I understand his feelings up to a point.
Eu entendo os sentimentos dele até certo ponto.

Competition is good but only up to a point.
Competição é bom, mas apenas até certo ponto.

My mind went blank when I heard the question.
Me deu um branco quando ouvi a pergunta.

When he asked me her name, my mind just went blank.
Quando ele me perguntou qual o nome dela, minha mente simplesmente deu branco.

My heart began to race and my mind went blank.
Meu coração começou a disparar e me deu um branco.

My mind went totally blank.
Me deu um branco total.

I tried to remember her name, but my mind was a complete blank.
Tentei me lembrar do nome dela, mas minha mente estava totalmente em branco.

Can you remind me of your name? I’m so sorry, but I’ve gone completely blank right now!
Você pode me lembrar do seu nome? Sinto muito, mas me deu um branco total nesse momento!

I just went blank and couldn’t remember his name for a minute.
Simplesmente me deu um branco e eu não consegui me lembrar do nome dele por um minuto.

I don’t know what happened – I just blanked out.
Não sei o que aconteceu – me deu um branco.

I totally blanked when it came to the written part of the exam.
Me deu um branco total quando cheguei à parte escrita da prova.

I was about to say something important, but I blanked out!
Eu estava a ponto de dizer algo importante, mas me deu branco!

I blank out every time I try to remember his name.
Me dá um branco toda vez que tento lembrar o nome dele.

Several publishers rejected her book, but that just made her all the more determined.
Vários editores rejeitaram o livro dela, mas isso só a tornou ainda mais determinada.

The fact that they’d written the play themselves made it all the more impressive.
O fato de eles próprios terem escrito a peça tornou tudo ainda mais impressionante.

The living room is decorated in light colours that make it all the more airy.
A sala de estar é decorada com cores claras que a tornam ainda mais arejada.

His progress as a boxer is all the more remarkable when taking into account his unique circumstances.
O progresso dele como boxeador é ainda mais notável quando se leva em conta as suas circunstâncias únicas.

You might think that my husband’s rudeness to me would turn me off, actually, it just makes me love him all the more.
Você talvez pense que a grosseria do meu marido para comigo me repeliria, na verdade, ela só me faz amá-lo ainda mais.

They are all the more deserving of our attention.
Eles são ainda mais merecedores da nossa atenção.

Any devaluation of the pound would make it even more difficult to keep inflation low.
Qualquer desvalorização da libra tornaria ainda mais difícil manter a inflação baixa.

The town’s even more prosperous than Nagahama.
A cidade é ainda mais próspera do que Nagahama.

I can offer you something even more powerful than money.
Eu posso lhe oferecer algo ainda mais poderoso do que dinheiro.

I think you should get her something even more romantic than that.
Eu acho que você deveria comprar para ela algo ainda mais romântico do que isso.

But that’s too hard, especially for you Americans. No offense.
Mas isso é difícil demais, ainda mais para vocês, americanos. Sem ofensas.

I find this outrageous, especially coming from you.
Eu acho isso ultrajante, ainda mais vindo de você.

He won’t try anything funny, especially here.
Ele não tentará nenhuma gracinha, ainda mais aqui.

You’re risking a lot to do this, especially after what happened this morning.
Você está arriscando muito ao fazer isso, ainda mais depois do que aconteceu nesta manhã.

Drinks will be served from seven o’clock.
As bebidas serão servidas a partir das sete horas.

I lived with him from the age of twenty.
Eu morei com ele a partir dos vinte anos.

Breakfast is available to fishermen from 6 a.m.
O café da manhã está disponível aos pescadores a partir das 6 da manhã.

From tomorrow every expense form that you submit must first be signed by Roger.
A partir de amanhã, todo formulário de despesas que você apresentar deverá primeiro ser assinado pelo Roger.

As of next month, all the prices will go up.
A partir do mês que vem, todos os preços subirão.

We won’t be living here anymore as of tomorrow.
Nós não moraremos mais aqui a partir de amanhã.

As of next Friday, all the airline’s fares will be going up.
A partir da próxima sexta-feira, o preço de todas as passagens da companhia aérea subirá.

As of this year, women hold 51.4 percent of all managerial positions.
A partir deste ano, as mulheres mantêm 51,4 por cento de todos os cargos administrativos.

As of 6th April 1999, all gifts to charities will be free of tax.
A partir de 6 de abril de 1999, todas as doações para instituições de caridade terão isenção fiscal.

The new law takes effect as from July 1.
A nova lei entra em vigor a partir de 1 de julho.

As from today, the bank will be open for business from 9.30 am.
A partir de hoje, o banco será aberto ao público a partir das 9:30 da manhã.

As from this weekend, we’ll be away for a few weeks.
A partir deste fim de semana, nós ficaremos fora por algumas semanas.

As from next Monday, she’ll have a new secretary.
A partir da próxima segunda-feira, ela terá uma nova secretária.

The car rolled and landed upside down.
O carro rolou e caiu de ponta-cabeça.

The bar staff put the chairs upside down on the tables.
O pessoal do bar colocou as cadeiras de ponta-cabeça nas mesas.

The counters were sparkling, the chairs were all upside-down on the tables, and the floor was swept.
Os balcões estavam brilhando, as cadeiras estavam todas de ponta-cabeça nas mesas e o chão estava varrido.

I left the book, open at page 3, upside-down on the side of the bath.
Eu deixei o livro, aberto na página 3, de ponta-cabeça ao lado da banheira. (Note que bath pode tanto significar “banho” quanto “banheira”. A palavra mais comum para “banheira” é bathtub, mas quando fica claro pelo contexto que você está se referindo a uma banheira, pode usar só bath.)

Turn the jar upside down and shake it.
Vire o pote de cabeça para baixo e o agite.

The plane was flying upside down at high speed.
O avião estava voando de cabeça para baixo a uma alta velocidade.

Turn the mould upside down and give it a gentle tap.
Vire a forma de ponta-cabeça e dê uma batida de leve.

It was an abstract painting and I couldn’t tell whether it was upside down or not.
Era uma pintura abstrata e eu não conseguia saber se estava de ponta-cabeça ou não.

The painting was hung upside down.
A pintura estava pendurada de cabeça para baixo.

His eyes were open and everything he saw was upside down.
Os olhos dele estavam abertos e tudo o que ele via estava de ponta-cabeça.

The car landed upside down in a ditch.
O carro caiu de cabeça para baixo em uma vala.

Thieves have turned our house upside down.
Ladrões deixaram a nossa casa de cabeça para baixo.

The basis of the past policy behind economic diplomacy is now turned upside down.
A base da antiga política que sustentava a diplomacia econômica está de ponta-cabeça agora.

Things have turned upside down in a matter of weeks thanks to the virus.
As coisas ficaram de ponta-cabeça em questão de semanas graças ao vírus.

If anything happens to her, I’ll hold you personally responsible.
Se algo acontecer com ela, vou responsabilizar você pessoalmente.

He may have had a terrible childhood, but he should still be held accountable for his own actions.
Ele pode ter tido uma infância terrível, mas ainda assim deve ser responsabilizado por suas próprias ações.

I hold the police responsible for what happened that day.
Eu responsabilizo a polícia pelo que aconteceu aquele dia.

He held me personally responsible whenever anything went wrong in the project.
Ele me responsabilizava pessoalmente sempre que algo dava errado no projeto.

If the plan fails I will hold you responsible.
Se o plano falhar, vou ter você como responsável.

He holds me responsible for the project’s failure.
Ele me tem como responsável pelo fracasso do projeto.

I don’t care if Vince is trying to blame this blunder on his staff — I hold him responsible.
Eu não estou nem aí se o Vince está tentando culpar este erro no seu pessoal – eu o responsabilizo.

Who do we hold responsible for this blunder?
Quem devemos responsabilizar por este erro?

I hold you accountable for John’s well-being.
Eu a responsabilizo pelo bem-estar do John.

He holds me responsible for his missing money.
Ele me responsabiliza pelo dinheiro dele que sumiu.

Managers should take more responsibility for their actions.
Os gerentes deveriam assumir mais responsabilidade por suas ações.

We all need to take responsibility for that.
Todos precisamos assumir responsabilidade por isto.

The biggest boy took the responsibility of answering for us all.
O garoto mais velho assumiu a responsabilidade de responder por todos nós.

Since it was my idea to throw the ball, I took responsibility for the broken window.
Dado que jogar a bola tinha sido minha ideia, eu assumi a responsabilidade pela janela quebrada.

You have to take responsibility for your life.
Você precisa assumir responsabilidade por sua vida.

– So you’re going to bring Kev, are you? – Not on your life!
– Então você vai trazer o Kev, é? – De jeito nenhum!

– “I want to see Clare alone.” – “Not on your life“, he replied.
– “Quero ver Clare a sós.” – “De jeito nenhum”, ele respondeu.

Lend him $50? Not on your life.
Emprestar $50 para ele? Nem pensar.

– Are you going to go and work for him then? – Not on your life!
– Você vai ir trabalhar para ele, então? – De jeito nenhum!

She wanted to change everything, but I told her not on your life, this room is mine.
Ela queria mudar tudo, mas eu disse para ela que de jeito nenhum, essa sala é minha.

– Are you going to tell him? – Not on your life.
– Você vai contar para ele? – De jeito nenhum.

– You should have given him a lift. – In that condition? Not on your life!
– Você deveria ter dado uma carona para ele. – Naquela condição? De jeito nenhum.

Do the government’s policies really help the average worker? Not on your life.
Será que as políticas do governo realmente ajudam o trabalhador mediano? De jeito nenhum.

Go out and miss the football match on TV? Not on your life!
Sair e perder o jogo de futebol na TV? Nem pensar!

– Hey, Johnny, come over and help me paint the house this afternoon. – Not on your life, Davey! I’ve got plans tonight and have no intention of getting dirtied up before then!
– Ei, Johnny, venha para cá e me ajude a pintar a casa essa tarde. – Sem pensar, Davey! Tenho planos para hoje à noite e não tenho intenção de me sujar antes disso!

His contribution did not go unnoticed.
A contribuição dele não passou despercebida.

She saw flaws that normally would have gone unnoticed.
Ela viu falhas que normalmente teriam passado despercebidas.

The results indicated that a significant percentage of the errors went unnoticed.
Os resultados indicaram que uma porcentagem significativa dos erros passou despercebida.

He hoped that his nervousness would go unnoticed.
Ele esperava que o seu nervosismo passasse despercebido.

It was dark and their entry into camp had gone unnoticed.
Estava escuro e a entrada deles no acampamento havia passado despercebida.

Feeding soldiers is not a glamorous business, for the most part, it is an administrative function that goes unnoticed.
Alimentar soldados não é um negócio glamoroso, em grande parte, é uma função administrativa que passa despercebida.

The success of the tests had not gone unnoticed at the Air Ministry.
O sucesso dos testes não havia passado despercebido no Ministério do Ar.

Underscoring this notion is the fact that other diseases continue to go unnoticed under the very nose of modern medicine.
Ressaltando esta noção está o fato de que outras doenças continuam a passar despercebidas bem debaixo do nariz da medicina moderna.

I hope her work to protect stray dogs doesn’t go unnoticed.
Eu espero que o trabalho dela de proteger cachorros de rua não passe despercebido.

If his sudden wealth had gone unnoticed, he wouldn’t have been caught.
Se a sua riqueza repentina tivesse passado despercebida, ele não teria sido pego.

The disease often has no symptoms and can go unnoticed.
A doença muitas vezes não tem sintomas e pode passar despercebida.

The attacks have not gone unnoticed in Brussels.
Os ataques não passaram despercebidos em Bruxelas.

A lot of work he does goes unnoticed.
Muitos serviços que ele faz passam despercebidos.

If the defect goes unnoticed beyond 18 months, pressure on the brain can cause permanent damage.
Se a deficiência passa despercebida por mais de 18 meses, a pressão no cérebro pode causar danos permanentes.

This woman is innocent – end of story.
Esta mulher é inocente – fim de papo.

I’m not going – end of story.
Eu não vou – fim de papo.

I’m not going to lend you any more money, end of story.
Eu não te emprestarei mais dinheiro algum, fim de papo.

I didn’t do anything wrong here, OK? End of story.
Eu não fiz nada de errado aqui, está bem? Fim de papo.

Don’t try to defend him. He’s just a snitch, end of story.
Não tente defendê-lo. Ele é simplesmente um dedo-duro, fim de papo.

I did it because I wanted to. End of story.
Eu fiz isso porque quis. Fim de papo.

The Beatles were the best band in history. End of discussion.
Os Beatles foram a melhor banda da história. Fim de papo.

Drop it, Marcus. End of discussion.
Desista, Marcus. Fim de papo.

He yelled at me, and I left. End of discussion.
Ele gritou comigo e eu fui embora. Fim de papo.

Look, I already told you I can’t give you a job here. End of discussion.
Olha, eu já te disse que não posso te dar um trabalho aqui. Fim de papo.

You’re not going out tonight – end of!
Você não vai sair hoje à noite – fim de papo!

It’s your turn to do the dishes, end of.
É a sua vez de lavar a louça, fim de papo.

Friends is the best TV series ever, end of.
Friends é a melhor série de TV de todas, fim de papo.

The countdown to the rocket launch will begin at 9.00 a.m.
A contagem regressiva para o lançamento do foguete começará às 9 da manhã.

The countdown has begun for the launch of the space shuttle.
A contagem regressiva começou para o lançamento do ônibus espacial.

There were three more things to do before countdown.
Havia mais três coisas para se fazer antes da contagem regressiva.

At the end of the countdown, everyone shouted, “Happy New Year!”
Ao final da contagem regressiva, todos gritaram: “feliz Ano Novo!”

He greeted the crowd, gave a few tips and instructions, then led us in a countdown from ten to one.
Ele saudou a multidão, deu algumas dicas e instruções, depois nos liderou em uma contagem regressiva de dez a um.

The countdown for the shuttle launch has already begun.
A contagem regressiva para o lançamento da nave já começou.

Both countdowns would proceed in parallel and required synchronization.
Ambas as contagens regressivas ocorreriam paralelamente e precisariam de sincronização.

The countdown to the election has already begun.
A contagem regressiva para a eleição já começou.

All eyes are on the skies this year for the countdown to July 20, 2019, which marks a half-century since Neil Armstrong landed on the moon.
Toda a atenção está nos céus este ano para a contagem regressiva até 20 de julho de 2019, que marca meio século desde que Neil Armstrong pousou na Lua.

Depending on the type of vehicle used, countdowns can start from 72 to 96 hours before launch time.
Dependendo do tipo de veículo usado, as contagens regressivas podem começar de 72 a 96 horas antes da hora do lançamento.

Would you like a glass of water?
Você quer um copo de água?

She poured herself a glass of water.
Ela se serviu de um copo de água.

Could I have a glass of water, please?
Poderia me dar um copo de água, por favor?

I’d just like a glass of water, please.
Eu só quero um copo de água, por favor.

I desperately need a glass of water.
Eu preciso desesperadamente de um copo de água.

Faith is like a glass of water ─ When you’re young, the glass is little, so it’s easy to fill. As you get older, the glass gets bigger.
A fé é como um copo de água ─ quando você é jovem, o copo é pequeno, então é fácil de encher. Conforme você fica mais velho, o copo fica maior.

He asked for a drink of water.
Ele pediu um copo de água.

Does anyone want a drink of water?
Alguém quer um copo de água?

He turned around and went back for a drink of water.
Ele se virou e voltou para beber um copo de água.

You came a long way for a drink of water.
Você veio de longe por um copo de água.

He came in for a drink of water and we began to talk.
Ele entrou para beber um copo de água e nós começamos a conversar.

The water glass should be the largest one you have.
O copo de água deve ser o maior que você tiver.

As soon as dinner was finished, the hostess tapped her water glass for attention.
Assim que o jantar acabou, a anfitriã bateu em seu copo de água para chamar a atenção.

The wine glass goes slightly to the right of the water glass, whether you will be serving red or white wine.
A taça de vinho vai levemente à direita do copo de água, quer você vá servir vinho tinto, quer branco.

I can’t believe I am late!
Eu não acredito que estou atrasado!

This train is always late.
Este trem está sempre atrasado.

Sorry I’m late. I was held up in traffic.
Desculpe, estou atrasado. Eu fiquei preso no trânsito.

I have to leave. I am so late!
Eu preciso ir embora. Eu estou tão atrasado!

Don’t worry, she is always late. She’ll be here soon.
Não se preocupe, ela está sempre atrasada. Ela estará aqui logo.

Boy, I am late for that meeting.
Rapaz, eu estou atrasado para aquela reunião.

Don’t be late for dinner.
Não chegue atrasado para o jantar.

You’ll be late for your flight if you don’t hurry up.
Você chegará atrasado para o seu voo se não se apressar.

Our ferry was two hours late because of the strike.
A nossa balsa chegou duas horas atrasada por causa da greve.

The bride was late for the ceremony.
A noiva chegou atrasada para a cerimônia.

I’m always late for class.
Eu sempre chego atrasado na aula.

He is going to be late for work.
Ele chegará atrasado no trabalho.

I missed the start of the exam because my bus was late.
Eu perdi o começo da prova porque o meu ônibus chegou atrasado.

I started my own company, so now I work for myself.
Eu abri a minha própria empresa, então agora eu trabalho por conta própria.

After one year, you can work for yourself.
Após um ano, você pode trabalhar por conta própria.

At the moment, I work for myself.
No momento, eu trabalho por conta própria.

Working freelance means having the freedom to choose your clients and work for yourself.
Trabalhar como freelance significa ter a liberdade de escolher os seus clientes e trabalhar por conta própria.

I’m happy because from now on I’ll work for myself.
Eu estou feliz porque, de agora em diante, eu trabalharei por conta própria.

He’s the kind of man who likes to work for himself.
Ele é o tipo de homem que gosta de trabalhar por conta própria.

Being allowed to work for yourself as a foreigner means being able to prove to the authorities that you can make ends meet.
Poder trabalhar por conta própria como estrangeiro significa ser capaz de provar às autoridades que você pode pagar as contas.

The two men have a dream to buy their own small farm, where they can work for themselves.
Os dois homens têm um sonho de comprar a sua própria pequena fazenda, onde eles poderão trabalhar por conta própria.

Do you pay less tax if you’re self-employed?
Você paga menos impostos se for autônomo?

They run an advice centre for the self-employed.
Eles administram um centro de consultoria para os autônomos.

Health insurance is a concern for the country’s 4 million self-employed.
O plano de saúde é uma preocupação para os 4 milhões de autônomos do país.

There are no paid holidays or sick leave if you are self-employed.
Não há férias pagas ou licença médica se você for autônomo.

Kate tried each of the keys, but none of them fit. ‘Now what?’ she thought.
Kate experimentou cada uma das chaves, mas nenhuma delas coube. “E agora?”, pensou ela.

He was doing everything possible, but what now?
Ele estava fazendo todo o possível, mas e agora?

And now what about these phone calls?
E agora, quanto a essas ligações telefônicas?

The car won’t start. Now what?
O carro não quer dar partida. E agora?

OK, I’m at the intersection you told me about — now what?
OK, estou na intersecção da qual você falou – e agora?

Well, now what? We rebooted the system, but we’re still not getting any signal.
Bem, e agora? Fizemos o reboot do sistema, mas ainda não estamos recebendo nenhum sinal.

“Oh, now what?” she muttered aloud when the alarm sounded for the third time.
“Ah, e agora?” ela murmurou em voz alta quando o alarme soou pela terceira vez.

Well, that idea didn’t work. Now what?
Bem, esta ideia não funcionou. E agora?

I tried everything you said but still the computer won’t start. Now what?
Eu tentei tudo o que você disse, mas o computador ainda não quer iniciar. E agora?

It didn’t work. Now what?
Não funcionou. E agora?

I kept trying all day but still this thing won’t start. What now?
Fiquei tentando o dia todo, mas ainda assim esse troço não quer iniciar. E agora?

I played all the right moves in the opening and got a perfect position, but what now?
Joguei todos os lances certos na abertura e consegui uma posição perfeita, mas e agora?

In business, it’s every man for himself.
Nos negócios, é cada um por si.

It might be a civilized place to shop at other times, but come the January sales, it’s every man for himself.
Pode ser um local civilizado para se fazer compras em outras épocas, mas quando chegam as vendas de janeiro, é cada um por si.

As soon as there was a crisis, it was every man for himself.
Assim que havia uma crise, era cada um por si.

In this company, no one helps anyone — it’s every man for himself.
Nesta empresa, ninguém ajuda ninguém — é cada um por si.

Once we realized that there was only one scoop of ice cream left, it was every man for himself.
Assim que nos demos conta de que só havia restado uma bola de sorvete, foi cada um por si.

Increasingly, it seems like it’s every man for himself during election season.
Cada vez mais, parece que é cada um por si durante o período eleitoral.

At first, we tried to help each other study for the exam, but just a few days later, it was every man for himself.
No início, nós tentamos ajudar uns aos outros a estudar para a prova, mas apenas alguns dias depois, era cada um por si.

When the ship began to sink, it was every man for himself.
Quando o navio começou a afundar, foi cada um por si.

Tribes survive by sticking together at all costs, and when it’s every man for himself, the tribe ceases to be a tribe.
As tribos sobrevivem por permanecerem juntas a todo custo, e quando é cada um por si, a tribo deixa de ser uma tribo.

I want to say emphatically: “every man for himself” is an illusory solution, a short-sighted way of looking at things.
Eu quero dizer enfaticamente: “cada um por si” é uma solução ilusória, uma maneira imediatista de enxergar as coisas.

There are no teams — it’s every man for himself.
Não há nenhum time — é cada um por si.

My condolences on the loss of your uncle.
Meus pêsames pela perda do seu tio.

“I just found out that my father passed away.” “My sympathies! Is there anything I can do for you?”
“Eu acabei de ficar sabendo que meu pai faleceu.” “Meus pêsames! Há algo que eu possa fazer por você?”

I want to express my condolences to your family.
Eu quero dar os pêsames à sua família.

She wishes to offer her sympathies to them.
Ela deseja dar os pêsames a eles.

The mayor offered his condolences.
O prefeito deu os pêsames.

Dignitaries from all over the world came to offer their condolences.
Dignitários de todo o mundo vieram dar os pêsames.

She wished to offer her condolences.
Ela queria dar os pêsames.

In the early evening, she answered the door to find Helen Morris, of all people, come to offer her condolences.
No início da noite, ela atendeu à porta para encontrar justo a Helen Morris vindo dar os pêsames.

Tom, I just heard about your wife’s passing and wanted to offer my most sincere condolences.
Tom, eu acabei de ficar sabendo do falecimento da sua esposa e queria dar os mais sinceros pêsames.

We’re ringing up after lunch to offer condolences to the family.
Nós ligaremos depois do almoço para dar os pêsames à família.

Jane wasn’t able to make it to the funeral, but she wanted to offer you her condolences nonetheless.
A Jane não conseguiu ir ao funeral, mas queria lhe dar os pêsames mesmo assim.

He expressed his condolences to the families of the people who died in the incident.
Ele deu os pêsames às famílias das pessoas que morreram no acidente.

We wish to express our sincere condolences to your family.
Nós queremos dar os sinceros pêsames para a sua família.

I therefore express my sincerest condolences to the victims.
Eu, portanto, dou os mais sinceros pêsames às vítimas.

Well, first of all, let me express my condolences to the entire firm.
Bem, antes de mais nada, permita-me dar os pêsames a toda a firma.

Lyla offered her sympathies to the mourning family.
A Lyla deu os pêsames à família enlutada.

May I offer my deepest sympathies on the death of Lady Milroy.
Permita-me dar os mais profundos pêsames pela morte da Lady Milroy.

By the way, I’d like to offer my sympathies to Mr. Armstrong.
A propósito, eu gostaria de dar os pêsames ao sr. Armstrong.

I am writing to offer my deepest sympathies to you and your family.
Eu estou escrevendo para dar os mais profundos pêsames a você e à sua família.

We were so saddened to hear about the passing of your sweet brother and we offer you our deepest sympathies.
Nós ficamos muito tristes de ficar sabendo do falecimento do seu querido irmão e lhe damos os mais profundos pêsames.

He didn’t talk about his exam results in case people thought he was boasting.
Ele não falava sobre seus resultados do exame para que as pessoas não pensassem que ele estava contando vantagem. (Note a estrutura in case people thought, “para o caso de as pessoas pensarem” ou “para que as pessoas não pensassem”.)

He keeps boasting about his heroic actions, but he really didn’t have that big of a role in the rescue efforts.
Ele fica contando vantagem sobre suas ações heróicas, mas na verdade ele não teve um papel tão grande assim nos esforços de resgate.

He spends half his time boasting about past victories.
Ele passa metade do tempo contando vantagem sobre vitórias passadas.

She’s always bragging about how much money she earns.
Ela está sempre contando vantagem sobre o quanto de dinheiro que ganha.

The government has been bragging about the good economy.
O governo tem estado contando vantagem sobre a boa economia.

He’s always bragging about his success.
Ele está sempre contando vantagem sobre seus sucessos.

He had a very successful year and has every right to blow his own trumpet.
Ele teve um ano muito bem sucedido e tem todo direito de contar vantagem.

I don’t mean to blow my own trumpet, but this pasta sauce I made is quite delicious!
Não quero ficar contando vantagem, mas este molho de macarrão que eu fiz é delicioso!

I can’t stand being around Marcus ever since his company became such a massive success. The guy just can’t stop blowing his own trumpet!
Não aguento ficar perto do Marcus desde que a companhia dele virou um sucesso tão enorme. O cara simplesmente não consegue parar de contar vantagem!

He talks big about all the things he’s doing to make the country safer, but so far his administration hasn’t done much.
Ele fica contando vantagem sobre todas as coisas que está fazendo para tornar o país mais seguro, mas até agora a administração dele não fez muito.

She likes to talk big about how great a tennis player she is, but I don’t think she’s even won a tournament.
Ela gosta de contar vantagem sobre a grande jogadora de tênis que é, mas eu acho que ela nem sequer ganhou um torneio.

The President talks big but he doesn’t do anything.
O presidente conta vantagem, mas não faz coisa alguma.

I don’t have the faintest idea what you’re talking about.
Eu não faço a mínima ideia do que você está falando.

I haven’t the slightest idea what you’re on about.
Não tenho a mínima ideia do que você se refere. (To be on about é um jeito de dizer “se referir” ou “querer dizer”. Geralmente, você usa esta expressão para dizer que não entende o que a pessoa quer dizer, como na frase acima.)

– Where did I put my keys?– I haven’t the foggiest.
– Onde coloquei as minhas chaves – Não faço a mínima.

I haven’t the foggiest idea what she’s talking about.
Não tenho a mínima ideia do que ela está falando.

I don’t have the foggiest idea what his address is.
Não faço a menor ideia de qual é o endereço dele.

I haven’t the faintest idea what you mean.
Eu não tenho a menor ideia do que você quer dizer.

– Is she home today? – I don’t have the slightest idea. Ask Elaine, she’ll know.
– Ela está em casa hoje? – Não tenho a menor ideia. Pergunte para a Elaine, ela vai saber.

– How often does it need to be changed?– Haven’t the foggiest.
– Com qual frequência precisa ser trocado? – Não faço ideia.

I did not have the foggiest idea what he meant.
Eu não tinha a menor ideia do que ele queria dizer.

I don’t have the foggiest idea why he called me.
Não tenho a menor ideia de que por que ele me chamou.

– When do we leave? – Haven’t the foggiest.
– Quando partimos? – Não faço ideia.

None of us had the foggiest idea about how to put the tent up.
Nenhum de nós tinha a menor ideia de como montar a barraca.

He likes being the center of attention.
Ele gosta de ser o centro das atenções.

She was the centre of attention – like all brides.
Ela era o centro das atenções – como todas as noivas.

He loves being the center of attention at any party.
Ele ama ser o centro das atenções em qualquer festa.

Do they want to be the centre of attention?
Eles querem ser o centro das atenções?

I loved talking and being the centre of attention, so I was chosen to be spokesperson.
Eu amava falar e ser o centro das atenções, então fui escolhido para ser o orador.

You can be the centre of attention in a conversation but then the focus changes as new participants enter the dialogue.
Você pode ser o centro das atenções em uma conversa, mas depois o foco muda conforme novos participantes entram no diálogo.

The tower is the centre of attention every morning when the choir sings on the rooftop.
A torre é o centro das atenções todas as manhãs, quando o coral canta no terraço.

You always loved doing plays back in college. And you especially loved being the center of attention.
Você sempre amou fazer peças lá na faculdade. E você amava especialmente ser o centro das atenções.

I don’t want a wedding. I can’t stand being the center of attention. I think we’ll just elope.
Eu não quero um casamento. Eu não suporto ser o centro das atenções. Eu acho que nós iremos simplesmente casar a dois.

And in this corner of the room, a gorgeous, three-tiered cake will be the center of attention.
E neste canto do aposento, um bolo lindo de três camadas será o centro das atenções.

She had a way of making herself the center of attention wherever she went.
Ela tinha o hábito de se tornar o centro das atenções onde quer que fosse.

My little sister always has to be the center of attention, so of course her drama overshadowed my birthday party.
Minha irmãzinha sempre tem que ser o centro das atenções, então é claro que o seu drama ofuscou a minha festa de aniversário.

Our neighbours put their house up for sale last week.
Os nossos vizinhos colocaram a casa deles à venda na semana passada.

We have decided to put the company up for sale.
Nós decidimos colocar a empresa à venda.

The old grocery store has been put up for sale.
A velha mercearia foi colocada à venda.

We’re putting the factory up for sale.
Nós estamos colocando a fábrica à venda.

The castle has been put up for sale.
O castelo foi colocado à venda.

The company put itself up for sale in January.
A empresa se colocou à venda em janeiro.

The Hyatt went bankrupt and was put up for sale.
A Hyatt faliu e foi colocada à venda.

I’m putting some of my stuff up for sale to help pay my bills.
Eu vou colocar algumas coisas minhas à venda para ajudar a pagar as minhas contas.

Freeport put up for sale all its oil and gas reserves, but the company didn’t receive any realistic offers.
A Freeport colocou à venda todas as suas reservas de petróleo e gás, mas a empresa não recebeu nenhuma oferta realista.

The equipment was finally put up for sale.
O equipamento finalmente foi colocado à venda.

The Herald has recently been put up for sale by the Scottish Media Group.
O The Herald foi recentemente colocado à venda pelo Scottish Media Group.

He never remembers anything I tell him. It just goes in one ear and out the other.
Ele nunca se lembra de nada que eu lhe falo. Simplesmente entra por um ouvido e sai pelo outro.

They gave me that information years ago, but it must have gone in one ear and out the other.
Eles me deram aquela informação há anos, mas ela deve ter entrado por um ouvido e saído pelo outro.

Everything I say to you seems to go in one ear and out the other.
Tudo que eu falo para você parece entrar por um ouvido e sair pelo outro.

“Why don’t you pay attention?” “I can’t concentrate. Things people say to me just go in one ear and out the other.”
“Por que você não presta atenção?” “Eu não consigo me concentrar. As coisas que as pessoas me falam simplesmente entram por um ouvido e saem pelo outro.

I’ve told him so many times — it just goes in one ear and out the other.
Eu disse para ele tantas vezes — simplesmente entra por um ouvido e sai pelo outro.

If I have to listen to something I don’t understand, it just goes in one ear and out the other.
Se eu tiver que ouvir algo que eu não entenda, aquilo simplesmente entra por um ouvido e sai pelo outro.

All the criticism is water off a duck’s back to me.
Para mim, toda a crítica entra por um ouvido e sai pelo outro.

He tried to convince her to take the job, but his advice was like water off a duck’s back.
Ele tentou convencê-la a aceitar o emprego, mas seu conselho entrou por um ouvido e saiu pelo outro.

All those things he said to me were just water off a duck’s back.
Todas aquelas coisas que ele me disse simplesmente entraram por um ouvido e saíram pelo outro.

I’ve told him that he can’t keep throwing money around like that, but he doesn’t listen – it’s just water off a duck’s back.
Eu lhe disse que ele não pode continuar torrando dinheiro assim, mas ele não escuta – simplesmente entra por um ouvido e sai pelo outro.

Every time you discipline him he will smile sweetly so that you may think your rebukes are like water off a duck’s back.
Toda vez que você o disciplina, ele sorri docemente para que você pense que as suas reprimendas entraram por um ouvido e saíram pelo outro.

We can buy them for $10 and sell them for $25 – easy money.
Nós podemos comprá-los por $10 e vendê-los por $25 – dinheiro fácil.

Schools facing tight budgets see corporate sponsorship as easy money.
Escolas que lidam com orçamentos apertados veem o patrocínio corporativo como dinheiro fácil.

Sincere spirit and moral authority count, not quick and easy money.
Espírito sincero e autoridade moral contam, não dinheiro fácil e rápido.

The thought of easy money draws many people to drug dealing.
A ideia de dinheiro fácil atrai muitas pessoas ao tráfico de drogas.

The business pages were calling it ‘the end of the era of easy money’.
As páginas de negócios estavam chamando isso de ‘o fim da era do dinheiro fácil’.

Babysitting is money for old rope if the children don’t wake up.
Ser babá é dinheiro fácil se as crianças não acordarem.

I had always believed that the top model’s job was money for old rope.
Eu sempre havia acreditado que o trabalho da top model era dinheiro fácil.

We are not part of that circle whose members regularly get money for old rope.
Nós não fazemos parte daquele círculo, cujos membros regularmente ganham dinheiro fácil.

That was money for old rope because they did not have to do anything.
Aquilo era dinheiro fácil porque eles não precisavam fazer nada.

He charged £65 for a 30 minute consultation — how’s that for money for old rope?
Ele cobrou £65 por uma consulta de 30 minutos — isso é que é dinheiro fácil!

Selling ice-cream is money for jam when it is very hot.
Vender sorvete é dinheiro fácil quando está muito quente.

“I’m getting paid to stay in my neighbours’ mansion while they’re on holiday.” “Wow, that’ll be money for jam!”
“Eu vou receber para ficar na mansão dos meus vizinhos enquanto eles estiverem de férias.” “Uau, isso vai ser dinheiro fácil!”

I love working on bicycles, so this job will be money for jam.
Eu amo trabalhar de bicicleta, então esse emprego será dinheiro fácil.

Twenty quid for watching a movie while the kids are asleep? Sounds like money for jam to me!
Vinte pratas para assistir a um filme enquanto as crianças estão dormindo? Parece ser dinheiro fácil para mim!

With his experience, the business was money for jam at $25.00 for a light morning’s work.
Com a experiência dele, o negócio era dinheiro fácil, ganhando $25,00 em uma manhã tranquila de trabalho.

It became obvious that all her complaints were in vain.
Ficou óbvio que todas as reclamações dela eram em vão.

He wants the world to know his son did not die in vain.
Ele quer que o mundo saiba que seu filho não morreu em vão.

I hope their sacrifices have not been in vain.
Espero que os sacrifícios deles não tenham sido em vão.

I tried in vain to start a conversation.
Eu tentei em vão puxar conversa.

All the police’s efforts to find him were in vain.
Todos os esforços da polícia em encontrá-lo foram em vão.

We walked on, looking in vain for a taxi.
Continuamos a andar, procurando em vão por um táxi.

He swore that his son’s death would not be in vain.
Ele jurou que a morte de seu filho não seria em vão.

Police searched in vain for the missing gunman.
A polícia procurou em vão o atirador desaparecido.

Workers tried in vain to keep the building from collapsing.
Os trabalhadores tentaram em vão impedir o edifício de desmoronar.

It took a great deal of courage to admit that all her efforts had been in vain.
Foi precisa muita coragem para admitir que todos os seus esforços haviam sido em vão.

The students asked the school to help them raise the money, but to no avail.
Os estudantes pediram à escola que os ajudasse a levantar o dinheiro, mas em vão.

They tried to discuss the issue calmly, but to no avail.
Eles tentaram discutir a questão calmamente, mas em vão.

All my protesting over the decision to fire Jeff was to no avail.
Todos os meus protestos relativos à decisão de demitir Jeff foram em vão. (Note a estrutura em inglês all my protesting, que literalmente soaria como “todo o meu protestamento”.)

Everything I did to help was of no avail. Nothing worked.
Tudo o que fiz para ajudar foi em vão. Nada funcionou.

All his shouting was to no avail, no one could hear him.
Toda a gritaria dele foi em vão, ninguém conseguia ouvi-lo.

We searched the whole area but all to no avail.
Pesquisamos a área inteira, mas sem resultado.

I apologized repeatedly, but to little avail.
Eu pedi desculpas várias vezes, mas com pouco resultado.

Her Spanish has improved by leaps and bounds this year.
O espanhol dela melhorou a passos largos este ano.

The airport continues to grow in leaps and bounds.
O aeroporto continua crescendo a passos largos.

The company is growing by leaps and bounds this year.
A companhia está crescendo a passos largos este ano.

He’s improved in leaps and bounds this season.
Ele melhorou a passos largos nesta temporada.

The total number of species on the planet appears to be growing by leaps and bounds.
O número total de espécies no planeta parece estar aumentando a passos largos.

The literature on nationalism has grown by leaps and bounds over the last two decades.
A literatura sobre nacionalismo cresceu a passos largos durante as últimas duas décadas.

We are progressing by leaps and bounds.
Estamos progredindo a passos largos.

Our small company has been growing by leaps and bounds over the past year.
Nossa pequena companhia tem estado crescendo a passos largos durante o último ano.

What was once a tiny music club has expanded by leaps and bounds over the years.
O que antes era um pequenino clube musical expandiu a passos largos com o passar dos anos.

The profits of my company are increasing by leaps and bounds.
Os lucros da minha companhia estão aumentando a passos largos.

Penny’s only son was the apple of her eye.
O filho único da Penny era a menina dos olhos dela.

I was the apple of my father’s eye.
Eu era a menina dos olhos do meu pai.

His youngest daughter was the apple of his eye.
Sua filha mais nova era a menina dos olhos dele.

She has three children, but her youngest son is the apple of her eye.
Ela tem três filhos, mas o seu filho mais novo é menina dos seus olhos.

While my grandmother loved all of us very much, my younger brother was the apple of her eye.
Embora a minha avó amasse muito a todos nós, o meu irmão mais novo era a menina dos olhos dela.

Poor Richard was to me as an eldest son, the apple of my eye.
O pobre Richard era para mim como um filho mais velho, a menina dos meus olhos.

She was a very charming little girl and a very bright student, and was the apple of her teachers’ eyes.
Ela era uma menininha muito encantadora e uma aluna muito inteligente, e era a menina dos olhos dos seus professores.

He loved his daughter very much. She was the apple of his eye.
Ele amava muito a sua filha. Ela era a menina dos seus olhos.

He said that Kelly was the apple of his eye. He could not imagine living without her.
Ele disse que a Kelly era a menina dos olhos dele. Ele não conseguia imaginar viver sem ela.

The young couple had a beautiful little son, and he was the apple of their eyes.
O jovem casal tinha um lindo filhinho e ele era a menina dos olhos deles.

He was the apple of her eye, and she promised to take care of him for as long as she could.
Ele era a menina dos olhos dela, e ela prometeu cuidar dele enquanto ela pudesse.

‘My granddaughter is the apple of my eye’, said the old man, lovingly looking at her playing in the distance.
“A minha neta é a menina dos meus olhos”, disse o senhor, carinhosamente observando-a brincar à distância.

I waited for half an hour.
Eu esperei por meia hora.

I’ll be back in half an hour.
Eu estarei de volta em meia hora.

Can you ring back in half an hour?
Você pode ligar de volta em meia hora?

Could they come back in half an hour?
Eles poderiam voltar em meia hora?

When I finally spoke to somebody, they said that an engineer would call me back within half an hour.
Quando eu finalmente falei com alguém, eles disseram que um engenheiro me ligaria de volta em meia hora.

Within half an hour, he was back on the front line where his men could see him alive and fighting again.
Dentro de meia hora, ele estava de volta à linha de frente, onde seus homens podiam vê-lo vivo e lutando novamente.

Half an hour later, she was smiling and chatting as if nothing had happened.
Meia hora depois, ela estava sorrindo e batendo papo como se nada tivesse acontecido.

Trains depart every half hour.
Os trens partem a cada meia hora.

Once Mrs. Black starts talking to you, you’re stuck with her for a good half hour.
Quando a senhora Black começa a conversar com você, você fica preso com ela por pelo menos meia hora.

The train doesn’t leave for another half hour yet.
O trem só sairá daqui meia hora ainda.

Then we had to sit through another half hour of tedious explanations.
Depois, nós tivemos que assistir a mais meia hora de explicações entediantes.

The first half hour of the day is usually spent on correspondence, emails and paperwork.
A primeira meia hora do dia geralmente é gasta com correspondências, e-mails e papelada.

I’ve spent the last half hour trying to get the baby off to sleep.
Eu passei a última meia hora tentando fazer o bebê dormir.

I waited a half-hour in line.
Eu esperei meia hora na fila.

I got off work a half-hour ago.
Eu saí do serviço há meia hora.

The lecture led to a half-hour of stimulating dialogue.
A palestra levou à meia hora de um diálogo estimulante.

There was a long half-hour wait before he was rescued.
Houve uma longa espera de meia hora antes de ele ser resgatado.

It’s a half-hour TV show.
É um programa de TV de meia hora.

I do half-hour sessions of meditation to relax.
Eu faço sessões de meditação de meia hora para relaxar.

I could eat whatever I want if I added three half-hour swims to my weekly routine.
Eu poderia comer o que quisesse se eu acrescentasse três nados de meia hora à minha rotina semanal.

I lay in my tent in the dead of night, listening to the noises in the woods.
Eu me deitei em minha tenda na calada da noite, escutando os barulhos na floresta.

I couldn’t fly illegally into a country in the dead of night.
Eu não poderia voar ilegalmente para um país na calada da noite.

Why are you calling me in the dead of night? Can’t this wait till morning?
Por que você está me ligando na calada da noite? Isso não pode esperar até amanhã de manhã?

In the dead of the night, he broke camp and fled.
Na calada da noite, ele levantou acampamento e fugiu.

She left in the dead of the night.
Ela partiu na calada da noite.

Have you ever wondered why the cat is so particular about settling territorial disputes in the dead of night, when everyone is asleep?
Já se perguntou por que os gatos são tão exigentes em resolver disputas territoriais na calada da noite, quando todos estão dormindo?

You never know what strange ideas will suddenly grip me in the dead of night, when I’m alone with my computer.
Nunca se sabe que ideias estranhas prenderão a minha atenção na calada da noite, quando estou a sós com o meu computador.

Theoretically, you could get there in 13 hours but then you’d probably have to travel in the dead of night.
Teoricamente, você poderia chegar lá em 13 horas, mas aí você provavelmente teria que viajar na calada da noite.

She received regular telephone calls in the dead of night from her father, helpless with pain.
Ela recebia ligações telefônicas regulares do seu pai na calada da noite, desesperado de dor.

It seems that someone is secretly dropping money all over the city in the dead of night, for no apparent purpose.
Parece que alguém está deixando dinheiro por toda a cidade na calada da noite, sem nenhum propósito aparente.

We buried it in the garden at dead of night.
Nós o enterramos no jardim, na calada da noite.

She crept in at dead of night, while they were asleep.
Ela se infiltrou na calada da noite, enquanto eles estavam dormindo.

At dead of night, Clive marched out of the fort.
Na calada da noite, o Clive marchou para fora do forte.

The research project will be assessed over time.
O projeto de pesquisa será avaliado com o passar do tempo.

Students are encouraged to consider the way language changes over time.
Os estudantes são encorajados a considerar a forma pela qual a língua muda com o tempo.

As well as differing from place to place, what is defined as crime changes over time.
Além de diferir de lugar para lugar, o que é definido como crime muda com o passar do tempo.

There were also important changes over time.
Também houve mudanças importantes com o tempo.

Things will get better over time.
As coisas vão ficar melhor com o passar do tempo.

It’s fascinating to watch how a baby changes and develops over time.
É fascinante ver como um bebê muda e se desenvolve com o passar do tempo.

However, as time goes by and they become more experienced, more time will be given to these important matters.
Contudo, conforme o tempo passar e eles se tornarem mais experientes, mais tempo será dedicado a estas importantes questões.

As time goes by, I feel as if I know less and less.
Conforme o tempo passa, sinto como se soubesse cada vez menos.

As time goes by, this will all disappear.
Com o tempo, isso tudo desaparecerá.

As time passed, we came to see the truth of what she had said.
Conforme o tempo passou, viemos a perceber a verdade daquilo que ela havia dito.

As time passes, you will begin to understand better.
Conforme o tempo passa, você começará a compreender melhor.

I became more and more confident as time passed and I learned new skills.
Tornei-me cada vez mais confiante conforme o tempo passava e eu aprendia novas habilidades.

With time, things always get better.
Com o tempo, as coisas sempre melhoram.

Time heals all wounds, as they say. With time, you’ll feel better.
O tempo cura todas as feridas, como dizem. Com o tempo, você se sentirá melhor.

Her condition should improve with time.
A condição dela deve melhorar com o tempo.

Let’s get to work right now.
Vamos pôr mãos à obra agora mesmo.

We need to stop delaying and get to work.
Precisamos parar de delongar e pôr mãos à obra.

He promised to get to work on the state’s massive deficit.
Ele prometeu se pôr a trabalhar (para resolver) o enorme déficit do estado.

He returned to America where he got to work on a new novel.
Ele voltou para a América, onde pôs-se a trabalhar em um novo romance.

We’d better get to work on stacking this wood if we want to finish before it gets dark.
É melhor começarmos a trabalhar amontoando estas madeiras se quisermos terminar antes que escureça. (Note o uso da estrutura had better. Note também que wood é mass noun que geralmente não leva plural, assim como, por exemplo, water. Woods, no plural, é uma palavra diferente que significa “mata” ou “bosque”.)

You had better buckle down if you want to get good grades.
É melhor você pôr mãos à obra se quiser obter boas notas. (Had better, uma vez mais…)

All right, we’ll buckle down now and study for exams.
Está bem, vamos pôr mãos à obra agora e estudar para as provas.

I’ve wasted a lot of time, and now I have to buckle down and finish my homework.
Gastei muito tempo e agora preciso pôr mãos à obra e terminar a lição de casa.

I’ve got a lot of work to do, but I can’t seem to get down to it.
Tenho muito trabalho para fazer, mas parece que não consigo meter mãos à obra.

OK, people, let’s get down to it.
OK, pessoal, vamos pôr mãos à obra.

The meeting’s not due to start for another five minutes but we’re all here, so let’s get down to it.
A reunião está para começar só daqui a cinco minutos, mas já estamos todos aqui, então mãos à obra.

We need to break camp and head back to town before nightfall.
Nós precisamos levantar acampamento e retornar à cidade antes de anoitecer.

First thing in the morning, we broke camp and moved on northward.
De manhã cedo, nós levantamos acampamento e seguimos para o norte.

Okay, everyone. It’s time to break camp. Take those tents down and fold them carefully.
Tudo bem, pessoal. Está na hora de levantar acampamento. Desmontem aquelas tendas e dobrem-nas cuidadosamente.

It is the hunter’s rule to see that the fire is extinguished before breaking camp.
É a norma do caçador verificar que o fogo está apagado antes de levantar acampamento.

When Atticus returned, he told me to break camp.
Quando o Atticus voltou, ele me disse para levantar acampamento.

It is midnight now, and we’ll break camp at six in the morning.
É meia-noite agora, e nós levantaremos acampamento às seis da manhã.

After passing a miserable night, we broke camp at 4:30 o’clock.
Depois de passar uma noite péssima, nós levantamos acampamento às 4:30.

We break camp reluctantly, for this place seems like home to us.
Nós levantamos acampamento com relutância, porque esse lugar é como um lar para nós.

They reached their objective just as the Indians were beginning to break camp.
Eles alcançaram o seu objetivo no momento em que os índios estavam começando a levantar acampamento.

They were glad to break camp after their experiences on that lake.
Eles estavam contentes em levantar acampamento depois das suas experiências naquele lago.

Jill had such a long face yesterday after she learned that she failed her exam.
Jill estava com uma cara tão amarrada ontem depois de ficar sabendo que não havia passado na prova.

Hey, kiddo, why the long face? Is something bothering you?
Ei, filho, por que esta cara amarrada? Algo está incomodando você?

Greg’s long face was a clear indication of his feelings.
A cara amarrada do Greg era uma clara indicação de seus sentimentos.

Why do you have such a long face?
Por que você está com uma cara tão amarrada?

He took one look at her long face and said ‘What’s wrong?’
Ele olhou uma vez para a cara amarrada dela e disse: “O que está errado?”

Don’t pull a long face when I tell you to go to bed.
Não faça uma cara tão amarrada quando lhe digo para ir para a cama.

I don’t know what’s troubling him, but he’s been pulling a long face for two days already.
Não sei o que o está incomodando, mas ele tem estado fazendo uma cara fechada já faz dois dias.

Why are you pulling such a long face?
Por que você está fazendo uma cara tão amarrada?

She’s got such a long face because her boyfriend broke up with her.
Ela está com uma cara tão amarrada porque seu namorado terminou com ela.

– Why has he got such a long face? – He failed his exam.
– Por que ele está de cara tão fechada? – Ele não passou no exame.

What’s the world coming to when you can’t leave your house for five minutes without someone trying to rob you?
Onde é que esse mundo vai parar uma vez que você não pode nem sair de casa por cinco minutos sem que alguém tente te assaltar?

What’s the world coming to when so many poor children have to go to bed hungry every night?
Onde é que esse mundo vai parar uma vez que tantas crianças pobres têm que ir dormir com fome todas as noites?

I saw in the paper that they arrested a kid just for bringing a fork to school. What’s the world coming to?
Eu vi no jornal que uma criança foi presa só por levar um garfo para a escola. Onde é que esse mundo vai parar?

The times have changed and I guess I’m old-fashioned because I keep asking myself, “What’s the world coming to?”
Os tempos mudaram e eu acho que sou antiquado, porque fico me perguntando: “onde é que esse mundo vai parar?”

What’s the world coming to when a businessman has to pay to buy back his own stuff?
Onde é que esse mundo vai parar uma vez que um empresário precisa pagar para comprar de volta as suas próprias coisas?

What’s the world coming to when you can’t kill a man and be sure he’ll stay dead?
Onde é que esse mundo vai parar uma vez que você não consegue matar um homem e ter a certeza de que ele permanecerá morto?

Instant tea? What’s the world coming to?
Chá instantâneo? Onde é que esse mundo vai parar?

When I read the news these days I sometimes wonder what’s the world coming to.
Quando leio as notícias hoje em dia, eu às vezes me pergunto onde é que esse mundo vai parar.

A reality show where two strangers try to survive in the wild for 21 days, naked. What’s the world coming to?
Um reality show no qual dois estranhos tentam sobreviver na selva por 21 dias, pelados. Onde é que esse mundo vai parar?

What’s the world coming to when we can’t even trust our own family?
Onde é que esse mundo vai parar uma vez que nós não podemos nem mesmo confiar na nossa própria família?

The books were normally kept under lock and key in the library vault.
Normalmente os livros eram mantidos a sete chaves no cofre da biblioteca.

We keep these family jewels under lock and key.
Mantemos estas joias da família guardadas a sete chaves.

Her jewellery is securely under lock and key at the bank.
As joias dela estão guardadas seguramente a sete chaves no banco.

The jewels are kept under lock and key.
As joias são guardadas a sete chaves.

These files should be kept under lock and key.
Estes arquivos devem ser guardados a sete chaves.

I keep my grandmother’s secret recipe under lock and key so that no one can steal it.
Eu guardo a receita secreta da minha avó a sete chaves para que ninguém possa roubá-la.

He keeps the wine under lock and key.
Ele mantém o vinho a sete chaves.

The exam papers must be kept under lock and key until half an hour before the exam.
Os papéis da prova devem ser mantidos a sete chaves até meia hora antes do exame.

Dad keeps all his liquor under lock and key.
O papai mantém todas suas bebidas a sete chaves. (Note a palavra liquor, que é usada como plural para se referir a diferentes bebidas alcoólicas, e não só a licores.)

I keep it under lock and key at all times.
Eu o mantenho a sete chaves o tempo todo.

The company went bankrupt.
A empresa foi à falência.

If the firm cannot sell its products, it will go bankrupt.
Se a firma não puder vender os seus produtos, ela irá à falência.

Several thousand companies go bankrupt in the UK each year.
Vários milhares de empresas vão à falência no Reino Unido todo ano.

They piled up such a huge debt that they soon went bankrupt.
Eles acumularam uma dívida tão grande que logo foram à falência.

Many small businesses will go bankrupt unless interest rates fall.
Muitos pequenos negócios irão à falência a menos que as taxas de juros caiam.

He went bankrupt after only a year in business.
Ele foi à falência após apenas um ano no mercado.

The recession has led to many small businesses going bankrupt.
A recessão resultou em muitos pequenos negócios irem à falência.

I’ll go bankrupt if you kids keep asking me for money!
Eu irei à falência se vocês, crianças, continuarem me pedindo dinheiro!

The company went bankrupt and was put into the hands of the receivers.
A empresa foi à falência e foi colocada nas mãos dos administradores judiciais.

When it was obvious the company was going bankrupt, the government ordered all their assets to be frozen.
Quando estava óbvio que a empresa iria à falência, o governo ordenou que todos os seus bens fossem congelados.

The business went bankrupt after investing an enormous amount on a product that failed to sell.
O negócio foi à falência depois de investir uma quantia enorme em um produto que fracassou em vendas.

Without the help of a generous investor, the theatre company would have gone bankrupt.
Sem a ajuda de um investidor generoso, a companhia de teatro teria ido à falência.

Vacuum the cake crumbs, would you?
Passe o aspirador nas migalhas de bolo, está bem?

Then I vacuumed the carpet.
Daí eu passei o aspirador no tapete.

I need to vacuum the living room before I go out.
Eu preciso passar o aspirador na sala de estar antes de sair.

It’s important to vacuum once a week.
É importante passar o aspirador uma vez por semana.

I vacuumed the carpets today.
Eu passei o aspirador nos tapetes hoje.

The chambermaid vacuumed the carpets yesterday.
A camareira passou o aspirador nos tapetes ontem.

You must vacuum all the carpets and rugs regularly.
Você precisa passar o aspirador em todos os tapetes e capachos regularmente.

Vacuum the carpet to pick up any loose dirt.
Passe o aspirador no tapete para coletar qualquer sujeira solta.

The inside of the house has been vacuumed recently.
Passaram o aspirador no interior da casa recentemente.

Can’t you vacuum later? We’re already late.
Você não pode passar o aspirador mais tarde? Nós já estamos atrasados.

Tom was vacuuming the carpet while Mary was mopping the kitchen floor.
O Tom estava passando o aspirador no tapete enquanto a Mary estava esfregando o chão da cozinha.

She knew he wouldn’t go back on his word.
Ela sabia que ele não voltaria atrás com a palavra.

In his five years as Treasurer he broke solemn promises, went back on guarantees and cooked the books whenever necessary.
Em seus cinco anos como tesoureiro, ele quebrou solenes promessas, voltou atrás em garantias e fraudou a contabilidade sempre que preciso.

He has promised me he will do it and he has never gone back on a promise.
Ele me prometeu que o fará, e ele nunca voltou atrás numa promessa.

The budget crisis has forced the President to go back on his word.
A crise orçamentária forçou o presidente a voltar atrás na sua palavra.

The government looks likely to go back on its decision to close the mines.
Parece provável que o governo volte atrás em sua decisão de fechar as minas.

You can rely on her. She won’t go back on her word.
Você pode confiar nela. Ela não voltará atrás na palavra.

She’s gone back on her word and decided not to give me the job after all.
Ela voltou atrás na palavra e decidiu não me dar o emprego, afinal de contas.

Jason is totally unreliable and always goes back on his word.
O Jason não é nem um pouco confiável e sempre volta atrás na palavra.

Both leaders feared that the other would go back on his word.
Ambos os líderes temiam que o outro voltaria atrás na palavra.

They claimed that the president had gone back on his word.
Eles alegaram que o presidente havia voltado atrás na palavra.

    """

    # Nome do arquivo CSV
    nome_arquivo = "frases_traducao.csv"

    # Processar a entrada para obter os pares
    pares = processar_entrada(texto)

    # Criar o arquivo CSV
    criar_csv(pares, nome_arquivo)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")