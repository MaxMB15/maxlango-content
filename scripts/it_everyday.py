"""it-everyday-v1: A2. Talking about the past and the future, handling daily life
(shops, travel, work, health), and the small pronouns that make Italian sound
native."""

from common import build_units, interleave, page, pack, topic, topic_labels
from it_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("riflessivi", "Verbi riflessivi", "reflexive verbs", ["presente"]),
    topic("pronomi-oggetto", "Pronomi oggetto", "object pronouns", ["pronomi"]),
    topic("ci-ne", "Ci e ne", "the pronouns ci and ne", ["pronomi-oggetto"]),
    topic("clothing", "Abbigliamento", "clothing", ["articoli"]),
    topic("weather", "Meteo", "weather and seasons", ["articoli"]),
    topic("travel", "Viaggi", "travel", ["articoli"]),
    topic("work", "Lavoro", "work and study", ["articoli"]),
    topic("health", "Salute", "health", ["articoli"]),
    topic("leisure", "Tempo libero", "free time", ["articoli"]),
    topic("feelings", "Sentimenti", "feelings and character", ["aggettivi"]),
    topic("shopping", "Acquisti", "shopping and money", ["articoli"]),
    topic("expressions", "Espressioni", "set phrases and short replies", []),
    {
        "id": "conn-consequence",
        "kind": "connective-class",
        "label": "Conseguenza",
        "labelGloss": "the next statement is the result of the last one (allora, di conseguenza)",
        "order": 4,
        "appliesTo": {"kind": "connective"},
        "dependsOn": [],
    },
]

PAGES = [
    page(
        "it-passato-prossimo",
        "The passato prossimo",
        r"""
The **passato prossimo** is the everyday past tense of spoken Italian: *I ate*, *I have eaten* and *I did eat* are all *ho mangiato*.

It has two parts: the present of **avere** (or **essere**, see the next page) and the **past participle**.

| | mangiare |
| --- | --- |
| io | ho mangiato |
| tu | hai mangiato |
| lui / lei | ha mangiato |
| noi | abbiamo mangiato |
| voi | avete mangiato |
| loro | hanno mangiato |

## Regular participles

| Infinitive | Participle | Example |
| --- | --- | --- |
| -are | -ato | parlare → parlato |
| -ere | -uto | vendere → venduto |
| -ire | -ito | dormire → dormito, capire → capito |

## Irregular participles worth learning now

Most of them belong to -ere verbs, and many end in **-so**, **-sto** or **-tto**.

| | | |
| --- | --- | --- |
| essere → stato | avere → avuto | fare → fatto |
| dire → detto | prendere → preso | mettere → messo |
| vedere → visto | leggere → letto | scrivere → scritto |
| aprire → aperto | chiudere → chiuso | chiedere → chiesto |
| rispondere → risposto | perdere → perso | correre → corso |
| bere → bevuto | vivere → vissuto | piangere → pianto |

:::examples
- Ieri sera ho mangiato una pizza. — I had a pizza last night.
- Avete visto questo film? — Have you seen this film?
- Ho perso le chiavi di casa. — I've lost my house keys.
:::

## Negation and short adverbs

*Non* goes before the auxiliary: *Non ho capito* (I didn't understand). Short adverbs such as *già* (already), *mai* (ever, never), *ancora* (yet) and *appena* (just) sit between the auxiliary and the participle: *Ho già mangiato*, *Non ho mai visto Venezia*, *Non hai ancora finito?*

## One tense, two English ones

English separates "I ate" from "I have eaten"; Italian uses the passato prossimo for both: *Stamattina ho bevuto un caffè* (This morning I drank a coffee), *Hai mai bevuto la grappa?* (Have you ever drunk grappa?)

In books, and in everyday speech in parts of the south, you'll also meet the **passato remoto** (*parlai*, *fu*), a past for events felt as distant. You can speak perfectly well without it.

:::predict{prompt="noi (finire)" answer="abbiamo finito"}
:::
""",
        ["passato-prossimo"],
        "it-passato-prossimo",
        explains=["passato-prossimo"],
    ),
    page(
        "it-essere-verbs",
        "Essere or avere?",
        r"""
A group of very common verbs builds the passato prossimo with **essere** instead of avere. Most are about going from one place to another, or a change of state, and *essere*, *stare*, *piacere* and *succedere* join them.

| | | |
| --- | --- | --- |
| andare → andato | venire → venuto | arrivare → arrivato |
| partire → partito | tornare → tornato | entrare → entrato |
| uscire → uscito | salire → salito | scendere → sceso |
| cadere → caduto | restare → restato | rimanere → rimasto |
| nascere → nato | morire → morto | diventare → diventato |
| essere → stato | stare → stato | succedere → successo |

## Agreement

With essere, the participle **agrees with the subject** like an adjective: -o, -a, -i, -e.

:::examples
- Marco è andato a Roma. — Marco went to Rome.
- Giulia è andata a Roma. — Giulia went to Rome.
- I ragazzi sono partiti stamattina. — The boys left this morning.
- Le ragazze sono tornate tardi. — The girls came back late.
:::

A mixed group takes -i. Unlike French, you hear the ending, so it matters in speech too. The tables in this app show both endings, *sono andato/a*, *siamo andati/e*: pick the one that fits whoever is talking.

## Moving isn't always essere

It depends on the verb, not on the idea of movement. *Camminare* (to walk), *viaggiare* (to travel), *passeggiare* and *nuotare* take avere: *Abbiamo camminato tanto* (We walked a lot).

A few verbs take avere when they have a direct object: *Sono sceso* (I went down), but *Ho sceso le scale* (I went down the stairs). *Finire* and *cominciare* take avere with a person as the subject and essere with a thing: *Ho finito il libro*, but *Il film è finito*.

## Reflexive verbs take essere too

Every reflexive verb uses essere: *mi sono alzato*, *si è vestita*.

:::sort{groups="Avere: mangiato, dormito, viaggiato, letto, camminato | Essere: andato, nato, rimasto, uscito, caduto"}
:::

:::cloze{sentence="Ieri sera ___ rimasti a casa." blank="siamo"}
:::
""",
        ["passato-prossimo"],
        "it-essere-verbs",
    ),
    page(
        "it-imperfetto",
        "Imperfetto or passato prossimo?",
        r"""
Italian has two everyday past tenses, and the choice between them is about how you see the action, not when it happened.

- **Passato prossimo**: a completed event. Something happened. *Ho mangiato una pizza.*
- **Imperfetto**: the background, a habit, or a state. What things were like. *Mangiavo una pizza* (I was eating a pizza / I used to eat pizza).

## Forming the imperfetto

Drop the **-re** of the infinitive and add **-vo, -vi, -va, -vamo, -vate, -vano**. It's the most regular tense in Italian. Only *essere* is irregular, and a few verbs build on an older, longer stem: *fare → facevo*, *dire → dicevo*, *bere → bevevo*.

| | parlare | vendere | dormire | essere |
| --- | --- | --- | --- | --- |
| io | parlavo | vendevo | dormivo | ero |
| tu | parlavi | vendevi | dormivi | eri |
| lui / lei | parlava | vendeva | dormiva | era |
| noi | parlavamo | vendevamo | dormivamo | eravamo |
| voi | parlavate | vendevate | dormivate | eravate |
| loro | parlavano | vendevano | dormivano | erano |

The loro form keeps the stress of the io form: *parlàvo*, *parlàvano*.

## The film test

Imagine the past as a film. The **imperfetto** is the scenery and whatever was already going on. The **passato prossimo** is the action that moves the story on.

| Use | Example |
| --- | --- |
| a habit | Da piccolo andavo al mare ogni estate. |
| background, description | Era tardi e faceva freddo. |
| a state of mind or body | Ero stanco e avevo fame. |
| in progress, then interrupted | Guardavo la TV quando è arrivato Marco. |

:::examples
- Pioveva quando sono uscito. — It was raining when I went out.
- Da bambino abitavo a Napoli. — As a child I lived in Naples.
- Ogni domenica pranzavamo dalla nonna. — Every Sunday we used to have lunch at Grandma's.
- All'improvviso è entrato un uomo. — Suddenly a man came in.
:::

Signal words help: *sempre*, *di solito*, *ogni giorno*, *da piccolo* and *mentre* point to the imperfetto; *ieri*, *un giorno*, *all'improvviso* and *a un tratto* point to the passato prossimo.

## A trap: a finished stretch of time

A period with a clear end takes the passato prossimo, however long it lasted: *Ho abitato a Roma per tre anni* (I lived in Rome for three years, and then moved). *Abitavo a Roma* only paints the background for something else.

:::cloze{sentence="Quando avevo dieci anni, ___ in campagna." blank="abitavo"}
:::
""",
        ["imperfetto"],
        "it-imperfetto",
        explains=["imperfetto"],
    ),
    page(
        "it-reflexive-verbs",
        "Reflexive verbs: mi alzo",
        r"""
A **reflexive verb** has an extra pronoun that refers back to the subject. English does this rarely (*I hurt myself*). Italian does it all the time, often where English says "get": *alzarsi* (to get up), *vestirsi* (to get dressed), *sposarsi* (to get married), *arrabbiarsi* (to get angry).

The infinitive ends in **-si**: *alzarsi* is *alzare* plus *si*.

| | alzarsi |
| --- | --- |
| io | mi alzo |
| tu | ti alzi |
| lui / lei | si alza |
| noi | ci alziamo |
| voi | vi alzate |
| loro | si alzano |

## Daily routine

A morning in Italian is almost all reflexive: *mi sveglio, mi alzo, mi lavo, mi vesto, mi pettino*.

With body parts and clothes, Italian uses the article, not a possessive: *Mi lavo **le** mani* (I wash my hands), *Si mette **il** cappotto* (She puts her coat on). The pronoun already says whose.

## With an infinitive

The pronoun changes with the person, and either goes before the helper verb or is glued to the end of the infinitive, which drops its final e: *Mi devo alzare presto* or *Devo alzarmi presto* (I have to get up early). Both are correct.

## Each other

In the plural the pronoun can mean "each other": *Ci vediamo domani* (See you tomorrow, literally "we see each other"), *Si amano* (They love each other).

## Past and negation

Reflexive verbs take **essere** in the passato prossimo, and the participle agrees: *mi sono alzato*, *Anna si è vestita*. *Non* goes before the pronoun: *Non mi ricordo* (I don't remember).

:::examples
- Mi sveglio alle sette ogni mattina. — I wake up at seven every morning.
- Ci siamo divertiti molto alla festa. — We had a great time at the party.
- Si veste sempre di nero. — She always dresses in black.
:::

:::predict{prompt="tu (svegliarsi)" answer="ti svegli"}
:::
""",
        ["riflessivi"],
        "it-reflexive-verbs",
        explains=["riflessivi"],
    ),
    page(
        "it-object-pronouns",
        "Object pronouns: lo, la, gli, le",
        r"""
Italian object pronouns usually go **before the verb**, the opposite of English. *I see him* is *lo vedo*.

| | direct (whom?) | indirect (to whom?) |
| --- | --- | --- |
| me | mi | mi |
| you | ti | ti |
| him, it | lo | gli |
| her, it | la | le |
| you (polite) | La | Le |
| us | ci | ci |
| you all | vi | vi |
| them | li (m), le (f) | gli |

## Direct or indirect?

Ask how the Italian verb attaches to the person, not the English one. *Telefonare a* and *dire a* take **a**, so they take the indirect pronoun: *Telefono a Marco → Gli telefono* (I'm phoning him). *Aiutare* and *chiamare* take the person directly: *Aiuto Marco → Lo aiuto* (I'm helping him).

*Gli* is "to him" and, in everyday Italian, also "to them": *Gli scrivo* (I'll write to them). *Le* is "to her".

## Where they go

- Before a conjugated verb: *La vedo stasera.*
- Glued to the end of an infinitive, which drops its e: *Voglio vederla*, or *La voglio vedere*.
- Glued to the end of an informal command: *Guardalo!* (Look at it!), *Dimmi!* (Tell me!). One-syllable commands double the consonant: *dimmi*, *fammi*, *dammi*.
- With the polite form they stay in front: *Mi dica* (Tell me, what can I do for you?).

## In the past

*Lo* and *la* become **l'** before *ho*, *hai*, *ha* and *hanno*, and the participle agrees with them: *Hai visto Anna? Sì, l'ho vista.* With *li* and *le* too: *Le chiavi? Le ho prese io.*

## Two together

When an indirect pronoun meets *lo, la, li, le* or *ne*, *mi, ti, ci, vi* become **me, te, ce, ve**, and *gli* and *le* both become **glie-**, written as one word with what follows: *Me lo dai?* (Will you give it to me?), *Te lo prometto* (I promise you), *Glielo dico io* (I'll tell him, or her).

:::examples
- Conosci Paolo? Sì, lo conosco bene. — Do you know Paolo? Yes, I know him well.
- Ti chiamo domani. — I'll call you tomorrow.
- Gli ho scritto un messaggio. — I sent him a message.
:::

:::cloze{sentence="Telefoni a Maria? Sì, ___ telefono stasera." blank="le"}
:::
""",
        ["pronomi-oggetto"],
        "it-object-pronouns",
        explains=["pronomi-oggetto"],
    ),
    page(
        "it-ci-ne",
        "Ci and ne",
        r"""
**Ci** and **ne** are two small pronouns with no English match. They're everywhere in spoken Italian, and inside many set phrases.

## Ci: there, and about it

**Ci** stands for a place, or for **a + a thing**:

:::examples
- Vai a Roma? Sì, ci vado domani. — Are you going to Rome? Yes, I'm going there tomorrow.
- Pensi al viaggio? Sì, ci penso sempre. — Are you thinking about the trip? Yes, I think about it all the time.
- Credi ai fantasmi? No, non ci credo. — Do you believe in ghosts? No, I don't believe in them.
:::

You already know it from *c'è* and *ci sono*. It also builds some everyday verbs:

| Expression | Meaning | Example |
| --- | --- | --- |
| volerci | to take (time, things needed) | Ci vuole un'ora. Ci vogliono due ore. |
| metterci | to take (someone, time) | Ci metto dieci minuti. |
| avercela (con qualcuno) | to be cross with someone | Ce l'hai con me? |
| farcela | to manage, to make it | Ce la fai? |

*Ci vuole* agrees with what is needed; *ci metto* agrees with the person: *Ci mettiamo poco* (It won't take us long).

In speech, *avere* also takes *ci* before *lo*, *la*, *li* and *le*: *Hai le chiavi? Sì, ce le ho.*

## Ne: of it, some

**Ne** stands for **di + something**, and above all for a quantity. Where English can drop the noun (*I've got three*), Italian has to say *ne*:

- *Quanti figli hai? Ne ho tre.* (How many children have you got? Three.)
- *Vuoi del vino? Sì, ne prendo un bicchiere.* (Some wine? Yes, I'll have a glass.)
- *Che ne pensi?* (What do you think of it?)

Leaving out *ne* (*ho tre*) is the classic mistake. In the passato prossimo the participle agrees with whatever *ne* stands for: *Le mele? Ne ho mangiate due.*

## In set phrases

*Me ne vado* (I'm off), *Non ne posso più* (I can't stand any more), *Non ne ho idea* (I've no idea), *Ne vale la pena* (It's worth it).

## Ci also means "us"

Don't confuse the two jobs of *ci*: *Ci vediamo* (we see each other) and *Ci vado* (I go there). The verb tells you which one it is.

:::cloze{sentence="Le mele sono buone, ___ compro un chilo." blank="ne"}
:::
""",
        ["ci-ne"],
        "it-ci-ne",
        explains=["ci-ne"],
    ),
    page(
        "it-futuro",
        "The future, and the future of guessing",
        r"""
The **futuro semplice** says what will happen. Italians often use the present for plans (*Domani parto*), so the future sounds a little more distant, formal or uncertain. It's the tense for promises, predictions and guesses.

Drop the final **-e** of the infinitive, change the **a** of -are verbs to **e**, and add **-ò, -ai, -à, -emo, -ete, -anno**.

| | parlare | vendere | dormire |
| --- | --- | --- | --- |
| io | parlerò | venderò | dormirò |
| tu | parlerai | venderai | dormirai |
| lui / lei | parlerà | venderà | dormirà |
| noi | parleremo | venderemo | dormiremo |
| voi | parlerete | venderete | dormirete |
| loro | parleranno | venderanno | dormiranno |

The written accent on *-ò* and *-à* matters: it puts the stress on the last syllable.

Spelling keeps the sound, as in the present: *cercare → cercherò*, *pagare → pagherò*, *mangiare → mangerò*, *cominciare → comincerò*.

## Irregular stems

The endings never change; only the stem does. Many verbs simply lose a vowel.

| | | |
| --- | --- | --- |
| essere → sarò | avere → avrò | andare → andrò |
| potere → potrò | dovere → dovrò | sapere → saprò |
| vedere → vedrò | vivere → vivrò | cadere → cadrò |
| fare → farò | dare → darò | stare → starò |
| volere → vorrò | venire → verrò | tenere → terrò |
| rimanere → rimarrò | bere → berrò | |

## Quando + future

After **quando** and **appena** (as soon as), Italian uses the future where English uses the present: *Quando avrò tempo, leggerò di più* (When I have time, I'll read more).

## The future of guessing

The future also makes guesses about the present, like English "must":

- *Dov'è Luca? Sarà ancora in ufficio.* (He must still be at the office.)
- *Che ore sono? Saranno le dieci.* (It must be about ten.)
- *Quanti anni ha? Avrà trent'anni.* (He must be about thirty.)

:::examples
- Domani farà bel tempo. — The weather will be nice tomorrow.
- Ti chiamerò stasera. — I'll call you tonight.
- Quando sarò a Roma, visiterò il Colosseo. — When I'm in Rome, I'll visit the Colosseum.
:::

:::predict{prompt="loro (venire)" answer="verranno"}
:::
""",
        ["futuro-semplice"],
        "it-futuro",
        explains=["futuro-semplice"],
    ),
    page(
        "it-comparisons",
        "Più, meno and -issimo",
        r"""
Comparisons put **più** (more) or **meno** (less) before the adjective, and **di** before the second thing.

| | Structure | Example |
| --- | --- | --- |
| more | più ... di | Marco è più alto di me. |
| less | meno ... di | Questo film è meno lungo dell'altro. |
| as | (così) ... come, (tanto) ... quanto | Anna è alta come sua sorella. |

*Di* joins the article as usual: *più grande della mia*, *meno caro del treno*. After *di*, *come* and *quanto*, use the stressed pronouns: *me, te, lui, lei, noi, voi, loro*.

## Di or che?

Use **che** when you compare two adjectives, two verbs, or two phrases that start with a preposition:

- *È più bello che utile.* (It's more beautiful than useful.)
- *Mi piace più leggere che guardare la TV.* (I like reading more than watching TV.)
- *Fa più caldo a Roma che a Milano.* (It's hotter in Rome than in Milan.)

With two nouns or pronouns, it's *di*, except when you compare two quantities: *Bevo più acqua che vino*.

## The superlative

Add the article, and use **di** for "in": *È la città più bella d'Italia* (It's the most beautiful city in Italy). Note the order: noun, then *più*.

## -issimo: very

Drop the last vowel and add **-issimo**: *bello → bellissimo*, *stanco → stanchissimo*, *caro → carissimo*. It means "very" and agrees like any -o adjective: *una giornata bellissima*. Italians use it far more than English uses "extremely".

## Better and worse

| | better | worse |
| --- | --- | --- |
| adjective (with a noun) | migliore | peggiore |
| adverb (with a verb) | meglio | peggio |

*Questo vino è migliore* (an adjective), *Oggi sto meglio* (an adverb). "The best" is *il migliore*. *Più buono* exists too, mostly for food that tastes better.

:::examples
- Il treno è più veloce dell'autobus. — The train is faster than the bus.
- Mia sorella è più alta di me. — My sister is taller than me.
- È il ristorante più caro della città. — It's the most expensive restaurant in town.
:::

:::cloze{sentence="Roma è più grande ___ Firenze." blank="di"}
:::
""",
        ["aggettivi"],
        "it-comparisons",
    ),
    page(
        "it-time-expressions",
        "Da, fa and per: time words",
        r"""
English uses the present perfect for something that started in the past and is still going on: *I've lived here for three years*. Italian uses the **present tense** with **da**.

:::examples
- Studio l'italiano da due anni. — I've been studying Italian for two years.
- Ti aspetto da un'ora! — I've been waiting for you for an hour!
- Da quanto tempo abiti qui? — How long have you lived here?
:::

Saying *ho abitato qui per tre anni* about something still true is a very common mistake: it tells people you've moved out.

## The other time words

| Word | Meaning | Example |
| --- | --- | --- |
| fa | ago (after the time) | Sono arrivato due giorni fa. |
| per | for (a finished period) | Ho dormito per otto ore. |
| tra, fra | in (from now) | Il treno parte tra dieci minuti. |
| in | in (the time it takes) | Ho fatto il viaggio in due ore. |
| ogni | every | Vado in palestra ogni giorno. |

*Tra* and *fra* mean the same; Italians pick whichever sounds better: *tra fratelli*, *fra tre giorni*.

## Days and parts of the day

A day with the article means "every": *il lunedì* (on Mondays). Without it, the coming or the last one: *lunedì* (on Monday). In the same way, *la mattina* is "in the mornings", and *stamattina*, *stasera* and *stanotte* are "this morning", "this evening" and "tonight" (or "last night").

Also: *ieri* (yesterday), *oggi* (today), *domani* (tomorrow), *dopodomani* (the day after tomorrow), *l'altro ieri* (the day before yesterday).

Months take no capital and use *a* or *in*: *a maggio*, *in agosto*. Dates use the plain number with *il* (*l'* before 8 and 11), except the first of the month: *il 3 marzo*, *l'8 marzo*, *il primo maggio*.

:::cloze{sentence="Abito a Bologna ___ tre anni." blank="da"}
:::
""",
        ["time"],
        "it-time-expressions",
        explains=["time"],
    ),
    page(
        "it-gender-patterns",
        "Masculine or feminine?",
        r"""
Most Italian nouns tell you their gender by their last letter. The rule works far more often than in French or German.

| Ending | Gender | Examples |
| --- | --- | --- |
| -o | masculine | il libro, il ragazzo |
| -a | feminine | la casa, la ragazza |
| -e | either: learn it | il fiore, la notte |
| -zione, -sione | feminine | la stazione, la televisione |
| -tà, -tù | feminine | la città, la gioventù |
| -ore | masculine | il colore, il dolore |
| a consonant | masculine (foreign words) | il bar, lo sport, il computer |

## The exceptions worth knowing

- Feminine in -o: *la mano* (hand), *la radio*, and short forms that keep the gender of the long word: *la foto* (fotografia), *la moto* (motocicletta), *l'auto* (automobile).
- Masculine in -a: many words from Greek in **-ma**, such as *il problema*, *il programma*, *il sistema*, *il clima* and *il tema*. Also *il cinema* (from cinematografo) and *il papà*.
- Words in **-ista** and **-ante** are the same for both sexes; only the article changes: *il turista*, *la turista*; *il cantante*, *la cantante*.
- Some jobs have a separate female form: *lo studente → la studentessa*, *il professore → la professoressa*, *l'attore → l'attrice*.

## Plurals that break the rule

| Type | Singular | Plural |
| --- | --- | --- |
| stressed last vowel | la città, il caffè | le città, i caffè |
| one syllable | il re, il tè | i re, i tè |
| foreign words | il bar, il film | i bar, i film |
| short forms | la foto, il cinema | le foto, i cinema |
| -ma words | il problema | i problemi |
| body parts that turn feminine | il braccio, il dito | le braccia, le dita |

And a few to learn by heart: *l'uovo → le uova*, *il paio → le paia*, *l'uomo → gli uomini*, *la mano → le mani*.

:::examples
- Il problema è il prezzo. — The problem is the price.
- Ho fatto tante foto in vacanza. — I took lots of photos on holiday.
- Il cinema è vicino alla stazione. — The cinema is near the station.
:::

:::sort{groups="Maschile: problema, cinema, fiore, sport, colore | Femminile: mano, foto, stazione, città, notte"}
:::
""",
        ["genere"],
        "it-gender-patterns",
        explains=["genere", "maschile", "femminile"],
    ),
    page(
        "it-stare-gerund",
        "Sto facendo: happening right now",
        r"""
To stress that something is going on **right now**, Italian uses **stare** and the gerund, much like English "be doing":

| Italian | English |
| --- | --- |
| sto lavorando | I'm working (right now) |
| stai mangiando | you're eating |
| sta piovendo | it's raining |
| stiamo uscendo | we're going out |
| state dormendo? | are you all asleep? |
| stanno arrivando | they're on their way |

## Forming the gerund

-are verbs take **-ando**; -ere and -ire verbs take **-endo**: *parlare → parlando*, *leggere → leggendo*, *partire → partendo*. Verbs with a longer old stem keep it: *fare → facendo*, *dire → dicendo*, *bere → bevendo*. The gerund never changes its ending.

## Less often than English

The plain present already means "I'm doing": *Che fai?* (What are you doing?), *Lavoro* (I'm working). Keep *stare* and the gerund for an action caught in the middle, never for plans: "I'm leaving tomorrow" is *Parto domani*.

## In the past

*Stare* in the imperfetto describes what was going on when something happened: *Stavo dormendo quando hai chiamato* (I was asleep when you called).

## Stare per: about to

**Stare per** and an infinitive means "to be about to": *Sto per uscire* (I'm about to go out), *Il film sta per cominciare* (The film is about to start).

## Pronouns

A pronoun goes before *stare* or on the end of the gerund: *Lo sto facendo* or *Sto facendolo*. The first is more common.

:::examples
- Che cosa stai facendo? — What are you doing?
- Sta piovendo, prendi l'ombrello. — It's raining, take your umbrella.
- Stavamo cenando quando è arrivato Luca. — We were having dinner when Luca arrived.
:::

:::cloze{sentence="Non posso rispondere, sto ___." blank="guidando"}
:::
""",
        ["presente"],
        "it-stare-gerund",
    ),
]

NOUNS = nouns(
    """
# clothing
vestito | m | dress; suit; (pl.) clothes | clothing | vestiti | Stasera metto il vestito rosso. | Tonight I'm wearing the red dress.
camicia | f | shirt | clothing | camicie | Questa camicia va stirata. | This shirt needs ironing.
gonna | f | skirt | clothing | gonne | Ti sta bene questa gonna. | That skirt suits you.
cappotto | m | coat | clothing | cappotti | Questo cappotto è caldissimo. | This coat is really warm.
giacca | f | jacket | clothing | giacche | Porta una giacca, stasera fa fresco. | Bring a jacket, it's chilly tonight.
maglione | m | jumper, sweater | clothing | maglioni | La nonna mi ha fatto un maglione. | Grandma knitted me a jumper.
maglietta | f | T-shirt | clothing | magliette | D'estate porto solo magliette. | In summer I only wear T-shirts.
scarpa | f | shoe | clothing | scarpe | Queste scarpe mi fanno male. | These shoes hurt my feet.
cappello | m | hat | clothing | cappelli | Metti il cappello, c'è il sole. | Put your hat on, it's sunny.
sciarpa | f | scarf | clothing | sciarpe | Fa freddo, prendi la sciarpa. | It's cold, take your scarf.
borsa | f | bag, handbag | clothing | borse | Ho dimenticato la borsa in macchina. | I left my bag in the car.
ombrello | m | umbrella | clothing | ombrelli | Hai preso l'ombrello? | Did you take the umbrella?
# weather
tempo | m | weather; time | weather | tempi | Con questo tempo restiamo a casa. | We're staying in with this weather.
pioggia | f | rain | weather | piogge | La pioggia non smette da ieri. | The rain hasn't stopped since yesterday.
neve | f | snow | weather | | I bambini giocano nella neve. | The children are playing in the snow.
vento | m | wind | weather | venti | Oggi c'è molto vento. | It's very windy today.
nuvola | f | cloud | weather | nuvole | Non c'è una nuvola in cielo. | There isn't a cloud in the sky.
cielo | m | sky | weather | cieli | Stanotte il cielo è pieno di stelle. | Tonight the sky is full of stars.
temporale | m | thunderstorm | weather | temporali | Stanotte c'è stato un temporale. | There was a thunderstorm last night.
estate | f | summer | weather | estati | D'estate andiamo sempre al mare. | In summer we always go to the seaside.
inverno | m | winter | weather | inverni | L'inverno a Milano è freddo e umido. | Winter in Milan is cold and damp.
primavera | f | spring | weather | primavere | In primavera fioriscono gli alberi. | In spring the trees blossom.
autunno | m | autumn | weather | autunni | In autunno cadono le foglie. | In autumn the leaves fall.
stagione | f | season | weather | stagioni | Qual è la tua stagione preferita? | What's your favourite season?
# travel
viaggio | m | journey, trip | travel | viaggi | Il viaggio in treno dura tre ore. | The train journey takes three hours.
biglietto | m | ticket | travel | biglietti | Ho comprato i biglietti online. | I bought the tickets online.
valigia | f | suitcase | travel | valigie | Non ho ancora fatto la valigia. | I haven't packed my suitcase yet.
passaporto | m | passport | travel | passaporti | Non dimenticare il passaporto! | Don't forget your passport!
albergo | m | hotel | travel | alberghi | L'albergo è vicino alla spiaggia. | The hotel is near the beach.
spiaggia | f | beach | travel | spiagge | Passiamo la giornata in spiaggia. | We're spending the day on the beach.
mare | m | sea; seaside | travel | mari | La casa ha la vista sul mare. | The house has a sea view.
montagna | f | mountain; the mountains | travel | montagne | D'inverno andiamo in montagna. | In winter we go to the mountains.
paese | m | country; village | travel | paesi | L'Italia è un paese bellissimo. | Italy is a beautiful country.
vacanza | f | holiday | travel | vacanze | Quest'anno andiamo in vacanza in Puglia. | This year we're going on holiday to Puglia.
# transport
aereo | m | plane | transport | aerei | L'aereo parte alle sei. | The plane leaves at six.
treno | m | train | transport | treni | Il treno è in ritardo di venti minuti. | The train is twenty minutes late.
autobus | m | bus | transport | autobus | Prendo l'autobus per andare al lavoro. | I take the bus to work.
bicicletta | f | bicycle | transport | biciclette | Vado al lavoro in bicicletta. | I go to work by bike.
metropolitana | f | underground, metro | transport | metropolitane | La metropolitana è più veloce. | The underground is quicker.
nave | f | ship | transport | navi | Andiamo in Sardegna in nave. | We're going to Sardinia by boat.
aeroporto | m | airport | transport | aeroporti | Ti accompagno io all'aeroporto. | I'll take you to the airport.
fermata | f | stop (bus, tram) | transport | fermate | Ci vediamo alla fermata del tram. | See you at the tram stop.
# work
lavoro | m | work; job | work | lavori | Ho trovato un nuovo lavoro. | I've found a new job.
ufficio | m | office | work | uffici | L'ufficio chiude alle sei. | The office closes at six.
azienda | f | company, firm | work | aziende | Lavoro in un'azienda di moda. | I work for a fashion company.
capo | m | boss | work | capi | Il mio capo è molto esigente. | My boss is very demanding.
riunione | f | meeting | work | riunioni | La riunione è alle dieci. | The meeting is at ten.
stipendio | m | salary, pay | work | stipendi | Lo stipendio arriva a fine mese. | Pay comes in at the end of the month.
mestiere | m | trade, job | work | mestieri | Che mestiere fa tuo padre? | What does your father do for a living?
studente | m | student | work | studenti | Sono uno studente di medicina. | I'm a medical student.
professore | m | teacher; professor | work | professori | Il professore spiega molto bene. | The teacher explains things very well.
lezione | f | lesson, class | work | lezioni | La lezione comincia alle nove. | The lesson starts at nine.
esame | m | exam | work | esami | Domani ho l'esame di storia. | Tomorrow I have my history exam.
computer | m | computer | work | computer | Lavoro al computer tutto il giorno. | I work at the computer all day.
# health
salute | f | health | health | | Il fumo fa male alla salute. | Smoking is bad for your health.
medico | m | doctor | health | medici | Devo andare dal medico. | I have to go to the doctor's.
farmacia | f | chemist's, pharmacy | health | farmacie | Compro l'aspirina in farmacia. | I buy aspirin at the chemist's.
medicina | f | medicine | health | medicine | Prendi la medicina dopo i pasti. | Take the medicine after meals.
raffreddore | m | cold (illness) | health | raffreddori | Ho il raffreddore da una settimana. | I've had a cold for a week.
febbre | f | fever, temperature | health | febbri | Il bambino ha la febbre alta. | The child has a high temperature.
dolore | m | pain | health | dolori | Ho un dolore alla spalla. | I've got a pain in my shoulder.
appuntamento | m | appointment; date | health | appuntamenti | Ho un appuntamento dal dentista. | I have a dentist's appointment.
# leisure
film | m | film | leisure | film | Abbiamo visto un bel film ieri sera. | We saw a good film last night.
musica | f | music | leisure | musiche | Ascolto musica mentre lavoro. | I listen to music while I work.
canzone | f | song | leisure | canzoni | Questa canzone mi piace tantissimo. | I love this song.
sport | m | sport | leisure | sport | Faccio sport tre volte alla settimana. | I do sport three times a week.
partita | f | match, game | leisure | partite | Stasera guardiamo la partita. | Tonight we're watching the match.
gioco | m | game; toy | leisure | giochi | I bambini hanno tanti giochi. | The children have lots of toys.
festa | f | party; holiday | leisure | feste | Sabato facciamo una festa. | We're having a party on Saturday.
compleanno | m | birthday | leisure | compleanni | Buon compleanno, Marta! | Happy birthday, Marta!
regalo | m | present, gift | leisure | regali | Grazie del regalo! | Thanks for the present!
foto | f | photo | leisure | foto | Facciamo una foto tutti insieme? | Shall we take a photo all together?
cinema | m | cinema | leisure | cinema | Andiamo al cinema stasera? | Shall we go to the cinema tonight?
# shopping
prezzo | m | price | shopping | prezzi | I prezzi sono saliti molto. | Prices have gone up a lot.
euro | m | euro | shopping | euro | Sono dieci euro in tutto. | That's ten euros altogether.
resto | m | change (money); the rest | shopping | resti | Tenga il resto. | Keep the change.
carta di credito | f | credit card | shopping | carte di credito | Accettate la carta di credito? | Do you take credit cards?
cassa | f | till, checkout | shopping | casse | Si paga alla cassa. | You pay at the till.
supermercato | m | supermarket | shopping | supermercati | Vado al supermercato a fare la spesa. | I'm going to the supermarket to do the shopping.
scontrino | m | receipt | shopping | scontrini | Mi può dare lo scontrino? | Could you give me the receipt?
# home
forchetta | f | fork | home | forchette | Mi porta una forchetta pulita? | Could you bring me a clean fork?
coltello | m | knife | home | coltelli | Attento, il coltello taglia molto. | Careful, the knife is very sharp.
cucchiaio | m | spoon | home | cucchiai | Mangio la minestra con il cucchiaio. | I eat soup with a spoon.
piatto | m | plate; dish | home | piatti | Stasera lavi tu i piatti? | Are you doing the dishes tonight?
bicchiere | m | glass | home | bicchieri | Posso avere un bicchiere d'acqua? | Can I have a glass of water?
bottiglia | f | bottle | home | bottiglie | Abbiamo bevuto una bottiglia di vino. | We drank a bottle of wine.
luce | f | light | home | luci | Spegni la luce, per favore. | Turn off the light, please.
# nature
fiore | m | flower | nature | fiori | Ti ho comprato dei fiori. | I bought you some flowers.
bosco | m | wood, forest | nature | boschi | Facciamo una passeggiata nel bosco. | Let's go for a walk in the woods.
fiume | m | river | nature | fiumi | Il Tevere è il fiume di Roma. | The Tiber is Rome's river.
lago | m | lake | nature | laghi | D'estate facciamo il bagno nel lago. | In summer we swim in the lake.
campagna | f | countryside | nature | campagne | Il fine settimana andiamo in campagna. | At the weekend we go to the countryside.
# animals
uccello | m | bird | animals | uccelli | Sento cantare gli uccelli. | I can hear the birds singing.
cavallo | m | horse | animals | cavalli | Mia figlia va a cavallo. | My daughter goes horse riding.
mucca | f | cow | animals | mucche | Le mucche sono nel prato. | The cows are in the field.
maiale | m | pig; pork | animals | maiali | Non mangio carne di maiale. | I don't eat pork.
"""
)

ADJECTIVES = adjectives(
    """
lungo, lunga, lunghi, lunghe | long | Ha i capelli lunghi. | She has long hair.
corto, corta, corti, corte | short (in length) | Questa gonna è troppo corta. | This skirt is too short.
alto, alta, alti, alte | tall; high | Mio fratello è molto alto. | My brother is very tall.
basso, bassa, bassi, basse | short (in height); low | Parla a voce bassa, il bambino dorme. | Speak quietly, the baby's asleep.
pesante, pesante, pesanti, pesanti | heavy | La valigia è troppo pesante. | The suitcase is too heavy.
leggero, leggera, leggeri, leggere | light | Stasera voglio una cena leggera. | I want a light dinner tonight.
veloce, veloce, veloci, veloci | fast, quick | Ho bisogno di una risposta veloce. | I need a quick answer.
lento, lenta, lenti, lente | slow | Il servizio in questo bar è lento. | The service in this café is slow.
"""
) + adjectives(
    """
felice, felice, felici, felici | happy | Sono felice per te! | I'm happy for you!
triste, triste, tristi, tristi | sad | Perché sei così triste? | Why are you so sad?
arrabbiato, arrabbiata, arrabbiati, arrabbiate | angry | Sei ancora arrabbiata con me? | Are you still angry with me?
divertente, divertente, divertenti, divertenti | funny, fun | Il film è molto divertente. | The film is really funny.
serio, seria, seri, serie | serious | Mio padre è una persona seria. | My father is a serious person.
timido, timida, timidi, timide | shy | Da piccolo ero molto timido. | I was very shy as a child.
pigro, pigra, pigri, pigre | lazy | La domenica sono pigrissimo. | On Sundays I'm really lazy.
sportivo, sportiva, sportivi, sportive | sporty | Mia sorella è molto sportiva. | My sister is very sporty.
""",
    ["feelings"],
) + adjectives(
    """
malato, malata, malati, malate | ill, sick | Oggi non vengo, sono malato. | I'm not coming today, I'm ill.
occupato, occupata, occupati, occupate | busy; taken, engaged | Scusi, questo posto è occupato? | Excuse me, is this seat taken?
libero, libera, liberi, libere | free | Sei libero sabato sera? | Are you free on Saturday evening?
pronto, pronta, pronti, pronte | ready; hello? (on the phone) | La cena è pronta! | Dinner's ready!
pieno, piena, pieni, piene | full | Il treno è pieno di turisti. | The train is full of tourists.
vuoto, vuota, vuoti, vuote | empty | Il frigo è vuoto, facciamo la spesa. | The fridge is empty, let's go shopping.
pulito, pulita, puliti, pulite | clean | Metti una maglietta pulita. | Put on a clean T-shirt.
sporco, sporca, sporchi, sporche | dirty | Hai le mani sporche! | Your hands are dirty!
primo, prima, primi, prime | first | È la prima volta che vengo a Roma. | It's the first time I've been to Rome. | before
ultimo, ultima, ultimi, ultime | last | Questo è l'ultimo treno per Milano. | This is the last train to Milan. | before
"""
)

VERBS = [
    # Reflexive: all take essere.
    verb("alzarsi", "to get up", [], pp="alzato",
         example="Domani mi alzo alle sei.", example_en="Tomorrow I'm getting up at six."),
    verb("svegliarsi", "to wake up", [], pp="svegliato",
         example="Mi sveglio sempre prima della sveglia.", example_en="I always wake up before the alarm."),
    verb("vestirsi", "to get dressed", [], pp="vestito",
         example="Mi vesto e arrivo.", example_en="I'll get dressed and be right there."),
    verb("lavarsi", "to wash (yourself)", [], pp="lavato",
         example="Mi lavo i capelli ogni mattina.", example_en="I wash my hair every morning."),
    verb("sentirsi", "to feel", ["health"], pp="sentito",
         example="Non mi sento bene oggi.", example_en="I don't feel well today."),
    verb("divertirsi", "to have fun, to enjoy yourself", ["leisure"], pp="divertito",
         example="Ti sei divertito alla festa?", example_en="Did you have fun at the party?"),
    verb("sedersi", "to sit down", [], pp="seduto",
         present="siedo siedi siede sediamo sedete siedono",
         subj="sieda sieda sieda sediamo sediate siedano",
         example="Posso sedermi qui?", example_en="May I sit here?"),
    # Essere in the passato prossimo.
    verb("tornare", "to come back, to return", [], aux="essere", pp="tornato",
         example="A che ora torni stasera?", example_en="What time are you back tonight?"),
    verb("entrare", "to come in, to go in", [], aux="essere", pp="entrato",
         example="Prego, entri pure.", example_en="Please, do come in."),
    verb("diventare", "to become", [], aux="essere", pp="diventato",
         example="Vuole diventare medico.", example_en="She wants to become a doctor."),
    verb("cadere", "to fall", [], aux="essere", pp="caduto", fut="cadr",
         example="Il bambino è caduto dalla bici.", example_en="The child fell off his bike."),
    verb("salire", "to go up; to get on, to get in", ["transport"], aux="essere", pp="salito",
         present="salgo sali sale saliamo salite salgono",
         subj="salga salga salga saliamo saliate salgano",
         example="Sali in macchina, ti porto io.", example_en="Get in the car, I'll drive you."),
    verb("scendere", "to go down; to get off", ["transport"], aux="essere", pp="sceso",
         example="Scendiamo alla prossima fermata.", example_en="We're getting off at the next stop."),
    verb("nascere", "to be born", [], aux="essere", pp="nato",
         example="Mia figlia è nata a marzo.", example_en="My daughter was born in March."),
    verb("morire", "to die", [], aux="essere", pp="morto",
         present="muoio muori muore moriamo morite muoiono",
         subj="muoia muoia muoia moriamo moriate muoiano",
         example="Muoio di fame!", example_en="I'm starving!"),
    verb("rimanere", "to stay, to remain", [], aux="essere", pp="rimasto",
         present="rimango rimani rimane rimaniamo rimanete rimangono", fut="rimarr",
         subj="rimanga rimanga rimanga rimaniamo rimaniate rimangano",
         example="Quanto tempo rimani a Roma?", example_en="How long are you staying in Rome?"),
    verb("succedere", "to happen", [], aux="essere", pp="successo",
         example="Che cosa è successo?", example_en="What happened?"),
    # Irregular participles.
    verb("aprire", "to open", [], pp="aperto",
         example="A che ora apre il museo?", example_en="What time does the museum open?"),
    verb("chiudere", "to close", [], pp="chiuso",
         example="Chiudi la porta, per favore.", example_en="Close the door, please."),
    verb("chiedere", "to ask", [], pp="chiesto",
         example="Posso chiederti un favore?", example_en="Can I ask you a favour?"),
    verb("rispondere", "to answer, to reply", [], pp="risposto",
         example="Perché non rispondi al telefono?", example_en="Why don't you answer the phone?"),
    verb("perdere", "to lose; to miss (a train, a bus)", [], pp="perso",
         example="Ho perso l'autobus di nuovo.", example_en="I missed the bus again."),
    verb("piangere", "to cry", [], pp="pianto",
         example="Il bambino piange perché ha fame.", example_en="The baby is crying because he's hungry."),
    verb("correre", "to run", ["leisure"], pp="corso",
         example="Corro al parco ogni mattina.", example_en="I go running in the park every morning."),
    verb("conoscere", "to know (a person, a place); to meet", [], pp="conosciuto",
         example="Conosci un buon dentista?", example_en="Do you know a good dentist?"),
    verb("credere", "to believe", [], pp="creduto",
         example="Non ci credo!", example_en="I don't believe it!"),
    verb("vivere", "to live", [], pp="vissuto", fut="vivr",
         example="Vivo in Italia da cinque anni.", example_en="I've been living in Italy for five years."),
    verb("ricevere", "to receive, to get", [], pp="ricevuto",
         example="Hai ricevuto il mio messaggio?", example_en="Did you get my message?"),
    verb("mandare", "to send", [], pp="mandato",
         example="Ti mando le foto stasera.", example_en="I'll send you the photos tonight."),
    verb("pagare", "to pay (for)", ["shopping"], pp="pagato",
         example="Oggi pago io.", example_en="It's on me today."),
    verb("dimenticare", "to forget", [], pp="dimenticato",
         example="Ho dimenticato il telefono a casa.", example_en="I left my phone at home."),
    verb("tenere", "to hold, to keep", [], pp="tenuto",
         present="tengo tieni tiene teniamo tenete tengono", fut="terr",
         subj="tenga tenga tenga teniamo teniate tengano",
         example="Tieni, questo è per te.", example_en="Here, this is for you."),
    verb("pulire", "to clean", ["home"], pp="pulito", isc=True,
         example="Il sabato puliamo la casa.", example_en="On Saturdays we clean the house."),
    verb("guidare", "to drive", ["transport"], pp="guidato",
         example="Guidi tu o guido io?", example_en="Are you driving, or shall I?"),
    verb("viaggiare", "to travel", ["travel"], pp="viaggiato",
         example="Mi piace viaggiare da sola.", example_en="I like travelling on my own."),
    verb("portare", "to bring, to carry; to wear", [], pp="portato",
         example="Porto io il vino stasera.", example_en="I'll bring the wine tonight."),
    verb("provare", "to try; to try on", ["shopping"], pp="provato",
         example="Posso provare questa giacca?", example_en="Can I try this jacket on?"),
    verb("lasciare", "to leave (something, someone); to let", [], pp="lasciato",
         example="Lasciami in pace!", example_en="Leave me alone!"),
]

PHRASES = phrases(
    """
ci vuole... | it takes... (time, things needed) | Per Roma ci vuole un'ora di treno. | It takes an hour by train to Rome. | there wants | It agrees with what is needed: ci vogliono due ore.
ci penso io | I'll take care of it | Non ti preoccupare, ci penso io. | Don't worry, I'll take care of it. | I think about it
non ne ho idea | I've no idea | Dov'è Marco? Non ne ho idea. | Where's Marco? I've no idea. | I don't have an idea of it
me ne vado | I'm off, I'm leaving | È tardi, me ne vado. | It's late, I'm off. | I take myself away from here
non ce la faccio più | I can't take it any more | Basta, non ce la faccio più! | That's it, I can't take any more! | I can't make it there any more
ci sto | I'm in, count me in | Una pizza stasera? Ci sto! | Pizza tonight? I'm in! | I stay there
ti va? | do you fancy it? | Ti va un gelato? | Do you fancy an ice cream? | does it go to you? | With a verb: ti va di uscire?
ti voglio bene | I love you (family, friends) | Ti voglio bene, mamma. | I love you, Mum. | I want good for you | Ti amo is for a partner.
lo prendo | I'll take it | Mi piace, lo prendo. | I like it, I'll take it. | I take it
mi dica | can I help you? (polite) | Buongiorno, mi dica. | Good morning, what can I get you? | tell me | What shop staff say to the next customer.
dimmi | tell me; yes? | Dimmi, che cosa è successo? | Tell me, what happened? | | The informal command di' (say) with mi, the m doubled.
figurati | don't mention it; not at all | Grazie mille! — Figurati! | Thanks so much! — Don't mention it! | imagine (it) | To someone you call Lei: si figuri.
fa bello | the weather's nice | Oggi fa bello, usciamo? | It's nice out today, shall we go out? | it makes beautiful
fa freddo | it's cold | In inverno fa freddo a Milano. | It's cold in Milan in winter. | it makes cold
piove | it's raining | Piove da stamattina. | It's been raining since this morning.
sto per... | I'm about to... | Sto per uscire, ti chiamo dopo. | I'm about to go out, I'll call you later. | I stay for
vorrei... | I'd like... | Vorrei un caffè, per favore. | I'd like a coffee, please. | I would want | The polite way to ask for anything; voglio sounds blunt.
dipende | it depends | Vieni domani? Dipende dal tempo. | Are you coming tomorrow? It depends on the weather.
nessun problema | no problem | Nessun problema, ci vediamo dopo. | No problem, see you later.
forse | maybe, perhaps | Forse vengo anch'io. | Maybe I'll come too.
ho mal di testa | I've got a headache | Ho mal di testa, vado a letto. | I've got a headache, I'm going to bed. | I have pain of head | Also mal di gola (sore throat), mal di denti (toothache).
volentieri | gladly, I'd love to | Un caffè? Volentieri! | A coffee? I'd love one!
meno male | thank goodness | Meno male che sei arrivato! | Thank goodness you're here! | less bad
avere bisogno di | to need | Ho bisogno di un po' di riposo. | I need a bit of rest. | to have need of
avere voglia di | to feel like | Non ho voglia di cucinare stasera. | I don't feel like cooking tonight. | to have desire of
fare la fila | to queue | Abbiamo fatto la fila per un'ora. | We queued for an hour. | to make the line
fare la spesa | to do the food shopping | Il sabato facciamo la spesa. | We do the shopping on Saturdays. | to make the expense
dai! | come on! | Dai, andiamo, è tardi! | Come on, let's go, it's late! | give! | Also to cheer someone on.
""",
    ["expressions"],
)

CONNECTIVES = connectors(
    "connective",
    """
allora | so, then | conn-consequence | Piove, allora restiamo a casa. | It's raining, so we're staying in.
di conseguenza | consequently | conn-consequence | Il treno è in ritardo; di conseguenza arriveremo a mezzogiorno. | The train is late; consequently we'll arrive at noon.
tuttavia | however | conn-contrast | È un buon lavoro; tuttavia lo stipendio è basso. | It's a good job; however, the pay is low.
invece | instead; on the other hand | conn-contrast | Io bevo il vino, mio marito invece preferisce la birra. | I drink wine; my husband, on the other hand, prefers beer. | Io bevo il vino, invece mio marito preferisce la birra.
in più | on top of that | conn-addition | È in ritardo, e in più ha dimenticato le chiavi. | He's late, and on top of that he's forgotten the keys.
infine | finally, lastly | conn-sequence | Infine, vorrei ringraziare tutti. | Finally, I'd like to thank everyone.
alla fine | in the end | conn-sequence | Alla fine abbiamo deciso di restare. | In the end we decided to stay.
""",
    ["connettivi"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
siccome | since, as (at the start of a sentence) | conj-subordinating | Siccome è tardi, prendiamo un taxi. | As it's late, let's take a taxi.
mentre | while | conj-subordinating | Lui cucina mentre io lavoro. | He cooks while I work. | Mentre io lavoro, lui cucina.
oppure | or (else) | conj-coordinating | Andiamo al cinema oppure restiamo a casa? | Shall we go to the cinema or stay in?
finché | until; as long as | conj-subordinating | Aspetto finché non arrivi. | I'll wait until you arrive.
""",
    ["congiunzioni"],
)

ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# Each grammar page's Unit carries the words that use it: the verbs with an
# irregular participle, the essere verbs, the reflexives, the verbs with an
# irregular or respelled future, the pronoun phrases, the adjectives people
# compare, the weather phrases that describe the past in the imperfetto, and
# the nouns that break the gender rule. Adjectives of feeling and of state,
# and the countryside, get Units of their own.
UNITS = [
    {
        "title": "Il passato prossimo",
        "page_id": "it-passato-prossimo",
        "word_ids": ["aprire", "chiudere", "chiedere", "rispondere", "perdere", "piangere", "correre"],
    },
    {
        "title": "Essere o avere",
        "page_id": "it-essere-verbs",
        "word_ids": [
            "tornare",
            "entrare",
            "cadere",
            "salire",
            "scendere",
            "diventare",
            "nascere",
            "morire",
            "rimanere",
            "succedere",
        ],
    },
    {
        "title": "L'imperfetto",
        "page_id": "it-imperfetto",
        "word_ids": ["credere", "conoscere", "vivere", "piove", "fa-bello", "fa-freddo"],
    },
    {
        "title": "I verbi riflessivi",
        "page_id": "it-reflexive-verbs",
        "word_ids": ["alzarsi", "svegliarsi", "vestirsi", "lavarsi", "sentirsi", "divertirsi", "sedersi"],
    },
    {
        "title": "I pronomi oggetto",
        "page_id": "it-object-pronouns",
        "word_ids": ["ti-va", "ti-voglio-bene", "lo-prendo", "mi-dica", "dimmi", "figurati"],
    },
    {
        "title": "Ci e ne",
        "page_id": "it-ci-ne",
        "word_ids": ["ci-vuole", "ci-penso-io", "non-ne-ho-idea", "me-ne-vado", "non-ce-la-faccio-piu", "ci-sto"],
    },
    {
        "title": "Il futuro",
        "page_id": "it-futuro",
        "word_ids": ["ricevere", "mandare", "pagare", "dimenticare", "tenere", "pulire"],
    },
    {
        "title": "I paragoni",
        "page_id": "it-comparisons",
        "word_ids": ["lungo", "corto", "alto", "basso", "pesante", "leggero", "veloce", "lento"],
    },
    {
        "title": "Da, fa, per",
        "page_id": "it-time-expressions",
        "word_ids": ["esame", "lezione", "riunione", "appuntamento", "infine", "alla-fine"],
    },
    {
        "title": "Maschile o femminile",
        "page_id": "it-gender-patterns",
        "word_ids": ["cinema", "foto", "sport", "autobus", "computer", "studente", "professore"],
    },
    {
        "title": "Stare + gerundio",
        "page_id": "it-stare-gerund",
        "word_ids": ["sto-per", "guidare", "viaggiare", "portare", "provare", "lasciare"],
    },
    {
        "title": "Carattere e umore",
        "word_ids": ["felice", "triste", "arrabbiato", "divertente", "serio", "timido", "pigro", "sportivo"],
    },
    {
        "title": "Com'è?",
        "word_ids": [
            "malato",
            "occupato",
            "libero",
            "pronto",
            "pieno",
            "vuoto",
            "pulito",
            "sporco",
            "primo",
            "ultimo",
        ],
    },
    {
        "title": "In campagna",
        "word_ids": ["fiore", "bosco", "fiume", "lago", "campagna", "uccello", "cavallo", "mucca", "maiale"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "home": "La casa",
    "transport": "I trasporti",
}

PACK = pack(
    "it-everyday-v1",
    2,
    "it",
    "Italiano · Ogni giorno (A2)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Pratica"),
)
