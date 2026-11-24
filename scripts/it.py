"""Italian Base Packs, in curriculum order.

French and Dutch upgrade a hand-written core pack (core_patch.py). Italian has
none, so its core is built here directly, like the level packs.
"""

import it_everyday
import it_fluency
import it_foundations
from common import pack, page, topic
from it_common import connectors, nouns, verb

DELTA = [
    topic("home", "Casa", "home", ["genere"]),
    topic("food", "Cibo", "food", ["genere"]),
    topic("connettivi", "Connettivi", "connectives", ["conn-contrast", "conn-cause", "conn-addition", "conn-sequence"]),
    topic("congiunzioni", "Congiunzioni", "conjunctions", ["conj-coordinating", "conj-subordinating"]),
    topic("animals", "Animali", "animals", ["genere"]),
    topic("nature", "Natura", "nature", ["genere"]),
    topic("people", "Persone", "people", ["genere"]),
    topic("objects", "Oggetti", "objects", ["genere"]),
    topic("transport", "Trasporti", "transport", ["genere"]),
    topic("time", "Tempo", "time", ["genere"]),
]

ARTICLES = page(
    "it-articles-gender",
    "Il, lo, la and l'",
    r"""
Every Italian noun is **masculine** or **feminine**, and the article shows which. Most masculine nouns end in **-o** and most feminine ones in **-a**. Nouns in **-e** can be either, so learn them with their article.

| | masculine | feminine |
| --- | --- | --- |
| the (singular) | il gatto, lo zio, l'albero | la casa, l'amica |
| the (plural) | i gatti, gli zii, gli alberi | le case, le amiche |
| a, an | un gatto, uno zio, un albero | una casa, un'amica |

Unlike English, the masculine article changes with the sound that follows it:

- **Il** (plural **i**) is the ordinary one: *il libro*, *i libri*.
- **Lo** (plural **gli**) goes before **s + consonant**, **z**, **gn**, **ps**, **x** and **y**: *lo studente*, *lo zucchero*, *gli gnocchi*. Its "a" is **uno**: *uno studente*.
- **L'** goes before any vowel, in both genders: *l'albero*, *l'acqua*. In the plural the masculine becomes **gli** (*gli alberi*) and the feminine **le** (*le amiche*).
- **Un'** with an apostrophe is feminine only: *un'amica* is a female friend, *un amico* a male one.

The article follows the word right after it, adjective or noun: *gli amici*, but *i vecchi amici*; *lo studente*, but *il bravo studente*.

:::examples
- Il gatto dorme sulla sedia. — The cat is sleeping on the chair.
- La finestra è aperta. — The window is open.
- L'acqua è fresca stamattina. — The water is cool this morning.
- Ho un cane e una macchina. — I have a dog and a car.
:::

Italian uses the article far more than English. A general statement takes it, and so do countries: *Mi piace il caffè* (I like coffee), *L'Italia è lunga*.

So learn every noun with its article: **il gatto**, **la casa**, **lo zio**, never the noun alone. When the article is *l'*, learn the gender too: *l'acqua* is feminine, *l'albero* masculine.
""",
    ["articoli", "genere"],
    "it-articles",
    explains=["articoli"],
)
# The session's Reading card shows these plain sentences and cloze lines,
# and leaves out the :::examples block the page itself shows.
ARTICLES["extras"] = {
    "examples": ["Il gatto dorme sulla sedia.", "La finestra è aperta.", "L'acqua è fresca stamattina."],
    "cloze": [{"sentence": "___ cane mangia.", "blank": "Il"}, {"sentence": "___ zaini sono pesanti.", "blank": "Gli"}],
    **ARTICLES["extras"],
}

# Every page after ARTICLES only explains a Tag: it unlocks nothing, so no
# session pushes it as Reading, and it opens when the learner taps one of its
# Tags.
CORE_PAGES = [
    page(
        "it-plural",
        "Plurals: -i, -e, and the ones that stay",
        r"""
An Italian plural changes the last vowel of the noun, and the article changes with it: *il libro*, *i libri*; *la casa*, *le case*.

| Singular ends in | Plural | Example |
| --- | --- | --- |
| -o (mostly masculine) | -i | il libro, i libri |
| -a (feminine) | -e | la casa, le case |
| -a (masculine) | -i | il problema, i problemi |
| -e (either gender) | -i | il cane, i cani; la notte, le notti |

## Nouns that don't change

- Nouns stressed on the last vowel, the ones with a written accent: *la città*, *le città*; *il caffè*, *i caffè*.
- Nouns that end in a consonant, mostly borrowed: *il film*, *i film*; *lo sport*, *gli sport*; *il bar*, *i bar*.
- Shortened words: *la foto*, *le foto*; *la moto*, *le moto*; *il cinema*, *i cinema*.

Only the article tells you these are plural, so listen for it.

## Keeping the hard sound

- **-ca** and **-ga** always keep the hard sound with an h: *l'amica*, *le amiche*; *la banca*, *le banche*.
- **-co** and **-go** usually do too: *il gioco*, *i giochi*; *il lago*, *i laghi*. Some soften instead, and those you just learn: *l'amico*, *gli amici*; *il medico*, *i medici*.
- **-cia** and **-gia** drop the i after a consonant (*l'arancia*, *le arance*; *la spiaggia*, *le spiagge*) and keep it after a vowel (*la camicia*, *le camicie*).

## Irregular plurals

- *l'uomo* (man), *gli uomini*
- *la mano* (hand) is feminine though it ends in -o: *le mani*
- *il braccio* (arm), *le braccia*; *il dito* (finger), *le dita*; *l'uovo* (egg), *le uova*. These turn feminine in the plural and end in -a.

Adjectives follow the same patterns: *un libro rosso*, *due libri rossi*; *una casa bianca*, *due case bianche*.

:::examples
- Ho due gatti e un cane. — I have two cats and a dog.
- Le città italiane sono bellissime. — Italian cities are beautiful.
- Mi fanno male le braccia. — My arms hurt.
- Gli uomini aspettano fuori. — The men are waiting outside.
:::
""",
        ["plurale"],
        explains=["plurale"],
    ),
    page(
        "it-coordinating-conjunctions",
        "E, ma, o and quindi",
        r"""
A coordinating conjunction joins two words, or two clauses of the same kind, and leaves both as they are.

| Italian | English |
| --- | --- |
| e | and |
| ma | but |
| o, oppure | or |
| quindi | so, therefore |
| però | but, however |
| né ... né | neither ... nor |
| anzi | in fact, or rather |

:::examples
- Ho un fratello e una sorella. — I have a brother and a sister.
- Vuoi un tè o un caffè? — Do you want tea or coffee?
- Voglio venire, ma non ho tempo. — I want to come, but I don't have time.
- Fa freddo, quindi metto il cappotto. — It's cold, so I'm putting my coat on.
:::

## E or ed?

Before a word that starts with **e**, *e* often becomes **ed** so the two vowels don't run together: *io ed Elena*. **A** (to) does the same and becomes **ad**: *ad Anna*. Don't confuse **e** (and) with **è** (is): the accent is the whole difference.

## Né ... né

*Né* usually comes twice. When the verb comes first, it takes **non**: *Non bevo né tè né caffè* (I drink neither tea nor coffee).

## Anzi

*Anzi* corrects what you just said, going one better: *Non è brutto, anzi, è bellissimo* (It isn't ugly; in fact, it's beautiful).
""",
        ["conj-coordinating"],
        explains=["conj-coordinating"],
    ),
    page(
        "it-subordinating-conjunctions",
        "Che, quando, se and perché",
        r"""
A subordinating conjunction starts a clause that depends on the main clause: *Resto a casa **perché** sono stanco.* The word order inside that clause stays as it is. What some conjunctions change is the mood of the verb.

| Italian | English |
| --- | --- |
| che | that |
| quando | when |
| se | if, whether |
| perché | because |
| mentre | while |
| siccome | since, as (at the start of the sentence) |
| benché, sebbene | although |
| affinché | so that |
| prima che | before |

## Che stays

English can leave out *that*. Italian can't leave out *che*: *Dice **che** arriva domani* (He says he's arriving tomorrow).

## Some take the congiuntivo

**Benché**, **sebbene**, **affinché**, **prima che** and **a meno che** always take the congiuntivo (subjunctive): *Benché **sia** tardi, resto ancora un po'.* Most others, *perché*, *quando*, *se* and *mentre* among them, take the ordinary indicative.

## Perché has two jobs

*Perché* means "why?" in a question and "because" in the answer: *Perché ridi? Perché sei buffo!* With the congiuntivo it can also mean "so that".

## Se and quando

After *se* and *quando*, careful Italian puts a future time in the future tense, where English uses the present: *Quando **arriverai**, chiamami* (When you arrive, call me). In speech the present is common too.

:::examples
- Penso che arrivi domani. — I think he's arriving tomorrow.
- Leggo quando piove. — I read when it rains.
- Usciamo se vuoi. — We'll go out if you want.
- Resto a casa perché sono stanco. — I'm staying home because I'm tired.
:::
""",
        ["conj-subordinating"],
        explains=["conj-subordinating"],
    ),
    page(
        "it-contrast-connectives",
        "Però, tuttavia and invece",
        r"""
A contrast connective says that what comes next goes against what came before, or against what you'd expect.

| Italian | English |
| --- | --- |
| però | but, however |
| tuttavia | however, nevertheless |
| invece | instead, on the other hand |
| comunque | anyway, all the same |
| eppure | and yet |
| al contrario | on the contrary |

## Which one?

- **Però** is the everyday one. Unlike *ma*, it can move into the clause: *È ricco, però non è felice*, or *È ricco, non è però felice*.
- **Tuttavia** says the same more formally, and suits writing.
- **Eppure** carries surprise, something true against all expectation: *Ha studiato tanto, eppure non ha passato l'esame.*
- **Invece** sets two people or facts side by side, often after the subject: *Io bevo vino, mio fratello invece beve birra.* It also means "instead": *Volevo uscire, invece sono rimasto a casa.*
- **Comunque** means "anyway": whatever was just said, this still holds.

## Ma and benché

**Ma** (but) is the plain way to set up a contrast, and it always comes first in its clause. **Benché** (although) starts a subordinate clause and takes the congiuntivo: *Benché **sia** ricco, non è felice.*

:::examples
- Piove, però usciamo lo stesso. — It's raining, but we're going out anyway.
- È difficile; tuttavia, è possibile. — It's difficult; nevertheless, it's possible.
- Io bevo vino, mio fratello invece beve birra. — I drink wine; my brother, on the other hand, drinks beer.
:::
""",
        ["conn-contrast"],
        explains=["conn-contrast"],
    ),
    page(
        "it-cause-connectives",
        "Infatti and in effetti",
        r"""
A cause connective backs up what was just said: it gives the reason, or the proof.

| Italian | English |
| --- | --- |
| infatti | indeed, and in fact |
| in effetti | actually, it's true that |
| in realtà | actually, in reality |

**Infatti** confirms what came before with a fact that proves it: *Sono stanco; infatti stanotte non ho dormito.* In a conversation it agrees: *Sembrava nervoso. — Infatti!* (He seemed nervous. — He was, wasn't he!) It doesn't correct anything, which is where English speakers go wrong.

**In effetti** admits that something is true, often a point the other person made: *In effetti hai ragione.* **In realtà** is the one that corrects: *Sembra facile, ma in realtà è difficile.*

## Perché, siccome and dato che

- **Perché** is the everyday "because": *Resto a casa perché sono stanco.*
- **Siccome** puts the reason first, at the start of the sentence: *Siccome piove, restiamo a casa.*
- **Dato che** and **visto che** give a reason both sides already know: *Visto che sei qui, aiutami.*
- **Poiché** says the same in formal writing.

:::examples
- Sono stanco; infatti stanotte non ho dormito. — I'm tired; in fact, I didn't sleep last night.
- In effetti hai ragione tu. — Actually, you're right.
- Siccome piove, restiamo a casa. — Since it's raining, we're staying home.
:::
""",
        ["conn-cause"],
        explains=["conn-cause"],
    ),
    page(
        "it-addition-connectives",
        "Anche, inoltre and in più",
        r"""
An addition connective adds one more point to what was said.

| Italian | English |
| --- | --- |
| anche | also, too |
| inoltre | moreover, besides |
| in più | on top of that |
| per di più | what's more |
| oltretutto | on top of everything |
| del resto | besides, after all |

*In più* is the everyday one, *inoltre* suits writing, and *per di più* usually adds something worse.

At the start of a clause they change nothing else: *Inoltre, è troppo caro.*

## Anche

**Anche** goes right before the word it adds to, and moving it changes the meaning:

- *Anche Marco parla francese.* (Marco speaks French too, as well as someone else.)
- *Marco parla anche francese.* (Marco speaks French too, as well as other languages.)

"Me too" is *anch'io*. The negative is **neanche** or **nemmeno**: *Non lo so neanch'io* (I don't know either).

:::examples
- Mi piace il tè, ma mi piace anche il caffè. — I like tea, but I like coffee too.
- Il film è lungo, inoltre è noioso. — The film is long; besides, it's boring.
- È in ritardo, e in più ha dimenticato le chiavi. — He's late, and on top of that he forgot the keys.
:::
""",
        ["conn-addition"],
        explains=["conn-addition"],
    ),
    page(
        "it-sequence-connectives",
        "Prima, poi and infine",
        r"""
Sequence connectives put events in order: first this, then that, and finally the last thing.

| Italian | English |
| --- | --- |
| prima | first, before |
| poi | then |
| dopo | afterwards, later |
| in seguito | subsequently |
| infine | finally, lastly |
| alla fine | in the end |
| finalmente | at last |

A story often runs *prima*, then *poi*, then *infine*: *Prima mangiamo, poi andiamo al cinema, infine torniamo a casa.*

## Infine, alla fine or finalmente?

- **Infine** brings in the last step of a list.
- **Alla fine** says how things turned out, often not as planned: *Abbiamo discusso a lungo, e alla fine siamo rimasti a casa.*
- **Finalmente** means "at last", after a wait: *Finalmente siamo arrivati!* It never introduces the last point of a list. That's the classic mistake.

## Prima di, dopo

*Prima* and *dopo* also work as prepositions. Before a noun or a verb, *prima* takes **di**: *prima di cena*, *prima di uscire*. *Dopo* usually takes nothing: *dopo cena*, *dopo la lezione*.

:::examples
- Prima mangiamo, poi usciamo. — First we eat, then we go out.
- Apre la porta, poi entra. — He opens the door, then he goes in.
- Finalmente siamo arrivati! — At last, we're here!
:::
""",
        ["conn-sequence"],
        explains=["conn-sequence"],
    ),
]

NOUNS = nouns(
    """
finestra | f | window | home | finestre | Puoi aprire la finestra? | Can you open the window?
gatto | m | cat | animals | gatti | Il gatto dorme sul divano. | The cat is sleeping on the sofa.
cane | m | dog | animals | cani | Il mio cane ama giocare fuori. | My dog loves playing outside.
casa | f | house; home | home | case | La loro casa è vicino al mare. | Their house is near the sea.
libro | m | book | objects | libri | Leggo un libro la sera. | I read a book in the evening.
acqua | f | water | food | | Vorrei un bicchiere d'acqua. | I'd like a glass of water.
pane | m | bread | food | | Il pane è ancora caldo. | The bread is still warm.
tavolo | m | table | home | tavoli | Le chiavi sono sul tavolo. | The keys are on the table.
sedia | f | chair | home | sedie | Prendi una sedia e siediti. | Take a chair and sit down.
porta | f | door | home | porte | Qualcuno bussa alla porta. | Someone is knocking at the door.
macchina | f | car | transport | macchine | La mia macchina è dal meccanico. | My car is at the mechanic's.
albero | m | tree | nature | alberi | Quest'albero ha cento anni. | This tree is a hundred years old.
sole | m | sun | nature | | Oggi c'è il sole. | It's sunny today.
notte | f | night | time | notti | Di notte fa freddo. | It's cold at night.
amico | m | friend (male) | people | amici | È il mio migliore amico. | He's my best friend.
bambino | m | child; little boy | people | bambini | Il bambino gioca con la palla. | The child is playing with the ball.
"""
)

VERBS = [
    verb("mangiare", "to eat", ["food"], pp="mangiato",
         example="Mangiamo a mezzogiorno.", example_en="We eat at noon."),
    verb("bere", "to drink", ["food"], pp="bevuto",
         present="bevo bevi beve beviamo bevete bevono", imp="beve", fut="berr",
         subj="beva beva beva beviamo beviate bevano",
         example="Bevi un caffè la mattina?", example_en="Do you have a coffee in the morning?"),
    verb("parlare", "to speak, to talk", [], pp="parlato",
         example="Lei parla tre lingue.", example_en="She speaks three languages."),
    verb("andare", "to go", [], aux="essere", pp="andato",
         present="vado vai va andiamo andate vanno", fut="andr",
         subj="vada vada vada andiamo andiate vadano",
         example="Domani vado al mare.", example_en="Tomorrow I'm going to the seaside."),
]

CONNECTIVES = connectors(
    "connective",
    """
però | but, however | conn-contrast | Piove, però usciamo lo stesso. | It's raining, but we're going out anyway.
infatti | indeed, and in fact | conn-cause | Sono stanco; infatti stanotte non ho dormito. | I'm tired; in fact, I didn't sleep last night.
inoltre | moreover, besides | conn-addition | Il film è lungo, inoltre è noioso. | The film is long; besides, it's boring.
poi | then | conn-sequence | Prima mangiamo, poi usciamo. | First we eat, then we go out.
""",
    ["connettivi"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
ma | but | conj-coordinating | Voglio venire, ma non ho tempo. | I want to come, but I don't have time.
quindi | so, therefore | conj-coordinating | Fa freddo, quindi metto il cappotto. | It's cold, so I'm putting my coat on.
perché | because | conj-subordinating | Resto a casa perché sono stanco. | I'm staying home because I'm tired.
benché | although | conj-subordinating | Benché sia tardi, resto ancora un po'. | Although it's late, I'm staying a little longer.
""",
    ["congiunzioni"],
)

ITEMS = [ARTICLES] + NOUNS + VERBS + CONNECTIVES + CONJUNCTIONS + CORE_PAGES

CORE = pack("it-core-v1", 1, "it", "Italiano · L'essenziale", ITEMS, DELTA)

PACKS = [CORE, it_foundations.PACK, it_everyday.PACK, it_fluency.PACK]
