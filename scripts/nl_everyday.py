"""nl-everyday-v1: A2. The past tenses, separable and reflexive verbs, adjective
endings, the little words (er, toch, even) and the vocabulary of daily life."""

from common import build_units, interleave, page, pack, topic, topic_labels
from nl_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("scheidbare-werkwoorden", "Scheidbare werkwoorden", "separable verbs", ["tegenwoordige-tijd"]),
    topic("wederkerende-werkwoorden", "Wederkerende werkwoorden", "reflexive verbs", ["tegenwoordige-tijd"]),
    topic("modale-partikels", "Modale partikels", "modal particles: even, toch, maar", ["tegenwoordige-tijd"]),
    topic("er", "Er", "the four jobs of er", ["tegenwoordige-tijd"]),
    topic("zinsdelen", "Zinsdelen", "the parts of a sentence", ["woordvolgorde"]),
    topic("clothing", "Kleding", "clothing", ["lidwoorden"]),
    topic("weather", "Weer", "weather", ["lidwoorden"]),
    topic("travel", "Reizen", "travel", ["lidwoorden"]),
    topic("work", "Werk", "work and study", ["lidwoorden"]),
    topic("health", "Gezondheid", "health", ["lidwoorden"]),
    topic("leisure", "Vrije tijd", "free time", ["lidwoorden"]),
    topic("feelings", "Gevoelens", "feelings and character", ["bijvoeglijke-naamwoorden"]),
    topic("shopping", "Winkelen", "shopping and money", ["lidwoorden"]),
    topic("uitdrukkingen", "Uitdrukkingen", "set phrases and idioms", []),
    {
        "id": "conn-consequence",
        "kind": "connective-class",
        "label": "Gevolg",
        "labelGloss": "the next statement is the result of the last one (dus, daarom)",
        "order": 4,
        "appliesTo": {"kind": "connective"},
        "dependsOn": [],
    },
]

PAGES = [
    page(
        "nl-perfect",
        "The perfect tense",
        r"""
The **voltooid tegenwoordige tijd** (perfectum) is the normal way to talk about the past in conversation: *ik heb gegeten* is "I ate" and "I have eaten".

It's **hebben** or **zijn** plus the **past participle**, and the participle goes to the end of the clause.

:::examples
- Ik heb gisteren pizza gegeten. — I ate pizza yesterday.
- We zijn naar Gent gegaan. — We went to Ghent.
- Heb je de film al gezien? — Have you seen the film yet?
:::

## Weak verbs: ge- + stem + t or d

Most verbs are **weak**: **ge** + stem + **t** or **d**. Which one? Look at the last letter of the stem. If it's in **'t kofschip** (t, k, f, s, ch, p), use **t**. Otherwise use **d**.

| Infinitive | Stem | Participle |
| --- | --- | --- |
| werken | werk | gewerkt |
| maken | maak | gemaakt |
| fietsen | fiets | gefietst |
| wonen | woon | gewoond |
| spelen | speel | gespeeld |

Use the stem's sound in the infinitive: *leven → leef*, but v isn't in 't kofschip, so it's *geleefd*. *Reizen → gereisd* for the same reason.

If the stem already ends in t or d, add nothing: *praten → gepraat*, *antwoorden → geantwoord*.

## Strong verbs: ge- + changed stem + en

Strong verbs change their vowel and end in **-en**. They have to be learned:

| | | |
| --- | --- | --- |
| eten → gegeten | drinken → gedronken | zien → gezien |
| lezen → gelezen | schrijven → geschreven | nemen → genomen |
| komen → gekomen | gaan → gegaan | doen → gedaan |
| zijn → geweest | hebben → gehad | brengen → gebracht |

## No ge- after be-, ge-, ver-, her-, ont-, er-

These prefixes are never stressed, and the participle doesn't add **ge**: *betalen → betaald*, *vertellen → verteld*, *gebruiken → gebruikt*, *ontmoeten → ontmoet*.

:::predict{prompt="ik (werken)" answer="heb gewerkt"}
:::
""",
        ["voltooid-tegenwoordige-tijd"],
        "nl-perfect",
        explains=["voltooid-tegenwoordige-tijd"],
    ),
    page(
        "nl-zijn-or-hebben",
        "Hebben or zijn?",
        r"""
Most verbs make their perfect with **hebben**. **Zijn** is for verbs that describe a **change of place or state**, plus *zijn* and *blijven* themselves.

| Zijn verbs | |
| --- | --- |
| gaan, komen, vertrekken, aankomen | movement with a direction |
| worden, sterven, beginnen, vallen | change of state |
| zijn, blijven | the exceptions |

## Movement: it depends on the destination

Verbs like *lopen*, *fietsen*, *rijden* and *zwemmen* take **hebben** when you describe the activity, and **zijn** when there's a destination:

:::examples
- Ik heb een uur gefietst. — I cycled for an hour.
- Ik ben naar huis gefietst. — I cycled home.
- We hebben gezwommen. — We went swimming.
- We zijn naar de overkant gezwommen. — We swam to the other side.
:::

## Vergeten

*Vergeten* takes both, and most people say *Ik ben mijn sleutels vergeten*. The drills use zijn.

## Sort them

Which helper goes with each participle?

:::sort{groups="Hebben (no change of place or state): gewerkt, gekookt, geslapen, gelachen, een uur gefietst | Zijn (change of place or state): vertrokken, gestorven, gebleven, begonnen, naar huis gefietst"}
:::

## Fill in hebben or zijn

:::cloze{sentence="Ik ___ gisteren met de trein naar Utrecht gegaan." blank="ben"}
:::

:::cloze{sentence="Wij ___ de hele middag in het park gewandeld." blank="hebben"}
:::

:::cloze{sentence="Mijn opa ___ vorig jaar tachtig geworden." blank="is"}
:::

:::cloze{sentence="Hij ___ in een uur naar Leiden gefietst." blank="is"}
:::
""",
        ["voltooid-tegenwoordige-tijd"],
        "nl-zijn-or-hebben",
    ),
    page(
        "nl-zinsdelen",
        "The parts of a sentence",
        r"""
Dutch schools teach grammar by **zinsdelen**: take a sentence apart and name each part. Grammar books, teachers and NT2 exams all use these names. Finding the parts is also how you check your own word order.

Find them in this order. Each step uses the one before.

## 1. Persoonsvorm

The finite verb, the one verb that changes with the time or the subject. Three ways to find it:

- Change the time: *Ik **werk** hier* becomes *Ik **werkte** hier*. The word that changes is the persoonsvorm.
- Change the subject to plural: *Hij **loopt*** becomes *Zij **lopen***.
- Make a yes/no question: the persoonsvorm moves to the front. *Jij **hebt** een fiets* becomes ***Heb** jij een fiets?*

In a main clause it's always the second part (see *Verb second*).

## 2. Onderwerp

Ask **wie of wat + persoonsvorm?** *Wie heeft een cadeau gekocht?* **Lisa**. The onderwerp agrees with the persoonsvorm: *ik loop*, *wij lopen*.

## 3. Werkwoordelijk gezegde

**All the verbs** in the sentence: the persoonsvorm, plus any infinitive or participle, plus the prefix of a separable verb like *opbellen*. In *Lisa heeft gisteren een cadeau gekocht*, it is *heeft … gekocht*. The persoonsvorm is always part of it.

## 4. Lijdend voorwerp

Ask **wie of wat + gezegde + onderwerp?** *Wat heeft Lisa gekocht?* **Een cadeau**. Many sentences have none: *Daan fietst naar huis* doesn't.

## 5. Meewerkend voorwerp

The person who gets something, or for whom something is done. Ask **aan wie?** or **voor wie?** It either has *aan* or *voor* already, or you could add it:

:::examples
- Ik geef mijn moeder bloemen. — I'm giving my mother flowers.
- Ik geef bloemen aan mijn moeder. — I'm giving flowers to my mother.
- Ik koop een cadeau voor mijn zus. — I'm buying a present for my sister.
:::

Here *mijn moeder*, *aan mijn moeder* and *voor mijn zus* are each the meewerkend voorwerp.

## 6. Bijwoordelijke bepaling

Everything else that says **when, where, how or why**: *gisteren*, *in Delft*, *met de trein*, *omdat het regent*. A sentence can have several, and each is a part of its own: *gisteren* and *in Delft* are two.

## Your turn

Find every part. A part the sentence doesn't have stays empty.

:::parse{sentence="Mijn buurman heeft gisteravond zijn auto in de garage gezet." en="My neighbour put his car in the garage last night."}
Persoonsvorm: heeft
Onderwerp: Mijn buurman
Werkwoordelijk gezegde: heeft gezet
Lijdend voorwerp: zijn auto
Meewerkend voorwerp: -
Bijwoordelijke bepaling: gisteravond | in de garage
:::

:::parse{sentence="Vanavond stuurt Tom zijn oma een kaart." en="Tonight Tom is sending his grandma a card."}
Persoonsvorm: stuurt
Onderwerp: Tom
Werkwoordelijk gezegde: stuurt
Lijdend voorwerp: een kaart
Meewerkend voorwerp: zijn oma
Bijwoordelijke bepaling: Vanavond
:::

:::parse{sentence="Na het werk fietst Daan met zijn zus naar huis." en="After work, Daan cycles home with his sister."}
Persoonsvorm: fietst
Onderwerp: Daan
Werkwoordelijk gezegde: fietst
Lijdend voorwerp: -
Meewerkend voorwerp: -
Bijwoordelijke bepaling: Na het werk | met zijn zus | naar huis
:::

:::parse{sentence="De docent legt de regel nog een keer aan de klas uit." en="The teacher explains the rule to the class once more."}
Persoonsvorm: legt
Onderwerp: De docent
Werkwoordelijk gezegde: legt uit
Lijdend voorwerp: de regel
Meewerkend voorwerp: aan de klas
Bijwoordelijke bepaling: nog een keer
:::

:::parse{sentence="Heb jij je vader de foto's al gestuurd?" en="Have you sent your father the photos yet?"}
Persoonsvorm: Heb
Onderwerp: jij
Werkwoordelijk gezegde: Heb gestuurd
Lijdend voorwerp: de foto's
Meewerkend voorwerp: je vader
Bijwoordelijke bepaling: al
:::

## Zijn, worden, blijven

With these verbs (and *lijken*, *blijken*, *heten*) the sentence says what the onderwerp **is** or becomes: *Het huis is groot*. The verb and *groot* together are the **naamwoordelijk gezegde**, which takes the place of the werkwoordelijk gezegde. The games here leave those sentences out.
""",
        ["zinsdelen"],
        "nl-zinsdelen",
        explains=["zinsdelen"],
    ),
    page(
        "nl-imperfect",
        "The simple past",
        r"""
The **onvoltooid verleden tijd** (imperfectum) is the past for stories, descriptions and habits. In conversation, Dutch prefers the perfect for single events. In writing and storytelling, the simple past takes over.

## Weak verbs: stem + te(n) or de(n)

The same **'t kofschip** rule as the participle: t, k, f, s, ch, p take **-te**, everything else takes **-de**. The plural adds **-n**.

| | werken | wonen |
| --- | --- | --- |
| ik, jij, hij | werkte | woonde |
| wij, jullie, zij | werkten | woonden |

## Strong verbs: a new vowel

| Infinitive | Singular | Plural |
| --- | --- | --- |
| zijn | was | waren |
| hebben | had | hadden |
| gaan | ging | gingen |
| komen | kwam | kwamen |
| eten | at | aten |
| drinken | dronk | dronken |
| zien | zag | zagen |
| doen | deed | deden |
| lezen | las | lazen |
| kijken | keek | keken |

## Which past?

- A single finished event, in speech: perfect. *Ik heb hem gisteren gezien.*
- A background, a habit, or a story: simple past. *Toen ik klein was, woonde ik in Delft.*

:::examples
- Het regende en ik had geen paraplu. — It was raining and I had no umbrella.
- Vroeger fietste ik elke dag naar school. — I used to cycle to school every day.
- Hij las een boek terwijl zij kookte. — He was reading a book while she cooked.
:::
""",
        ["onvoltooid-verleden-tijd"],
        "nl-imperfect",
        explains=["onvoltooid-verleden-tijd"],
    ),
    page(
        "nl-separable-verbs",
        "Separable verbs",
        r"""
Many Dutch verbs start with a prefix that **splits off** in a main clause and goes to the end. English has something similar in phrasal verbs (*call up*, *pick up*), but Dutch moves the particle much further away.

| Verb | Main clause | Meaning |
| --- | --- | --- |
| opbellen | Ik bel je morgen op. | to phone |
| meenemen | Neem je een jas mee? | to take along |
| opstaan | Ik sta om zeven uur op. | to get up |
| uitgaan | We gaan vanavond uit. | to go out |
| aankomen | De trein komt om vijf uur aan. | to arrive |
| schoonmaken | Ik maak de keuken schoon. | to clean |

The stress falls on the prefix: *OPbellen*, *MEEnemen*. That's how you can tell a separable verb from an inseparable one like *be-TA-len*.

## When it stays together

The verb stays in one piece when it's at the end of the clause:

- After a modal: *Ik wil je morgen **opbellen**.*
- In a subordinate clause: *...omdat ik je morgen **opbel**.*

## Participle and te

**ge** goes between prefix and verb: *opgebeld*, *meegenomen*, *aangekomen*. So does **te**: *Ik probeer je op **te** bellen.*

:::examples
- Hij heeft me gisteren opgebeld. — He called me yesterday.
- Vergeet niet je paraplu mee te nemen. — Don't forget to take your umbrella.
:::
""",
        ["scheidbare-werkwoorden"],
        "nl-separable-verbs",
        explains=["scheidbare-werkwoorden"],
    ),
    page(
        "nl-modal-verbs",
        "Kunnen, willen, moeten, mogen",
        r"""
The modal verbs take an infinitive, and the infinitive goes to the **end** of the clause.

| | kunnen | willen | moeten | mogen | zullen |
| --- | --- | --- | --- | --- | --- |
| ik | kan | wil | moet | mag | zal |
| jij | kunt / kan | wilt / wil | moet | mag | zult / zal |
| hij | kan | wil | moet | mag | zal |
| wij | kunnen | willen | moeten | mogen | zullen |

:::examples
- Ik kan morgen niet komen. — I can't come tomorrow.
- Wil je iets drinken? — Would you like something to drink?
- Je mag hier niet roken. — You're not allowed to smoke here.
:::

## Moeten niet is not must not

*Je moet niet...* means "you shouldn't" or "you don't have to", depending on context. "You must not" is **je mag niet**. English speakers get this backwards.

## The missing verb of motion

Dutch drops *gaan* after a modal when a direction makes it obvious:

- *Ik moet naar huis.* (I have to go home.)
- *Wil je mee?* (Do you want to come along?)
- *Ik mag vanavond naar het feest.* (I'm allowed to go to the party tonight.)

## Zullen

*Zullen* makes the future (*ik zal het doen*, I'll do it) and suggestions: *Zullen we gaan?* (Shall we go?)
""",
        ["toekomende-tijd"],
        "nl-modal-verbs",
    ),
    page(
        "nl-reflexive-verbs",
        "Reflexive verbs: zich",
        r"""
Some Dutch verbs always come with a reflexive pronoun. Their English equivalents often don't: *zich vergissen* (to be mistaken), *zich herinneren* (to remember), *zich haasten* (to hurry).

| | zich vergissen |
| --- | --- |
| ik | vergis me |
| jij | vergist je |
| hij / zij | vergist zich |
| wij | vergissen ons |
| jullie | vergissen je |
| zij | vergissen zich |

*U* takes **zich** or **u**: *u vergist zich*.

## Where the pronoun goes

Right after the finite verb, or after the subject if the subject follows the verb:

:::examples
- Ik voel me niet lekker. — I don't feel well.
- Herinner je je die dag? — Do you remember that day?
- Ik heb me vergist. — I made a mistake.
:::

Reflexive verbs take **hebben** in the perfect, unlike French.

## Fill in the pronoun

:::cloze{sentence="Mijn broer heeft ___ in de datum vergist." blank="zich"}
:::

:::cloze{sentence="Wij vervelen ___ nooit op vakantie." blank="ons"}
:::

:::cloze{sentence="Herinner jij ___ onze eerste les nog?" blank="je"}
:::

:::cloze{sentence="De kinderen moeten ___ haasten, de bus vertrekt zo." blank="zich"}
:::
""",
        ["wederkerende-werkwoorden"],
        "nl-reflexive-verbs",
        explains=["wederkerende-werkwoorden"],
    ),
    page(
        "nl-adjective-endings",
        "Groot or grote?",
        r"""
An adjective after the noun (*het huis is groot*) never changes. An adjective **before** a noun takes **-e**, with one exception.

## The exception: een + het-word

No **-e** when the noun is a singular **het-word** with **een**, **geen**, or no article at all.

| | de-word (de tafel) | het-word (het huis) |
| --- | --- | --- |
| de / het | de grote tafel | het grote huis |
| een | een grote tafel | een **groot** huis |
| plural | grote tafels | grote huizen |

So: *een groot huis*, *geen mooi weer*, *lekker brood*, but *het grote huis* and *een grote auto*.

:::examples
- We hebben een groot huis gekocht. — We bought a big house.
- Het grote huis op de hoek is te koop. — The big house on the corner is for sale.
- Ik zoek een goedkope fiets. — I'm looking for a cheap bike.
- Deze soep is heel lekker. — This soup is really tasty.
:::

## Spelling

The long-and-short vowel rule again: *groot → grote*, *wit → witte*, *lief → lieve*, *vies → vieze*.

Adjectives ending in **-en** never take -e: *een open deur*, *de gouden ring*. Neither do a few loanwords: *oranje*, *roze*, *gratis*.

## Material adjectives

Materials take **-en**: *een houten tafel* (wooden), *een gouden ring*, *een wollen trui*. They never take an extra -e, so it is *de houten tafel* too.

Plastic and nylon stay as they are: *een plastic tas*, *een nylon touw*.
""",
        ["bijvoeglijke-naamwoorden"],
        "nl-adjective-endings",
        explains=["bijvoeglijke-naamwoorden"],
    ),
    page(
        "nl-er",
        "The four jobs of er",
        r"""
**Er** is one of the hardest words in Dutch, because English has nothing that does all of its jobs. Learners usually pick it up by ear. Here are its four uses.

## 1. There is, there are

*Er is een probleem.* *Er zijn veel mensen.* The same as English *there*.

## 2. A place already mentioned

*Ben je in Parijs geweest? Ja, ik ben er vorig jaar geweest.* (Yes, I was there last year.) Unstressed; *daar* is the stressed version.

## 3. With a number: of them

When a number or quantity has no noun after it, Dutch needs **er**:

*Hoeveel kinderen heb je? Ik heb er twee.* (I have two.) Leaving out *er* is the mistake that marks you as a foreigner.

## 4. With a preposition: it, them

Dutch doesn't say *op het* or *met het* for things. It says **erop**, **ermee**, **erover**, **ervan**:

:::examples
- Ik denk erover na. — I'm thinking about it.
- Wat vind je ervan? — What do you think of it?
- Ik ben er blij mee. — I'm happy with it.
:::

*Met* becomes *mee* and *tot* becomes *toe*: *ermee*, *ertoe*. The two parts can split: *Ik heb er niet over nagedacht.*

## In passive-like sentences

*Er wordt gebeld.* (Someone's ringing the doorbell.) *Er wordt veel gefietst in Nederland.* (People cycle a lot in the Netherlands.)
""",
        ["er"],
        "nl-er",
        explains=["er"],
    ),
    page(
        "nl-modal-particles",
        "Even, toch, maar, eens, hoor",
        r"""
Dutch speakers soften, stress and colour almost every request with small words that don't translate. Get them right and you sound friendly. Leave them out and a correct sentence can sound curt.

| Particle | Effect | Example |
| --- | --- | --- |
| even | "just quickly", makes a request small | Kun je even helpen? |
| maar | "go ahead", encouraging | Kom maar binnen. |
| eens | "some time", casual | Kijk eens! |
| toch | "surely", "after all", seeks agreement | Je komt toch? |
| hoor | reassures, softens | Het is goed, hoor. |
| wel | contradicts a negative, "actually" | Ik kom wel. |
| nou | impatience or emphasis | Nou, en? |
| gewoon | "just", "simply" | Doe gewoon normaal. |

They stack, and the order is fixed: *Kom **toch maar even** binnen.* (Do come in for a bit, go on.)

## Compare

- *Geef me het zout.* Give me the salt. (Blunt.)
- *Geef me **even** het zout.* Pass me the salt for a sec.
- *Wil je me **even** het zout geven?* Could you pass me the salt? (Friendly.)

The best way to learn them is to notice them. Once you start hearing *even*, you'll hear it everywhere.
""",
        ["modale-partikels"],
        "nl-modal-particles",
        explains=["modale-partikels"],
    ),
    page(
        "nl-comparisons",
        "Groter, grootst, liever",
        r"""
The comparative adds **-er**; the superlative adds **-st**.

| | comparative | superlative |
| --- | --- | --- |
| groot | groter | grootst |
| mooi | mooier | mooist |
| duur | duurder (-r takes -der) | duurst |

Compare with **dan**: *Hij is groter **dan** ik.* Equal with **even ... als**: *Ze is even oud **als** ik.*

Before a noun the superlative takes -e: *het grootste huis*. After the verb, use **het**: *Dit huis is **het** grootst.*

## Irregular

| | | |
| --- | --- | --- |
| goed | beter | best |
| veel | meer | meest |
| weinig | minder | minst |
| graag | liever | liefst |

## Graag, liever, het liefst

*Graag* turns a verb into "like to": *Ik lees graag* (I like reading). *Liever* is "prefer": *Ik drink liever thee.* *Het liefst* is "most of all": *Ik ga het liefst naar zee.*

This is how Dutch talks about preferences. *Ik hou van lezen* is stronger, closer to "I love reading".
""",
        ["bijvoeglijke-naamwoorden"],
        "nl-comparisons",
    ),
]

NOUNS = nouns(
    """
# clothing
kleding | de | - | clothing | clothing
overhemd | het | overhemden | (dress) shirt | clothing
broek | de | broeken | trousers | clothing
rok | de | rokken | skirt | clothing
jurk | de | jurken | dress | clothing
jas | de | jassen | coat | clothing
trui | de | truien | jumper, sweater | clothing
schoen | de | schoenen | shoe | clothing
sok | de | sokken | sock | clothing
hoed | de | hoeden | hat | clothing
tas | de | tassen | bag | clothing
bril | de | brillen | glasses | clothing
paraplu | de | paraplu's | umbrella | clothing
# weather
weer | het | - | weather | weather
regen | de | - | rain | weather
sneeuw | de | - | snow | weather
wind | de | winden | wind | weather
wolk | de | wolken | cloud | weather
lucht | de | luchten | sky; air | weather
zomer | de | zomers | summer | weather
winter | de | winters | winter | weather
lente | de | lentes | spring | weather
herfst | de | herfsten | autumn | weather
seizoen | het | seizoenen | season | weather
# travel and transport
reis | de | reizen | trip, journey | travel
vakantie | de | vakanties | holiday | travel
kaartje | het | kaartjes | ticket | travel
koffer | de | koffers | suitcase | travel
paspoort | het | paspoorten | passport | travel
hotel | het | hotels | hotel | travel
strand | het | stranden | beach | travel
zee | de | zeeën | sea | travel
berg | de | bergen | mountain | travel
land | het | landen | country; land | travel
vliegtuig | het | vliegtuigen | aeroplane | transport
trein | de | treinen | train | transport
bus | de | bussen | bus | transport
tram | de | trams | tram | transport
boot | de | boten | boat | transport
vliegveld | het | vliegvelden | airport | transport
kaart | de | kaarten | map; card | travel
# work and study
kantoor | het | kantoren | office | work
bedrijf | het | bedrijven | company | work
collega | de | collega's | colleague | work
baas | de | bazen | boss | work
vergadering | de | vergaderingen | meeting | work
salaris | het | salarissen | salary | work
beroep | het | beroepen | profession | work
student | de | studenten | student | work
leraar | de | leraren | teacher | work
les | de | lessen | lesson | work
examen | het | examens | exam | work
computer | de | computers | computer | work
# health
gezondheid | de | - | health | health
dokter | de | dokters | doctor | health
huisarts | de | huisartsen | GP, family doctor | health
apotheek | de | apotheken | pharmacy | health
medicijn | het | medicijnen | medicine | health
verkoudheid | de | verkoudheden | cold (illness) | health
koorts | de | - | fever | health
pijn | de | pijnen | pain | health
afspraak | de | afspraken | appointment | health
# leisure
film | de | films | film | leisure
muziek | de | - | music | leisure
liedje | het | liedjes | song | leisure
sport | de | sporten | sport | leisure
wedstrijd | de | wedstrijden | match, game | leisure
spel | het | spellen | game | leisure
feest | het | feesten | party | leisure
verjaardag | de | verjaardagen | birthday | leisure
cadeau | het | cadeaus | present, gift | leisure
foto | de | foto's | photo | leisure
# shopping
prijs | de | prijzen | price; prize | shopping
euro | de | euro's | euro | shopping
bonnetje | het | bonnetjes | receipt | shopping
pinpas | de | pinpassen | debit card | shopping
kassa | de | kassa's | till, checkout | shopping
supermarkt | de | supermarkten | supermarket | shopping
boodschappen | de | boodschappen | groceries | shopping
# home and objects
vork | de | vorken | fork | home
mes | het | messen | knife | home
lepel | de | lepels | spoon | home
bord | het | borden | plate | home
glas | het | glazen | glass | home
fles | de | flessen | bottle | home
lamp | de | lampen | lamp | home
# nature and animals
bloem | de | bloemen | flower | nature
bos | het | bossen | forest, wood | nature
rivier | de | rivieren | river | nature
meer | het | meren | lake | nature
vogel | de | vogels | bird | animals
paard | het | paarden | horse | animals
koe | de | koeien | cow | animals
varken | het | varkens | pig | animals
muis | de | muizen | mouse | animals
"""
)
# Only ever used in the plural, so the article drill would have no right answer.
NOUNS = [n for n in NOUNS if n["id"] != "boodschappen"]

ADJECTIVES = adjectives(
    """
boos, boze | angry
bang, bange | afraid, scared
verdrietig, verdrietige | sad
vrolijk, vrolijke | cheerful
rustig, rustige | calm, quiet
druk, drukke | busy (a place, a person)
grappig, grappige | funny
serieus, serieuze | serious
verlegen, verlegen | shy (-en: no ending)
lui, luie | lazy
leuk, leuke | nice, fun
saai, saaie | boring
eng, enge | scary, creepy
ziek, zieke | ill, sick
gezond, gezonde | healthy
vrij, vrije | free
vol, volle | full
leeg, lege | empty
lang, lange | long; tall
kort, korte | short
zwaar, zware | heavy
licht, lichte | light
schoon, schone | clean
vies, vieze | dirty; disgusting
snel, snelle | fast
langzaam, langzame | slow
"""
)
for a in ADJECTIVES[:13]:
    a["tags"].append("feelings")

VERBS = [
    verb("opbellen", "bel", "to phone", ["scheidbare-werkwoorden"], prefix="op",
         example="Ik bel je morgen op.", example_en="I'll call you tomorrow."),
    verb("opstaan", "sta", "to get up", ["scheidbare-werkwoorden"], prefix="op", aux="zijn",
         present="sta staat staat staan staan staan", past="stond stonden", pp="opgestaan",
         example="Ik sta om zeven uur op.", example_en="I get up at seven."),
    verb("meenemen", "neem", "to take along", ["scheidbare-werkwoorden"], prefix="mee",
         past="nam namen", pp="meegenomen",
         example="Neem een paraplu mee.", example_en="Take an umbrella."),
    verb("uitgaan", "ga", "to go out", ["scheidbare-werkwoorden", "leisure"], prefix="uit", aux="zijn",
         present="ga gaat gaat gaan gaan gaan", past="ging gingen", pp="uitgegaan",
         example="We gaan vanavond uit.", example_en="We're going out tonight."),
    verb("aankomen", "kom", "to arrive", ["scheidbare-werkwoorden", "travel"], prefix="aan", aux="zijn",
         past="kwam kwamen", pp="aangekomen",
         example="De trein komt om vijf uur aan.", example_en="The train arrives at five."),
    verb("terugkomen", "kom", "to come back", ["scheidbare-werkwoorden"], prefix="terug", aux="zijn",
         past="kwam kwamen", pp="teruggekomen",
         example="Ik kom zo terug.", example_en="I'll be right back."),
    verb("weggaan", "ga", "to leave, to go away", ["scheidbare-werkwoorden"], prefix="weg", aux="zijn",
         present="ga gaat gaat gaan gaan gaan", past="ging gingen", pp="weggegaan",
         example="Ga je al weg?", example_en="Are you leaving already?"),
    verb("schoonmaken", "maak", "to clean", ["scheidbare-werkwoorden", "home"], prefix="schoon",
         example="Ik maak de keuken schoon.", example_en="I'm cleaning the kitchen."),
    verb("opruimen", "ruim", "to tidy up", ["scheidbare-werkwoorden", "home"], prefix="op",
         example="Ruim je kamer op!", example_en="Tidy your room!"),
    verb("afspreken", "spreek", "to arrange, to agree to meet", ["scheidbare-werkwoorden"], prefix="af",
         past="sprak spraken", pp="afgesproken",
         example="Zullen we morgen afspreken?", example_en="Shall we meet up tomorrow?"),
    verb("zich aankleden", "kleed", "to get dressed", ["scheidbare-werkwoorden", "wederkerende-werkwoorden", "clothing"],
         prefix="aan", refl=True,
         example="Ik kleed me snel aan.", example_en="I get dressed quickly."),
    verb("zich vergissen", "vergis", "to be mistaken", ["wederkerende-werkwoorden"], refl=True,
         example="Sorry, ik heb me vergist.", example_en="Sorry, I was mistaken."),
    verb("zich herinneren", "herinner", "to remember", ["wederkerende-werkwoorden"], refl=True,
         example="Herinner je je mij nog?", example_en="Do you still remember me?"),
    verb("zich voelen", "voel", "to feel", ["wederkerende-werkwoorden", "health"], refl=True,
         example="Ik voel me niet lekker.", example_en="I don't feel well."),
    verb("zich haasten", "haast", "to hurry", ["wederkerende-werkwoorden"], refl=True,
         example="Haast je, de trein vertrekt!", example_en="Hurry, the train's leaving!"),
    verb("zich vervelen", "verveel", "to be bored", ["wederkerende-werkwoorden", "feelings"], refl=True,
         example="De kinderen vervelen zich.", example_en="The children are bored."),
    verb("vallen", "val", "to fall", [], aux="zijn", past="viel vielen", pp="gevallen",
         example="Pas op, je valt!", example_en="Watch out, you'll fall!"),
    verb("worden", "word", "to become", [], aux="zijn", past="werd werden", pp="geworden",
         example="Ik word volgend jaar dertig.", example_en="I'll turn thirty next year."),
    verb("vertrekken", "vertrek", "to leave, to depart", ["travel"], aux="zijn",
         past="vertrok vertrokken", pp="vertrokken",
         example="De bus vertrekt om negen uur.", example_en="The bus leaves at nine."),
    verb("reizen", "reis", "to travel", ["travel"],
         example="Ik reis graag.", example_en="I like travelling."),
    verb("rijden", "rijd", "to drive; to ride", ["transport"], past="reed reden", pp="gereden",
         example="Kun jij rijden?", example_en="Can you drive?"),
    verb("vliegen", "vlieg", "to fly", ["travel"], past="vloog vlogen", pp="gevlogen",
         example="We vliegen naar Spanje.", example_en="We're flying to Spain."),
    verb("zwemmen", "zwem", "to swim", ["leisure"], past="zwom zwommen", pp="gezwommen",
         example="Ik zwem elke week.", example_en="I swim every week."),
    verb("dragen", "draag", "to wear; to carry", ["clothing"], past="droeg droegen", pp="gedragen",
         example="Hij draagt een bril.", example_en="He wears glasses."),
    verb("brengen", "breng", "to bring", [], past="bracht brachten", pp="gebracht",
         example="Ik breng je naar het station.", example_en="I'll take you to the station."),
    verb("krijgen", "krijg", "to get, to receive", [], past="kreeg kregen", pp="gekregen",
         example="Ik heb een cadeau gekregen.", example_en="I got a present."),
    verb("sturen", "stuur", "to send", [],
         example="Ik stuur je een berichtje.", example_en="I'll send you a message."),
    verb("vergeten", "vergeet", "to forget", [], aux="zijn", past="vergat vergaten", pp="vergeten",
         example="Ik ben mijn sleutels vergeten.", example_en="I've forgotten my keys."),
    verb("verliezen", "verlies", "to lose", [], past="verloor verloren", pp="verloren",
         example="We hebben de wedstrijd verloren.", example_en="We lost the match."),
    verb("antwoorden", "antwoord", "to answer", [],
         example="Hij antwoordt niet.", example_en="He isn't answering."),
    verb("horen", "hoor", "to hear", [],
         example="Hoor je dat?", example_en="Can you hear that?"),
    verb("openen", "open", "to open", [],
         example="De winkel opent om negen uur.", example_en="The shop opens at nine."),
    verb("sluiten", "sluit", "to close", [], past="sloot sloten", pp="gesloten",
         example="Sluit de deur, alsjeblieft.", example_en="Close the door, please."),
    verb("proberen", "probeer", "to try", [],
         example="Ik probeer het nog een keer.", example_en="I'll try again."),
    verb("gebruiken", "gebruik", "to use", [],
         example="Mag ik je telefoon gebruiken?", example_en="May I use your phone?"),
    verb("vertellen", "vertel", "to tell", [],
         example="Vertel eens, hoe was het?", example_en="So tell me, how was it?"),
    verb("verkopen", "verkoop", "to sell", ["shopping"], past="verkocht verkochten", pp="verkocht",
         example="Ze verkopen hun huis.", example_en="They're selling their house."),
    verb("lachen", "lach", "to laugh", ["feelings"], pp="gelachen",
         example="Waarom lach je?", example_en="Why are you laughing?"),
    verb("huilen", "huil", "to cry", ["feelings"],
         example="De baby huilt.", example_en="The baby is crying."),
]

PHRASES = phrases(
    """
het regent | it's raining
het is koud | it's cold
ik wil graag... | I'd like... | I want gladly
ik ben aan het... | I'm (in the middle of)... | I am at the
het hangt ervan af | it depends | it hangs of it
geen probleem | no problem
natuurlijk | of course | naturally
misschien | maybe
ik heb hoofdpijn | I have a headache | I have head-pain
laat maar | never mind, forget it | let but
tot zo | see you in a bit | until so
heb je zin om...? | do you feel like...? | have you mind to
graag! | yes please!, gladly!
jammer | what a pity
gelukkig | fortunately; happy
wat is er aan de hand? | what's the matter? | what is there at the hand?
zullen we gaan? | shall we go?
ik kan niet meer | I can't take any more; I'm full
zin hebben in | to feel like, to look forward to | to have mind in
nodig hebben | to need | to have necessary
aan de beurt zijn | to be someone's turn | to be at the turn
in de rij staan | to queue | to stand in the row
boodschappen doen | to do the grocery shopping | to do errands
op tijd | on time
te laat | too late; late
met pinnen | by card (paying) | with pinning
"""
    ,
    ["uitdrukkingen"],
)

CONNECTIVES = connectors(
    "connective",
    """
dus | so | conn-consequence | Het regent, dus blijven we thuis. | It's raining, so we're staying home. | Het regent, dus we blijven thuis.
daarom | that's why | conn-consequence | Ik was ziek, daarom ben ik niet gekomen. | I was ill; that's why I didn't come.
toch | still, all the same | conn-contrast | Het regende, maar we zijn toch gegaan. | It was raining, but we went all the same.
aan de andere kant | on the other hand | conn-contrast | Het huis is klein; aan de andere kant is het goedkoop. | The house is small; on the other hand, it's cheap.
verder | further, apart from that | conn-addition | Verder heb ik niets nodig. | Apart from that, I don't need anything.
ten slotte | finally, lastly | conn-sequence | Ten slotte wil ik iedereen bedanken. | Finally, I'd like to thank everyone.
eindelijk | at last | conn-sequence | Eindelijk is het weekend! | At last, it's the weekend!
""",
    ["verbindingswoorden"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
toen | when (one time in the past) | conj-subordinating | Toen ik thuiskwam, sliep hij al. | When I got home, he was already asleep.
terwijl | while | conj-subordinating | Hij kookt terwijl ik werk. | He cooks while I work.
voordat | before | conj-subordinating | Bel me voordat je komt. | Call me before you come.
nadat | after | conj-subordinating | Nadat we gegeten hadden, gingen we wandelen. | After we had eaten, we went for a walk. | Nadat we hadden gegeten, gingen we wandelen.
wanneer | when (whenever, or in future) | conj-subordinating | Wanneer het mooi weer is, fietsen we. | When the weather's nice, we cycle. | Wanneer het weer mooi is, fietsen we.
""",
    ["voegwoorden"],
)

ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# nl-separable-verbs and nl-reflexive-verbs are literal matches: the
# op-/uit-/aan-/terug-/weg-/schoon- verbs and the zich- verbs in the
# tegenwoordige-tijd pool are exactly what those pages teach. The four past-
# tense pages split what's left of that pool by hand, since they all share
# the same tag. nl-modal-particles uses the full verbindingswoorden set
# ("toch" is one of the particles the page names). "Gevoelens" pulls the
# character adjectives out of the general bijvoeglijke-naamwoorden pool the
# way Fondations split its colours.
UNITS = [
    {
        "title": "Het perfectum",
        "page_id": "nl-perfect",
        "word_ids": ["vallen", "worden", "vertrekken", "reizen", "rijden", "vliegen"],
    },
    {
        "title": "Hebben of zijn",
        "page_id": "nl-zijn-or-hebben",
        "word_ids": ["zwemmen", "dragen", "brengen", "krijgen", "sturen", "vergeten"],
    },
    {
        "title": "De onvoltooid verleden tijd",
        "page_id": "nl-imperfect",
        "word_ids": ["verliezen", "antwoorden", "horen", "openen", "sluiten", "proberen"],
    },
    {
        "title": "Scheidbare werkwoorden",
        "page_id": "nl-separable-verbs",
        "word_ids": [
            "opbellen", "opstaan", "meenemen", "uitgaan", "aankomen",
            "terugkomen", "weggaan", "schoonmaken", "opruimen", "afspreken",
        ],
    },
    {
        "title": "Kunnen, willen, moeten, mogen",
        "page_id": "nl-modal-verbs",
        "word_ids": ["gebruiken", "vertellen", "verkopen", "lachen", "huilen", "natuurlijk"],
    },
    {
        "title": "Wederkerende werkwoorden",
        "page_id": "nl-reflexive-verbs",
        "word_ids": ["zich-aankleden", "zich-vergissen", "zich-herinneren", "zich-voelen", "zich-haasten", "zich-vervelen"],
    },
    {
        "title": "Bijvoeglijke naamwoorden",
        "page_id": "nl-adjective-endings",
        "word_ids": ["leuk", "saai", "eng", "ziek", "gezond", "vrij"],
    },
    {
        "title": "Er",
        "page_id": "nl-er",
        "word_ids": ["misschien", "laat-maar", "tot-zo", "jammer", "gelukkig", "graag"],
    },
    {
        "title": "Modale partikels",
        "page_id": "nl-modal-particles",
        "word_ids": ["dus", "daarom", "toch", "aan-de-andere-kant", "verder", "ten-slotte", "eindelijk"],
    },
    {
        "title": "Groter, grootst",
        "page_id": "nl-comparisons",
        "word_ids": ["lang", "kort", "zwaar", "licht", "snel", "langzaam"],
    },
    {
        "title": "Gevoelens",
        "word_ids": ["boos", "bang", "verdrietig", "vrolijk", "rustig", "druk", "grappig", "serieus", "verlegen", "lui"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "home": "Huis",
    "transport": "Vervoer",
}

PACK = pack(
    "nl-everyday-v1",
    8,
    "nl",
    "Nederlands · Dagelijks (A2)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Oefening"),
)
