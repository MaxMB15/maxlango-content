"""Dutch Base Packs, in curriculum order."""

import nl_everyday
import nl_fluency
import nl_foundations
from common import page
from core_patch import patch_core
from nl_conj import conjugate, participle


def _core_verb(inf, stem, **kw):
    return (
        conjugate(inf, stem, **kw),
        {"auxiliary": kw.get("aux", "hebben"), "participle": participle(inf, stem, **kw)},
    )


def _fix_echter(item):
    # "Het regent, echter wij gaan" is not Dutch: echter inverts or sits mid-clause.
    item["extras"]["example"] = "Het regent. Wij gaan echter toch naar buiten."


ARTICLES = page(
    "nl-articles-de-het",
    "De, het and een",
    r"""
Dutch has two words for "the": **de** and **het**. Every noun takes one of them, and the noun decides which.

| | de-word | het-word |
| --- | --- | --- |
| the | de kat | het huis |
| a, an | een kat | een huis |
| the (plural) | de katten | de huizen |

- **De** goes with about three nouns in four, the common-gender nouns.
- **Het** goes with the neuter nouns, and with every diminutive.
- **Een** (a, an) is the same for both. Unstressed, it sounds like *un*. Stressed and written **één**, it means "one".
- Every plural takes **de**.

The article also decides the form of other words: *het grote huis* but *een groot huis*, and *deze kat* but *dit huis* (this).

:::examples
- De kat slaapt op de bank. — The cat is sleeping on the sofa.
- Het huis is groot en mooi. — The house is big and beautiful.
- De man leest het boek. — The man is reading the book.
:::

## This, that, which, every

The words for *this*, *that*, *which* and *every* have a de-word form and a het-word form too:

| | de-word | het-word | plural |
| --- | --- | --- | --- |
| this | deze kat | dit huis | deze huizen |
| that | die kat | dat huis | die huizen |
| which | welke kat | welk huis | welke huizen |
| every | elke kat | elk huis | — |

A plural always takes the de-word form, even when its singular is a het-word: *dit huis*, but *deze huizen*.

So learn every noun with its article: **de kat**, never just *kat*. A few endings and meanings do predict the article, and the **de** and **het** tags on a noun open a page about them.
""",
    ["lidwoorden"],
    "nl-articles",
    explains=["lidwoorden"],
)
# The session's Reading card shows these plain sentences and cloze lines,
# and leaves out the :::examples block the page itself shows.
ARTICLES["extras"] = {
    "examples": ["De kat slaapt op de bank.", "Het huis is groot en mooi.", "De man leest het boek."],
    "cloze": [{"sentence": "___ katje slaapt.", "blank": "Het"}, {"sentence": "___ boeken liggen op tafel.", "blank": "De"}],
    **ARTICLES["extras"],
}

# Upserted into the committed core pack. Every page after ARTICLES only
# explains a Tag: it unlocks nothing, so no session pushes it as Reading, and
# it opens when the learner taps one of its Tags.
CORE_PAGES = [
    ARTICLES,
    page(
        "nl-de-het-words",
        "De-words and het-words",
        r"""
Most nouns you have to learn with their article. Some groups of nouns, though, always or nearly always take the same one, and knowing them saves a lot of guessing.

## Always het

- **Diminutives**: *het huisje*, *het meisje*, *het kopje*. Even *de tafel* becomes *het tafeltje*.
- **Infinitives used as nouns**: *het eten* (food), *het leven* (life), *het lezen* (reading).
- **Languages**: *het Nederlands*, *het Engels*.

## Usually het

- Words ending in **-isme** or **-ment**: *het toerisme*, *het appartement*, *het moment*.
- Words ending in **-um**: *het museum*, *het centrum*. *De datum* is the exception you'll meet.
- Nouns made from a verb with an unstressed **ge-**, **be-**, **ver-** or **ont-** and no ending: *het gesprek*, *het begin*, *het verhaal*, *het ontbijt*. With an ending like *-ing*, it's *de*: *de vergadering*.
- Metals: *het goud*, *het zilver*, *het ijzer*.

## Always de

- **Plurals**: *de huizen*, *de kinderen*.
- Words ending in **-heid**, **-tie** or **-teit**: *de vrijheid*, *de informatie*, *de universiteit*.
- Nouns made from a verb with **-ing**: *wonen*, *de woning*; *oefenen*, *de oefening*.

## Usually de

Words for people: *de man*, *de vrouw*, *de leraar*. *Het kind* is the big exception, and *het meisje* is a diminutive.

## Compounds

A compound takes the article of its last part: *de deur*, so *de voordeur*; *het huis*, so *het ziekenhuis*.

If a noun fits none of these, guess **de**. You'll be right about three times in four.

:::examples
- Het meisje drinkt een kopje thee. — The girl is drinking a cup of tea.
- Het eten is klaar. — Dinner's ready.
- De vergadering begint om negen uur. — The meeting starts at nine.
- Het ziekenhuis ligt naast het station. — The hospital is next to the station.
:::
""",
        ["de", "het"],
        explains=["de", "het"],
    ),
    page(
        "nl-future",
        "The future: zullen and gaan",
        r"""
The **toekomende tijd** is **zullen** plus an infinitive, and the infinitive goes to the end of the clause.

| | zullen |
| --- | --- |
| ik | zal |
| jij, u | zult / zal |
| hij, zij, het | zal |
| wij, jullie, zij | zullen |

*Zult* drops its -t when *je* follows, as every verb does: *Zul je het doen?*

## When Dutch says zullen

Dutch uses *zullen* far less than English uses *will*. It's mostly for promises, predictions and suggestions:

- A promise: *Ik zal je helpen.* (I'll help you.)
- A prediction or a guess: *Het zal wel meevallen.* (It probably won't be that bad.) *Hij zal wel moe zijn.* (He must be tired.)
- A suggestion, as a question: *Zullen we gaan?* (Shall we go?)

## Plans: the present or gaan

For plans and arrangements, Dutch uses the present tense with a time word, or **gaan** plus an infinitive, the everyday "going to":

- *Ik bel je morgen.* (I'll call you tomorrow.)
- *We gaan vanavond koken.* (We're going to cook tonight.)

:::examples
- Ik zal je morgen helpen. — I'll help you tomorrow.
- Zullen we morgen gaan zwemmen? — Shall we go swimming tomorrow?
- Volgend jaar gaan we in Spanje wonen. — Next year we're going to live in Spain.
- De trein vertrekt om acht uur. — The train leaves at eight.
:::
""",
        ["toekomende-tijd"],
        explains=["toekomende-tijd"],
    ),
    page(
        "nl-coordinating-conjunctions",
        "En, maar, of, want and dus",
        r"""
Five short words link two main clauses, or two words, and leave the word order alone: **en** (and), **maar** (but), **of** (or), **want** (because, for) and **dus** (so). Both clauses keep the verb in second place.

:::examples
- Ik kook en jij wast af. — I cook and you do the dishes.
- Het is koud, maar de zon schijnt. — It's cold, but the sun is shining.
- Wil je thee of koffie? — Do you want tea or coffee?
- Ik ga naar bed, want ik ben moe. — I'm going to bed, because I'm tired.
- Het regent, dus we blijven binnen. — It's raining, so we're staying in.
:::

## The conjunction takes no place

The conjunction stands outside the clause it starts, so that clause begins as it would on its own. When it opens with something other than the subject, the verb still comes second: *Ik werk vandaag, maar **morgen heb** ik tijd.*

## Want or omdat?

Both mean "because". **Want** keeps the order: *Ik blijf thuis, want ik **ben** moe.* **Omdat** starts a subordinate clause and sends the verb to the end: *Ik blijf thuis omdat ik moe **ben**.*

## Dus and of

- **Dus** can also take the first place itself, like an adverb, with the verb straight after it: *Het regent, dus **blijven** we binnen.* Both orders are correct.
- **Of** also means "whether", and then it sends the verb to the end: *Ik weet niet of hij **komt**.*
""",
        ["conj-coordinating"],
        explains=["conj-coordinating"],
    ),
    page(
        "nl-contrast-connectives",
        "Echter and toch",
        r"""
A contrast connective says that what comes next goes against what came before, or against what you'd expect.

| Dutch | English |
| --- | --- |
| echter | however |
| toch | still, all the same |
| aan de andere kant | on the other hand |
| desondanks | nevertheless |
| integendeel | on the contrary |

## Word order

These words are adverbs, not conjunctions like *maar*. When one starts a clause it takes the first place, so the verb follows straight after: *Toch **ging** hij.* *Desondanks **is** het gelukt.*

*Echter* usually goes after the verb rather than first: *Het plan is **echter** duur.* *Integendeel* stands apart with a comma, and the clause after it keeps its own order: *Hij is niet verlegen; integendeel, hij praat met iedereen.*

## Maar and hoewel

**Maar** (but) joins two clauses without taking a place, so nothing moves: *Het regende, maar we zijn toch gegaan.* **Hoewel** (although) starts a subordinate clause and sends its verb to the end: *Hoewel het **regende**, zijn we gegaan.*

:::examples
- Het regent. Wij gaan echter toch naar buiten. — It's raining. However, we're still going outside.
- Het huis is klein; aan de andere kant is het goedkoop. — The house is small; on the other hand, it's cheap.
- Het was moeilijk; desondanks is het gelukt. — It was hard; nevertheless, it worked.
:::
""",
        ["conn-contrast"],
        explains=["conn-contrast"],
    ),
    page(
        "nl-cause-connectives",
        "Namelijk and immers",
        r"""
A cause connective gives the reason for what was just said. Two adverbs do this job:

| Dutch | English |
| --- | --- |
| namelijk | you see, because; namely |
| immers | after all |

*Namelijk* brings in a reason the listener didn't know: *Ik blijf thuis, ik ben **namelijk** ziek.* It comes after the verb, never first: *Namelijk ben ik ziek* is wrong. *Immers* points to a reason the listener already knows: *Hij kan niet komen; hij is **immers** ziek.*

## Want, omdat and doordat

The plain words for "because" are conjunctions, and each treats word order differently:

- **Want** joins two main clauses and moves nothing: *Ik blijf thuis, want ik ben moe.*
- **Omdat** starts a subordinate clause, so its verb goes to the end: *Ik blijf thuis omdat ik moe ben.*
- **Doordat** names what caused something, not why someone chose it, and also sends the verb to the end: *Doordat de trein vertraging had, kwam ik te laat.*

To give a result instead of a reason, use *dus* or *daarom*: *Ik was ziek, daarom ben ik niet gekomen.*

:::examples
- Ik blijf thuis, ik ben namelijk ziek. — I'm staying at home; I'm ill, you see.
- Hij kan niet komen; hij is immers ziek. — He can't come; he's ill, after all.
- Ik blijf thuis omdat ik moe ben. — I'm staying at home because I'm tired.
:::
""",
        ["conn-cause"],
        explains=["conn-cause"],
    ),
    page(
        "nl-addition-connectives",
        "Ook and bovendien",
        r"""
An addition connective adds one more point to what was said.

| Dutch | English |
| --- | --- |
| ook | also, too |
| bovendien | moreover, besides |
| verder | apart from that, further |
| trouwens | by the way, besides |
| overigens | incidentally |

## Word order

Like other adverbs, they take the first place when they start a clause, and the verb follows: *Bovendien **is** hij saai.* *Verder **heb** ik niets nodig.* Inside a main clause they come after the verb: *Ik spreek **ook** Frans.*

*Trouwens* often stands apart at the start, with a comma, and the sentence after it keeps its own order: *Trouwens, heb je mijn sleutels gezien?*

## En

The conjunction **en** (and) adds too, but it joins two clauses without taking a place in either: *Ik spreek Engels en ik spreek ook Frans.*

:::examples
- Ik spreek Engels, en ik spreek ook Frans. — I speak English, and I also speak French.
- De film is lang, bovendien is hij saai. — The film is long; besides, it's boring.
- Verder heb ik niets nodig. — Apart from that, I don't need anything.
- Trouwens, heb je mijn sleutels gezien? — By the way, have you seen my keys?
:::
""",
        ["conn-addition"],
        explains=["conn-addition"],
    ),
    page(
        "nl-sequence-connectives",
        "Eerst, dan and daarna",
        r"""
Sequence connectives put events in order: first this, then that, and finally the last thing.

| Dutch | English |
| --- | --- |
| eerst | first |
| dan | then |
| daarna | after that, afterwards |
| ten slotte | finally, lastly |
| uiteindelijk | in the end |
| eindelijk | at last |

At the start of a clause each one takes the first place, so the verb follows straight after: *Eerst **eten** we, dan **gaan** we weg.*

## Three kinds of finally

- **Ten slotte** brings in the last item of a list: *Ten slotte wil ik iedereen bedanken.*
- **Uiteindelijk** says how things turned out: *Uiteindelijk zijn we gebleven.*
- **Eindelijk** is relief after a wait: *Eindelijk is het weekend!*

## Toen in a story

When you tell what happened in the past, "then" is usually **toen** or **daarna** rather than *dan*: *We aten eerst, toen gingen we naar huis.*

:::examples
- Eerst eten we, dan gaan we weg. — First we eat, then we leave.
- We eten eerst, daarna gaan we weg. — We'll eat first, and after that we'll leave.
- We twijfelden lang, maar uiteindelijk zijn we gebleven. — We hesitated a long time, but in the end we stayed.
- Eindelijk is het weekend! — At last, it's the weekend!
:::
""",
        ["conn-sequence"],
        explains=["conn-sequence"],
    ),
]

CORE = patch_core(
    "nl",
    9,
    {
        "eten": _core_verb("eten", "eet", past="at aten", pp="gegeten"),
        "drinken": _core_verb("drinken", "drink", past="dronk dronken", pp="gedronken"),
        "spreken": _core_verb("spreken", "spreek", past="sprak spraken", pp="gesproken"),
        "gaan": _core_verb(
            "gaan", "ga", aux="zijn", present="ga gaat gaat gaan gaan gaan", past="ging gingen", pp="gegaan"
        ),
    },
    fixes={("connective", "echter"): _fix_echter},
    pages=CORE_PAGES,
)

PACKS = [CORE, nl_foundations.PACK, nl_everyday.PACK, nl_fluency.PACK]
