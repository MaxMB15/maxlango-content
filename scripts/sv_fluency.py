"""sv-fluency-v1: B1. The bisats in full and relative som, the passive and the
conditional, modal particles and spoken Swedish, and the idioms,
untranslatables and false friends of real Swedish."""

from common import build_units, interleave, page, pack, topic, topic_labels
from sv_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("bisatser", "Bisatser", "subordinate clauses", ["ordfoljd"]),
    topic("passiv", "Passiv", "the passive", ["s-verb", "perfekt"]),
    topic("konditionalis", "Konditionalis", "would: the conditional", ["futurum", "preteritum"]),
    topic("modalpartiklar", "Modalpartiklar", "ju, väl, nog: modal particles", []),
    topic("talsprak", "Talspråk", "spoken Swedish", []),
    topic("falska-vanner", "Falska vänner", "false friends", []),
    topic("idioms", "Idiom", "idioms", []),
    topic("society", "Samhälle", "society and ideas", ["artiklar"]),
]

PAGES = [
    page(
        "sv-subordinate-clauses",
        "Inside the bisats",
        r"""
The core pack gave the main rule: in a **bisats** (a subordinate clause), *inte* goes in front of the verb. This page shows the whole pattern, and the two places where English speakers most often go wrong: indirect questions and *som*.

## Two word orders

A main clause keeps its verb in second place, whatever comes first. A bisats has a fixed order of its own: the conjunction, the subject, any short adverb, then the verb.

| First place | Verb | Subject | Adverb | Rest |
| --- | --- | --- | --- | --- |
| I dag | kommer | hon | inte | till jobbet. |
| Nu | har | vi | redan | ätit. |

| Conjunction | Subject | Adverb | Verb | Rest |
| --- | --- | --- | --- | --- |
| eftersom | hon | inte | mår | bra |
| att | vi | redan | har | ätit |

The adverbs that move are the short ones that comment on the whole sentence: *inte, aldrig, alltid, ofta, sällan, redan, gärna, kanske, nog, också, bara, verkligen*.

- *Han säger att han **aldrig** dricker kaffe.*
- *Jag hoppas att du **också** kan komma.*

## Indirect questions

A question inside another sentence is a bisats too, so it loses its question word order. A yes-or-no question takes **om** (whether, if):

| Direct question | Indirect question |
| --- | --- |
| Var bor han? | Vet du var han bor? |
| När börjar filmen? | Jag undrar när filmen börjar. |
| Kommer hon? | Jag vet inte om hon kommer. |

*Vet du var bor han?* is the classic mistake: it keeps the order of the direct question.

## Vem som, vad som

When the question word is the **subject** of an indirect question, Swedish adds **som**:

| Direct question | Indirect question |
| --- | --- |
| Vem ringde? | Jag vet inte vem som ringde. |
| Vad händer? | Kan du berätta vad som händer? |
| Vilka kommer? | Vet du vilka som kommer? |

Only when it's the subject, though. *Vem ringde du?* (Who did you call?) becomes *Jag vet inte vem du ringde*, with no *som*.

## Att-clauses in speech

When people report what someone said, they often keep main-clause order after *att*: *Han sa att han kunde inte komma.* You'll hear it all the time. In writing, use the bisats order: *Han sa att han inte kunde komma.*

## A bisats first

When a bisats opens the sentence, the main clause starts with its verb. The comma between them is optional, and often left out:

- *När jag kom hem **satt** barnen och läste.*
- *Om du vill **kan** vi äta ute.*

:::examples
- Jag vet inte om hon har tid. — I don't know if she has time.
- Kan du säga var stationen ligger? — Can you tell me where the station is?
- Han lovade att han aldrig skulle göra det igen. — He promised he'd never do it again.
:::

:::cloze{sentence="Jag undrar vem ___ har tagit min cykel." blank="som"}
:::

:::cloze{sentence="Fråga honom ___ han vill följa med." blank="om"}
:::
""",
        ["bisatser"],
        "sv-subordinate-clauses",
        explains=["bisatser"],
    ),
    page(
        "sv-relative-som",
        "Som: who, which and that",
        r"""
**Som** is the all-purpose relative word. It means *who*, *which* and *that*, for people and things, singular and plural:

- *Mannen **som** bor bredvid är polis.* (The man who lives next door is a police officer.)
- *Boken **som** ligger på bordet är min.* (The book that's on the table is mine.)

A relative clause is a bisats, so *inte* and the other short adverbs go before its verb: *en film som jag **aldrig** har sett* (a film I've never seen).

## When som can go

As with English *that*, you can leave out **som** when it's the object of its clause, but never when it's the subject:

| som is the object | som is the subject |
| --- | --- |
| filmen (som) vi såg i går | filmen som gick på tv i går |
| en vän (som) jag träffade i Lund | en vän som bor i Lund |

## The preposition goes last

Swedish never puts a preposition in front of *som*. It goes to the end of the clause, as in relaxed English:

- *huset som vi bor i* (the house we live in)
- *flickan som jag pratade med* (the girl I was talking to)

*I som* and *med som* are never possible.

## Där, dit, vars, vilket

| Swedish | English | Example |
| --- | --- | --- |
| där | where (at) | staden där jag föddes |
| dit | where (to) | landet dit de flyttade |
| vars | whose | en granne vars son spelar fotboll |
| vilket | which (a whole idea) | Han kom för sent, vilket var typiskt. |

**Vilket** points back to a whole statement, not a single noun: *Hon fick jobbet, vilket gladde alla.* (She got the job, which pleased everyone.)

## Det är ... som

Swedish likes to put the important part first with *det är ... som*: *Det är Anna som har bakat kakan* (It's Anna who baked the cake). It's the usual way to stress one part: *Det var i går som hon ringde* (It was yesterday that she called, not today).

:::examples
- Det är en låt som alla kan. — It's a song everyone knows.
- Var är tröjan jag köpte i lördags? — Where's the jumper I bought on Saturday?
- Det är min bror som bor i Umeå. — It's my brother who lives in Umeå.
:::

:::cloze{sentence="Det är huset som vi bodde ___ förut." blank="i"}
:::

:::cloze{sentence="Jag har en kollega ___ pappa är från Chile." blank="vars"}
:::
""",
        ["bisatser"],
        "sv-relative-som",
    ),
    page(
        "sv-passive",
        "The passive: byggs, byggdes",
        r"""
English makes the passive with *be*: *The house was built in 1890.* Swedish has two ways, and the more common one is a single letter: **-s**.

## The s-passive

Add **-s** to the active form. In the present, the **-r** goes first:

| | Active | Passive |
| --- | --- | --- |
| present | Man bygger ett hus. | Ett hus byggs. |
| past | Man byggde ett hus. | Ett hus byggdes. |
| perfect | Man har byggt ett hus. | Ett hus har byggts. |
| future | Man ska bygga ett hus. | Ett hus ska byggas. |

In group 2 the *-er* of the present usually goes too: *stänger → stängs, köper → köps*. A stem that already ends in *-s* keeps its *e*: *läser → läses*.

The s-passive is everywhere in news, instructions and signs:

- *Här talas svenska.* (Swedish is spoken here.)
- *Biljetter säljs i kassan.* (Tickets are sold at the till.)
- *Vägen stängs i natt.* (The road is being closed tonight.)

## Av: by

The person or thing doing the action takes **av**: *Huset ritades av en känd arkitekt.* (The house was designed by a famous architect.)

## Bli + participle

The other passive is **bli** and the participle, which agrees like an adjective: *Katten blev påkörd av en bil* (The cat was hit by a car). *Fönstren blev krossade* (The windows got smashed). It's more about what happened to someone, often suddenly. The s-passive is more neutral, and the usual choice in writing.

## Vara + participle: a state

With *är* or *var*, the participle describes a state, not an action, as on the perfect page: *Dörren stängs klockan sex* (is shut at six, an action), but *Dörren är stängd* (is shut, a state).

## Man: the passive you don't need

In speech Swedes often skip the passive and use **man** (one, people, you): *Man säger så.* (That's what people say.) *Hur stavar man det?* (How do you spell it?)

## Not every -s is a passive

*Hoppas, trivas, finnas* and the other s-verbs from the A2 pack only look passive. And *vi ses* means "see each other", not "we are seen".

:::examples
- Huset byggdes på 1700-talet. — The house was built in the 18th century.
- Resultatet meddelas i morgon. — The result will be announced tomorrow.
- Hon blev erbjuden jobbet. — She was offered the job.
:::

:::cloze{sentence="Svenska ___ i Sverige och Finland." blank="talas"}
:::

:::cloze{sentence="Mötet har ___ till fredag." blank="flyttats"}
:::
""",
        ["passiv"],
        "sv-passive",
        explains=["passiv"],
    ),
    page(
        "sv-conditional",
        "Skulle: would",
        r"""
English *would* is Swedish **skulle** + the infinitive. *Skulle* is the past tense of *ska*.

- *Jag skulle gärna följa med.* (I'd love to come along.)
- *Vad skulle du göra?* (What would you do?)

## If ... then

For something imagined or unlikely, put the past tense in the *om*-clause and *skulle* in the main clause, as English does:

| Real | Imagined |
| --- | --- |
| Om jag har tid hjälper jag dig. | Om jag hade tid skulle jag hjälpa dig. |
| Om det regnar stannar vi hemma. | Om det regnade skulle vi stanna hemma. |

**Vore** is an old form of *var* that survives here: *Om jag vore du...* (If I were you...). *Om jag var du* is common in speech too. *Det vore kul* means the same as *Det skulle vara kul* (That would be fun).

## Would have: hade + supine

For something that didn't happen, use **hade** and the supine on both sides. Swedish doesn't need *skulle* here:

- *Om jag hade vetat det hade jag kommit.* (If I'd known, I would have come.)
- *Det hade varit roligt.* (That would have been fun.)

*Skulle ha* + supine is also correct: *Jag skulle ha ringt.*

## Polite requests

*Skulle* softens a request, like English *would* and *could*:

- *Skulle du kunna hjälpa mig?* (Could you help me?)
- *Jag skulle vilja beställa.* (I'd like to order.)

## If only, what if

- *Om jag bara hade mer tid!* (If only I had more time!)
- *Tänk om det börjar regna!* (What if it starts raining?)

## Would for a habit

English *would* can also mean "used to": *Every summer we would go to the lake.* Swedish doesn't use *skulle* for that. Use the past tense, or **brukade**: *Varje sommar brukade vi åka till sjön.*

:::examples
- Vad skulle du göra om du vann en miljon? — What would you do if you won a million?
- Om jag vore du skulle jag ringa henne. — If I were you, I'd call her.
- Vi hade missat tåget om du inte hade väckt oss. — We'd have missed the train if you hadn't woken us.
:::

:::cloze{sentence="Om jag hade mer pengar ___ jag köpa en båt." blank="skulle"}
:::

:::cloze{sentence="Om du hade frågat mig ___ jag sagt ja." blank="hade"}
:::
""",
        ["konditionalis"],
        "sv-conditional",
        explains=["konditionalis"],
    ),
    page(
        "sv-modal-particles",
        "Ju, väl, nog and då",
        r"""
Spoken Swedish is full of small unstressed words that change the tone of a sentence without changing its facts. English does the same job with tone of voice, or with tags like *you know* and *surely*. These four are the most common.

| Particle | Tone | Example |
| --- | --- | --- |
| ju | as we both know | Det är ju söndag i dag. (It's Sunday today, you know.) |
| väl | I assume, surely | Du har väl ätit? (You have eaten, haven't you?) |
| nog | probably, I think | Hon kommer nog snart. (She'll probably be here soon.) |
| då | then, in that case | Vad gör vi nu då? (So what do we do now?) |

## Ju

*Ju* reminds the listener of something they already know, or should know. It can sound friendly or a little impatient: *Jag har ju sagt det!* (I've told you!)

## Väl

*Väl* asks for agreement, like a question tag: *Det är väl okej?* (That's okay, isn't it?) With *inte* it voices a worry: *Du är väl inte sjuk?* (You're not ill, are you?) Stressed, it means "well": *Sov väl!* (Sleep well!)

## Nog

Unstressed, *nog* means "probably": *Det blir nog regn i morgon.* Stressed, it means "enough": *Nu får det vara **nog**!* (That's enough now!)

## Då

At the end of a question or a command, *då* adds "then", and often some impatience: *Skynda dig då!* (Hurry up, then!)

## Where they go

Like *inte*, they come straight after the verb in a main clause, and before *inte* when both are there: *Han kommer **ju inte**.* In a bisats they go before the verb: *...eftersom hon **ju** bor här.* *Då* is the exception: it usually ends the sentence.

:::examples
- Vi ses väl i morgon? — We'll see each other tomorrow, won't we?
- Det är ju självklart. — Well, that's obvious.
- Han har nog glömt det. — He's probably forgotten.
:::

:::cloze{sentence="Ta med en jacka, det blir ___ kallt i kväll." blank="nog"}
:::
""",
        ["modalpartiklar"],
        "sv-modal-particles",
        explains=["modalpartiklar"],
    ),
    page(
        "sv-spoken-swedish",
        "How Swedes really talk",
        r"""
Written Swedish is close to the spoken language, but a handful of very common words sound different from how they're spelled. Hear them once and you'll hear them everywhere.

| Written | Said | English |
| --- | --- | --- |
| jag | ja | I |
| mig, dig, sig | mej, dej, sej | me, you, oneself |
| de, dem | dom | they, them |
| det | de | it |
| och | å | and |
| att (before a verb) | å | to |
| sedan | sen | then; since |
| någon, något, några | nån, nåt, nåra | someone, something, some |
| mycket | mycke | much, very |
| vad, var | va | what, where |
| säger | säjer | says |

Some of these turn up in texts and chat too: *nån, nåt, sen, dom, mej*. Use the full forms in anything formal.

## Small words that do a lot of work

| Word | Use |
| --- | --- |
| typ | like, roughly: *Det tog typ en timme.* |
| liksom | like, kind of (a filler) |
| asså | I mean, so (from *alltså*) |
| eller? | ..., or what? at the end of a question |
| eller hur? | isn't it?, right? |
| precis | exactly |
| jaså | oh really?, I see |
| nämen! | oh!, well I never! |
| nja | well..., not really |

## Ja on the in-breath

Many Swedes, especially in the north, say *ja* or *jo* while breathing in, as a short gasp. It means "yes, I'm listening", not surprise.

## One language, many accents

Stockholm, Göteborg, Skåne and Norrland sound clearly different. In most of Sweden the **r** is rolled or tapped, but in Skåne it's said in the back of the throat, as in French or Danish. Finland-Swedish has none of the sing-song word tones of Sweden, and so sounds flatter to Swedes. All of these are correct Swedish.

:::examples
- Det var typ jättekul. — It was, like, really fun.
- Du kommer på festen, eller? — You're coming to the party, right?
- Jaså, bor du i Malmö nu? — Oh, so you live in Malmö now?
:::

:::cloze{sentence="Det är kallt i dag, ___ hur?" blank="eller"}
:::
""",
        ["talsprak"],
        "sv-spoken-swedish",
        explains=["talsprak"],
    ),
    page(
        "sv-untranslatables",
        "Lagom, fika and allemansrätten",
        r"""
Some Swedish words carry an idea that English needs a whole sentence for. They also say a lot about how Swedes see the world.

## Lagom

Not too much and not too little: just right. Coffee can be *lagom varmt*, a flat *lagom stor*, a party *lagom lång*. *Lagom är bäst* is close to a national motto. *Lagom* never takes an ending: *en lagom portion*.

## Fika

A break for coffee or tea with something sweet, ideally in company. It's both a verb (*Ska vi fika?*) and a noun (*Vi tar en fika*). At many workplaces the morning and afternoon *fika* is close to sacred.

## Allemansrätten

The right of public access. Anyone may walk, cycle, camp for a night, and pick berries and mushrooms on almost any land, even private land, as long as they don't disturb or destroy. Children learn it as *inte störa, inte förstöra*.

## Jantelagen

The "Jante law": the unwritten rule that you shouldn't think you're better than anyone else. It's why Swedes tend to play down their own success. The name comes from a 1933 novel by the Danish-Norwegian writer Aksel Sandemose.

## Fredagsmys

"Friday cosiness": an evening on the sofa with the family, tacos or crisps, and a film. *Mys* is the noun behind *mysig*. Saturday has its own ritual, *lördagsgodis*: the one day of the week many children get sweets.

## Smultronställe

Literally "a wild strawberry patch": a small, special place you love and don't tell everyone about. Ingmar Bergman's film *Smultronstället* (Wild Strawberries) takes its title from it.

## Gökotta

Getting up at dawn to go outside and listen to the birds. *Gök* is the cuckoo.

## Mellanmål

"Between-meal": the afternoon snack, a proper part of the Swedish day, at school and at home.

:::examples
- Det är lagom varmt i vattnet. — The water's just the right temperature.
- Vi fikar klockan tre. — We have our coffee break at three.
- Det här är mitt smultronställe. — This is my special place.
:::
""",
        ["idioms"],
        "sv-untranslatables",
    ),
    page(
        "sv-false-friends",
        "False friends",
        r"""
Swedish and English share a lot of words, and learners guess, usually right. These are the places where guessing goes wrong.

| Swedish | Means | Not |
| --- | --- | --- |
| eventuell, eventuellt | possible, any; possibly | eventual, eventually (*så småningom, till slut*) |
| aktuell | current, topical | actual (*verklig, faktisk*) |
| sensibel | sensitive | sensible (*förnuftig*) |
| sympatisk | likeable, nice | sympathetic (*förstående*) |
| genial | brilliant, ingenious | genial (*vänlig*) |
| konsekvent | consistent | consequent |
| gift | married | gift (*en present*) |
| en glass | an ice cream | a glass (*ett glas*) |
| en fart | speed | |
| en novell | a short story | a novel (*en roman*) |
| en rock | a coat; rock music | a rock (*en sten*) |
| ett prov | a test | a proof (*ett bevis*) |
| en chef | a boss | a chef (*en kock*) |
| ett barn | a child | a barn (*en lada*) |
| en semester | a holiday | a semester (*en termin*) |
| en fabrik | a factory | fabric (*ett tyg*) |
| kissa | to pee | to kiss (*pussa, kyssa*) |
| slut | finished, over; sold out | |

*Eventuellt* is the classic. *Jag kommer eventuellt* means "I might come", not "I'll get there in the end".

*Gift* is a double trap: as an adjective it means married, and *ett gift* is a poison.

*Slut* has none of its English meaning: *Mjölken är slut* (We're out of milk), *Det är slut mellan oss* (It's over between us).

A *farthinder* is a speed bump, and *full fart* is full speed.

:::examples
- Jag kommer eventuellt lite senare. — I might come a bit later.
- Hon är en väldigt sympatisk person. — She's a really likeable person.
- Biljetterna är slut. — The tickets are sold out.
:::

:::cloze{sentence="Kan jag få ett ___ vatten?" blank="glas"}
:::

:::cloze{sentence="Barnen vill ha ___ efter maten." blank="glass"}
:::
""",
        ["falska-vanner"],
        "sv-false-friends",
        explains=["falska-vanner"],
    ),
    page(
        "sv-idioms",
        "How Swedish idioms work",
        r"""
Swedish idioms come from the farm, the forest and the kitchen, and many have an English cousin with a different animal or a different food.

| Swedish | Literally | Meaning |
| --- | --- | --- |
| det är ingen ko på isen | there's no cow on the ice | no need to worry, there's no rush |
| glida in på en räkmacka | slide in on a prawn sandwich | have it easy |
| ana ugglor i mossen | suspect owls in the bog | smell a rat |
| slå två flugor i en smäll | hit two flies with one swat | kill two birds with one stone |
| ha tummen mitt i handen | have your thumb in the middle of your hand | be all thumbs |
| inte för allt smör i Småland | not for all the butter in Småland | not for all the tea in China |
| gå som katten kring het gröt | walk like the cat around hot porridge | beat about the bush |
| vara ute och cykla | be out cycling | be way off, be completely wrong |

The literal translation is stored with each idiom in this pack. It's often what makes it stick.

## They bend to fit

An idiom is a phrase, not a fixed string. The verb takes whatever tense the sentence needs, and the pronouns change: *Han gick som katten kring het gröt* (He beat about the bush). *Nu är du ute och cyklar!* (Now you're way off!)

Some flip into the opposite: *Nu är det ko på isen!* means "Now we're in trouble".

## Proverbs

Swedes also quote proverbs in everyday talk, often just the first half: *Borta bra men hemma bäst* (East or west, home is best), or simply *Borta bra...* when coming home from a trip.

:::examples
- Det är ingen ko på isen, vi har gott om tid. — No need to worry, we've got plenty of time.
- Jag anade ugglor i mossen när han inte svarade. — I smelled a rat when he didn't answer.
- Hon har tummen mitt i handen. — She's all thumbs.
:::
""",
        ["idioms"],
        "sv-idioms",
        explains=["idioms"],
    ),
]

NOUNS = nouns(
    """
# society: the passive unit
samhälle | ett | samhället | samhällen | society; community | society | Vi lever i ett öppet samhälle. | We live in an open society.
regering | en | regeringen | regeringar | government | society | Regeringen presenterade budgeten i går. | The government presented the budget yesterday.
riksdag | en | riksdagen | riksdagar | parliament (the Riksdag) | society | Lagen röstades igenom av riksdagen. | The law was voted through by parliament.
val | ett | valet | val | election; choice | society | Valet hålls i september. | The election is held in September.
demokrati | en | demokratin | demokratier | democracy | society | Sverige har varit en demokrati länge. | Sweden has been a democracy for a long time.
skatt | en | skatten | skatter | tax | society | Skatten dras automatiskt från lönen. | The tax is taken from your pay automatically.
kommun | en | kommunen | kommuner | municipality, local council | society | Skolorna drivs av kommunen. | The schools are run by the council.
beslut | ett | beslutet | beslut | decision | society | Beslutet fattades i går kväll. | The decision was taken last night.
# society
politik | en | politiken | - | politics; policy | society | Jag är inte så intresserad av politik. | I'm not very interested in politics.
medborgare | en | medborgaren | medborgare | citizen | society | Hon blev svensk medborgare förra året. | She became a Swedish citizen last year.
rättighet | en | rättigheten | rättigheter | right | society | Alla har samma rättigheter. | Everyone has the same rights.
frihet | en | friheten | friheter | freedom | society | Friheten att välja är viktig. | The freedom to choose is important.
jämställdhet | en | jämställdheten | - | equality (between women and men) | society | Sverige satsar mycket på jämställdhet. | Sweden puts a lot into gender equality.
välfärd | en | välfärden | - | welfare | society | Välfärden betalas med skatter. | Welfare is paid for with taxes.
sjukvård | en | sjukvården | - | health care | society | Sjukvården är en viktig fråga i valet. | Health care is a big issue in the election.
miljö | en | miljön | miljöer | environment | society | Vi måste tänka på miljön. | We have to think about the environment.
ekonomi | en | ekonomin | ekonomier | economy; finances | society | Min ekonomi är lite dålig just nu. | My finances are a bit tight right now.
# history and culture
historia | en | historien | historier | history; story | society | Jag läser historia på universitetet. | I'm studying history at university.
krig | ett | kriget | krig | war | society | Sverige har inte varit i krig sedan 1814. | Sweden hasn't been at war since 1814.
fred | en | freden | - | peace | society | Alla vill leva i fred. | Everyone wants to live in peace.
kung | en | kungen | kungar | king | society | Kungen har ingen politisk makt. | The king has no political power.
drottning | en | drottningen | drottningar | queen | society | Drottning Kristina abdikerade 1654. | Queen Christina abdicated in 1654.
århundrade | ett | århundradet | århundraden | century | society | Det tog nästan ett århundrade att bygga kyrkan. | It took almost a century to build the church.
viking | en | vikingen | vikingar | Viking | society | Vikingarna reste ända till Konstantinopel. | The Vikings travelled all the way to Constantinople.
tradition | en | traditionen | traditioner | tradition | society | Midsommar är en viktig tradition i Sverige. | Midsummer is an important tradition in Sweden.
kultur | en | kulturen | kulturer | culture | society | Jag är intresserad av svensk kultur. | I'm interested in Swedish culture.
# opinions
åsikt | en | åsikten | åsikter | opinion, view | society | Vad är din åsikt om saken? | What's your view on the matter?
argument | ett | argumentet | argument | argument (a reason, not a quarrel) | society | Det är ett bra argument. | That's a good argument.
fördel | en | fördelen | fördelar | advantage | society | En fördel med staden är att allt ligger nära. | One advantage of the city is that everything's close by.
nackdel | en | nackdelen | nackdelar | disadvantage, downside | society | Nackdelen är att det tar lång tid. | The downside is that it takes a long time.
diskussion | en | diskussionen | diskussioner | discussion | society | Vi hade en lång diskussion om framtiden. | We had a long discussion about the future.
problem | ett | problemet | problem | problem | society | Det är inget problem! | It's no problem!
lösning | en | lösningen | lösningar | solution | society | Vi måste hitta en lösning. | We need to find a solution.
anledning | en | anledningen | anledningar | reason | society | Finns det någon anledning att oroa sig? | Is there any reason to worry?
nyhet | en | nyheten | nyheter | piece of news; novelty | society | Har du hört nyheten? | Have you heard the news?
# false friends
glass | en | glassen | glassar | ice cream | falska-vanner | Ska vi köpa en glass? | Shall we buy an ice cream?
glas | ett | glaset | glas | glass (to drink from); glass | falska-vanner | Ställ glasen i diskmaskinen. | Put the glasses in the dishwasher.
fart | en | farten | - | speed | falska-vanner | Sänk farten nära skolan! | Slow down near the school!
novell | en | novellen | noveller | short story | falska-vanner | Hon har skrivit en samling noveller. | She has written a collection of short stories.
roman | en | romanen | romaner | novel | falska-vanner | Jag läser en tjock roman just nu. | I'm reading a thick novel at the moment.
# untranslatables
allemansrätt | en | allemansrätten | - | the right of public access (to nature) | idioms | Allemansrätten gör att vi får tälta här. | The right of public access means we can camp here.
jantelag | en | jantelagen | - | the Jante law (don't think you're special) | idioms | Jantelagen lever kvar i Sverige. | The Jante law is still alive in Sweden.
smultronställe | ett | smultronstället | smultronställen | a special place of your own | idioms | Den här lilla stranden är mitt smultronställe. | This little beach is my special place.
fredagsmys | ett | fredagsmyset | - | a cosy Friday night in | idioms | Vi har fredagsmys med tacos och film. | We're having a cosy Friday night in with tacos and a film.
gökotta | en | gökottan | gökottor | going out at dawn to hear the birds | idioms | Vi gick upp klockan fyra för en gökotta. | We got up at four to go out and hear the birds.
mellanmål | ett | mellanmålet | mellanmål | snack (between meals) | idioms | Barnen äter en frukt som mellanmål. | The children have a piece of fruit as a snack.
"""
)

ADJECTIVES = (
    adjectives(
        """
aktuell, aktuellt, aktuella | current, topical | Frågan är väldigt aktuell just nu. | The issue is very topical right now.
eventuell, eventuellt, eventuella | possible, any (that may come up) | Eventuella frågor kan du skicka till mig. | You can send any questions to me.
gift, gift, gifta | married | Är du gift eller sambo? | Are you married, or living with a partner?
sensibel, sensibelt, sensibla | sensitive | Han är en sensibel och omtänksam person. | He's a sensitive, caring person.
sympatisk, sympatiskt, sympatiska | likeable, nice | Din nya kollega verkar sympatisk. | Your new colleague seems nice.
""",
        ["falska-vanner"],
    )
    + adjectives(
        """
lagom, lagom, lagom | just right, just enough | Portionen var precis lagom. | The portion was just right.
""",
        ["idioms"],
    )
    + adjectives(
        """
rolig, roligt, roliga | fun; funny | Det var en jätterolig kväll! | It was a really fun evening!
stressad, stressat, stressade | stressed | Jag är så stressad på jobbet just nu. | I'm so stressed at work at the moment.
förvånad, förvånat, förvånade | surprised | Alla blev förvånade när hon kom. | Everyone was surprised when she came.
avundsjuk, avundsjukt, avundsjuka | jealous, envious | Jag är lite avundsjuk på din semester. | I'm a bit jealous of your holiday.
tacksam, tacksamt, tacksamma | grateful | Vi är så tacksamma för hjälpen. | We're so grateful for the help.
envis, envist, envisa | stubborn | Min dotter är lika envis som jag. | My daughter is as stubborn as I am.
ärlig, ärligt, ärliga | honest | Var ärlig, vad tycker du egentligen? | Be honest, what do you really think?
modig, modigt, modiga | brave | Det var modigt av dig att säga ifrån. | That was brave of you to speak up.
självisk, själviskt, själviska | selfish | Det var lite själviskt av honom. | That was a bit selfish of him.
""",
        ["feelings"],
    )
    + adjectives(
        """
viktig, viktigt, viktiga | important | Det är viktigt att sova ordentligt. | It's important to get enough sleep.
möjlig, möjligt, möjliga | possible | Är det möjligt att boka en tid i dag? | Is it possible to book an appointment today?
nödvändig, nödvändigt, nödvändiga | necessary | Är det verkligen nödvändigt? | Is that really necessary?
rättvis, rättvist, rättvisa | fair | Det är inte rättvist! | It's not fair!
konstig, konstigt, konstiga | strange, weird | Vilket konstigt väder! | What strange weather!
"""
    )
    + adjectives(
        """
genial, genialt, geniala | brilliant, ingenious | Vilken genial idé! | What a brilliant idea!
konsekvent, konsekvent, konsekventa | consistent | Man måste vara konsekvent med barn. | You have to be consistent with children.
""",
        ["falska-vanner"],
    )
)

KA = "kommer att"

VERBS = [
    # bisatser
    verb("tro", "to think, to believe", [], group="3", fut=KA,
         example="Tror du att hon kommer?", example_en="Do you think she's coming?"),
    verb("anse", "to consider, to be of the opinion", [], group="4", pres="anser", pret="ansåg",
         sup="ansett", fut=KA,
         example="Många anser att skatten är för hög.", example_en="Many people think taxes are too high."),
    verb("undra", "to wonder", [], group="1", fut=KA,
         example="Jag undrar om hon har fått mitt mejl.", example_en="I wonder if she's got my email."),
    verb("påstå", "to claim", [], group="4", pres="påstår", pret="påstod", sup="påstått", fut=KA,
         example="Han påstår att han aldrig har varit här.", example_en="He claims he's never been here."),
    verb("bestämma", "to decide", [], group="2a",
         example="Det är du som bestämmer.", example_en="You're the one who decides."),
    verb("förklara", "to explain", [], group="1",
         example="Kan du förklara varför du är sen?", example_en="Can you explain why you're late?"),
    # relativ som
    verb("hända", "to happen", [], group="2a", fut=KA,
         example="Vad är det som har hänt?", example_en="What's happened?"),
    verb("försöka", "to try", [], group="2b",
         example="Jag försöker lära mig något nytt varje dag.", example_en="I try to learn something new every day."),
    verb("lova", "to promise", [], group="1",
         example="Du lovade att du skulle ringa!", example_en="You promised you'd call!"),
    verb("jämföra", "to compare", [], group="2a",
         example="Man kan inte jämföra äpplen och päron.", example_en="You can't compare apples and oranges."),
    verb("upptäcka", "to discover, to notice", [], group="2b", fut=KA,
         example="Vi upptäckte ett kafé som ingen känner till.", example_en="We discovered a café nobody knows about."),
    verb("tjäna", "to earn", [], group="1",
         example="Hon tjänar bra på sitt nya jobb.", example_en="She earns good money in her new job."),
    # konditionalis
    verb("önska", "to wish", [], group="1", fut=KA,
         example="Jag önskar att jag kunde flyga.", example_en="I wish I could fly."),
    verb("drömma", "to dream", [], group="2a", fut=KA,
         example="Jag drömmer om att bo vid havet.", example_en="I dream of living by the sea."),
    verb("välja", "to choose", [], group="4", pres="väljer", pret="valde", sup="valt",
         example="Vilken skulle du välja?", example_en="Which one would you choose?"),
    verb("föreställa sig", "to imagine", ["reflexiva-verb"], group="2a", fut=KA,
         example="Jag kan inte föreställa mig ett liv utan musik.", example_en="I can't imagine a life without music."),
    verb("spara", "to save (money, time)", [], group="1",
         example="Om vi sparade varje månad skulle vi ha råd.", example_en="If we saved every month, we could afford it."),
    verb("flytta", "to move (house)", [], group="1",
         example="Vi skulle gärna flytta till landet.", example_en="We'd love to move to the country."),
    # more verbs
    verb("klaga", "to complain", [], group="1", fut=KA,
         example="Han klagar alltid på vädret.", example_en="He's always complaining about the weather."),
    verb("skämmas", "to be ashamed, to be embarrassed", ["s-verb"], group="2a",
         pres="skäms", pret="skämdes", sup="skämts", fut=KA,
         example="Jag skäms över att jag glömde din födelsedag.", example_en="I'm embarrassed that I forgot your birthday."),
    verb("oroa sig", "to worry", ["reflexiva-verb"], group="1", fut=KA,
         example="Mamma oroar sig alltid för mig.", example_en="Mum always worries about me."),
    verb("bry sig om", "to care about", ["reflexiva-verb"], group="3", fut=KA,
         example="Han bryr sig inte om vad andra tycker.", example_en="He doesn't care what other people think."),
    verb("erkänna", "to admit", [], group="2a",
         example="Jag erkänner att jag hade fel.", example_en="I admit I was wrong."),
    verb("påverka", "to affect, to influence", [], group="1", fut=KA,
         example="Vädret påverkar mitt humör.", example_en="The weather affects my mood."),
    verb("rösta", "to vote", [], group="1",
         example="Vem ska du rösta på i valet?", example_en="Who are you voting for in the election?"),
]

IDIOMS = phrases(
    """
det är ingen ko på isen | there's no rush, no need to worry | Det är ingen ko på isen, vi hinner till tåget. | No need to worry, we'll make the train. | there's no cow on the ice
glida in på en räkmacka | to have it easy, to get something without working for it | Han har glidit in på en räkmacka hela livet. | He's had it easy his whole life. | to slide in on a prawn sandwich
ana ugglor i mossen | to smell a rat | Jag anade ugglor i mossen direkt. | I smelled a rat straight away. | to suspect owls in the bog
slå två flugor i en smäll | to kill two birds with one stone | Då slår vi två flugor i en smäll. | Then we'll kill two birds with one stone. | to hit two flies with one swat
ha tummen mitt i handen | to be all thumbs, to be clumsy | Min pappa har tummen mitt i handen. | My dad is all thumbs. | to have the thumb in the middle of the hand
inte för allt smör i Småland | not for anything, not for all the tea in China | Jag skulle inte bo där för allt smör i Småland. | I wouldn't live there for all the tea in China. | not for all the butter in Småland
gå som katten kring het gröt | to beat about the bush | Sluta gå som katten kring het gröt! | Stop beating about the bush! | to walk like the cat around hot porridge
vara ute och cykla | to be way off, to be completely wrong | Nej, där är du ute och cyklar! | No, you're way off there! | to be out cycling
lägga rabarber på något | to grab something, to claim something for yourself | Grannen har lagt rabarber på vår parkeringsplats. | The neighbour has grabbed our parking space. | to put rhubarb on something
köpa grisen i säcken | to buy a pig in a poke | Provkör bilen, köp inte grisen i säcken. | Test-drive the car, don't buy a pig in a poke. | to buy the pig in the sack
dra alla över en kam | to tar everyone with the same brush | Man ska inte dra alla över en kam. | You shouldn't tar everyone with the same brush. | to pull everyone over one comb
göra en höna av en fjäder | to make a mountain out of a molehill | Nu gör du en höna av en fjäder. | Now you're making a mountain out of a molehill. | to make a hen out of a feather
ha en räv bakom örat | to be sly, to have something up your sleeve | Akta dig för honom, han har en räv bakom örat. | Watch out for him, he's a sly one. | to have a fox behind the ear
sitta med skägget i brevlådan | to be caught out, to be stuck | Nu sitter vi där med skägget i brevlådan. | Now we're stuck. | to sit with your beard in the letterbox
lova guld och gröna skogar | to promise the earth | Politikerna lovar guld och gröna skogar. | The politicians are promising the earth. | to promise gold and green forests
inte ha alla hästar hemma | to not be all there | Han har inte alla hästar hemma. | He's not quite all there. | to not have all your horses at home
ha is i magen | to keep your cool | Man måste ha is i magen när man förhandlar. | You have to keep your cool when you negotiate. | to have ice in your stomach
det är inte hela världen | it's not the end of the world | Missade du bussen? Det är inte hela världen. | Did you miss the bus? It's not the end of the world. | it's not the whole world
borta bra men hemma bäst | east or west, home is best | Skönt att vara hemma igen, borta bra men hemma bäst. | Nice to be home again: east or west, home is best. | away is good but home is best
sälja skinnet förrän björnen är skjuten | to count your chickens before they're hatched | Sälj inte skinnet förrän björnen är skjuten! | Don't count your chickens before they're hatched! | to sell the skin before the bear is shot
""",
    ["idioms"],
)

SPOKEN = phrases(
    """
eller hur? | right?, isn't it? | Du är från Göteborg, eller hur? | You're from Gothenburg, aren't you? | or how
precis | exactly | Precis, det var det jag menade. | Exactly, that's what I meant.
jaså | oh, really?; I see | Jaså, har du flyttat? | Oh, have you moved?
det är lugnt | it's fine, no worries | Det är lugnt, jag kan vänta. | It's fine, I can wait. | it is calm
typ | like, about, sort of | Det tog typ en timme. | It took like an hour. | type
liksom | like, kind of (a filler) | Jag var liksom helt slut. | I was, like, totally exhausted. | as it were
nämen! | oh!, well I never! | Nämen, är det du? | Oh, is that you? | no but
nja | well..., not really | Nja, jag vet inte riktigt. | Well, I'm not really sure. | | A mix of *nej* and *ja*: a polite way to disagree.
""",
    ["talsprak"],
)

PARTICLES = phrases(
    """
det vet du ju | you know that (as well as I do) | Det vet du ju, vi har pratat om det. | You know that, we've talked about it.
du kommer väl? | you're coming, aren't you? | Du kommer väl på min fest? | You're coming to my party, aren't you?
det går nog bra | it'll probably be fine | Var inte nervös, det går nog bra. | Don't be nervous, it'll probably be fine.
kom igen då! | come on, then! | Kom igen då, vi är sena! | Come on, then, we're late!
det får väl duga | it'll have to do | Det är inte perfekt, men det får väl duga. | It's not perfect, but it'll have to do.
jag sa ju det | I told you so | Ser du? Jag sa ju det! | See? I told you so!
""",
    ["modalpartiklar"],
)

EXPRESSIONS = phrases(
    """
enligt mig | in my opinion | Enligt mig är det för dyrt. | In my opinion, it's too expensive. | according to me
vad tycker du? | what do you think? | Vad tycker du om förslaget? | What do you think of the proposal?
det stämmer | that's right | Det stämmer, hon har bott här länge. | That's right, she's lived here a long time.
jag är inte så säker på det | I'm not so sure about that | Billigare? Jag är inte så säker på det. | Cheaper? I'm not so sure about that.
det kan man diskutera | that's debatable | Är det bättre? Det kan man diskutera. | Is it better? That's debatable. | that can one discuss
det är en bra poäng | that's a good point | Det är en bra poäng, du har rätt. | That's a good point, you're right.
i och för sig | admittedly, in itself | I och för sig har du rätt. | Admittedly, you're right. | in and for itself
så att säga | so to speak | Det var så att säga en nystart. | It was a fresh start, so to speak.
faktiskt | actually, in fact | Jag tycker faktiskt om surströmming. | I actually like fermented herring.
jag har ändrat mig | I've changed my mind | Jag har ändrat mig, jag följer med ändå. | I've changed my mind, I'm coming after all.
det är inte säkert | that's not certain | Det är inte säkert att han kommer. | It's not certain that he's coming.
jag tvivlar på det | I doubt it | Kommer han i tid? Jag tvivlar på det. | Will he be on time? I doubt it.
det ordnar sig | it'll work out | Oroa dig inte, det ordnar sig. | Don't worry, it'll work out. | it arranges itself
hur som helst | anyway; any old how | Hur som helst, vi ses i morgon. | Anyway, see you tomorrow. | how as you like
på riktigt | for real, really | Menar du det på riktigt? | Do you really mean it? | on real
det var på tiden | about time too | Har bussen kommit? Det var på tiden! | Has the bus come? About time! | it was on the time
så är det bara | that's just how it is | Vintern är mörk, så är det bara. | Winter is dark, that's just how it is. | so is it only
ta det inte personligt | don't take it personally | Ta det inte personligt, han är trött. | Don't take it personally, he's tired.
""",
    ["expressions"],
)

CONNECTIVES = connectors(
    "connective",
    """
däremot | on the other hand, however | conn-contrast | Hotellet var dyrt. Maten var däremot billig. | The hotel was expensive. The food, on the other hand, was cheap.
å andra sidan | on the other hand | conn-contrast | Lägenheten är liten, men å andra sidan är den billig. | The flat is small, but on the other hand it's cheap. | Lägenheten är liten, men den är å andra sidan billig.
trots allt | after all, despite everything | conn-contrast | Det regnade, men vi hade trots allt en fin dag. | It rained, but we had a nice day after all. | Det regnade, men trots allt hade vi en fin dag.
alltså | so, therefore | conn-consequence | Tåget är inställt, vi får alltså ta bussen. | The train's cancelled, so we'll have to take the bus. | Tåget är inställt, alltså får vi ta bussen.
kort sagt | in short | conn-consequence | Kort sagt var det en lyckad kväll. | In short, it was a successful evening. | Det var kort sagt en lyckad kväll.
för övrigt | incidentally, besides | conn-addition | Maten var god, och vinet var för övrigt också bra. | The food was good, and the wine was good too, incidentally.
till exempel | for example | conn-addition | Här kan man till exempel vandra eller fiska. | Here you can go hiking or fishing, for example. | Man kan till exempel vandra eller fiska här.
slutligen | finally, lastly | conn-sequence | Slutligen vill jag tacka alla som har hjälpt till. | Finally, I'd like to thank everyone who has helped. | Jag vill slutligen tacka alla som har hjälpt till.
""",
    ["sambandsord"],
)

CONJUNCTIONS = connectors(
    "conjunction",
    """
utan | but (rather), after a negative | conj-coordinating | Han är inte lat utan trött. | He isn't lazy, just tired.
så att | so that | conj-subordinating | Jag pratar långsamt så att du förstår. | I'm speaking slowly so that you understand.
trots att | even though | conj-subordinating | Vi gick ut trots att det regnade. | We went out even though it was raining. | Trots att det regnade gick vi ut.
ifall | in case; if | conj-subordinating | Ta med ett paraply ifall det börjar regna. | Take an umbrella in case it starts raining.
så fort | as soon as | conj-subordinating | Ring mig så fort du är framme. | Call me as soon as you get there.
som om | as if | conj-subordinating | Han låtsas som om han inte hör. | He's pretending he can't hear.
så länge | as long as | conj-subordinating | Du får stanna så länge du vill. | You can stay as long as you like.
därför att | because | conj-subordinating | Jag stannade hemma därför att jag var sjuk. | I stayed at home because I was ill.
""",
    ["konjunktioner"],
)

ITEMS = PAGES + interleave(
    IDIOMS, SPOKEN + PARTICLES + EXPRESSIONS, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS
)

# One explicit Unit per page. sv-passive pairs with the society words, whose
# examples use the passive; sv-false-friends takes the false-friend nouns and
# adjectives; sv-untranslatables takes lagom and the untranslatable nouns.
# The rest becomes automatic Units by first tag via LABELS.
UNITS = [
    {
        "title": "Bisatser",
        "page_id": "sv-subordinate-clauses",
        "word_ids": ["tro", "anse", "undra", "pasta", "bestamma", "forklara"],
    },
    {
        "title": "Som",
        "page_id": "sv-relative-som",
        "word_ids": ["handa", "forsoka", "lova", "jamfora", "upptacka", "tjana"],
    },
    {
        "title": "Passiv",
        "page_id": "sv-passive",
        "word_ids": ["samhalle", "regering", "riksdag", "val", "demokrati", "skatt", "kommun", "beslut"],
    },
    {
        "title": "Konditionalis",
        "page_id": "sv-conditional",
        "word_ids": ["onska", "dromma", "valja", "forestalla-sig", "spara", "flytta"],
    },
    {
        "title": "Modalpartiklar",
        "page_id": "sv-modal-particles",
        "word_ids": ["det-vet-du-ju", "du-kommer-val", "det-gar-nog-bra", "kom-igen-da", "det-far-val-duga", "jag-sa-ju-det"],
    },
    {
        "title": "Talspråk",
        "page_id": "sv-spoken-swedish",
        "word_ids": ["eller-hur", "precis", "jasa", "det-ar-lugnt", "typ", "liksom", "namen", "nja"],
    },
    {
        "title": "Oöversättbart",
        "page_id": "sv-untranslatables",
        "word_ids": ["lagom", "allemansratt", "jantelag", "smultronstalle", "fredagsmys", "gokotta", "mellanmal"],
    },
    {
        "title": "Falska vänner",
        "page_id": "sv-false-friends",
        "word_ids": ["glass", "glas", "fart", "novell", "roman", "aktuell", "eventuell", "gift", "sensibel", "sympatisk"],
    },
    {
        "title": "Idiom",
        "page_id": "sv-idioms",
        "word_ids": [
            "det-ar-ingen-ko-pa-isen",
            "glida-in-pa-en-rakmacka",
            "ana-ugglor-i-mossen",
            "sla-tva-flugor-i-en-small",
            "ha-tummen-mitt-i-handen",
            "inte-for-allt-smor-i-smaland",
            "ga-som-katten-kring-het-grot",
            "vara-ute-och-cykla",
        ],
    },
    {
        "title": "Känslor",
        "word_ids": ["rolig", "stressad", "forvanad", "avundsjuk", "tacksam", "envis", "arlig", "modig", "sjalvisk"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "expressions": "Uttryck",
    "adjektiv": "Adjektiv",
    "presens": "Verb",
    "sambandsord": "Sambandsord",
    "konjunktioner": "Konjunktioner",
}

PACK = pack(
    "sv-fluency-v1",
    1,
    "sv",
    "Svenska · Flyt (B1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Repetition"),
)
