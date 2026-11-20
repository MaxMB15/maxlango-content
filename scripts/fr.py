"""French Base Packs, in curriculum order."""

import fr_everyday
import fr_fluency
import fr_foundations
from common import page
from core_patch import patch_core
from fr_conj import agreement_alternatives, conjugate

ARTICLES = page(
    "fr-articles-gender",
    "Le, la, un and une",
    r"""
Every French noun is **masculine** or **feminine**, and the article shows which.

| | masculine | feminine | plural |
| --- | --- | --- | --- |
| the | le chat | la fenêtre | les chats, les fenêtres |
| a, an, some | un chat | une fenêtre | des chats, des fenêtres |

- **Le** and **la** become **l'** before a vowel or a silent h: *l'ami*, *l'eau*, *l'hôtel*.
- **Les** and **des** are the same for both genders, so only the singular shows a noun's gender.
- French uses the article far more than English. A general statement takes *le*, *la* or *les*: *J'aime le café* (I like coffee).

:::examples
- Le chat dort sur la chaise. — The cat is sleeping on the chair.
- La fenêtre est ouverte. — The window is open.
- L'eau est fraîche ce matin. — The water is cool this morning.
- J'ai un chien et une voiture. — I have a dog and a car.
:::

So learn every noun with its article: **le chat**, **la fenêtre**, never the noun alone. When the article is *l'*, learn the gender too: *l'eau* is feminine, *l'arbre* masculine.
""",
    ["articles", "genre"],
    "fr-articles",
    explains=["articles"],
)
# The session's Reading card shows these plain sentences and cloze lines,
# and leaves out the :::examples block the page itself shows.
ARTICLES["extras"] = {
    "examples": ["Le chat dort sur la chaise.", "La fenêtre est ouverte.", "L'eau est fraîche ce matin."],
    "cloze": [{"sentence": "___ chat mange.", "blank": "Le"}, {"sentence": "___ fenêtre est grande.", "blank": "La"}],
    **ARTICLES["extras"],
}

# Upserted into the committed core pack. Every page after ARTICLES only
# explains a Tag: it unlocks nothing, so no session pushes it as Reading, and
# it opens when the learner taps one of its Tags.
CORE_PAGES = [
    ARTICLES,
    page(
        "fr-plural",
        "Plurals: -s, -x and -aux",
        r"""
Most French nouns add **-s** in the plural, and the article becomes **les** or **des**: *le chat*, *les chats*; *une maison*, *des maisons*.

The -s is silent, so *chat* and *chats* sound the same. You hear the plural in the article, and in the liaison before a vowel: *les amis* sounds like "lay-zah-mee".

## Other endings

| Singular ends in | Plural | Example |
| --- | --- | --- |
| -s, -x, -z | no change | le bras, les bras; la voix, les voix |
| -eau | add -x | le bateau, les bateaux |
| -au, -eu | usually add -x | le jeu, les jeux, but le pneu, les pneus |
| -al | -aux | le journal, les journaux; le cheval, les chevaux |
| -ail | usually add -s | le détail, les détails, but le travail, les travaux |
| -ou | usually add -s | le trou, les trous |

Seven nouns in -ou take **-x** instead: *bijou*, *caillou*, *chou*, *genou*, *hibou*, *joujou* and *pou*. A few in -al just add -s: *le festival*, *les festivals*.

## Irregular plurals

- *l'œil* (eye), *les yeux*
- *monsieur*, *messieurs*; *madame*, *mesdames*

Adjectives follow the same patterns: *un livre intéressant*, *des livres intéressants*; *un journal national*, *des journaux nationaux*.

:::examples
- J'ai deux chats et un chien. — I have two cats and a dog.
- Les journaux sont sur la table. — The newspapers are on the table.
- Elle a les yeux bleus. — She has blue eyes.
- Les bateaux arrivent ce soir. — The boats arrive this evening.
:::
""",
        ["pluriel"],
        explains=["pluriel"],
    ),
    page(
        "fr-coordinating-conjunctions",
        "Mais, ou, et, donc, or, ni and car",
        r"""
French schoolchildren learn the coordinating conjunctions as a question: *Mais où est donc Ornicar ?* It hides **mais** (but), **ou** (or), **et** (and), **donc** (so), **or** (now, yet), **ni** (nor) and **car** (because, for).

They join two words, or two clauses of the same kind, and leave both as they are.

:::examples
- J'ai un frère et une sœur. — I have a brother and a sister.
- Tu veux du thé ou du café ? — Do you want tea or coffee?
- Je veux venir, mais je n'ai pas le temps. — I want to come, but I don't have time.
- Il fait froid, donc je porte un manteau. — It's cold, so I'm wearing a coat.
:::

## Car or parce que?

Both mean "because". **Parce que** is the everyday word, and it starts a subordinate clause. **Car** belongs to writing and careful speech. It comes after a comma and never starts a sentence: *Je reste ici, car il pleut.*

## Ni

**Ni** needs **ne** before the verb, and usually comes twice: *Je ne bois ni thé ni café.* (I drink neither tea nor coffee.)

## Or

**Or** brings in a fact that changes the argument, often one that gets in the way: *Il devait venir, or il n'est pas venu.* (He was supposed to come, yet he didn't.) It belongs to formal French.
""",
        ["conj-coordinating"],
        explains=["conj-coordinating"],
    ),
    page(
        "fr-subordinating-conjunctions",
        "Que, quand, si and parce que",
        r"""
A subordinating conjunction starts a clause that depends on the main clause: *Je reste ici **parce que** je suis fatigué.* The word order inside that clause stays as it is. What some conjunctions change is the mood of its verb.

| French | English |
| --- | --- |
| que | that |
| quand, lorsque | when |
| si | if |
| parce que | because |
| comme | as, since (at the start of the sentence) |
| puisque | since (a reason both sides know) |
| pendant que | while |
| bien que | although |
| pour que | so that |

## Que stays

English can leave out *that*. French can't leave out *que*: *Je pense **qu'**il vient.* (I think he's coming.)

## Some take the subjunctive

**Bien que**, **pour que**, **avant que**, **à moins que** and **sans que** take the subjunctive: *Bien que tu **sois** jeune, tu comprends vite.* Most others, *parce que*, *quand* and *si* among them, take the indicative.

## Si and quand

- When **si** means "if", the verb after it is never in the future or the conditional: *Si tu viens, je serai content.* When it means "whether", the future is fine: *Je ne sais pas s'il viendra.*
- After **quand**, French puts a future time in the future tense, where English uses the present: *Quand tu arriveras, appelle-moi.* (When you arrive, call me.)

:::examples
- Je pense qu'il va pleuvoir. — I think it's going to rain.
- Je lis quand il pleut. — I read when it rains.
- On sort si tu veux. — We'll go out if you want.
- Je reste ici parce que je suis fatigué. — I'm staying here because I'm tired.
:::
""",
        ["conj-subordinating"],
        explains=["conj-subordinating"],
    ),
    page(
        "fr-contrast-connectives",
        "Cependant and pourtant",
        r"""
A contrast connective says that what comes next goes against what came before, or against what you'd expect.

| French | English |
| --- | --- |
| cependant | however |
| pourtant | yet, and yet |
| en revanche | on the other hand |
| néanmoins | nevertheless |
| toutefois | however (formal) |
| au contraire | on the contrary |

At the start of a clause they usually take a comma, and the word order stays as it is: *Pourtant, il n'est pas heureux.* Most can also sit after the verb: *Il n'est **pourtant** pas heureux.*

## Which one?

- **Pourtant** carries surprise, something true against what you'd expect: *Il est riche ; pourtant, il n'est pas heureux.*
- **Cependant** is a plainer "however". *Toutefois* and *néanmoins* say the same more formally.
- **En revanche** sets two facts side by side: *Le logement est cher ; en revanche, la nourriture est bon marché.*
- **Au contraire** follows a negative and says the opposite is true: *Il n'est pas timide ; au contraire, il parle à tout le monde.*

## Mais and bien que

**Mais** (but) is the everyday way to set up a contrast: *Je veux venir, mais je n'ai pas le temps.* **Bien que** (although) starts a subordinate clause and takes the subjunctive: *Bien qu'il **soit** riche, il n'est pas heureux.*

:::examples
- Il pleut, cependant nous sortons. — It's raining; however, we're going out.
- Il est riche ; pourtant, il n'est pas heureux. — He's rich, and yet he isn't happy.
- C'est difficile ; néanmoins, c'est possible. — It's difficult; nevertheless, it's possible.
:::
""",
        ["conn-contrast"],
        explains=["conn-contrast"],
    ),
    page(
        "fr-cause-connectives",
        "En effet and en fait",
        r"""
A cause connective gives the reason for what was just said.

| French | English |
| --- | --- |
| en effet | indeed, as it happens |
| en fait | in fact, actually |

**En effet** backs up what you just said with its reason: *Je reste à la maison ; en effet, je suis malade.* It doesn't mean "in effect". **En fait** brings in what is really the case, often to correct an impression: *Je ne viens pas ; en fait, je suis malade.*

## Parce que, car, puisque and comme

- **Parce que** is the everyday "because": *Je reste ici parce que je suis fatigué.*
- **Car** says the same in writing, after a comma, and never starts a sentence: *Je reste ici, car il pleut.*
- **Puisque** gives a reason the listener already knows: *Puisque tu es là, aide-moi.*
- **Comme** puts the reason first, at the start of the sentence: *Comme il pleut, on reste ici.*

:::examples
- Je reste à la maison, en effet je suis malade. — I'm staying at home; I'm ill, you see.
- Je ne viens pas ; en fait, je suis malade. — I'm not coming; actually, I'm ill.
- Puisque tu es là, aide-moi. — Since you're here, help me.
:::
""",
        ["conn-cause"],
        explains=["conn-cause"],
    ),
    page(
        "fr-addition-connectives",
        "Aussi and en plus",
        r"""
An addition connective adds one more point to what was said.

| French | English |
| --- | --- |
| aussi | also, too |
| en plus | on top of that |
| de plus | moreover |
| d'ailleurs | besides, what's more |
| en outre | furthermore |

*En plus* is the everyday one, *de plus* suits writing, and *en outre* is formal.

At the start of a clause they take a comma and change nothing else: *De plus, il est ennuyeux.* **Aussi** is the exception. For "also", it goes after the verb: *J'aime aussi le café.* At the start of a sentence, in formal writing, *aussi* means "so".

## D'ailleurs

*D'ailleurs* adds a point that backs up what you said, often one that settles it: *Je n'ai pas faim ; d'ailleurs, j'ai déjà mangé.*

:::examples
- J'aime le thé. J'aime aussi le café. — I like tea. I also like coffee.
- Le film est long, de plus il est ennuyeux. — The film is long; moreover, it's boring.
- Il est en retard, et en plus il a oublié les clés. — He's late, and on top of that he forgot the keys.
:::
""",
        ["conn-addition"],
        explains=["conn-addition"],
    ),
    page(
        "fr-sequence-connectives",
        "D'abord, ensuite and enfin",
        r"""
Sequence connectives put events in order: first this, then that, and finally the last thing.

| French | English |
| --- | --- |
| d'abord | first, first of all |
| ensuite | then, next |
| puis | then |
| après | afterwards |
| enfin | finally, at last |
| finalement | in the end |

A story often runs *d'abord*, then *ensuite* or *puis*, then *enfin*: *D'abord, on mange ; ensuite, on va au cinéma ; enfin, on rentre.*

## Enfin or finalement?

- **Enfin** brings in the last step of a list, or says "at last" after a wait: *Enfin, nous sommes arrivés !*
- **Finalement** says how things turned out, often not as planned: *On a beaucoup hésité, et finalement on est restés.*

## Après

*Après* is also a preposition: *après le dîner* (after dinner). On its own at the end of a clause it means "afterwards": *On mange d'abord, et on sort après.*

:::examples
- D'abord, on mange ; après, on sort. — First we eat; then we go out.
- Il ouvre la porte, puis il entre. — He opens the door, then he goes in.
- Nous mangeons, ensuite nous partons. — We eat, then we leave.
- Enfin, nous sommes arrivés. — At last, we arrived.
:::
""",
        ["conn-sequence"],
        explains=["conn-sequence"],
    ),
]

CORE = patch_core(
    "fr",
    7,
    {
        "manger": (conjugate("manger", pp="mangé"), {"auxiliary": "avoir", "participle": "mangé"}),
        "boire": (
            conjugate("boire", pp="bu", present="bois bois boit buvons buvez boivent"),
            {"auxiliary": "avoir", "participle": "bu"},
        ),
        "parler": (conjugate("parler", pp="parlé"), {"auxiliary": "avoir", "participle": "parlé"}),
        "aller": (
            conjugate(
                "aller",
                pp="allé",
                aux="être",
                present="vais vas va allons allez vont",
                fut="ir",
                subj="aille ailles aille allions alliez aillent",
            ),
            {"auxiliary": "être", "participle": "allé", "agreement": agreement_alternatives("allé")},
        ),
    },
    pages=CORE_PAGES,
)

PACKS = [CORE, fr_foundations.PACK, fr_everyday.PACK, fr_fluency.PACK]
