"""sv-foundations-v1: A1. Pronunciation, pronouns, the present tense, verb-second
word order, negation, questions, the definite form, en or ett, numbers and the
clock, and the words for a first conversation."""

from common import build_units, interleave, page, pack, topic, topic_labels
from sv_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("uttal", "Uttal", "pronunciation", []),
    topic("pronomen", "Pronomen", "pronouns", ["presens"]),
    topic("ordfoljd", "Ordföljd", "word order", ["presens"]),
    topic("fragor", "Frågor", "asking questions", ["ordfoljd"]),
    topic("tal", "Tal och klockan", "numbers and time", []),
    topic("family", "Familj", "family", ["artiklar"]),
    topic("body", "Kroppen", "body", ["artiklar"]),
    topic("city", "Staden", "city and places", ["artiklar"]),
    topic("greetings", "Hälsningar", "greetings and politeness", []),
    topic("colors", "Färger", "colours", ["adjektiv"]),
]

PAGES = [
    page(
        "sv-pronunciation",
        "Reading Swedish aloud",
        r"""
Swedish spelling is regular enough that you can read most words aloud once you know a handful of rules. The alphabet has three extra letters at the end, **å, ä, ö**, and they are separate letters, not a, a and o with marks on.

## The vowels

Swedish has nine vowel letters, and four of them have no English match.

| Spelling | Sound | Example |
| --- | --- | --- |
| å | "o" as in *more* | *[båt](lango:say)*, *[två](lango:say)* |
| ä | "e" as in *bed*; before r, like the *a* in *cat* | *[äta](lango:say)*, *[där](lango:say)* |
| ö | "e" said with rounded lips, like the *u* in *fur* | *[öga](lango:say)*, *[dörr](lango:say)* |
| y | "ee" said with tightly rounded lips | *[ny](lango:say)*, *[fyra](lango:say)* |
| u | long: "ee" pushed forward through pursed lips | *[hus](lango:say)*, *[ut](lango:say)* |
| o | mostly "oo" as in *food*, sometimes like å | *[sol](lango:say)*, *[son](lango:say)* |

The **o** is the unpredictable one: *sol* (sun) has the "oo" sound, *son* (son) and *komma* (come) the å sound. Listen to each new word once.

## Long and short

Every stressed syllable is long: either the vowel is long, or the consonant after it is. A double consonant makes the vowel before it short:

- *[tak](lango:say)* (roof) and *[tack](lango:say)* (thanks)
- *[vit](lango:say)* (white) and *[vitt](lango:say)* (white, for an ett-word)

## Soft k, g and sk

Before **e, i, y, ä, ö**, three common letters soften:

| Spelling | Sound | Example |
| --- | --- | --- |
| k | like *sh* in *sheep*, said further forward | *[kyrka](lango:say)*, *[kök](lango:say)* |
| g | "y" as in *yes* | *[göra](lango:say)*, *[gärna](lango:say)* |
| sk | the **sj-sound**, a breathy whoosh with no English match | *[skicka](lango:say)*, *[sked](lango:say)* |

Before **a, o, u, å** they stay hard: *[kaka](lango:say)*, *[gata](lango:say)*, *[skola](lango:say)*. A few words break the rule, such as *kille* (guy) and *kilo*, which keep a hard k.

The same two sounds have other spellings. The soft k is also **tj** and **kj**: *[tjugo](lango:say)*. The sj-sound is also **sj, stj, skj** and **-tion**: *[sju](lango:say)*, *[station](lango:say)*. The y sound is also **j, dj, hj, lj**, with the first letter silent: *[hjälpa](lango:say)*, *[ljus](lango:say)*.

## R and its neighbours

The r is a quick tap of the tongue. In most of Sweden, **r** melts into a following **d, l, n, s, t**, and the pair becomes one sound with the tongue tip curled back: *[bord](lango:say)*, *[barn](lango:say)*, *[först](lango:say)*. *Rs* sounds like English *sh*. In Skåne, in the far south, the r is made at the back of the throat and doesn't melt.

## Words said shorter than they're spelled

A few of the most common words have a spoken form of their own. Read them this way and you'll sound natural from day one:

| Written | Said |
| --- | --- |
| jag | ja |
| mig, dig, sig | mej, dej, sej |
| de, dem | dom |
| det | de |
| och | å |
| med | me |

## Word melody

Swedish words carry one of two melodies. *Anden* with a single falling tone is "the duck"; *anden* with two rises and falls is "the spirit". You'll be understood with either, so copy the melody of the recordings and don't worry about it yet.

## This unit's words

- *[hej](lango:say)*: just like English *hey*.
- *[hej då](lango:say)*: **å** is the *o* of *more*: "hey DOH".
- *[god morgon](lango:say)*: in this greeting the **d** of *god* is silent and so is the **g** of *morgon*: "goo MOR-ron".
- *[god natt](lango:say)*: the double **t** keeps the **a** short: "goo NATT".
- *[tack](lango:say)*: a short **a** before **ck**. Compare *[tak](lango:say)*, roof, with a long one.
- *[tack så mycket](lango:say)*: **y** is "ee" with tightly rounded lips, and the **t** of *mycket* is silent: "tack soh MÜK-keh".
- *[varsågod](lango:say)*: one word, the **rs** melts into a *sh*, and the stress falls on *god*: "vah-shoh-GOOD".
""",
        ["uttal"],
        "sv-pronunciation",
        explains=["uttal"],
    ),
    page(
        "sv-pronouns",
        "Jag, du, ni and de",
        r"""
Swedish pronouns have a subject form and an object form, as English *I* and *me* do.

| Person | Subject | Object | English |
| --- | --- | --- | --- |
| 1st singular | jag | mig | I, me |
| 2nd singular | du | dig | you |
| 3rd singular | han, hon | honom, henne | he, him; she, her |
| 3rd singular | den, det | den, det | it |
| 1st plural | vi | oss | we, us |
| 2nd plural | ni | er | you (more than one) |
| 3rd plural | de | dem | they, them |

## Du with everyone

Since the late 1960s Swedes have said **du** to almost everyone: strangers, doctors, teachers, the boss, the prime minister. Using **ni** to one person sounds either very old-fashioned or cold. Use *ni* when you speak to more than one person.

## Den or det?

There's no single word for *it*. Use **den** for an en-word and **det** for an ett-word:

- *Var är bilen? **Den** står på gatan.* (en bil)
- *Var är huset? **Det** ligger vid sjön.* (ett hus)

**Det** is also the empty *it* of *det regnar* (it's raining) and *det är kallt* (it's cold).

## De or dem?

*De* and *dem* are both said **dom**, so even Swedes mix them up in writing, and many write *dom* in texts and chat. Use **de** as the subject and **dem** as the object of a verb or after a preposition: *De bor här. Jag känner dem.*

## Man and hen

**Man** is the general *you* or *one*: *Man tar av sig skorna här* (You take your shoes off here). **Hen** is a gender-neutral *he or she*, used when the gender isn't known or doesn't matter, and by people who are neither.

:::examples
- Jag ser honom varje morgon. — I see him every morning.
- Var är nyckeln? Den ligger på bordet. — Where's the key? It's on the table.
- Känner ni dem? — Do you know them?
:::
""",
        ["pronomen"],
        "sv-pronouns",
        explains=["pronomen"],
    ),
    page(
        "sv-vara-ha",
        "Vara and ha",
        r"""
**Vara** (to be) and **ha** (to have) are the two verbs you'll use most. Like every Swedish verb, each has one form for all persons in a tense.

| | vara | ha |
| --- | --- | --- |
| present | är | har |
| past | var | hade |
| perfect | har varit | har haft |

*Jag är, du är, hon är, vi är, ni är, de är.* No *am, is, are* to choose between.

## Where Swedish differs from English

| Swedish | Literally | English |
| --- | --- | --- |
| jag fryser | I freeze | I'm cold |
| jag har rätt | I have right | I'm right |
| jag har bråttom | I have hurry | I'm in a hurry |
| jag har ont i magen | I have pain in the stomach | I have a stomach ache |
| hon är trettio år | she is thirty years | she's thirty |
| det finns | it is found | there is, there are |

*Jag är kall* means you are cold-hearted, or cold to the touch. When you feel cold, say **jag fryser**.

For *there is* Swedish uses **det finns**, not *det är*: *Det finns en bra restaurang här.*

## No article for jobs

With a job, a nationality or a religion, Swedish drops the *a*: *Hon är lärare* (She's a teacher), *Jag är engelsman*. *Hon är en lärare* sounds as if you're picking her out from a group.

:::examples
- Är du hemma i kväll? — Are you home tonight?
- Vi har en stor lägenhet i stan. — We have a big flat in town.
- Han var sjuk i går. — He was ill yesterday.
:::

:::cloze{sentence="Vi ___ två barn och en hund." blank="har"}
:::

:::cloze{sentence="Min syster ___ läkare i Umeå." blank="är"}
:::
""",
        ["presens"],
        "sv-vara-ha",
    ),
    page(
        "sv-present-tense",
        "The present tense",
        r"""
Swedish verbs don't change for the person. Where English says *I speak, she speaks*, Swedish says *jag talar, hon talar*, with the same form for everyone. Learn one form and you have the whole tense.

| | tala | köpa | bo |
| --- | --- | --- | --- |
| jag, du | talar | köper | bor |
| han, hon, den, det | talar | köper | bor |
| vi, ni, de | talar | köper | bor |

## Building the present

Almost every present form ends in **-r**. The modal verbs *kan, vill, ska, måste* and the verb *vet* don't. For the rest, the infinitive tells you how to get there:

| Group | Infinitive | Present | Rule |
| --- | --- | --- | --- |
| 1 | tala, arbeta | talar, arbetar | add -r |
| 2 | köpa, läsa | köper, läser | drop -a, add -er |
| 2 | höra, köra | hör, kör | stem ends in r: just drop -a |
| 3 | bo, tro | bor, tror | short verbs ending in another vowel: add -r |
| 4 | göra, vara | gör, är | irregular: learn them one by one |

Group 1 is the biggest, and new verbs join it: *googla, googlar*. You can't always tell group 1 from group 2 by looking at the infinitive, so every verb card shows the present.

## No *do*, no *-ing*

*Jag läser* is "I read", "I'm reading" and "I do read". Swedish has no *do* in questions or negatives either: *Läser du?* (Do you read? Are you reading?), *Jag läser inte* (I don't read).

## The infinitive

The infinitive usually ends in **-a**, and *to* is **att**: *Det är roligt att läsa.* After *vill, kan, måste, ska* there's no *att*: *Jag vill läsa*, never *Jag vill att läsa*.

## Present for the future

With a time word, the present also covers the future, as English *I'm leaving tomorrow* does: *Jag åker i morgon.*

:::examples
- Jag arbetar på ett kafé. — I work at a café.
- Han läser tidningen på bussen. — He reads the paper on the bus.
- Vi bor i Göteborg. — We live in Gothenburg.
- Vad gör du i kväll? — What are you doing tonight?
:::

:::predict{prompt="hon (prata)" answer="pratar"}
:::

:::predict{prompt="vi (köpa)" answer="köper"}
:::
""",
        ["presens"],
        "sv-present-tense",
        explains=["presens"],
    ),
    page(
        "sv-word-order",
        "Verb second",
        r"""
The most important rule of Swedish word order: in a main clause, **the verb is the second element**. Not the second word, the second *element*. Whatever comes first, the verb follows it.

| First | Verb | Rest |
| --- | --- | --- |
| Jag | åker | till Stockholm i morgon. |
| I morgon | åker | jag till Stockholm. |
| Till Stockholm | åker | jag i morgon. |

When anything other than the subject starts the sentence, the subject moves to just after the verb. English speakers write *I morgon jag åker*, and it's wrong every time.

Swedes start sentences with a time or place word all the time, so you'll need this rule from the first day: *Nu regnar det. I helgen ska vi bada. Här bor jag.*

## Inte and other short adverbs

**Inte** (not), **alltid** (always), **ofta** (often), **aldrig** (never) and **också** (also) go straight after the verb, or after the subject if the subject has moved behind the verb:

- *Hon kommer **alltid** sent.*
- *I dag kommer hon **inte**.*

## Two verbs stay together

Unlike Dutch and German, Swedish doesn't send a second verb to the end. It follows the first one, as in English:

- *Jag vill åka till Stockholm i morgon.*
- *Jag har läst boken.*

## How, where, when

At the end of the sentence, Swedish puts things in the same order as English: how, then where, then when. *Jag åker **med tåg** **till Stockholm** **i morgon**.*

:::examples
- I dag regnar det. — It's raining today.
- På lördag spelar vi fotboll. — On Saturday we're playing football.
- Nu förstår jag! — Now I understand!
:::

:::cloze{sentence="På söndag ___ vi till landet." blank="åker"}
:::
""",
        ["ordfoljd"],
        "sv-word-order",
        explains=["ordfoljd"],
    ),
    page(
        "sv-negation",
        "Inte, ingen and inget",
        r"""
## Inte

**Inte** is *not*. In a main clause it comes after the verb. With two verbs, it comes after the first:

:::examples
- Jag dricker inte kaffe. — I don't drink coffee.
- Hon är inte hemma. — She isn't home.
- Vi kan inte komma i kväll. — We can't come tonight.
- Jag har inte sett filmen. — I haven't seen the film.
:::

There's no *do* in a Swedish negative: *Jag förstår inte* (I don't understand), never *Jag gör inte förstå*.

## Ingen, inget, inga

For *no* or *not any* before a noun, Swedish has a word that agrees with the noun:

| | Positive | Negative |
| --- | --- | --- |
| en-word | en bil | ingen bil |
| ett-word | ett hus | inget hus |
| plural | barn | inga barn |

*Vi har ingen bil* (We don't have a car) is more natural than *Vi har inte en bil*. In speech you'll also hear **inte någon, inte något, inte några**: *Vi har inte någon bil.* Both are correct.

## In a subordinate clause

After words like *att, om, när* and *eftersom*, **inte** moves in front of the verb: *Jag tror att han **inte** kommer.* The conjunctions page explains why.

## Other negatives

| Swedish | English |
| --- | --- |
| aldrig | never |
| ingenting | nothing |
| ingen | nobody |
| ingenstans | nowhere |
| inte längre | no longer |
| inte än | not yet |

:::cloze{sentence="Hon har ___ syskon." blank="inga"}
:::
""",
        ["negation"],
        "sv-negation",
        explains=["negation"],
    ),
    page(
        "sv-questions",
        "Asking questions",
        r"""
A yes/no question starts with the verb. There's no *do*: *Talar du svenska?* is "Do you speak Swedish?"

A question with a question word puts that word first, then the verb, then the subject, keeping the verb in second place.

:::examples
- Är du trött? — Are you tired?
- Var bor du? — Where do you live?
- Varför är du så glad? — Why are you so happy?
:::

## Question words

| Word | Meaning |
| --- | --- |
| vem | who |
| vad | what |
| var | where |
| vart | where to |
| varifrån | where from |
| när | when |
| hur | how |
| hur mycket, hur många | how much, how many |
| varför | why |
| vilken, vilket, vilka | which (en-word, ett-word, plural) |

**Var** asks where something is, **vart** where it's going: *Var är du? Vart åker ni?* English uses *where* for both, so this one needs practice.

## Jo: yes to a negative question

When a question contains *inte*, answer **jo** to mean "yes, I do" or "yes, it is":

- *Kommer du inte? — **Jo**, jag kommer!* (Aren't you coming? Yes, I am!)

*Ja* would agree with the *inte*, and the asker can't be sure what you mean.

## Asking for agreement

Where English says *isn't it?* or *right?*, Swedish adds **eller hur?** or a short **va?**: *Det är fint väder, eller hur? Du kommer, va?*

:::cloze{sentence="___ ska du i sommar?" blank="Vart"}
:::
""",
        ["fragor"],
        "sv-questions",
        explains=["fragor"],
    ),
    page(
        "sv-definite-form",
        "The definite form",
        r"""
Swedish has no separate word for *the*. A noun takes an ending instead, and the ending depends on the gender and the last letter.

| | en-word | ett-word |
| --- | --- | --- |
| ends in a consonant | bil → bil**en** | hus → hus**et** |
| ends in a vowel | flicka → flicka**n** | äpple → äpple**t** |

A few spelling habits:

- Nouns ending in **-el, -en, -er** usually add just **-n** or lose an e: *nyckel → nyckeln*, *syster → systern*, *fönster → fönstret*.
- A short vowel before **m** doubles it: *rum → rummet*, *dröm → drömmen*.

## Plural with *the*

| Plural | Definite plural |
| --- | --- |
| bilar, flickor, parker | bilar**na**, flickor**na**, parker**na** |
| äpplen | äpplen**a** |
| hus, barn | hus**en**, barn**en** |

## The adjective adds a second *the*

With an adjective, Swedish says *the* twice: once with **den, det, de** in front, once with the ending.

| | en-word | ett-word | plural |
| --- | --- | --- | --- |
| a ... | en stor bil | ett stort hus | stora bilar |
| the ... | den stora bilen | det stora huset | de stora bilarna |

*Den stor bil* and *den stora bil* are both classic beginner mistakes. The A2 pack covers the adjective endings in full.

## Where Swedish uses *the* and English doesn't

Swedish takes the definite form for body parts and for things in general:

- *Jag har ont i huvudet.* (I have a headache. Literally: in the head.)
- *Hon tvättar håret.* (She's washing her hair.)
- *Livet är kort.* (Life is short.)

:::examples
- Bilen står på gatan. — The car is in the street.
- Äpplena ligger i köket. — The apples are in the kitchen.
- Barnen sover redan. — The children are already asleep.
:::

:::cloze{sentence="Kan du stänga ___? Det är kallt." blank="fönstret"}
:::
""",
        ["bestamd-form"],
        "sv-definite-form",
        explains=["bestamd-form"],
    ),
    page(
        "sv-en-ett",
        "En-word or ett-word?",
        r"""
Every noun is either an **en-word** or an **ett-word**, and there's no sure way to tell from its meaning. About three nouns in four are en-words, so *en* is the better guess, but learn each noun with its article: not *bil* but *en bil*.

The gender shows up all over the sentence:

| | en-word | ett-word |
| --- | --- | --- |
| a | en bil | ett hus |
| the | bilen | huset |
| big | en stor bil | ett stort hus |
| my | min bil | mitt hus |
| it | den | det |
| which? | vilken bil? | vilket hus? |

## Clues that help

- **People and animals** are mostly en-words: *en man, en kvinna, en katt*. The big exceptions are *ett barn* (a child) and *ett djur* (an animal).
- Nouns ending in **-a** are almost always en-words: *en gata, en flicka*. The exceptions are body parts: *ett öga* (an eye), *ett hjärta* (a heart).
- Endings that always mean en: **-are** (*en bagare*), **-het** (*en nyhet*), **-ing** (*en tidning*), **-tion** (*en station*).
- Endings that mean ett: **-eri** (*ett bageri*), **-um** (*ett museum*).
- A compound takes the gender of its last part: *ett sjukhus* (hospital) is an ett-word because *hus* is.

:::examples
- Jag har ett stort rum. — I have a big room.
- Var är min nyckel? — Where's my key?
- Mitt kök är litet. — My kitchen is small.
:::

:::sort{groups="en: kyrka, lärare, potatis, ost | ett: öra, kök, bibliotek, vin"}
:::
""",
        ["en", "ett"],
        "sv-en-ett",
        explains=["en", "ett"],
    ),
    page(
        "sv-numbers-time",
        "Numbers and telling the time",
        r"""
## Numbers

| | |
| --- | --- |
| 0 noll | 11 elva |
| 1 en, ett | 12 tolv |
| 2 två | 13 tretton |
| 3 tre | 14 fjorton |
| 4 fyra | 15 femton |
| 5 fem | 16 sexton |
| 6 sex | 17 sjutton |
| 7 sju | 18 arton |
| 8 åtta | 19 nitton |
| 9 nio | 20 tjugo |
| 10 tio | 21 tjugoett |

Tens: 30 trettio, 40 fyrtio, 50 femtio, 60 sextio, 70 sjuttio, 80 åttio, 90 nittio, 100 hundra, 1000 tusen.

The order is the same as in English, and a number is written as one word: *trettiosju* (37), *tvåhundrafemtio* (250). In speech the tens get shorter: *tjugo* is said "tjugi" or "tjugå", *fyrtio* "förti".

*One* agrees with the noun: *en bil, ett hus*. When you count, it's *ett*: *ett, två, tre*.

## Telling the time

*Vad är klockan?* asks the time. The answer starts with *Den är...* or *Klockan är...*.

| Time | Swedish | Literally |
| --- | --- | --- |
| 2:00 | klockan två | the clock two |
| 2:15 | kvart över två | quarter over two |
| 2:20 | tjugo över två | twenty over two |
| 2:25 | fem i halv tre | five to half three |
| 2:30 | halv tre | half three |
| 2:35 | fem över halv tre | five over half three |
| 2:45 | kvart i tre | quarter to three |

The trap is **halv**. *Halv tre* is **half past two**: half of the way *to* three. Every English speaker in Sweden has turned up an hour late at least once.

Timetables and offices use the 24-hour clock: *klockan femton* (15.00).

## Days

Days are written with a small letter: *måndag, tisdag, onsdag, torsdag, fredag, lördag, söndag*. *På måndag* is "on Monday" (this coming one), *på måndagar* is "on Mondays".

:::examples
- Jag är tjugofem år. — I'm twenty-five.
- Bussen går kvart i åtta. — The bus leaves at a quarter to eight.
- Vi ses på fredag klockan sju. — See you on Friday at seven.
:::

:::cloze{sentence="Filmen börjar ___ nio, alltså 20.30." blank="halv"}
:::
""",
        ["tal"],
        "sv-numbers-time",
        explains=["tal"],
    ),
    page(
        "sv-possessives",
        "Min, mitt and mina",
        r"""
*My, your, our* agree with the thing owned, not with the owner:

| Owner | en-word | ett-word | plural | English |
| --- | --- | --- | --- | --- |
| jag | min | mitt | mina | my |
| du | din | ditt | dina | your |
| han | hans | hans | hans | his |
| hon | hennes | hennes | hennes | her |
| vi | vår | vårt | våra | our |
| ni | er | ert | era | your (more than one) |
| de | deras | deras | deras | their |

*Min bil, mitt hus, mina barn.* **Hans, hennes** and **deras** never change.

After a possessive the noun has no ending: *min bil*, never *min bilen*.

## Sin, sitt, sina

Swedish has a possessive that English lacks. When *his, her, its* or *their* points back to the subject of the same clause, use **sin, sitt, sina**:

- *Erik ringer **sin** mamma.* (Erik calls his own mother.)
- *Erik ringer **hans** mamma.* (Erik calls another man's mother.)

Get this wrong and you change who you're talking about. *Sin* never goes in the subject itself: *Hans mamma ringer*, not *Sin mamma ringer*.

## Names

Add **-s** with no apostrophe: *Annas bok, Sveriges huvudstad.*

:::examples
- Var är dina nycklar? — Where are your keys?
- Vårt hus är gammalt. — Our house is old.
- Lisa bor hos sina föräldrar. — Lisa lives with her parents.
:::

:::cloze{sentence="Peter lagar mat med ___ dotter i köket." blank="sin"}
:::

:::cloze{sentence="Du har ett eget rum nu. Är det här ___ rum?" blank="ditt"}
:::
""",
        ["pronomen"],
        "sv-possessives",
    ),
]

NOUNS = nouns(
    """
# family and people
pappa | en | pappan | pappor | dad, father | family | Min pappa jobbar på ett sjukhus. | My dad works at a hospital.
mamma | en | mamman | mammor | mum, mother | family | Mamma lagar mat i köket. | Mum is cooking in the kitchen.
bror | en | brodern | bröder | brother | family | Min bror bor i Malmö. | My brother lives in Malmö.
syster | en | systern | systrar | sister | family | Har du en syster? | Do you have a sister?
son | en | sonen | söner | son | family | Deras son går i skolan. | Their son is at school.
dotter | en | dottern | döttrar | daughter | family | Min dotter är sju år. | My daughter is seven.
man | en | mannen | män | man; husband | family | Hennes man heter Johan. | Her husband is called Johan.
fru | en | frun | fruar | wife | family | Han ringer sin fru varje kväll. | He calls his wife every evening.
förälder | en | föräldern | föräldrar | parent | family | Mina föräldrar bor på landet. | My parents live in the country.
mormor | en | mormodern | mormödrar | grandmother (mother's mother) | family | Mormor bakar de bästa bullarna. | Grandma bakes the best buns.
morfar | en | morfadern | morfäder | grandfather (mother's father) | family | Morfar fyller åttio i år. | Grandpa turns eighty this year.
kusin | en | kusinen | kusiner | cousin | family | Min kusin kommer på besök i morgon. | My cousin is coming to visit tomorrow.
moster | en | mostern | mostrar | aunt (mother's sister) | family | Min moster bor i Kiruna. | My aunt lives in Kiruna.
familj | en | familjen | familjer | family | family | Hela familjen äter middag tillsammans. | The whole family eats dinner together.
syskon | ett | syskonet | syskon | brother or sister, sibling | family | Hur många syskon har du? | How many brothers and sisters do you have?
pojke | en | pojken | pojkar | boy | people | Pojken spelar fotboll i parken. | The boy is playing football in the park.
flicka | en | flickan | flickor | girl | people | Flickan läser en bok. | The girl is reading a book.
granne | en | grannen | grannar | neighbour | people | Vår granne har en stor hund. | Our neighbour has a big dog.
namn | ett | namnet | namn | name | people | Jag glömmer alltid hennes namn. | I always forget her name.
människa | en | människan | människor | person, human being | people | Det är många människor i parken i dag. | There are a lot of people in the park today.
kvinna | en | kvinnan | kvinnor | woman | people | Kvinnan i kassan är mycket snäll. | The woman at the till is very kind.
# body
huvud | ett | huvudet | huvuden | head | body | Jag har ont i huvudet. | I have a headache.
öga | ett | ögat | ögon | eye | body | Hon har blå ögon. | She has blue eyes.
öra | ett | örat | öron | ear | body | Hunden har stora öron. | The dog has big ears.
näsa | en | näsan | näsor | nose | body | Min näsa är röd av kylan. | My nose is red from the cold.
mun | en | munnen | munnar | mouth | body | Prata inte med mat i munnen! | Don't talk with your mouth full!
hand | en | handen | händer | hand | body | Tvätta händerna före maten. | Wash your hands before you eat.
arm | en | armen | armar | arm | body | Min arm gör ont. | My arm hurts.
ben | ett | benet | ben | leg; bone | body | Mina ben är trötta efter promenaden. | My legs are tired after the walk.
fot | en | foten | fötter | foot | body | Mina fötter är kalla. | My feet are cold.
hjärta | ett | hjärtat | hjärtan | heart | body | Hjärtat slår snabbt när jag springer. | My heart beats fast when I run.
mage | en | magen | magar | stomach, tummy | body | Barnet har ont i magen. | The child has a stomach ache.
hår | ett | håret | hår | hair | body | Hon har långt, mörkt hår. | She has long dark hair.
tand | en | tanden | tänder | tooth | body | Glöm inte att borsta tänderna! | Don't forget to brush your teeth!
# food
frukost | en | frukosten | frukostar | breakfast | food | Jag äter frukost klockan sju. | I have breakfast at seven.
lunch | en | lunchen | luncher | lunch | food | Vi äter lunch tillsammans i dag. | We're having lunch together today.
middag | en | middagen | middagar | dinner | food | Vad blir det till middag? | What's for dinner?
mat | en | maten | - | food; a meal | food | Maten är klar! | Dinner's ready!
ost | en | osten | ostar | cheese | food | Ost på knäckebröd är gott. | Cheese on crispbread is tasty.
kött | ett | köttet | - | meat | food | Hon äter inte kött. | She doesn't eat meat.
fisk | en | fisken | fiskar | fish | food | Vi äter fisk på fredagar. | We eat fish on Fridays.
ägg | ett | ägget | ägg | egg | food | Jag kokar två ägg till frukost. | I'm boiling two eggs for breakfast.
mjölk | en | mjölken | - | milk | food | Mjölken står i kylskåpet. | The milk is in the fridge.
kaffe | ett | kaffet | - | coffee | food | Vill du ha en kopp kaffe? | Would you like a cup of coffee?
te | ett | teet | - | tea | food | Jag dricker te med mjölk. | I drink tea with milk.
vin | ett | vinet | viner | wine | food | Ett glas rött vin, tack. | A glass of red wine, please.
äpple | ett | äpplet | äpplen | apple | food | Hon tar med ett äpple till skolan. | She takes an apple to school.
potatis | en | potatisen | potatisar | potato | food | Vi äter potatis nästan varje dag. | We eat potatoes almost every day.
grönsak | en | grönsaken | grönsaker | vegetable | food | Barnen äter inte gärna grönsaker. | The children aren't keen on vegetables.
frukt | en | frukten | frukter | fruit | food | Jag köper frukt på torget. | I buy fruit at the market.
socker | ett | sockret | - | sugar | food | Tar du socker i kaffet? | Do you take sugar in your coffee?
salt | ett | saltet | - | salt | food | Kan du skicka saltet? | Can you pass the salt?
ris | ett | riset | - | rice | food | Riset är klart om tio minuter. | The rice is ready in ten minutes.
smör | ett | smöret | - | butter | food | Det finns inget smör kvar. | There's no butter left.
tårta | en | tårtan | tårtor | cake, gateau | food | Vi äter tårta på min födelsedag. | We eat cake on my birthday.
kanelbulle | en | kanelbullen | kanelbullar | cinnamon bun | food | En kanelbulle och en kaffe, tack. | A cinnamon bun and a coffee, please.
smörgås | en | smörgåsen | smörgåsar | sandwich (open) | food | Jag gör en smörgås med ost. | I'm making a cheese sandwich.
knäckebröd | ett | knäckebrödet | knäckebröd | crispbread | food | Svenskar äter mycket knäckebröd. | Swedes eat a lot of crispbread.
# home
rum | ett | rummet | rum | room | home | Lägenheten har tre rum och kök. | The flat has three rooms and a kitchen.
sovrum | ett | sovrummet | sovrum | bedroom | home | Sovrummet ligger på övervåningen. | The bedroom is upstairs.
kök | ett | köket | kök | kitchen | home | Vi äter frukost i köket. | We have breakfast in the kitchen.
badrum | ett | badrummet | badrum | bathroom | home | Badrummet är ledigt nu. | The bathroom is free now.
vardagsrum | ett | vardagsrummet | vardagsrum | living room | home | Vi tittar på tv i vardagsrummet. | We watch TV in the living room.
säng | en | sängen | sängar | bed | home | Katten sover i min säng. | The cat sleeps in my bed.
nyckel | en | nyckeln | nycklar | key | home | Var är nyckeln till cykeln? | Where's the key to the bike?
lägenhet | en | lägenheten | lägenheter | flat, apartment | home | De bor i en liten lägenhet. | They live in a small flat.
trädgård | en | trädgården | trädgårdar | garden | home | Barnen leker i trädgården. | The children are playing in the garden.
soffa | en | soffan | soffor | sofa | home | Han sover på soffan i natt. | He's sleeping on the sofa tonight.
# time
dag | en | dagen | dagar | day | time | Vilken dag är det i dag? | What day is it today?
vecka | en | veckan | veckor | week | time | Vi ses nästa vecka. | See you next week.
månad | en | månaden | månader | month | time | Hyran är åttatusen kronor i månaden. | The rent is eight thousand kronor a month.
år | ett | året | år | year | time | Jag har bott här i två år. | I've lived here for two years.
timme | en | timmen | timmar | hour | time | Resan tar en timme. | The journey takes an hour.
minut | en | minuten | minuter | minute | time | Bussen kommer om fem minuter. | The bus comes in five minutes.
morgon | en | morgonen | morgnar | morning | time | På morgonen är det kallt ute. | It's cold outside in the morning.
eftermiddag | en | eftermiddagen | eftermiddagar | afternoon | time | Vi fikar varje eftermiddag. | We have a coffee break every afternoon.
kväll | en | kvällen | kvällar | evening | time | Vad gör du på kvällarna? | What do you do in the evenings?
måndag | en | måndagen | måndagar | Monday | time | Affären är stängd på måndagar. | The shop is closed on Mondays.
tisdag | en | tisdagen | tisdagar | Tuesday | time | Jag spelar tennis på tisdag. | I'm playing tennis on Tuesday.
onsdag | en | onsdagen | onsdagar | Wednesday | time | Vi har svenska på onsdagar. | We have Swedish on Wednesdays.
torsdag | en | torsdagen | torsdagar | Thursday | time | På torsdagar äter många ärtsoppa. | On Thursdays a lot of people eat pea soup.
fredag | en | fredagen | fredagar | Friday | time | På fredag kväll ser vi en film. | On Friday evening we're watching a film.
lördag | en | lördagen | lördagar | Saturday | time | Barnen får godis på lördagar. | The children get sweets on Saturdays.
söndag | en | söndagen | söndagar | Sunday | time | På söndag sover jag länge. | On Sunday I'm having a lie-in.
# city
stad | en | staden | städer | town, city | city | Göteborg är en stor stad. | Gothenburg is a big city.
gata | en | gatan | gator | street | city | Vi bor på en lugn gata. | We live on a quiet street.
affär | en | affären | affärer | shop | city | Affären stänger klockan åtta. | The shop closes at eight.
torg | ett | torget | torg | square, market square | city | Vi träffas på torget klockan tre. | We'll meet in the square at three.
bageri | ett | bageriet | bagerier | bakery | city | Bageriet säljer goda kanelbullar. | The bakery sells good cinnamon buns.
station | en | stationen | stationer | station | city | Hur kommer jag till stationen? | How do I get to the station?
skola | en | skolan | skolor | school | city | Skolan ligger nära vårt hus. | The school is near our house.
kyrka | en | kyrkan | kyrkor | church | city | Kyrkan är från 1200-talet. | The church is from the 13th century.
sjukhus | ett | sjukhuset | sjukhus | hospital | city | Sjukhuset ligger i centrum. | The hospital is in the centre.
restaurang | en | restaurangen | restauranger | restaurant | city | Vi äter på en restaurang i kväll. | We're eating at a restaurant tonight.
bro | en | bron | broar | bridge | city | Vi cyklar över bron. | We cycle over the bridge.
jobb | ett | jobbet | jobb | job, work | city | Hon har ett nytt jobb. | She has a new job.
cykel | en | cykeln | cyklar | bicycle, bike | transport | Min cykel står utanför. | My bike is outside.
telefon | en | telefonen | telefoner | telephone, phone | objects | Din telefon ringer i väskan. | Your phone is ringing in your bag.
"""
)

ADJECTIVES = adjectives(
    """
stor, stort, stora | big, large | Vi har en stor trädgård. | We have a big garden.
liten, litet, små | small, little | Vårt kök är litet men fint. | Our kitchen is small but nice.
bra, bra, bra | good, fine (never changes) | Det är en bra idé. | That's a good idea.
dålig, dåligt, dåliga | bad; poorly | Vädret är dåligt i dag. | The weather's bad today.
fin, fint, fina | nice, fine, pretty | Vilken fin klänning! | What a nice dress!
vacker, vackert, vackra | beautiful | Stockholm är en vacker stad. | Stockholm is a beautiful city.
ung, ungt, unga | young | Han är ung men mycket duktig. | He's young but very good at it.
gammal, gammalt, gamla | old | Huset är över hundra år gammalt. | The house is over a hundred years old.
ny, nytt, nya | new | Jag har köpt en ny cykel. | I've bought a new bike.
snäll, snällt, snälla | kind, nice | Din mormor är så snäll. | Your grandma is so kind.
glad, glatt, glada | happy, glad | Barnen är glada i dag. | The children are happy today.
god, gott, goda | good, tasty | Kakan är mycket god. | The cake is very good.
varm, varmt, varma | warm, hot | Är kaffet för varmt? | Is the coffee too hot?
kall, kallt, kalla | cold | Vattnet är kallt i juni. | The water's cold in June.
lätt, lätt, lätta | easy; light | Den här övningen är lätt. | This exercise is easy.
svår, svårt, svåra | difficult, hard | Uttalet är svårt i början. | The pronunciation is hard at first.
dyr, dyrt, dyra | expensive | Allt är så dyrt här. | Everything is so expensive here.
billig, billigt, billiga | cheap | Lunchen är billig på måndagar. | Lunch is cheap on Mondays.
trött, trött, trötta | tired | Jag är så trött i dag. | I'm so tired today.
hungrig, hungrigt, hungriga | hungry | Är du hungrig? Maten är klar. | Are you hungry? The food is ready.
ledsen, ledset, ledsna | sad; sorry | Jag är ledsen, men jag kan inte. | I'm sorry, but I can't.
röd, rött, röda | red | Sverige har många röda hus. | Sweden has lots of red houses.
blå, blått, blå | blue | Himlen är blå i dag. | The sky is blue today.
grön, grönt, gröna | green | Gräset är grönt efter regnet. | The grass is green after the rain.
gul, gult, gula | yellow | Hon har en gul jacka. | She has a yellow jacket.
svart, svart, svarta | black | Jag dricker kaffet svart. | I drink my coffee black.
vit, vitt, vita | white | Han har en vit skjorta på sig. | He's wearing a white shirt.
brun, brunt, bruna | brown | Hunden har bruna ögon. | The dog has brown eyes.
rosa, rosa, rosa | pink (never changes) | Hon har ett rosa paraply. | She has a pink umbrella.
"""
)
for a in ADJECTIVES[-8:]:
    a["tags"].append("colors")

VERBS = [
    verb("vara", "to be", [], group="4", pres="är", pret="var", sup="varit",
         example="Är du hemma i kväll?", example_en="Are you home tonight?"),
    verb("ha", "to have", [], group="4", pres="har", pret="hade", sup="haft",
         example="Har du tid i morgon?", example_en="Do you have time tomorrow?"),
    verb("göra", "to do, to make", [], group="4", pres="gör", pret="gjorde", sup="gjort",
         example="Vad gör du i helgen?", example_en="What are you doing at the weekend?"),
    verb("komma", "to come", [], group="4", pres="kommer", pret="kom", sup="kommit",
         example="Kommer du på festen?", example_en="Are you coming to the party?"),
    verb("vilja", "to want", [], group="4", pres="vill", pret="ville", sup="velat", fut="kommer att",
         example="Jag vill åka hem nu.", example_en="I want to go home now."),
    verb("kunna", "can, to be able to", [], group="4", pres="kan", pret="kunde", sup="kunnat",
         fut="kommer att",
         example="Kan du hjälpa mig?", example_en="Can you help me?"),
    verb("måste", "must, to have to", [], group="4", pres="måste", pret="måste", sup="måst",
         future="kommer att behöva",
         example="Jag måste jobba i morgon.", example_en="I have to work tomorrow."),
    verb("få", "to get; may, to be allowed to", [], group="4", pres="får", pret="fick", sup="fått",
         example="Får jag sitta här?", example_en="May I sit here?"),
    verb("veta", "to know (a fact)", [], group="4", pres="vet", pret="visste", sup="vetat",
         fut="kommer att",
         example="Vet du var stationen ligger?", example_en="Do you know where the station is?"),
    verb("känna", "to know (a person); to feel", [], group="2a", fut="kommer att",
         example="Känner du min bror?", example_en="Do you know my brother?"),
    verb("se", "to see", [], group="4", pres="ser", pret="såg", sup="sett",
         example="Ser du huset där borta?", example_en="Can you see the house over there?"),
    verb("säga", "to say", [], group="4", pres="säger", pret="sa", sup="sagt",
         example="Vad sa du?", example_en="What did you say?"),
    verb("heta", "to be called", [], group="4", pres="heter", pret="hette", sup="hetat",
         fut="kommer att",
         example="Vad heter din hund?", example_en="What's your dog called?"),
    verb("bo", "to live (somewhere)", ["home"], group="3",
         example="Jag bor i Stockholm.", example_en="I live in Stockholm."),
    verb("arbeta", "to work", [], group="1",
         example="Hon arbetar på en bank.", example_en="She works at a bank."),
    verb("spela", "to play", [], group="1",
         example="Barnen spelar fotboll.", example_en="The children are playing football."),
    verb("titta", "to look, to watch", [], group="1",
         example="Vi tittar på en film i kväll.", example_en="We're watching a film tonight."),
    verb("lyssna", "to listen", [], group="1",
         example="Jag lyssnar på musik på bussen.", example_en="I listen to music on the bus."),
    verb("läsa", "to read; to study", [], group="2b",
         example="Han läser tidningen varje morgon.", example_en="He reads the paper every morning."),
    verb("skriva", "to write", [], group="4", pres="skriver", pret="skrev", sup="skrivit",
         example="Jag skriver ett mejl till chefen.", example_en="I'm writing an email to my boss."),
    verb("sova", "to sleep", [], group="4", pres="sover", pret="sov", sup="sovit",
         example="Bebisen sover äntligen.", example_en="The baby's asleep at last."),
    verb("cykla", "to cycle", ["transport"], group="1",
         example="Jag cyklar till jobbet.", example_en="I cycle to work."),
    verb("köpa", "to buy", [], group="2b",
         example="Vi köper bröd på bageriet.", example_en="We buy bread at the bakery."),
    verb("betala", "to pay", [], group="1",
         example="Kan jag betala med kort?", example_en="Can I pay by card?"),
    verb("leta", "to look (for), to search", [], group="1",
         example="Jag letar efter mina glasögon.", example_en="I'm looking for my glasses."),
    verb("hitta", "to find", [], group="1",
         example="Jag hittar inte min telefon.", example_en="I can't find my phone."),
    verb("tycka", "to think (have an opinion)", [], group="2b", fut="kommer att",
         example="Vad tycker du om filmen?", example_en="What do you think of the film?"),
    verb("tänka", "to think", [], group="2b",
         example="Jag tänker på dig.", example_en="I'm thinking of you."),
    verb("ge", "to give", [], group="4", pres="ger", pret="gav", sup="gett",
         example="Kan du ge mig vattnet?", example_en="Can you give me the water?"),
    verb("ta", "to take", [], group="4", pres="tar", pret="tog", sup="tagit",
         example="Vi tar tåget till Göteborg.", example_en="We're taking the train to Gothenburg."),
    verb("börja", "to begin, to start", [], group="1",
         example="Filmen börjar klockan åtta.", example_en="The film starts at eight."),
    verb("stanna", "to stay; to stop", [], group="1",
         example="Vi stannar hemma i dag.", example_en="We're staying at home today."),
    verb("stå", "to stand", [], group="4", pres="står", pret="stod", sup="stått",
         example="Vi står i kö.", example_en="We're queueing."),
    verb("sitta", "to sit", [], group="4", pres="sitter", pret="satt", sup="suttit",
         example="Får jag sitta bredvid dig?", example_en="May I sit next to you?"),
    verb("ligga", "to lie; to be (somewhere)", [], group="4", pres="ligger", pret="låg", sup="legat",
         example="Boken ligger på bordet.", example_en="The book is on the table."),
    verb("vänta", "to wait", [], group="1",
         example="Vänta lite, jag kommer!", example_en="Wait a moment, I'm coming!"),
    verb("laga", "to cook (laga mat); to mend", [], group="1",
         example="Vem lagar maten i kväll?", example_en="Who's cooking tonight?"),
    verb("hjälpa", "to help", [], group="2b",
         example="Hjälper du mig med väskan?", example_en="Will you help me with the bag?"),
    verb("fråga", "to ask", [], group="1",
         example="Får jag fråga en sak?", example_en="Can I ask you something?"),
    verb("förstå", "to understand", [], group="4", pres="förstår", pret="förstod", sup="förstått",
         fut="kommer att",
         example="Förstår du vad jag menar?", example_en="Do you understand what I mean?"),
    verb("åka", "to go (by car, bus, train), to travel", ["transport"], group="2b",
         example="Vi åker till landet i helgen.", example_en="We're going to the countryside at the weekend."),
    verb("prata", "to talk, to chat", [], group="1",
         example="Vi pratar ofta i telefon.", example_en="We often talk on the phone."),
    verb("fika", "to have a coffee break", ["food"], group="1",
         example="Ska vi fika efter jobbet?", example_en="Shall we get a coffee after work?"),
    verb("gilla", "to like", [], group="1",
         example="Jag gillar din nya tröja.", example_en="I like your new jumper."),
]

PHRASES = phrases(
    """
hej | hi, hello | Hej, jag heter Sara. | Hi, I'm Sara.
hej då | bye | Hej då, vi ses i morgon! | Bye, see you tomorrow!
god morgon | good morning | God morgon! Har du sovit gott? | Good morning! Did you sleep well?
god natt | good night | God natt och sov gott! | Good night, sleep well!
tack | thanks, thank you; please | Tack för hjälpen! | Thanks for your help! | | Swedish has no everyday word for *please*. *Tack* covers it when you accept or ask for something: *En kaffe, tack.* *Snälla* is a pleading please: *Snälla, hjälp mig!*
tack så mycket | thank you very much | Tack så mycket för presenten! | Thank you so much for the present!
varsågod | here you are; help yourself | Varsågod, här är ditt kaffe. | Here you are, here's your coffee. | be so good | Said when you hand something over, and by the host when the food is on the table.
ingen orsak | you're welcome | Ingen orsak, det var så lite. | You're welcome, it was nothing. | no reason
förlåt | sorry | Förlåt, jag kommer lite sent. | Sorry, I'm a bit late.
ursäkta | excuse me | Ursäkta, var ligger stationen? | Excuse me, where's the station?
vi ses | see you | Vi ses på lördag! | See you on Saturday! | we see each other
hur mår du? | how are you? | Hej Anna, hur mår du i dag? | Hi Anna, how are you today?
bara bra | fine, just fine | Bara bra, tack. Och du? | Just fine, thanks. And you? | only good
välkommen | welcome | Välkommen till Sverige! | Welcome to Sweden!
trevligt att träffas | nice to meet you | Jag heter Erik. Trevligt att träffas! | I'm Erik. Nice to meet you!
ja | yes | Ja, det låter bra! | Yes, that sounds good!
nej | no | Nej tack, jag är mätt. | No thanks, I'm full.
jo | yes (to a question with inte) | Är du inte hungrig? Jo, lite. | Aren't you hungry? Yes, a bit. | | The yes that contradicts a negative question. *Ja* there would sound as if you agree with the *inte*.
tack för maten | thanks for the meal | Tack för maten, det var jättegott! | Thanks for the meal, it was delicious! | thanks for the food | Said to the cook or the host after every meal, at home too.
ha det så bra | take care | Hej då, ha det så bra! | Bye, take care! | have it so good
trevlig helg | have a nice weekend | Hej då och trevlig helg! | Bye, and have a nice weekend!
grattis | congratulations; happy birthday | Grattis på födelsedagen! | Happy birthday!
skål | cheers | Skål och välkommen hem! | Cheers, and welcome home!
det gör inget | never mind, it doesn't matter | Det gör inget, jag väntar gärna. | Never mind, I'm happy to wait. | it does nothing
ingen fara | no worries, no problem | Ingen fara, det händer alla. | No worries, it happens to everyone. | no danger
självklart | of course | Självklart kan du låna min cykel. | Of course you can borrow my bike.
gärna | gladly, I'd love to | Vill du ha mer kaffe? Ja, gärna! | Would you like more coffee? Yes, please!
"""
    ,
    ["greetings"],
) + phrases(
    """
talar du engelska? | do you speak English? | Ursäkta, talar du engelska? | Excuse me, do you speak English?
jag förstår inte | I don't understand | Förlåt, jag förstår inte. | Sorry, I don't understand.
kan du upprepa det? | could you say that again? | Förlåt, kan du upprepa det? | Sorry, could you say that again? | can you repeat it
vad kostar det? | how much is it? | Ursäkta, vad kostar det? | Excuse me, how much is it? | what costs it
var är toaletten? | where's the toilet? | Ursäkta, var är toaletten? | Excuse me, where's the toilet?
vad är klockan? | what time is it? | Vet du vad klockan är? | Do you know what time it is? | what is the clock
vad heter du? | what's your name? | Hej! Vad heter du? | Hi! What's your name? | what are you called
var bor du? | where do you live? | Var bor du någonstans? | Whereabouts do you live?
hur gammal är du? | how old are you? | Hur gammal är du? Jag är tjugo. | How old are you? I'm twenty.
jag kommer från | I'm from | Jag kommer från Kanada. | I'm from Canada. | I come from
jag vet inte | I don't know | Jag vet inte var han bor. | I don't know where he lives.
""",
    ["fragor"],
)

CONNECTIVES = connectors(
    "connective",
    """
först | first, first of all | conn-sequence | Först duschar jag och sedan äter jag frukost. | First I have a shower and then I have breakfast. | Jag duschar först och sedan äter jag frukost.
också | also, too | conn-addition | Min bror bor också i Stockholm. | My brother lives in Stockholm too.
ändå | still, anyway | conn-contrast | Det regnade, men vi gick ut ändå. | It was raining, but we went out anyway. | Det regnade, men vi gick ändå ut.
""",
    ["sambandsord"],
)

CONJUNCTIONS = connectors(
    "conjunction",
    """
och | and | conj-coordinating | Jag dricker kaffe och hon dricker te. | I drink coffee and she drinks tea.
eller | or | conj-coordinating | Vill du ha kaffe eller te? | Would you like coffee or tea?
att | that | conj-subordinating | Jag tror att han är hemma. | I think he's at home.
när | when | conj-subordinating | Ring mig när du är hemma. | Call me when you're home.
""",
    ["konjunktioner"],
)

PRONOUNS = phrases(
    """
jag | I | Jag heter Sara och jag bor i Malmö. | I'm Sara and I live in Malmö. | | Said *ja*. As the object of a verb or after a preposition it's *mig*, said *mej*.
du | you (one person) | Du pratar bra svenska! | You speak good Swedish! | | Swedes say *du* to almost everyone, the boss and the doctor too.
han | he | Han arbetar på ett kafé. | He works at a café. | | As the object of a verb or after a preposition it's *honom*: *Jag ser honom.*
hon | she | Hon bor i Göteborg. | She lives in Gothenburg. | | As the object of a verb or after a preposition it's *henne*.
den | it (for an en-word) | Jag har en ny cykel. Den är röd. | I have a new bike. It's red. | | Stands for an en-word: *en cykel*, so *den*.
det | it (for an ett-word) | Huset är gammalt, men det är fint. | The house is old, but it's nice. | | Said *de*. Also the empty *it* of *det regnar* (it's raining).
vi | we | Vi bor i Uppsala. | We live in Uppsala. | | As the object of a verb or after a preposition it's *oss*.
ni | you (more than one) | Vill ni ha kaffe? | Would you all like coffee? | | To one person it sounds old-fashioned or cold. Say *du*.
de | they | De kommer från Norge. | They're from Norway. | | Said *dom*. As the object of a verb or after a preposition it's *dem*, also said *dom*.
hen | he or she | Hen heter Alex. | Their name is Alex. | | For someone whose gender isn't known or doesn't matter, and for people who are neither.
""",
    ["pronomen"],
)

ORDER = phrases(
    """
nu | now | Nu måste jag gå. | I have to go now. | | First in the sentence, so the verb comes straight after it.
i dag | today | I dag är det måndag. | It's Monday today. | | Also written *idag*.
i kväll | tonight, this evening | I kväll äter vi hemma. | We're eating at home tonight. | | Also written *ikväll*.
här | here | Här är nyckeln. | Here's the key.
där | there | Där borta ligger stationen. | The station is over there. | | *Där borta* is *over there*.
alltid | always | Jag dricker alltid kaffe på morgonen. | I always drink coffee in the morning. | | Goes straight after the verb, like *inte*.
ofta | often | Vi äter ofta fisk. | We often eat fish. | | Goes straight after the verb, like *inte*.
ibland | sometimes | Ibland cyklar jag till jobbet. | Sometimes I cycle to work. | | First in the sentence, it puts the verb before the subject.
""",
    ["ordfoljd"],
)
for p in ORDER:
    if p["primary_form"] == "här":
        p["id"] = "har-adverb"

NEGATIVES = phrases(
    """
inte | not | Jag talar inte tyska. | I don't speak German. | | Comes after the verb. Swedish has no *do* in a negative.
ingen | no, not any (before an en-word); nobody | Det finns ingen mjölk kvar. | There's no milk left. | | Alone it means *nobody*: *Ingen vet.*
inget | no, not any (before an ett-word); nothing | Jag har inget paraply. | I don't have an umbrella. | | Also *nothing*, as in *det gör inget*.
inga | no, not any (before a plural) | Det finns inga bussar i dag. | There are no buses today.
aldrig | never | Jag dricker aldrig kaffe på kvällen. | I never drink coffee in the evening. | | Goes where *inte* goes.
ingenting | nothing | Jag förstår ingenting! | I don't understand anything!
inte än | not yet | Är du klar? Inte än. | Are you done? Not yet. | | In a sentence *än* goes to the end: *Han är inte här än.*
inte längre | no longer, not any more | Jag röker inte längre. | I don't smoke any more. | | In a sentence *längre* goes to the end: *Hon bor inte här längre.*
""",
    ["negation"],
)

NUMBERS = phrases(
    """
ett | one | Jag har bara ett barn. | I only have one child. | | *En* before an en-word, *ett* before an ett-word and when you count: *ett, två, tre*.
två | two | Två kaffe, tack. | Two coffees, please.
tre | three | Vi är tre i familjen. | There are three of us in the family.
fyra | four | Lektionen börjar klockan fyra. | The lesson starts at four.
fem | five | Min dotter är fem år. | My daughter is five.
sex | six | Det finns sex ägg i kylskåpet. | There are six eggs in the fridge.
sju | seven | En vecka har sju dagar. | A week has seven days. | | Starts with the breathy sj-sound.
åtta | eight | Jag arbetar åtta timmar om dagen. | I work eight hours a day.
nio | nine | Museet öppnar klockan nio. | The museum opens at nine.
tio | ten | Det kostar tio kronor. | It costs ten kronor.
""",
    ["tal"],
)

ITEMS = PAGES + interleave(
    PHRASES, PRONOUNS + ORDER + NEGATIVES + NUMBERS, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS
)

UNITS = [
    {
        "title": "Uttal",
        "page_id": "sv-pronunciation",
        "word_ids": ["hej", "hej-da", "god-morgon", "god-natt", "tack", "tack-sa-mycket", "varsagod"],
    },
    {
        "title": "Pronomen",
        "page_id": "sv-pronouns",
        "word_ids": ["jag", "du", "han", "hon", "den", "det", "vi", "ni", "de", "hen"],
    },
    {
        "title": "Vara och ha",
        "page_id": "sv-vara-ha",
        "word_ids": ["vara", "ha", "gora", "komma", "vilja", "kunna", "maste"],
    },
    {
        "title": "Presens",
        "page_id": "sv-present-tense",
        "word_ids": ["arbeta", "bo", "heta", "prata", "spela", "titta", "lyssna"],
    },
    {
        "title": "Verbet på andra plats",
        "page_id": "sv-word-order",
        "word_ids": ["aka", "nu", "i-dag", "i-kvall", "har-adverb", "dar", "alltid", "ofta", "ibland"],
    },
    {
        "title": "Inte och ingen",
        "page_id": "sv-negation",
        "word_ids": ["inte", "ingen", "inget", "inga", "aldrig", "ingenting", "inte-an", "inte-langre"],
    },
    {
        "title": "Frågor",
        "page_id": "sv-questions",
        "word_ids": [
            "talar-du-engelska",
            "jag-forstar-inte",
            "kan-du-upprepa-det",
            "vad-kostar-det",
            "var-ar-toaletten",
            "vad-ar-klockan",
            "vad-heter-du",
        ],
    },
    {
        "title": "Bestämd form",
        "page_id": "sv-definite-form",
        "word_ids": ["rum", "sovrum", "kok", "badrum", "vardagsrum", "sang", "nyckel"],
    },
    {
        "title": "En eller ett",
        "page_id": "sv-en-ett",
        "word_ids": ["huvud", "oga", "ora", "nasa", "mun", "hjarta"],
    },
    {
        "title": "Tal och klockan",
        "page_id": "sv-numbers-time",
        "word_ids": ["ett", "tva", "tre", "fyra", "fem", "sex", "sju", "atta", "nio", "tio"],
    },
    {
        "title": "Min, mitt och mina",
        "page_id": "sv-possessives",
        "word_ids": ["pappa", "mamma", "bror", "syster", "son", "dotter", "man", "fru"],
    },
    {
        "title": "Färger",
        "word_ids": ["rod", "bla", "gron", "gul", "svart", "vit", "brun", "rosa"],
    },
    {
        "title": "Små ord",
        "word_ids": ["forst", "ocksa", "anda", "och", "eller", "att", "nar"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "food": "Mat",
    "home": "Hemma",
    "time": "Tid",
    "people": "Människor",
    "adjektiv": "Adjektiv",
    "presens": "Verb",
}

PACK = pack(
    "sv-foundations-v1",
    2,
    "sv",
    "Svenska · Grunder (A1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Övning"),
)
