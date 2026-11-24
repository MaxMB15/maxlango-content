"""Swedish Base Packs, in curriculum order.

Swedish has no hand-written core pack to patch, so the core is built here
directly, modelled on fr-core-v1: the articles page, the plural page, the
two conjunction pages and the four connective pages, with the same kinds of
Words.
"""

import sv_everyday
import sv_fluency
import sv_foundations
from common import pack, page, topic
from sv_common import connectors, nouns, verb

DELTA = [
    topic("home", "Hem", "home", ["artiklar"]),
    topic("food", "Mat", "food", ["artiklar"]),
    topic(
        "sambandsord",
        "Sambandsord",
        "connectives",
        ["conn-contrast", "conn-cause", "conn-addition", "conn-sequence"],
    ),
    topic("konjunktioner", "Konjunktioner", "conjunctions", ["conj-coordinating", "conj-subordinating"]),
    topic("animals", "Djur", "animals", ["artiklar"]),
    topic("nature", "Natur", "nature", ["artiklar"]),
    topic("people", "Människor", "people", ["artiklar"]),
    topic("objects", "Föremål", "objects", ["artiklar"]),
    topic("transport", "Transport", "transport", ["artiklar"]),
    topic("time", "Tid", "time", ["artiklar"]),
]

ARTICLES = page(
    "sv-articles",
    "En, ett and the",
    r"""
Swedish nouns come in two genders: **en-words** (common gender) and **ett-words** (neuter). About three nouns in four are en-words, and the noun decides which it is.

| | en-word | ett-word |
| --- | --- | --- |
| a, an | en katt | ett hus |
| the | katten | huset |
| the (plural) | katterna | husen |

- **En** and **ett** mean *a, an*. **Ett** is also the number *one*: *ett år* is "a year" or "one year".
- Swedish has no separate word for *the*. It's an ending on the noun: **-en** or **-n** for en-words, **-et** or **-t** for ett-words: *katten*, *huset*, *äpplet*.
- Plurals have their own *the*-ending, mostly **-na**: *katterna*, *bilarna*. A plural with no ending of its own takes **-en**: *husen*.

The gender also decides the form of other words: *en stor bil* but *ett stort hus*, and *min katt* but *mitt hus* (my).

:::examples
- Katten sover på soffan. — The cat is sleeping on the sofa.
- Huset är stort och vackert. — The house is big and beautiful.
- Mannen läser en bok. — The man is reading a book.
:::

## This, that, which, no

| | en-word | ett-word | plural |
| --- | --- | --- | --- |
| this | den här katten | det här huset | de här husen |
| that | den där katten | det där huset | de där husen |
| which | vilken katt | vilket hus | vilka hus |
| no, not any | ingen katt | inget hus | inga hus |

*Den här katten*, "this cat", keeps the *the*-ending on the noun. English speakers tend to drop it.

So learn every noun with its article: **en katt**, **ett hus**, never just *katt*. A few endings and meanings do predict the gender, and the **en** and **ett** tags on a noun open a page about them.
""",
    ["artiklar"],
    "sv-articles",
    explains=["artiklar"],
)
# The session's Reading card shows these plain sentences and cloze lines,
# and leaves out the :::examples block the page itself shows.
ARTICLES["extras"] = {
    "examples": ["Katten sover på soffan.", "Huset är stort och vackert.", "Mannen läser en bok."],
    "cloze": [
        {"sentence": "Jag bor i ___ litet hus.", "blank": "ett"},
        {"sentence": "Hon har ___ ny bil.", "blank": "en"},
    ],
    **ARTICLES["extras"],
}

PLURAL = page(
    "sv-plural",
    "Plural: five endings",
    r"""
English adds *-s*. Swedish has five ways to make a plural, and the noun's gender and its last sound pick the way.

| Group | Ending | Which nouns | Example |
| --- | --- | --- | --- |
| 1 | -or | en-words ending in -a | en flicka, två flickor |
| 2 | -ar | many short en-words, and en-words in -e, -el, -en, -er | en bil, två bilar |
| 3 | -er | many en-words borrowed from other languages | en telefon, två telefoner |
| 4 | -n | ett-words ending in a vowel | ett äpple, två äpplen |
| 5 | no ending | ett-words ending in a consonant, en-words in -are | ett hus, två hus |

The groups are a strong guide, not a law: *en pojke* takes -ar (*pojkar*), but *en sko* takes -r (*skor*). The plural is on every noun's card, so learn it with the word: *en bil, bilar*.

## Vowel changes

A few common nouns change their vowel, as English *man* becomes *men*:

| Singular | Plural |
| --- | --- |
| en man | män |
| en hand | händer |
| en bok | böcker |
| en fot | fötter |
| en stad | städer |
| en natt | nätter |

## The plural with *the*

Plurals in -or, -ar and -er add **-na**: *bilarna*, *flickorna*. Plurals in -n add **-a**: *äpplena*. A plural with no ending adds **-en**: *husen*, *barnen*. En-words in -are drop the e and add -na: *lärarna* (the teachers).

:::examples
- Barnen leker i parken. — The children are playing in the park.
- Vi har två katter och tre hundar. — We have two cats and three dogs.
- Flickorna äter äpplen. — The girls are eating apples.
:::

:::sort{groups="-or: gata, klocka, skola | -ar: dag, stol, hund | -er: park, färg, sak | -n: hjärta, ställe, möte | no ending: barn, bord, fönster"}
:::
""",
    ["plural"],
    explains=["plural"],
)

CORE_PAGES = [
    page(
        "sv-coordinating-conjunctions",
        "Och, men, eller, för, så",
        r"""
Six short words link two main clauses, or two words, and leave the word order alone: **och** (and), **men** (but), **eller** (or), **för** (because, for), **så** (so) and **utan** (but, after a negative). Both clauses keep the verb in second place.

:::examples
- Jag lagar mat och du diskar. — I cook and you do the dishes.
- Det är kallt, men solen skiner. — It's cold, but the sun is shining.
- Vill du ha te eller kaffe? — Do you want tea or coffee?
- Jag lägger mig nu, för jag är trött. — I'm going to bed now, because I'm tired.
- Det regnar, så vi stannar inne. — It's raining, so we're staying in.
:::

## The conjunction takes no place

The conjunction stands outside the clause it starts, so that clause begins as it would on its own. When it opens with something other than the subject, the verb still comes second: *Jag jobbar i dag, men **i morgon har** jag tid.*

## För or eftersom?

Both mean "because". **För** joins two main clauses and never starts a sentence: *Jag stannar hemma, för jag **är** sjuk.* **Eftersom** starts a subordinate clause, where *inte* jumps in front of the verb: *Jag stannar hemma eftersom jag **inte mår** bra.*

## Men or utan?

Both are "but" in English. When the first part is negative and the second part **replaces** it, Swedish uses **utan**: *Han är inte lärare, utan läkare.* (He isn't a teacher but a doctor.) Everywhere else it's **men**: *Han är lärare, men han vill bli läkare.*

## Så

**Så** can also take the first place itself, like an adverb, with the verb straight after it: *Det regnar, så **stannar** vi inne.* Both orders are correct.
""",
        ["conj-coordinating"],
        explains=["conj-coordinating"],
    ),
    page(
        "sv-subordinating-conjunctions",
        "Att, när, om, eftersom",
        r"""
A subordinating conjunction starts a **bisats**, a clause that leans on the main clause: *Jag stannar hemma **eftersom** jag är trött.* Inside it the subject comes first and the verb straight after, as in English.

| Swedish | English |
| --- | --- |
| att | that |
| när | when |
| om | if, whether |
| eftersom, därför att | because |
| fastän, trots att | although |
| medan | while |
| innan | before |
| tills | until |
| så att | so that |

## Inte goes before the verb

In a main clause, *inte* follows the verb: *Han kommer **inte**.* In a bisats it moves in front of the verb, and so do *aldrig* (never), *alltid* (always), *ofta* (often) and *redan* (already): *Jag vet att han **inte kommer**.* Swedish teachers call this **BIFF**: *i bisats inte före finitum*, "in a bisats, inte before the verb".

## A bisats first

A bisats can open the sentence. It then fills the first place, so the main clause starts with its verb: ***Om** det regnar **stannar** vi hemma.*

## Att can go

As in English, *att* (that) is often left out after verbs like *tro* and *tycka*: *Jag tror (att) hon är hemma.*

## När or om?

English *if* and *when* overlap; Swedish keeps them apart. **När** is for something that will happen: *när du kommer hem* (when you get home). **Om** is for something that may or may not: *om du kommer hem* (if you get home). **Om** also means "whether": *Jag vet inte om han kommer.*

:::examples
- Jag tror att det blir regn. — I think it's going to rain.
- Jag läser när det regnar. — I read when it rains.
- Vi går ut om du vill. — We'll go out if you want.
- Fastän han är ung förstår han mycket. — Although he's young, he understands a lot.
:::
""",
        ["conj-subordinating"],
        explains=["conj-subordinating"],
    ),
    page(
        "sv-contrast-connectives",
        "Dock, ändå and däremot",
        r"""
A contrast connective says that what comes next goes against what came before, or against what you'd expect.

| Swedish | English |
| --- | --- |
| dock | however |
| ändå | still, anyway, all the same |
| däremot | on the other hand, by contrast |
| trots det | despite that, nevertheless |
| tvärtom | on the contrary |
| i stället | instead |

## Word order

These words are adverbs, not conjunctions like *men*. When one starts a clause it takes the first place, so the verb follows straight after: *Ändå **gick** han.* *Trots det **lyckades** vi.*

*Dock* usually sits after the verb rather than first, and it sounds a little written: *Planen är **dock** dyr.* In speech, people more often use *men*.

*Ändå* is the everyday one, and it often comes last: *Det regnade, men vi gick ut **ändå**.*

## Men and fastän

**Men** (but) joins two clauses without taking a place, so nothing moves. **Fastän** (although) starts a bisats, where *inte* goes before the verb: *Fastän det **inte** var varmt badade vi.*

:::examples
- Det snöar. Vi tar dock cykeln till jobbet. — It's snowing. However, we're cycling to work.
- Hon var trött men jobbade ändå. — She was tired but worked anyway.
- Jag gillar kaffe. Min fru dricker däremot bara te. — I like coffee. My wife, on the other hand, only drinks tea.
:::
""",
        ["conn-contrast"],
        explains=["conn-contrast"],
    ),
    page(
        "sv-cause-connectives",
        "Nämligen and ju",
        r"""
A cause connective gives the reason for what was just said.

| Swedish | English |
| --- | --- |
| nämligen | you see, because |
| ju | after all, as you know |
| därför att | because |
| på grund av | because of |
| tack vare | thanks to |

## Nämligen

*Nämligen* gives the reason for the sentence before it, and sits after the verb, never first: *Han äter inte kött. Han **är nämligen** vegetarian.* (He doesn't eat meat. He's a vegetarian, you see.) English has no single word for it: "you see" or "because" comes close.

## Ju

*Ju* means "as we both know". It's short, unstressed and everywhere in speech, and it always comes after the verb: *Du vet **ju** att jag inte äter fisk.* (You know I don't eat fish.)

## På grund av and tack vare

These are prepositions, so a noun follows them, not a clause: *på grund av regnet* (because of the rain), *tack vare dig* (thanks to you). Before a whole clause, use *eftersom* or *därför att*.

:::examples
- Vi kom sent. Bussen var nämligen full. — We were late. The bus was full, you see.
- Tåget var sent på grund av snön. — The train was late because of the snow.
- Det gick bra tack vare dig. — It went well thanks to you.
:::
""",
        ["conn-cause"],
        explains=["conn-cause"],
    ),
    page(
        "sv-addition-connectives",
        "Också and dessutom",
        r"""
An addition connective adds another point to the one before.

| Swedish | English |
| --- | --- |
| också | also, too |
| även | also, even (a little formal) |
| dessutom | besides, what's more |
| för övrigt | moreover, for that matter |
| förresten | by the way |
| inte heller | not ... either |

## Också goes after the verb

English often puts *also* before the verb. Swedish puts *också* after it: *Jag **talar också** franska.* (I also speak French.) *Jag också* is "me too".

## Dessutom

*Dessutom* adds a stronger point, often the one that settles it. At the start of a clause it takes the first place, and the verb follows: *Rummet är litet. Dessutom **är** det dyrt.*

## Inte heller

After a negative, *också* becomes **inte heller**: *Han dricker inte kaffe, och jag gör det inte heller.* "Me neither" is *inte jag heller*.

:::examples
- Hon talar också tyska. — She speaks German too.
- Förresten, har du sett min nyckel? — By the way, have you seen my key?
- Jag har inte heller tid. — I don't have time either.
:::
""",
        ["conn-addition"],
        explains=["conn-addition"],
    ),
    page(
        "sv-sequence-connectives",
        "Först, sedan and till sist",
        r"""
A sequence connective puts events, or the steps of an argument, in order.

| Swedish | English |
| --- | --- |
| först | first |
| sedan, sen | then, after that |
| därefter | after that (more formal) |
| till sist, slutligen | finally, lastly |
| till slut | in the end |
| äntligen | at last |

## Word order

At the start of a clause these words take the first place, so the verb follows straight after: *Först **duschar** jag, sedan **äter** jag frukost.* After *och*, the clause still inverts: *och sedan **går** vi.*

## Till slut or äntligen?

**Till slut** is "in the end", after a long time or many tries: *Till slut hittade vi huset.* **Äntligen** is "at last!", the relief when it finally happens: *Äntligen är det fredag!*

## Sedan and sen

*Sen* is the spoken form of *sedan*, and you'll see it written too. Both also mean "since": *sedan i måndags* (since Monday).

:::examples
- Först tvättar vi, sedan städar vi. — First we do the laundry, then we clean.
- Till sist vill jag tacka er alla. — Finally, I'd like to thank you all.
- Äntligen är det helg! — At last it's the weekend!
:::
""",
        ["conn-sequence"],
        explains=["conn-sequence"],
    ),
]

NOUNS = nouns(
    """
fönster | ett | fönstret | fönster | window | home | Kan du öppna fönstret? | Can you open the window?
katt | en | katten | katter | cat | animals | Vår katt heter Musse. | Our cat is called Musse.
hund | en | hunden | hundar | dog | animals | Hunden vill gå ut. | The dog wants to go out.
hus | ett | huset | hus | house | home | De bor i ett gult hus. | They live in a yellow house.
bok | en | boken | böcker | book | objects | Jag läser en spännande bok. | I'm reading an exciting book.
vatten | ett | vattnet | - | water | food | Kan jag få ett glas vatten? | Can I have a glass of water?
bröd | ett | brödet | bröd | bread | food | Brödet är färskt i dag. | The bread is fresh today.
bord | ett | bordet | bord | table | home | Maten står på bordet. | The food is on the table.
stol | en | stolen | stolar | chair | home | Sätt dig på stolen här. | Sit down on this chair here.
dörr | en | dörren | dörrar | door | home | Någon knackar på dörren. | Someone is knocking at the door.
bil | en | bilen | bilar | car | transport | Bilen står utanför huset. | The car is parked outside the house.
träd | ett | trädet | träd | tree | nature | Det står ett stort träd i trädgården. | There's a big tree in the garden.
sol | en | solen | solar | sun | nature | Solen skiner i dag. | The sun is shining today.
natt | en | natten | nätter | night | time | Jag sov dåligt i natt. | I slept badly last night.
vän | en | vännen | vänner | friend | people | Hon är min bästa vän. | She's my best friend.
barn | ett | barnet | barn | child | people | De har tre barn. | They have three children.
"""
)

VERBS = [
    verb(
        "äta",
        "to eat",
        ["food"],
        group="4",
        pres="äter",
        pret="åt",
        sup="ätit",
        example="Vi äter middag klockan sex.",
        example_en="We eat dinner at six o'clock.",
    ),
    verb(
        "dricka",
        "to drink",
        ["food"],
        group="4",
        pres="dricker",
        pret="drack",
        sup="druckit",
        example="Hon dricker kaffe varje morgon.",
        example_en="She drinks coffee every morning.",
    ),
    verb(
        "tala",
        "to speak",
        [],
        group="1",
        example="Talar du engelska eller svenska?",
        example_en="Do you speak English or Swedish?",
    ),
    verb(
        "gå",
        "to go, to walk",
        [],
        group="4",
        pres="går",
        pret="gick",
        sup="gått",
        example="Jag går till jobbet varje dag.",
        example_en="I walk to work every day.",
    ),
]

CONNECTIVES = connectors(
    "connective",
    """
dock | however | conn-contrast | Det regnar. Vi går dock ut på en promenad. | It's raining. However, we're going out for a walk.
nämligen | you see, because | conn-cause | Jag kan inte komma i kväll. Jag är nämligen sjuk. | I can't come tonight. I'm ill, you see.
dessutom | besides, what's more | conn-addition | Filmen är lång. Dessutom är den tråkig. | The film is long. What's more, it's boring. | Filmen är lång. Den är dessutom tråkig.
sedan | then, after that | conn-sequence | Vi äter först och sedan går vi hem. | We'll eat first and then we'll go home. | Först äter vi och sedan går vi hem.
""",
    ["sambandsord"],
)

CONJUNCTIONS = connectors(
    "conjunction",
    """
men | but | conj-coordinating | Det är kallt ute, men solen skiner. | It's cold outside, but the sun is shining.
för | because, for | conj-coordinating | Jag stannar hemma, för jag är trött. | I'm staying home, because I'm tired.
eftersom | because, since | conj-subordinating | Vi tar bussen eftersom det regnar. | We're taking the bus because it's raining. | Eftersom det regnar tar vi bussen.
fastän | although | conj-subordinating | Fastän hon är ung kan hon mycket. | Although she's young, she knows a lot. | Hon kan mycket fastän hon är ung.
""",
    ["konjunktioner"],
)

CORE = pack(
    "sv-core-v1",
    1,
    "sv",
    "Svenska · Kärnord",
    [ARTICLES] + NOUNS + VERBS + CONNECTIVES + CONJUNCTIONS + [PLURAL] + CORE_PAGES,
    DELTA,
)

PACKS = [CORE, sv_foundations.PACK, sv_everyday.PACK, sv_fluency.PACK]
