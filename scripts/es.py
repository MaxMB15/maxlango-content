"""Spanish Base Packs, in curriculum order."""

import es_everyday
import es_fluency
import es_foundations
from common import interleave, pack, page, topic
from es_common import connectors, nouns, verb
from es_conj import IR

DELTA = [
    topic("home", "Casa", "home", ["género"]),
    topic("food", "Comida", "food", ["género"]),
    topic(
        "conectores",
        "Conectores",
        "connectives",
        ["conn-contrast", "conn-cause", "conn-addition", "conn-sequence"],
    ),
    topic("conjunciones", "Conjunciones", "conjunctions", ["conj-coordinating", "conj-subordinating"]),
    topic("animals", "Animales", "animals", ["género"]),
    topic("nature", "Naturaleza", "nature", ["género"]),
    topic("people", "Personas", "people", ["género"]),
    topic("objects", "Objetos", "objects", ["género"]),
    topic("transport", "Transporte", "transport", ["género"]),
    topic("time", "Tiempo", "time", ["género"]),
]

ARTICLES = page(
    "es-articles-gender",
    "El, la, un and una",
    r"""
Every Spanish noun is **masculine** or **feminine**, and the article shows which.

| | masculine | feminine |
| --- | --- | --- |
| the | el gato | la casa |
| the (plural) | los gatos | las casas |
| a, an | un gato | una casa |
| some, a few | unos gatos | unas casas |

- Most nouns in **-o** are masculine and most in **-a** are feminine. The exceptions start on day one: *el día* (the day) is masculine and *la mano* (the hand) feminine.
- The plural articles keep the gender too, so *los* and *las* tell you as much as *el* and *la*.
- Spanish says "the" where English says nothing. A general statement takes *el*, *la*, *los* or *las*: *Me gusta el café* (I like coffee), *Los perros son leales* (Dogs are loyal).
- After *ser*, a job or nationality takes no *un* or *una*: *Soy profesor* (I'm a teacher).

## El agua

A few feminine nouns start with a stressed **a-** or **ha-**. They take **el** and **un** in the singular so that two a sounds don't run together, but they stay feminine: *el agua fría* (the cold water), *las aguas*. *El hambre* (hunger) works the same way.

## Al and del

**A** + **el** becomes **al**, and **de** + **el** becomes **del**: *Voy al parque*, *la puerta del coche*. These are the only two contractions in Spanish. *La*, *los* and *las* never merge.

:::examples
- El gato duerme en la silla. — The cat is sleeping on the chair.
- La ventana está abierta. — The window is open.
- Tengo un perro y una bicicleta. — I have a dog and a bike.
- El agua está fría. — The water is cold.
:::

So learn every noun with its article: **el libro**, **la mesa**, never the noun alone.
""",
    ["artículos", "género"],
    "es-articles",
    explains=["artículos"],
)
# The session's Reading card shows these plain sentences and cloze lines,
# and leaves out the :::examples block the page itself shows.
ARTICLES["extras"] = {
    "examples": ["El gato duerme en la silla.", "La ventana está abierta.", "El agua está fría."],
    "cloze": [{"sentence": "___ perro come.", "blank": "El"}, {"sentence": "___ casas son grandes.", "blank": "Las"}],
    **ARTICLES["extras"],
}

# Every page after ARTICLES only explains a Tag: it unlocks nothing, so no
# session pushes it as Reading, and it opens when the learner taps a Tag.
PAGES = [
    ARTICLES,
    page(
        "es-plural",
        "Plurals: -s and -es",
        r"""
The Spanish plural is easy to hear, because the final -s is always pronounced. The article changes too: *el gato*, *los gatos*; *la casa*, *las casas*.

## The endings

| Singular ends in | Plural | Example |
| --- | --- | --- |
| a vowel | add **-s** | el libro, los libros; la mesa, las mesas |
| a consonant | add **-es** | la ciudad, las ciudades; el árbol, los árboles |
| -z | **-ces** | el lápiz, los lápices; la vez, las veces |
| an unstressed vowel + s | no change | el lunes, los lunes; la crisis, las crisis |

A stressed **-á**, **-é** or **-ó** just adds -s: *el sofá, los sofás*; *el café, los cafés*.

## Written accents come and go

The stress stays on the same syllable, so the written accent sometimes has to move:

- It disappears when -es adds a syllable after it: *la canción, las canciones*; *el autobús, los autobuses*; *inglés, ingleses*.
- It appears when -es pushes the stress further from the end: *el joven, los jóvenes*; *el examen, los exámenes*.

## A masculine plural can mean both

A mixed group takes the masculine plural. *Los padres* are "the parents", *los hermanos* "brothers and sisters", *los hijos* "the children" (sons and daughters) and *los reyes* "the king and queen". So *Tengo dos hermanos* can mean two brothers, or a brother and a sister.

Adjectives follow the same rules: *un coche rojo, dos coches rojos*; *una persona feliz, dos personas felices*.

:::examples
- Tengo dos gatos y un perro. — I have two cats and a dog.
- Los árboles del parque son muy altos. — The trees in the park are very tall.
- ¿Cuántos hermanos tienes? — How many brothers and sisters do you have?
- Las canciones de este disco son preciosas. — The songs on this album are beautiful.
:::
""",
        ["plural"],
        explains=["plural"],
    ),
    page(
        "es-coordinating-conjunctions",
        "Y, o, pero and sino",
        r"""
The coordinating conjunctions join two words, or two clauses of the same kind, and leave both as they are.

| Spanish | English |
| --- | --- |
| y | and |
| o | or |
| pero | but |
| sino | but, rather (after a negative) |
| ni | nor; ni ... ni, neither ... nor |

:::examples
- Tengo un hermano y una hermana. — I have a brother and a sister.
- ¿Quieres té o café? — Do you want tea or coffee?
- Quiero ir, pero no tengo tiempo. — I want to go, but I don't have time.
- No es mi hermano, sino mi primo. — He isn't my brother, he's my cousin.
:::

## Y becomes e, o becomes u

Before a word that starts with the sound **i**, *y* becomes **e**: *padre e hijo* (father and son), *español e inglés*. Before the sound **o**, *o* becomes **u**: *siete u ocho* (seven or eight). It goes by sound, not spelling, so *agua y hielo* keeps *y*, because *hielo* starts with a "y" sound.

## Pero or sino?

Both translate as "but".

- **Pero** adds something that limits or goes against what came before: *Es caro, pero es muy bueno.*
- **Sino** corrects a negative. The first part says what something isn't, and *sino* says what it is: *No vivo en Madrid, sino en Sevilla.* (I don't live in Madrid but in Seville.)

Before a whole clause with its own verb, *sino* becomes **sino que**: *No solo canta, sino que también baila.*

## Ni

**Ni** joins two negatives. With the verb first, *no* goes before it: *No bebo ni té ni café.* (I drink neither tea nor coffee.) Put before the verb, *ni* needs no *no*: *Ni Juan ni Ana lo saben.*
""",
        ["conj-coordinating"],
        explains=["conj-coordinating"],
    ),
    page(
        "es-subordinating-conjunctions",
        "Que, cuando, si and porque",
        r"""
A subordinating conjunction starts a clause that depends on the main one: *Me quedo en casa **porque** estoy cansado.* The word order inside that clause stays normal. What some conjunctions change is the mood of the verb.

| Spanish | English |
| --- | --- |
| que | that |
| cuando | when |
| si | if, whether |
| porque | because |
| como | as, since (at the start of the sentence) |
| aunque | although, even if |
| mientras | while |
| para que | so that |

## Que stays

English can drop "that". Spanish can't drop *que*: *Creo **que** viene.* (I think he's coming.)

## Porque, por qué and el porqué

Three spellings, one sound:

- **¿Por qué?** asks why: *¿Por qué no vienes?*
- **Porque** answers: *Porque estoy cansado.*
- **El porqué** is a noun, "the reason": *No entiendo el porqué.*

## Some take the subjunctive

A few conjunctions always take the subjunctive, *para que* and *antes de que* among them. Others take it when the clause talks about something that hasn't happened yet. After **cuando**, a future event takes the subjunctive where English uses the present: *Cuando llegues, llámame.* (When you arrive, call me.) The subjunctive comes in the B1 pack; until then, learn these as set lines.

## Si

After **si** meaning "if", Spanish never uses the future or the present subjunctive. Use the present: *Si llueve, nos quedamos en casa.* (If it rains, we'll stay at home.)

:::examples
- Creo que va a llover. — I think it's going to rain.
- Leo cuando llueve. — I read when it rains.
- Salimos si quieres. — We'll go out if you want.
- Me quedo en casa porque estoy cansado. — I'm staying at home because I'm tired.
:::
""",
        ["conj-subordinating"],
        explains=["conj-subordinating"],
    ),
    page(
        "es-contrast-connectives",
        "Sin embargo and en cambio",
        r"""
A contrast connective says that what comes next goes against what came before, or against what you'd expect.

| Spanish | English |
| --- | --- |
| sin embargo | however |
| en cambio | on the other hand, whereas |
| no obstante | nevertheless (formal) |
| aun así | even so |
| de todas formas | anyway, in any case |
| al contrario | on the contrary |

At the start of a clause they take a comma, and nothing else changes: *Sin embargo, no es feliz.* Most can also sit later in the sentence, between commas: *No es, sin embargo, feliz.*

## Which one?

- **Sin embargo** is the all-purpose "however", in speech and in writing.
- **En cambio** sets two different facts side by side: *Mi hermano es muy alto; yo, en cambio, soy bajito.*
- **Aun así** means "even so": *Estaba cansado y, aun así, fue a trabajar.*
- **Al contrario** follows a negative and says the opposite is true: *No es tímido; al contrario, habla con todo el mundo.*

## Pero and aunque

**Pero** (but) is the everyday way to set up a contrast: *Quiero ir, pero no puedo.* **Aunque** (although) starts a subordinate clause: *Aunque es rico, no es feliz.*

:::examples
- Llueve; sin embargo, salimos a pasear. — It's raining; however, we're going out for a walk.
- El piso es pequeño; en cambio, el barrio es precioso. — The flat is small; the neighbourhood, on the other hand, is lovely.
- Es difícil; aun así, es posible. — It's difficult; even so, it's possible.
:::
""",
        ["conn-contrast"],
        explains=["conn-contrast"],
    ),
    page(
        "es-cause-connectives",
        "Es que, como and ya que",
        r"""
A cause connective gives the reason for what was just said.

**Es que** is the everyday one. It starts a sentence that explains or excuses: *No puedo ir. Es que tengo que trabajar.* (I can't go. The thing is, I have to work.) It softens a refusal, so you'll hear it many times a day. In a question it sounds annoyed: *¿Es que no me escuchas?* (Aren't you listening to me?)

**De hecho** (in fact) backs up what you just said with a fact: *Es muy buen cocinero; de hecho, trabajó en un restaurante.*

## Porque, como, ya que and puesto que

These four start a clause that gives a cause.

| Spanish | Use | Example |
| --- | --- | --- |
| porque | the everyday "because", after the main clause | Me voy porque es tarde. |
| como | "as", always at the start of the sentence | Como es tarde, me voy. |
| ya que | "since", a reason the listener will accept | Ya que estás aquí, ayúdame. |
| puesto que | "since", formal and written | Puesto que nadie contesta, me voy. |

*Porque* starts a sentence only when it answers *¿por qué?*. To put the reason first, use *como*: *Como llueve, nos quedamos en casa*, not *Porque llueve, nos quedamos*.

:::examples
- No puedo ir; es que tengo que trabajar. — I can't go; the thing is, I have to work.
- Como llueve, nos quedamos en casa. — As it's raining, we're staying at home.
- Ya que estás aquí, ayúdame con esto. — Since you're here, help me with this.
:::
""",
        ["conn-cause"],
        explains=["conn-cause"],
    ),
    page(
        "es-addition-connectives",
        "Además and también",
        r"""
An addition connective adds one more point to what was said.

| Spanish | English |
| --- | --- |
| también | also, too |
| además | besides, on top of that |
| incluso | even |
| encima | on top of that (spoken, annoyed) |
| es más | what's more |
| asimismo | likewise (formal) |

**Además** is the everyday one, in speech and in writing: *El piso es bonito y, además, es barato.* At the start of a sentence it takes a comma.

**También** goes next to the verb, before or after it: *También hablo francés* or *Hablo también francés.* Its negative partner is **tampoco** (not ... either): *Yo tampoco hablo alemán.* In a reply, they agree with what was said: *—Me gusta el jazz. —A mí también.* *—No me gusta el jazz. —A mí tampoco.*

**Encima** piles a complaint on a complaint: *Llegó tarde y, encima, sin las llaves.*

**Incluso** means "even": *Trabaja todos los días, incluso los domingos.*

:::examples
- Me gusta el té. También me gusta el café. — I like tea. I like coffee too.
- La película es larga y, además, es aburrida. — The film is long, and on top of that it's boring.
- Llegó tarde y, encima, sin las llaves. — He turned up late, and without the keys on top of that.
:::
""",
        ["conn-addition"],
        explains=["conn-addition"],
    ),
    page(
        "es-sequence-connectives",
        "Primero, luego and al final",
        r"""
Sequence connectives put events in order: first this, then that, and in the end the last thing.

| Spanish | English |
| --- | --- |
| primero | first |
| luego | then, later |
| después | afterwards, then |
| entonces | then, at that moment; so |
| por último | lastly |
| al final | in the end |
| por fin | at last |

A story often runs *primero*, then *luego* or *después*, then *al final*: *Primero cenamos, luego fuimos al cine y al final tomamos algo en un bar.*

## Después or luego?

In a sequence they mean the same and swap freely. **Después de** with an infinitive or a noun means "after": *después de comer*, *después de la clase*. **Luego** on its own also means "later": *¡Hasta luego!* (See you later!)

## Por último, al final and por fin

- **Por último** brings in the last item of a list: *Por último, quiero dar las gracias a todos.*
- **Al final** says how things turned out, often not as planned: *Al final no fuimos.*
- **Por fin** says "at last" after a wait: *¡Por fin es viernes!*

:::examples
- Primero desayuno y después me ducho. — First I have breakfast and then I have a shower.
- Comemos y luego vamos al cine. — We'll eat and then go to the cinema.
- Al final no fuimos a la playa. — In the end we didn't go to the beach.
- ¡Por fin has llegado! — You're here at last!
:::
""",
        ["conn-sequence"],
        explains=["conn-sequence"],
    ),
]

NOUNS = nouns(
    """
ventana | f | window | home | | ¿Puedes abrir la ventana? | Can you open the window?
gato | m | cat | animals | | El gato duerme en el sofá. | The cat is sleeping on the sofa.
perro | m | dog | animals | | Mi perro juega en el parque. | My dog plays in the park.
casa | f | house; home | home | | Su casa está cerca del mar. | Their house is near the sea. | En casa means "at home".
libro | m | book | objects | | Leo un libro antes de dormir. | I read a book before I go to sleep.
agua | f | water | food | | El agua del mar está fría. | The sea water is cold. | Feminine, but el agua in the singular; las aguas in the plural.
pan | m | bread | food | | El pan todavía está caliente. | The bread is still warm.
mesa | f | table | home | | Las llaves están en la mesa. | The keys are on the table.
silla | f | chair | home | | Hay una silla libre al lado de la ventana. | There's a free chair by the window.
puerta | f | door | home | | Alguien llama a la puerta. | Someone's knocking at the door.
coche | m | car | transport | | Mi coche está en el taller. | My car is at the garage. | Latin America: el carro or el auto.
árbol | m | tree | nature | | Este árbol tiene cien años. | This tree is a hundred years old.
sol | m | sun | nature | | Hoy hace mucho sol. | It's very sunny today.
noche | f | night | time | | Por la noche hace frío. | It's cold at night.
amigo | m | friend | people | | Es mi mejor amigo. | He's my best friend. | A female friend is una amiga.
niño | m | child, boy | people | | El niño juega con su pelota. | The boy is playing with his ball. | A girl is una niña; los niños also means children in general.
"""
)

VERBS = [
    verb("comer", "to eat; to have lunch", ["food"],
         example="Comemos a las dos.", example_en="We have lunch at two.",
         note="In Spain la comida, the main meal, is eaten around two."),
    verb("beber", "to drink", ["food"],
         example="¿Bebes café por la mañana?", example_en="Do you drink coffee in the morning?",
         note="Latin America often says tomar for drinks."),
    verb("hablar", "to speak, to talk", [],
         example="Habla tres idiomas.", example_en="She speaks three languages."),
    verb("ir", "to go", [], **IR,
         example="Mañana voy a la playa.", example_en="I'm going to the beach tomorrow."),
]

CONNECTIVES = connectors(
    "connective",
    """
sin embargo | however | conn-contrast | Llueve; sin embargo, salimos a pasear. | It's raining; however, we're going out for a walk.
es que | the thing is, it's just that | conn-cause | No puedo ir; es que tengo que trabajar. | I can't go; the thing is, I have to work.
además | besides, on top of that | conn-addition | La película es larga y, además, es aburrida. | The film is long, and on top of that it's boring.
luego | then, later | conn-sequence | Comemos y luego vamos al cine. | We'll eat and then go to the cinema.
""",
    ["conectores"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
pero | but | conj-coordinating | Quiero ir, pero no tengo tiempo. | I want to go, but I don't have time.
sino | but, rather (after a negative) | conj-coordinating | No es mi hermano, sino mi primo. | He isn't my brother, he's my cousin.
porque | because | conj-subordinating | Me quedo en casa porque estoy cansado. | I'm staying at home because I'm tired.
aunque | although, even though | conj-subordinating | Aunque llueve, vamos a la playa. | Although it's raining, we're going to the beach. | Vamos a la playa aunque llueve.
""",
    ["conjunciones"],
)

ITEMS = PAGES + interleave(NOUNS, VERBS, CONNECTIVES + CONJUNCTIONS)

CORE = pack("es-core-v1", 1, "es", "Español · Lo esencial", ITEMS, DELTA)

PACKS = [CORE, es_foundations.PACK, es_everyday.PACK, es_fluency.PACK]
