"""es-fluency-v1: B1. The subjunctive and the conditional, relative clauses,
impersonal se, register across Spain and Latin America, false friends and
idioms."""

from common import build_units, interleave, page, pack, topic, topic_labels
from es_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("relativos", "Pronombres relativos", "relative pronouns", ["presente"]),
    topic("se-impersonal", "Se impersonal", "se for people in general, and for accidents", ["presente"]),
    topic("registro", "Registro", "register: formal, spoken, slang", []),
    topic("falsos-amigos", "Falsos amigos", "false friends", []),
    topic("idioms", "Modismos", "idioms", []),
    topic("society", "Sociedad", "society and ideas", ["género"]),
]

PAGES = [
    page(
        "es-subjunctive",
        "Quiero que vengas: the subjunctive",
        r"""
The **subjuntivo** is a mood, not a tense. It marks what is wanted, felt, needed, doubted or not yet real. Spanish uses it every day, nearly always after **que**.

## Forming it

Take the yo form of the present, drop the **-o** and swap the vowel of the ending: -ar verbs take **e**, and -er and -ir verbs take **a**.

| | hablar (hablo) | comer (como) | vivir (vivo) |
| --- | --- | --- | --- |
| yo | hable | coma | viva |
| tú | hables | comas | vivas |
| él, ella, usted | hable | coma | viva |
| nosotros | hablemos | comamos | vivamos |
| vosotros | habléis | comáis | viváis |
| ellos, ellas, ustedes | hablen | coman | vivan |

Because it starts from the yo form, an irregular yo carries over: *hago*, *haga*; *digo*, *diga*; *pongo*, *ponga*; *conozco*, *conozca*. Stem changes stay as well (*quiera*, *pueda*, *duerma*), and -car, -gar and -zar verbs change their spelling: *busque*, *pague*, *empiece*.

Six verbs don't follow the rule:

| Verb | Subjunctive |
| --- | --- |
| ser | sea |
| estar | esté |
| ir | vaya |
| haber | haya |
| saber | sepa |
| dar | dé |

## What triggers it

The subjunctive goes after *que* when the first half of the sentence does one of these:

| The first half... | For example |
| --- | --- |
| wants something | quiero que, espero que, prefiero que, te pido que |
| reacts with a feeling | me alegra que, me molesta que, siento que |
| says it's needed or matters | es importante que, es necesario que, hace falta que |
| doubts or denies | no creo que, dudo que, no es verdad que |

*Quiero que vengas* (I want you to come). *Es importante que lo sepas* (It's important for you to know). *Dudo que llueva* (I doubt it'll rain).

With one subject there's no *que* and no subjunctive: *Quiero ir* (I want to go), but *Quiero que vayas* (I want you to go).

*Creo que* states what you hold to be true, so it takes the indicative: *Creo que tienes razón.* With *no* in front it takes the subjunctive: *No creo que sea verdad.*

## Ojalá

**Ojalá** (I hope, if only) always takes the subjunctive, with or without *que*: *¡Ojalá no llueva el sábado!* The word comes from Arabic and once meant "if God wills".

## Cuando about the future

When *cuando* looks ahead, the verb after it goes into the subjunctive, where English uses the present: *Cuando llegues, llámame* (Call me when you arrive). *Cuando sea mayor, viviré en el campo* (When I grow up, I'll live in the country).

About the past or a habit it takes the indicative: *Cuando llegué, estabas dormido.* *En cuanto* (as soon as) and *hasta que* (until) follow the same rule.

## Commands

Negative commands and usted commands are subjunctive forms: *No te preocupes* (Don't worry), *No me digas* (You don't say), *Pase, por favor* (Come in, please).

:::examples
- Espero que te guste el regalo. — I hope you like the present.
- Es importante que bebas mucha agua. — It's important to drink plenty of water.
- No creo que venga hoy. — I don't think he'll come today.
- Cuando tengas tiempo, llámame. — Call me when you have time.
:::

:::predict{prompt="que tú (tener)" answer="tengas"}
:::

:::cloze{sentence="Ojalá ___ buen tiempo el fin de semana." blank="haga"}
:::

:::cloze{sentence="Cuando ___ a casa, te mando un mensaje." blank="llegue"}
:::
""",
        ["subjuntivo"],
        "es-subjunctive",
        explains=["subjuntivo"],
    ),
    page(
        "es-conditional",
        "Comería: the conditional",
        r"""
The **condicional** is English "would": *comería* (I would eat). Like the future, it adds its endings to the whole infinitive, and the endings are those of the -er imperfect.

| | hablar | comer | vivir |
| --- | --- | --- | --- |
| yo | hablaría | comería | viviría |
| tú | hablarías | comerías | vivirías |
| él, ella, usted | hablaría | comería | viviría |
| nosotros | hablaríamos | comeríamos | viviríamos |
| vosotros | hablaríais | comeríais | viviríais |
| ellos, ellas, ustedes | hablarían | comerían | vivirían |

The irregular stems are the future's: *tendría*, *pondría*, *saldría*, *vendría*, *sabría*, *querría*, *habría*, *haría*, *diría*.

## When to use it

- **Polite requests and wishes**: *¿Podrías cerrar la ventana?* *Me gustaría un café.*
- **Advice**: *Deberías dormir más.* *Yo que tú, no lo compraría* (If I were you, I wouldn't buy it).
- **Imagining**: *Con más dinero, viviría en la playa.*
- **What someone said would happen**: *Dijo que vendría a las ocho.* (He said he'd come at eight.)
- **Guessing about the past**, the way the future guesses about now: *—¿A qué hora llegó? —Serían las tres.* (It must have been about three.)

## If I had...

For an "if" that isn't real, Spanish puts a past subjunctive after *si* and the conditional in the other half: *Si tuviera tiempo, te ayudaría* (If I had time, I'd help you).

The past subjunctive is a B2 topic. For now, learn the commonest forms as set pieces: *si tuviera* (if I had), *si fuera* (if I were), *si pudiera* (if I could), *si supiera* (if I knew).

The conditional itself never goes straight after *si*. Spaniards do say *si tendría* in some regions, but it counts as a mistake.

:::examples
- ¿Podría hablar con el director? — Could I speak to the manager?
- Me encantaría ir a Cuba. — I'd love to go to Cuba.
- Yo que tú, hablaría con ella. — If I were you, I'd talk to her.
- Si fuera rico, no trabajaría. — If I were rich, I wouldn't work.
:::

:::predict{prompt="nosotros (poder)" answer="podríamos"}
:::

:::cloze{sentence="Mi madre me prometió que ___ pronto." blank="volvería"}
:::
""",
        ["condicional"],
        "es-conditional",
        explains=["condicional"],
    ),
    page(
        "es-relative-pronouns",
        "La casa en la que vivo",
        r"""
**Que** is the everyday word for "who", "which" and "that". English often drops "that"; Spanish never drops *que*: *la película que vimos ayer* is "the film we saw yesterday".

| Word | Use | Example |
| --- | --- | --- |
| que | people and things, most of the time | La chica que vive arriba es médica. |
| quien, quienes | people, after a preposition | El amigo con quien viajé es de Lima. |
| el que, la que, los que, las que | after a preposition | La casa en la que vivo es pequeña. |
| lo que | what, the thing that | No entiendo lo que dices. |
| donde | where | Es el bar donde nos conocimos. |
| cuyo, cuya | whose (formal) | Es una autora cuyas novelas me encantan. |

## The preposition goes first

English can end a sentence with a preposition: "the flat I live in". Spanish can't, so the preposition goes before the relative: *el piso en el que vivo*, *la persona con la que hablé*.

The article agrees with the noun it refers back to: *el chico con el que*, *la chica con la que*, *los amigos con los que*.

## Lo que

*Lo que* is "what" inside a sentence, and it can open one: *Lo que necesito es dormir* (What I need is sleep). A direct question uses *qué*: *¿Qué necesitas?*

## Cuyo

*Cuyo* agrees with the thing owned, not the owner: *el vecino cuya hija es actriz* (the neighbour whose daughter is an actress). It's mostly written; in speech people rephrase.

:::examples
- El hombre que habla con mi padre es mi profesor. — The man talking to my father is my teacher.
- Esa es la razón por la que me fui. — That's the reason I left.
- Haz lo que quieras. — Do whatever you like.
- Es el pueblo donde nació mi abuela. — It's the village where my grandmother was born.
:::

:::cloze{sentence="El autobús ___ va al aeropuerto sale cada hora." blank="que"}
:::

:::cloze{sentence="Te voy a contar ___ pasó ayer." blank="lo que"}
:::
""",
        ["relativos"],
        "es-relative-pronouns",
        explains=["relativos"],
    ),
    page(
        "es-register",
        "Tío, qué guay: register",
        r"""
Spanish changes a lot between a chat with friends and a letter to the bank, and between Spain and Latin America.

## Tú, usted and vos

In Spain **tú** is normal with almost everyone, including shop staff and colleagues. **Usted** is for older people, officials, and anyone you want to keep at a polite distance. Much of Latin America uses *usted* more, and in Colombia and Costa Rica some families use it even with their children.

**Ustedes** is the only plural "you" in Latin America and the Canary Islands, friendly or formal. Most of Spain uses *vosotros* with friends.

Argentina, Uruguay, Paraguay and much of Central America use **vos** in place of *tú*, with present forms of its own: *vos tenés*, *vos sos*, *vos hablás*.

## Spoken Spain

| Word | Meaning |
| --- | --- |
| tío, tía | mate, guy (literally uncle, aunt) |
| guay | cool |
| mola | it's cool, I like it |
| currar, el curro | to work, a job |
| la pasta | money |
| majo | nice, friendly |
| flipar | to be amazed |
| en plan | like, kind of |

## Spoken Latin America

| Word | Where | Meaning |
| --- | --- | --- |
| chévere | Venezuela, Colombia, the Caribbean | great |
| padre, chido | Mexico | cool |
| bacán | Chile, Peru | great |
| che | Argentina, Uruguay | hey, mate |
| la plata | most of the region | money |
| ¿mande? | Mexico | pardon?, yes? |

Some words are harmless in one country and rude in another. *Coger* (to take, to catch) is everyday Spanish in Spain but vulgar in Mexico and Argentina, where people *toman* the bus.

## Writing

A formal letter or email opens with *Estimado señor* or *Estimada señora* and closes with *Atentamente* or *Un saludo*. To a friend, open with *Hola* and close with *Un abrazo* or *Besos*.

:::examples
- Tío, ¿vienes o qué? — Mate, are you coming or not?
- Me mola mucho tu chaqueta. — I really like your jacket.
- ¿Vos sos de Buenos Aires? — Are you from Buenos Aires?
:::

:::sort{groups="España (Spain): guay, mola, majo | Latinoamérica (Latin America): chévere, chido, bacán"}
:::

:::cloze{sentence="Con mis amigos de Madrid uso vosotros, pero en Lima uso ___." blank="ustedes"}
:::
""",
        ["registro"],
        "es-register",
        explains=["registro"],
    ),
    page(
        "es-false-friends",
        "Embarazada is not embarrassed",
        r"""
Some Spanish words look like English ones and mean something else. These cause the most trouble.

| Spanish | Means | Not | Which is |
| --- | --- | --- | --- |
| embarazada | pregnant | embarrassed | avergonzado |
| constipado | having a cold | constipated | estreñido |
| actual | current | actual | real, verdadero |
| éxito | success | exit | salida |
| carpeta | folder | carpet | alfombra |
| librería | bookshop | library | biblioteca |
| discusión | argument, row | discussion | conversación |
| sensible | sensitive | sensible | sensato |
| educado | polite | educated | culto |
| suceso | event, incident | success | éxito |
| pariente | relative | parent | padre, madre |
| fábrica | factory | fabric | tela |
| molestar | to bother | to molest | abusar de |
| realizar | to carry out | to realise | darse cuenta |
| asistir | to attend | to assist | ayudar |

## The classic mistakes

*Está embarazada* means "she's pregnant". Someone who's embarrassed *tiene vergüenza*, or in Latin America *está apenado*.

A Spaniard who's *constipado* has a cold and wants tissues, not a laxative.

*Actual* means "current": *el presidente actual* is the current president, and *actualmente* is "nowadays". "Actually" is *en realidad* or *de hecho*.

*Un éxito* is a success. The way out of a building is *la salida*.

:::examples
- La película fue un gran éxito. — The film was a big hit.
- Tengo un catarro: estoy constipada. — I've got a cold.
- Compré el libro en la librería de la esquina. — I bought the book at the bookshop on the corner.
:::

:::cloze{sentence="Mi mujer está ___: el bebé nace en mayo." blank="embarazada"}
:::

:::cloze{sentence="Ese chico es muy ___: siempre da las gracias." blank="educado"}
:::
""",
        ["falsos-amigos"],
        "es-false-friends",
        explains=["falsos-amigos"],
    ),
    page(
        "es-idioms",
        "Modismos",
        r"""
Idioms rarely translate word for word. Spanish ones lean on the body, food and animals: you *take someone's hair* where English pulls their leg, and an easy task is *eaten bread*. The literal meaning on each card helps it stick.

An idiom's verb conjugates as normal, and its possessive changes with the person: *tomar el pelo* becomes *me estás tomando el pelo*; *estar en su salsa* becomes *estoy en mi salsa*.

Some are Spain-only. *Estar sin blanca* (to be broke) and *pasarlo bomba* (to have a great time) will puzzle a Mexican, who might say *estar quebrado* and *pasarla padre*.

:::examples
- ¡No me tomes el pelo! — Stop pulling my leg!
- Mi hermano siempre mete la pata. — My brother always puts his foot in it.
- Este móvil me ha costado un ojo de la cara. — This phone cost me an arm and a leg.
- ¿Me echas una mano con las bolsas? — Can you give me a hand with the bags?
:::

:::cloze{sentence="No te preocupes, este examen es pan ___." blank="comido"}
:::

:::cloze{sentence="Con tanto ruido no he pegado ___ en toda la noche." blank="ojo"}
:::
""",
        ["idioms"],
        "es-idioms",
        explains=["idioms"],
    ),
    page(
        "es-se",
        "Se habla español: impersonal se",
        r"""
## People in general

**Se** + a third-person verb says what people in general do, with nobody in particular as the subject: *Aquí se come muy bien* (You eat very well here). *¿Cómo se dice "window" en español?* (How do you say "window" in Spanish?)

## Signs and adverts

With a noun, the verb agrees with it: *Se vende piso* (Flat for sale), but *Se venden pisos*. This is the se of signs: *Se alquila* (To let), *Se habla inglés* (English spoken), *Se prohíbe fumar* (No smoking).

## Accidents

When something happens that nobody meant, Spanish makes the thing the subject and adds the person as an indirect pronoun: *Se me ha roto el móvil* (My phone's broken; I broke it, but not on purpose). *Se nos ha acabado la leche* (We've run out of milk). *Se le cayeron las llaves* (She dropped her keys).

The verb agrees with the thing: *se me ha olvidado el nombre*, but *se me han olvidado los nombres*.

## Other ways to say "they" and "you"

A third-person plural verb with no subject also works: *Dicen que va a llover* (They say it's going to rain). *Me han robado la cartera* (Someone's stolen my wallet). And **uno** speaks for anyone: *Uno nunca sabe* (You never know).

:::examples
- En España se cena muy tarde. — In Spain people have dinner very late.
- Se busca camarero. — Waiter wanted.
- Se me ha olvidado la contraseña. — I've forgotten the password.
:::

:::cloze{sentence="En esta tienda ___ habla inglés y francés." blank="se"}
:::

:::cloze{sentence="A Luis se le ___ las gafas en el tren." blank="olvidaron"}
:::
""",
        ["se-impersonal"],
        "es-se",
        explains=["se-impersonal"],
    ),
    page(
        "es-ser-estar-adjectives",
        "Ser listo, estar listo",
        r"""
The A1 pack split *ser* (what something is) from *estar* (how it is now, and where it is). With some adjectives the choice changes the meaning completely.

| Adjective | With ser | With estar |
| --- | --- | --- |
| listo | clever | ready |
| rico | rich | tasty |
| malo | bad | ill |
| aburrido | boring | bored |
| despierto | sharp | awake |
| vivo | lively | alive |
| seguro | safe | sure |
| verde | green | unripe |
| orgulloso | arrogant | proud |

*Es muy listo* (He's very clever), but *¿Estás listo?* (Are you ready?).

## Food, looks and change

With food, *estar* says how it tastes: *La sopa está muy rica.* *Ser rico* is about money.

*Estar* also marks a change or a first impression: *¡Qué guapa estás!* (You look lovely), *El café está frío*. *Ser* gives the usual state: *Es guapa*, *El café de aquí es bueno*.

## Results

*Muerto* and *casado* take *estar*, though they rarely change: they're the result of something that happened. *Está muerto*, *Estoy casada*.

:::examples
- La paella está buenísima. — The paella is delicious.
- Su familia es muy rica. — Her family is very rich.
- ¿Estáis listos? Nos vamos. — Are you ready? We're off.
- Mi hijo es muy despierto para su edad. — My son is very sharp for his age.
:::

:::cloze{sentence="Hoy no voy a trabajar porque ___ malo." blank="estoy"}
:::

:::cloze{sentence="Mi profesor ___ muy aburrido: siempre habla de lo mismo." blank="es"}
:::
""",
        ["adjetivos"],
        "es-ser-estar-adjectives",
    ),
    page(
        "es-nuance-connectives",
        "Aunque, para que, en cuanto",
        r"""
Many Spanish conjunctions decide the mood of the verb after them. Some always take the subjunctive; others take it only when the event hasn't happened yet.

## Always the subjunctive

| Conjunction | Meaning | Example |
| --- | --- | --- |
| para que | so that | Te lo explico para que lo entiendas. |
| antes de que | before | Vámonos antes de que llueva. |
| sin que | without | Lo preparo sin que se entere mi madre. |
| a menos que | unless | Comemos fuera, a menos que prefieras cocinar. |

When both halves have the same subject, use the infinitive: *Estudio para aprobar*, but *Estudio para que mis padres estén contentos*. *Antes de salir*, but *antes de que salgas*.

## The future or a fact

*Cuando*, **en cuanto** (as soon as), *hasta que* (until) and *mientras* (as long as) take the subjunctive about the future and the indicative about the past or a habit:

- *En cuanto llegue, te aviso.* (I'll let you know as soon as I arrive.)
- *En cuanto llegué, me fui a dormir.* (As soon as I arrived, I went to bed.)

## Aunque

**Aunque** with the indicative states a fact: *Aunque llueve, voy a salir* (Even though it's raining, I'm going out). With the subjunctive it leaves it open: *Aunque llueva, voy a salir* (Even if it rains, I'm going out). **A pesar de que** works the same way and sounds more formal.

## Because and since

| Word | Use | Example |
| --- | --- | --- |
| porque | answers "why?" | No voy porque estoy cansado. |
| como | starts the sentence | Como no contestas, te escribo. |
| ya que, puesto que | the reason is known; puesto que is formal | Puesto que nadie pregunta, terminamos. |
| gracias a | thanks to | Gracias a ti, he aprobado. |
| por culpa de | because of (a bad cause) | Llegamos tarde por culpa del tráfico. |

## So

*Así que* is what people say. *De modo que* is a little more careful, and *por lo tanto* belongs in writing.

:::examples
- Te dejo mi coche para que vayas al médico. — I'll lend you my car so you can go to the doctor.
- Aunque no me guste, lo voy a hacer. — Even if I don't like it, I'm going to do it.
- Llámame en cuanto sepas algo. — Call me as soon as you hear anything.
:::

:::sort{groups="Subjuntivo (always): para que, antes de que, sin que | Indicativo (a reason): porque, ya que, puesto que"}
:::

:::cloze{sentence="Habla más alto para que te ___ todos." blank="oigan"}
:::
""",
        ["conjunciones", "subjuntivo"],
        "es-nuance-connectives",
        explains=["conjunciones"],
    ),
]

NOUNS = nouns(
    """
sociedad | f | society | society | | Vivimos en una sociedad muy diversa. | We live in a very diverse society.
gobierno | m | government | society | | El gobierno ha subido los impuestos. | The government has raised taxes.
ley | f | law | society | leyes | Es una ley muy polémica. | It's a very controversial law.
derecho | m | right; law (the subject) | society | | Todos tenemos derecho a una vivienda digna. | Everyone has the right to a decent home. | Estudiar Derecho: to study law.
política | f | politics; policy | society | - | No me gusta hablar de política. | I don't like talking about politics. | A politician is un político or una política.
elección | f | election; choice | society | elecciones | Las elecciones son en mayo. | The elections are in May.
contaminación | f | pollution | society | - | La contaminación es un problema en las grandes ciudades. | Pollution is a problem in big cities.
medio ambiente | m | environment | society | - | Hay que proteger el medio ambiente. | We have to protect the environment.
paro | m | unemployment | society | - | Mi hermano está en el paro. | My brother is out of work. | Spain. Latin America says el desempleo.
huelga | f | strike | society | | Mañana hay huelga de metro. | There's a metro strike tomorrow.
sueldo | m | salary, wages | society | | Con este sueldo no llego a fin de mes. | On this salary I can't make it to the end of the month.
alquiler | m | rent; renting | society | | El alquiler en Madrid es carísimo. | Rent in Madrid is very expensive.
vivienda | f | housing; home | society | | El precio de la vivienda no para de subir. | House prices keep going up.
impuesto | m | tax | society | | Pagamos muchos impuestos. | We pay a lot of tax.
ciudadano | m | citizen | society | | Es un derecho de todos los ciudadanos. | It's a right of every citizen. | A woman is la ciudadana.
guerra | f | war | society | | Mi abuelo vivió la guerra. | My grandfather lived through the war.
paz | f | peace | society | - | Todos queremos vivir en paz. | We all want to live in peace.
igualdad | f | equality | society | - | Luchan por la igualdad entre hombres y mujeres. | They're fighting for equality between men and women.
crisis | f | crisis | society | crisis | La crisis de 2008 fue muy dura en España. | The 2008 crisis hit Spain very hard. | The plural is the same: las crisis.
noticia | f | piece of news | society | | ¿Has visto las noticias? | Have you seen the news? | The TV news is las noticias, or in Spain el telediario.
periódico | m | newspaper | society | | Leo el periódico en el móvil. | I read the paper on my phone.
red social | f | social network | society | redes sociales | Paso demasiado tiempo en las redes sociales. | I spend too much time on social media.
arma | f | weapon | society | | Está prohibido llevar armas. | Carrying weapons is against the law. | Feminine, but el arma, like el agua.
área | f | area | society | | Esta es un área peatonal. | This is a pedestrian area. | Feminine, but el área, like el agua; las áreas.
costumbre | f | custom, habit | society | | En España es costumbre dar dos besos. | In Spain it's the custom to greet people with two kisses.
verdad | f | truth | society | | Dime la verdad. | Tell me the truth. | ¿Verdad? at the end of a sentence: right?
mentira | f | lie | society | | Eso es mentira. | That's a lie.
consejo | m | piece of advice | society | | Te voy a dar un consejo. | I'm going to give you some advice. | Also a council: el consejo de ministros.
cita | f | appointment; date | society | | Tengo cita con el dentista a las cinco. | I have a dentist's appointment at five. | Also a romantic date.
fracaso | m | failure | society | | La fiesta fue un fracaso. | The party was a flop.
tema | m | subject, topic | society | | Cambiemos de tema. | Let's change the subject. | Masculine, though it ends in -a.
recuerdo | m | memory; souvenir | feelings | | Tengo muy buenos recuerdos de ese verano. | I have very fond memories of that summer. | Also a souvenir: un recuerdo de Sevilla.
alma | f | soul | feelings | | Tiene un alma muy generosa. | She has a very generous soul. | Feminine, but el alma and un alma, like el agua: el alma buena, las almas.
águila | f | eagle | animals | | Vimos un águila en la montaña. | We saw an eagle in the mountains. | Feminine, but el águila and un águila, like el agua.
éxito | m | success | falsos-amigos | | La obra ha sido un éxito. | The play has been a success. | Not "exit": that's la salida.
carpeta | f | folder | falsos-amigos | | Guarda los documentos en esta carpeta. | Keep the documents in this folder. | Not "carpet": that's la alfombra.
librería | f | bookshop | falsos-amigos | | Hay una librería muy buena en mi calle. | There's a very good bookshop on my street. | Not "library": that's la biblioteca.
discusión | f | argument, row | falsos-amigos | | Tuvieron una discusión por el dinero. | They had a row about money. | Usually an argument, not a calm discussion.
suceso | m | event, incident | falsos-amigos | | El periódico habla del suceso. | The paper reports on the incident. | Not "success": that's el éxito.
pariente | m | relative | falsos-amigos | | Tengo parientes en Argentina. | I have relatives in Argentina. | Not "parent": parents are los padres.
fábrica | f | factory | falsos-amigos | | Mi padre trabajaba en una fábrica de coches. | My father worked in a car factory. | Not "fabric": that's la tela.
compromiso | m | commitment; engagement | falsos-amigos | | Tengo un compromiso esta noche. | I've got something on tonight. | A compromise is usually un acuerdo or un término medio.
"""
)

VERBS = [
    verb("deber", "must, should; to owe", [],
         example="Debes descansar más.", example_en="You should rest more.",
         note="Deberías is softer advice. Deber dinero: to owe money."),
    verb("creer", "to believe, to think", [],
         pret="creí creíste creyó creímos creísteis creyeron", pp="creído",
         example="Creo que va a llover.", example_en="I think it's going to rain."),
    verb("dudar", "to doubt", [],
         example="Dudo que tenga tiempo.", example_en="I doubt he'll have time."),
    verb("alegrarse", "to be glad", [],
         example="Me alegro mucho de verte.", example_en="I'm really glad to see you.",
         note="Me alegro on its own: I'm glad to hear it."),
    verb("molestar", "to bother", ["falsos-amigos"],
         example="¿Te molesta la música?", example_en="Does the music bother you?",
         note="Not \"to molest\". Works like gustar: me molesta el ruido."),
    verb("realizar", "to carry out, to do", ["falsos-amigos"],
         example="Realizamos una encuesta a mil personas.", example_en="We carried out a survey of a thousand people.",
         note="Not \"to realise\": that's darse cuenta."),
    verb("asistir", "to attend", ["falsos-amigos"],
         example="Más de mil personas asistieron al concierto.", example_en="Over a thousand people attended the concert.",
         note="Asistir a: to attend. To assist is ayudar."),
    verb("aprobar", "to pass (an exam); to approve", [], stem="o>ue",
         example="¡He aprobado el examen de conducir!", example_en="I've passed my driving test!"),
    verb("suspender", "to fail (an exam); to call off", [],
         example="Suspendí matemáticas en junio.", example_en="I failed maths in June.",
         note="Spain. Mexico says reprobar."),
    verb("convencer", "to convince", [],
         present="convenzo convences convence convencemos convencéis convencen",
         example="Me has convencido.", example_en="You've convinced me."),
    verb("conseguir", "to get, to manage to", [], stem="e>i",
         present="consigo consigues consigue conseguimos conseguís consiguen",
         subj="consiga consigas consiga consigamos consigáis consigan",
         example="Por fin he conseguido entradas.", example_en="I've finally got tickets."),
    verb("sugerir", "to suggest", [], stem="e>ie",
         example="Te sugiero que pruebes el pulpo.", example_en="I suggest you try the octopus."),
    verb("prohibir", "to forbid, to ban", [],
         present="prohíbo prohíbes prohíbe prohibimos prohibís prohíben",
         subj="prohíba prohíbas prohíba prohibamos prohibáis prohíban",
         example="Mis padres me prohíben salir entre semana.", example_en="My parents don't let me go out on weekdays."),
    verb("caer", "to fall", [],
         present="caigo caes cae caemos caéis caen",
         pret="caí caíste cayó caímos caísteis cayeron",
         pp="caído",
         example="Cuidado, que te vas a caer.", example_en="Careful, you're going to fall.",
         note="Caer bien: me cae bien, I like him."),
    verb("acabar", "to finish; to run out", [],
         example="Se nos ha acabado el café.", example_en="We've run out of coffee.",
         note="Acabar de + infinitive: to have just. Acabo de llegar: I've just arrived."),
    verb("alquilar", "to rent, to let", [],
         example="Alquilamos un piso cerca de la playa.", example_en="We rented a flat near the beach."),
    verb("mentir", "to lie", [], stem="e>ie",
         example="Sé que me mientes.", example_en="I know you're lying to me."),
    verb("elegir", "to choose", [], stem="e>i",
         present="elijo eliges elige elegimos elegís eligen",
         subj="elija elijas elija elijamos elijáis elijan",
         example="Siempre elijo la mesa de la ventana.", example_en="I always choose the table by the window."),
    verb("construir", "to build", [],
         present="construyo construyes construye construimos construís construyen",
         pret="construí construiste construyó construimos construisteis construyeron",
         example="Están construyendo un hospital nuevo.", example_en="They're building a new hospital."),
    verb("producir", "to produce", [], zc=True, pret_stem="produj",
         example="España produce mucho aceite de oliva.", example_en="Spain produces a lot of olive oil."),
    verb("proponer", "to propose, to suggest", [],
         present="propongo propones propone proponemos proponéis proponen",
         pret_stem="propus", fut="propondr", pp="propuesto",
         example="Os propongo un plan para el sábado.", example_en="I'd like to suggest a plan for Saturday, everyone."),
    verb("mantener", "to keep; to support", [],
         present="mantengo mantienes mantiene mantenemos mantenéis mantienen",
         pret_stem="mantuv", fut="mantendr",
         example="Es difícil mantener la calma.", example_en="It's hard to keep calm."),
    verb("quejarse", "to complain", [],
         example="Mi vecino siempre se queja del ruido.", example_en="My neighbour is always complaining about the noise."),
    verb("casarse", "to get married", [],
         example="Se casaron en Sevilla en 2015.", example_en="They got married in Seville in 2015.",
         note="Casarse con: to marry someone."),
]

ADJECTIVES = (
    adjectives(
        """
actual, actual, actuales, actuales | current, present-day | La situación actual es complicada. | The current situation is complicated. | Not "actual": that's real. Actualmente means nowadays.
sensible, sensible, sensibles, sensibles | sensitive | Tengo la piel muy sensible. | I have very sensitive skin. | Not "sensible": that's sensato.
constipado, constipada, constipados, constipadas | having a cold | Estoy constipado y no puedo respirar. | I've got a cold and can't breathe. | Not "constipated": that's estreñido. Latin America prefers resfriado.
educado, educada, educados, educadas | polite, well-mannered | Tus hijos son muy educados. | Your children are very polite. | Educated is culto, or con estudios.
raro, rara, raros, raras | strange, odd | ¡Qué raro! No contesta. | How odd! She isn't answering. | It can mean rare, but strange is the usual sense.
""",
        ["falsos-amigos"],
    )
    + adjectives(
        """
listo, lista, listos, listas | clever; ready | Tu hija es muy lista. | Your daughter is very clever. | Ser listo: clever. Estar listo: ready.
rico, rica, ricos, ricas | rich; tasty | Este gazpacho está muy rico. | This gazpacho is delicious. | Ser rico: rich. Estar rico: tasty.
seguro, segura, seguros, seguras | safe; sure | ¿Estás seguro? | Are you sure? | Ser seguro: safe. Estar seguro: sure.
despierto, despierta, despiertos, despiertas | awake; sharp | ¿Todavía estás despierto? | Are you still awake? | Ser despierto: quick-witted.
vivo, viva, vivos, vivas | alive; lively | Es un niño muy vivo. | He's a very lively child. | Estar vivo: alive. Ser vivo: lively, sharp.
pesado, pesada, pesados, pesadas | heavy; annoying | ¡Qué pesado eres! | You're such a pain! | Also heavy: una maleta pesada.
""",
    )
    + adjectives(
        """
orgulloso, orgullosa, orgullosos, orgullosas | proud | Estoy muy orgullosa de ti. | I'm very proud of you. | Ser orgulloso can mean arrogant.
celoso, celosa, celosos, celosas | jealous | Mi novio es un poco celoso. | My boyfriend is a bit jealous.
generoso, generosa, generosos, generosas | generous | Mi abuelo era muy generoso. | My grandfather was very generous.
sincero, sincera, sinceros, sinceras | honest, sincere | Para ser sincero, no me gusta. | To be honest, I don't like it.
harto, harta, hartos, hartas | fed up | Estoy harta de este trabajo. | I'm fed up with this job.
agotado, agotada, agotados, agotadas | exhausted; sold out | Después del viaje estoy agotado. | I'm exhausted after the journey. | Also sold out: las entradas están agotadas.
majo, maja, majos, majas | nice, friendly | Tu novia es muy maja. | Your girlfriend's really nice. | Spain, informal.
""",
        ["feelings"],
    )
    + adjectives(
        """
necesario, necesaria, necesarios, necesarias | necessary | No es necesario reservar. | You don't need to book.
imposible, imposible, imposibles, imposibles | impossible | Es imposible aparcar en el centro. | It's impossible to park in the centre.
"""
    )
)

IDIOMS = phrases(
    """
tomar el pelo | to pull someone's leg | ¿Me estás tomando el pelo? | Are you pulling my leg? | to take the hair
estar en las nubes | to be miles away | Perdona, estaba en las nubes. | Sorry, I was miles away. | to be in the clouds
costar un ojo de la cara | to cost an arm and a leg | El piso nos costó un ojo de la cara. | The flat cost us an arm and a leg. | to cost an eye from the face
ser pan comido | to be a piece of cake | El examen fue pan comido. | The exam was a piece of cake. | to be eaten bread
meter la pata | to put your foot in it | Le pregunté por su novia y metí la pata. | I asked him about his girlfriend and put my foot in it. | to put the paw in
no tener pelos en la lengua | to not mince your words | Mi abuela no tiene pelos en la lengua. | My grandmother doesn't mince her words. | to have no hairs on your tongue
estar como una cabra | to be off your head | Tu primo está como una cabra. | Your cousin is completely bonkers. | to be like a goat
echar una mano | to give a hand | ¿Me echas una mano con la mudanza? | Will you give me a hand with the move? | to throw a hand
ponerse las pilas | to get your act together | Si quieres aprobar, ponte las pilas. | If you want to pass, get your act together. | to put your batteries in
llover a cántaros | to pour with rain | Está lloviendo a cántaros. | It's pouring down. | to rain in jugs
quedarse de piedra | to be stunned | Cuando me lo contó, me quedé de piedra. | When she told me, I was stunned. | to be turned to stone
dar en el clavo | to hit the nail on the head | Has dado en el clavo. | You've hit the nail on the head. | to hit on the nail
no pegar ojo | to not sleep a wink | Con este calor no pego ojo. | I can't sleep a wink in this heat. | to not stick an eye
irse por las ramas | to beat about the bush | No te vayas por las ramas y dime la verdad. | Stop beating about the bush and tell me the truth. | to go off along the branches
hablar por los codos | to never stop talking | Mi vecina habla por los codos. | My neighbour never stops talking. | to talk through your elbows
estar sin blanca | to be broke | Este mes estoy sin blanca. | I'm broke this month. | to be without a blanca (an old coin) | Spain.
dormir como un tronco | to sleep like a log | Después de la excursión dormí como un tronco. | After the hike I slept like a log. | to sleep like a trunk
tener mala pata | to be unlucky | Tengo muy mala pata con los coches. | I have really bad luck with cars. | to have a bad paw
dar plantón | to stand someone up | Me dio plantón y esperé una hora. | He stood me up and I waited for an hour. | to give a long wait
ser uña y carne | to be inseparable | Ana y Lucía son uña y carne. | Ana and Lucía are inseparable. | to be nail and flesh
tirar la casa por la ventana | to splash out | Para la boda tiraron la casa por la ventana. | They pushed the boat out for the wedding. | to throw the house out of the window
estar hasta las narices | to be fed up | Estoy hasta las narices del ruido. | I'm sick to death of the noise. | to be up to your nostrils
en un abrir y cerrar de ojos | in the blink of an eye | Se comió el bocadillo en un abrir y cerrar de ojos. | He ate the sandwich in the blink of an eye. | in an opening and closing of eyes
buscarle tres pies al gato | to overcomplicate things | No le busques tres pies al gato: es muy sencillo. | Don't overcomplicate it: it's very simple. | to look for three feet on the cat
ser un cero a la izquierda | to count for nothing | En la oficina soy un cero a la izquierda. | At the office I count for nothing. | to be a zero on the left
dar la lata | to pester | Los niños me han dado la lata toda la tarde. | The kids have been pestering me all afternoon. | to give the tin can
echar de menos | to miss | Echo de menos a mi familia. | I miss my family. | to throw as less | Latin America says extrañar.
tener buena pinta | to look good | Esta tarta tiene muy buena pinta. | This cake looks great. | to have a good look
no hay mal que por bien no venga | every cloud has a silver lining | Perdí el tren, pero conocí a Marta: no hay mal que por bien no venga. | I missed the train but met Marta: every cloud has a silver lining. | there's no bad that doesn't come for some good | Venga is a subjunctive.
más vale tarde que nunca | better late than never | Ya has llegado: más vale tarde que nunca. | You made it: better late than never. | late is worth more than never
a otra cosa, mariposa | let's move on | Bueno, eso ya está. ¡A otra cosa, mariposa! | Right, that's done. On to the next thing! | to another thing, butterfly
estar en su salsa | to be in your element | En la cocina, mi padre está en su salsa. | In the kitchen my father is in his element. | to be in your sauce
ponerse rojo como un tomate | to go as red as a beetroot | Cuando la vio, se puso rojo como un tomate. | When he saw her, he went as red as a beetroot. | to go as red as a tomato
hacer la vista gorda | to turn a blind eye | El profesor hizo la vista gorda. | The teacher turned a blind eye. | to make the sight fat
pasarlo bomba | to have a great time | Lo pasamos bomba en la fiesta. | We had a great time at the party. | to spend it bomb | Spain.
cada loco con su tema | each to their own | Él colecciona piedras. Cada loco con su tema. | He collects stones. Each to their own. | every madman with his subject
""",
    ["idioms"],
)

EXPRESSIONS = phrases(
    """
vale la pena | it's worth it | Si vas a Granada, la Alhambra vale la pena. | If you go to Granada, the Alhambra is worth it. | it's worth the pain | Spain also says merece la pena.
darse cuenta | to realise | No me di cuenta de la hora. | I didn't notice the time. | to give yourself account | Realizar is not "to realise".
estar embarazada | to be pregnant | Mi hermana está embarazada de cinco meses. | My sister is five months pregnant. | | Not "embarrassed": that's tener vergüenza.
tener que ver con | to have to do with | Eso no tiene nada que ver con nosotros. | That's got nothing to do with us. | to have to see with
en absoluto | not at all | —¿Te molesta? —En absoluto. | "Does it bother you?" "Not at all." | | Not "absolutely": that's totalmente.
ojalá | I hope, if only | ¡Ojalá aprobemos el examen! | I hope we pass the exam! | | From Arabic, "if God wills". Takes the subjunctive.
hace falta | it's needed, you need | Hace falta mucha paciencia con los niños. | You need a lot of patience with children. | it makes lack
¡no me digas! | you don't say! | —Ana y Luis se han separado. —¡No me digas! | "Ana and Luis have split up." "You don't say!" | don't tell me
¡ni idea! | no idea! | —¿Dónde está Pepe? —¡Ni idea! | "Where's Pepe?" "No idea!" | not an idea
sin querer | by accident | Perdona, lo he hecho sin querer. | Sorry, I didn't mean to. | without wanting
por si acaso | just in case | Llévate un paraguas, por si acaso. | Take an umbrella, just in case. | for if by chance
se me ha olvidado | I've forgotten | Lo siento, se me ha olvidado tu cumpleaños. | Sorry, I forgot your birthday. | it has forgotten itself on me
""",
    ["expressions"],
)
for e in EXPRESSIONS:
    if e["primary_form"] in {"estar embarazada", "en absoluto"}:
        e["tags"] = e["tags"] + ["falsos-amigos"]

SLANG = phrases(
    """
en plan | like, sort of | Estaba en plan "no me hables". | She was like, "don't talk to me". | in plan | Spain, young people.
¡qué guay! | how cool! | ¿Tienes entradas para el concierto? ¡Qué guay! | You've got tickets for the concert? How cool! | | Spain.
¡venga! | come on!; OK then | ¡Venga, que llegamos tarde! | Come on, we'll be late! | come | Spain. Also a goodbye: ¡venga, hasta luego!
o sea | I mean; so | O sea, que no vienes. | So you're not coming, then. | or be it
¡qué fuerte! | wow!, that's outrageous! | ¿Se ha ido sin pagar? ¡Qué fuerte! | He left without paying? That's outrageous! | how strong | Spain.
me mola | I love it, it's cool | Me mola esta canción. | I love this song. | | Spain, informal. Works like gustar: me molan tus zapatos.
estoy flipando | I can't believe it | Estoy flipando con este paisaje. | I'm blown away by this landscape. | | Spain, informal.
¡qué chévere! | how great! | ¡Qué chévere tu casa! | Your house is great! | | Venezuela, Colombia and the Caribbean.
¡qué padre! | how cool! | ¡Qué padre tu carro! | Your car's so cool! | how father | Mexico.
¿mande? | pardon?, yes? | —Pedro, ven aquí. —¿Mande? | "Pedro, come here." "Yes?" | at your command | Mexico: a polite answer when someone calls you or you didn't hear.
""",
    ["expressions", "registro"],
)

CONNECTIVES = connectors(
    "connective",
    """
no obstante | nevertheless | conn-contrast | El hotel era caro; no obstante, mereció la pena. | The hotel was expensive; nevertheless, it was worth it.
en cualquier caso | in any case | conn-contrast | No sé si iré; en cualquier caso, te aviso. | I don't know if I'll go; in any case, I'll let you know.
por lo tanto | therefore | conn-consequence | No hay mayoría; por lo tanto, habrá nuevas elecciones. | There's no majority; therefore, there'll be fresh elections.
de hecho | in fact, actually | conn-cause | No está enfadado; de hecho, está muy contento. | He isn't angry; in fact, he's very happy.
encima | on top of that | conn-addition | Llegó tarde y encima sin regalo. | He was late, and on top of that he didn't bring a present.
es decir | that is, in other words | conn-addition | Vuelvo dentro de quince días, es decir, el día diez. | I'm back in a fortnight, that is, on the tenth.
mientras tanto | meanwhile | conn-sequence | Yo hago la cena; mientras tanto, tú pones la mesa. | I'll make dinner; meanwhile, you lay the table.
finalmente | finally, in the end | conn-sequence | Lo pensó mucho y finalmente aceptó el trabajo. | She thought about it for a long time and finally took the job.
""",
    ["conectores"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
para que | so that (+ subjunctive) | conj-subordinating | Te lo repito para que no lo olvides. | I'll say it again so that you don't forget it.
antes de que | before (+ subjunctive) | conj-subordinating | Vuelve antes de que anochezca. | Come back before it gets dark. | Antes de que anochezca, vuelve.
en cuanto | as soon as | conj-subordinating | Te llamo en cuanto llegue. | I'll call you as soon as I arrive. | En cuanto llegue, te llamo.
a menos que | unless (+ subjunctive) | conj-subordinating | Iremos andando, a menos que llueva. | We'll walk, unless it rains.
sin que | without (+ subjunctive) | conj-subordinating | Lo arreglo sin que lo sepa tu padre. | I'll sort it out without your father knowing.
puesto que | since (formal) | conj-subordinating | Puesto que no hay más preguntas, terminamos aquí. | Since there are no more questions, we'll finish here. | Terminamos aquí, puesto que no hay más preguntas.
mientras que | whereas | conj-subordinating | Yo prefiero el mar, mientras que mi pareja prefiere la montaña. | I prefer the sea, whereas my partner prefers the mountains.
de modo que | so | conj-subordinating | No me contestaba, de modo que me fui. | She wasn't answering, so I left.
a pesar de que | even though | conj-subordinating | Salimos a pesar de que hacía frío. | We went out even though it was cold. | A pesar de que hacía frío, salimos.
""",
    ["conjunciones"],
)

ITEMS = PAGES + interleave(IDIOMS, EXPRESSIONS + SLANG, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

UNITS = [
    {
        "title": "El subjuntivo",
        "page_id": "es-subjunctive",
        "word_ids": ["dudar", "alegrarse", "sugerir", "prohibir", "ojala", "hace-falta", "no-me-digas"],
    },
    {
        "title": "El condicional",
        "page_id": "es-conditional",
        "word_ids": ["deber", "convencer", "conseguir", "proponer", "mantener", "elegir"],
    },
    {
        "title": "Los relativos",
        "page_id": "es-relative-pronouns",
        "word_ids": ["creer", "mentir", "construir", "producir", "casarse", "quejarse"],
    },
    {
        "title": "Registro",
        "page_id": "es-register",
        "word_ids": [
            "en-plan", "que-guay", "venga", "o-sea", "que-fuerte",
            "me-mola", "estoy-flipando", "que-chevere", "que-padre", "mande",
        ],
    },
    {
        "title": "Falsos amigos",
        "page_id": "es-false-friends",
        "word_ids": [
            "exito", "carpeta", "libreria", "discusion", "suceso",
            "pariente", "fabrica", "compromiso", "estar-embarazada", "en-absoluto",
        ],
    },
    {
        "title": "Más falsos amigos",
        "word_ids": ["actual", "sensible", "constipado", "educado", "raro", "molestar", "realizar", "asistir"],
    },
    {
        "title": "Modismos",
        "page_id": "es-idioms",
        "word_ids": [
            "tomar-el-pelo", "estar-en-las-nubes", "costar-un-ojo-de-la-cara", "ser-pan-comido",
            "meter-la-pata", "no-tener-pelos-en-la-lengua", "estar-como-una-cabra",
            "echar-una-mano", "ponerse-las-pilas", "no-pegar-ojo",
        ],
    },
    {
        "title": "Se vende",
        "page_id": "es-se",
        "word_ids": ["se-me-ha-olvidado", "sin-querer", "caer", "acabar", "alquilar", "alquiler", "vivienda"],
    },
    {
        "title": "Ser listo, estar listo",
        "page_id": "es-ser-estar-adjectives",
        "word_ids": ["listo", "rico", "seguro", "despierto", "vivo", "pesado"],
    },
    {
        "title": "Aunque, para que",
        "page_id": "es-nuance-connectives",
        "word_ids": [
            "para-que", "antes-de-que", "en-cuanto", "a-menos-que", "sin-que",
            "puesto-que", "mientras-que", "de-modo-que", "a-pesar-de-que",
        ],
    },
    {
        "title": "El carácter",
        "word_ids": ["orgulloso", "celoso", "generoso", "sincero", "harto", "agotado", "majo"],
    },
]

LABELS = topic_labels(DELTA)

PACK = pack(
    "es-fluency-v1",
    2,
    "es",
    "Español · Soltura (B1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Práctica"),
)
