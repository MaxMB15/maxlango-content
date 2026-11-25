"""nl-fluency-v1: B1. Subordinate clauses and verb clusters, the passive and the
conditional, and the idioms, untranslatables and false friends of real Dutch."""

from common import build_units, interleave, page, pack, topic, topic_labels
from nl_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("bijzinnen", "Bijzinnen", "subordinate clauses", ["tegenwoordige-tijd"]),
    topic("lijdende-vorm", "Lijdende vorm", "the passive", ["voltooid-tegenwoordige-tijd"]),
    topic("voorwaardelijke-wijs", "Voorwaardelijke wijs", "would: the conditional", ["toekomende-tijd"]),
    topic("valse-vrienden", "Valse vrienden", "false friends", []),
    topic("idioms", "Idioom", "idioms", []),
    topic("vlaams", "Vlaams", "Belgian Dutch", []),
    topic("society", "Maatschappij", "society and ideas", ["lidwoorden"]),
]

PAGES = [
    page(
        "nl-subordinate-clauses",
        "Omdat sends the verb to the end",
        r"""
In a **subordinate clause**, every verb goes to the **end**. The clause starts with a subordinating conjunction (*omdat, dat, als, toen, hoewel, terwijl, of*) or a relative pronoun.

| Main clause | Subordinate clause |
| --- | --- |
| Ik ben moe. | ...omdat ik moe **ben**. |
| Hij komt morgen. | Ik denk dat hij morgen **komt**. |
| Ik bel je op. | ...als ik je **opbel**. |

Separable verbs join back together at the end: *opbel*.

## Want or omdat?

Both mean "because". **Want** is coordinating and keeps normal word order. **Omdat** is subordinating and sends the verb to the end.

:::examples
- Ik blijf thuis, want ik ben ziek. — I'm staying home, because I'm ill.
- Ik blijf thuis omdat ik ziek ben. — I'm staying home because I'm ill.
:::

The coordinating conjunctions are few: **en, maar, of** (when it means "or"), **want** and **dus**. *Dus* can also act as an adverb, with the verb straight after it: *dus blijven we thuis*. Every other conjunction sends the verb to the end.

## Verb clusters

With two verbs at the end, the order is often flexible. The finite verb can go first or last:

- *...omdat ik het **heb gedaan**.* / *...omdat ik het **gedaan heb**.*
- *...omdat ik morgen **moet werken**.* (*werken moet* is possible, but much less common.)

The Netherlands and Flanders lean different ways. Both are correct.

## A subordinate clause first

When the subordinate clause comes first, it counts as the first element of the main clause, so the main verb comes straight after: *Omdat ik ziek ben, **blijf** ik thuis.* Verb, comma, verb.

:::examples
- Ik denk dat het morgen gaat regenen. — I think it's going to rain tomorrow.
- Als je tijd hebt, kun je me helpen. — If you have time, you can help me.
- Hoewel het koud was, gingen we zwemmen. — Although it was cold, we went swimming.
:::
""",
        ["bijzinnen"],
        "nl-subordinate-clauses",
        explains=["conj-subordinating", "bijzinnen"],
    ),
    page(
        "nl-om-te",
        "Om ... te",
        r"""
Where English uses *to* + verb, Dutch uses **te** + infinitive, often inside **om ... te**, with everything else in between.

## Om ... te: in order to

:::examples
- Ik ga naar de winkel om brood te kopen. — I'm going to the shop to buy bread.
- Het is te koud om buiten te zitten. — It's too cold to sit outside.
- Ik heb geen tijd om te koken. — I have no time to cook.
:::

## Te without om

After verbs like *proberen, beginnen, vergeten, hopen, durven, besluiten*, the *om* is optional or left out:

- *Ik probeer (om) Nederlands te leren.*
- *Vergeet niet de deur dicht te doen.*

## No te

The modal verbs (*kunnen, willen, moeten, mogen, zullen*) and a few others (*gaan, komen, laten, zien, horen*) take a bare infinitive: *Ik wil slapen*, *Ik ga zwemmen*, *Laat me gaan*.

## Separable verbs

**Te** goes between the prefix and the verb: *op te bellen*, *mee te nemen*, *uit te gaan*.
""",
        ["bijzinnen"],
        "nl-om-te",
    ),
    page(
        "nl-relative-pronouns",
        "Die, dat and waar-",
        r"""
The relative pronoun follows the noun's article: **die** for de-words and all plurals, **dat** for singular het-words.

:::examples
- De man die daar staat, is mijn buurman. — The man who's standing there is my neighbour.
- Het boek dat ik lees, is spannend. — The book I'm reading is exciting.
- De boeken die ik lees, zijn spannend. — The books I'm reading are exciting.
:::

The relative clause is a subordinate clause, so the verb goes to the end.

## Wie after a preposition (people)

*De vrouw met wie ik praat.* (The woman I'm talking to.)

## Waar + preposition (things)

For things, Dutch doesn't say *met die* or *over dat*. It says **waarmee, waarover, waarop, waarin**:

- *Het mes waarmee ik snijd.* (The knife I'm cutting with.)
- *Het onderwerp waarover we praten.* (The subject we're talking about.)

This is the same pattern as *ermee, erover* on the page about **er**.

## Wat

After *alles, iets, niets, het enige* and after a whole clause, use **wat**: *Alles wat je zegt*, *Hij komt niet, wat jammer is.*
""",
        ["bijzinnen"],
        "nl-relative-pronouns",
    ),
    page(
        "nl-passive",
        "The passive: worden",
        r"""
The Dutch passive uses **worden** (to become) plus the participle, where English uses *to be*.

:::examples
- Het huis wordt verkocht. — The house is being sold.
- De brief werd gisteren geschreven. — The letter was written yesterday.
- Het boek is door een Belg geschreven. — The book was written by a Belgian.
:::

The one who does the action is introduced with **door** (by).

## Worden or zijn?

The present and simple past use **worden**. The perfect uses **zijn**, and *geworden* drops out:

| Tense | Passive |
| --- | --- |
| present | Het huis **wordt** verkocht. |
| simple past | Het huis **werd** verkocht. |
| perfect | Het huis **is** verkocht. |
| past perfect | Het huis **was** verkocht. |

So *het huis is verkocht* is "the house has been sold", not "the house is sold (right now, in progress)".

## Er + passive

Dutch can make a passive with no subject at all, with **er**: *Er wordt gebeld.* (Someone's at the door.) *Er wordt hier veel gelachen.* (People laugh a lot here.)
""",
        ["lijdende-vorm"],
        "nl-passive",
        explains=["lijdende-vorm"],
    ),
    page(
        "nl-conditional",
        "Zou: the conditional",
        r"""
**Zou** / **zouden** plus an infinitive is Dutch *would*.

| | zullen (past) |
| --- | --- |
| ik, jij, hij | zou |
| wij, jullie, zij | zouden |

## Politeness

:::examples
- Zou je me kunnen helpen? — Could you help me?
- Ik zou graag een kamer reserveren. — I'd like to book a room.
- Je zou eens met hem moeten praten. — You should talk to him some time.
:::

## If

Unlike French, Dutch allows *zou* on both sides of *als*, and speech often uses the simple past:

- *Als ik rijk was, zou ik een boot kopen.* (If I were rich, I'd buy a boat.)
- *Als ik rijk zou zijn, zou ik een boot kopen.* (Same meaning.)

Missed chances use *had* or *was*: *Als ik het had geweten, was ik gekomen.* (If I'd known, I'd have come.)

## Hearsay

Like French, the conditional marks a rumour: *De minister zou ontslag nemen.* (The minister is said to be resigning.)
""",
        ["voorwaardelijke-wijs"],
        "nl-conditional",
        explains=["voorwaardelijke-wijs"],
    ),
    page(
        "nl-untranslatables",
        "Gezellig, lekker and uitwaaien",
        r"""
Some Dutch words carry a whole idea that English needs a sentence for. You'll hear these every day.

## Gezellig

A place, an evening, a person or a conversation can be *gezellig*: cosy, convivial, relaxed, warm, with people you like. A birthday party is *gezellig*. So is a crowded café, a candle on a table, or a chat with a neighbour. *Ongezellig* is the opposite, and a real criticism.

*Het was heel gezellig!* is the standard thing to say when leaving.

## Lekker

Literally "tasty", but it's used for anything pleasant: *lekker weer* (lovely weather), *lekker slapen* (sleep well), *lekker bezig* (doing great). *Ik voel me niet lekker* means "I don't feel well".

## Uitwaaien

To go for a walk in strong wind, usually by the sea, to clear your head.

## Gedogen

To officially tolerate something that's technically illegal. The Dutch coffeeshop policy is the famous case. The word says a lot about how the Netherlands governs.

## Polderen

To reach a decision by long consensus between everyone involved. Named after the polders, reclaimed land that only stayed dry because neighbours cooperated.

## Borrel

Drinks and snacks after work or on a Friday afternoon. *Kom je ook naar de borrel?*

## Sterkte and beterschap

*Beterschap* is "get well soon". *Sterkte* ("strength") is what you wish someone facing something hard: an exam, an illness, a funeral. English has no single word for it.
""",
        ["idioms"],
        "nl-untranslatables",
    ),
    page(
        "nl-false-friends",
        "False friends",
        r"""
Dutch and English share so much that learners guess, and usually guess right. These are where guessing fails.

| Dutch | Means | Not |
| --- | --- | --- |
| eventueel | possibly, if need be | eventually (*uiteindelijk*) |
| actueel | current, topical | actual (*werkelijk*) |
| brutaal | cheeky | brutal (*wreed*) |
| slim | clever | slim (*slank*) |
| bellen | to phone; to ring | to bell |
| de brand | fire | brand (*het merk*) |
| de kok | cook | cock |
| de room | cream | room (*de kamer*) |
| het bad | bath | bad (*slecht*) |
| de rok | skirt | rock (*de rots*) |
| eerlijk | honest; fair | early (*vroeg*) |
| wandelen | to go for a walk | to wander (*zwerven*) |
| de winkel | shop | winkle |
| door | through; by | door (*de deur*) |
| durven | to dare | |
| de map | folder | map (*de kaart*) |
| de hut | cabin | hut |
| de gift | donation | gift (*het cadeau*) |
| het cadeau | present, gift | |

*Gift* is the classic one: a *gift* is a donation, and *het gif* is poison.
""",
        ["valse-vrienden"],
        "nl-false-friends",
        explains=["valse-vrienden"],
    ),
    page(
        "nl-flemish",
        "Flemish: Dutch in Belgium",
        r"""
This page is about Flemish, the Dutch spoken in Flanders, the northern half of Belgium. It is not the Dutch this app teaches: the app teaches the Dutch of the Netherlands. The written standard is shared, but speech differs, so here each Flemish word sits next to the Netherlands word you learn.

| Netherlands Dutch | Flemish (Belgium) | English |
| --- | --- | --- |
| jij, je | gij, ge | you |
| zin | goesting | desire, appetite |
| jeetje! | amai! | wow! |
| kom op, nou | allez | come on, well |
| mooi | schoon | beautiful (in the Netherlands, *schoon* means clean) |
| leuk | plezant | fun, pleasant |
| een biertje | een pintje | a beer |
| tevreden | content | pleased |
| even | efkes | a moment |
| deze hier | den dezen | this one |
| pardon? | wablieft? | sorry, what did you say? |

## Politeness

Flanders uses **u** more readily than the Netherlands, and speech is generally softer. The Dutch are often seen in Flanders as blunt; Flemish speakers in the Netherlands as formal.

## Pronunciation

In the north of the Netherlands the **g** is a hard rasp, harsher than the *ch* in Scottish *loch*. Flemish speakers, and many in the south of the Netherlands, say a soft **g**, voiced and further forward in the mouth.
""",
        ["vlaams"],
        "nl-flemish",
        explains=["vlaams"],
    ),
    page(
        "nl-idioms",
        "How Dutch idioms work",
        r"""
Dutch idioms are rooted in farming, the sea, and cheerful rudeness. Many have an English cousin with a different animal.

| Dutch | Literally | Meaning |
| --- | --- | --- |
| nu komt de aap uit de mouw | now the monkey comes out of the sleeve | now the truth comes out |
| met de deur in huis vallen | to fall into the house with the door | to get straight to the point |
| het regent pijpenstelen | it's raining pipe stems | it's raining cats and dogs |
| van een mug een olifant maken | to make an elephant of a mosquito | to make a mountain out of a molehill |
| dat is een eitje | that's a little egg | that's a piece of cake |

The literal translation is stored with each idiom in this pack. It's often what makes it stick.

*Met de deur in huis vallen* is also a fair description of the Dutch conversational style: people get to the point, and that isn't rude.
""",
        ["idioms"],
        "nl-idioms",
        explains=["idioms"],
    ),
]

NOUNS = nouns(
    """
# society and ideas
maatschappij | de | maatschappijen | society | society
regering | de | regeringen | government | society
wet | de | wetten | law | society
recht | het | rechten | right; law (the subject) | society
vrijheid | de | vrijheden | freedom | society
gelijkheid | de | - | equality | society
verkiezing | de | verkiezingen | election | society
oorlog | de | oorlogen | war | society
vrede | de | - | peace | society
milieu | het | - | environment | society
vervuiling | de | - | pollution | society
toekomst | de | - | future | society
verleden | het | - | past | society
geschiedenis | de | - | history | society
cultuur | de | culturen | culture | society
taal | de | talen | language | society
probleem | het | problemen | problem | society
oplossing | de | oplossingen | solution | society
reden | de | redenen | reason | society
mening | de | meningen | opinion | society
idee | het | ideeën | idea | society
keuze | de | keuzes | choice | society
kans | de | kansen | chance | society
succes | het | successen | success | society
angst | de | angsten | fear | feelings
vreugde | de | - | joy | feelings
woede | de | - | anger | feelings
schaamte | de | - | shame | feelings
herinnering | de | herinneringen | memory (something remembered) | feelings
droom | de | dromen | dream | feelings
hoop | de | - | hope | feelings
liefde | de | - | love | feelings
vriendschap | de | vriendschappen | friendship | feelings
# the Netherlands
borrel | de | borrels | after-work drinks | idioms
gezelligheid | de | - | cosiness, conviviality | idioms
polder | de | polders | reclaimed land | nature
dijk | de | dijken | dyke | nature
klomp | de | klompen | clog | clothing
molen | de | molens | windmill; mill | nature
# false friends
brand | de | branden | fire | valse-vrienden
merk | het | merken | brand | valse-vrienden
room | de | - | cream | valse-vrienden
kamer | de | kamers | room | valse-vrienden
map | de | mappen | folder | valse-vrienden
gift | de | giften | donation | valse-vrienden
"""
)

ADJECTIVES = adjectives(
    """
gezellig, gezellige | cosy, convivial, fun
eerlijk, eerlijke | honest; fair
brutaal, brutale | cheeky
slim, slimme | clever
eventueel, eventuele | possible
actueel, actuele | current, topical
bijzonder, bijzondere | special, unusual
belangrijk, belangrijke | important
mogelijk, mogelijke | possible
ongerust, ongeruste | worried
trots, trotse | proud
jaloers, jaloerse | jealous
gul, gulle | generous
dom, domme | stupid
zacht, zachte | soft, gentle
vers, verse | fresh
vals, valse | false; out of tune
nuchter, nuchtere | sober; down-to-earth
zuinig, zuinige | thrifty, careful with money
eigenwijs, eigenwijze | headstrong, know-it-all
stoer, stoere | tough, cool
"""
)
for a in ADJECTIVES[1:6]:
    a["tags"].append("valse-vrienden")

VERBS = [
    verb("zich afvragen", "vraag", "to wonder", ["scheidbare-werkwoorden", "wederkerende-werkwoorden"],
         prefix="af", refl=True, past="vroeg vroegen", pp="afgevraagd",
         example="Ik vraag me af of hij komt.", example_en="I wonder whether he's coming."),
    verb("overleggen", "overleg", "to consult, to discuss", [], pp="overlegd",
         example="We moeten even overleggen.", example_en="We need to talk it over."),
    verb("beslissen", "beslis", "to decide", [],
         example="Jij mag beslissen.", example_en="You can decide."),
    verb("ontmoeten", "ontmoet", "to meet", [],
         example="Leuk je te ontmoeten!", example_en="Nice to meet you!"),
    verb("verdienen", "verdien", "to earn; to deserve", [],
         example="Hij verdient veel geld.", example_en="He earns a lot of money."),
    verb("veranderen", "verander", "to change, become different", [], aux="zijn",
         example="Er is veel veranderd.", example_en="A lot has changed."),
    verb("ontdekken", "ontdek", "to discover", [],
         example="Ik heb een leuk café ontdekt.", example_en="I've discovered a nice café."),
    verb("gebeuren", "gebeur", "to happen", [], aux="zijn",
         example="Wat is er gebeurd?", example_en="What happened?"),
    verb("bestaan", "besta", "to exist", [], present="besta bestaat bestaat bestaan bestaan bestaan",
         past="bestond bestonden", pp="bestaan",
         example="Dat woord bestaat niet.", example_en="That word doesn't exist."),
    verb("verwachten", "verwacht", "to expect", [],
         example="Dat had ik niet verwacht.", example_en="I didn't expect that."),
    verb("vergelijken", "vergelijk", "to compare", [], past="vergeleek vergeleken", pp="vergeleken",
         example="Je kunt het niet vergelijken.", example_en="You can't compare them."),
    verb("beloven", "beloof", "to promise", [],
         example="Ik beloof het.", example_en="I promise."),
    verb("durven", "durf", "to dare", [],
         example="Durf jij te springen?", example_en="Do you dare to jump?"),
    verb("klagen", "klaag", "to complain", [],
         example="Hij klaagt altijd over het weer.", example_en="He always complains about the weather."),
    verb("zeuren", "zeur", "to nag, to whine", [],
         example="Niet zo zeuren!", example_en="Stop whining!"),
    verb("gedogen", "gedoog", "to tolerate (officially)", ["idioms"],
         example="De gemeente gedoogt het.", example_en="The council tolerates it."),
    verb("uitleggen", "leg", "to explain", ["scheidbare-werkwoorden"], prefix="uit",
         example="Kun je dat uitleggen?", example_en="Can you explain that?"),
    verb("voorstellen", "stel", "to propose; to introduce", ["scheidbare-werkwoorden"], prefix="voor",
         example="Mag ik mijn vriend voorstellen?", example_en="May I introduce my friend?"),
    verb("nadenken", "denk", "to think (something over)", ["scheidbare-werkwoorden"], prefix="na",
         past="dacht dachten", pp="nagedacht",
         example="Ik moet erover nadenken.", example_en="I need to think about it."),
    verb("meedoen", "doe", "to take part, to join in", ["scheidbare-werkwoorden"], prefix="mee",
         past="deed deden", pp="meegedaan",
         example="Doe je mee?", example_en="Are you joining in?"),
    verb("ophouden", "houd", "to stop", ["scheidbare-werkwoorden"], prefix="op",
         present="houd houdt houdt houden houden houden", past="hield hielden", pp="opgehouden",
         example="Hou op!", example_en="Stop it!"),
    verb("toegeven", "geef", "to admit; to give in", ["scheidbare-werkwoorden"], prefix="toe",
         past="gaf gaven", pp="toegegeven",
         example="Ik geef het toe, ik had ongelijk.", example_en="I admit it, I was wrong."),
    verb("uitwaaien", "waai", "to blow the cobwebs away (walk in the wind)", ["scheidbare-werkwoorden", "idioms"],
         prefix="uit",
         example="We gaan uitwaaien op het strand.", example_en="We're going for a windy walk on the beach."),
]

IDIOMS = phrases(
    """
nu komt de aap uit de mouw | now the truth comes out | now the monkey comes out of the sleeve
met de deur in huis vallen | to get straight to the point | to fall into the house with the door
het regent pijpenstelen | it's raining cats and dogs | it's raining pipe stems
iets onder de knie hebben | to have mastered something | to have something under the knee
een appeltje met iemand te schillen hebben | to have a bone to pick with someone | to have an apple to peel with someone
de kat uit de boom kijken | to wait and see | to watch the cat out of the tree
nu breekt mijn klomp | well I never! | now my clog breaks
tussen de soep en de aardappelen | in between, squeezed in | between the soup and the potatoes
door de mand vallen | to be found out | to fall through the basket
iemand een oor aannaaien | to con someone | to sew an ear on someone
ze zijn koek en ei | they're thick as thieves | they're cake and egg
ik heb er een hard hoofd in | I'm pessimistic about it | I have a hard head in it
wie het eerst komt, het eerst maalt | first come, first served | who comes first, grinds first
de koe bij de hoorns vatten | to take the bull by the horns | to take the cow by the horns
met je neus in de boter vallen | to strike lucky | to fall with your nose in the butter
een kat in de zak kopen | to buy a pig in a poke | to buy a cat in the bag
iets uit je duim zuigen | to make something up | to suck something from your thumb
hij heeft ze niet allemaal op een rijtje | he's not all there | he doesn't have them all in a row
oost west, thuis best | there's no place like home | east, west, home is best
twee vliegen in één klap | to kill two birds with one stone | two flies in one swat
op je tenen lopen | to push yourself to the limit | to walk on your toes
van een mug een olifant maken | to make a mountain out of a molehill | to make an elephant of a mosquito
iemand in de maling nemen | to pull someone's leg | to take someone into the grinder
het zal me worst wezen | I couldn't care less | it'll be sausage to me
aan de bel trekken | to raise the alarm | to pull the bell
de puntjes op de i zetten | to dot the i's and cross the t's | to put the dots on the i
dat is een eitje | that's a piece of cake | that's a little egg
tot in de puntjes | down to the last detail | into the little points
dat kost een rib uit je lijf | that costs an arm and a leg | that costs a rib from your body
een gat in de lucht springen | to jump for joy | to jump a hole in the air
met de noorderzon vertrekken | to vanish without paying | to leave with the northern sun
roeien met de riemen die je hebt | to make do with what you have | to row with the oars you have
nood breekt wet | necessity knows no law | need breaks law
"""
    ,
    ["idioms"],
)

EXPRESSIONS = phrases(
    """
doe normaal | act normal, calm down | do normal
doe maar gewoon, dan doe je al gek genoeg | just act normal, that's crazy enough | just act ordinary, then you're acting crazy enough
het valt mee | it's not as bad as expected | it falls along
het valt tegen | it's worse than expected, disappointing | it falls against
dat klopt | that's right | that knocks
je weet wel | you know | you know well
nou ja | oh well
hè hè | phew, finally
echt waar? | really? | truly true?
jeetje | gosh, wow
succes! | good luck!
sterkte! | be strong, I'm thinking of you | strength!
beterschap! | get well soon! | betterment!
gefeliciteerd! | congratulations!; happy birthday!
lekker bezig! | nice going!, well done! | tastily busy
gatverdamme | yuck, gross
het was heel gezellig | it was really lovely (said when leaving)
niet zo zeuren | stop whining | not so nag
ik heb er zin in | I'm looking forward to it | I have mind in it
kom op! | come on!
"""
    ,
    ["uitdrukkingen"],
)

CONNECTIVES = connectors(
    "connective",
    """
desondanks | nevertheless | conn-contrast | Het was moeilijk; desondanks is het gelukt. | It was hard; nevertheless, it worked.
integendeel | on the contrary | conn-contrast | Hij is niet verlegen; integendeel, hij praat met iedereen. | He isn't shy; on the contrary, he talks to everyone.
trouwens | by the way; besides | conn-addition | Trouwens, heb je mijn sleutels gezien? | By the way, have you seen my keys?
overigens | incidentally | conn-addition | Het eten was lekker; de wijn was overigens ook goed. | The food was good; incidentally, so was the wine.
immers | after all | conn-cause | Hij kan niet komen; hij is immers ziek. | He can't come; he's ill, after all.
kortom | in short | conn-consequence | Kortom, het was een geweldige dag. | In short, it was a great day.
zodoende | and so, as a result | conn-consequence | De trein reed niet; zodoende kwam ik te laat. | The train wasn't running; as a result, I was late.
uiteindelijk | in the end | conn-sequence | We twijfelden lang, maar uiteindelijk zijn we gebleven. | We hesitated a long time, but in the end we stayed.
""",
    ["verbindingswoorden"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
zodat | so that | conj-subordinating | Ik spreek langzaam zodat je het begrijpt. | I speak slowly so that you understand.
tenzij | unless | conj-subordinating | We gaan fietsen, tenzij het regent. | We'll go cycling, unless it rains.
zodra | as soon as | conj-subordinating | Bel me zodra je er bent. | Call me as soon as you get there.
sinds | since | conj-subordinating | Sinds ik hier woon, fiets ik elke dag. | Since I've lived here, I've cycled every day.
doordat | because (the cause of a result) | conj-subordinating | Doordat de trein vertraging had, kwam ik te laat. | Because the train was delayed, I was late.
alsof | as if | conj-subordinating | Hij doet alsof hij het niet weet. | He acts as if he doesn't know.
zolang | as long as | conj-subordinating | Je mag blijven zolang je wilt. | You can stay as long as you like.
""",
    ["voegwoorden"],
)

ITEMS = PAGES + interleave(IDIOMS, EXPRESSIONS, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# nl-subordinate-clauses, nl-om-te and nl-relative-pronouns share the
# "bijzinnen" tag, so each takes its own slice of the tegenwoordige-tijd
# pool. nl-passive pairs with society vocabulary — formal/legal Dutch is
# where "worden" shows up constantly. nl-false-friends uses every
# valse-vrienden word, an exact match. nl-idioms and nl-untranslatables
# split the idioms pool by hand; the rest becomes automatic "Idioom" Units
# via LABELS below.
UNITS = [
    {
        "title": "Bijzinnen",
        "page_id": "nl-subordinate-clauses",
        "word_ids": ["zich-afvragen", "overleggen", "beslissen", "ontmoeten", "verdienen", "veranderen"],
    },
    {
        "title": "Om ... te",
        "page_id": "nl-om-te",
        "word_ids": ["ontdekken", "gebeuren", "bestaan", "verwachten", "vergelijken", "beloven"],
    },
    {
        "title": "Die, dat en waar-",
        "page_id": "nl-relative-pronouns",
        "word_ids": ["durven", "klagen", "zeuren", "gedogen", "uitleggen", "voorstellen"],
    },
    {
        "title": "De lijdende vorm",
        "page_id": "nl-passive",
        "word_ids": ["regering", "wet", "recht", "vrijheid", "gelijkheid", "verkiezing"],
    },
    {
        "title": "Zou: de voorwaardelijke wijs",
        "page_id": "nl-conditional",
        "word_ids": ["nadenken", "meedoen", "ophouden", "toegeven", "uitwaaien", "zodat"],
    },
    {
        "title": "Onvertaalbare woorden",
        "page_id": "nl-untranslatables",
        "word_ids": ["gezelligheid", "borrel", "dat-is-een-eitje", "tot-in-de-puntjes", "oost-west-thuis-best", "roeien-met-de-riemen-die-je-hebt"],
    },
    {
        "title": "Valse vrienden",
        "page_id": "nl-false-friends",
        "word_ids": ["brand", "merk", "room", "kamer", "map", "gift"],
    },
    {
        "title": "Vlaams",
        "page_id": "nl-flemish",
        "word_ids": ["doe-normaal", "echt-waar", "nou-ja", "he-he", "jeetje", "kom-op"],
    },
    {
        "title": "Idioom",
        "page_id": "nl-idioms",
        "word_ids": [
            "nu-komt-de-aap-uit-de-mouw",
            "met-de-deur-in-huis-vallen",
            "het-regent-pijpenstelen",
            "iets-onder-de-knie-hebben",
            "een-appeltje-met-iemand-te-schillen-hebben",
            "de-kat-uit-de-boom-kijken",
            "nu-breekt-mijn-klomp",
            "tussen-de-soep-en-de-aardappelen",
        ],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "feelings": "Gevoelens",
}

PACK = pack(
    "nl-fluency-v1",
    7,
    "nl",
    "Nederlands · Vloeiend (B1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Oefening"),
)
