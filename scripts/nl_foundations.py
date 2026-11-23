"""nl-foundations-v1: A1. Pronunciation, the present tense and its spelling rules,
verb-second word order, negation, and the words for a first conversation."""

from common import build_units, interleave, page, pack, topic, topic_labels
from nl_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("uitspraak", "Uitspraak", "pronunciation", []),
    topic("voornaamwoorden", "Voornaamwoorden", "pronouns", ["tegenwoordige-tijd"]),
    topic("woordvolgorde", "Woordvolgorde", "word order", ["tegenwoordige-tijd"]),
    topic("vraagzinnen", "Vraagzinnen", "asking questions", ["woordvolgorde"]),
    topic("verkleinwoorden", "Verkleinwoorden", "diminutives", ["het"]),
    topic("getallen", "Getallen", "numbers and time", []),
    topic("family", "Familie", "family", ["lidwoorden"]),
    topic("body", "Lichaam", "body", ["lidwoorden"]),
    topic("city", "Stad", "city and places", ["lidwoorden"]),
    topic("greetings", "Begroetingen", "greetings and politeness", []),
    topic("colors", "Kleuren", "colours", ["bijvoeglijke-naamwoorden"]),
]

PAGES = [
    page(
        "nl-pronunciation",
        "Reading Dutch aloud",
        r"""
Dutch spelling is close to phonetic: once you know the sound of each letter group, you can read almost any word. A few sounds have no English equivalent.

## The sounds English doesn't have

| Spelling | Sound | Example |
| --- | --- | --- |
| g, ch | a rasp at the back of the throat, like Scottish *loch* | *[goed](lango:say)*, *[acht](lango:say)* |
| ui | between "ow" and "oy", lips rounded | *[huis](lango:say)*, *[uit](lango:say)* |
| eu | like French *peu*, "e" with rounded lips | *[leuk](lango:say)*, *[neus](lango:say)* |
| ij, ei | "ay" as in *day*, a bit wider | *[ijs](lango:say)*, *[klein](lango:say)* |
| u | like French *tu*: "ee" with rounded lips | *[u](lango:say)*, *[nu](lango:say)* |
| oe | "oo" as in *food* | *[boek](lango:say)*, *[goed](lango:say)* |
| ou, au | "ow" as in *how* | *[oud](lango:say)*, *[blauw](lango:say)* |
| sch | s + the g sound | *[school](lango:say)* ("s-gohl", never "skool") |

In the south of the Netherlands and in Flanders, the **g** is soft. In the north it's harsh. Both are correct.

## Long and short vowels

A double vowel is long: *[maan](lango:say)* (moon), *[boom](lango:say)* (tree). A single vowel is long when it ends a syllable (*[ma-ken](lango:say/maken)*) and short when a consonant closes it (*[man](lango:say)*, *[bed](lango:say)*). This one rule explains most Dutch spelling. The next pages use it.

## Endings

- **-en** at the end of a word is usually said as a short "uh": *[maken](lango:say)* sounds like "maakuh".
- **-d** at the end of a word is said as **t**: *[hond](lango:say)* sounds like "hont".
- **v** and **z** soften towards f and s at the start of a word in many accents.

## W

The Dutch **w** is softer than English w, somewhere between v and w, made with the lower lip against the top teeth.
""",
        ["uitspraak"],
        "nl-pronunciation",
        explains=["uitspraak"],
    ),
    page(
        "nl-pronouns",
        "Ik, jij, u and the short forms",
        r"""
Most Dutch pronouns have a **stressed** and an **unstressed** form. In writing and speech the unstressed one is normal; the stressed one adds emphasis or contrast.

| Person | Stressed | Unstressed | English |
| --- | --- | --- | --- |
| 1st singular | ik | ('k) | I |
| 2nd singular | jij | je | you (familiar) |
| 2nd polite | u | u | you (polite, one or more) |
| 3rd singular | hij / zij / het | (ie) / ze / 't | he / she / it |
| 1st plural | wij | we | we |
| 2nd plural | jullie | (je) | you (plural, familiar) |
| 3rd plural | zij | ze | they |

*Heb je tijd?* is the everyday way to ask. *Heb **jij** tijd?* means "do **you** have time?", as opposed to someone else.

## Jij or u?

The Netherlands is informal. **Jij** is normal with almost everyone your own age or younger, and in many workplaces. Use **u** with older people you don't know, officials, and customers in formal settings. Flanders uses **u** more, and often *gij* in speech.

*U* takes the jij form of the verb: *u bent*, *u hebt* (or *u heeft*).

## Men

*Men* is the formal "one": *Men zegt dat...* (People say that...). In speech, Dutch says *je* or *ze*: *Je weet nooit* (You never know), *Ze zeggen dat...* (They say that...).
""",
        ["voornaamwoorden"],
        "nl-pronouns",
        explains=["voornaamwoorden"],
    ),
    page(
        "nl-zijn-hebben",
        "Zijn and hebben",
        r"""
**Zijn** (to be) and **hebben** (to have) are irregular, very common, and the helper verbs of the perfect tense.

| | zijn | hebben |
| --- | --- | --- |
| ik | ben | heb |
| jij / je | bent | hebt |
| u | bent | hebt / heeft |
| hij / zij / het | is | heeft |
| wij / we | zijn | hebben |
| jullie | zijn | hebben |
| zij / ze | zijn | hebben |

## Where Dutch differs from English

| Dutch | Literally | English |
| --- | --- | --- |
| ik heb honger | I have hunger | I'm hungry |
| ik heb dorst | I have thirst | I'm thirsty |
| ik heb het koud / warm | I have it cold / warm | I'm cold / hot |
| ik heb gelijk | I have right | I'm right |
| ik heb zin in... | I have mind in | I feel like... |
| ik heb haast | I have haste | I'm in a hurry |
| ik ben twintig (jaar) | I am twenty (years) | I'm twenty |

Like English, and unlike French, Dutch uses *zijn* for age.

*Ik ben koud* means your body is cold to the touch, like a corpse. You want *ik heb het koud*.

:::cloze{sentence="Wij ___ haast, de trein vertrekt zo." blank="hebben"}
:::
""",
        ["tegenwoordige-tijd"],
        "nl-zijn-hebben",
    ),
    page(
        "nl-present-spelling",
        "The present tense and its spelling",
        r"""
The Dutch present tense has only three forms. The hard part is spelling the stem.

## The rule

1. Find the **stem**: the infinitive minus **-en**, spelled as it sounds.
2. **ik** gets the stem. **jij, u, hij, zij, het** get stem + **t**. All plurals get the infinitive.

| | werken | maken | zitten |
| --- | --- | --- | --- |
| ik | werk | maak | zit |
| jij | werkt | maakt | zit |
| hij | werkt | maakt | zit |
| wij, jullie, zij | werken | maken | zitten |

## Spelling the stem

The long-and-short vowel rule from the pronunciation page does all the work:

- *ma-ken* has a long **a** at the end of a syllable. Once *-en* is gone, the a is in a closed syllable and needs doubling to stay long: **maak**.
- *zit-ten* has a double consonant only to keep the i short. In *zit* the syllable is already closed: drop one t.
- A stem never ends in **v** or **z**: *leven → leef*, *reizen → reis*.
- If the stem already ends in **t**, don't add another: *zitten → hij zit*, *weten → hij weet*.

## Inversion drops the t

When *jij* or *je* comes **after** the verb, the -t disappears: *Jij werkt* but *Werk jij?*, *Wanneer kom je?* This only happens with jij/je, never with hij or u.

:::examples
- Ik werk elke dag. — I work every day.
- Hij maakt het ontbijt. — He's making breakfast.
- Werk je morgen? — Are you working tomorrow?
- We wonen in Utrecht. — We live in Utrecht.
:::

## One tense, three English ones

*Ik werk* is "I work", "I am working" and "I do work". To stress that something is happening right now, say *ik ben aan het werken*.

:::predict{prompt="jij (lopen)" answer="loopt"}
:::
""",
        ["tegenwoordige-tijd"],
        "nl-present-spelling",
        explains=["tegenwoordige-tijd"],
    ),
    page(
        "nl-word-order",
        "Verb second",
        r"""
The single most important rule of Dutch word order: in a main clause, **the finite verb is the second element**. Not the second word, the second *element*. Whatever comes first, the verb follows it.

| First | Verb | Rest |
| --- | --- | --- |
| Ik | ga | morgen naar Utrecht. |
| Morgen | ga | ik naar Utrecht. |
| Naar Utrecht | ga | ik morgen. |

If anything other than the subject starts the sentence, the subject moves after the verb. English speakers write *Morgen ik ga*, and it's wrong every time.

## The rest of the verb goes to the end

When there's a second verb (an infinitive, a participle, a separable prefix), it goes to the **end** of the clause:

:::examples
- Ik wil morgen naar Utrecht gaan. — I want to go to Utrecht tomorrow.
- Ik heb gisteren een boek gelezen. — I read a book yesterday.
- Ik bel je morgen op. — I'll call you tomorrow.
:::

The finite verb and the rest form a bracket around everything else. Dutch grammar calls it the *tangconstructie*, the pincer.

## Time, manner, place

In the middle, the usual order is **time, manner, place**: *Ik ga **morgen** **met de trein** **naar Utrecht***. English tends to put place first.

## Questions

Yes/no questions start with the verb: *Ga je morgen naar Utrecht?* Question words take the first slot: *Wanneer ga je naar Utrecht?*
""",
        ["woordvolgorde"],
        "nl-word-order",
        explains=["woordvolgorde"],
    ),
    page(
        "nl-negation",
        "Geen or niet?",
        r"""
Dutch has two words for "not", and choosing between them follows a clear rule.

## Geen

Use **geen** to negate a noun that would otherwise have **een** or no article. It means "no", "not a" or "not any".

:::examples
- Ik heb een auto. → Ik heb geen auto. — I don't have a car.
- Ik drink koffie. → Ik drink geen koffie. — I don't drink coffee.
- Hij heeft kinderen. → Hij heeft geen kinderen. — He doesn't have any children.
:::

## Niet

Use **niet** for everything else: verbs, adjectives, adverbs, and nouns with *de*, *het* or a possessive.

:::examples
- Ik werk niet. — I don't work.
- Het huis is niet groot. — The house isn't big.
- Ik zie de hond niet. — I don't see the dog.
:::

## Where niet goes

*Niet* goes **after** the object and time words, but **before** adjectives, prepositions and the verb parts at the end:

- *Ik zie hem vandaag **niet**.*
- *Het is **niet** mooi.*
- *Ik ga **niet** naar school.*
- *Ik heb het **niet** gedaan.*

## Other negatives

*nooit* (never), *niets* / *niks* (nothing), *niemand* (nobody), *nergens* (nowhere), *niet meer* (no longer), *nog niet* (not yet).
""",
        ["ontkenning"],
        "nl-negation",
        explains=["ontkenning"],
    ),
    page(
        "nl-questions",
        "Asking questions",
        r"""
A yes/no question puts the verb first. A question word takes the first slot, and the verb stays second.

:::examples
- Spreek je Engels? — Do you speak English?
- Waar woon je? — Where do you live?
- Hoe heet je? — What's your name?
:::

Remember that *jij* and *je* drop the verb's -t when they come after it: *Woon je hier?*, never *Woont je hier?*

## Question words

| Word | Meaning |
| --- | --- |
| wie | who |
| wat | what |
| waar | where |
| waarheen, waar ... naartoe | where to |
| wanneer | when |
| hoe | how |
| hoe laat | what time |
| waarom | why |
| hoeveel | how much, how many |
| welk / welke | which (welk for het-words, welke otherwise) |

## Tag questions

Dutch adds **hè** or **toch** at the end where English says "isn't it?" or "right?": *Mooi weer, hè?* *Je komt toch?*
""",
        ["vraagzinnen"],
        "nl-questions",
        explains=["vraagzinnen"],
    ),
    page(
        "nl-plurals",
        "Plurals: -en or -s",
        r"""
Every plural noun takes **de**, whatever its singular article. *Het huis*, *de huizen*.

## Which ending?

- Most nouns take **-en**: *boek → boeken*, *stoel → stoelen*.
- Nouns ending in unstressed **-el, -em, -en, -er, -je** take **-s**: *tafel → tafels*, *vader → vaders*, *meisje → meisjes*.
- Nouns ending in a vowel usually take **'s** or **s**: *auto → auto's*, *foto → foto's*, *zee → zeeën*.

This is a strong tendency, not a law. Learn the plural with the word; every noun in these packs carries it.

## Spelling changes

The long-and-short vowel rule applies again:

- A long vowel spelled double in a closed syllable becomes single when the syllable opens: *boom → bomen*, *maan → manen*.
- A short vowel needs its consonant doubled: *bed → bedden*, *kat → katten*.
- **f** and **s** often become **v** and **z**: *brief → brieven*, *huis → huizen*.

## Irregular plurals

| Singular | Plural |
| --- | --- |
| kind | kinderen |
| ei | eieren |
| stad | steden |
| schip | schepen |
| dag | dagen (short a becomes long) |

:::examples
- Ik heb twee katten en drie honden. — I have two cats and three dogs.
- De kinderen spelen buiten. — The children are playing outside.
- Waar zijn mijn foto's? — Where are my photos?
:::
""",
        ["meervoud"],
        "nl-plurals",
        explains=["meervoud"],
    ),
    page(
        "nl-diminutives",
        "Verkleinwoorden: -je, -tje, -pje",
        r"""
Dutch uses diminutives constantly, and not only for small things. A *biertje* is just a beer, and ordering one sounds friendlier than ordering *een bier*. Diminutives mark affection, informality, or that something is small.

**Every diminutive is a het-word**, whatever the original article: *de tafel → het tafeltje*. This is one of the few reliable de/het rules.

## Which ending?

| Ending | When | Example |
| --- | --- | --- |
| -je | most words | huis → huisje, boek → boekje |
| -tje | after a vowel, or -l, -n, -r, -w after a long vowel | stoel → stoeltje, auto → autootje |
| -pje | after -m after a long vowel | boom → boompje |
| -etje | after -l, -m, -n, -ng, -r after a short vowel | bal → balletje, ring → ringetje |
| -kje | after unstressed -ing | koning → koninkje |

Some words exist mostly as diminutives: *meisje* (girl), *koekje* (biscuit), *broodje* (bread roll), *kopje* (cup), *ijsje* (ice cream). The plural takes **-s**: *meisjes*, *broodjes*.

:::examples
- Zullen we een biertje drinken? — Shall we have a beer?
- Wil je een kopje koffie? — Would you like a cup of coffee?
- Ik neem een broodje kaas. — I'll have a cheese roll.
:::
""",
        ["verkleinwoorden", "het"],
        "nl-diminutives",
        explains=["verkleinwoorden"],
    ),
    page(
        "nl-numbers-time",
        "Numbers and telling the time",
        r"""
## Numbers read backwards

From 21, Dutch says the units first, like the English nursery rhyme *four-and-twenty blackbirds*.

| | |
| --- | --- |
| 1 een | 11 elf |
| 2 twee | 12 twaalf |
| 3 drie | 13 dertien |
| 4 vier | 14 veertien |
| 5 vijf | 15 vijftien |
| 6 zes | 16 zestien |
| 7 zeven | 17 zeventien |
| 8 acht | 18 achttien |
| 9 negen | 19 negentien |
| 10 tien | 20 twintig |

Tens: 30 dertig, 40 veertig, 50 vijftig, 60 zestig, 70 zeventig, 80 tachtig, 90 negentig, 100 honderd, 1000 duizend.

*21 eenentwintig* (one-and-twenty), *37 zevenendertig*, *99 negenennegentig*. When the unit ends in e, the *en* takes a trema: *tweeëntwintig*, *drieëntwintig*.

Numbers are written as one word up to a thousand: *zevenhonderdvijfenveertig*.

## Telling the time

The trap is **half**. *Half drie* is **half past two**: half *towards* three, not half past it.

| Time | Dutch | Literally |
| --- | --- | --- |
| 2:00 | twee uur | two hour |
| 2:15 | kwart over twee | quarter over two |
| 2:25 | vijf voor half drie | five before half three |
| 2:30 | half drie | half three |
| 2:35 | vijf over half drie | five past half three |
| 2:45 | kwart voor drie | quarter to three |

From 20 past to 20 to the hour, Dutch counts from the half hour. It takes practice, and every English speaker has turned up an hour late at least once.

*Hoe laat is het?* What time is it?
""",
        ["getallen"],
        "nl-numbers-time",
        explains=["getallen"],
    ),
    page(
        "nl-possessives",
        "Mijn, jouw, ons and onze",
        r"""
| Owner | Stressed | Unstressed | English |
| --- | --- | --- | --- |
| ik | mijn | (m'n) | my |
| jij | jouw | je | your |
| u | uw | uw | your (polite) |
| hij | zijn | (z'n) | his |
| zij | haar | (d'r) | her |
| wij | ons / onze | | our |
| jullie | jullie | je | your (plural) |
| zij | hun | | their |

Only **ons / onze** changes with the noun: **ons** before a singular het-word, **onze** everywhere else.

:::examples
- ons huis — our house (het huis)
- onze auto — our car (de auto)
- onze huizen — our houses (plural)
:::

## Hun or hen?

*Hun* is "their" before a noun: *hun kinderen*. As an object pronoun, grammar books separate *hun* (to them) and *hen* (them), but many native speakers mix them up. Using *ze* avoids the question entirely.

## Van

You can also show possession with **van**, like English *of*: *de auto van mijn vader* (my father's car). Dutch has an *'s* too, but mostly with names: *Annes fiets*, *Pieters huis*.
""",
        ["voornaamwoorden"],
        "nl-possessives",
    ),
]

NOUNS = nouns(
    """
# family and people
vader | de | vaders | father | family
moeder | de | moeders | mother | family
broer | de | broers | brother | family
zus | de | zussen | sister | family
zoon | de | zonen | son | family
dochter | de | dochters | daughter | family
man | de | mannen | man; husband | family
vrouw | de | vrouwen | woman; wife | family
ouder | de | ouders | parent | family
opa | de | opa's | grandpa | family
oma | de | oma's | grandma | family
oom | de | ooms | uncle | family
tante | de | tantes | aunt | family
neef | de | neven | nephew; male cousin | family
nicht | de | nichten | niece; female cousin | family
jongen | de | jongens | boy | people
meisje | het | meisjes | girl | people
baby | de | baby's | baby | people
buurman | de | buren | neighbour | people
naam | de | namen | name | people
mens | de | mensen | person, human being | people
# body
hoofd | het | hoofden | head | body
oog | het | ogen | eye | body
mond | de | monden | mouth | body
neus | de | neuzen | nose | body
oor | het | oren | ear | body
hand | de | handen | hand | body
arm | de | armen | arm | body
been | het | benen | leg | body
voet | de | voeten | foot | body
rug | de | ruggen | back | body
hart | het | harten | heart | body
buik | de | buiken | belly, stomach | body
haar | het | haren | hair | body
tand | de | tanden | tooth | body
# food
ontbijt | het | ontbijten | breakfast | food
lunch | de | lunches | lunch | food
avondeten | het | - | dinner | food
kaas | de | kazen | cheese | food
vlees | het | - | meat | food
vis | de | vissen | fish | food
kip | de | kippen | chicken | food
ei | het | eieren | egg | food
melk | de | - | milk | food
koffie | de | - | coffee | food
thee | de | - | tea | food
wijn | de | wijnen | wine | food
bier | het | bieren | beer | food
appel | de | appels | apple | food
aardappel | de | aardappelen | potato | food
groente | de | groenten | vegetable | food
fruit | het | - | fruit | food
suiker | de | - | sugar | food
zout | het | - | salt | food
rijst | de | - | rice | food
boter | de | - | butter | food
taart | de | taarten | cake, tart | food
koekje | het | koekjes | biscuit, cookie | food
broodje | het | broodjes | bread roll, sandwich | food
hagelslag | de | - | chocolate sprinkles (on bread) | food
stroopwafel | de | stroopwafels | syrup waffle | food
drop | de | - | liquorice | food
# home
slaapkamer | de | slaapkamers | bedroom | home
keuken | de | keukens | kitchen | home
badkamer | de | badkamers | bathroom | home
woonkamer | de | woonkamers | living room | home
bed | het | bedden | bed | home
sleutel | de | sleutels | key | home
appartement | het | appartementen | flat, apartment | home
tuin | de | tuinen | garden | home
bank | de | banken | sofa; bank | home
# time
dag | de | dagen | day | time
week | de | weken | week | time
maand | de | maanden | month | time
jaar | het | jaren | year | time
uur | het | uren | hour; o'clock | time
minuut | de | minuten | minute | time
ochtend | de | ochtenden | morning | time
middag | de | middagen | afternoon | time
avond | de | avonden | evening | time
maandag | de | maandagen | Monday | time
dinsdag | de | dinsdagen | Tuesday | time
woensdag | de | woensdagen | Wednesday | time
donderdag | de | donderdagen | Thursday | time
vrijdag | de | vrijdagen | Friday | time
zaterdag | de | zaterdagen | Saturday | time
zondag | de | zondagen | Sunday | time
# city
stad | de | steden | town, city | city
straat | de | straten | street | city
winkel | de | winkels | shop | city
markt | de | markten | market | city
bakker | de | bakkers | baker; bakery | city
station | het | stations | station | city
school | de | scholen | school | city
kerk | de | kerken | church | city
ziekenhuis | het | ziekenhuizen | hospital | city
restaurant | het | restaurants | restaurant | city
gracht | de | grachten | canal (in a city) | city
plein | het | pleinen | square | city
brug | de | bruggen | bridge | city
fiets | de | fietsen | bicycle | transport
werk | het | - | work, job | city
geld | het | - | money | objects
telefoon | de | telefoons | telephone | objects
"""
)

ADJECTIVES = adjectives(
    """
groot, grote | big, tall
klein, kleine | small, little
goed, goede | good
slecht, slechte | bad
mooi, mooie | beautiful, nice
lelijk, lelijke | ugly
jong, jonge | young
oud, oude | old
nieuw, nieuwe | new
aardig, aardige | kind, nice
blij, blije | happy, glad
lekker, lekkere | tasty; nice, pleasant
warm, warme | warm, hot
koud, koude | cold
makkelijk, makkelijke | easy
moeilijk, moeilijke | difficult
duur, dure | expensive
goedkoop, goedkope | cheap
rood, rode | red
blauw, blauwe | blue
groen, groene | green
geel, gele | yellow
zwart, zwarte | black
wit, witte | white
bruin, bruine | brown
oranje, oranje | orange (never takes -e)
"""
)
for a in ADJECTIVES[-8:]:
    a["tags"].append("colors")

VERBS = [
    verb("zijn", "ben", "to be", [], aux="zijn", present="ben bent is zijn zijn zijn",
         past="was waren", pp="geweest",
         example="Ik ben moe vandaag.", example_en="I'm tired today."),
    verb("hebben", "heb", "to have", [], present="heb hebt heeft hebben hebben hebben",
         past="had hadden", pp="gehad",
         example="Heb je tijd?", example_en="Do you have time?"),
    verb("doen", "doe", "to do", [], past="deed deden", pp="gedaan",
         example="Wat doe je?", example_en="What are you doing?"),
    verb("komen", "kom", "to come", [], aux="zijn", past="kwam kwamen", pp="gekomen",
         example="Kom je ook?", example_en="Are you coming too?"),
    verb("willen", "wil", "to want", [], present="wil wilt wil willen willen willen",
         past="wilde wilden", pp="gewild",
         example="Ik wil naar huis.", example_en="I want to go home."),
    verb("kunnen", "kan", "to be able to, can", [], present="kan kunt kan kunnen kunnen kunnen",
         past="kon konden", pp="gekund",
         example="Kun je me helpen?", example_en="Can you help me?"),
    verb("moeten", "moet", "to have to, must", [], past="moest moesten", pp="gemoeten",
         example="Ik moet werken.", example_en="I have to work."),
    verb("mogen", "mag", "to be allowed to, may", [], present="mag mag mag mogen mogen mogen",
         past="mocht mochten", pp="gemogen",
         example="Mag ik binnenkomen?", example_en="May I come in?"),
    verb("weten", "weet", "to know (a fact)", [], past="wist wisten", pp="geweten",
         example="Ik weet het niet.", example_en="I don't know."),
    verb("kennen", "ken", "to know (a person, a place)", [],
         example="Ken je mijn zus?", example_en="Do you know my sister?"),
    verb("zien", "zie", "to see", [], past="zag zagen", pp="gezien",
         example="Zie je dat?", example_en="Do you see that?"),
    verb("zeggen", "zeg", "to say", [], past="zei zeiden", pp="gezegd",
         example="Wat zeg je?", example_en="What are you saying?"),
    verb("maken", "maak", "to make", [],
         example="Ik maak een taart.", example_en="I'm making a cake."),
    verb("wonen", "woon", "to live (somewhere)", ["home"],
         example="Ik woon in Amsterdam.", example_en="I live in Amsterdam."),
    verb("werken", "werk", "to work", [],
         example="Ze werkt bij een bank.", example_en="She works at a bank."),
    verb("leren", "leer", "to learn; to teach", [],
         example="Ik leer Nederlands.", example_en="I'm learning Dutch."),
    verb("spelen", "speel", "to play", [],
         example="De kinderen spelen buiten.", example_en="The children are playing outside."),
    verb("kijken", "kijk", "to look, to watch", [], past="keek keken", pp="gekeken",
         example="We kijken een film.", example_en="We're watching a film."),
    verb("luisteren", "luister", "to listen", [],
         example="Ik luister naar muziek.", example_en="I'm listening to music."),
    verb("lezen", "lees", "to read", [], past="las lazen", pp="gelezen",
         example="Hij leest de krant.", example_en="He's reading the newspaper."),
    verb("schrijven", "schrijf", "to write", [], past="schreef schreven", pp="geschreven",
         example="Ik schrijf een brief.", example_en="I'm writing a letter."),
    verb("slapen", "slaap", "to sleep", [], past="sliep sliepen", pp="geslapen",
         example="De baby slaapt.", example_en="The baby is sleeping."),
    verb("lopen", "loop", "to walk", [], past="liep liepen", pp="gelopen",
         example="Ik loop naar huis.", example_en="I'm walking home."),
    verb("fietsen", "fiets", "to cycle", ["transport"],
         example="Ik fiets elke dag naar mijn werk.", example_en="I cycle to work every day."),
    verb("kopen", "koop", "to buy", [], past="kocht kochten", pp="gekocht",
         example="Ik koop brood bij de bakker.", example_en="I buy bread at the baker's."),
    verb("betalen", "betaal", "to pay", [],
         example="Kan ik met pin betalen?", example_en="Can I pay by card?"),
    verb("zoeken", "zoek", "to look for", [], past="zocht zochten", pp="gezocht",
         example="Ik zoek het station.", example_en="I'm looking for the station."),
    verb("vinden", "vind", "to find; to think (an opinion)", [], past="vond vonden", pp="gevonden",
         example="Ik vind het mooi.", example_en="I think it's nice."),
    verb("denken", "denk", "to think", [], past="dacht dachten", pp="gedacht",
         example="Ik denk van wel.", example_en="I think so."),
    verb("geven", "geef", "to give", [], past="gaf gaven", pp="gegeven",
         example="Geef me de sleutel.", example_en="Give me the key."),
    verb("nemen", "neem", "to take", [], past="nam namen", pp="genomen",
         example="Ik neem de trein.", example_en="I take the train."),
    verb("beginnen", "begin", "to begin", [], aux="zijn", past="begon begonnen", pp="begonnen",
         example="De film begint om acht uur.", example_en="The film starts at eight."),
    verb("blijven", "blijf", "to stay", [], aux="zijn", past="bleef bleven", pp="gebleven",
         example="Ik blijf thuis.", example_en="I'm staying home."),
    verb("staan", "sta", "to stand", [], present="sta staat staat staan staan staan", past="stond stonden", pp="gestaan",
         example="De fiets staat voor het huis.", example_en="The bike is (standing) in front of the house."),
    verb("zitten", "zit", "to sit", [], past="zat zaten", pp="gezeten",
         example="Ik zit in de trein.", example_en="I'm on the train."),
    verb("liggen", "lig", "to lie (be lying down)", [], past="lag lagen", pp="gelegen",
         example="Het boek ligt op tafel.", example_en="The book is (lying) on the table."),
    verb("heten", "heet", "to be called", ["people"], pp="geheten",
         example="Ik heet Sanne.", example_en="My name is Sanne."),
    verb("wachten", "wacht", "to wait", [],
         example="Ik wacht op de bus.", example_en="I'm waiting for the bus."),
    verb("koken", "kook", "to cook", ["food"],
         example="Wie kookt er vanavond?", example_en="Who's cooking tonight?"),
    verb("helpen", "help", "to help", [], past="hielp hielpen", pp="geholpen",
         example="Kan ik u helpen?", example_en="Can I help you?"),
    verb("vragen", "vraag", "to ask", [], past="vroeg vroegen", pp="gevraagd",
         example="Mag ik iets vragen?", example_en="Can I ask something?"),
    verb("begrijpen", "begrijp", "to understand", [], past="begreep begrepen", pp="begrepen",
         example="Ik begrijp het niet.", example_en="I don't understand."),
]

PHRASES = phrases(
    """
hallo | hello
hoi | hi (informal)
goedemorgen | good morning
goedemiddag | good afternoon
goedenavond | good evening
welterusten | good night (going to sleep) | rest well
dag | hello; goodbye | day
doei | bye (informal)
tot ziens | goodbye | until seeing
tot straks | see you later (today) | until soon
tot morgen | see you tomorrow
dank je wel | thank you (informal)
dank u wel | thank you (polite)
bedankt | thanks
alsjeblieft | please; here you are (informal) | if it pleases you
alstublieft | please; here you are (polite) | if it pleases you
graag gedaan | you're welcome | gladly done
sorry | sorry
pardon | excuse me; pardon?
ja | yes
nee | no
oké | OK
hoe gaat het? | how are you? | how goes it?
goed, dank je | fine, thanks
prettig kennis te maken | nice to meet you | pleasant to make acquaintance
ik begrijp het niet | I don't understand
kunt u dat herhalen? | could you repeat that?
spreekt u Engels? | do you speak English?
ik weet het niet | I don't know
hoeveel kost het? | how much does it cost?
mag ik de rekening? | may I have the bill?
waar is de wc? | where is the toilet?
er is, er zijn | there is, there are
wat is dat? | what's that?
hoe laat is het? | what time is it? | how late is it?
eet smakelijk | enjoy your meal | eat tastily
proost! | cheers!
fijne dag | have a nice day
fijn weekend | have a nice weekend
het maakt niet uit | it doesn't matter | it makes not out
geen idee | no idea
"""
    ,
    ["greetings"],
)

CONNECTIVES = connectors(
    "connective",
    """
eerst | first | conn-sequence | Eerst eten we, dan gaan we weg. | First we eat, then we leave.
dan | then | conn-sequence | Eerst eten we, dan gaan we weg. | First we eat, then we leave.
ook | also, too | conn-addition | Ik spreek Engels, en ik spreek ook Frans. | I speak English, and I also speak French.
""",
    ["verbindingswoorden"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
en | and | conj-coordinating | Ik heb een broer en twee zussen. | I have a brother and two sisters.
of | or; whether | conj-coordinating | Wil je thee of koffie? | Do you want tea or coffee?
als | if; when | conj-subordinating | Ik lees als het regent. | I read when it rains.
dat | that | conj-subordinating | Ik denk dat hij morgen komt. | I think that he's coming tomorrow.
""",
    ["voegwoorden"],
)

ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# None of the grammar pages (pronunciation, pronouns, word order, negation,
# questions, plurals, numbers) tag any vocabulary of their own, so each gets
# a hand-picked slice: greeting phrases for the ones about speaking and
# asking, "werken/maken/zitten" (its own page examples) plus kin for the
# present-tense spelling rule, family for possessives, het-words for
# diminutives. "Kleuren" pulls the colour adjectives out of the general
# bijvoeglijke-naamwoorden pool, same as fr-foundations's colour split.
UNITS = [
    {
        "title": "Uitspraak",
        "page_id": "nl-pronunciation",
        "word_ids": ["hallo", "goedemorgen", "dank-je-wel", "alsjeblieft", "sorry", "pardon"],
    },
    {
        "title": "Voornaamwoorden",
        "page_id": "nl-pronouns",
        "word_ids": ["hoi", "dag", "doei", "tot-ziens", "hoe-gaat-het", "spreekt-u-engels"],
    },
    {
        "title": "Zijn en hebben",
        "page_id": "nl-zijn-hebben",
        "word_ids": ["zijn", "hebben", "doen", "willen", "kunnen", "moeten"],
    },
    {
        "title": "De tegenwoordige tijd",
        "page_id": "nl-present-spelling",
        "word_ids": ["werken", "maken", "zitten", "wonen", "leren", "spelen", "kijken"],
    },
    {
        "title": "Werkwoord op de tweede plaats",
        "page_id": "nl-word-order",
        "word_ids": ["lopen", "fietsen", "kopen", "betalen", "zoeken", "vinden"],
    },
    {
        "title": "Geen of niet",
        "page_id": "nl-negation",
        "word_ids": ["denken", "geven", "nemen", "beginnen", "blijven", "staan"],
    },
    {
        "title": "Vraagzinnen",
        "page_id": "nl-questions",
        "word_ids": ["hoeveel-kost-het", "waar-is-de-wc", "wat-is-dat", "hoe-laat-is-het", "kunt-u-dat-herhalen", "ik-begrijp-het-niet"],
    },
    {
        "title": "Meervoud",
        "page_id": "nl-plurals",
        "word_ids": ["liggen", "heten", "wachten", "koken", "helpen", "vragen", "begrijpen"],
    },
    {
        "title": "Verkleinwoorden",
        "page_id": "nl-diminutives",
        "word_ids": ["hoofd", "oog", "oor", "hart", "bed", "appartement"],
    },
    {
        "title": "Getallen en tijd",
        "page_id": "nl-numbers-time",
        "word_ids": ["uur", "minuut", "maandag", "dinsdag", "woensdag", "ochtend"],
    },
    {
        "title": "Mijn, jouw, ons en onze",
        "page_id": "nl-possessives",
        "word_ids": ["vader", "moeder", "broer", "zus", "man", "vrouw"],
    },
    {
        "title": "Kleuren",
        "word_ids": ["rood", "blauw", "groen", "geel", "zwart", "wit", "bruin", "oranje"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "food": "Eten",
    "home": "Huis",
    "time": "Tijd",
    "people": "Mensen",
}

PACK = pack(
    "nl-foundations-v1",
    4,
    "nl",
    "Nederlands · Basis (A1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Oefening"),
)
