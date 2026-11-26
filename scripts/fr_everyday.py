"""fr-everyday-v1: A2. Talking about the past and the future, handling daily life
(shops, travel, work, health), and the pronouns that make sentences sound native."""

from common import build_units, interleave, page, pack, topic, topic_labels
from fr_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("verbes-pronominaux", "Verbes pronominaux", "reflexive verbs", ["présent"]),
    topic("pronoms-objets", "Pronoms objets", "object pronouns", ["présent"]),
    topic("clothing", "Vêtements", "clothing", ["articles"]),
    topic("weather", "Météo", "weather", ["articles"]),
    topic("travel", "Voyage", "travel", ["articles"]),
    topic("work", "Travail", "work and study", ["articles"]),
    topic("health", "Santé", "health", ["articles"]),
    topic("leisure", "Loisirs", "free time", ["articles"]),
    topic("feelings", "Sentiments", "feelings and character", ["adjectifs"]),
    topic("shopping", "Achats", "shopping and money", ["articles"]),
    topic("expressions", "Expressions", "set phrases and idioms", []),
    {
        "id": "conn-consequence",
        "kind": "connective-class",
        "label": "Conséquence",
        "labelGloss": "the next statement is the result of the last one (alors, par conséquent)",
        "order": 4,
        "appliesTo": {"kind": "connective"},
        "dependsOn": [],
    },
]

PAGES = [
    page(
        "fr-passe-compose",
        "The passé composé",
        r"""
The **passé composé** is the everyday past tense for things that happened: *I ate*, *I have eaten* and *I did eat* are all *j'ai mangé*.

It has two parts: the present of **avoir** (or **être**, see the next page) and the **past participle**.

| | manger |
| --- | --- |
| j' | ai mangé |
| tu | as mangé |
| il / elle | a mangé |
| nous | avons mangé |
| vous | avez mangé |
| ils / elles | ont mangé |

## Regular participles

| Infinitive | Participle | Example |
| --- | --- | --- |
| -er | -é | parler → parlé |
| -ir | -i | finir → fini |
| -re | -u | vendre → vendu |

## Irregular participles worth learning now

| | | |
| --- | --- | --- |
| être → été | avoir → eu | faire → fait |
| prendre → pris | mettre → mis | dire → dit |
| écrire → écrit | voir → vu | lire → lu |
| boire → bu | pouvoir → pu | vouloir → voulu |
| devoir → dû | savoir → su | venir → venu |
| ouvrir → ouvert | naître → né | mourir → mort |

:::examples
- J'ai mangé une pizza hier soir. — I ate a pizza last night.
- Nous avons fini le travail. — We've finished the work.
- Tu as vu ce film ? — Have you seen this film?
:::

## Negation and questions

*Ne ... pas* wraps the helper verb, not the participle: *Je n'ai pas mangé.* With inversion, the helper moves too: *As-tu mangé ?*

:::predict{prompt="nous (choisir)" answer="avons choisi"}
:::
""",
        ["passé-composé"],
        "fr-passe-compose",
        explains=["passé-composé"],
    ),
    page(
        "fr-etre-verbs",
        "Verbs that take être",
        r"""
About twenty verbs, mostly about movement or change of state, build the passé composé with **être** instead of avoir. English speakers remember them as **DR MRS VANDERTRAMP**:

| | | |
| --- | --- | --- |
| **D**evenir (devenu) | **R**evenir (revenu) | **M**onter (monté) |
| **R**entrer (rentré) | **S**ortir (sorti) | **V**enir (venu) |
| **A**ller (allé) | **N**aître (né) | **D**escendre (descendu) |
| **E**ntrer (entré) | **R**ester (resté) | **T**omber (tombé) |
| **R**etourner (retourné) | **A**rriver (arrivé) | **M**ourir (mort) |
| **P**artir (parti) | | |

Picture a house: you arrive, go in, go up the stairs, come down, go out, fall. Those are the être verbs.

## Agreement

With être, the participle **agrees with the subject** like an adjective: *il est allé*, but *elle est allée*.

:::examples
- Il est allé à Paris. — He went to Paris.
- Elle est allée à Paris. — She went to Paris.
- Ils sont allés à Paris. — They went to Paris.
- Elles sont allées à Paris. — They (all women) went to Paris.
:::

The agreement is mostly silent, so you'll see it more than hear it. The drills in this app use the masculine form (*je suis allé*); if you're a woman, write *allée* in real life.

## Reflexive verbs take être too

Every reflexive verb uses être: *je me suis levé*, *elle s'est habillée*.
""",
        ["passé-composé"],
        "fr-etre-verbs",
    ),
    page(
        "fr-imparfait",
        "Imparfait or passé composé?",
        r"""
French has two main past tenses, and the choice between them is about how you see the action, not when it happened.

- **Passé composé**: a completed event. Something happened. *J'ai mangé une pizza.*
- **Imparfait**: the background, a habit, or a state. What things were like. *Je mangeais une pizza* (I was eating a pizza / I used to eat pizza).

## Forming the imparfait

Take the **nous** form of the present, drop **-ons**, add **-ais, -ais, -ait, -ions, -iez, -aient**. Only *être* is irregular (stem *ét-*).

| | parler (nous parlons) | être |
| --- | --- | --- |
| je | parlais | étais |
| tu | parlais | étais |
| il | parlait | était |
| nous | parlions | étions |
| vous | parliez | étiez |
| ils | parlaient | étaient |

## The film test

Imagine the past as a film. The **imparfait** is the scenery and what was already going on. The **passé composé** is the action that moves the plot.

:::examples
- Il pleuvait quand je suis sorti. — It was raining when I went out.
- Quand j'étais petit, j'habitais à Nice. — When I was little, I lived in Nice.
- Tous les étés, nous allions à la mer. — Every summer, we used to go to the sea.
- Soudain, le téléphone a sonné. — Suddenly, the phone rang.
:::

Signal words help: *tous les jours*, *souvent*, *d'habitude*, *quand j'étais...* point to the imparfait; *soudain*, *un jour*, *hier*, *tout à coup* point to the passé composé.
""",
        ["imparfait"],
        "fr-imparfait",
        explains=["imparfait"],
    ),
    page(
        "fr-reflexive-verbs",
        "Reflexive verbs: se lever",
        r"""
A **reflexive verb** has an extra pronoun that refers back to the subject. English does this rarely (*I hurt myself*). French does it constantly, often where English uses "get": *se lever* (get up), *s'habiller* (get dressed), *se marier* (get married).

| | se lever |
| --- | --- |
| je | me lève |
| tu | te lèves |
| il / elle | se lève |
| nous | nous levons |
| vous | vous levez |
| ils / elles | se lèvent |

*Me, te, se* become *m', t', s'* before a vowel: *je m'appelle*, *il s'habille*.

## Daily routine

The morning routine in French is almost all reflexive: *je me réveille, je me lève, je me douche, je m'habille, je me brosse les dents*.

Notice *je me brosse **les** dents*: with body parts, French uses the article, not a possessive. The reflexive pronoun already says whose teeth.

## Each other

In the plural, the pronoun can mean "each other": *Ils s'aiment* (they love each other), *On se voit demain* (see each other tomorrow).

## Past and negation

Reflexive verbs take **être** in the passé composé: *je me suis levé*. The negation wraps pronoun and verb together: *Je ne me lève pas.*
""",
        ["verbes-pronominaux"],
        "fr-reflexive-verbs",
        explains=["verbes-pronominaux"],
    ),
    page(
        "fr-object-pronouns",
        "Le, lui, y, en: object pronouns",
        r"""
French object pronouns go **before the verb**, which is the opposite of English. *I see him* is *je **le** vois*. In a positive command they go after it, joined by a hyphen: *Prends-le*. *Me* becomes *moi* there: *Dis-moi*.

## Direct objects: le, la, les

Replace a noun that follows the verb directly.

:::examples
- Je vois Paul. → Je le vois. — I see him.
- Tu prends la voiture ? → Tu la prends ? — Are you taking it?
- Il aime les chats. → Il les aime. — He likes them.
:::

## Indirect objects: lui, leur

Replace **à + a person**. *Lui* is both "to him" and "to her".

:::examples
- Je parle à Marie. → Je lui parle. — I talk to her.
- Je téléphone à mes parents. → Je leur téléphone. — I phone them.
:::

**Me, te, nous, vous** are both direct and indirect: *Il me voit*, *Il me parle*.

## Y and en

These two have no English equivalent.

- **y** replaces **à + a place or thing**: *Tu vas à Paris ? Oui, j'y vais.* (Yes, I'm going there.)
- **en** replaces **de + something**, including quantities and partitives: *Tu veux du café ? Oui, j'en veux.* (Yes, I want some.) *J'ai trois frères, j'en ai trois.*

*Il y a* (there is) and *Je m'en vais* (I'm leaving) are fixed expressions that use them.

## Order when there are two

me / te / se / nous / vous → le / la / les → lui / leur → y → en

*Il me le donne.* (He gives it to me.) *Je la lui donne.* (I give it to him.) *Il y en a.* (There are some.)

## With an infinitive

The pronoun goes before the verb it belongs to: *Je vais le faire.* *Je peux t'aider.*
""",
        ["pronoms-objets"],
        "fr-object-pronouns",
        explains=["pronoms-objets"],
    ),
    page(
        "fr-futur-simple",
        "The futur simple",
        r"""
The **futur simple** says what will happen. It's more formal than *aller + infinitive*, and it often feels further off or less settled. It's the tense for promises and predictions.

Take the **infinitive** (drop the final **-e** of -re verbs) and add the endings of *avoir*: **-ai, -as, -a, -ons, -ez, -ont**.

| | parler | prendre |
| --- | --- | --- |
| je | parlerai | prendrai |
| tu | parleras | prendras |
| il | parlera | prendra |
| nous | parlerons | prendrons |
| vous | parlerez | prendrez |
| ils | parleront | prendront |

## Irregular stems

The endings never change; only the stem does. These are worth learning as a list:

| | | |
| --- | --- | --- |
| être → ser- | avoir → aur- | aller → ir- |
| faire → fer- | venir → viendr- | voir → verr- |
| pouvoir → pourr- | vouloir → voudr- | savoir → saur- |
| devoir → devr- | envoyer → enverr- | il faut → il faudra |

## Quand + future

After **quand** and **dès que**, French uses the future where English uses the present: *Quand je serai grand, je serai pilote.* (When I grow up, I'll be a pilot.)

:::examples
- Demain, il fera beau. — Tomorrow the weather will be nice.
- Je t'appellerai ce soir. — I'll call you tonight.
- Quand je serai à Paris, je visiterai le Louvre. — When I'm in Paris, I'll visit the Louvre.
:::
""",
        ["futur-simple"],
        "fr-futur-simple",
        explains=["futur-simple"],
    ),
    page(
        "fr-comparisons",
        "More, less, as ... as",
        r"""
Comparisons put a word before the adjective and **que** after it.

| | Structure | Example |
| --- | --- | --- |
| more | plus ... que | Paul est plus grand que moi. |
| less | moins ... que | Ce film est moins long que l'autre. |
| as | aussi ... que | Elle est aussi intelligente que sa sœur. |

After *que*, use the stressed pronouns: *moi, toi, lui, elle, nous, vous, eux, elles*.

## The superlative

Add the article: *le plus*, *la plus*, *les plus*. *C'est la plus belle ville du monde.* (The most beautiful city in the world: note **du**, not *dans*.)

## Good and well

*Bon* (good, an adjective) and *bien* (well, an adverb) have irregular forms:

| | better | the best |
| --- | --- | --- |
| bon | meilleur | le meilleur |
| bien | mieux | le mieux |

*Ce gâteau est meilleur.* *Elle chante mieux que moi.* Saying *plus bon* is a classic mistake.

## With nouns and verbs

With a noun, use **plus de / moins de / autant de**: *J'ai plus de travail que toi.* With a verb, **plus / moins / autant** follow it: *Il travaille plus que moi.*
""",
        ["adjectifs"],
        "fr-comparisons",
    ),
    page(
        "fr-time-expressions",
        "Depuis, il y a, pendant",
        r"""
English uses the present perfect for something that started in the past and is still going on: *I have lived here for three years*. French uses the **present tense** with **depuis**.

:::examples
- J'habite ici depuis trois ans. — I've lived here for three years.
- Je t'attends depuis une heure ! — I've been waiting for you for an hour!
- Depuis quand tu apprends le français ? — How long have you been learning French?
:::

Saying *j'ai habité ici depuis trois ans* is a very common mistake. It's wrong.

## The other time words

| Word | Meaning | Example |
| --- | --- | --- |
| il y a | ago | Je suis arrivé il y a deux jours. |
| pendant | for, during (a length of time) | J'ai dormi pendant huit heures. |
| dans | in (from now) | Le train part dans dix minutes. |
| en | in (time it takes) | J'ai fait le trajet en deux heures. |

*Dans dix minutes* is when something will start. *En dix minutes* is how long it takes.
""",
        ["time"],
        "fr-time-expressions",
        explains=["time"],
    ),
    page(
        "fr-gender-patterns",
        "Guessing a noun's gender",
        r"""
There's no rule that always works, but word endings are right far more often than guessing.

## Usually feminine

| Ending | Examples |
| --- | --- |
| -tion, -sion | la nation, la télévision |
| -té | la liberté, la société (but *l'été*, summer, is masculine) |
| -ure | la voiture, la culture |
| -ette | la baguette, la fourchette |
| -ence, -ance | la patience, la chance |
| -ie | la vie, la boulangerie |
| -ée | l'année, la journée (but *le musée*, *le lycée*) |

## Usually masculine

| Ending | Examples |
| --- | --- |
| -ment | le moment, le gouvernement |
| -age | le fromage, le voyage (but *la plage*, *la page*, *l'image*) |
| -eau | le bateau, le gâteau (but *l'eau*, *la peau*) |
| -isme | le tourisme |
| -er, -ier | le boucher, le papier |
| -oir | le soir, le miroir |

Days, months, seasons, languages, metals and trees are masculine: *le lundi*, *le français*, *le chêne*.

:::examples
- La voiture est devant le garage. — The car is in front of the garage.
- Le fromage et la baguette sont sur la table. — The cheese and the baguette are on the table.
- Le musée est fermé le lundi. — The museum is closed on Mondays.
:::

## Same word, two genders

A few nouns change meaning with gender. They're worth knowing because the wrong one sounds funny:

| masculine | feminine |
| --- | --- |
| le livre (book) | la livre (pound) |
| le tour (tour, turn) | la tour (tower) |
| le poste (job, post) | la poste (post office) |
| le mode (method, mood) | la mode (fashion) |
| le vase (vase) | la vase (mud) |
| le moule (mould) | la moule (mussel) |
| le manche (handle) | la manche (sleeve); la Manche (English Channel) |
""",
        ["genre"],
        "fr-gender-patterns",
        explains=["genre", "masculin", "féminin"],
    ),
]

NOUNS = nouns(
    """
# clothing
vêtement | m | piece of clothing | clothing
chemise | f | shirt | clothing
pantalon | m | trousers | clothing
jupe | f | skirt | clothing
robe | f | dress | clothing
manteau | m | coat | clothing | manteaux
veste | f | jacket | clothing
pull | m | jumper, sweater | clothing
chaussure | f | shoe | clothing
chaussette | f | sock | clothing
chapeau | m | hat | clothing | chapeaux
sac | m | bag | clothing
# weather and seasons
temps | m | weather; time | weather | temps
pluie | f | rain | weather
neige | f | snow | weather
vent | m | wind | weather
nuage | m | cloud | weather
ciel | m | sky | weather | cieux
orage | m | storm | weather
été | m | summer | weather
hiver | m | winter | weather
printemps | m | spring | weather | printemps
automne | m | autumn | weather
saison | f | season | weather
# travel and transport
voyage | m | trip, journey | travel
billet | m | ticket; banknote | travel
valise | f | suitcase | travel
passeport | m | passport | travel
hôtel | m | hotel | travel
plage | f | beach | travel
mer | f | sea | travel
montagne | f | mountain | travel
pays | m | country | travel | pays
avion | m | aeroplane | transport
train | m | train | transport
bus | m | bus | transport | bus
vélo | m | bicycle | transport
métro | m | underground, metro | transport
bateau | m | boat | transport | bateaux
aéroport | m | airport | transport
carte | f | map; card; menu | travel
# work and study
bureau | m | office; desk | work | bureaux
entreprise | f | company | work
collègue | m | colleague | work
patron | m | boss | work
réunion | f | meeting | work
salaire | m | salary | work
métier | m | trade, profession | work
étudiant | m | student | work
professeur | m | teacher | work
cours | m | lesson, class | work | cours
examen | m | exam | work
ordinateur | m | computer | work
# health
santé | f | health | health
médecin | m | doctor | health
pharmacie | f | chemist's, pharmacy | health
médicament | m | medicine (a drug) | health
rhume | m | cold (illness) | health
fièvre | f | fever | health
douleur | f | pain | health
rendez-vous | m | appointment; date | health | rendez-vous
# leisure
film | m | film | leisure
musique | f | music | leisure
chanson | f | song | leisure
sport | m | sport | leisure
match | m | match, game | leisure
jeu | m | game | leisure | jeux
fête | f | party; celebration | leisure
anniversaire | m | birthday | leisure
cadeau | m | present, gift | leisure | cadeaux
photo | f | photo | leisure
# shopping
prix | m | price | shopping | prix
euro | m | euro | shopping
monnaie | f | change (coins); currency | shopping
carte bancaire | f | bank card | shopping | cartes bancaires
caisse | f | till, checkout | shopping
supermarché | m | supermarket | shopping
boutique | f | small shop | shopping
# home and objects
fourchette | f | fork | home
couteau | m | knife | home | couteaux
cuillère | f | spoon | home
assiette | f | plate | home
verre | m | glass | home
bouteille | f | bottle | home
lumière | f | light | home
# nature and animals
fleur | f | flower | nature
forêt | f | forest | nature
rivière | f | river | nature
lac | m | lake | nature
oiseau | m | bird | animals | oiseaux
cheval | m | horse | animals | chevaux
vache | f | cow | animals
cochon | m | pig | animals
souris | f | mouse | animals | souris
"""
)

ADJECTIVES = adjectives(
    """
heureux, heureuse, heureux, heureuses | happy
triste, triste, tristes, tristes | sad
fâché, fâchée, fâchés, fâchées | angry
calme, calme, calmes, calmes | calm, quiet
sympa, sympa, sympas, sympas | nice, friendly (informal)
drôle, drôle, drôles, drôles | funny
sérieux, sérieuse, sérieux, sérieuses | serious
timide, timide, timides, timides | shy
paresseux, paresseuse, paresseux, paresseuses | lazy
sportif, sportive, sportifs, sportives | sporty
malade, malade, malades, malades | ill, sick
occupé, occupée, occupés, occupées | busy
libre, libre, libres, libres | free (not busy)
prêt, prête, prêts, prêtes | ready
plein, pleine, pleins, pleines | full
vide, vide, vides, vides | empty
long, longue, longs, longues | long | before
court, courte, courts, courtes | short
lourd, lourde, lourds, lourdes | heavy
léger, légère, légers, légères | light (weight)
propre, propre, propres, propres | clean; own
sale, sale, sales, sales | dirty
rapide, rapide, rapides, rapides | fast
lent, lente, lents, lentes | slow
premier, première, premiers, premières | first | before
dernier, dernière, derniers, dernières | last
"""
)
for a in ADJECTIVES[:10]:
    a["tags"].append("feelings")

VERBS = [
    verb("se lever", "to get up", [], pp="levé", refl=True,
         present="lève lèves lève levons levez lèvent", fut="lèver",
         example="Je me lève à sept heures.", example_en="I get up at seven."),
    verb("se réveiller", "to wake up", [], pp="réveillé", refl=True,
         example="Il se réveille tôt.", example_en="He wakes up early."),
    verb("s'habiller", "to get dressed", ["clothing"], pp="habillé", refl=True,
         example="Elle s'habille vite.", example_en="She gets dressed quickly."),
    verb("se coucher", "to go to bed", [], pp="couché", refl=True,
         example="Les enfants se couchent à huit heures.", example_en="The children go to bed at eight."),
    verb("se promener", "to go for a walk", ["leisure"], pp="promené", refl=True,
         present="promène promènes promène promenons promenez promènent", fut="promèner",
         example="On se promène au parc.", example_en="We're going for a walk in the park."),
    verb("se sentir", "to feel", ["health"], pp="senti", refl=True,
         present="sens sens sent sentons sentez sentent",
         example="Je ne me sens pas bien.", example_en="I don't feel well."),
    verb("rester", "to stay", [], aux="être", pp="resté",
         example="Nous sommes restés à la maison.", example_en="We stayed at home."),
    verb("tomber", "to fall", [], aux="être", pp="tombé",
         example="Elle est tombée dans l'escalier.", example_en="She fell down the stairs."),
    verb("entrer", "to go in, to enter", [], aux="être", pp="entré",
         example="Entrez, je vous en prie.", example_en="Come in, please."),
    verb("rentrer", "to go home, to come back", [], aux="être", pp="rentré",
         example="Je suis rentré tard hier soir.", example_en="I got home late last night."),
    verb("monter", "to go up; to get on", [], aux="être", pp="monté",
         example="Ils sont montés dans le bus.", example_en="They got on the bus."),
    verb("descendre", "to go down; to get off", [], aux="être", pp="descendu",
         example="Tu es descendu au bon arrêt ?", example_en="Did you get off at the right stop?"),
    verb("devenir", "to become", [], aux="être", pp="devenu",
         present="deviens deviens devient devenons devenez deviennent", fut="deviendr",
         example="Il veut devenir médecin.", example_en="He wants to become a doctor."),
    verb("revenir", "to come back", [], aux="être", pp="revenu",
         present="reviens reviens revient revenons revenez reviennent", fut="reviendr",
         example="Je reviens tout de suite.", example_en="I'll be right back."),
    verb("naître", "to be born", [], aux="être", pp="né",
         present="nais nais naît naissons naissez naissent", fut="naîtr",
         example="Je suis né en 1990.", example_en="I was born in 1990."),
    verb("mourir", "to die", [], aux="être", pp="mort",
         present="meurs meurs meurt mourons mourez meurent", fut="mourr",
         example="Je meurs de faim !", example_en="I'm starving! (I'm dying of hunger)"),
    verb("ouvrir", "to open", [], pp="ouvert",
         present="ouvre ouvres ouvre ouvrons ouvrez ouvrent",
         example="Tu peux ouvrir la fenêtre ?", example_en="Can you open the window?"),
    verb("fermer", "to close", [], pp="fermé",
         example="Le magasin ferme à sept heures.", example_en="The shop closes at seven."),
    verb("connaître", "to know (a person, a place)", [], pp="connu",
         present="connais connais connaît connaissons connaissez connaissent", fut="connaîtr",
         example="J'ai connu Marie à l'université.", example_en="I got to know Marie at university."),
    verb("croire", "to believe", [], pp="cru",
         present="crois crois croit croyons croyez croient",
         example="Je n'ai pas cru son histoire.", example_en="I didn't believe his story."),
    verb("recevoir", "to receive", [], pp="reçu",
         present="reçois reçois reçoit recevons recevez reçoivent", fut="recevr",
         example="J'ai reçu ton message.", example_en="I got your message."),
    verb("envoyer", "to send", [], pp="envoyé",
         present="envoie envoies envoie envoyons envoyez envoient", fut="enverr",
         example="Tu as envoyé la photo à Paul ?", example_en="Did you send the photo to Paul?"),
    verb("payer", "to pay (for)", ["shopping"], pp="payé",
         present="paie paies paie payons payez paient", fut="paier",
         example="Nous avons payé l'addition.", example_en="We paid the bill."),
    verb("essayer", "to try; to try on", ["clothing"], pp="essayé",
         present="essaie essaies essaie essayons essayez essaient", fut="essaier",
         example="Elle a essayé la robe rouge.", example_en="She tried on the red dress."),
    verb("oublier", "to forget", [], pp="oublié",
         example="J'ai oublié mon parapluie.", example_en="I forgot my umbrella."),
    verb("porter", "to wear; to carry", ["clothing"], pp="porté",
         example="Il porte un chapeau.", example_en="He's wearing a hat."),
    verb("perdre", "to lose", [], pp="perdu",
         example="J'ai perdu mon portefeuille.", example_en="I've lost my wallet."),
    verb("répondre", "to answer", [], pp="répondu",
         example="Réponds au téléphone !", example_en="Answer the phone!"),
    verb("entendre", "to hear", [], pp="entendu",
         example="Tu entends ce bruit ?", example_en="Can you hear that noise?"),
    verb("courir", "to run", ["leisure"], pp="couru",
         present="cours cours court courons courez courent", fut="courr",
         example="Je cours tous les matins.", example_en="I run every morning."),
    verb("conduire", "to drive", ["transport"], pp="conduit",
         present="conduis conduis conduit conduisons conduisez conduisent",
         example="Tu sais conduire ?", example_en="Can you drive?"),
    verb("vivre", "to live (be alive, live a life)", [], pp="vécu",
         present="vis vis vit vivons vivez vivent",
         example="On ne vit qu'une fois.", example_en="You only live once."),
    verb("préférer", "to prefer", [], pp="préféré",
         present="préfère préfères préfère préférons préférez préfèrent",
         example="Je préfère le thé.", example_en="I prefer tea."),
    verb("appeler", "to call", [], pp="appelé",
         present="appelle appelles appelle appelons appelez appellent", fut="appeller",
         example="Je t'appelle ce soir.", example_en="I'll call you tonight."),
    verb("demander", "to ask", [], pp="demandé",
         example="Je vais demander le chemin.", example_en="I'll ask the way."),
    verb("laisser", "to leave (something); to let", [], pp="laissé",
         example="Laisse-moi tranquille !", example_en="Leave me alone!"),
    verb("rendre", "to give back", [], pp="rendu",
         example="Je te rends ton livre demain.", example_en="I'll give you your book back tomorrow."),
    verb("pleurer", "to cry", ["feelings"], pp="pleuré",
         example="Pourquoi tu pleures ?", example_en="Why are you crying?"),
]

PHRASES = phrases(
    """
il fait beau | the weather is nice | it makes beautiful
il fait froid | it's cold (weather)
il pleut | it's raining
je voudrais... | I would like...
je suis en train de... | I'm in the middle of (doing)... | I am in the process of
ça dépend | it depends
pas de problème | no problem
bien sûr | of course | well sure
peut-être | maybe | can be
j'ai mal à la tête | I have a headache | I have hurt at the head
ça ne fait rien | never mind, it doesn't matter | that makes nothing
je m'en fiche | I don't care (informal)
c'est pas grave | it's no big deal | it's not serious
à tout à l'heure | see you later (today)
ça te dit ? | do you fancy it? | does that say to you?
volontiers | gladly, I'd love to
tant pis | too bad, oh well | so much the worse
tant mieux | so much the better, good
quoi de neuf ? | what's new?
on y va ? | shall we go? | we there go?
je n'en peux plus | I can't take any more | I can no more of it
il vaut mieux... | it's better to... | it is worth better
avoir besoin de | to need | to have need of
avoir envie de | to feel like, to want | to have desire of
avoir l'air | to seem, to look | to have the air
faire la queue | to queue | to make the tail
faire les courses | to do the shopping | to make the runs
"""
    ,
    ["expressions"],
)

CONNECTIVES = connectors(
    "connective",
    """
alors | so, then | conn-consequence | Il pleut, alors on reste à la maison. | It's raining, so we're staying in.
par conséquent | consequently | conn-consequence | Le train est en retard ; par conséquent, nous arriverons à midi. | The train is late; consequently, we'll arrive at noon.
pourtant | yet, and yet | conn-contrast | Il est riche ; pourtant, il n'est pas heureux. | He's rich, and yet he isn't happy.
en revanche | on the other hand | conn-contrast | Le logement est cher ; en revanche, la nourriture est bon marché. | Housing is expensive; food, on the other hand, is cheap.
en plus | on top of that | conn-addition | Il est en retard, et en plus il a oublié les clés. | He's late, and on top of that he forgot the keys.
enfin | finally, at last | conn-sequence | Enfin, nous sommes arrivés. | At last, we arrived.
après | afterwards | conn-sequence | On mange d'abord, et on sort après. | We eat first, and go out afterwards.
""",
    ["connecteurs"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
car | for, because (written) | conj-coordinating | Je reste ici, car il pleut. | I'm staying here, for it's raining.
comme | as, since (at the start) | conj-subordinating | Comme il pleut, on reste ici. | As it's raining, we're staying here.
pendant que | while | conj-subordinating | Il cuisine pendant que je travaille. | He cooks while I work.
lorsque | when (formal) | conj-subordinating | Lorsque je suis arrivé, il dormait. | When I arrived, he was asleep.
""",
    ["conjonctions"],
)

# Items learned together land together: routine verbs with clothing words, etc.
ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# fr-passe-compose and fr-etre-verbs share the "passé-composé" tag, so does
# fr-imparfait's family of verbs pull from the same présent-tagged pool: each
# grammar page's Unit gets its own hand-picked slice instead of one mechanical
# group per tag. fr-etre-verbs's words are literally the DR MRS VANDERTRAMP
# être-verbs the page teaches. "Sentiments" pulls the character/emotion
# adjectives out of the general adjectifs pool the way "Les couleurs" did in
# Fondations, since they share the same first tag as every other adjective.
UNITS = [
    {
        "title": "Le passé composé",
        "page_id": "fr-passe-compose",
        "word_ids": ["connaitre", "croire", "recevoir", "envoyer", "payer", "essayer"],
    },
    {
        "title": "Les verbes avec être",
        "page_id": "fr-etre-verbs",
        "word_ids": ["rester", "tomber", "entrer", "rentrer", "monter", "descendre", "devenir", "revenir", "naitre", "mourir"],
    },
    {
        "title": "L'imparfait",
        "page_id": "fr-imparfait",
        "word_ids": ["oublier", "porter", "perdre", "repondre", "entendre", "courir"],
    },
    {
        "title": "Les verbes pronominaux",
        "page_id": "fr-reflexive-verbs",
        "word_ids": ["se-lever", "se-reveiller", "s-habiller", "se-coucher", "se-promener", "se-sentir"],
    },
    {
        "title": "Les pronoms objets",
        "page_id": "fr-object-pronouns",
        "word_ids": ["je-m-en-fiche", "ca-te-dit", "on-y-va", "je-n-en-peux-plus", "ca-depend", "il-vaut-mieux"],
    },
    {
        "title": "Le futur simple",
        "page_id": "fr-futur-simple",
        "word_ids": ["ouvrir", "fermer", "conduire", "vivre", "preferer", "appeler", "demander", "laisser", "rendre", "pleurer"],
    },
    {
        "title": "Les comparaisons",
        "page_id": "fr-comparisons",
        "word_ids": ["long", "court", "lourd", "leger", "rapide", "lent"],
    },
    {
        "title": "Sentiments",
        "word_ids": ["heureux", "triste", "fache", "calme", "sympa", "drole", "serieux", "timide", "paresseux", "sportif"],
    },
    {
        "title": "Depuis, il y a, pendant",
        "page_id": "fr-time-expressions",
        "word_ids": ["examen", "cours", "reunion", "rendez-vous", "apres", "enfin"],
    },
    {
        "title": "Le genre des noms",
        "page_id": "fr-gender-patterns",
        "word_ids": ["voyage", "plage", "ordinateur", "fourchette", "medicament", "photo"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "home": "La maison",
    "transport": "Les transports",
}

PACK = pack(
    "fr-everyday-v1",
    8,
    "fr",
    "Français · Au quotidien (A2)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Pratique"),
)
