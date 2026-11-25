"""es-foundations-v1: A1. The grammar that blocks a beginner first, and the words
needed to talk about yourself, your family, your day and your food."""

from common import build_units, interleave, page, pack, topic, topic_labels
from es_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("pronunciación", "Pronunciación", "pronunciation", []),
    topic("pronombres", "Pronombres", "pronouns", ["presente"]),
    topic("preguntas", "Preguntas", "asking questions", ["presente"]),
    topic("números", "Números", "numbers", []),
    topic("family", "Familia", "family", ["género"]),
    topic("body", "Cuerpo", "body", ["género"]),
    topic("city", "Ciudad", "city and places", ["género"]),
    topic("greetings", "Saludos", "greetings and politeness", []),
    topic("colors", "Colores", "colours", ["adjetivos"]),
]

PAGES = [
    page(
        "es-pronunciation",
        "Reading Spanish aloud",
        r"""
Spanish is spelled the way it sounds. Learn a handful of rules and you can read any word aloud, even one you've never seen.

## Five pure vowels

Spanish has five vowel sounds, always short and clear. They never glide the way English "o" does in "go", and an unstressed vowel keeps its full sound.

| Letter | Sound | Example |
| --- | --- | --- |
| a | "ah", as in *father* | *[casa](lango:say)* |
| e | "eh", as in *bed* | *[mesa](lango:say)* |
| i | "ee", as in *see* | *[libro](lango:say)* |
| o | "oh", short | *[ojo](lango:say)* |
| u | "oo", as in *food* | *[uno](lango:say)* |

*[Chocolate](lango:say)* has four clear vowels: cho-co-la-te.

## Consonants that differ from English

- **h** is always silent: *[hola](lango:say)*, *[hermano](lango:say)*, *[ahora](lango:say)*.
- **j**, and **g** before e or i, is a rasp in the throat, like the *ch* in Scottish *loch*: *[rojo](lango:say)*, *[gente](lango:say)*.
- **g** before a, o or u is hard, as in *go*: *[gato](lango:say)*. To keep it hard before e or i, Spanish writes **gu**, and the u is silent: *[guitarra](lango:say)*.
- **c** before a, o or u, and **qu** before e or i, is a plain k: *[casa](lango:say)*, *[queso](lango:say)*, *[aquí](lango:say)*.
- **c** before e or i, and **z** everywhere, is the *th* of *think* in most of Spain: *[cerveza](lango:say)*, *[cine](lango:say)*. In Latin America, the Canary Islands and much of Andalusia it's an s. Both are correct.
- **ll** and **y** sound like the *y* in *yes* for most speakers: *[llave](lango:say)*, *[calle](lango:say)*, *[yo](lango:say)*. In Argentina and Uruguay they sound closer to *sh*.
- **ñ** is the *ny* in *canyon*: *[España](lango:say)*, *[mañana](lango:say)*.
- **r** between vowels is one quick tap of the tongue, like the *tt* in American *butter*. **rr**, and an r at the start of a word, is rolled: *[pero](lango:say)* (but) and *[perro](lango:say)* (dog) are different words.
- **b** and **v** are the same sound: *[vino](lango:say)* and *[bien](lango:say)* start alike.
- **d** between vowels is soft, like the *th* in *this*, and almost disappears at the end of a word: *[nada](lango:say)*, *[Madrid](lango:say)*.

## Which syllable is stressed

Three rules cover every word:

1. A word ending in a vowel, **-n** or **-s** stresses the second-to-last syllable: *[casa](lango:say)*, *[hablan](lango:say)*, *[lunes](lango:say)*.
2. A word ending in any other consonant stresses the last syllable: *[hablar](lango:say)*, *[ciudad](lango:say)*, *[español](lango:say)*.
3. A written accent breaks the rules and marks the stress: *[café](lango:say)*, *[árbol](lango:say)*, *[música](lango:say)*, *[canción](lango:say)*.

So a written accent is never decoration. *[Papá](lango:say)* (dad) and *[papa](lango:say)* (the pope) differ only in their stress.

## Accents that tell twins apart

A few short words carry an accent only to tell them from a twin that sounds the same:

| With an accent | Without |
| --- | --- |
| tú (you) | tu (your) |
| él (he) | el (the) |
| sí (yes) | si (if) |
| mí (me) | mi (my) |
| sé (I know) | se (oneself) |
| té (tea) | te (you, to you) |

Question words always take one: *qué*, *cómo*, *dónde*, *cuándo*.

## Upside-down marks

A question opens with **¿** and an exclamation with **¡**, so you know the tone before you read it: *¿Hablas español?* *¡Qué bonito!*

## This unit's words

- *[hola](lango:say)*: the **h** is silent, so the word starts on the **o**: "OH-lah".
- *[buenos días](lango:say)*: **ue** glides like the *we* in *wet*, and the accent keeps the **í** and the **a** apart: "BWEH-nohs DEE-ahs".
- *[gracias](lango:say)*: a tapped **r**, and **c** before **i** is the *th* of *think* in Spain, an s in Latin America: "GRAH-thyahs" or "GRAH-syahs".
- *[por favor](lango:say)*: *favor* ends in a consonant, so the stress goes on its last syllable, and the **v** is a soft b: "por fah-BOR".
- *[perdón](lango:say)*: the written accent moves the stress to the end: "pair-DOHN".
- *[encantado](lango:say)*: four clear vowels, and the **d** between vowels is soft, like the *th* in *this*: "en-kahn-TAH-doh".
""",
        ["pronunciación"],
        "es-pronunciation",
        explains=["pronunciación"],
    ),
    page(
        "es-subject-pronouns",
        "Yo, tú, usted and vosotros",
        r"""
Spanish has four words for "you". Which one you pick depends on how many people you're talking to, how well you know them, and which side of the Atlantic you're on.

| Person | Pronoun | English |
| --- | --- | --- |
| 1st singular | yo | I |
| 2nd singular | tú | you (one person, familiar) |
| | usted | you (one person, polite) |
| 3rd singular | él / ella | he / she |
| 1st plural | nosotros / nosotras | we |
| 2nd plural | vosotros / vosotras | you (several, familiar, Spain only) |
| | ustedes | you (several, polite; any group in Latin America) |
| 3rd plural | ellos / ellas | they |

## Usually left out

The verb ending already says who is doing it, so Spanish drops the pronoun most of the time: *Hablo español*, not *yo hablo español*. Put it in to stress or contrast: *Yo trabajo y tú descansas.* (I work and you rest.)

"It" as a subject has no word at all: *Es tarde* (It's late), *Llueve* (It's raining).

## Tú or usted?

**Usted** takes the verb form of *él* and *ella*: *¿Cómo está usted?* It comes from an old title, *vuestra merced* (your grace), which is why it takes the third-person verb. In writing it's shortened to *Ud.* or *Vd.*

Spain uses *tú* widely: with friends, colleagues, people of your own age and often shop staff. Keep *usted* for older people, officials and formal settings. When in doubt, start with *usted* and let the other person offer *tú*: *Puedes tutearme* (You can call me tú).

## Vosotros or ustedes?

In Spain, **vosotros** is a group of people you'd each call *tú*, and **ustedes** a group you'd each call *usted*. In Latin America *vosotros* isn't used: *ustedes* is for any group, friends and children included. *Ustedes* takes the verb form of *ellos*: *¿Ustedes son de aquí?*

## Vos

In Argentina, Uruguay and much of Central America, **vos** replaces *tú* and has its own verb forms: *vos hablás*, *vos tenés*, *vos sos*. You'll hear it in films and songs. This course teaches the *tú* forms of Spain, which every Spanish speaker understands.

## Women only

*Nosotras*, *vosotras* and *ellas* are for groups made up only of women. A group with even one man in it takes the masculine: Ana and Pedro are *ellos*.

:::examples
- Somos de Valencia. — We're from Valencia.
- ¿Usted es el señor García? — Are you Mr García?
- ¿Vosotros venís a la fiesta? — Are you all coming to the party?
- Ellas viven en Bilbao. — They live in Bilbao.
:::

:::sort{groups="Tú (a friend): perdona, ¿cómo estás?, ¿de dónde eres? | Usted (a stranger): disculpe, ¿cómo está usted?, ¿puede repetir?"}
:::
""",
        ["pronombres"],
        "es-subject-pronouns",
        explains=["pronombres"],
    ),
    page(
        "es-ser-estar",
        "Ser, estar and hay",
        r"""
English has one verb "to be". Spanish has two, **ser** and **estar**, and choosing between them is the first big decision a learner makes.

| | ser | estar |
| --- | --- | --- |
| yo | soy | estoy |
| tú | eres | estás |
| él, ella, usted | es | está |
| nosotros | somos | estamos |
| vosotros | sois | estáis |
| ellos, ellas, ustedes | son | están |

## Ser: what something is

Use **ser** for identity, origin, jobs, nationality, character, what something is made of, the time and the date:

- *Soy Ana. Soy de Sevilla.* (I'm Ana. I'm from Seville.)
- *Es enfermera.* (She's a nurse.) No *una* before the job.
- *Mi hermano es muy simpático.* (My brother is very nice.)
- *Son las tres. Hoy es lunes.* (It's three o'clock. Today is Monday.)

## Estar: where and how something is

Use **estar** for where people and things are, and for states that can change, such as moods, health and how food tastes today:

- *Madrid está en el centro de España.* (Madrid is in the centre of Spain.)
- *Estoy cansado. ¿Cómo estás?* (I'm tired. How are you?)
- *La sopa está fría.* (The soup is cold.)

Place always takes *estar*, even for a city that won't move. The one exception is an event: *La fiesta es en mi casa* (The party is at my place), because an event "takes place".

## One adjective, two meanings

The verb can change what an adjective means: *Juan es aburrido* (Juan is boring), but *Juan está aburrido* (Juan is bored). The B1 pack has more of these pairs.

## Hay: there is, there are

**Hay**, a form of *haber*, says that something exists. It has one form for singular and plural:

- *Hay un banco en la plaza.* (There's a bank in the square.)
- *Hay dos hoteles cerca.* (There are two hotels nearby.)

*Hay* goes with *un*, *una*, a number or no article. Once you say *el* or *la*, you're asking where a known thing is, and that takes *estar*: *¿Hay una farmacia por aquí?* (Is there a pharmacy around here?), but *¿Dónde está la farmacia?* (Where's the pharmacy?)

## Tener where English says "be"

Age, hunger, thirst, heat and cold take **tener** (to have): *Tengo veinte años* (I'm twenty), *Tengo hambre* (I'm hungry), *Tengo frío* (I'm cold).

:::examples
- Soy de Valencia, pero vivo en Madrid. — I'm from Valencia, but I live in Madrid.
- La farmacia está al lado del banco. — The pharmacy is next to the bank.
- Hay dos camas en la habitación. — There are two beds in the room.
- Estamos muy contentos con el piso. — We're very happy with the flat.
:::

:::cloze{sentence="Mis padres ___ en Málaga de vacaciones." blank="están"}
:::

:::cloze{sentence="Mi madre ___ profesora de inglés." blank="es"}
:::
""",
        ["presente"],
        "es-ser-estar",
    ),
    page(
        "es-present-tense",
        "The present: -ar, -er and -ir",
        r"""
Every Spanish infinitive ends in **-ar**, **-er** or **-ir**. Take off those two letters and add the ending for the person.

| | hablar | comer | vivir |
| --- | --- | --- | --- |
| yo | hablo | como | vivo |
| tú | hablas | comes | vives |
| él, ella, usted | habla | come | vive |
| nosotros | hablamos | comemos | vivimos |
| vosotros | habláis | coméis | vivís |
| ellos, ellas, ustedes | hablan | comen | viven |

*-Er* and *-ir* verbs share every ending except the nosotros and vosotros forms.

:::examples
- Vivo en un piso pequeño en el centro. — I live in a small flat in the centre.
- ¿Trabajas los sábados? — Do you work on Saturdays?
- Mis hijos juegan en el parque. — My children are playing in the park.
- Empezamos a las nueve. — We start at nine.
:::

## Stem-changing verbs

In many common verbs the last vowel of the stem changes when the stress falls on it. That's every form except nosotros and vosotros, so the verb makes a "boot" shape in the table.

| Change | Verb | Forms |
| --- | --- | --- |
| e → ie | querer | quiero, quieres, quiere, queremos, queréis, quieren |
| o → ue | poder | puedo, puedes, puede, podemos, podéis, pueden |
| e → i | pedir | pido, pides, pide, pedimos, pedís, piden |
| u → ue | jugar | juego, juegas, juega, jugamos, jugáis, juegan |

You can't tell from the infinitive. Dictionaries mark these verbs: *pensar (ie)*, *empezar (ie)*, *entender (ie)*, *volver (ue)*, *dormir (ue)*, *pedir (i)*. *Jugar* is the only u → ue verb.

## Irregular yo forms

Some verbs are regular except in the yo form:

| Verb | yo | Verb | yo |
| --- | --- | --- | --- |
| hacer | hago | poner | pongo |
| salir | salgo | conocer | conozco |
| saber | sé | dar | doy |
| ver | veo | traer | traigo |

*Tener*, *venir* and *decir* add a stem change on top: *tengo, tienes*; *vengo, vienes*; *digo, dices*.

## One tense for three English ones

*Como* is "I eat", "I'm eating" and "I do eat". Spanish also uses the present for plans: *Mañana trabajo* (I'm working tomorrow). And where English asks "Shall I...?", Spanish asks in the present: *¿Abro la ventana?* (Shall I open the window?)

:::predict{prompt="nosotros (escribir)" answer="escribimos"}
:::

:::predict{prompt="ellos (dormir)" answer="duermen"}
:::
""",
        ["presente"],
        "es-present-tense",
        explains=["presente"],
    ),
    page(
        "es-negation",
        "Saying no: no, nunca and nada",
        r"""
To make a sentence negative, put **no** straight before the verb. There's no helper verb like English "don't".

:::examples
- No hablo alemán. — I don't speak German.
- No tengo nada en la nevera. — There's nothing in my fridge.
- Nunca comemos en casa los domingos. — We never eat at home on Sundays.
- Aquí no hay nadie. — There's nobody here.
:::

If the verb has object pronouns in front of it, *no* goes before them: *No lo sé* (I don't know).

## Other negative words

| Spanish | English | Example |
| --- | --- | --- |
| nunca | never | Nunca bebo café. |
| nada | nothing | No veo nada. |
| nadie | nobody | No viene nadie. |
| tampoco | not ... either | Yo tampoco. |
| todavía no | not yet | Todavía no tengo coche. |
| ningún, ninguna | no, not a single | No tengo ningún problema. |
| ni ... ni | neither ... nor | No como ni carne ni pescado. |

## Double negatives are correct

In Spanish, two negatives don't cancel out. When the negative word comes after the verb, *no* must still come before it: *No veo nada* (literally "I don't see nothing"). When the negative word comes first, drop the *no*: *Nadie viene*, *Nunca bebo café*.

## Answering a question

A short answer often says *no* twice. The first answers the question; the second negates the verb: *—¿Tienes coche? —No, no tengo.* To refuse politely, say *No, gracias*.

:::cloze{sentence="No conozco a ___ en esta ciudad." blank="nadie"}
:::
""",
        ["negación"],
        "es-negation",
        explains=["negación"],
    ),
    page(
        "es-questions",
        "Asking questions",
        r"""
A written question opens with **¿** and closes with **?**. The marks sit around the question itself, which may be only part of the sentence: *Y tú, ¿de dónde eres?*

## Yes-or-no questions

The easiest way is to say a statement with your voice rising at the end: *¿Hablas inglés?* (Do you speak English?) You can also put the subject after the verb: *¿Habla usted inglés?*, *¿Viene tu hermano?* Spanish has no helper like English "do".

## Question words

Every question word carries a written accent.

| Spanish | English |
| --- | --- |
| qué | what |
| quién, quiénes | who |
| dónde | where |
| adónde | where to |
| cuándo | when |
| cómo | how |
| cuánto, cuánta | how much |
| cuántos, cuántas | how many |
| cuál, cuáles | which, what |
| por qué | why |

The question word comes first, then the verb, then the subject: *¿Dónde vive tu hermana?* (Where does your sister live?)

A preposition goes before the question word, never at the end as in English: *¿Con quién vives?* (Who do you live with?), *¿De dónde eres?* (Where are you from?)

*Cuánto* agrees with the noun it counts: *¿Cuántas hermanas tienes?*

## Qué or cuál?

Both can mean "what". Before a noun, use **qué**: *¿Qué libro lees?* Before *ser*, **cuál** asks you to pick one answer from many: *¿Cuál es tu número de teléfono?* *¿Qué es...?* asks for a definition: *¿Qué es el gazpacho?* (What is gazpacho?)

## The accent stays in a hidden question

A question inside a statement keeps its accent: *No sé dónde vive* (I don't know where she lives). Without the accent the same words are connectors: *donde* (where, in a place), *cuando* (when), *como* (as, like), *que* (that), *porque* (because).

:::examples
- ¿Dónde está la estación? — Where's the station?
- ¿Cuántos años tienes? — How old are you?
- ¿Con quién vives? — Who do you live with?
- ¿Cuál es tu película favorita? — What's your favourite film?
:::

:::cloze{sentence="¿___ es tu cumpleaños? —El 3 de mayo." blank="Cuándo"}
:::
""",
        ["preguntas"],
        "es-questions",
        explains=["preguntas"],
    ),
    page(
        "es-gustar",
        "Me gusta: liking things",
        r"""
Spanish doesn't say "I like coffee". It says "coffee pleases me": *Me gusta el café*. The thing you like is the subject of the verb, and the person who likes it is an indirect object pronoun.

| Spanish | English |
| --- | --- |
| me gusta | I like |
| te gusta | you like |
| le gusta | he, she likes; you (usted) like |
| nos gusta | we like |
| os gusta | you (vosotros) like |
| les gusta | they like; you (ustedes) like |

## Gusta or gustan?

The verb agrees with the thing liked, not with the person:

- *Me gusta el chocolate.* One thing: *gusta*.
- *Me gustan las fresas.* Several things: *gustan*.
- *Me gusta bailar.* An activity is always singular, even two of them: *Me gusta leer y cocinar.*

The thing liked takes an article where English has none: *Me gusta el café*, never *me gusta café*.

## A mí, a ti, a Juan

To stress the person, or to say who *le* and *les* are, add *a* + a pronoun or a name: *A mí me gusta, ¿y a ti?* With a name the *le* stays: *A Juan le gusta el fútbol.* That's how you agree or disagree in a reply: *—Me gusta el jazz. —A mí también.* or *—A mí no.*

## Other verbs that work the same way

- **encantar**, to love (a thing): *Me encanta Madrid.*
- **interesar**, to interest: *¿Te interesa la historia?*
- **doler**, to hurt: *Me duelen los pies.* (My feet hurt.)
- **apetecer**, to feel like (Spain): *¿Te apetece un café?*

## Careful with people

*Me gustas* means "I fancy you". For family and friends, say *te quiero* (I love you) or *me cae bien* (I like him, her).

:::examples
- Me gusta mucho el pescado. — I really like fish.
- ¿Te gustan los perros? — Do you like dogs?
- A mi madre le encanta bailar. — My mother loves dancing.
:::

:::cloze{sentence="A mis hijos no les ___ las verduras." blank="gustan"}
:::
""",
        ["presente"],
        "es-gustar",
    ),
    page(
        "es-adjectives",
        "Adjectives agree",
        r"""
A Spanish adjective matches its noun in gender and number, and it usually comes after the noun: *un coche rojo*, *una casa blanca*, *unos zapatos negros*.

| Ending | masculine | feminine |
| --- | --- | --- |
| -o | alto, altos | alta, altas |
| -e | grande, grandes | grande, grandes |
| consonant | azul, azules; fácil, fáciles | the same (but -or adds -a: trabajadora) |
| nationality | español, españoles | española, españolas |

Nationality adjectives that end in a consonant add **-a** for the feminine: *inglés, inglesa*; *alemán, alemana*. Like days and months, they take no capital letter.

A group of mixed gender takes the masculine plural: *Juan y María son altos.*

## Before the noun

A few short, common adjectives can come before the noun, and some change there:

- **bueno** and **malo** drop their -o before a masculine singular noun: *un buen día*, *un mal momento*, but *una buena idea*.
- **grande** becomes **gran** before any singular noun and then means "great": *un gran amigo*, *una gran ciudad*. After the noun it means "big": *una ciudad grande*.

## Muy and mucho

**Muy** (very) goes before an adjective and never changes: *muy alta*, *muy caros*. **Mucho** (a lot of, many) goes with a noun and agrees: *mucha gente*, *muchos libros*.

:::examples
- Tengo un perro negro y una gata blanca. — I have a black dog and a white cat.
- Las manzanas son muy baratas aquí. — Apples are very cheap here.
- Es un buen restaurante. — It's a good restaurant.
- Mis abuelos son muy simpáticos. — My grandparents are very nice.
:::

:::cloze{sentence="Mis hermanas son muy ___ (alto)." blank="altas"}
:::
""",
        ["adjetivos"],
        "es-adjectives",
        explains=["adjetivos"],
    ),
    page(
        "es-colors",
        "Colours: which ones agree",
        r"""
Colours are adjectives, so they follow the adjectives page: they go after the noun and agree with it. *Un coche rojo*, *una casa roja*, *unos zapatos rojos*.

## Colours ending in -o have four forms

| masculine | feminine | masculine plural | feminine plural |
| --- | --- | --- | --- |
| rojo | roja | rojos | rojas |
| amarillo | amarilla | amarillos | amarillas |
| negro | negra | negros | negras |
| blanco | blanca | blancos | blancas |
| morado | morada | morados | moradas |

## The others only change for the plural

A colour ending in **-e** or a consonant is the same for masculine and feminine. In the plural it adds **-s** after a vowel and **-es** after a consonant.

| singular | plural |
| --- | --- |
| verde | verdes |
| azul | azules |
| gris | grises |
| marrón | marrones |

*Marrón* loses its accent in the plural, because *marrones* already stresses the right syllable.

## Rosa and naranja

*Rosa* (a rose) and *naranja* (an orange) are named after things, so they don't change for gender: *un jersey rosa*, *una camiseta naranja*. In the plural you'll hear both *unas flores rosa* and *unas flores rosas*, and both are correct.

A colour of two words never changes: *unos ojos azul claro*, *una falda verde oscuro*.

:::examples
- Mi hermana tiene los ojos verdes. — My sister has green eyes.
- Quiero las zapatillas negras. — I want the black trainers.
- Las paredes de mi cuarto son azules. — My bedroom walls are blue.
- Lleva una camiseta rosa. — She's wearing a pink T-shirt.
:::
""",
        ["colors"],
        "es-colors",
        explains=["colors"],
    ),
    page(
        "es-numbers",
        "Numbers, the time and the date",
        r"""
## 0 to 29

| | | | |
| --- | --- | --- | --- |
| 0 cero | 1 uno | 2 dos | 3 tres |
| 4 cuatro | 5 cinco | 6 seis | 7 siete |
| 8 ocho | 9 nueve | 10 diez | 11 once |
| 12 doce | 13 trece | 14 catorce | 15 quince |
| 16 dieciséis | 17 diecisiete | 18 dieciocho | 19 diecinueve |
| 20 veinte | 21 veintiuno | 22 veintidós | 26 veintiséis |

From 16 to 29 the numbers are written as one word.

## 30 and up

From 31, tens and units are joined by **y**: *treinta y uno*, *cuarenta y dos*, *noventa y nueve*. The tens are *treinta*, *cuarenta*, *cincuenta*, *sesenta*, *setenta*, *ochenta*, *noventa*.

**Cien** is exactly 100; above it, **ciento**: *ciento veinte*. The hundreds agree with the noun: *doscientos euros*, *doscientas personas*. Three are irregular: *quinientos* (500), *setecientos* (700), *novecientos* (900). **Mil** is 1,000 and never takes *un*: *mil euros*, *dos mil*.

**Uno** becomes **un** before a masculine noun and **una** before a feminine one: *un libro*, *veintiún años*, *una casa*.

Spain writes a decimal comma and a thousands point: *3,5* is three and a half, *1.500* is fifteen hundred.

## Telling the time

*¿Qué hora es?* (What time is it?) One o'clock is singular, every other hour plural:

- *Es la una.* (It's one o'clock.)
- *Son las dos.* (It's two o'clock.)
- *Son las tres y cuarto.* (It's quarter past three.)
- *Son las cinco menos cuarto.* (It's quarter to five.)
- *Son las siete y veinte.* (It's twenty past seven.)

"At" is **a**: *a las nueve*. Add *de la mañana*, *de la tarde* or *de la noche* for a.m. and p.m. Timetables use the 24-hour clock: *a las 21:15*.

## Days, months and dates

Days and months take no capital letter. Before a day, use *el* instead of "on": *el lunes* (on Monday), *los lunes* (on Mondays).

The months are *enero*, *febrero*, *marzo*, *abril*, *mayo*, *junio*, *julio*, *agosto*, *septiembre*, *octubre*, *noviembre* and *diciembre*. A date is *el* + number + *de* + month: *el 5 de mayo*. For the first of the month, Spain says *el uno*, and Latin America *el primero*.

:::examples
- Tengo veintiún años. — I'm twenty-one.
- El tren sale a las nueve y media. — The train leaves at half past nine.
- Mi cumpleaños es el 12 de octubre. — My birthday is on the 12th of October.
:::

:::cloze{sentence="La película empieza a las diez y ___, a las 22:30." blank="media"}
:::
""",
        ["números"],
        "es-numbers",
        explains=["números"],
    ),
    page(
        "es-ir-a",
        "Ir a: the near future",
        r"""
The easiest way to talk about the future is **ir a** + infinitive, just like English "going to".

| | ir | + a + infinitive |
| --- | --- | --- |
| yo | voy | a comer |
| tú | vas | a salir |
| él, ella, usted | va | a llover |
| nosotros | vamos | a ver |
| vosotros | vais | a jugar |
| ellos, ellas, ustedes | van | a estudiar |

*Voy a estudiar* (I'm going to study) is the everyday future in speech, on both sides of the Atlantic. The future tense proper comes in the A2 pack.

*Vamos a* also means "let's": *¡Vamos a comer!* (Let's eat!)

## More verbs that take an infinitive

| Spanish | English | Example |
| --- | --- | --- |
| tener que | to have to | Tengo que trabajar mañana. |
| hay que | one has to, you need to | Hay que comprar pan. |
| querer | to want to | Quiero aprender a nadar. |
| poder | can | ¿Puedes venir? |
| acabar de | to have just | Acabo de llegar. |
| empezar a | to start to | Empieza a llover. |
| volver a | to do again | Vuelvo a llamar. |

*Hay que* has no person: it says what needs doing, by anyone.

## Time words for the future

*Mañana* (tomorrow), *pasado mañana* (the day after tomorrow), *esta tarde* (this afternoon), *esta noche* (tonight), *el lunes* (on Monday), *la semana que viene* (next week), *el año que viene* (next year).

:::examples
- Voy a llamar a mi madre esta tarde. — I'm going to call my mother this afternoon.
- ¿Qué vais a hacer el sábado? — What are you all going to do on Saturday?
- Tengo que trabajar mañana. — I have to work tomorrow.
- Acabo de llegar a casa. — I've just got home.
:::

:::cloze{sentence="Esta noche mi hermano y yo ___ a cenar en casa de mis abuelos." blank="vamos"}
:::
""",
        ["presente"],
        "es-ir-a",
    ),
    page(
        "es-possessives",
        "Mi, tu, su; este, ese, aquel",
        r"""
## Possessives

| Owner | one thing | several things |
| --- | --- | --- |
| yo | mi | mis |
| tú | tu | tus |
| él, ella, usted | su | sus |
| nosotros | nuestro, nuestra | nuestros, nuestras |
| vosotros | vuestro, vuestra | vuestros, vuestras |
| ellos, ellas, ustedes | su | sus |

A possessive agrees with the thing owned, never with the owner: a woman's son is *su hijo*, and a man's house is *su casa*. Only *nuestro* and *vuestro* have a feminine form: *nuestra casa*, *nuestros hijos*.

**Su** can mean his, her, its, your (usted) or their. When that's unclear, say *de* + the person: *la casa de ella*, *el coche de usted*.

Spanish has no 's. Use *de*: *el coche de Pedro* (Pedro's car), *la madre de mi novio* (my boyfriend's mother).

After *ser*, or after a noun, the long forms take over: *mío*, *tuyo*, *suyo*, *nuestro*, *vuestro*, *suyo*, each with -a, -os and -as. *¿Es tuyo?* (Is it yours?), *un amigo mío* (a friend of mine).

For parts of the body and clothes, Spanish uses *el* or *la* where English says "my": *Abre los ojos* (Open your eyes).

## This, that and that over there

Spanish has three distances: near me, near you, and away from both of us.

| | near me | near you | over there |
| --- | --- | --- | --- |
| masculine | este | ese | aquel |
| feminine | esta | esa | aquella |
| masculine plural | estos | esos | aquellos |
| feminine plural | estas | esas | aquellas |

For something unknown, or an idea, use the neuter forms **esto**, **eso** and **aquello**: *¿Qué es esto?* (What's this?), *Eso es verdad* (That's true).

:::examples
- Mi hermana vive con su novio. — My sister lives with her boyfriend.
- ¿Es este tu móvil? — Is this your phone?
- Aquella casa es de mis tíos. — That house over there belongs to my aunt and uncle.
:::

:::cloze{sentence="Nosotros vivimos con ___ abuela." blank="nuestra"}
:::
""",
        ["artículos"],
        "es-possessives",
    ),
    page(
        "es-personal-a",
        "The personal a",
        r"""
When the direct object of a verb is a particular person, Spanish puts **a** in front of it. English has nothing like it, so it's easy to forget.

- *Veo a María.* (I see María.) But *Veo la casa.* (I see the house.)
- *Busco a mi hermano.* (I'm looking for my brother.) But *Busco mi móvil.*
- *Quiero mucho a mi perro.* Pets count as people.

There is no personal *a* when the person isn't anyone in particular, or after *tener*: *Necesito un médico* (I need a doctor, any doctor), *Tengo dos hermanos*.

*Nadie* and *alguien* take it too: *¿Conoces a alguien aquí?* (Do you know anyone here?)

## Al and del

**A** + **el** becomes **al**, and **de** + **el** becomes **del**: *Llamo al médico* (I'm calling the doctor), *Vengo del mercado* (I'm coming from the market).

## Conocer or saber?

Both mean "to know", and both are common.

- **Conocer** is knowing a person or a place, being familiar with it: *Conozco a Juan*, *¿Conoces Sevilla?* It takes the personal *a* before a person.
- **Saber** is knowing a fact, or knowing how to do something: *Sé dónde vive*, *¿Sabes nadar?* (Can you swim?)

:::examples
- Llamo a mi madre todos los domingos. — I call my mother every Sunday.
- ¿Conoces a mis padres? — Have you met my parents?
- No sé dónde están las llaves. — I don't know where the keys are.
:::

:::cloze{sentence="Esta tarde visito ___ mis abuelos." blank="a"}
:::
""",
        ["artículos"],
        "es-personal-a",
    ),
]

PHRASES = phrases(
    """
hola | hello, hi | ¡Hola, Marta! ¿Qué tal todo? | Hi, Marta! How's everything?
buenos días | good morning | Buenos días, ¿tiene pan de hoy? | Good morning, do you have today's bread? | good days | Used until lunch, which in Spain is around two.
buenas tardes | good afternoon, good evening | Buenas tardes, una mesa para dos, por favor. | Good evening, a table for two, please. | good afternoons | From lunch until it gets dark.
buenas noches | good evening; good night | Buenas noches, hasta mañana. | Good night, see you tomorrow. | good nights | A greeting after dark, and a goodbye before bed.
adiós | goodbye | Adiós, hasta el lunes. | Goodbye, see you on Monday. | | Also a quick hello in passing, when you won't stop to talk.
hasta luego | see you later; bye | Me voy a casa. ¡Hasta luego! | I'm going home. See you later! | until later | Spaniards say it even when they won't see you again for weeks.
hasta mañana | see you tomorrow | Buenas noches, papá. Hasta mañana. | Good night, Dad. See you tomorrow. | until tomorrow
gracias | thank you, thanks | Gracias por el café. | Thanks for the coffee.
muchas gracias | thank you very much | Muchas gracias por la ayuda. | Thank you very much for your help. | many thanks
de nada | you're welcome | —Gracias. —De nada. | "Thanks." "You're welcome." | of nothing
por favor | please | Un café con leche, por favor. | A white coffee, please.
perdón | sorry; excuse me | Perdón, ¿está libre esta silla? | Excuse me, is this chair free?
perdona | excuse me (to someone you call tú) | Perdona, ¿sabes dónde está la estación? | Excuse me, do you know where the station is? | | Perdone to someone you call usted.
disculpe | excuse me (polite) | Disculpe, ¿dónde está la parada del autobús? | Excuse me, where's the bus stop? | | The usted form; to a friend, disculpa.
lo siento | I'm sorry | Lo siento, no tengo cambio. | I'm sorry, I don't have any change. | I feel it
vale | OK, fine | —¿Nos vemos a las ocho? —Vale. | "Shall we meet at eight?" "OK." | | Heard all the time in Spain. Latin America says está bien, bueno or dale.
de acuerdo | all right, agreed | De acuerdo, mañana te llamo. | All right, I'll call you tomorrow. | in agreement
¿qué tal? | how are you?, how's it going? | Hola, Pedro, ¿qué tal? | Hi, Pedro, how's it going? | what such? | Also asks about a thing: ¿Qué tal el viaje? (How was the trip?)
¿cómo estás? | how are you? (to a friend) | ¿Cómo estás? Hace mucho que no te veo. | How are you? I haven't seen you for ages.
¿cómo está usted? | how are you? (polite) | Buenos días, señora López, ¿cómo está usted? | Good morning, Mrs López, how are you?
encantado | pleased to meet you | —Te presento a mi hermana. —Encantado. | "This is my sister." "Pleased to meet you." | delighted | A woman says encantada.
mucho gusto | nice to meet you | Mucho gusto, me llamo Andrés. | Nice to meet you, my name's Andrés. | much pleasure
¿cómo te llamas? | what's your name? | Hola, me llamo Lucía. ¿Cómo te llamas? | Hi, I'm Lucía. What's your name? | how do you call yourself? | To someone you call usted: ¿cómo se llama?
¿de dónde eres? | where are you from? | Hablas muy bien español. ¿De dónde eres? | You speak Spanish very well. Where are you from? | from where are you?
no entiendo | I don't understand | Perdona, no entiendo. ¿Hablas inglés? | Sorry, I don't understand. Do you speak English?
¿puede repetir? | could you say that again? | Perdone, ¿puede repetir el número? | Sorry, could you repeat the number? | can you repeat? | To a friend: ¿puedes repetir?
más despacio, por favor | slower, please | Más despacio, por favor; estoy aprendiendo español. | Slower, please; I'm learning Spanish. | more slowly, please
no sé | I don't know | —¿A qué hora abre el museo? —No sé. | "What time does the museum open?" "I don't know."
¿cuánto cuesta? | how much is it? | ¿Cuánto cuesta este libro? | How much is this book? | how much does it cost? | For several things: ¿cuánto cuestan?
la cuenta, por favor | the bill, please | Camarero, la cuenta, por favor. | Waiter, the bill, please. | | In Spain the bill rarely comes until you ask for it.
¿dónde está el baño? | where's the toilet? | Perdone, ¿dónde está el baño? | Excuse me, where's the toilet? | where is the bathroom? | In bars and restaurants you'll also see los servicios or los aseos.
¿qué es esto? | what's this? | ¿Qué es esto? ¿Es pescado o carne? | What's this? Is it fish or meat?
¿a qué hora? | at what time? | ¿A qué hora empieza la película? | What time does the film start?
¡que aproveche! | enjoy your meal | Aquí tenéis la paella. ¡Que aproveche! | Here's your paella. Enjoy your meal! | may it do you good | Said to anyone you see eating, even strangers. Also ¡buen provecho!
¡salud! | cheers!; bless you! | ¡Salud! Por los novios. | Cheers! To the bride and groom. | health! | Also what you say when someone sneezes.
bienvenido | welcome | Bienvenido a Madrid. | Welcome to Madrid. | well come | To a woman, bienvenida; to a group, bienvenidos.
claro | of course, sure | —¿Me ayudas? —Claro. | "Will you help me?" "Sure." | clear
un momento | just a moment | Un momento, por favor, ahora vuelvo. | Just a moment, please, I'll be right back.
hay | there is, there are | Hay un supermercado en esta calle. | There's a supermarket on this street. | | One form for singular and plural: hay dos bancos.
""",
    ["greetings"],
)

NOUNS = nouns(
    """
padre | m | father | family | | Mi padre trabaja en un banco. | My father works in a bank. | Los padres means "the parents".
madre | f | mother | family | | Mi madre cocina muy bien. | My mother is a very good cook.
hermano | m | brother | family | | Mi hermano tiene diez años. | My brother is ten. | Los hermanos can mean brothers and sisters.
hermana | f | sister | family | | Mi hermana vive en Barcelona. | My sister lives in Barcelona.
hijo | m | son | family | | Su hijo estudia en Granada. | Her son is a student in Granada. | Los hijos also means children, sons and daughters.
hija | f | daughter | family | | Tienen una hija de seis años. | They have a six-year-old daughter.
marido | m | husband | family | | Mi marido es de Toledo. | My husband is from Toledo. | Also el esposo, a little more formal.
mujer | f | woman; wife | family | | Te presento a mi mujer, Carmen. | This is my wife, Carmen. | Also la esposa, a little more formal.
abuelo | m | grandfather | family | | Mi abuelo tiene ochenta años. | My grandfather is eighty. | Los abuelos are grandparents.
abuela | f | grandmother | family | | Los domingos comemos en casa de la abuela. | On Sundays we have lunch at Grandma's.
tío | m | uncle | family | | Mi tío vive en Argentina. | My uncle lives in Argentina. | In Spain, tío is also slang for "mate, guy".
tía | f | aunt | family | | Mi tía tiene una tienda de ropa. | My aunt has a clothes shop.
primo | m | cousin (male) | family | | Mi primo y yo tenemos la misma edad. | My cousin and I are the same age.
prima | f | cousin (female) | family | | Mi prima es profesora de música. | My cousin is a music teacher.
novio | m | boyfriend; groom | family | | Lucía tiene un novio nuevo. | Lucía has a new boyfriend. | Los novios are also the bride and groom.
novia | f | girlfriend; bride | family | | Su novia es italiana. | His girlfriend is Italian.
familia | f | family | family | | Mi familia es muy grande. | My family is very big.
hombre | m | man | people | | Ese hombre es mi vecino. | That man is my neighbour.
chico | m | boy, young man | people | | El chico de la tienda es muy simpático. | The guy in the shop is very nice.
chica | f | girl, young woman | people | | Hay dos chicas nuevas en clase. | There are two new girls in the class.
persona | f | person | people | | Tu padre es una persona muy simpática. | Your father is a very nice person. | Always feminine, even for a man.
señor | m | man, gentleman; Mr | people | | Un señor pregunta por ti. | A man is asking for you. | La señora is a lady, or Mrs.
nombre | m | name | people | | Mi nombre es Laura, pero todos me llaman Lau. | My name is Laura, but everyone calls me Lau.
cabeza | f | head | body | | Me duele mucho la cabeza. | I've got a bad headache.
cara | f | face | body | | Tiene una cara muy simpática. | She has a very friendly face.
ojo | m | eye | body | | Mi hija tiene los ojos azules. | My daughter has blue eyes.
nariz | f | nose | body | | Tengo la nariz roja por el frío. | My nose is red from the cold.
boca | f | mouth | body | | No hables con la boca llena. | Don't talk with your mouth full.
diente | m | tooth | body | | Me lavo los dientes después de comer. | I brush my teeth after lunch.
oreja | f | ear | body | | El perro tiene las orejas muy grandes. | The dog has very big ears. | The inner ear, and hearing, is el oído.
pelo | m | hair | body | | Tiene el pelo largo y negro. | She has long black hair.
mano | f | hand | body | | Lávate las manos antes de comer. | Wash your hands before you eat. | Feminine, though it ends in -o.
brazo | m | arm | body | | Me duele el brazo derecho. | My right arm hurts.
pierna | f | leg | body | | Tiene las piernas muy largas. | He has very long legs.
pie | m | foot | body | | Vamos a pie, está muy cerca. | Let's walk, it's very close. | A pie means "on foot".
café | m | coffee; café | food | | ¿Tomamos un café? | Shall we have a coffee? | Café con leche is coffee with milk; un cortado has just a dash.
té | m | tea | food | | Por la tarde tomo un té con limón. | In the afternoon I have a tea with lemon.
leche | f | milk | food | - | ¿Hay leche en la nevera? | Is there any milk in the fridge?
vino | m | wine | food | | Un vino tinto, por favor. | A red wine, please. | Red wine is vino tinto, never vino rojo.
cerveza | f | beer | food | | Dos cervezas, por favor. | Two beers, please. | Una caña is a small glass of draught beer.
zumo | m | juice | food | | Un zumo de naranja, por favor. | An orange juice, please. | Latin America: el jugo.
azúcar | m | sugar | food | - | ¿Tomas el café con azúcar? | Do you take sugar in your coffee? | Usually masculine, though you'll also hear la azúcar.
sal | f | salt | food | - | ¿Me pasas la sal? | Can you pass me the salt?
carne | f | meat | food | | No como carne. | I don't eat meat.
pescado | m | fish (as food) | food | | Los viernes comemos pescado. | On Fridays we eat fish. | A live fish is un pez.
pollo | m | chicken | food | | Hoy hay pollo con patatas. | There's chicken and potatoes today.
huevo | m | egg | food | | Desayuno dos huevos fritos. | I have two fried eggs for breakfast.
queso | m | cheese | food | | Este queso es de La Mancha. | This cheese is from La Mancha.
fruta | f | fruit | food | | En verano como mucha fruta. | I eat a lot of fruit in summer.
manzana | f | apple | food | | Siempre llevo una manzana en el bolso. | I always carry an apple in my bag.
arroz | m | rice | food | - | La paella se hace con arroz. | Paella is made with rice.
desayuno | m | breakfast | food | | El desayuno está en la mesa. | Breakfast is on the table.
cena | f | dinner, supper | food | | En España la cena es tarde, a las diez. | In Spain dinner is late, at ten.
calle | f | street | city | | Vivo en la calle Mayor. | I live on Calle Mayor.
ciudad | f | city, town | city | | Sevilla es una ciudad preciosa. | Seville is a beautiful city.
plaza | f | square | city | | Nos vemos en la plaza a las seis. | See you in the square at six.
tienda | f | shop | city | | La tienda abre a las diez. | The shop opens at ten.
banco | m | bank; bench | city | | El banco cierra a las dos. | The bank closes at two. | Also a bench in a park.
colegio | m | school | city | | Los niños van al colegio a pie. | The children walk to school. | For children; a secondary school is un instituto.
hospital | m | hospital | city | | El hospital está al final de la calle. | The hospital is at the end of the street.
restaurante | m | restaurant | city | | Conozco un restaurante muy bueno. | I know a very good restaurant.
estación | f | station | city | | ¿Dónde está la estación de tren? | Where's the train station?
mercado | m | market | city | | Compro la fruta en el mercado. | I buy my fruit at the market.
iglesia | f | church | city | | La iglesia es del siglo XII. | The church dates from the 12th century.
museo | m | museum | city | | El Museo del Prado está en Madrid. | The Prado museum is in Madrid.
parque | m | park | city | | Los niños juegan en el parque. | The children are playing in the park.
farmacia | f | pharmacy, chemist's | city | | ¿Hay una farmacia cerca de aquí? | Is there a pharmacy near here?
hotel | m | hotel | city | | El hotel está cerca de la playa. | The hotel is near the beach.
día | m | day | time | | Hoy es un día precioso. | It's a beautiful day today. | Masculine, though it ends in -a: buenos días.
semana | f | week | time | | Trabajo cinco días a la semana. | I work five days a week.
mes | m | month | time | meses | El mes que viene voy a Lisboa. | Next month I'm going to Lisbon.
año | m | year | time | | Tengo treinta años. | I'm thirty. | Age goes with tener: tengo treinta años.
hora | f | hour; time | time | | ¿Qué hora es? | What time is it?
minuto | m | minute | time | | El autobús llega en cinco minutos. | The bus arrives in five minutes.
mañana | f | morning | time | | Trabajo por la mañana. | I work in the morning. | Without an article, mañana means "tomorrow".
tarde | f | afternoon, evening | time | | Por la tarde voy al gimnasio. | In the afternoon I go to the gym. | As an adverb, tarde means "late": llego tarde.
lunes | m | Monday | time | lunes | El lunes empiezo un trabajo nuevo. | I start a new job on Monday. | No capital letter, and no word for "on": el lunes.
martes | m | Tuesday | time | martes | Los martes tengo clase de inglés. | I have English class on Tuesdays.
miércoles | m | Wednesday | time | miércoles | El miércoles es el cumpleaños de mi madre. | Wednesday is my mother's birthday.
jueves | m | Thursday | time | jueves | Los jueves salimos a cenar. | On Thursdays we go out for dinner.
viernes | m | Friday | time | viernes | El viernes por la noche hay un concierto. | There's a concert on Friday night.
sábado | m | Saturday | time | | El sábado vamos a la playa. | On Saturday we're going to the beach.
domingo | m | Sunday | time | | Los domingos como con mi familia. | On Sundays I have lunch with my family.
piso | m | flat, apartment; floor | home | | Vivimos en un piso del centro. | We live in a flat in the centre. | Latin America: el departamento or el apartamento.
cocina | f | kitchen; cooking | home | | La cocina es pequeña pero muy bonita. | The kitchen is small but very pretty.
baño | m | bathroom, toilet | home | | El piso tiene dos baños. | The flat has two bathrooms.
habitación | f | room; bedroom | home | | Mi habitación da a la calle. | My bedroom looks onto the street.
cama | f | bed | home | | Me voy a la cama, estoy cansada. | I'm off to bed, I'm tired.
jardín | m | garden | home | | Mis abuelos tienen un jardín con flores. | My grandparents have a garden with flowers.
dinero | m | money | objects | - | No tengo dinero en efectivo. | I don't have any cash.
móvil | m | mobile phone | objects | | ¿Me das tu número de móvil? | Can I have your mobile number? | Latin America: el celular.
llave | f | key | objects | | ¿Dónde están las llaves del coche? | Where are the car keys?
trabajo | m | work; job | city | | Mi trabajo está muy cerca de casa. | My work is very close to home.
idioma | m | language | people | | ¿Cuántos idiomas hablas? | How many languages do you speak? | Masculine, though it ends in -a.
país | m | country | people | países | España es un país muy diverso. | Spain is a very varied country.
"""
)

VERBS = [
    verb("ser", "to be (what something is)", [],
         present="soy eres es somos sois son",
         pret="fui fuiste fue fuimos fuisteis fueron",
         imp="era eras era éramos erais eran",
         subj="sea seas sea seamos seáis sean",
         example="Soy de Madrid, pero vivo en Londres.", example_en="I'm from Madrid, but I live in London.",
         note="For identity, origin, jobs, character and the time."),
    verb("estar", "to be (where or how something is)", [],
         present="estoy estás está estamos estáis están",
         pret_stem="estuv",
         subj="esté estés esté estemos estéis estén",
         example="¿Dónde estás? Estoy en casa.", example_en="Where are you? I'm at home.",
         note="For place, and for states that can change."),
    verb("tener", "to have", [],
         present="tengo tienes tiene tenemos tenéis tienen", pret_stem="tuv", fut="tendr",
         example="Tengo dos hermanos y una hermana.", example_en="I have two brothers and a sister.",
         note="Also age (tengo veinte años) and tener que + infinitive, \"to have to\"."),
    verb("hacer", "to do; to make", [],
         present="hago haces hace hacemos hacéis hacen",
         pret="hice hiciste hizo hicimos hicisteis hicieron", fut="har", pp="hecho",
         example="¿Qué haces el fin de semana?", example_en="What are you doing at the weekend?",
         note="Also the weather: hace frío, hace sol."),
    verb("poder", "can, to be able to", [], stem="o>ue", pret_stem="pud", fut="podr",
         example="¿Puedes cerrar la ventana?", example_en="Can you close the window?"),
    verb("querer", "to want; to love", [], stem="e>ie", pret_stem="quis", fut="querr",
         example="Quiero un café con leche.", example_en="I'd like a white coffee.",
         note="Te quiero: I love you."),
    verb("decir", "to say, to tell", [],
         present="digo dices dice decimos decís dicen", pret_stem="dij", fut="dir", pp="dicho",
         example="¿Qué dice el profesor?", example_en="What's the teacher saying?"),
    verb("venir", "to come", [],
         present="vengo vienes viene venimos venís vienen", pret_stem="vin", fut="vendr",
         example="¿Vienes a la fiesta el sábado?", example_en="Are you coming to the party on Saturday?"),
    verb("saber", "to know (a fact); to know how to", [],
         present="sé sabes sabe sabemos sabéis saben", pret_stem="sup", fut="sabr",
         subj="sepa sepas sepa sepamos sepáis sepan",
         example="No sé dónde está la estación.", example_en="I don't know where the station is.",
         note="Sé nadar: I can swim."),
    verb("poner", "to put; to turn on", [],
         present="pongo pones pone ponemos ponéis ponen", pret_stem="pus", fut="pondr", pp="puesto",
         example="¿Dónde pongo las llaves?", example_en="Where shall I put the keys?",
         note="Also poner la tele, to turn on the TV."),
    verb("salir", "to go out, to leave", [],
         present="salgo sales sale salimos salís salen", fut="saldr",
         example="Salgo de casa a las ocho.", example_en="I leave home at eight."),
    verb("dar", "to give", [],
         present="doy das da damos dais dan",
         pret="di diste dio dimos disteis dieron",
         subj="dé des dé demos deis den",
         example="Te doy mi número de teléfono.", example_en="I'll give you my phone number."),
    verb("ver", "to see; to watch", [],
         present="veo ves ve vemos veis ven",
         pret="vi viste vio vimos visteis vieron",
         imp="veía veías veía veíamos veíais veían", pp="visto",
         example="Vemos la tele después de cenar.", example_en="We watch TV after dinner."),
    verb("haber", "to have (forming the perfect); there is (hay)", [],
         present="he has ha hemos habéis han", pret_stem="hub", fut="habr",
         subj="haya hayas haya hayamos hayáis hayan",
         example="Hay mucha gente en la plaza.", example_en="There are a lot of people in the square.",
         note="Its forms build the perfect tenses (he comido). Hay, había, hubo and habrá mean there is, there was and there will be."),
    verb("conocer", "to know (a person or place); to meet", [], zc=True,
         example="¿Conoces Barcelona?", example_en="Have you been to Barcelona?",
         note="Conocer a alguien is also \"to meet someone\" for the first time."),
    verb("vivir", "to live", [],
         example="Vivimos en un pueblo cerca de Sevilla.", example_en="We live in a village near Seville."),
    verb("trabajar", "to work", [],
         example="Trabajo en un hospital.", example_en="I work in a hospital."),
    verb("estudiar", "to study", [],
         example="Mi hermana estudia Medicina.", example_en="My sister is studying medicine."),
    verb("comprar", "to buy", [],
         example="Compro el pan todas las mañanas.", example_en="I buy bread every morning."),
    verb("tomar", "to take; to have (food, drink)", [],
         example="¿Qué vas a tomar?", example_en="What are you having?",
         note="Tomar el autobús works everywhere. Coger el autobús is everyday Spain but vulgar in much of Latin America."),
    verb("necesitar", "to need", [],
         example="Necesito un taxi para ir al aeropuerto.", example_en="I need a taxi to get to the airport."),
    verb("escuchar", "to listen to", [],
         example="Escucho la radio en el coche.", example_en="I listen to the radio in the car."),
    verb("mirar", "to look at, to watch", [],
         example="Mira, ahí está el museo.", example_en="Look, there's the museum."),
    verb("buscar", "to look for", [],
         example="Busco un piso en el centro.", example_en="I'm looking for a flat in the centre.",
         note="No word for \"for\": busco las llaves."),
    verb("llegar", "to arrive", [],
         example="El tren llega a las tres.", example_en="The train arrives at three."),
    verb("abrir", "to open", [], pp="abierto",
         example="¿A qué hora abre el banco?", example_en="What time does the bank open?"),
    verb("escribir", "to write", [], pp="escrito",
         example="Escribo un correo a mi jefe.", example_en="I'm writing an email to my boss."),
    verb("leer", "to read", [],
         pret="leí leíste leyó leímos leísteis leyeron", pp="leído",
         example="Leo el periódico en el tren.", example_en="I read the newspaper on the train."),
    verb("aprender", "to learn", [],
         example="Aprendo español en una academia.", example_en="I'm learning Spanish at a language school."),
    verb("entender", "to understand", [], stem="e>ie",
         example="No entiendo esta palabra.", example_en="I don't understand this word."),
    verb("pensar", "to think", [], stem="e>ie",
         example="¿Qué piensas de mi idea?", example_en="What do you think of my idea?",
         note="Pensar en: to think about."),
    verb("empezar", "to begin, to start", [], stem="e>ie",
         example="La clase empieza a las nueve.", example_en="The class starts at nine."),
    verb("volver", "to come back, to return", [], stem="o>ue", pp="vuelto",
         example="Vuelvo a casa a las siete.", example_en="I get back home at seven.",
         note="Volver a + infinitive means doing something again: vuelvo a llamar."),
    verb("dormir", "to sleep", [], stem="o>ue",
         example="Duermo muy mal en verano.", example_en="I sleep very badly in summer."),
    verb("pedir", "to ask for; to order", [], stem="e>i",
         example="Voy a pedir una paella.", example_en="I'm going to order a paella.",
         note="Pedir asks for a thing; preguntar asks a question."),
    verb("jugar", "to play (a game, a sport)", [], stem="u>ue",
         example="Los sábados juego al fútbol.", example_en="On Saturdays I play football.",
         note="An instrument takes tocar: toco la guitarra."),
    verb("gustar", "to please (to like)", [],
         example="Me gusta mucho tu casa.", example_en="I really like your house.",
         note="The thing liked is the subject: me gustan los gatos."),
    verb("llamar", "to call", [],
         example="Te llamo esta noche.", example_en="I'll call you tonight.",
         note="Llamar a la puerta: to knock at the door."),
]

ADJECTIVES = adjectives(
    """
grande, grande, grandes, grandes | big, large; great | Viven en una casa muy grande. | They live in a very big house. | Before a singular noun it becomes gran and means "great": un gran amigo.
pequeño, pequeña, pequeños, pequeñas | small, little | Tengo un piso pequeño en el centro. | I have a small flat in the centre.
bueno, buena, buenos, buenas | good | Este pan está muy bueno. | This bread is really good. | Before a masculine singular noun: buen. Un buen libro.
malo, mala, malos, malas | bad | Es una mala idea. | It's a bad idea. | Before a masculine singular noun: mal. Un mal día.
bonito, bonita, bonitos, bonitas | pretty, nice | Tienes una casa muy bonita. | You have a lovely house.
guapo, guapa, guapos, guapas | good-looking | Tu hermano es muy guapo. | Your brother is very good-looking. | In Spain also "dressed up, smart": ¡Qué guapa vas!
alto, alta, altos, altas | tall; high | Mi padre es muy alto. | My father is very tall.
bajo, baja, bajos, bajas | short; low | Mi abuela es baja y muy delgada. | My grandmother is short and very thin.
joven, joven, jóvenes, jóvenes | young | Su madre es muy joven. | His mother is very young.
viejo, vieja, viejos, viejas | old | Este coche ya es muy viejo. | This car is very old now. | For people, mayor is politer: una señora mayor.
nuevo, nueva, nuevos, nuevas | new | Tengo un móvil nuevo. | I have a new phone.
simpático, simpática, simpáticos, simpáticas | nice, friendly | Tus amigos son muy simpáticos. | Your friends are very nice. | Not "sympathetic", which is comprensivo.
contento, contenta, contentos, contentas | happy, pleased | Estoy muy contenta con mi trabajo. | I'm very happy with my job. | Used with estar.
cansado, cansada, cansados, cansadas | tired | Estamos cansados del viaje. | We're tired after the journey.
caliente, caliente, calientes, calientes | hot (to the touch) | Cuidado, la sopa está muy caliente. | Careful, the soup is very hot. | Hot weather is hace calor; spicy food is picante.
frío, fría, fríos, frías | cold | Quiero una cerveza bien fría. | I want a nice cold beer.
fácil, fácil, fáciles, fáciles | easy | El examen es muy fácil. | The exam is very easy.
difícil, difícil, difíciles, difíciles | difficult, hard | El español no es tan difícil. | Spanish isn't that hard.
caro, cara, caros, caras | expensive | Los restaurantes del centro son muy caros. | The restaurants in the centre are very expensive.
barato, barata, baratos, baratas | cheap | La fruta es barata en el mercado. | Fruit is cheap at the market.
español, española, españoles, españolas | Spanish | Mi mujer es española. | My wife is Spanish. | No capital letter. The language is el español, or el castellano.
"""
) + adjectives(
    """
rojo, roja, rojos, rojas | red | Tengo un coche rojo. | I have a red car.
azul, azul, azules, azules | blue | Tienes unos ojos azules preciosos. | You have beautiful blue eyes.
verde, verde, verdes, verdes | green | Las manzanas verdes son mis favoritas. | Green apples are my favourites.
amarillo, amarilla, amarillos, amarillas | yellow | Me gustan las flores amarillas. | I like yellow flowers.
negro, negra, negros, negras | black | Tengo un gato negro. | I have a black cat.
blanco, blanca, blancos, blancas | white | En Andalucía hay muchos pueblos blancos. | There are lots of white villages in Andalusia. | Vino blanco is white wine.
gris, gris, grises, grises | grey | Hoy el cielo está gris. | The sky is grey today.
marrón, marrón, marrones, marrones | brown | Tengo los ojos marrones. | I have brown eyes. | For hair, castaño is more usual: pelo castaño.
morado, morada, morados, moradas | purple | Las berenjenas son moradas. | Aubergines are purple.
""",
    ["colors"],
)

PRONOUNS = phrases(
    """
yo | I | Yo trabajo y mi hermano estudia. | I work and my brother studies. | | Usually left out, since the verb already says who: hablo español. Put it in to stress or contrast.
tú | you (one person, familiar) | ¿Tú también eres de Madrid? | Are you from Madrid too? | | Without the accent, tu means your.
usted | you (one person, polite) | ¿Usted es la doctora Ruiz? | Are you Dr Ruiz? | | Takes the él form of the verb. Written Ud. for short.
él | he | Él es mi hermano. | He's my brother. | | Without the accent, el means the.
ella | she | Ella vive en Bilbao. | She lives in Bilbao.
nosotros | we | Nosotros comemos a las dos. | We have lunch at two. | | Nosotras for a group of women only.
vosotros | you (several, familiar; Spain) | ¿Vosotros habláis inglés? | Do you all speak English? | | Vosotras for women only. Latin America says ustedes instead.
ellos | they (men, or a mixed group) | Ellos viven en el centro. | They live in the centre. | | A group with even one man in it is ellos.
ellas | they (women only) | Ellas son mis primas. | They're my cousins.
ustedes | you (several, polite; any group in Latin America) | ¿Ustedes son de aquí? | Are you from here? | | Takes the ellos form of the verb.
""",
    ["pronombres"],
)

NEGATIVES = phrases(
    """
no | no; not | Mi hermano no come carne. | My brother doesn't eat meat. | | Goes straight before the verb, with no helper like "don't".
nunca | never | Nunca veo la tele por la mañana. | I never watch TV in the morning. | | After the verb it needs no in front: no veo nunca la tele.
nada | nothing, not anything | No quiero nada, gracias. | I don't want anything, thanks. | | After the verb it needs no in front, so two negatives are correct.
nadie | nobody, no one | Nadie sabe dónde está Pedro. | Nobody knows where Pedro is. | | After the verb: no viene nadie.
tampoco | not ... either, neither | Ana no viene y yo tampoco. | Ana isn't coming, and neither am I. | | The negative of también: yo también, yo tampoco.
todavía no | not yet | Todavía no tengo coche. | I don't have a car yet.
""",
    ["negación"],
)

NUMBERS = phrases(
    """
uno | one | Solo tengo uno. | I only have one. | | Before a masculine noun it's un, before a feminine one una: un libro, una casa.
dos | two | Tengo dos gatos. | I have two cats.
tres | three | Somos tres. | There are three of us.
cuatro | four | La clase empieza a las cuatro. | The class starts at four.
cinco | five | Mi hija tiene cinco años. | My daughter is five.
seis | six | Hay seis huevos en la nevera. | There are six eggs in the fridge.
siete | seven | La semana tiene siete días. | A week has seven days.
ocho | eight | Trabajo ocho horas al día. | I work eight hours a day.
nueve | nine | El museo abre a las nueve. | The museum opens at nine.
diez | ten | Son diez euros, por favor. | That's ten euros, please.
""",
    ["números"],
)

CONNECTIVES = connectors(
    "connective",
    """
primero | first | conn-sequence | Primero comemos y después vamos al cine. | First we'll eat and then we'll go to the cinema.
después | afterwards, then | conn-sequence | Ceno y después veo la tele. | I have dinner and then I watch TV.
también | also, too | conn-addition | Me gusta el té. También me gusta el café. | I like tea. I like coffee too. | Me gusta el té. Me gusta también el café.
""",
    ["conectores"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
y | and | conj-coordinating | Tengo un hermano y una hermana. | I have a brother and a sister.
o | or | conj-coordinating | ¿Quieres té o café? | Do you want tea or coffee?
cuando | when | conj-subordinating | Leo cuando llueve. | I read when it rains. | Cuando llueve, leo.
si | if | conj-subordinating | Salimos si quieres. | We'll go out if you want. | Si quieres, salimos.
""",
    ["conjunciones"],
)

ITEMS = PAGES + interleave(
    PHRASES, PRONOUNS + NEGATIVES + NUMBERS, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS
)

# Each grammar page's Unit practises the words its page explains: the
# pronunciation page ends on how each greeting in its unit sounds, the
# pronouns, negation and numbers pages get their own pronouns, negative
# words and numbers, and colours get a page on which ones agree.
# Possessives pairs with the family, the personal a with the verbs that
# most often take a person.
UNITS = [
    {
        "title": "La pronunciación",
        "page_id": "es-pronunciation",
        "word_ids": ["hola", "buenos-dias", "gracias", "por-favor", "perdon", "encantado"],
    },
    {
        "title": "Tú o usted",
        "page_id": "es-subject-pronouns",
        "word_ids": ["yo", "tu", "usted", "el", "ella", "nosotros", "vosotros", "ellos", "ellas", "ustedes"],
    },
    {
        "title": "Ser y estar",
        "page_id": "es-ser-estar",
        "word_ids": ["ser", "estar", "haber", "hay", "tener", "hacer", "querer"],
    },
    {
        "title": "El presente",
        "page_id": "es-present-tense",
        "word_ids": ["entender", "pensar", "empezar", "volver", "dormir", "pedir", "jugar"],
    },
    {
        "title": "La negación",
        "page_id": "es-negation",
        "word_ids": ["no", "nunca", "nada", "nadie", "tampoco", "todavia-no", "no-entiendo", "no-se"],
    },
    {
        "title": "Las preguntas",
        "page_id": "es-questions",
        "word_ids": [
            "cuanto-cuesta",
            "donde-esta-el-bano",
            "que-es-esto",
            "a-que-hora",
            "de-donde-eres",
            "como-te-llamas",
            "puede-repetir",
        ],
    },
    {
        "title": "Me gusta",
        "page_id": "es-gustar",
        "word_ids": ["gustar", "cafe", "te", "leche", "vino", "cerveza", "zumo"],
    },
    {
        "title": "Los adjetivos",
        "page_id": "es-adjectives",
        "word_ids": ["grande", "pequeno", "bueno", "malo", "bonito", "nuevo", "viejo"],
    },
    {
        "title": "Los colores",
        "page_id": "es-colors",
        "word_ids": ["rojo", "azul", "verde", "amarillo", "negro", "blanco", "gris", "marron", "morado"],
    },
    {
        "title": "Cómo es la gente",
        "word_ids": ["guapo", "alto", "bajo", "joven", "simpatico", "contento", "cansado"],
    },
    {
        "title": "Cómo son las cosas",
        "word_ids": ["caliente", "frio", "facil", "dificil", "caro", "barato", "espanol"],
    },
    {
        "title": "Los números",
        "page_id": "es-numbers",
        "word_ids": ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"],
    },
    {
        "title": "Ir a",
        "page_id": "es-ir-a",
        "word_ids": ["trabajar", "estudiar", "llegar", "aprender", "escribir", "leer", "comprar"],
    },
    {
        "title": "Los posesivos",
        "page_id": "es-possessives",
        "word_ids": ["padre", "madre", "hermano", "hermana", "hijo", "hija", "marido", "mujer"],
    },
    {
        "title": "La a personal",
        "page_id": "es-personal-a",
        "word_ids": ["conocer", "buscar", "llamar", "mirar", "escuchar", "ver"],
    },
    {
        "title": "Y, o, cuando, si",
        "word_ids": ["primero", "despues", "tambien", "y", "o", "cuando", "si"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "food": "La comida",
    "home": "La casa",
    "time": "Los días",
    "people": "La gente",
}

PACK = pack(
    "es-foundations-v1",
    2,
    "es",
    "Español · Fundamentos (A1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Práctica"),
)
