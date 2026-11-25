"""fr-fluency-v1: B1. Mood (subjunctive, conditional), complex sentences, register,
and the idioms and false friends that separate textbook French from real French."""

from common import build_units, interleave, page, pack, topic, topic_labels
from fr_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("relatifs", "Pronoms relatifs", "relative pronouns", ["présent"]),
    topic("registre", "Registre", "register: formal, spoken, slang", []),
    topic("faux-amis", "Faux amis", "false friends", []),
    topic("idioms", "Idiomes", "idioms", []),
    topic("society", "Société", "society and ideas", ["articles"]),
    {
        "id": "gérondif",
        "kind": "topic",
        "label": "Gérondif",
        "labelGloss": "en + -ant: while doing, by doing",
        "dependsOn": ["présent"],
    },
]

PAGES = [
    page(
        "fr-subjunctive",
        "The subjunctive",
        r"""
The **subjonctif** is a mood, not a tense. It marks a clause as wished for, feared, doubted, necessary or not yet real. English has traces of it (*I insist that he **be** there*); French uses it every day.

It appears almost only after **que**, in a clause whose main verb expresses something other than a plain fact.

## Forming it

Take the **ils** form of the present, drop **-ent**, add **-e, -es, -e, -ions, -iez, -ent**. The nous and vous forms look like the imparfait.

| | parler (ils parlent) | finir (ils finissent) | prendre (ils prennent) |
| --- | --- | --- | --- |
| que je | parle | finisse | prenne |
| que tu | parles | finisses | prennes |
| qu'il | parle | finisse | prenne |
| que nous | parlions | finissions | prenions |
| que vous | parliez | finissiez | preniez |
| qu'ils | parlent | finissent | prennent |

Irregular: **être** (sois, soit, soyons), **avoir** (aie, ait, ayons), **aller** (aille, allions), **faire** (fasse), **pouvoir** (puisse), **savoir** (sache), **vouloir** (veuille, voulions).

## What triggers it

| Trigger | Examples |
| --- | --- |
| Necessity | il faut que, il est important que |
| Wanting | vouloir que, souhaiter que, préférer que |
| Feeling | être content que, avoir peur que, regretter que |
| Doubt | douter que, ne pas penser que, ne pas croire que |
| Some conjunctions | bien que, pour que, avant que, à moins que, sans que, jusqu'à ce que |

:::examples
- Il faut que tu viennes. — You have to come.
- Je veux qu'il soit là. — I want him to be there.
- Bien qu'il pleuve, on sort. — Although it's raining, we're going out.
:::

## What doesn't trigger it

- **Espérer que** takes the indicative: *J'espère qu'il viendra.*
- **Penser que** and **croire que** take the indicative when positive, the subjunctive when negated: *Je pense qu'il a raison* / *Je ne pense pas qu'il ait raison.*
- **Après que** takes the indicative (in careful French), unlike *avant que*.
- If both clauses have the same subject, use an infinitive: *Je veux partir*, not *je veux que je parte*.

:::cloze{sentence="Il faut que tu ___ patient." blank="sois"}
:::
""",
        ["subjonctif"],
        "fr-subjunctive",
        explains=["subjonctif"],
    ),
    page(
        "fr-conditional",
        "The conditional and si clauses",
        r"""
The **conditionnel** is *would*. It uses the future stem with the imparfait endings: *je parlerais, tu pourrais, il serait*.

## Politeness

The conditional makes requests softer, the way *could* and *would* do in English:

:::examples
- Je voudrais un café. — I'd like a coffee.
- Pourriez-vous m'aider ? — Could you help me?
- Tu devrais te reposer. — You should rest.
- Ça serait génial. — That would be great.
:::

## Si clauses

French pairs tenses strictly in *if* sentences. The rule English speakers break: **never put the conditional after si**.

| Situation | si + | main clause | Example |
| --- | --- | --- | --- |
| Likely | présent | futur (or présent) | Si tu viens, je serai content. |
| Hypothetical | imparfait | conditionnel | Si j'avais le temps, je voyagerais. |
| Missed chance | plus-que-parfait | conditionnel passé | Si j'avais su, je serais venu. |

*Si je serais riche* is wrong. It's *si j'étais riche*.

*Si* becomes *s'* only before *il* and *ils*: *s'il pleut*, but *si elle pleure*.

## Reported speech and rumours

Journalists use the conditional for unconfirmed facts: *Le président serait malade* means "the president is reportedly ill".
""",
        ["conditionnel"],
        "fr-conditional",
        explains=["conditionnel"],
    ),
    page(
        "fr-relative-pronouns",
        "Qui, que, dont, où",
        r"""
Relative pronouns join two sentences about the same thing. English can often leave them out (*the book I read*); French never can.

| Pronoun | Replaces | Example |
| --- | --- | --- |
| qui | the subject | L'homme **qui** parle est mon père. |
| que (qu') | the direct object | Le livre **que** je lis est long. |
| dont | something after **de** | Le film **dont** je parle est sorti hier. |
| où | a place or a time | La ville **où** j'habite. Le jour **où** il est parti. |

## Qui or que?

Look at what comes right after it. If a verb follows, it's usually **qui** (it is the subject). If a subject follows, it's **que**: *le chat qui dort* / *le chat que je vois*.

## Dont

**Dont** replaces **de + noun** after verbs and expressions that take *de*: *parler de*, *avoir besoin de*, *se souvenir de*, *avoir peur de*.

*J'ai besoin de ce livre* → *C'est le livre dont j'ai besoin.* (the book I need)

## Ce qui, ce que

When there's no noun to refer back to, add **ce**: *Ce qui compte, c'est la santé* (What matters is health). *Je fais ce que je veux* (I do what I want).

## Où for time

*Le jour où je t'ai rencontré* (the day I met you). English says *when* or nothing; French says *où*.
""",
        ["relatifs"],
        "fr-relative-pronouns",
        explains=["relatifs"],
    ),
    page(
        "fr-register",
        "Spoken French, slang and verlan",
        r"""
Written French and spoken French are further apart than written and spoken English. A learner who only knows the textbook will understand a news bulletin and miss half of a dinner conversation.

## What speech drops or shortens

| Written | Spoken | |
| --- | --- | --- |
| Je ne sais pas | Je sais pas, chais pas | *ne* disappears |
| Tu es | T'es | *tu* elides |
| Il y a | Y a | |
| Nous allons | On va | *on* replaces *nous* |
| Est-ce que tu viens ? | Tu viens ? | intonation replaces est-ce que |
| Cela | Ça | |

## Everyday informal words

| Informal | Standard | English |
| --- | --- | --- |
| le boulot | le travail | job |
| le fric, le pognon | l'argent | money |
| la bagnole | la voiture | car |
| un mec | un homme | a guy |
| une nana | une femme | a girl, woman |
| un truc | une chose | a thing |
| bouffer | manger | to eat |
| bosser | travailler | to work |
| crevé | très fatigué | knackered |
| sympa | sympathique | nice |

## Verlan

**Verlan** swaps the syllables of a word; *verlan* itself is *l'envers* (the reverse) reversed. Some verlan words are now plain everyday French:

| Verlan | From | Meaning |
| --- | --- | --- |
| une meuf | femme | a woman |
| relou | lourd | annoying |
| chelou | louche | shady, weird |
| ouf | fou | crazy |
| vénère | énervé | angry |
| laisse béton | laisse tomber | forget it |

Use these with friends, not in a job interview.
""",
        ["registre"],
        "fr-register",
        explains=["registre"],
    ),
    page(
        "fr-false-friends",
        "False friends",
        r"""
French and English share thousands of words, and most mean the same thing. These don't. Each one has caught out generations of learners.

| French | Means | Not |
| --- | --- | --- |
| actuellement | currently | actually (*en fait*) |
| éventuellement | possibly | eventually (*finalement*) |
| une librairie | a bookshop | a library (*une bibliothèque*) |
| sensible | sensitive | sensible (*raisonnable*) |
| attendre | to wait | to attend (*assister à*) |
| rester | to stay | to rest (*se reposer*) |
| une location | a rental | a location (*un endroit*) |
| blesser | to injure | to bless (*bénir*) |
| une déception | a disappointment | a deception (*une tromperie*) |
| un coin | a corner | a coin (*une pièce*) |
| la monnaie | change, coins | money (*l'argent*) |
| un préservatif | a condom | a preservative (*un conservateur*) |
| supporter | to put up with | to support (*soutenir*) |
| large | wide | large (*grand*) |
| le raisin | grapes | raisins (*les raisins secs*) |
| une journée | a day | a journey (*un voyage*) |
| excité | excited, but can mean aroused | say *j'ai hâte* for "I'm excited" |

*J'ai hâte !* (I can't wait!) is the safe way to say you're excited about something.
""",
        ["faux-amis"],
        "fr-false-friends",
        explains=["faux-amis"],
    ),
    page(
        "fr-idioms",
        "How French idioms work",
        r"""
Idioms are phrases whose meaning isn't the sum of their words. French idioms lean on food, animals and the body, and many have a close English cousin with a different image.

| French | Literally | Meaning |
| --- | --- | --- |
| avoir un chat dans la gorge | to have a cat in the throat | to have a frog in your throat |
| il pleut des cordes | it's raining ropes | it's raining cats and dogs |
| coûter les yeux de la tête | to cost the eyes of the head | to cost an arm and a leg |
| quand les poules auront des dents | when hens have teeth | when pigs fly |
| poser un lapin | to put down a rabbit | to stand someone up |

Idioms in this pack are drilled like any other phrase: the card shows the French, you recall the meaning. The literal translation is stored with each one because it's usually what makes the idiom stick.

Use them sparingly at first. One well-placed idiom sounds natural; five in a row sound like a phrasebook.
""",
        ["idioms"],
        "fr-idioms",
        explains=["idioms"],
    ),
    page(
        "fr-past-perfect-and-literary",
        "Plus-que-parfait and passé simple",
        r"""
Two more past tenses complete the picture.

## Plus-que-parfait: had done

The past before the past. Use the **imparfait** of avoir or être plus the participle, exactly like English *had + participle*.

:::examples
- J'avais déjà mangé quand il est arrivé. — I had already eaten when he arrived.
- Elle était partie. — She had left.
:::

The same verbs take être as in the passé composé.

## Passé simple: recognise it, don't produce it

The **passé simple** is the literary past. Novels, fairy tales and history books use it where speech uses the passé composé. You'll meet it in the third person almost exclusively.

| Infinitive | il / elle | ils / elles |
| --- | --- | --- |
| parler | parla | parlèrent |
| finir | finit | finirent |
| être | fut | furent |
| avoir | eut | eurent |
| faire | fit | firent |
| aller | alla | allèrent |
| venir | vint | vinrent |
| prendre | prit | prirent |

*Il était une fois un roi qui avait trois filles. Un jour, il tomba malade.* (Once upon a time there was a king who had three daughters. One day, he fell ill.) The imparfait sets the scene; the passé simple tells the story.
""",
        ["passé-composé", "registre"],
        "fr-past-literary",
    ),
    page(
        "fr-gerund",
        "En faisant: the gérondif",
        r"""
The **gérondif** is **en + present participle**. It links two actions done by the same person, and covers English *while*, *by* and *on*.

## Forming the present participle

Take the **nous** form, drop **-ons**, add **-ant**: *nous parlons → parlant*, *nous finissons → finissant*, *nous faisons → faisant*.

Three irregular ones: *être → étant*, *avoir → ayant*, *savoir → sachant*.

## Uses

:::examples
- Il chante en prenant sa douche. — He sings while taking a shower.
- C'est en forgeant qu'on devient forgeron. — Practice makes perfect. (It's by forging that you become a blacksmith.)
- En arrivant, j'ai vu le problème. — On arriving, I saw the problem.
- Tout en étant fatigué, il a fini le travail. — Even though he was tired, he finished the work.
:::

*Tout en* stresses that the two actions happen at once, often with a hint of contrast.

Both actions must have the same subject. *En sortant, la pluie a commencé* is wrong: the rain didn't go out.
""",
        ["gérondif"],
        "fr-gerund",
        explains=["gérondif"],
    ),
    page(
        "fr-nuance-connectives",
        "Although, even if, because",
        r"""
French has several words where English has one, and each carries its own grammar.

## Although and even if

- **Bien que** + subjunctive: *Bien qu'il soit tard, je continue.*
- **Même si** + indicative: *Même s'il est tard, je continue.* Same meaning, different mood. Many learners keep *même si* for speech because it avoids the subjunctive.
- **Quoique** + subjunctive is a more literary *bien que*.

## Because

| Word | Use | Example |
| --- | --- | --- |
| parce que | answers "why?", neutral | Je reste parce que j'ai froid. |
| car | written, never starts a sentence | Il est parti, car il était tard. |
| puisque | the reason is already known | Puisque tu es là, aide-moi. |
| comme | starts the sentence | Comme il pleut, on reste. |
| grâce à | thanks to (good cause) | Grâce à toi, j'ai réussi. |
| à cause de | because of (bad cause) | À cause de la pluie, on reste. |

## However

*Cependant*, *pourtant*, *toutefois* and *néanmoins* all translate as "however". *Pourtant* carries surprise (and yet); *toutefois* and *néanmoins* are formal; *mais* is what people actually say.
""",
        ["conjonctions", "subjonctif"],
        "fr-nuance-connectives",
        explains=["conjonctions"],
    ),
]

NOUNS = nouns(
    """
# society and ideas
société | f | society; company | society
gouvernement | m | government | society
loi | f | law | society
droit | m | right; law (the subject) | society
liberté | f | freedom | society
égalité | f | equality | society
élection | f | election | society
guerre | f | war | society
paix | f | peace | society
environnement | m | environment | society
pollution | f | pollution | society
avenir | m | future | society
passé | m | past | society
histoire | f | history; story | society
culture | f | culture | society
langue | f | language; tongue | society
problème | m | problem | society
solution | f | solution | society
raison | f | reason | society
avis | m | opinion | society | avis
idée | f | idea | society
choix | m | choice | society | choix
chance | f | luck; chance | society
succès | m | success | society | succès
échec | m | failure | society
peur | f | fear | feelings
joie | f | joy | feelings
colère | f | anger | feelings
*honte | f | shame | feelings
*hâte | f | haste, eagerness | feelings
souvenir | m | memory (something remembered) | feelings
mémoire | f | memory (the faculty) | feelings
rêve | m | dream | feelings
espoir | m | hope | feelings
amour | m | love | feelings
amitié | f | friendship | feelings
# untranslatables and false friends
flemme | f | laziness, can't-be-bothered feeling | idioms
dépaysement | m | the feeling of being away from familiar surroundings | idioms
rentrée | f | the September return to school and work | idioms
terroir | m | the land and climate that give food its character | idioms
bibliothèque | f | library | faux-amis
librairie | f | bookshop | faux-amis
location | f | rental | faux-amis
déception | f | disappointment | faux-amis
coin | m | corner | faux-amis
journée | f | day (its length) | faux-amis
"""
)

ADJECTIVES = adjectives(
    """
actuel, actuelle, actuels, actuelles | current, present-day
éventuel, éventuelle, éventuels, éventuelles | possible
sensible, sensible, sensibles, sensibles | sensitive
large, large, larges, larges | wide, broad
ancien, ancienne, anciens, anciennes | old; former (before the noun)
propre, propre, propres, propres | own (before); clean (after)
seul, seule, seuls, seules | alone; only
important, importante, importants, importantes | important
nécessaire, nécessaire, nécessaires, nécessaires | necessary
possible, possible, possibles, possibles | possible
inquiet, inquiète, inquiets, inquiètes | worried
fier, fière, fiers, fières | proud
jaloux, jalouse, jaloux, jalouses | jealous
généreux, généreuse, généreux, généreuses | generous
bête, bête, bêtes, bêtes | stupid, silly
malin, maligne, malins, malignes | clever, crafty
doux, douce, doux, douces | soft, gentle, sweet
frais, fraîche, frais, fraîches | fresh, cool
faux, fausse, faux, fausses | false, wrong
crevé, crevée, crevés, crevées | knackered (informal)
"""
)
# "propre" is already taught in the everyday pack; keep one card for it.
ADJECTIVES = [a for a in ADJECTIVES if a["id"] != "propre"]
for a in ADJECTIVES[:4]:
    a["tags"].append("faux-amis")

VERBS = [
    verb("se souvenir", "to remember", ["feelings"], pp="souvenu", refl=True,
         present="souviens souviens souvient souvenons souvenez souviennent", fut="souviendr",
         example="Tu te souviens de moi ?", example_en="Do you remember me?"),
    verb("s'occuper", "to take care of, to deal with", [], pp="occupé", refl=True,
         example="Je m'occupe de tout.", example_en="I'll take care of everything."),
    verb("se tromper", "to be mistaken", [], pp="trompé", refl=True,
         example="Je me suis trompé de numéro.", example_en="I dialled the wrong number."),
    verb("s'inquiéter", "to worry", ["feelings"], pp="inquiété", refl=True,
         present="inquiète inquiètes inquiète inquiétons inquiétez inquiètent",
         example="Ne t'inquiète pas.", example_en="Don't worry."),
    verb("se plaindre", "to complain", [], pp="plaint", refl=True,
         present="plains plains plaint plaignons plaignez plaignent",
         example="Il se plaint tout le temps.", example_en="He complains all the time."),
    verb("réussir", "to succeed; to pass (an exam)", [], pp="réussi",
         example="J'ai réussi mon examen !", example_en="I passed my exam!"),
    verb("réfléchir", "to think (something over)", [], pp="réfléchi",
         example="Laisse-moi réfléchir.", example_en="Let me think about it."),
    verb("grandir", "to grow up", [], pp="grandi",
         example="J'ai grandi à la campagne.", example_en="I grew up in the countryside."),
    verb("tenir", "to hold", [], pp="tenu",
         present="tiens tiens tient tenons tenez tiennent", fut="tiendr",
         example="Tiens, c'est pour toi.", example_en="Here, this is for you."),
    verb("obtenir", "to obtain, to get", [], pp="obtenu",
         present="obtiens obtiens obtient obtenons obtenez obtiennent", fut="obtiendr",
         example="Elle a obtenu son diplôme.", example_en="She got her degree."),
    verb("permettre", "to allow", [], pp="permis",
         present="permets permets permet permettons permettez permettent",
         example="Vous permettez ?", example_en="May I?"),
    verb("promettre", "to promise", [], pp="promis",
         present="promets promets promet promettons promettez promettent",
         example="Je te le promets.", example_en="I promise you."),
    verb("construire", "to build", [], pp="construit",
         present="construis construis construit construisons construisez construisent",
         example="Ils construisent une maison.", example_en="They're building a house."),
    verb("craindre", "to fear", ["feelings"], pp="craint",
         present="crains crains craint craignons craignez craignent",
         example="Je crains le pire.", example_en="I fear the worst."),
    verb("rire", "to laugh", ["feelings"], pp="ri",
         present="ris ris rit rions riez rient",
         subj="rie ries rie riions riiez rient",
         example="Il rit de tout.", example_en="He laughs at everything."),
    verb("sourire", "to smile", ["feelings"], pp="souri",
         present="souris souris sourit sourions souriez sourient",
         subj="sourie souries sourie souriions souriiez sourient",
         example="Souris, tu es filmé !", example_en="Smile, you're on camera!"),
    verb("mentir", "to lie (tell lies)", [], pp="menti",
         present="mens mens ment mentons mentez mentent",
         example="Tu mens !", example_en="You're lying!"),
    verb("servir", "to serve; to be for", [], pp="servi",
         present="sers sers sert servons servez servent",
         example="À quoi ça sert ?", example_en="What's it for?"),
    verb("disparaître", "to disappear", [], pp="disparu",
         present="disparais disparais disparaît disparaissons disparaissez disparaissent",
         fut="disparaîtr",
         example="Mes clés ont disparu.", example_en="My keys have disappeared."),
    verb("jeter", "to throw (away)", [], pp="jeté",
         present="jette jettes jette jetons jetez jettent", fut="jetter",
         example="Ne jette pas ça !", example_en="Don't throw that away!"),
    verb("espérer", "to hope", ["feelings"], pp="espéré",
         present="espère espères espère espérons espérez espèrent",
         example="J'espère que tu vas bien.", example_en="I hope you're well."),
    verb("nettoyer", "to clean", ["home"], pp="nettoyé",
         present="nettoie nettoies nettoie nettoyons nettoyez nettoient", fut="nettoier",
         example="Je nettoie la cuisine.", example_en="I'm cleaning the kitchen."),
    verb("suivre", "to follow", [], pp="suivi",
         present="suis suis suit suivons suivez suivent",
         example="Suivez-moi.", example_en="Follow me."),
]

IDIOMS = phrases(
    """
avoir le cafard | to feel down, to have the blues | to have the cockroach
avoir la flemme | to not be able to be bothered | to have the laziness
poser un lapin | to stand someone up | to put down a rabbit
il pleut des cordes | it's raining cats and dogs | it's raining ropes
coûter les yeux de la tête | to cost an arm and a leg | to cost the eyes of the head
avoir un chat dans la gorge | to have a frog in your throat | to have a cat in the throat
quand les poules auront des dents | when pigs fly | when hens have teeth
ce n'est pas la mer à boire | it's not that hard | it's not the sea to drink
avoir la pêche | to be full of energy | to have the peach
casser les pieds | to annoy someone | to break the feet
donner sa langue au chat | to give up guessing | to give your tongue to the cat
tomber dans les pommes | to faint | to fall in the apples
mettre son grain de sel | to put your two cents in | to put in your grain of salt
avoir d'autres chats à fouetter | to have bigger fish to fry | to have other cats to whip
raconter des salades | to tell tall stories | to tell salads
être dans la lune | to be daydreaming | to be in the moon
les carottes sont cuites | the game is up, it's all over | the carrots are cooked
faire la grasse matinée | to have a lie-in | to make the fat morning
avoir le coup de foudre | to fall in love at first sight | to have the lightning strike
se prendre un râteau | to be turned down (romantically) | to take a rake
appeler un chat un chat | to call a spade a spade | to call a cat a cat
revenir à nos moutons | to get back to the subject | to come back to our sheep
chercher la petite bête | to nitpick | to look for the little beast
en avoir marre | to be fed up | to have enough of it
ça me fait une belle jambe | a fat lot of good that does me | that makes me a beautiful leg
être au bout du rouleau | to be at the end of your tether | to be at the end of the roll
faire d'une pierre deux coups | to kill two birds with one stone | to make two hits with one stone
il y a anguille sous roche | something fishy is going on | there's an eel under the rock
avoir la tête dans le cul | to be groggy, half asleep (vulgar) | to have your head in your backside
les doigts dans le nez | easily, with no effort | fingers in the nose
occupe-toi de tes oignons | mind your own business | take care of your onions
ne pas être dans son assiette | to feel under the weather | to not be in your plate
tirer les vers du nez | to worm information out of someone | to pull the worms from the nose
avoir un poil dans la main | to be very lazy | to have a hair in your hand
coûter la peau des fesses | to cost a fortune (informal) | to cost the skin of the buttocks
"""
    ,
    ["idioms"],
)

EXPRESSIONS = phrases(
    """
bref | in short, anyway | brief
du coup | so, as a result (spoken) | of the blow
les retrouvailles | reunion, meeting again after a long time | the re-findings
en tout cas | in any case, anyway
n'importe quoi | nonsense; anything at all | no matter what
tant que | as long as
à la limite | at a push, if need be | at the limit
bof | meh, not really
ça marche | sounds good, deal | that walks
c'est pas mon truc | it's not my thing
j'ai hâte | I can't wait | I have haste
on verra | we'll see
laisse tomber | forget it, drop it | let fall
tu parles ! | you must be joking!, yeah right! | you speak!
c'est la vie | that's life
je t'en prie | don't mention it; go ahead | I pray you of it
il n'y a pas de quoi | don't mention it | there is nothing of what
à vrai dire | to tell the truth | to true say
système D | resourcefulness, making do | system D (from débrouiller)
l'esprit de l'escalier | thinking of the perfect reply too late | the spirit of the staircase
"""
    ,
    ["expressions"],
)
for e in EXPRESSIONS:
    if e["primary_form"] in {"du coup", "bof", "ça marche", "tu parles !", "c'est pas mon truc"}:
        e["tags"].append("registre")

CONNECTIVES = connectors(
    "connective",
    """
néanmoins | nevertheless | conn-contrast | C'est difficile ; néanmoins, c'est possible. | It's difficult; nevertheless, it's possible.
toutefois | however (formal) | conn-contrast | Le projet est bon ; toutefois, il coûte cher. | The project is good; however, it's expensive.
au contraire | on the contrary | conn-contrast | Il n'est pas timide ; au contraire, il parle à tout le monde. | He isn't shy; on the contrary, he talks to everyone.
d'ailleurs | besides, moreover | conn-addition | Je n'ai pas faim ; d'ailleurs, j'ai déjà mangé. | I'm not hungry; besides, I've already eaten.
en outre | furthermore (formal) | conn-addition | Le loyer est bas ; en outre, le quartier est calme. | The rent is low; furthermore, the area is quiet.
c'est pourquoi | that's why | conn-consequence | Il était malade, c'est pourquoi il n'est pas venu. | He was ill; that's why he didn't come.
ainsi | thus, so | conn-consequence | Il a travaillé dur et ainsi il a réussi. | He worked hard and thus succeeded.
en fait | in fact, actually | conn-cause | Je ne viens pas ; en fait, je suis malade. | I'm not coming; actually, I'm ill.
finalement | in the end | conn-sequence | On a beaucoup hésité, et finalement on est restés. | We hesitated a lot, and in the end we stayed.
""",
    ["connecteurs"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
puisque | since (the reason is known) | conj-subordinating | Puisque tu es là, aide-moi. | Since you're here, help me.
pour que | so that (+ subjunctive) | conj-subordinating | Je parle lentement pour que tu comprennes. | I speak slowly so that you understand.
avant que | before (+ subjunctive) | conj-subordinating | Rentre avant que la nuit tombe. | Come home before night falls.
à moins que | unless (+ subjunctive) | conj-subordinating | On sortira, à moins que la pluie continue. | We'll go out, unless the rain keeps up.
même si | even if (+ indicative) | conj-subordinating | Je viendrai même si la route est longue. | I'll come even if it's a long way.
tandis que | whereas; while | conj-subordinating | Il aime la mer, tandis que je préfère la montagne. | He loves the sea, whereas I prefer the mountains.
dès que | as soon as | conj-subordinating | Appelle-moi dès que tu arriveras. | Call me as soon as you arrive.
sans que | without (+ subjunctive) | conj-subordinating | Il est parti sans que je le voie. | He left without my seeing him.
or | now, yet (in an argument) | conj-coordinating | Il devait venir, or il n'est pas venu. | He was supposed to come, yet he didn't.
""",
    ["conjonctions"],
)

ITEMS = PAGES + interleave(IDIOMS, EXPRESSIONS, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# fr-idioms and fr-false-friends anchor on the idioms/faux-amis pools their
# tag already names; the rest of each pool still becomes an automatic
# "Idiomes" Unit via LABELS below (false friends is small enough that its
# page unit uses all six and there's no remainder). fr-nuance-connectives
# uses every conjonctions-tagged item — the "although, because, even if"
# family the page teaches is exactly that tag. Grammar concepts with no
# tagged vocabulary of their own (subjonctif, conditionnel, relatifs) draw
# illustrative verbs from the leftover présent pool; fr-register and
# fr-gerund draw from the colloquial "expressions" pool.
UNITS = [
    {
        "title": "Le subjonctif",
        "page_id": "fr-subjunctive",
        "word_ids": ["reussir", "reflechir", "grandir", "esperer", "mentir", "servir"],
    },
    {
        "title": "Le conditionnel",
        "page_id": "fr-conditional",
        "word_ids": ["disparaitre", "jeter", "nettoyer", "suivre", "rire", "sourire"],
    },
    {
        "title": "Pronoms relatifs",
        "page_id": "fr-relative-pronouns",
        "word_ids": ["tenir", "obtenir", "permettre", "promettre", "construire", "craindre"],
    },
    {
        "title": "Registre familier",
        "page_id": "fr-register",
        "word_ids": ["bref", "du-coup", "bof", "ca-marche", "c-est-pas-mon-truc", "tu-parles", "c-est-la-vie"],
    },
    {
        "title": "Faux amis",
        "page_id": "fr-false-friends",
        "word_ids": ["bibliotheque", "librairie", "location", "deception", "coin", "journee"],
    },
    {
        "title": "Idiomes",
        "page_id": "fr-idioms",
        "word_ids": [
            "avoir-le-cafard",
            "avoir-la-flemme",
            "poser-un-lapin",
            "il-pleut-des-cordes",
            "couter-les-yeux-de-la-tete",
            "avoir-un-chat-dans-la-gorge",
            "quand-les-poules-auront-des-dents",
            "ce-n-est-pas-la-mer-a-boire",
        ],
    },
    {
        "title": "Le plus-que-parfait et le passé simple",
        "page_id": "fr-past-perfect-and-literary",
        "word_ids": ["passe", "histoire", "avenir", "guerre", "paix", "culture"],
    },
    {
        "title": "Le gérondif",
        "page_id": "fr-gerund",
        "word_ids": ["en-tout-cas", "tant-que", "a-la-limite", "laisse-tomber", "on-verra", "j-ai-hate"],
    },
    {
        "title": "Bien que, même si, parce que",
        "page_id": "fr-nuance-connectives",
        "word_ids": [
            "puisque",
            "pour-que",
            "avant-que",
            "a-moins-que",
            "meme-si",
            "tandis-que",
            "des-que",
            "sans-que",
            "or",
        ],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "feelings": "Sentiments",
}

PACK = pack(
    "fr-fluency-v1",
    6,
    "fr",
    "Français · Aisance (B1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Pratique"),
)
