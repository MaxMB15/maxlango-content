"""es-everyday-v1: A2. The past tenses, the future, pronouns, and the words for
daily routines, weather, clothes, travel, work, health and shopping."""

from common import build_units, interleave, page, pack, topic, topic_labels
from es_common import adjectives, connectors, nouns, phrases, verb
from es_conj import IR

DELTA = [
    topic("reflexivos", "Verbos reflexivos", "reflexive verbs", ["presente"]),
    topic("pronombres-objeto", "Pronombres de objeto", "object pronouns", ["presente"]),
    topic("comparativos", "Comparativos", "comparing", ["adjetivos"]),
    topic("preposiciones", "Por y para", "por and para", []),
    topic("gerundio", "Gerundio", "the -ing form", ["presente"]),
    topic("clothing", "Ropa", "clothing", ["género"]),
    topic("weather", "Clima", "weather", []),
    topic("travel", "Viajes", "travel", ["género"]),
    topic("work", "Trabajo", "work and study", ["género"]),
    topic("health", "Salud", "health", ["género"]),
    topic("leisure", "Ocio", "free time", ["género"]),
    topic("feelings", "Sentimientos", "feelings and character", ["adjetivos"]),
    topic("shopping", "Compras", "shopping and money", ["género"]),
    topic("expressions", "Expresiones", "set phrases and short replies", []),
    {
        "id": "conn-consequence",
        "kind": "connective-class",
        "label": "Consecuencia",
        "labelGloss": "the next statement is the result of the last one (por eso, así que)",
        "order": 4,
        "appliesTo": {"kind": "connective"},
        "dependsOn": [],
    },
]

PAGES = [
    page(
        "es-perfect",
        "He comido: the present perfect",
        r"""
The **pretérito perfecto** is a form of **haber** plus a past participle, just like English "have" + "done": *He comido* (I've eaten).

| | haber | + participle |
| --- | --- | --- |
| yo | he | hablado |
| tú | has | comido |
| él, ella, usted | ha | vivido |
| nosotros | hemos | estado |
| vosotros | habéis | sido |
| ellos, ellas, ustedes | han | tenido |

## The participle

**-ar** verbs take **-ado** and **-er** and **-ir** verbs take **-ido**: *hablado*, *comido*, *vivido*. A handful of common verbs have their own:

| Verb | Participle | Verb | Participle |
| --- | --- | --- | --- |
| abrir | abierto | poner | puesto |
| decir | dicho | romper | roto |
| escribir | escrito | ver | visto |
| hacer | hecho | volver | vuelto |
| morir | muerto | descubrir | descubierto |

Verbs built on these follow them: *devolver*, *devuelto*.

## Two rules English doesn't have

- The participle never changes. *Ella ha llegado*, *ellas han llegado*. It agrees only when it's used as an adjective: *la puerta está abierta*.
- Nothing goes between *haber* and the participle. *No* and pronouns go before *haber*: *No lo he visto* (I haven't seen it). *Ya* (already) goes before the whole verb or after it: *Ya he comido*, or *He comido ya*.

## When Spain uses it

In Spain the perfect is for a past action in a stretch of time that isn't over yet, or that still feels connected to now:

- with *hoy*, *esta mañana*, *esta semana*, *este año*: *Esta semana he trabajado mucho.*
- with *ya* and *todavía no* (not yet): *¿Ya has terminado? —No, todavía no.*
- with *alguna vez* (ever) and *nunca*: *¿Has estado alguna vez en México?*
- for something that has just happened: *¡Me he cortado!* (I've cut myself!)

For a time that's over, such as *ayer* or *el año pasado*, Spain uses the preterite, on the next page.

Most of Latin America uses the perfect much less. Where Spain asks *¿Ya has comido?*, a Mexican or an Argentine asks *¿Ya comiste?* Both are understood everywhere.

:::examples
- Hoy he trabajado diez horas. — I've worked ten hours today.
- ¿Has visto mis llaves? — Have you seen my keys?
- Todavía no hemos comido. — We haven't eaten yet.
- Nunca he estado en Argentina. — I've never been to Argentina.
:::

:::predict{prompt="tú (hacer)" answer="has hecho"}
:::

:::cloze{sentence="Mis padres nunca ___ estado en Londres." blank="han"}
:::
""",
        ["pretérito-perfecto"],
        "es-perfect",
        explains=["pretérito-perfecto"],
    ),
    page(
        "es-preterite",
        "Comí: the preterite",
        r"""
The **pretérito indefinido** tells what happened at a finished moment in the past: *Ayer comí paella* (Yesterday I had paella). Grammars also call it the *pretérito perfecto simple*.

| | hablar | comer | vivir |
| --- | --- | --- | --- |
| yo | hablé | comí | viví |
| tú | hablaste | comiste | viviste |
| él, ella, usted | habló | comió | vivió |
| nosotros | hablamos | comimos | vivimos |
| vosotros | hablasteis | comisteis | vivisteis |
| ellos, ellas, ustedes | hablaron | comieron | vivieron |

The written accent matters: *hablo* is "I speak", *habló* is "he spoke". The nosotros form of -ar and -ir verbs is the same as in the present, so *hablamos* is "we speak" or "we spoke". The rest of the sentence tells you which.

## Spelling changes

- In the yo form, verbs in **-car**, **-gar** and **-zar** change their spelling to keep their sound: *buscar*, *busqué*; *llegar*, *llegué*; *empezar*, *empecé*.
- **-ir** verbs with a stem change switch e to i and o to u in the él and ellos forms: *pedir*, *pidió*; *dormir*, *durmió*.
- *Leer* and *oír* take a y: *leyó*, *oyeron*.

## The irregular preterites

The commonest verbs have a new stem, their own endings and no written accent:

| Verb | Stem | yo | él, ella |
| --- | --- | --- | --- |
| estar | estuv- | estuve | estuvo |
| tener | tuv- | tuve | tuvo |
| poder | pud- | pude | pudo |
| poner | pus- | puse | puso |
| saber | sup- | supe | supo |
| querer | quis- | quise | quiso |
| venir | vin- | vine | vino |
| hacer | hic- | hice | hizo |
| decir | dij- | dije | dijo |
| traer | traj- | traje | trajo |

The endings are -e, -iste, -o, -imos, -isteis, -ieron. After a j the last one is -eron.

**Ser** and **ir** share one set of forms: *fui, fuiste, fue, fuimos, fuisteis, fueron*. *Fui a Cádiz* is "I went to Cádiz"; *Fue un día precioso* is "It was a lovely day". **Dar** and **ver** take short endings with no accent: *di, dio*; *vi, vio*.

## Perfecto or indefinido?

Spain decides by the time words. If the period is over, use the indefinido. If you're still in it, use the perfect.

| Indefinido: the time is over | Perfecto: the time isn't over |
| --- | --- |
| ayer | hoy |
| el lunes pasado | esta semana |
| el año pasado | este año |
| hace dos días | alguna vez |

*Ayer fui al cine* (I went to the cinema yesterday), but *Hoy he ido al cine* (I've been to the cinema today).

Latin America and the Canary Islands use the indefinido for nearly all of these: *Hoy fui al cine.*

:::examples
- Ayer cené con mis padres. — Yesterday I had dinner with my parents.
- ¿Qué hiciste el fin de semana? — What did you do at the weekend?
- El año pasado estuvimos en Perú. — Last year we were in Peru.
- No pude dormir anoche. — I couldn't sleep last night.
:::

:::sort{groups="Perfecto (time not over): esta mañana, este mes, nunca | Indefinido (time over): anoche, la semana pasada, en 2010"}
:::

:::predict{prompt="nosotros (tener)" answer="tuvimos"}
:::

:::predict{prompt="ellos (conducir)" answer="condujeron"}
:::
""",
        ["pretérito-indefinido"],
        "es-preterite",
        explains=["pretérito-indefinido"],
    ),
    page(
        "es-imperfect",
        "Comía: the imperfect",
        r"""
The **imperfecto** shows the past as it was going on: what used to happen, what things were like, and what was in progress.

| | hablar | comer | vivir |
| --- | --- | --- | --- |
| yo | hablaba | comía | vivía |
| tú | hablabas | comías | vivías |
| él, ella, usted | hablaba | comía | vivía |
| nosotros | hablábamos | comíamos | vivíamos |
| vosotros | hablabais | comíais | vivíais |
| ellos, ellas, ustedes | hablaban | comían | vivían |

The yo and él forms are the same, so Spanish keeps the pronoun more often here: *yo vivía*, *ella vivía*.

Only three verbs are irregular:

| Verb | Imperfect |
| --- | --- |
| ser | era, eras, era, éramos, erais, eran |
| ir | iba, ibas, iba, íbamos, ibais, iban |
| ver | veía, veías, veía, veíamos, veíais, veían |

## When to use it

- **Habits**, what used to happen: *De pequeño, iba andando al colegio.* (As a boy, I used to walk to school.) Words like *siempre*, *todos los días*, *a menudo*, *de niño* and *antes* point to it.
- **Description**: the time, age, weather, and what people and places were like: *Eran las once de la noche. Mi abuelo era muy alto.*
- **Something in progress** when something else happened: *Dormía cuando llegaste.*
- **Politeness**: *Quería un café, por favor.* (I'd like a coffee, please.)

## Imperfecto or indefinido?

In a story the imperfect sets the scene and the preterite moves the action along. Think of a film: the imperfect is the background, and the preterite is what happens in front of it.

*Hacía buen tiempo y la playa estaba llena. De repente, empezó a llover y todos se fueron a casa.* (The weather was nice and the beach was full. Suddenly it started to rain and everyone went home.)

One finished event takes the indefinido: *Ayer fui al médico.* A repeated or ongoing one takes the imperfect: *Iba al médico cada semana.*

A few verbs change their meaning. *Conocí a Ana* is "I met Ana"; *conocía a Ana* is "I knew Ana". *Supe la verdad* is "I found out the truth"; *sabía la verdad* is "I knew the truth".

:::examples
- Cuando era pequeña, vivía en un pueblo. — When I was little, I lived in a village.
- Todos los veranos íbamos a la playa. — Every summer we went to the beach.
- Estaba en la ducha cuando llamaste. — I was in the shower when you called.
:::

:::cloze{sentence="Mi padre ___ al fútbol todos los sábados." blank="jugaba"}
:::

:::cloze{sentence="Leía en el sofá cuando ___ el teléfono." blank="sonó"}
:::

:::sort{groups="Imperfecto (background): hacía frío, había mucha gente, estaba cansado | Indefinido (event): sonó el teléfono, llegó el tren, se rompió el vaso"}
:::
""",
        ["imperfecto"],
        "es-imperfect",
        explains=["imperfecto"],
    ),
    page(
        "es-reflexive-verbs",
        "Me levanto: reflexive verbs",
        r"""
A reflexive verb has a pronoun that points back at the subject: *levantarse* is "to get (yourself) up". Dictionaries list these verbs with **-se** on the end.

| | levantarse |
| --- | --- |
| yo | me levanto |
| tú | te levantas |
| él, ella, usted | se levanta |
| nosotros | nos levantamos |
| vosotros | os levantáis |
| ellos, ellas, ustedes | se levantan |

In the perfect the pronoun goes before *haber*: *me he levantado*.

## Where the pronoun goes

- Before a conjugated verb: *Me ducho.*
- With an infinitive or a gerund, before the first verb or joined to the end: *Me voy a duchar* or *Voy a ducharme*; *Me estoy duchando* or *Estoy duchándome*.
- Joined to a positive command: *¡Levántate!* (Get up!) *¡Siéntate!* (Sit down!)

## The daily routine

Most of a morning is reflexive in Spanish: *me despierto* (I wake up), *me levanto*, *me ducho*, *me visto* (I get dressed), *me lavo los dientes*, and at night *me acuesto* (I go to bed).

For parts of the body and clothes Spanish uses *el* and *la*, not "my": *Me lavo el pelo* (I wash my hair), *Me pongo la chaqueta* (I put my jacket on).

## Same verb, new meaning

The pronoun often changes what a verb means:

| Without se | With se |
| --- | --- |
| ir, to go | irse, to leave |
| llamar, to call | llamarse, to be called |
| quedar, to arrange to meet | quedarse, to stay |
| dormir, to sleep | dormirse, to fall asleep |
| poner, to put | ponerse, to put on (clothes) |

## Each other

In the plural, *nos*, *os* and *se* can also mean "each other": *Nos vemos mañana* (See you tomorrow, literally "we see each other"), *Se quieren mucho* (They love each other very much).

:::examples
- Me levanto a las siete y desayuno en casa. — I get up at seven and have breakfast at home.
- ¿A qué hora te acuestas? — What time do you go to bed?
- Nos vamos de vacaciones mañana. — We're going on holiday tomorrow.
- Mis hijos se visten solos. — My children get dressed by themselves.
:::

:::predict{prompt="ella (despertarse)" answer="se despierta"}
:::

:::cloze{sentence="Yo siempre ___ ducho por la noche." blank="me"}
:::
""",
        ["reflexivos"],
        "es-reflexive-verbs",
        explains=["reflexivos"],
    ),
    page(
        "es-object-pronouns",
        "Lo, la, le: object pronouns",
        r"""
A **direct object** answers "what?" or "whom?": *I see* **it**. An **indirect object** answers "to whom?" or "for whom?": *I give* **her** *the book*. Spanish has a pronoun for each.

| English | Direct | Indirect |
| --- | --- | --- |
| me | me | me |
| you (tú) | te | te |
| him, it, you (usted, m) | lo | le |
| her, it, you (usted, f) | la | le |
| us | nos | nos |
| you (vosotros) | os | os |
| them, you (ustedes, m) | los | les |
| them, you (ustedes, f) | las | les |

Only the third person differs. *Lo* and *la* follow the gender of the thing: *¿El libro? Lo leo esta noche.* *¿La película? La vi ayer.*

## Where they go

The same rules as for reflexive pronouns: before a conjugated verb (*Te llamo mañana*), and before the first verb or joined to an infinitive, a gerund or a positive command (*Lo quiero ver* or *Quiero verlo*; *¡Cómelo!*).

## Two pronouns together

The indirect one comes first: *Me lo das* (You give it to me). When *le* or *les* meets *lo*, *la*, *los* or *las*, it becomes **se**: you say *se lo doy*, never *le lo doy*.

## Saying it twice

Spanish often names the indirect object and uses the pronoun too: *Le doy el libro a María*, *Les escribo a mis padres*. That isn't a mistake; it's normal.

## Lo for an idea

*Lo* also stands for a whole statement: *Ya lo sé* (I know), *No lo creo* (I don't think so).

## Le for a man

In much of Spain, people use *le* instead of *lo* for a man or boy: *¿Has visto a Pedro? —Sí, le vi ayer.* The Spanish Academy accepts it. Latin America says *lo vi*, and for things everyone says *lo*.

:::examples
- Te llamo esta noche. — I'll call you tonight.
- ¿Le has dicho la verdad a tu padre? — Have you told your father the truth?
- Las flores son para ti: te las he comprado en el mercado. — The flowers are for you: I bought them for you at the market.
- ¿Las gafas? No las encuentro. — My glasses? I can't find them.
:::

:::cloze{sentence="—¿Has comprado el pan? —Sí, ___ he comprado esta mañana." blank="lo"}
:::

:::cloze{sentence="¿El regalo para mamá? Mañana ___ lo doy." blank="se"}
:::
""",
        ["pronombres-objeto"],
        "es-object-pronouns",
        explains=["pronombres-objeto"],
    ),
    page(
        "es-future",
        "Comeré: the future",
        r"""
The **futuro** adds one set of endings to the whole infinitive. The endings are the same for -ar, -er and -ir verbs.

| | hablar | comer | vivir |
| --- | --- | --- | --- |
| yo | hablaré | comeré | viviré |
| tú | hablarás | comerás | vivirás |
| él, ella, usted | hablará | comerá | vivirá |
| nosotros | hablaremos | comeremos | viviremos |
| vosotros | hablaréis | comeréis | viviréis |
| ellos, ellas, ustedes | hablarán | comerán | vivirán |

Every form except nosotros carries a written accent.

## Irregular stems

Twelve common verbs shorten or change the infinitive. The endings stay the same.

| Verb | Stem | yo |
| --- | --- | --- |
| tener | tendr- | tendré |
| poner | pondr- | pondré |
| salir | saldr- | saldré |
| venir | vendr- | vendré |
| poder | podr- | podré |
| saber | sabr- | sabré |
| querer | querr- | querré |
| haber | habr- | habrá (there will be) |
| hacer | har- | haré |
| decir | dir- | diré |

## Ir a or the future?

For plans, conversation prefers *ir a* + infinitive: *Voy a cenar con Ana.* The future is for predictions, promises and more formal speech: *Mañana lloverá en el norte.* *Te lo devolveré, te lo prometo.*

## Guessing about now

The future also says what is probably true at this moment: *—¿Dónde está Luis? —Estará en el trabajo.* (He's probably at work.) *¿Qué hora será?* (I wonder what time it is.)

## After si

After *si* (if), Spanish uses the present, as English does: *Si llueve, nos quedaremos en casa.* (If it rains, we'll stay at home.) After *cuando* about the future, Spanish needs the subjunctive, which comes in the B1 pack.

:::examples
- Mañana hará sol en todo el país. — Tomorrow it'll be sunny across the country.
- El año que viene viviremos en Valencia. — Next year we'll live in Valencia.
- ¿Vendrás a mi cumpleaños? — Will you come to my birthday?
:::

:::predict{prompt="nosotros (salir)" answer="saldremos"}
:::

:::predict{prompt="ellos (hacer)" answer="harán"}
:::
""",
        ["futuro"],
        "es-future",
        explains=["futuro"],
    ),
    page(
        "es-comparisons",
        "Más que, tan como: comparing",
        r"""
## More and less

**Más** + adjective + **que** is "more ... than", and **menos** ... **que** is "less ... than":

- *Madrid es más grande que Sevilla.* (Madrid is bigger than Seville.)
- *Este piso es menos caro que el otro.* (This flat is less expensive than the other one.)

Before a number, use **de**: *Tiene más de cien años.* (It's over a hundred years old.)

## As ... as

**Tan** + adjective + **como**: *Pedro es tan simpático como su padre.*

With a noun it's **tanto**, which agrees: *No tengo tanto dinero como tú*, *No hay tanta gente como ayer*. After a verb it's plain *tanto como*: *Trabajo tanto como tú.*

## Four irregular ones

| Adjective | Comparative | English |
| --- | --- | --- |
| bueno, bien | mejor | better |
| malo, mal | peor | worse |
| grande (in age) | mayor | older |
| pequeño (in age) | menor | younger |

*Mi hermano mayor* is "my older brother". For size, say *más grande* and *más pequeño*.

## The most

Put **el**, **la**, **los** or **las** before the comparative, and use **de** where English says "in": *Es la ciudad más bonita de España.* (It's the most beautiful city in Spain.) *Es el mejor restaurante del barrio.*

## -ísimo

To say "really, extremely", drop the last vowel and add **-ísimo**, which agrees like any adjective: *guapísimo*, *carísima*, *muchísimos*. The spelling keeps the sound: *rico*, *riquísimo*; *largo*, *larguísimo*.

:::examples
- Mi hermana es mayor que yo. — My sister is older than me.
- El tren es más rápido que el autobús. — The train is faster than the bus.
- Hoy no hace tanto frío como ayer. — It isn't as cold today as yesterday.
- La comida está buenísima. — The food is absolutely delicious.
:::

:::cloze{sentence="Mi hermana es ___ alta como yo." blank="tan"}
:::

:::cloze{sentence="Este hotel es el ___ caro de la ciudad." blank="más"}
:::
""",
        ["comparativos"],
        "es-comparisons",
        explains=["comparativos"],
    ),
    page(
        "es-por-para",
        "Por or para",
        r"""
Both often translate as "for", but they don't swap. **Para** looks ahead to a goal; **por** looks back at a cause, or at the way through.

## Para

| Use | Example |
| --- | --- |
| purpose, "in order to" | Estudio español para viajar. |
| who it's for | Esta carta es para usted. |
| where you're heading | Mañana salgo para Lima. |
| a deadline | Necesito el informe para el lunes. |
| an opinion | Para mí, es el mejor. |

## Por

| Use | Example |
| --- | --- |
| cause, reason | No salimos por la lluvia. |
| through, along, around | Paseamos por el parque. |
| means | Te llamo por teléfono. |
| exchange, price | Lo compré por veinte euros. |
| "per" | Voy al gimnasio tres veces por semana. |
| a part of the day | Trabajo por la mañana. |
| thanks | Gracias por todo. |

## One sentence, two meanings

*Lo hago para ti* is "I'm doing it for you", so you'll get it. *Lo hago por ti* is "I'm doing it because of you", or in your place.

## Set phrases with por

*por favor* (please), *por eso* (that's why), *por fin* (at last), *por supuesto* (of course), *por ejemplo* (for example), *por cierto* (by the way).

:::examples
- Trabajo para una empresa alemana. — I work for a German company.
- Vamos a dar un paseo por el centro. — Let's go for a walk around the centre.
- Gracias por la invitación. — Thanks for the invitation.
:::

:::cloze{sentence="Voy a la farmacia ___ comprar aspirinas." blank="para"}
:::

:::cloze{sentence="Te mando las fotos ___ correo." blank="por"}
:::

:::cloze{sentence="El tren ___ Sevilla sale a las diez." blank="para"}
:::
""",
        ["preposiciones"],
        "es-por-para",
        explains=["preposiciones"],
    ),
    page(
        "es-time-weather",
        "Hace frío, hace dos años",
        r"""
## The weather

Spanish talks about the weather with **hacer**, **hay**, **estar** and two verbs of its own:

| Spanish | English |
| --- | --- |
| hace frío, hace calor | it's cold, it's hot |
| hace sol | it's sunny |
| hace viento | it's windy |
| hace buen tiempo, hace mal tiempo | the weather's nice, the weather's bad |
| hay niebla, hay tormenta | it's foggy, there's a storm |
| está nublado | it's cloudy |
| llueve (llover) | it's raining |
| nieva (nevar) | it's snowing |

*Frío* and *calor* are nouns here, so "very" is *mucho*, not *muy*: *hace mucho frío*. A person who feels cold says *tengo frío*.

*¿Qué tiempo hace?* asks what the weather is like. *Tiempo* means both "weather" and "time".

South of the equator the seasons swap: in Buenos Aires, Christmas is in summer.

## Hace: ago

**Hace** + a length of time means "ago": *Llegué hace dos días.* (I arrived two days ago.)

## Still going on

For something that started in the past and is still going on, English says "have been". Spanish uses the present, with any of three patterns:

- *Vivo aquí desde hace tres años.*
- *Hace tres años que vivo aquí.*
- *Llevo tres años aquí.*

All three mean "I've lived here for three years". Don't translate this "for" with *por*.

## Other time words

| Word | Meaning | Example |
| --- | --- | --- |
| desde | since (a point in time) | Estoy aquí desde las ocho. |
| durante | for, during | Dormí durante ocho horas. |
| dentro de | in (from now) | El tren sale dentro de diez minutos. |
| en | in (the time it takes) | Hice el trabajo en dos horas. |

:::examples
- Hoy hace mucho calor. — It's very hot today.
- En invierno nieva mucho en la sierra. — In winter it snows a lot in the mountains.
- Estudio español desde hace un año. — I've been learning Spanish for a year.
:::

:::cloze{sentence="Mis abuelos se casaron ___ cincuenta años." blank="hace"}
:::

:::cloze{sentence="En agosto ___ mucho calor en Sevilla." blank="hace"}
:::
""",
        ["time", "weather"],
        "es-time-weather",
        explains=["time", "weather"],
    ),
    page(
        "es-gender-patterns",
        "El or la? Spotting the gender",
        r"""
Every Spanish noun is masculine or feminine, and the articles and adjectives around it follow. The ending usually tells you which.

## Usually masculine

- **-o**: *el libro*, *el vaso*.
- **-or**: *el color*, *el dolor*, *el ordenador*.
- **-aje**: *el viaje*, *el garaje*.
- **-ma**, in words that come from Greek: *el problema*, *el tema*, *el programa*, *el idioma*.
- Days, months, languages, colours, rivers and seas: *el lunes*, *el español*, *el rojo*, *el Ebro*, *el Mediterráneo*.

## Usually feminine

- **-a**: *la casa*, *la maleta*.
- **-ción** and **-sión**: *la canción*, *la televisión*.
- **-dad**, **-tad** and **-tud**: *la ciudad*, *la libertad*, *la salud*.
- **-umbre**: *la costumbre*.
- Letters of the alphabet: *la a*, *la be*.

## The exceptions to learn

| Masculine, though it ends in -a | Feminine, though it ends in -o |
| --- | --- |
| el día | la mano |
| el mapa | la foto |
| el planeta | la moto |
| el sofá | la radio |

*Foto* and *moto* are short for *la fotografía* and *la motocicleta*.

## El agua: feminine with el

A feminine noun that starts with a stressed **a-** or **ha-** takes *el* and *un* in the singular, so that two a sounds don't run together: *el agua*, *un aula*, *el hambre*, *el águila*, *el alma*.

They're still feminine. Adjectives agree in the feminine (*el agua fría*), the plural takes *las* (*las aguas*), and other words in front stay feminine (*esta agua*, *mucha hambre*). If the first a isn't stressed, nothing changes: *la abuela*, *la amiga*.

## People

Many words for people have two forms: *el profesor*, *la profesora*; *el médico*, *la médica*. Words in **-ista** and **-nte** usually change only the article: *el artista*, *la artista*; *el estudiante*, *la estudiante*.

A few nouns change their meaning with their gender: *el capital* is money, *la capital* is a capital city.

:::examples
- El problema es que no tengo tiempo. — The problem is that I don't have time.
- Tengo mucha hambre. — I'm really hungry.
- La foto del viaje es preciosa. — The photo from the trip is lovely.
- El aula está vacía. — The classroom is empty.
:::

:::sort{groups="Masculino (el): sistema, paisaje, calor, clima | Femenino (la): estación, verdad, actitud, información"}
:::

:::cloze{sentence="El agua está muy ___." blank="fría"}
:::
""",
        ["género", "masculino", "femenino"],
        "es-gender-patterns",
        explains=["género", "masculino", "femenino"],
    ),
    page(
        "es-gerund",
        "Estoy comiendo: right now",
        r"""
**Estar** + the gerund says that something is going on right now, like English "be + -ing": *Estoy comiendo* (I'm eating).

## The gerund

| Verb | Ending | Gerund |
| --- | --- | --- |
| -ar | -ando | hablar, hablando |
| -er, -ir | -iendo | comer, comiendo; vivir, viviendo |

After a vowel, -iendo becomes **-yendo**: *leer*, *leyendo*; *oír*, *oyendo*; *traer*, *trayendo*; *ir*, *yendo*.

**-ir** verbs with a stem change switch e to i and o to u: *pedir*, *pidiendo*; *decir*, *diciendo*; *venir*, *viniendo*; *sentir*, *sintiendo*; *morir*, *muriendo*.

The gerund never changes for gender or number.

## When to use it

- For what's happening at this moment: *—¿Qué haces? —Estoy cocinando.*
- For something going on these days: *Este mes estoy trabajando mucho.*

## Less than in English

- Not for the future. "I'm leaving tomorrow" is *Me voy mañana*, in the present.
- Not for positions and clothes. "I'm sitting" is *Estoy sentado*; "she's wearing a coat" is *Lleva un abrigo*.
- Often not even for now: *¿Qué haces?* is the usual way to ask "What are you doing?"

## Pronouns

The pronoun goes before *estar* or on the end of the gerund, which then needs an accent: *Me estoy duchando* or *Estoy duchándome*.

## Seguir and llevar

- **Seguir** + gerund is "still" or "keep on": *Sigo viviendo en Madrid.* (I still live in Madrid.)
- **Llevar** + a time + gerund is "have been doing": *Llevo dos horas esperando.* (I've been waiting for two hours.)

:::examples
- Estoy hablando por teléfono, ahora te llamo. — I'm on the phone, I'll call you back.
- Está lloviendo mucho. — It's raining hard.
- ¿Sigues trabajando en el banco? — Are you still working at the bank?
- Llevamos una hora esperando el autobús. — We've been waiting for the bus for an hour.
:::

:::predict{prompt="tú (escribir)" answer="estás escribiendo"}
:::

:::predict{prompt="ellos (dormir)" answer="están durmiendo"}
:::
""",
        ["gerundio"],
        "es-gerund",
        explains=["gerundio"],
    ),
]

NOUNS = nouns(
    """
ropa | f | clothes | clothing | - | Tengo que lavar la ropa. | I need to do the washing. | Always singular: la ropa means "clothes".
camisa | f | shirt | clothing | | Llevas una camisa muy elegante. | You're wearing a very smart shirt.
camiseta | f | T-shirt | clothing | | En verano solo llevo camisetas. | In summer I only wear T-shirts. | Mexico says la playera; Argentina, la remera.
pantalón | m | trousers | clothing | | Estos pantalones me quedan grandes. | These trousers are too big for me. | One pair can be el pantalón or los pantalones.
falda | f | skirt | clothing | | Me he comprado una falda azul. | I've bought a blue skirt.
vestido | m | dress | clothing | | ¡Qué vestido tan bonito! | What a lovely dress!
zapato | m | shoe | clothing | | Necesito unos zapatos para la boda. | I need some shoes for the wedding.
abrigo | m | coat | clothing | | Ponte el abrigo, que hace frío. | Put your coat on, it's cold.
chaqueta | f | jacket | clothing | | Esta chaqueta es de cuero. | This jacket is leather. | Mexico says la chamarra; Argentina, la campera.
jersey | m | jumper, sweater | clothing | jerséis | Mi abuela me hace un jersey cada invierno. | My grandmother knits me a jumper every winter. | Latin America: el suéter.
tiempo | m | weather; time | weather | | ¿Qué tiempo hace en Madrid? | What's the weather like in Madrid? | Also "time": no tengo tiempo. The time on the clock is la hora.
calor | m | heat | weather | - | ¡Qué calor hace hoy! | It's so hot today! | Hace calor: it's hot. Tengo calor: I'm hot.
lluvia | f | rain | weather | | Con esta lluvia no salimos. | We're not going out in this rain.
nieve | f | snow | weather | - | Los niños juegan en la nieve. | The children are playing in the snow.
viento | m | wind | weather | | Hoy hace mucho viento. | It's very windy today.
clima | m | climate | weather | | El clima de Canarias es muy suave. | The Canary Islands have a very mild climate. | Masculine, though it ends in -a. In Latin America it also means "the weather".
primavera | f | spring | weather | | En primavera el campo está precioso. | The countryside is beautiful in spring.
verano | m | summer | weather | | Este verano vamos a Galicia. | This summer we're going to Galicia.
otoño | m | autumn | weather | | En otoño llueve mucho en el norte. | It rains a lot in the north in autumn.
invierno | m | winter | weather | | El invierno en Madrid es frío y seco. | Winter in Madrid is cold and dry.
viaje | m | trip, journey | travel | | ¿Qué tal el viaje? | How was the trip?
billete | m | ticket; banknote | travel | | He comprado los billetes de tren por internet. | I've bought the train tickets online. | Latin America: el boleto or el pasaje. A ticket for a show is una entrada.
maleta | f | suitcase | travel | | Todavía no he hecho la maleta. | I still haven't packed. | Hacer la maleta: to pack.
pasaporte | m | passport | travel | | No olvides el pasaporte. | Don't forget your passport.
aeropuerto | m | airport | travel | | El aeropuerto está a veinte minutos del centro. | The airport is twenty minutes from the centre.
playa | f | beach | travel | | Pasamos el día en la playa. | We spent the day at the beach.
montaña | f | mountain | travel | | Los fines de semana vamos a la montaña. | At weekends we go to the mountains.
mapa | m | map | travel | | ¿Tienes un mapa de la ciudad? | Do you have a map of the city? | Masculine, though it ends in -a.
equipaje | m | luggage | travel | - | Solo llevo equipaje de mano. | I've only got hand luggage.
tren | m | train | transport | | El tren sale del andén tres. | The train leaves from platform three.
avión | m | plane | transport | | Odio viajar en avión. | I hate flying.
autobús | m | bus | transport | autobuses | El autobús para delante de mi casa. | The bus stops outside my house. | Mexico says el camión; Argentina, el colectivo; the Canaries and the Caribbean, la guagua.
metro | m | underground, metro | transport | | Voy al trabajo en metro. | I go to work on the metro.
moto | f | motorbike | transport | | Mi hermano tiene una moto roja. | My brother has a red motorbike. | Feminine: it's short for la motocicleta.
oficina | f | office | work | | Trabajo en una oficina en el centro. | I work in an office in the centre.
empresa | f | company, firm | work | | Es una empresa pequeña de cinco personas. | It's a small company of five people.
jefe | m | boss | work | | Mi jefe me ha dado el viernes libre. | My boss has given me Friday off. | A woman boss is la jefa.
reunión | f | meeting | work | | Tengo una reunión a las diez. | I have a meeting at ten.
ordenador | m | computer | work | | Mi ordenador es muy lento. | My computer is very slow. | Latin America: la computadora.
correo | m | email; post | work | | Te mando un correo con los detalles. | I'll send you an email with the details. | Correos is the post office.
cliente | m | customer, client | work | | Hoy tenemos muchos clientes. | We've got a lot of customers today. | A woman is la cliente or la clienta.
compañero | m | colleague; classmate | work | | Como con mis compañeros de trabajo. | I have lunch with my workmates. | Compañero de piso: flatmate.
examen | m | exam | work | exámenes | Mañana tengo un examen de inglés. | I have an English exam tomorrow.
aula | f | classroom | work | | El aula está en el segundo piso. | The classroom is on the second floor. | Feminine, but el aula: like el agua, it starts with a stressed a.
problema | m | problem | work | | No hay ningún problema. | There's no problem at all. | Masculine, though it ends in -a.
médico | m | doctor | health | | Tengo que ir al médico. | I have to go to the doctor's. | A woman doctor is la médica.
salud | f | health | health | - | Lo más importante es la salud. | Health is what matters most.
dolor | m | pain, ache | health | | Tengo dolor de cabeza. | I've got a headache.
fiebre | f | fever, temperature | health | - | El niño tiene fiebre. | The child has a temperature.
medicamento | m | medicine, drug | health | | Tómate este medicamento dos veces al día. | Take this medicine twice a day.
receta | f | prescription; recipe | health | | Este medicamento no necesita receta. | This medicine doesn't need a prescription. | Also a recipe: la receta de la paella.
espalda | f | back | health | | Mi padre tiene problemas de espalda. | My father has back problems.
estómago | m | stomach | health | | Me duele el estómago. | I've got a stomach ache.
película | f | film | leisure | | ¿Vemos una película esta noche? | Shall we watch a film tonight?
cine | m | cinema | leisure | | Vamos al cine el viernes. | We're going to the cinema on Friday.
música | f | music | leisure | - | ¿Qué música te gusta? | What music do you like?
fútbol | m | football | leisure | - | El fútbol es el deporte más popular de España. | Football is Spain's most popular sport.
deporte | m | sport | leisure | | Hago deporte tres veces por semana. | I do sport three times a week.
fiesta | f | party; public holiday | leisure | | El sábado hay una fiesta en casa de Luis. | There's a party at Luis's place on Saturday. | Also a public holiday: mañana es fiesta.
concierto | m | concert | leisure | | El concierto empieza a las nueve. | The concert starts at nine.
canción | f | song | leisure | | Esta canción me encanta. | I love this song.
foto | f | photo | leisure | | ¿Nos haces una foto? | Could you take a photo of us? | Feminine: it's short for la fotografía.
precio | m | price | shopping | | El precio incluye el desayuno. | The price includes breakfast.
euro | m | euro | shopping | | Son quince euros. | That's fifteen euros.
tarjeta | f | card | shopping | | ¿Aceptan tarjeta? | Do you take cards?
talla | f | size (of clothes) | shopping | | ¿Qué talla usa? | What size do you take? | A shoe size is el número.
supermercado | m | supermarket | shopping | | El supermercado cierra a las diez. | The supermarket closes at ten.
cambio | m | change; exchange | shopping | | Aquí tiene el cambio. | Here's your change.
bolsa | f | bag | shopping | | ¿Quiere una bolsa? | Would you like a bag? | A handbag is un bolso.
miedo | m | fear | feelings | | Mi hija tiene miedo a la oscuridad. | My daughter is afraid of the dark. | Tener miedo: to be afraid.
alegría | f | joy, happiness | feelings | | ¡Qué alegría verte! | How lovely to see you!
hambre | f | hunger | feelings | - | ¿Tienes hambre? | Are you hungry? | Feminine, but el hambre, like el agua. Tener hambre: to be hungry.
sueño | m | sleepiness; dream | feelings | | Tengo mucho sueño. | I'm really sleepy. | Also a dream: un sueño.
prisa | f | hurry | feelings | - | Lo siento, tengo prisa. | Sorry, I'm in a hurry. | Much of Latin America says apuro.
suerte | f | luck | feelings | - | ¡Buena suerte con el examen! | Good luck with the exam!
salón | m | living room | home | | Vemos la tele en el salón. | We watch TV in the living room. | Latin America: la sala.
dormitorio | m | bedroom | home | | El piso tiene tres dormitorios. | The flat has three bedrooms.
ducha | f | shower | home | | La ducha no funciona. | The shower doesn't work.
nevera | f | fridge | home | | Hay cerveza en la nevera. | There's beer in the fridge. | Latin America: el refrigerador, or la heladera in Argentina.
sofá | m | sofa | home | | Me quedo dormido en el sofá. | I fall asleep on the sofa.
armario | m | wardrobe; cupboard | home | | La ropa está en el armario. | The clothes are in the wardrobe.
comida | f | food; lunch | food | | La comida española es muy variada. | Spanish food is very varied. | In Spain also the main meal, eaten around two.
patata | f | potato | food | | La tortilla lleva huevos y patatas. | Spanish omelette is made with eggs and potatoes. | Latin America: la papa.
tomate | m | tomato | food | | El gazpacho se hace con tomate. | Gazpacho is made with tomatoes.
verdura | f | vegetables | food | | Tienes que comer más verdura. | You should eat more vegetables.
naranja | f | orange | food | | Estas naranjas son de Valencia. | These oranges are from Valencia.
sopa | f | soup | food | | En invierno hago sopa de pollo. | In winter I make chicken soup.
pájaro | m | bird | animals | | Por la mañana oigo los pájaros. | In the morning I hear the birds.
caballo | m | horse | animals | | Mi prima monta a caballo. | My cousin rides horses.
flor | f | flower | nature | | Te he comprado unas flores. | I've bought you some flowers.
río | m | river | nature | | El río Ebro pasa por Zaragoza. | The River Ebro flows through Zaragoza.
mar | m | sea | nature | | Desde mi ventana se ve el mar. | You can see the sea from my window. | Usually el mar; poets and sailors say la mar.
pueblo | m | village, small town | city | | Mis abuelos viven en un pueblo de Asturias. | My grandparents live in a village in Asturias. | Also "a people": el pueblo español.
"""
)

VERBS = [
    verb("levantarse", "to get up", [],
         example="Me levanto a las siete todos los días.", example_en="I get up at seven every day."),
    verb("despertarse", "to wake up", [], stem="e>ie",
         example="Los domingos me despierto tarde.", example_en="On Sundays I wake up late."),
    verb("ducharse", "to have a shower", [],
         example="Me ducho por la mañana.", example_en="I shower in the morning."),
    verb("vestirse", "to get dressed", [], stem="e>i",
         example="Mi hijo ya se viste solo.", example_en="My son gets dressed by himself now."),
    verb("acostarse", "to go to bed", [], stem="o>ue",
         example="Nos acostamos muy tarde los sábados.", example_en="We go to bed very late on Saturdays."),
    verb("llamarse", "to be called", [],
         example="Mi perro se llama Toby.", example_en="My dog's called Toby.",
         note="Literally \"to call yourself\": me llamo Ana."),
    verb("sentirse", "to feel", [], stem="e>ie",
         example="Hoy no me siento muy bien.", example_en="I don't feel very well today."),
    verb("quedarse", "to stay", [],
         example="Este verano nos quedamos en casa.", example_en="This summer we're staying at home.",
         note="Without se, quedar is to arrange to meet: ¿quedamos a las ocho?"),
    verb("irse", "to leave, to go away", [], **IR,
         example="Me voy, que es muy tarde.", example_en="I'm off, it's very late.",
         note="Ir is to go somewhere; irse is to leave where you are."),
    verb("lavarse", "to wash (yourself)", [],
         example="Me lavo el pelo cada dos días.", example_en="I wash my hair every other day."),
    verb("preocuparse", "to worry", [],
         example="Mi madre se preocupa por todo.", example_en="My mother worries about everything.",
         note="No te preocupes: don't worry."),
    verb("divertirse", "to have a good time", [], stem="e>ie",
         example="Los niños se divierten mucho en la piscina.", example_en="The children have a great time in the pool."),
    verb("oír", "to hear", [],
         present="oigo oyes oye oímos oís oyen",
         pret="oí oíste oyó oímos oísteis oyeron",
         pp="oído",
         example="¿Me oyes bien?", example_en="Can you hear me all right?",
         note="Oír is to hear; escuchar is to listen."),
    verb("traer", "to bring", [],
         present="traigo traes trae traemos traéis traen",
         pret_stem="traj",
         pp="traído",
         example="¿Qué te traigo de Granada?", example_en="What shall I bring you from Granada?"),
    verb("conducir", "to drive", [], zc=True, pret_stem="conduj",
         example="Mi hermana conduce muy bien.", example_en="My sister drives very well.",
         note="Latin America mostly says manejar."),
    verb("seguir", "to follow; to keep on", [], stem="e>i",
         present="sigo sigues sigue seguimos seguís siguen",
         subj="siga sigas siga sigamos sigáis sigan",
         example="Siga todo recto y luego a la derecha.", example_en="Go straight on and then turn right.",
         note="Seguir + gerund is \"still\": sigo viviendo aquí."),
    verb("devolver", "to give back, to return", [], stem="o>ue", pp="devuelto",
         example="Te devuelvo el libro mañana.", example_en="I'll give you the book back tomorrow."),
    verb("romper", "to break", [], pp="roto",
         example="El niño ha roto un vaso.", example_en="The little boy has broken a glass."),
    verb("pagar", "to pay (for)", [],
         example="Hoy pago yo.", example_en="It's on me today.",
         note="No \"for\" in Spanish: pagar la cena is to pay for dinner."),
    verb("viajar", "to travel", [],
         example="Me encanta viajar en tren.", example_en="I love travelling by train."),
    verb("esperar", "to wait (for); to hope", [],
         example="Te espero en la puerta del cine.", example_en="I'll wait for you outside the cinema."),
    verb("ayudar", "to help", [],
         example="¿Te ayudo con las bolsas?", example_en="Shall I help you with the bags?"),
    verb("cambiar", "to change", [],
         example="Quiero cambiar estos zapatos.", example_en="I'd like to change these shoes."),
    verb("olvidar", "to forget", [],
         example="Siempre olvido su nombre.", example_en="I always forget her name.",
         note="Also olvidarse de: me he olvidado de las llaves."),
    verb("encontrar", "to find", [], stem="o>ue",
         example="No encuentro mi móvil.", example_en="I can't find my phone."),
    verb("perder", "to lose; to miss", [], stem="e>ie",
         example="Si no te das prisa, vas a perder el tren.", example_en="If you don't hurry, you'll miss the train."),
    verb("cerrar", "to close", [], stem="e>ie",
         example="Las tiendas cierran a las nueve.", example_en="The shops close at nine."),
    verb("preguntar", "to ask (a question)", [],
         example="Voy a preguntar el precio.", example_en="I'm going to ask the price.",
         note="To ask for something is pedir."),
    verb("recordar", "to remember; to remind", [], stem="o>ue",
         example="No recuerdo dónde he aparcado.", example_en="I can't remember where I've parked."),
    verb("cocinar", "to cook", [],
         example="Mi padre cocina muy bien.", example_en="My father is a very good cook."),
    verb("limpiar", "to clean", [],
         example="Los sábados limpiamos la casa.", example_en="On Saturdays we clean the house."),
    verb("llevar", "to take, to carry; to wear", [],
         example="Lleva un vestido rojo.", example_en="She's wearing a red dress.",
         note="Traer is to bring here; llevar is to take there."),
    verb("dejar", "to leave; to lend; to let", [],
         example="He dejado las llaves en la mesa.", example_en="I've left the keys on the table."),
    verb("ganar", "to win; to earn", [],
         example="El Betis ganó el partido.", example_en="Betis won the match."),
    verb("doler", "to hurt", [], stem="o>ue",
         example="Me duele mucho la cabeza.", example_en="I've got a bad headache.",
         note="Works like gustar: me duelen los pies, my feet hurt."),
    verb("nadar", "to swim", [],
         example="Nado en el mar todos los veranos.", example_en="I swim in the sea every summer."),
    verb("bailar", "to dance", [],
         example="¿Sabes bailar salsa?", example_en="Can you dance salsa?"),
    verb("cantar", "to sing", [],
         example="Mi abuela canta en un coro.", example_en="My grandmother sings in a choir."),
    verb("descansar", "to rest", [],
         example="Necesitas descansar un poco.", example_en="You need to rest a bit."),
    verb("terminar", "to finish", [],
         example="La clase termina a las doce.", example_en="The class finishes at twelve."),
    verb("explicar", "to explain", [],
         example="¿Me lo puedes explicar otra vez?", example_en="Can you explain it to me again?"),
]

ADJECTIVES = adjectives(
    """
feliz, feliz, felices, felices | happy | Estoy muy feliz con mi nuevo trabajo. | I'm very happy with my new job. | Takes ser or estar.
triste, triste, tristes, tristes | sad | ¿Por qué estás triste? | Why are you sad?
enfadado, enfadada, enfadados, enfadadas | angry | Mi padre está enfadado conmigo. | My father is angry with me. | Latin America: enojado.
nervioso, nerviosa, nerviosos, nerviosas | nervous | Estoy nerviosa por la entrevista. | I'm nervous about the interview.
preocupado, preocupada, preocupados, preocupadas | worried | Estamos preocupados por el abuelo. | We're worried about Grandad.
tranquilo, tranquila, tranquilos, tranquilas | calm, quiet | Vivo en un barrio muy tranquilo. | I live in a very quiet neighbourhood. | Tranquilo on its own: don't worry, calm down.
aburrido, aburrida, aburridos, aburridas | bored; boring | Estoy aburrido: no hay nada en la tele. | I'm bored: there's nothing on TV. | Estar aburrido is bored; ser aburrido is boring.
divertido, divertida, divertidos, divertidas | fun, funny | La película es muy divertida. | The film is really funny.
serio, seria, serios, serias | serious | Tu hermano es muy serio. | Your brother is very serious.
tímido, tímida, tímidos, tímidas | shy | De pequeña era muy tímida. | She was very shy as a child.
perezoso, perezosa, perezosos, perezosas | lazy | Mi gato es muy perezoso. | My cat is very lazy. | Spain also says vago.
amable, amable, amables, amables | kind | Gracias, es usted muy amable. | Thank you, that's very kind of you.
largo, larga, largos, largas | long | Es un viaje muy largo. | It's a very long journey. | Not "large": that's grande.
corto, corta, cortos, cortas | short (in length) | Llevo el pelo corto. | I have short hair. | A short person is bajo.
rápido, rápida, rápidos, rápidas | fast, quick | El AVE es un tren muy rápido. | The AVE is a very fast train.
lento, lenta, lentos, lentas | slow | Internet va muy lento hoy. | The internet is really slow today.
limpio, limpia, limpios, limpias | clean | La cocina está limpia. | The kitchen is clean.
sucio, sucia, sucios, sucias | dirty | Tienes las manos sucias. | Your hands are dirty.
lleno, llena, llenos, llenas | full | El restaurante está lleno. | The restaurant is full.
vacío, vacía, vacíos, vacías | empty | La nevera está vacía. | The fridge is empty.
enfermo, enferma, enfermos, enfermas | ill, sick | Hoy no voy a trabajar, estoy enfermo. | I'm not going to work today, I'm ill.
mejor, mejor, mejores, mejores | better; best | Este café es mejor que el otro. | This coffee is better than the other one. | The comparative of bueno and bien.
peor, peor, peores, peores | worse; worst | Hoy el tráfico está peor que ayer. | The traffic is worse today than yesterday. | The comparative of malo and mal.
mayor, mayor, mayores, mayores | older; bigger | Mi hermana mayor vive en Chile. | My older sister lives in Chile. | Also "elderly": las personas mayores.
menor, menor, menores, menores | younger; smaller | Soy el menor de cuatro hermanos. | I'm the youngest of four.
""",
    ["feelings"],
)

PHRASES = phrases(
    """
¡qué bien! | great!, how nice! | —Mañana no hay clase. —¡Qué bien! | "There's no class tomorrow." "Great!"
¡qué pena! | what a shame! | ¿No puedes venir? ¡Qué pena! | You can't come? What a shame!
¡qué suerte! | how lucky! | ¿Te vas a Cuba? ¡Qué suerte! | You're off to Cuba? Lucky you!
¿en serio? | really? | —Me caso en junio. —¿En serio? | "I'm getting married in June." "Really?"
no pasa nada | it doesn't matter, don't worry | —Perdona, llego tarde. —No pasa nada. | "Sorry I'm late." "Don't worry about it." | nothing happens
me da igual | I don't mind | —¿Pizza o pasta? —Me da igual. | "Pizza or pasta?" "I don't mind." | it gives me the same
depende | it depends | —¿Vienes mañana? —Depende del tiempo. | "Are you coming tomorrow?" "It depends on the weather."
a lo mejor | maybe | A lo mejor vamos a la playa el domingo. | Maybe we'll go to the beach on Sunday. | at the best
por supuesto | of course | —¿Me ayudas? —Por supuesto. | "Will you help me?" "Of course."
¡qué va! | not at all!, no way! | —¿Estás cansado? —¡Qué va! | "Are you tired?" "Not at all!" | | Very common in Spain.
menos mal | thank goodness | Menos mal que has traído el paraguas. | Thank goodness you brought the umbrella. | less bad
ya veremos | we'll see | —¿Vamos a ganar? —Ya veremos. | "Are we going to win?" "We'll see."
¡enhorabuena! | congratulations! | ¿Has aprobado? ¡Enhorabuena! | You passed? Congratulations! | | For an achievement. Latin America says ¡felicitaciones!
¡felicidades! | happy birthday!, congratulations! | ¡Felicidades! ¿Cuántos años cumples? | Happy birthday! How old are you today? | happinesses
¡que te mejores! | get well soon! | Descansa mucho y que te mejores. | Get plenty of rest, and get well soon. | that you get better
¡buen viaje! | have a good trip! | Adiós, ¡buen viaje! | Bye, have a good trip!
¡cuidado! | careful!, watch out! | ¡Cuidado, que quema! | Careful, it's hot!
¿qué te pasa? | what's wrong? | Tienes mala cara. ¿Qué te pasa? | You don't look well. What's wrong? | what happens to you
ida y vuelta | return (ticket) | Un billete de ida y vuelta a Bilbao, por favor. | A return ticket to Bilbao, please. | going and coming back | One way is solo ida.
ya lo sé | I know | —Hace frío. —Ya lo sé. | "It's cold." "I know." | already I know it
no me lo creo | I can't believe it | ¿Has ganado la lotería? ¡No me lo creo! | You've won the lottery? I can't believe it!
me lo llevo | I'll take it | Este jersey me gusta. Me lo llevo. | I like this jumper. I'll take it.
te lo prometo | I promise | Mañana te devuelvo el dinero, te lo prometo. | I'll pay you back tomorrow, I promise.
¿me lo dejas? | can I borrow it? | Qué libro tan interesante. ¿Me lo dejas? | What an interesting book. Can I borrow it? | will you leave it to me?
¿te importa? | do you mind? | ¿Te importa si abro la ventana? | Do you mind if I open the window?
solo estoy mirando | I'm just looking | —¿Le puedo ayudar? —No, gracias, solo estoy mirando. | "Can I help you?" "No, thanks, I'm just looking."
¿qué estás haciendo? | what are you doing? | ¿Qué estás haciendo? Huele muy bien. | What are you making? It smells great.
""",
    ["expressions"],
)

CONNECTIVES = connectors(
    "connective",
    """
por eso | that's why, so | conn-consequence | Estaba cansado, por eso me fui a casa. | I was tired, so I went home.
así que | so | conn-consequence | Llueve mucho, así que nos quedamos en casa. | It's pouring, so we're staying in.
entonces | so, then | conn-consequence | —No tengo coche. —Entonces vamos en metro. | "I haven't got a car." "Then let's take the metro."
en cambio | whereas, on the other hand | conn-contrast | Mi hermano es muy alto; yo, en cambio, soy bajo. | My brother is very tall; I, on the other hand, am short.
de todas formas | anyway, in any case | conn-contrast | No sé si puedo ir, pero de todas formas te llamo. | I don't know if I can go, but I'll call you anyway.
al final | in the end | conn-sequence | Al final no fuimos a la playa. | In the end we didn't go to the beach.
incluso | even | conn-addition | Trabaja todos los días, incluso los domingos. | She works every day, even on Sundays.
""",
    ["conectores"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
mientras | while | conj-subordinating | Escucho la radio mientras cocino. | I listen to the radio while I cook. | Mientras cocino, escucho la radio.
como | as, since | conj-subordinating | Como llueve, nos quedamos en casa. | As it's raining, we're staying at home.
ya que | since, as | conj-subordinating | Ya que estás aquí, ¿me ayudas? | Since you're here, will you give me a hand? | ¿Me ayudas, ya que estás aquí?
ni | nor, or | conj-coordinating | No bebo ni fumo. | I don't drink or smoke.
""",
    ["conjunciones"],
)

ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

UNITS = [
    {
        "title": "He comido",
        "page_id": "es-perfect",
        "word_ids": ["romper", "olvidar", "perder", "encontrar", "dejar", "cambiar"],
    },
    {
        "title": "Comí",
        "page_id": "es-preterite",
        "word_ids": ["conducir", "traer", "oir", "pagar", "viajar", "ganar"],
    },
    {
        "title": "Comía",
        "page_id": "es-imperfect",
        "word_ids": ["nadar", "bailar", "cantar", "recordar", "ayudar", "cocinar"],
    },
    {
        "title": "Me levanto",
        "page_id": "es-reflexive-verbs",
        "word_ids": [
            "levantarse", "despertarse", "ducharse", "vestirse",
            "acostarse", "lavarse", "quedarse", "irse",
        ],
    },
    {
        "title": "Lo, la, le",
        "page_id": "es-object-pronouns",
        "word_ids": ["ya-lo-se", "no-me-lo-creo", "me-lo-llevo", "te-lo-prometo", "me-lo-dejas", "te-importa"],
    },
    {
        "title": "El futuro",
        "page_id": "es-future",
        "word_ids": ["devolver", "preguntar", "cerrar", "llevar", "limpiar", "esperar"],
    },
    {
        "title": "Más que, tan como",
        "page_id": "es-comparisons",
        "word_ids": ["mejor", "peor", "mayor", "menor", "largo", "corto", "rapido", "lento"],
    },
    {
        "title": "Por y para",
        "page_id": "es-por-para",
        "word_ids": ["viaje", "billete", "tren", "avion", "autobus", "metro"],
    },
    {
        "title": "Hace frío",
        "page_id": "es-time-weather",
        "word_ids": [
            "tiempo", "calor", "lluvia", "nieve", "viento",
            "primavera", "verano", "otono", "invierno",
        ],
    },
    {
        "title": "¿El o la?",
        "page_id": "es-gender-patterns",
        "word_ids": ["problema", "clima", "aula", "foto", "moto", "hambre", "mapa"],
    },
    {
        "title": "Estoy comiendo",
        "page_id": "es-gerund",
        "word_ids": ["seguir", "descansar", "terminar", "explicar", "solo-estoy-mirando", "que-estas-haciendo"],
    },
    {
        "title": "Cómo te sientes",
        "word_ids": [
            "feliz", "triste", "enfadado", "nervioso", "preocupado",
            "tranquilo", "aburrido", "divertido", "sentirse", "preocuparse",
        ],
    },
    {
        "title": "Cómo eres",
        "word_ids": ["serio", "timido", "perezoso", "amable", "limpio", "sucio", "lleno", "vacio", "enfermo"],
    },
]

LABELS = {**topic_labels(DELTA), "home": "En casa", "food": "La comida"}

PACK = pack(
    "es-everyday-v1",
    1,
    "es",
    "Español · Día a día (A2)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Práctica"),
)
