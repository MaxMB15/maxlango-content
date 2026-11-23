"""fr-foundations-v1: A1. The grammar that blocks a beginner first, and the words
needed to talk about yourself, your family, your day and your food."""

from common import build_units, interleave, page, pack, topic, topic_labels
from fr_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("prononciation", "Prononciation", "pronunciation", []),
    topic("pronoms", "Pronoms", "pronouns", ["présent"]),
    topic("questions", "Questions", "asking questions", ["présent"]),
    topic("partitif", "Partitif", "partitive articles", ["articles"]),
    topic("nombres", "Nombres", "numbers", []),
    topic("family", "Famille", "family", ["articles"]),
    topic("body", "Corps", "body", ["articles"]),
    topic("city", "Ville", "city and places", ["articles"]),
    topic("greetings", "Salutations", "greetings and politeness", []),
    topic("colors", "Couleurs", "colours", ["adjectifs"]),
]

PAGES = [
    page(
        "fr-pronunciation",
        "Reading French aloud",
        r"""
French spelling looks chaotic, but it's regular once you know what to ignore. Most of the work is learning which letters stay silent.

## Silent endings

A final **e**, **s**, **t**, **d**, **x** and **z** are usually silent. *[Petit](lango:say)*, *[grand](lango:say)*, *[les amis](lango:say)* and *[vous parlez](lango:say)* all end on a vowel sound.

A handy exception: final **c**, **r**, **f** and **l** are often pronounced. Think of the English word *CaReFuL*: *[parc](lango:say)*, *[bonjour](lango:say)*, *[neuf](lango:say)*, *[sel](lango:say)*. The **-er** of an infinitive is the big exception to the exception: *[parler](lango:say)* ends in "é".

## Nasal vowels

When a vowel sits before **n** or **m** in the same syllable, the n is not pronounced. Air goes through the nose instead.

| Spelling | Sound | Example |
| --- | --- | --- |
| an, en, am, em | "ahn" | *[enfant](lango:say)*, *[temps](lango:say)* |
| on, om | "ohn" | *[bon](lango:say)*, *[nom](lango:say)* |
| in, ain, ein, un | "ahn" (front) | *[vin](lango:say)*, *[pain](lango:say)*, *[un](lango:say)* |

If a vowel follows the n (*[bonne](lango:say)*, *[une](lango:say)*), the nasal disappears and the n is pronounced.

## Liaison and elision

**Liaison**: a silent final consonant is pronounced when the next word starts with a vowel. *[Les amis](lango:say)* sounds like "lé-z-ami". *[Vous avez](lango:say)* sounds like "vou-z-avé".

**Elision**: short words drop their vowel before another vowel and take an apostrophe. *Le ami* becomes *[l'ami](lango:say)*, *je aime* becomes *[j'aime](lango:say)*, *ne est* becomes *[n'est](lango:say)*.

## Accents

- **é** (accent aigu) is a closed "ay": *[été](lango:say)*.
- **è** and **ê** are an open "eh": *[mère](lango:say)*, *[fête](lango:say)*.
- **ç** makes c soft before a, o, u: *[ça](lango:say)*, *[garçon](lango:say)*.
- **à**, **ù**, **â**, **î**, **ô**, **û** don't change the sound much. They tell words apart: *[a](lango:say)* (has) and *[à](lango:say)* (to), *[ou](lango:say)* (or) and *[où](lango:say)* (where).
""",
        ["prononciation"],
        "fr-pronunciation",
        explains=["prononciation"],
    ),
    page(
        "fr-subject-pronouns",
        "Je, tu, vous and on",
        r"""
French has two words for "you", and choosing one is a social decision you make in every sentence.

| Person | Pronoun | English |
| --- | --- | --- |
| 1st singular | je (j') | I |
| 2nd singular | tu | you (one person, familiar) |
| 3rd singular | il / elle / on | he / she / one, we |
| 1st plural | nous | we |
| 2nd plural | vous | you (plural, or polite) |
| 3rd plural | ils / elles | they |

## Tu or vous?

Use **tu** with friends, family, children, animals and people your own age in casual settings. Use **vous** with strangers, shop staff, colleagues you don't know well, and anyone older or senior. When in doubt, say *vous*. Switching to tu is usually offered: *On peut se tutoyer ?* (Shall we say tu?)

**Vous** is also the only plural "you", so a group of friends is *vous* too.

## Ils or elles?

*Elles* is only for groups that are entirely feminine. One masculine member makes the group *ils*.

## On

*On* is grammatically "one", like "one never knows". In speech it almost always means **we**: *On va au cinéma ?* (Shall we go to the cinema?) It takes the il/elle form of the verb.

:::examples
- Tu parles français ? — Do you speak French? (to a friend)
- Vous parlez français ? — Do you speak French? (polite, or to several people)
- On mange à huit heures. — We eat at eight.
:::
""",
        ["pronoms"],
        "fr-subject-pronouns",
        explains=["pronoms"],
    ),
    page(
        "fr-etre-avoir",
        "Être and avoir",
        r"""
**Être** (to be) and **avoir** (to have) are the two most important verbs in French. Both are irregular, and both are also the helper verbs of the past tense, so you'll use them constantly.

| | être | avoir |
| --- | --- | --- |
| je | suis | ai (j'ai) |
| tu | es | as |
| il / elle / on | est | a |
| nous | sommes | avons |
| vous | êtes | avez |
| ils / elles | sont | ont |

## Where French says "have" and English says "be"

French describes many states as things you *have*. This is one of the first real differences from English.

| French | Literally | English |
| --- | --- | --- |
| j'ai faim | I have hunger | I'm hungry |
| j'ai soif | I have thirst | I'm thirsty |
| j'ai chaud / froid | I have heat / cold | I'm hot / cold |
| j'ai peur | I have fear | I'm scared |
| j'ai raison / tort | I have reason / wrong | I'm right / wrong |
| j'ai vingt ans | I have twenty years | I'm twenty |
| j'ai besoin de... | I have need of | I need... |
| j'ai envie de... | I have desire of | I feel like... |

Saying *je suis vingt* for your age is the classic beginner mistake. It means nothing.

## C'est or il est?

Use **c'est** before a noun with an article: *C'est un médecin*, *C'est mon frère*. Use **il est / elle est** before a bare adjective or profession: *Il est médecin*, *Elle est grande*.

:::cloze{sentence="J'___ faim, on mange ?" blank="ai"}
:::
""",
        ["présent"],
        "fr-etre-avoir",
    ),
    page(
        "fr-present-tense",
        "The present tense: three families",
        r"""
French verbs are grouped by their infinitive ending. Learn the three regular patterns and you can conjugate thousands of verbs.

## -er verbs (parler)

About 90% of French verbs. Remove **-er** and add **-e, -es, -e, -ons, -ez, -ent**. The je, tu, il and ils forms all sound the same.

## -ir verbs (finir)

Remove **-ir** and add **-is, -is, -it, -issons, -issez, -issent**. The plural adds **-iss-**. Some -ir verbs (partir, dormir, sortir) don't follow this and are learned separately.

## -re verbs (vendre)

Remove **-re** and add **-s, -s, (nothing), -ons, -ez, -ent**. *Il vend*, with no ending.

| | parler | finir | vendre |
| --- | --- | --- | --- |
| je | parle | finis | vends |
| tu | parles | finis | vends |
| il | parle | finit | vend |
| nous | parlons | finissons | vendons |
| vous | parlez | finissez | vendez |
| ils | parlent | finissent | vendent |

:::examples
- Je parle français et anglais. — I speak French and English.
- Nous finissons à six heures. — We finish at six.
- Il vend sa voiture. — He's selling his car.
- Tu manges avec nous ce soir ? — Are you eating with us tonight?
:::

## Spelling changes that keep the sound

- Verbs in **-ger** keep an **e** before -ons: *nous mangeons*.
- Verbs in **-cer** take **ç** before -ons: *nous commençons*.
- Some verbs change their stem vowel when the ending is silent: *acheter → j'achète*, *appeler → j'appelle*, *préférer → je préfère*. The nous and vous forms keep the infinitive's spelling.

## One tense for three English ones

*Je mange* is "I eat", "I am eating" and "I do eat". French has no continuous tense. To stress that something is happening right now, say *je suis en train de manger*.

:::predict{prompt="nous (nager)" answer="nageons"}
:::
""",
        ["présent"],
        "fr-present-tense",
        explains=["présent"],
    ),
    page(
        "fr-negation",
        "Saying no: ne ... pas",
        r"""
French negation has two parts that wrap around the verb: **ne** before it and **pas** after it.

:::examples
- Je ne parle pas allemand. — I don't speak German.
- Il n'est pas là. — He isn't here.
- Nous ne mangeons pas de viande. — We don't eat meat.
:::

*Ne* becomes *n'* before a vowel.

## Other negations

Swap *pas* for another word to change the meaning:

| Negation | Meaning | Example |
| --- | --- | --- |
| ne ... jamais | never | Je ne bois jamais de café. |
| ne ... plus | no longer | Il n'habite plus ici. |
| ne ... rien | nothing | Je ne vois rien. |
| ne ... personne | nobody | Je ne connais personne. |
| ne ... que | only | Je n'ai que deux euros. |

## Pas de

After a negation, **un, une, du, de la** and **des** all become **de** (or **d'**).

*J'ai une voiture* → *Je n'ai pas de voiture.*
*Je bois du café* → *Je ne bois pas de café.*

This doesn't apply to *être*: *C'est un chat* → *Ce n'est pas un chat.*

## In conversation

Spoken French usually drops the *ne*. *Je sais pas*, *C'est pas grave*, *J'ai pas le temps*. Write the *ne*, but expect not to hear it.

:::cloze{sentence="Je n'ai pas ___ frères." blank="de"}
:::
""",
        ["négation"],
        "fr-negation",
        explains=["négation"],
    ),
    page(
        "fr-questions",
        "Asking questions",
        r"""
French has three ways to ask a yes/no question. They mean the same thing and differ in register.

| Register | How | Example |
| --- | --- | --- |
| Casual | raise your voice at the end | Tu viens ? |
| Neutral | put **est-ce que** in front | Est-ce que tu viens ? |
| Formal | swap subject and verb, add a hyphen | Viens-tu ? |

With inversion, a **-t-** is inserted between two vowels so it's easier to say: *Parle-t-il français ?*, *A-t-elle faim ?*

## Question words

| Word | Meaning |
| --- | --- |
| qui | who |
| que / quoi | what |
| où | where |
| quand | when |
| comment | how |
| pourquoi | why |
| combien (de) | how much, how many |
| quel, quelle, quels, quelles | which, what (agrees with the noun) |

In speech the question word often goes last: *Tu vas où ?*, *Il arrive quand ?*, *C'est quoi ?*

:::examples
- Où est-ce que tu habites ? — Where do you live?
- Comment tu t'appelles ? — What's your name?
- Quelle heure est-il ? — What time is it?
- Pourquoi est-ce qu'il pleure ? — Why is he crying?
:::
""",
        ["questions"],
        "fr-questions",
        explains=["questions"],
    ),
    page(
        "fr-partitive",
        "Some bread: du, de la, des",
        r"""
English often says nothing before a noun (*I eat bread*) or says "some". French can't leave the noun bare. It uses the **partitive article** for an unspecified amount.

| | Article | Example |
| --- | --- | --- |
| masculine | du | du pain |
| feminine | de la | de la confiture |
| before a vowel | de l' | de l'eau |
| plural | des | des pommes |

## Partitive or definite?

- **Le, la, les** talk about the thing in general, and follow verbs of liking: *J'aime le café* (I like coffee).
- **Du, de la** talk about some of it: *Je bois du café* (I drink coffee).

## Quantities

After a word of quantity the article becomes plain **de**: *beaucoup de café*, *un peu de sucre*, *un kilo de pommes*, *une bouteille d'eau*, *assez de temps*.

After a negation too: *Je ne veux pas de sucre.*

:::cloze{sentence="Tu veux ___ eau ?" blank="de l'"}
:::
""",
        ["partitif"],
        "fr-partitive",
        explains=["partitif"],
    ),
    page(
        "fr-contractions",
        "Au, aux, du, des",
        r"""
The prepositions **à** (to, at) and **de** (of, from) merge with *le* and *les*. They never merge with *la* or *l'*.

| | + le | + la | + l' | + les |
| --- | --- | --- | --- | --- |
| à | **au** | à la | à l' | **aux** |
| de | **du** | de la | de l' | **des** |

:::examples
- Je vais au cinéma. — I'm going to the cinema.
- Elle est à la plage. — She's at the beach.
- Il parle aux enfants. — He talks to the children.
- Je viens du Canada. — I come from Canada.
- C'est la voiture des voisins. — It's the neighbours' car.
:::

## Countries and cities

Cities take **à**: *à Paris*. Feminine countries (most end in -e) take **en**: *en France*, *en Belgique*. Masculine countries take **au**: *au Canada*, *au Japon*. Plural ones take **aux**: *aux États-Unis*.
""",
        ["articles"],
        "fr-contractions",
    ),
    page(
        "fr-adjectives",
        "Adjectives: agreement and position",
        r"""
French adjectives agree with their noun in gender and number, and most go **after** the noun.

## Agreement

Start from the masculine singular. Add **-e** for feminine and **-s** for plural.

| | singular | plural |
| --- | --- | --- |
| masculine | petit | petits |
| feminine | petite | petites |

Common irregular patterns:

| masculine | feminine | example |
| --- | --- | --- |
| -e | -e (no change) | rouge, rouge |
| -eux | -euse | heureux, heureuse |
| -if | -ive | sportif, sportive |
| -el, -en, -on | -elle, -enne, -onne | bon, bonne |
| -er | -ère | cher, chère |

## Position: BAGS

Most adjectives follow the noun: *une voiture rouge*, *un film intéressant*. A short list goes **before**, remembered as **BAGS**:

- **B**eauty: beau, joli
- **A**ge: jeune, vieux, nouveau
- **G**ood and bad: bon, mauvais, gentil
- **S**ize: grand, petit, gros, long

*Un petit chat*, *une belle maison*, *un bon repas*.

:::examples
- J'ai acheté une voiture rouge. — I bought a red car.
- C'est un petit village. — It's a small village.
- Ces chaussures sont trop chères. — These shoes are too expensive.
- Nous avons visité une belle maison ancienne. — We visited a beautiful old house.
:::

## Beau, nouveau, vieux

Before a masculine noun starting with a vowel, these take a special form: *un bel homme*, *un nouvel ami*, *un vieil arbre*.

## Meaning changes with position

A few adjectives mean different things before and after:

- *un ancien professeur* (a former teacher) / *une maison ancienne* (an old house)
- *mon cher ami* (my dear friend) / *un restaurant cher* (an expensive restaurant)
- *la dernière semaine* (the final week) / *la semaine dernière* (last week)
- *ma propre chambre* (my own room) / *une chambre propre* (a clean room)
""",
        ["adjectifs"],
        "fr-adjectives",
        explains=["adjectifs"],
    ),
    page(
        "fr-numbers",
        "Numbers, and counting in twenties",
        r"""
French numbers are regular up to 69. Then they switch to counting in twenties, a leftover from an older system.

| | | | |
| --- | --- | --- | --- |
| 1 un | 6 six | 11 onze | 16 seize |
| 2 deux | 7 sept | 12 douze | 17 dix-sept |
| 3 trois | 8 huit | 13 treize | 18 dix-huit |
| 4 quatre | 9 neuf | 14 quatorze | 19 dix-neuf |
| 5 cinq | 10 dix | 15 quinze | 20 vingt |

Tens: 30 trente, 40 quarante, 50 cinquante, 60 soixante.

The ones in 21, 31, 41, 51, 61 take **et**: *vingt et un*. The others take a hyphen: *vingt-deux*.

## 70 to 99

| Number | French | Literally |
| --- | --- | --- |
| 70 | soixante-dix | sixty-ten |
| 71 | soixante et onze | sixty and eleven |
| 75 | soixante-quinze | sixty-fifteen |
| 80 | quatre-vingts | four twenties |
| 81 | quatre-vingt-un | four-twenty-one |
| 90 | quatre-vingt-dix | four-twenty-ten |
| 97 | quatre-vingt-dix-sept | four-twenty-ten-seven |

Belgium and Switzerland use *septante* (70) and *nonante* (90). Switzerland often says *huitante* for 80.

100 is *cent*, 1000 is *mille* (never *un mille*). A year like 2026 is *deux mille vingt-six*.

:::examples
- J'ai quatre-vingt-deux ans. — I'm eighty-two.
- Ça fait soixante-quinze euros. — That's seventy-five euros.
:::
""",
        ["nombres"],
        "fr-numbers",
        explains=["nombres"],
    ),
    page(
        "fr-near-future",
        "Going to, and just did",
        r"""
Two everyday constructions let you talk about the near future and the recent past with only the present tense.

## Aller + infinitive: the near future

Just like English "going to": conjugate *aller* and add the infinitive.

:::examples
- Je vais manger. — I'm going to eat.
- On va voir un film ce soir. — We're going to see a film tonight.
- Il va pleuvoir. — It's going to rain.
:::

This is how most people talk about the future in everyday French. The *futur simple* comes later, and sounds more planned or formal.

## Venir de + infinitive: the recent past

Conjugate *venir*, add **de**, then the infinitive. It means "to have just done".

:::examples
- Je viens de manger. — I've just eaten.
- Elle vient d'arriver. — She's just arrived.
:::

Careful: *je viens manger* without *de* means "I'm coming to eat".
""",
        ["présent"],
        "fr-near-future",
    ),
    page(
        "fr-possessives",
        "Mon, ma, mes: possessives",
        r"""
A French possessive agrees with the **thing owned**, not with the owner. *Son* and *sa* both mean "his" and "her"; the choice depends on the noun that follows.

| Owner | masculine | feminine | plural |
| --- | --- | --- | --- |
| je | mon | ma | mes |
| tu | ton | ta | tes |
| il / elle | son | sa | ses |
| nous | notre | notre | nos |
| vous | votre | votre | vos |
| ils / elles | leur | leur | leurs |

:::examples
- Pierre aime sa mère. — Pierre loves his mother.
- Marie aime son père. — Marie loves her father.
- C'est leur maison. — It's their house.
:::

## Mon before a vowel

Before a feminine word starting with a vowel, **ma, ta, sa** become **mon, ton, son** so the words don't collide: *mon amie*, *son école*, *ton histoire*.
""",
        ["pronoms"],
        "fr-possessives",
    ),
]

NOUNS = nouns(
    """
# family and people
père | m | father | family
mère | f | mother | family
frère | m | brother | family
sœur | f | sister | family
fils | m | son | family | fils
fille | f | daughter; girl | family
mari | m | husband | family
femme | f | wife; woman | family
parent | m | parent | family
grand-père | m | grandfather | family | grands-pères
grand-mère | f | grandmother | family | grands-mères
oncle | m | uncle | family
tante | f | aunt | family
cousin | m | cousin (male) | family
cousine | f | cousin (female) | family
homme | m | man | people
garçon | m | boy | people
bébé | m | baby | people
voisin | m | neighbour | people
nom | m | name; surname | people
prénom | m | first name | people
# body
tête | f | head | body
œil | m | eye | body | yeux
bouche | f | mouth | body
nez | m | nose | body | nez
oreille | f | ear | body
main | f | hand | body
bras | m | arm | body | bras
jambe | f | leg | body
pied | m | foot | body
dos | m | back | body | dos
cœur | m | heart | body
ventre | m | belly, stomach | body
dent | f | tooth | body
# food
petit-déjeuner | m | breakfast | food | petits-déjeuners
déjeuner | m | lunch | food
dîner | m | dinner | food
fromage | m | cheese | food
viande | f | meat | food
poisson | m | fish (to eat) | food
poulet | m | chicken | food
œuf | m | egg | food
lait | m | milk | food
café | m | coffee; café | food
thé | m | tea | food
vin | m | wine | food
bière | f | beer | food
pomme | f | apple | food
pomme de terre | f | potato | food | pommes de terre
légume | m | vegetable | food
fruit | m | fruit | food
sucre | m | sugar | food
sel | m | salt | food
riz | m | rice | food
confiture | f | jam | food
gâteau | m | cake | food | gâteaux
# home
chambre | f | bedroom | home
cuisine | f | kitchen; cooking | home
salle de bains | f | bathroom | home | salles de bains
salon | m | living room | home
lit | m | bed | home
clé | f | key | home
appartement | m | flat, apartment | home
jardin | m | garden | home
# time and calendar
jour | m | day | time
semaine | f | week | time
mois | m | month | time | mois
an | m | year (counting: trois ans) | time
année | f | year (duration, a school year) | time
heure | f | hour; o'clock | time
minute | f | minute | time
matin | m | morning | time
soir | m | evening | time
lundi | m | Monday | time
mardi | m | Tuesday | time
mercredi | m | Wednesday | time
jeudi | m | Thursday | time
vendredi | m | Friday | time
samedi | m | Saturday | time
dimanche | m | Sunday | time
# city
ville | f | town, city | city
rue | f | street | city
magasin | m | shop | city
marché | m | market | city
boulangerie | f | bakery | city
gare | f | train station | city
école | f | school | city
église | f | church | city
banque | f | bank | city
hôpital | m | hospital | city | hôpitaux
restaurant | m | restaurant | city
travail | m | work, job | city | travaux
argent | m | money; silver | objects
téléphone | m | telephone | objects
"""
)

ADJECTIVES = adjectives(
    """
grand, grande, grands, grandes | big, tall | before
petit, petite, petits, petites | small, little | before
bon, bonne, bons, bonnes | good | before
mauvais, mauvaise, mauvais, mauvaises | bad | before
beau, belle, beaux, belles | beautiful, handsome | before
joli, jolie, jolis, jolies | pretty | before
jeune, jeune, jeunes, jeunes | young | before
vieux, vieille, vieux, vieilles | old | before
nouveau, nouvelle, nouveaux, nouvelles | new | before
gentil, gentille, gentils, gentilles | kind, nice | before
content, contente, contents, contentes | happy, pleased
fatigué, fatiguée, fatigués, fatiguées | tired
chaud, chaude, chauds, chaudes | hot, warm
froid, froide, froids, froides | cold
facile, facile, faciles, faciles | easy
difficile, difficile, difficiles, difficiles | difficult
cher, chère, chers, chères | expensive; dear
rouge, rouge, rouges, rouges | red
bleu, bleue, bleus, bleues | blue
vert, verte, verts, vertes | green
jaune, jaune, jaunes, jaunes | yellow
noir, noire, noirs, noires | black
blanc, blanche, blancs, blanches | white
gris, grise, gris, grises | grey
"""
)
for a in ADJECTIVES:
    if a["primary_form"] in {"rouge", "bleu", "vert", "jaune", "noir", "blanc", "gris"}:
        a["tags"].append("colors")

VERBS = [
    verb("être", "to be", [], aux="avoir", pp="été",
         present="suis es est sommes êtes sont", imp="ét", fut="ser",
         subj="sois sois soit soyons soyez soient",
         example="Je suis fatigué ce soir.", example_en="I'm tired tonight."),
    verb("avoir", "to have", [], pp="eu",
         present="ai as a avons avez ont", fut="aur",
         subj="aie aies ait ayons ayez aient",
         example="Tu as quel âge ?", example_en="How old are you?"),
    verb("faire", "to do, to make", [], pp="fait",
         present="fais fais fait faisons faites font", fut="fer",
         subj="fasse fasses fasse fassions fassiez fassent",
         example="Il fait beau aujourd'hui.", example_en="The weather's nice today."),
    verb("venir", "to come", [], aux="être", pp="venu",
         present="viens viens vient venons venez viennent", fut="viendr",
         example="Tu viens avec nous ?", example_en="Are you coming with us?"),
    verb("vouloir", "to want", [], pp="voulu",
         present="veux veux veut voulons voulez veulent", fut="voudr",
         subj="veuille veuilles veuille voulions vouliez veuillent",
         example="Je voudrais un café, s'il vous plaît.", example_en="I'd like a coffee, please."),
    verb("pouvoir", "to be able to, can", [], pp="pu",
         present="peux peux peut pouvons pouvez peuvent", fut="pourr",
         subj="puisse puisses puisse puissions puissiez puissent",
         example="Est-ce que je peux entrer ?", example_en="May I come in?"),
    verb("devoir", "to have to, must; to owe", [], pp="dû",
         present="dois dois doit devons devez doivent", fut="devr",
         example="Je dois partir.", example_en="I have to go."),
    verb("savoir", "to know (a fact, how to)", [], pp="su",
         present="sais sais sait savons savez savent", fut="saur",
         subj="sache saches sache sachions sachiez sachent",
         example="Je ne sais pas.", example_en="I don't know."),
    verb("prendre", "to take", [], pp="pris",
         present="prends prends prend prenons prenez prennent",
         example="Je prends le train.", example_en="I take the train."),
    verb("mettre", "to put; to put on", [], pp="mis",
         present="mets mets met mettons mettez mettent",
         example="Mets ton manteau !", example_en="Put your coat on!"),
    verb("dire", "to say, to tell", [], pp="dit",
         present="dis dis dit disons dites disent",
         example="Qu'est-ce que tu dis ?", example_en="What are you saying?"),
    verb("voir", "to see", [], pp="vu",
         present="vois vois voit voyons voyez voient", fut="verr",
         example="On se voit demain ?", example_en="See each other tomorrow?"),
    verb("habiter", "to live (somewhere)", ["home"], pp="habité",
         example="J'habite à Lyon.", example_en="I live in Lyon."),
    verb("aimer", "to like, to love", [], pp="aimé",
         example="J'aime le chocolat.", example_en="I like chocolate."),
    verb("travailler", "to work", [], pp="travaillé",
         example="Elle travaille à la banque.", example_en="She works at the bank."),
    verb("regarder", "to watch, to look at", [], pp="regardé",
         example="On regarde un film ?", example_en="Shall we watch a film?"),
    verb("écouter", "to listen (to)", [], pp="écouté",
         example="J'écoute de la musique.", example_en="I'm listening to music."),
    verb("jouer", "to play", [], pp="joué",
         example="Les enfants jouent dans le jardin.", example_en="The children are playing in the garden."),
    verb("chercher", "to look for", [], pp="cherché",
         example="Je cherche la gare.", example_en="I'm looking for the station."),
    verb("donner", "to give", [], pp="donné",
         example="Donne-moi la main.", example_en="Give me your hand."),
    verb("trouver", "to find", [], pp="trouvé",
         example="Je ne trouve pas mes clés.", example_en="I can't find my keys."),
    verb("penser", "to think", [], pp="pensé",
         example="Je pense que oui.", example_en="I think so."),
    verb("arriver", "to arrive; to happen", [], aux="être", pp="arrivé",
         example="Le train arrive à midi.", example_en="The train arrives at noon."),
    verb("commencer", "to begin, to start", [], pp="commencé",
         example="Le film commence à huit heures.", example_en="The film starts at eight."),
    verb("acheter", "to buy", ["food"], pp="acheté",
         present="achète achètes achète achetons achetez achètent", fut="achèter",
         example="J'achète du pain.", example_en="I'm buying bread."),
    verb("finir", "to finish", [], pp="fini",
         example="Je finis à cinq heures.", example_en="I finish at five."),
    verb("choisir", "to choose", [], pp="choisi",
         example="Tu choisis le vin ?", example_en="Will you choose the wine?"),
    verb("vendre", "to sell", [], pp="vendu",
         example="Il vend des fruits au marché.", example_en="He sells fruit at the market."),
    verb("attendre", "to wait (for)", [], pp="attendu",
         example="J'attends le bus.", example_en="I'm waiting for the bus."),
    verb("comprendre", "to understand", [], pp="compris",
         present="comprends comprends comprend comprenons comprenez comprennent",
         example="Je ne comprends pas.", example_en="I don't understand."),
    verb("apprendre", "to learn", [], pp="appris",
         present="apprends apprends apprend apprenons apprenez apprennent",
         example="J'apprends le français.", example_en="I'm learning French."),
    verb("partir", "to leave", [], aux="être", pp="parti",
         present="pars pars part partons partez partent",
         example="Nous partons demain.", example_en="We're leaving tomorrow."),
    verb("sortir", "to go out", [], aux="être", pp="sorti",
         present="sors sors sort sortons sortez sortent",
         example="On sort ce soir ?", example_en="Shall we go out tonight?"),
    verb("dormir", "to sleep", [], pp="dormi",
         present="dors dors dort dormons dormez dorment",
         example="Le bébé dort.", example_en="The baby is sleeping."),
    verb("lire", "to read", [], pp="lu",
         present="lis lis lit lisons lisez lisent",
         example="Je lis le journal.", example_en="I'm reading the newspaper."),
    verb("écrire", "to write", [], pp="écrit",
         present="écris écris écrit écrivons écrivez écrivent",
         example="J'écris une lettre.", example_en="I'm writing a letter."),
    verb("s'appeler", "to be called (name)", ["people"], pp="appelé", refl=True,
         present="appelle appelles appelle appelons appelez appellent", fut="appeller",
         example="Je m'appelle Julie.", example_en="My name is Julie."),
]

PHRASES = phrases(
    """
bonjour | hello, good morning | good day
bonsoir | good evening
salut | hi; bye (informal)
au revoir | goodbye | until the re-seeing
à bientôt | see you soon
à demain | see you tomorrow
bonne nuit | good night
merci | thank you
merci beaucoup | thank you very much
de rien | you're welcome | of nothing
je vous en prie | you're welcome (polite); please, go ahead | I pray you of it
s'il vous plaît | please (polite) | if it pleases you
s'il te plaît | please (informal) | if it pleases you
excusez-moi | excuse me (polite)
pardon | sorry; pardon?
désolé | sorry
oui | yes
non | no
si | yes (contradicting a negative question) | | Tu ne viens pas ? Si ! (You're not coming? Yes I am!)
d'accord | OK, agreed | of agreement
ça va ? | how are you? how's it going? | it goes?
ça va bien, merci | I'm fine, thanks | it goes well
comment allez-vous ? | how are you? (polite) | how go you?
enchanté | nice to meet you | enchanted
je ne comprends pas | I don't understand
vous pouvez répéter ? | could you repeat that?
parlez plus lentement, s'il vous plaît | please speak more slowly
je ne sais pas | I don't know
combien ça coûte ? | how much does it cost?
l'addition, s'il vous plaît | the bill, please
où sont les toilettes ? | where is the toilet?
il y a | there is, there are | it there has
qu'est-ce que c'est ? | what is it? | what is it that it is?
à quelle heure ? | at what time?
bon appétit | enjoy your meal | good appetite
santé ! | cheers! | health!
bonne journée | have a good day
bon week-end | have a good weekend
"""
    ,
    ["greetings"],
)

CONNECTIVES = connectors(
    "connective",
    """
d'abord | first, first of all | conn-sequence | D'abord, on mange ; après, on sort. | First we eat; then we go out.
puis | then | conn-sequence | Il ouvre la porte, puis il entre. | He opens the door, then he goes in.
aussi | also, too | conn-addition | J'aime le thé. J'aime aussi le café. | I like tea. I also like coffee.
""",
    ["connecteurs"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
et | and | conj-coordinating | J'ai un frère et une sœur. | I have a brother and a sister.
ou | or | conj-coordinating | Tu veux du thé ou du café ? | Do you want tea or coffee?
quand | when | conj-subordinating | Je lis quand il pleut. | I read when it rains.
si | if | conj-subordinating | On sort si tu veux. | We'll go out if you want.
""",
    ["conjonctions"],
)

ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# Each grammar page's Unit carries the words that use or illustrate it, not
# just whatever happens to share its tag (most of these grammar concepts —
# négation, questions, partitif, nombres, pronoms — tag no vocabulary item at
# all). Pronunciation/pronoun/question phrases are drawn from the greetings
# set without overlap; numbers pairs with the time words used to tell time;
# possessives pairs with family, its most natural example domain.
UNITS = [
    {
        "title": "La prononciation",
        "page_id": "fr-pronunciation",
        "word_ids": ["bonjour", "bonsoir", "merci", "enchante", "pardon", "s-il-vous-plait"],
    },
    {
        "title": "Tu ou vous",
        "page_id": "fr-subject-pronouns",
        "word_ids": ["salut", "ca-va", "comment-allez-vous", "s-il-te-plait", "d-accord", "excusez-moi"],
    },
    {
        "title": "Être et avoir",
        "page_id": "fr-etre-avoir",
        "word_ids": ["etre", "avoir", "faire", "vouloir", "pouvoir", "devoir"],
    },
    {
        "title": "Le présent",
        "page_id": "fr-present-tense",
        "word_ids": ["habiter", "aimer", "travailler", "finir", "choisir", "vendre", "attendre"],
    },
    {
        "title": "La négation",
        "page_id": "fr-negation",
        "word_ids": ["prendre", "mettre", "dire", "voir", "regarder", "ecouter"],
    },
    {
        "title": "Les questions",
        "page_id": "fr-questions",
        "word_ids": [
            "ou-sont-les-toilettes",
            "a-quelle-heure",
            "qu-est-ce-que-c-est",
            "combien-ca-coute",
            "vous-pouvez-repeter",
            "parlez-plus-lentement-s-il-vous-plait",
            "il-y-a",
        ],
    },
    {
        "title": "Le partitif",
        "page_id": "fr-partitive",
        "word_ids": ["cafe", "the", "vin", "biere", "lait", "sucre"],
    },
    {
        "title": "Au, à la, aux",
        "page_id": "fr-contractions",
        "word_ids": ["banque", "ecole", "hopital", "restaurant", "gare", "marche"],
    },
    {
        "title": "Les adjectifs",
        "page_id": "fr-adjectives",
        "word_ids": ["grand", "petit", "bon", "beau", "vieux", "nouveau", "gentil"],
    },
    {
        "title": "Les couleurs",
        "word_ids": ["rouge", "bleu", "vert", "jaune", "noir", "blanc", "gris"],
    },
    {
        "title": "Les nombres",
        "page_id": "fr-numbers",
        "word_ids": ["heure", "minute", "jour", "lundi", "mardi", "mercredi"],
    },
    {
        "title": "Le futur proche",
        "page_id": "fr-near-future",
        "word_ids": ["venir", "arriver", "partir", "sortir", "dormir", "lire", "ecrire"],
    },
    {
        "title": "Les possessifs",
        "page_id": "fr-possessives",
        "word_ids": ["pere", "mere", "frere", "s-ur", "mari", "femme"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "food": "La nourriture",
    "home": "La maison",
    "time": "Le temps",
    "people": "Les gens",
}

PACK = pack(
    "fr-foundations-v1",
    5,
    "fr",
    "Français · Fondations (A1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Pratique"),
)
