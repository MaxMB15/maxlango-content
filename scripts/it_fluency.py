"""it-fluency-v1: B1. Mood (congiuntivo, condizionale), complex sentences, register,
and the idioms and false friends that separate textbook Italian from real Italian."""

from common import build_units, interleave, page, pack, topic, topic_labels
from it_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("relativi", "Pronomi relativi", "relative pronouns", ["pronomi"]),
    topic("registro", "Registro", "register: formal, spoken, slang", []),
    topic("falsi-amici", "Falsi amici", "false friends", []),
    topic("idioms", "Modi di dire", "idioms", []),
    topic("society", "Società", "society and ideas", ["articoli"]),
    topic("si-impersonale", "Si impersonale", "si: one, people, you in general", ["presente"]),
]

PAGES = [
    page(
        "it-congiuntivo",
        "The congiuntivo",
        r"""
The **congiuntivo** (subjunctive) is a mood, not a tense. It marks a clause as an opinion, a wish, a fear, a doubt or something not yet real. English has traces of it (*I insist that he **be** there*); Italian uses it every day.

It appears almost only after **che**, in a clause whose main verb expresses something other than a plain fact.

## Forming it

-are verbs take **-i**; -ere and -ire verbs take **-a**. The three singular forms are the same, so Italians often keep the subject pronoun: *che io parli*, *che tu parli*.

| | parlare | vendere | dormire | finire |
| --- | --- | --- | --- | --- |
| che io | parli | venda | dorma | finisca |
| che tu | parli | venda | dorma | finisca |
| che lui / lei | parli | venda | dorma | finisca |
| che noi | parliamo | vendiamo | dormiamo | finiamo |
| che voi | parliate | vendiate | dormiate | finiate |
| che loro | parlino | vendano | dormano | finiscano |

Most irregular verbs build it on the io form of the present: *faccio → faccia*, *vado → vada*, *vengo → venga*, *posso → possa*, *voglio → voglia*, *dico → dica*, *esco → esca*. Six are irregular throughout:

| | essere | avere | sapere | dare | stare | dovere |
| --- | --- | --- | --- | --- | --- | --- |
| che io, tu, lui | sia | abbia | sappia | dia | stia | debba |
| che noi | siamo | abbiamo | sappiamo | diamo | stiamo | dobbiamo |
| che voi | siate | abbiate | sappiate | diate | stiate | dobbiate |
| che loro | siano | abbiano | sappiano | diano | stiano | debbano |

## What triggers it

| Trigger | Examples |
| --- | --- |
| Opinion, belief | penso che, credo che, mi sembra che, immagino che |
| Wanting, hoping | voglio che, spero che, preferisco che |
| Feeling | sono contento che, ho paura che, mi dispiace che |
| Doubt | dubito che, non sono sicuro che |
| Impersonal phrases | è importante che, bisogna che, è meglio che, è possibile che |
| Some conjunctions | benché, sebbene, affinché, prima che, a meno che, purché |

Unlike French, Italian uses it after **penso che**, **credo che** and **spero che** even in positive sentences: an opinion is not a fact.

:::examples
- Penso che Marco abbia ragione. — I think Marco is right.
- Voglio che tu venga con me. — I want you to come with me.
- È importante che tutti siano d'accordo. — It's important that everyone agrees.
- Ho paura che sia troppo tardi. — I'm afraid it's too late.
:::

## What doesn't trigger it

- Certainty takes the indicative: *So che hai ragione*, *Sono sicuro che viene*, *È vero che è tardi*.
- If both clauses have the same subject, use **di** and an infinitive: *Penso di avere ragione* (not *penso che io abbia*), *Spero di vederti presto*. *Volere* takes the infinitive directly: *Voglio venire*.
- In relaxed speech many people use the indicative after *penso che*. The congiuntivo is never wrong there, and in writing it's expected.

:::cloze{sentence="Spero che tu ___ bene." blank="stia"}
:::
""",
        ["congiuntivo"],
        "it-congiuntivo",
        explains=["congiuntivo"],
    ),
    page(
        "it-condizionale",
        "The condizionale and se clauses",
        r"""
The **condizionale** is *would*. It uses the same stem as the future, with its own endings: **-ei, -esti, -ebbe, -emmo, -este, -ebbero**.

| | parlare | essere | volere |
| --- | --- | --- | --- |
| io | parlerei | sarei | vorrei |
| tu | parleresti | saresti | vorresti |
| lui / lei | parlerebbe | sarebbe | vorrebbe |
| noi | parleremmo | saremmo | vorremmo |
| voi | parlereste | sareste | vorreste |
| loro | parlerebbero | sarebbero | vorrebbero |

Every irregular future stem carries over: *avrei, andrei, potrei, dovrei, saprei, verrei, farei, starei*. Listen for the double **m** in the noi form: *parleremmo* (we would speak) against the future *parleremo* (we will speak).

## Politeness and advice

The condizionale softens requests and advice, the way *could*, *would* and *should* do in English:

:::examples
- Vorrei un bicchiere di vino rosso. — I'd like a glass of red wine.
- Potrebbe aiutarmi? — Could you help me?
- Dovresti riposarti un po'. — You should rest a bit.
- Mi piacerebbe vivere al mare. — I'd love to live by the sea.
:::

## Se clauses

Italian pairs the tenses in *if* sentences, and the rule English speakers break is this: **no condizionale after se**.

| Situation | se + | main clause | Example |
| --- | --- | --- | --- |
| Real, likely | presente | presente or futuro | Se piove, resto a casa. |
| Imagined | congiuntivo imperfetto | condizionale | Se avessi tempo, viaggerei di più. |
| Too late now | congiuntivo trapassato | condizionale passato | Se l'avessi saputo, sarei venuto. |

*Se sarei ricco* is a famous mistake, even among Italians. It's *se fossi ricco*.

The **congiuntivo imperfetto** is easy to form: the imperfetto stem plus **-ssi, -ssi, -sse, -ssimo, -ste, -ssero**: *parlassi*, *avessi*, *dormissi*. *Essere* gives *fossi, fosse, fossimo, foste, fossero*; *fare*, *dire*, *stare* and *dare* give *facessi*, *dicessi*, *stessi*, *dessi*.

## Reported news

Newspapers use the condizionale for facts they can't confirm: *Secondo i giornali, il ministro sarebbe in ospedale* (According to the papers, the minister is reportedly in hospital).

:::cloze{sentence="Se fossi in te, ___ più attento." blank="starei"}
:::
""",
        ["condizionale"],
        "it-condizionale",
        explains=["condizionale"],
    ),
    page(
        "it-relative-pronouns",
        "Che, cui and il quale",
        r"""
Relative pronouns join two sentences about the same thing. English can often leave them out (*the book I'm reading*); Italian never can: *il libro che sto leggendo*.

| Pronoun | Use | Example |
| --- | --- | --- |
| che | the subject or the direct object | La ragazza che parla è mia sorella. |
| cui | after a preposition | La città in cui abito. L'amico a cui ho scritto. |
| il cui, la cui | whose | Il ragazzo la cui madre fa il medico. |
| il quale, la quale, i quali, le quali | a formal che or cui | La signora, la quale mi ha spiegato tutto. |
| dove | a place | Il paese dove sono nato. |

## Che or cui?

**Che** never follows a preposition. As soon as there's one, it's **cui**: *la persona con cui lavoro* (the person I work with), *il motivo per cui ti chiamo* (the reason I'm calling you). English puts the preposition at the end; Italian puts it first.

## Whose

In *il cui*, *la cui*, *i cui* and *le cui*, the article agrees with the thing owned, not the owner: *il ragazzo **la** cui madre...* (the boy whose mother...).

## Il quale

**Il quale** agrees with the noun it stands for, and joins prepositions like a noun: *della quale*, *ai quali*. It's formal, and it helps when *che* would be unclear about who is meant.

## Quello che and chi

Without a noun to refer back to, say **quello che** or **ciò che** (what, the thing that): *Fai quello che vuoi* (Do what you like), *Ciò che conta è la salute* (What matters is your health).

**Chi** means "whoever, those who", with a singular verb: *Chi cerca trova* (Seek and you shall find).

## In cui for time

*Il giorno in cui ci siamo conosciuti* (the day we met). English says *when* or nothing; Italian says *in cui*.

:::cloze{sentence="Questa è la casa in ___ sono cresciuto." blank="cui"}
:::
""",
        ["relativi"],
        "it-relative-pronouns",
        explains=["relativi"],
    ),
    page(
        "it-register",
        "Tu, Lei and spoken Italian",
        r"""
Italian marks politeness in its grammar, and spoken Italian takes shortcuts the textbook leaves out.

## Tu or Lei?

**Tu** is for friends, family, children, and anyone young enough to be a classmate. **Lei** (she, but here *you*, with a third-person verb) is for strangers, shop staff, older people and colleagues until they suggest otherwise: *Lei è di qui?* (Are you from here?). Written in a letter, it often takes a capital L.

Switching is a small ritual: *Diamoci del tu!* (Let's say tu to each other). In the plural, **voi** covers both.

## What speech shortens

| Written | Spoken | |
| --- | --- | --- |
| Che cosa vuoi? | Cosa vuoi? Che vuoi? | che cosa shrinks |
| Hai fame? | C'hai fame? | ci + avere, never written formally |
| Non lo so. | Boh. | with a shrug |
| Non è difficile. | Non è mica difficile. | mica adds "you know" |
| Mangio una pizza. | Mi mangio una pizza. | an extra pronoun adds relish |

## Everyday informal words

| Informal | Standard | English |
| --- | --- | --- |
| un sacco di | molto, tanti | loads of |
| figo, una figata | bello, una cosa bella | cool |
| un casino | una gran confusione | a mess; a racket |
| beccare | trovare, sorprendere | to catch, to bump into |
| fregarsene | non importare | not to care: chi se ne frega? |
| mitico | fantastico | legendary, brilliant |
| sfigato | sfortunato | unlucky; a loser |
| un tipo, una tipa | un uomo, una donna | a guy, a girl |

## Accents and dialects

Every region has its own accent and words, and many Italians speak a dialect at home. A Milanese and a Neapolitan may struggle with each other's dialect, but standard Italian, the language of this course, is understood everywhere.

Use the slang with friends, not in a job interview.
""",
        ["registro"],
        "it-register",
        explains=["registro"],
    ),
    page(
        "it-false-friends",
        "False friends",
        r"""
Italian and English share thousands of Latin words, and most mean the same thing. These don't. Each one has tripped up generations of learners.

| Italian | Means | Not |
| --- | --- | --- |
| attualmente | currently | actually (*in realtà*) |
| eventualmente | if need be, possibly | eventually (*alla fine*) |
| finalmente | at last | finally, in a list (*infine*) |
| la libreria | bookshop; bookcase | library (*la biblioteca*) |
| la camera | room, bedroom | camera (*la macchina fotografica*) |
| il parente | relative | parent (*il genitore*) |
| la fattoria | farm | factory (*la fabbrica*) |
| il magazzino | warehouse, storeroom | magazine (*la rivista*) |
| sensibile | sensitive | sensible (*ragionevole*) |
| largo | wide; loose | large (*grande*) |
| educato | polite | educated (*istruito*) |
| morbido | soft | morbid (*morboso*) |
| annoiato | bored | annoyed (*seccato*) |
| fastidioso | annoying | fastidious (*pignolo*) |
| pretendere | to demand, to expect | to pretend (*fingere*) |
| il rumore | noise | rumour (*la voce*) |
| l'argomento | topic | argument (*la lite*) |
| i confetti | sugared almonds | confetti (*i coriandoli*) |
| il preservativo | condom | preservative (*il conservante*) |

*Grandi magazzini* are department stores, and *una camera doppia* is a double room in a hotel.
""",
        ["falsi-amici"],
        "it-false-friends",
        explains=["falsi-amici"],
    ),
    page(
        "it-idioms",
        "How Italian idioms work",
        r"""
Idioms are phrases whose meaning isn't the sum of their words. Italian idioms lean on food, animals and the body, and many have an English cousin with a different picture.

| Italian | Literally | Meaning |
| --- | --- | --- |
| in bocca al lupo | into the wolf's mouth | good luck |
| piove a catinelle | it's raining by the basinful | it's pouring |
| costare un occhio della testa | to cost an eye from your head | to cost an arm and a leg |
| essere al verde | to be at the green | to be broke |
| dormire come un ghiro | to sleep like a dormouse | to sleep like a log |

*In bocca al lupo* has a fixed reply: **crepi!** (may it die, meaning the wolf), never *grazie*.

Idioms in this pack are drilled like any other phrase: the card shows the Italian, you recall the meaning. Each one keeps its literal translation, because the picture is usually what makes it stick.

The verb inside an idiom changes like any verb: *costa un occhio della testa*, *sono al verde*, *ho dormito come un ghiro*.

Use them sparingly at first. One well-placed idiom sounds natural; five in a row sound like a phrasebook.
""",
        ["idioms"],
        "it-idioms",
        explains=["idioms"],
    ),
    page(
        "it-passato-remoto",
        "Trapassato prossimo and passato remoto",
        r"""
Two more past tenses complete the picture.

## Trapassato prossimo: had done

The past before the past. Use the **imperfetto** of avere or essere with the participle, just like English *had* with a participle.

:::examples
- Avevo già mangiato quando è arrivato Paolo. — I had already eaten when Paolo arrived.
- Quando siamo arrivati, il treno era già partito. — When we got there, the train had already left.
:::

The same verbs take essere as in the passato prossimo, with the same agreement: *Anna era già uscita*.

## Passato remoto: recognise it

The **passato remoto** is the past of history books, novels and fairy tales. In much of the south people also use it in speech, for events that feel closed and distant. You'll meet it mostly in the third person.

| Infinitive | lui / lei | loro |
| --- | --- | --- |
| parlare | parlò | parlarono |
| vendere | vendé, vendette | venderono, vendettero |
| dormire | dormì | dormirono |
| essere | fu | furono |
| avere | ebbe | ebbero |
| fare | fece | fecero |
| dire | disse | dissero |
| venire | venne | vennero |
| vedere | vide | videro |
| nascere | nacque | nacquero |
| prendere | prese | presero |

*Dante nacque a Firenze nel 1265* (Dante was born in Florence in 1265). In a story, the imperfetto still sets the scene and the passato remoto moves it on: *C'era una volta un re che aveva tre figlie. Un giorno la più giovane partì.*
""",
        ["passato-prossimo", "registro"],
        "it-passato-remoto",
    ),
    page(
        "it-nuance-conjunctions",
        "Although, even if, because",
        r"""
Italian has several words where English has one, and each comes with its own grammar.

## Although and even if

- **Benché** and **sebbene** take the congiuntivo: *Benché non abbia fame, mangio qualcosa.*
- **Anche se** takes the ordinary indicative: *Anche se non ho fame, mangio qualcosa.* Same meaning, simpler grammar, and the everyday choice in speech.
- **Nonostante** takes the congiuntivo, or simply a noun: *Nonostante la pioggia, siamo usciti.*

## Because

| Word | Use | Example |
| --- | --- | --- |
| perché | answers "why?", neutral | Resto a casa perché ho la febbre. |
| siccome | starts the sentence | Siccome è domenica, i negozi sono chiusi. |
| dato che, visto che | given that, since | Visto che ci sei, apri la finestra. |
| poiché | written | Poiché il treno era in ritardo, abbiamo preso un taxi. |
| grazie a | thanks to (a good cause) | Grazie a te, ho trovato lavoro. |
| a causa di | because of (a bad cause) | A causa dello sciopero, la scuola è chiusa. |

*Perché* with the congiuntivo means "so that", like *affinché*: *Te lo ripeto perché tu lo sappia* (I'm telling you again so that you know).

## Before, unless, as long as

All three take the congiuntivo:

- **prima che**: *Partiamo prima che arrivi il temporale.* With the same subject, say **prima di** and an infinitive: *Mi lavo le mani prima di mangiare.*
- **a meno che (non)**: *Usciamo, a meno che tu non sia stanco.* The *non* here is no negation; it's just part of the phrase.
- **purché**: *Va bene, purché sia l'ultima volta.*

## As soon as

**Appena** takes the indicative. For a future event, careful Italian puts both verbs in the future: *Appena avrò i risultati, ti scriverò.* In speech the present is just as common: *Appena ho i risultati, ti scrivo.*

:::cloze{sentence="Ti presto la macchina, purché tu ___ attento." blank="sia"}
:::
""",
        ["congiunzioni", "congiuntivo"],
        "it-nuance-conjunctions",
        explains=["congiunzioni"],
    ),
    page(
        "it-si-impersonale",
        "Si: one, people, you",
        r"""
English says *you*, *people*, *they* or *one* when it means people in general. Italian uses **si** with a third-person verb.

:::examples
- In questo ristorante si mangia benissimo. — You eat really well in this restaurant.
- Come si dice "fork" in italiano? — How do you say "fork" in Italian?
- Qui non si fuma. — No smoking here.
:::

## Singular or plural?

With a plural noun, the verb goes plural: *Si vende la casa* (The house is for sale), but *Si vendono case* (Houses for sale). On signs, *si* is often glued to the end: *Affittasi* (To let), *Vendesi* (For sale).

## Some things that look odd

- An adjective after *si è* is plural, because it describes people in general: *Quando si è giovani, si ha tanta energia* (When you're young, you have lots of energy).
- A reflexive verb can't have two *si* in a row, so the first becomes **ci**: *Ci si alza presto in campagna* (People get up early in the country).
- In the passato prossimo it takes essere: *Si è mangiato bene* (We ate well).
- *Si dice che...* means "they say that...": *Si dice che il nuovo sindaco sia molto giovane.*

In Tuscany, *si* even stands in for *noi*: *Noi si va al mare* (We're going to the seaside). You'll hear it in Florence; you don't need to copy it.

:::cloze{sentence="In questo negozio si ___ anche libri usati." blank="vendono"}
:::
""",
        ["si-impersonale"],
        "it-si-impersonale",
        explains=["si-impersonale"],
    ),
]

NOUNS = nouns(
    """
# society and ideas
società | f | society; company | society | società | La società italiana sta cambiando. | Italian society is changing.
governo | m | government | society | governi | Il governo ha approvato la nuova legge. | The government has passed the new law.
legge | f | law | society | leggi | La legge è uguale per tutti. | The law is the same for everyone.
diritto | m | right; law (the subject) | society | diritti | Tutti hanno diritto all'istruzione. | Everyone has the right to an education.
libertà | f | freedom | society | libertà | La libertà di stampa è fondamentale. | Freedom of the press is essential.
uguaglianza | f | equality | society | uguaglianze | Lottiamo per l'uguaglianza tra uomini e donne. | We're fighting for equality between men and women.
elezione | f | election | society | elezioni | Le elezioni sono a maggio. | The elections are in May.
guerra | f | war | society | guerre | Mio nonno ha fatto la guerra. | My grandfather fought in the war.
pace | f | peace | society | | Tutti vogliono vivere in pace. | Everyone wants to live in peace.
ambiente | m | environment; atmosphere | society | ambienti | Dobbiamo proteggere l'ambiente. | We have to protect the environment.
inquinamento | m | pollution | society | | L'inquinamento in città è un problema serio. | Pollution in the city is a serious problem.
futuro | m | future | society | | Nessuno sa che cosa ci riserva il futuro. | Nobody knows what the future holds.
passato | m | past | society | | Non pensare troppo al passato. | Don't dwell on the past.
storia | f | history; story | society | storie | Mi piace molto la storia romana. | I really like Roman history.
cultura | f | culture | society | culture | La cultura italiana è famosa in tutto il mondo. | Italian culture is famous all over the world.
lingua | f | language; tongue | society | lingue | Quante lingue parli? | How many languages do you speak?
problema | m | problem | society | problemi | Abbiamo un piccolo problema. | We have a small problem.
soluzione | f | solution | society | soluzioni | Troveremo una soluzione insieme. | We'll find a solution together.
ragione | f | reason; (avere ragione) to be right | society | ragioni | Hai ragione tu, scusa. | You're right, sorry.
opinione | f | opinion | society | opinioni | Rispetto la tua opinione. | I respect your opinion.
idea | f | idea | society | idee | Che bella idea! | What a lovely idea!
scelta | f | choice | society | scelte | È stata una scelta difficile. | It was a difficult choice.
fortuna | f | luck; fortune | society | fortune | Abbiamo avuto fortuna con il tempo. | We were lucky with the weather.
successo | m | success; hit | society | successi | Il concerto è stato un grande successo. | The concert was a big success.
fallimento | m | failure; bankruptcy | society | fallimenti | Il progetto è stato un fallimento. | The project was a failure.
# feelings
paura | f | fear | feelings | paure | Ho paura dei cani. | I'm scared of dogs.
gioia | f | joy | feelings | gioie | Che gioia rivederti! | What a joy to see you again!
rabbia | f | anger | feelings | | Ha urlato per la rabbia. | He shouted in anger.
vergogna | f | shame; embarrassment | feelings | | Che vergogna, ho dimenticato il suo nome! | How embarrassing, I've forgotten her name!
ricordo | m | memory (something remembered) | feelings | ricordi | Ho tanti bei ricordi di quell'estate. | I have lots of happy memories of that summer.
memoria | f | memory (the faculty) | feelings | memorie | Ho una pessima memoria per i nomi. | I have a terrible memory for names.
sogno | m | dream | feelings | sogni | Il mio sogno è vivere in Toscana. | My dream is to live in Tuscany.
speranza | f | hope | feelings | speranze | Non perdere la speranza. | Don't lose hope.
amore | m | love | feelings | amori | L'amore non ha età. | Love knows no age.
amicizia | f | friendship | feelings | amicizie | La nostra amicizia dura da vent'anni. | Our friendship has lasted twenty years.
nostalgia | f | nostalgia; homesickness | feelings | | Ho nostalgia di casa. | I'm homesick.
# untranslatables and false friends
campanilismo | m | loyalty to your own town above all (from campanile, bell tower) | idioms | | Il campanilismo in Italia è fortissimo. | Local pride is very strong in Italy.
menefreghismo | m | a couldn't-care-less attitude | idioms | | Il suo menefreghismo mi fa arrabbiare. | His couldn't-care-less attitude makes me angry.
passeggiata | f | stroll; the evening walk through town | idioms | passeggiate | Dopo cena facciamo una passeggiata in centro. | After dinner we go for a stroll in the centre.
aperitivo | m | early-evening drink with snacks | idioms | aperitivi | Ci vediamo per un aperitivo alle sette? | Shall we meet for an aperitivo at seven?
camera | f | room, bedroom | falsi-amici | camere | La mia camera è al primo piano. | My bedroom is on the first floor.
parente | m | relative | falsi-amici | parenti | A Natale vengono tutti i parenti. | All the relatives come at Christmas.
fattoria | f | farm | falsi-amici | fattorie | I bambini hanno visitato una fattoria. | The children visited a farm.
libreria | f | bookshop; bookcase | falsi-amici | librerie | Ho comprato questo libro in libreria. | I bought this book at the bookshop.
magazzino | m | warehouse, storeroom | falsi-amici | magazzini | La merce è ancora in magazzino. | The goods are still in the warehouse.
biblioteca | f | library | falsi-amici | biblioteche | Studio in biblioteca tutti i pomeriggi. | I study in the library every afternoon.
"""
)

ADJECTIVES = adjectives(
    """
attuale, attuale, attuali, attuali | current, present-day | La situazione attuale è difficile. | The current situation is difficult.
eventuale, eventuale, eventuali, eventuali | possible (should it happen) | Ci scusiamo per eventuali ritardi. | We apologise for any delays.
sensibile, sensibile, sensibili, sensibili | sensitive | È una ragazza molto sensibile. | She's a very sensitive girl.
largo, larga, larghi, larghe | wide; loose | Questi pantaloni sono troppo larghi. | These trousers are too loose.
educato, educata, educati, educate | polite, well-mannered | Tuo figlio è molto educato. | Your son is very polite.
morbido, morbida, morbidi, morbide | soft | Questo cuscino è morbidissimo. | This pillow is really soft.
""",
    ["falsi-amici"],
) + adjectives(
    """
solo, sola, soli, sole | alone; only | Vivo da solo da due anni. | I've lived alone for two years.
importante, importante, importanti, importanti | important | È importante dormire bene. | It's important to sleep well.
necessario, necessaria, necessari, necessarie | necessary | Non è necessario prenotare. | There's no need to book.
possibile, possibile, possibili, possibili | possible | È possibile pagare con la carta? | Can I pay by card?
preoccupato, preoccupata, preoccupati, preoccupate | worried | Sono preoccupata per mia madre. | I'm worried about my mother.
orgoglioso, orgogliosa, orgogliosi, orgogliose | proud | Sono orgoglioso di te. | I'm proud of you.
geloso, gelosa, gelosi, gelose | jealous | Il mio ragazzo è molto geloso. | My boyfriend is very jealous.
generoso, generosa, generosi, generose | generous | Grazie, sei troppo generoso. | Thanks, you're too generous.
stupido, stupida, stupidi, stupide | stupid, silly | Che domanda stupida! | What a stupid question!
furbo, furba, furbi, furbe | crafty, cunning; clever | Marco è furbo, trova sempre una soluzione. | Marco is crafty, he always finds a way.
dolce, dolce, dolci, dolci | sweet; gentle | Questo vino è troppo dolce. | This wine is too sweet.
fresco, fresca, freschi, fresche | fresh; cool | Il pesce oggi è freschissimo. | The fish is really fresh today.
falso, falsa, falsi, false | false; fake | Questa borsa è falsa. | This bag is a fake.
distrutto, distrutta, distrutti, distrutte | shattered, exhausted (informal); destroyed | Dopo il trasloco ero distrutto. | After the move I was shattered.
"""
)

VERBS = [
    # Reflexive: all take essere.
    verb("ricordarsi", "to remember", ["feelings"], pp="ricordato",
         example="Ti ricordi di me?", example_en="Do you remember me?"),
    verb("occuparsi", "to take care of, to deal with", [], pp="occupato",
         example="Mi occupo io dei bambini.", example_en="I'll look after the children."),
    verb("sbagliarsi", "to be wrong, to make a mistake", [], pp="sbagliato",
         example="Scusi, mi sono sbagliato.", example_en="Sorry, my mistake."),
    verb("preoccuparsi", "to worry", ["feelings"], pp="preoccupato",
         example="Non preoccuparti, va tutto bene.", example_en="Don't worry, everything's fine."),
    verb("lamentarsi", "to complain", [], pp="lamentato",
         example="Si lamenta sempre del tempo.", example_en="He's always complaining about the weather."),
    # The rest.
    verb("riuscire", "to manage, to succeed", [], aux="essere", pp="riuscito",
         present="riesco riesci riesce riusciamo riuscite riescono",
         subj="riesca riesca riesca riusciamo riusciate riescano",
         example="Non riesco a dormire.", example_en="I can't get to sleep."),
    verb("riflettere", "to think it over, to reflect", [], pp="riflettuto",
         example="Ci devo riflettere un po'.", example_en="I need to think it over."),
    verb("crescere", "to grow, to grow up", [], aux="essere", pp="cresciuto",
         example="Sono cresciuta in un piccolo paese.", example_en="I grew up in a small village."),
    verb("ottenere", "to get, to obtain", [], pp="ottenuto",
         present="ottengo ottieni ottiene otteniamo ottenete ottengono", fut="otterr",
         subj="ottenga ottenga ottenga otteniamo otteniate ottengano",
         example="Ha ottenuto il permesso di soggiorno.", example_en="He got his residence permit."),
    verb("permettere", "to allow, to let", [], pp="permesso",
         example="I miei genitori non me lo permettono.", example_en="My parents won't let me."),
    verb("promettere", "to promise", [], pp="promesso",
         example="Ti prometto che torno presto.", example_en="I promise I'll be back soon."),
    verb("costruire", "to build", [], pp="costruito", isc=True,
         example="Hanno costruito un nuovo ponte.", example_en="They've built a new bridge."),
    verb("temere", "to fear, to be afraid", ["feelings"], pp="temuto",
         example="Temo che sia troppo tardi.", example_en="I'm afraid it's too late."),
    verb("ridere", "to laugh", [], pp="riso",
         example="Mi fai sempre ridere.", example_en="You always make me laugh."),
    verb("sorridere", "to smile", [], pp="sorriso",
         example="Sorride sempre a tutti.", example_en="She always smiles at everyone."),
    verb("mentire", "to lie (tell lies)", [], pp="mentito",
         example="Non mentire, ti conosco!", example_en="Don't lie, I know you!"),
    verb("servire", "to serve; (mi serve) to need", [], pp="servito",
         example="Mi serve una mano.", example_en="I need a hand."),
    verb("sparire", "to disappear", [], aux="essere", pp="sparito", isc=True,
         example="Dove sono sparite le mie chiavi?", example_en="Where have my keys got to?"),
    verb("buttare", "to throw; to throw away", [], pp="buttato",
         example="Non buttare la carta per terra!", example_en="Don't throw paper on the ground!"),
    verb("sperare", "to hope", [], pp="sperato",
         example="Spero di vederti presto.", example_en="I hope to see you soon."),
    verb("proporre", "to suggest, to propose", [], pp="proposto",
         present="propongo proponi propone proponiamo proponete propongono", imp="propone", fut="proporr",
         subj="proponga proponga proponga proponiamo proponiate propongano",
         example="Propongo di andare al mare.", example_en="I suggest we go to the seaside."),
    verb("seguire", "to follow", [], pp="seguito",
         example="Mi segua, prego.", example_en="Follow me, please."),
    verb("scegliere", "to choose", [], pp="scelto",
         present="scelgo scegli sceglie scegliamo scegliete scelgono",
         subj="scelga scelga scelga scegliamo scegliate scelgano",
         example="Scegli tu il ristorante.", example_en="You choose the restaurant."),
]

IDIOMS = phrases(
    """
in bocca al lupo | good luck! | In bocca al lupo per l'esame! | Good luck with the exam! | into the wolf's mouth | The reply is crepi! (may it die), never grazie.
avere le mani bucate | to spend money like water | Marco ha le mani bucate, non risparmia mai. | Marco spends money like water, he never saves. | to have hands with holes in
costare un occhio della testa | to cost an arm and a leg | Quella macchina costa un occhio della testa. | That car costs an arm and a leg. | to cost an eye from your head
piove a catinelle | it's pouring | Prendi l'ombrello, piove a catinelle! | Take an umbrella, it's pouring! | it's raining by the basinful
non vedo l'ora | I can't wait | Non vedo l'ora di partire! | I can't wait to leave! | I don't see the hour | With a verb: non vedo l'ora di + infinitive.
essere al verde | to be broke | Non posso uscire, sono al verde. | I can't go out, I'm broke. | to be at the green
prendere in giro | to make fun of, to tease | Smettila di prendermi in giro! | Stop making fun of me! | to take around
acqua in bocca | mum's the word | Acqua in bocca, è una sorpresa! | Mum's the word, it's a surprise! | water in the mouth
essere in gamba | to be capable, to be on the ball | La tua collega è davvero in gamba. | Your colleague is really capable. | to be in leg
fare quattro chiacchiere | to have a chat | Passa da me, facciamo quattro chiacchiere. | Drop by, we'll have a chat. | to make four chats
non avere peli sulla lingua | to speak your mind | Mia nonna non ha peli sulla lingua. | My grandmother doesn't mince her words. | to have no hairs on your tongue
cadere dalle nuvole | to be taken aback | Quando gliel'ho detto, è caduto dalle nuvole. | When I told him, he was completely taken aback. | to fall from the clouds
rompere le scatole | to get on someone's nerves | Mio fratello mi rompe sempre le scatole. | My brother is always getting on my nerves. | to break the boxes | A polite stand-in for a much ruder phrase.
ogni morte di papa | once in a blue moon | Mi telefona ogni morte di papa. | He phones me once in a blue moon. | every time a pope dies
essere una buona forchetta | to love your food | Mio zio è una buona forchetta. | My uncle loves his food. | to be a good fork
andare a gonfie vele | to go swimmingly | Il nuovo lavoro va a gonfie vele. | The new job is going swimmingly. | to go with swollen sails
fare una figuraccia | to make a fool of yourself | Ho fatto una figuraccia davanti al capo. | I made a fool of myself in front of the boss. | to make an ugly figure
fare bella figura | to make a good impression | Vuole fare bella figura con i suoceri. | He wants to make a good impression on his in-laws. | to make a beautiful figure | Making a good impression, la bella figura, matters a lot in Italy.
tagliare la corda | to make a run for it | Quando è arrivata la polizia, hanno tagliato la corda. | When the police arrived, they made a run for it. | to cut the rope
l'abito non fa il monaco | don't judge a book by its cover | Sembra severo, ma l'abito non fa il monaco. | He looks strict, but don't judge a book by its cover. | the habit doesn't make the monk
meglio tardi che mai | better late than never | Sei arrivato! Meglio tardi che mai. | You made it! Better late than never.
dormire come un ghiro | to sleep like a log | Stanotte ho dormito come un ghiro. | Last night I slept like a log. | to sleep like a dormouse
alzare il gomito | to have a drop too much | Ieri sera Luca ha alzato un po' il gomito. | Luca had a few too many last night. | to raise the elbow
fare il ponte | to take the day off between a holiday and the weekend | Giovedì è festa, venerdì facciamo il ponte. | Thursday's a holiday, so we're taking Friday off too. | to make the bridge
chi dorme non piglia pesci | the early bird catches the worm | Alzati, chi dorme non piglia pesci! | Get up, the early bird catches the worm! | whoever sleeps catches no fish
avere la testa fra le nuvole | to have your head in the clouds | Scusa, oggi ho la testa fra le nuvole. | Sorry, my head's in the clouds today. | to have your head among the clouds
essere al settimo cielo | to be over the moon | Da quando ha trovato lavoro è al settimo cielo. | Since she found a job she's been over the moon. | to be in the seventh heaven
stare con le mani in mano | to sit around doing nothing | Non stare con le mani in mano, aiutami! | Don't just sit there, help me! | to stay with your hands in your hands
avere un diavolo per capello | to be in a foul mood | Oggi il capo ha un diavolo per capello. | The boss is in a foul mood today. | to have a devil for each hair
non tutte le ciambelle riescono col buco | things don't always turn out as planned | Pazienza, non tutte le ciambelle riescono col buco. | Never mind, you can't win them all. | not every ring doughnut comes out with a hole
avere la coda di paglia | to have a guilty conscience | Perché ti arrabbi? Hai la coda di paglia? | Why are you getting angry? Guilty conscience? | to have a straw tail | A straw tail catches fire easily: whoever has one is quick to feel accused.
campa cavallo che l'erba cresce | don't hold your breath | Riparare la strada? Campa cavallo che l'erba cresce! | Fix the road? Don't hold your breath! | live on, horse, the grass is growing
essere nato con la camicia | to be born lucky | Vince sempre, è nato con la camicia. | He always wins, he was born lucky. | to be born with a shirt on
essere come il prezzemolo | to turn up everywhere | Quel ragazzo è come il prezzemolo, è a ogni festa. | That guy turns up everywhere, he's at every party. | to be like parsley
""",
    ["idioms"],
)

EXPRESSIONS = phrases(
    """
boh | dunno (with a shrug) | Dov'è Marco? Boh, non l'ho visto. | Where's Marco? Dunno, I haven't seen him.
mica | not at all, hardly (with non) | Non è mica facile! | It's not that easy, you know! | crumb | Mica male! means "not bad at all".
magari | maybe; if only! | Ti piacerebbe vivere a Roma? Magari! | Would you like to live in Rome? If only!
insomma | in short; well; so-so | Il film? Insomma, non mi è piaciuto molto. | The film? Well, I didn't like it much. | in sum
tipo | like, sort of (filler) | C'erano tipo cento persone. | There were like a hundred people. | type
un sacco | loads, a lot | Mi piace un sacco questa città. | I love this city. | a sack | With a noun: un sacco di soldi (loads of money).
ci mancherebbe | of course; don't mention it | Grazie dell'aiuto! — Ci mancherebbe! | Thanks for the help! — Don't mention it! | that would be missing
che figata! | how cool! | Hai preso i biglietti? Che figata! | You got the tickets? How cool!
non ci posso credere | I can't believe it | Abbiamo vinto? Non ci posso credere! | We won? I can't believe it!
vabbè | oh well, OK then | Vabbè, non importa. | Oh well, it doesn't matter. | | Short for va bene.
che schifo! | yuck!, how disgusting! | Che schifo, questo caffè è freddo! | Yuck, this coffee is cold!
tanto | anyway (so it makes no difference) | Non preoccuparti, tanto non lo sa nessuno. | Don't worry, nobody knows anyway. | so much
a proposito | by the way | A proposito, hai sentito Giulia? | By the way, have you heard from Giulia? | to the purpose
per carità | heaven forbid; please, don't | Un altro caffè? Per carità, ne ho già bevuti tre! | Another coffee? Good heavens no, I've already had three! | for charity
non mi va | I don't feel like it | Stasera non mi va di uscire. | I don't feel like going out tonight. | it doesn't go to me
mi raccomando | please make sure; don't forget | Chiamami quando arrivi, mi raccomando! | Call me when you get there, won't you! | I commend myself
ci vediamo | see you | Ci vediamo domani alle otto. | See you tomorrow at eight. | we see each other
ecco | here it is; there you go | Ecco il tuo caffè. | Here's your coffee.
beh | well... | Beh, tu che ne pensi? | Well, what do you think?
non fa niente | never mind, it doesn't matter | Ho dimenticato il libro. — Non fa niente. | I've forgotten the book. — Never mind. | it does nothing
che ne so | how should I know? | Dov'è andato? Che ne so io! | Where's he gone? How should I know! | what do I know of it
""",
    ["expressions"],
)
for e in EXPRESSIONS:
    if e["primary_form"] in {"boh", "mica", "tipo", "un sacco", "che figata!", "vabbè", "che ne so"}:
        e["tags"].append("registro")

CONNECTIVES = connectors(
    "connective",
    """
comunque | anyway; all the same | conn-contrast | Non mi piace molto, comunque lo compro. | I don't like it much; I'll buy it anyway.
anzi | on the contrary; or rather | conn-contrast | Non sono stanco, anzi, ho voglia di ballare. | I'm not tired; on the contrary, I feel like dancing.
in realtà | actually, in reality | conn-contrast | Sembra facile, ma in realtà è difficilissimo. | It looks easy, but actually it's really hard.
del resto | after all, besides | conn-addition | Non preoccuparti, del resto non è colpa tua. | Don't worry; after all, it's not your fault.
per di più | what's more | conn-addition | La casa è piccola e per di più è cara. | The house is small, and what's more it's expensive.
perciò | so, therefore | conn-consequence | Ho perso il treno, perciò sono arrivato tardi. | I missed the train, so I arrived late.
così | so, that way | conn-consequence | Parto presto, così evito il traffico. | I'm leaving early; that way I'll avoid the traffic.
in effetti | indeed, as a matter of fact | conn-cause | Sei stanco? In effetti ho dormito poco stanotte. | You're tired? Well, I did sleep badly last night.
finalmente | at last | conn-sequence | Dopo tre ore di viaggio, finalmente siamo arrivati. | After three hours on the road, we're here at last.
""",
    ["connettivi"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
sebbene | although (+ congiuntivo) | conj-subordinating | Sebbene sia stanco, continuo a lavorare. | Although I'm tired, I'm carrying on working.
affinché | so that (+ congiuntivo) | conj-subordinating | Parlo piano affinché tutti capiscano. | I speak slowly so that everyone understands.
prima che | before (+ congiuntivo) | conj-subordinating | Torniamo a casa prima che faccia buio. | Let's go home before it gets dark.
a meno che | unless (+ congiuntivo) | conj-subordinating | Vengo, a meno che non piova. | I'll come, unless it rains.
purché | as long as (+ congiuntivo) | conj-subordinating | Puoi uscire, purché torni entro mezzanotte. | You can go out, as long as you're back by midnight.
nonostante | although, despite (+ congiuntivo) | conj-subordinating | Nonostante piova, andiamo a fare una passeggiata. | Although it's raining, we're going for a walk.
anche se | even if, even though | conj-subordinating | Anche se è tardi, ti aspetto. | Even though it's late, I'll wait for you.
dato che | since, given that | conj-subordinating | Dato che sei qui, mi aiuti a cucinare? | Since you're here, will you help me cook?
appena | as soon as | conj-subordinating | Ti chiamo appena arrivo. | I'll call you as soon as I arrive.
""",
    ["congiunzioni"],
)

ITEMS = PAGES + interleave(IDIOMS, EXPRESSIONS, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# it-idioms and it-false-friends anchor on the pools their tag already names;
# the rest of the idioms become automatic "Modi di dire" Units via LABELS.
# it-nuance-conjunctions takes every congiunzioni-tagged item, the family the
# page teaches. The mood pages (congiuntivo, condizionale) and the relatives
# have no vocabulary of their own, so they draw verbs that suit them: the
# verbs of hoping and fearing that trigger the congiuntivo, and so on.
# it-si-impersonale takes the reflexives, which turn into "ci si", and the
# reciprocal "ci vediamo". Adjectives share one first tag, so they get Units
# of their own.
UNITS = [
    {
        "title": "Il congiuntivo",
        "page_id": "it-congiuntivo",
        "word_ids": ["sperare", "temere", "paura", "riuscire", "crescere", "mentire", "servire"],
    },
    {
        "title": "Il condizionale",
        "page_id": "it-condizionale",
        "word_ids": ["sparire", "buttare", "seguire", "ridere", "sorridere", "scegliere"],
    },
    {
        "title": "I pronomi relativi",
        "page_id": "it-relative-pronouns",
        "word_ids": ["riflettere", "ottenere", "permettere", "promettere", "costruire", "proporre"],
    },
    {
        "title": "Registro informale",
        "page_id": "it-register",
        "word_ids": ["boh", "mica", "tipo", "un-sacco", "che-figata", "vabbe", "che-ne-so"],
    },
    {
        "title": "Falsi amici",
        "page_id": "it-false-friends",
        "word_ids": ["camera", "parente", "fattoria", "libreria", "magazzino", "biblioteca"],
    },
    {
        "title": "Modi di dire",
        "page_id": "it-idioms",
        "word_ids": [
            "in-bocca-al-lupo",
            "avere-le-mani-bucate",
            "costare-un-occhio-della-testa",
            "piove-a-catinelle",
            "non-vedo-l-ora",
            "essere-al-verde",
            "prendere-in-giro",
            "dormire-come-un-ghiro",
        ],
    },
    {
        "title": "Il passato remoto",
        "page_id": "it-passato-remoto",
        "word_ids": ["passato", "storia", "futuro", "guerra", "pace", "cultura"],
    },
    {
        "title": "Benché, anche se, perché",
        "page_id": "it-nuance-conjunctions",
        "word_ids": [
            "sebbene",
            "affinche",
            "prima-che",
            "a-meno-che",
            "purche",
            "nonostante",
            "anche-se",
            "dato-che",
            "appena",
        ],
    },
    {
        "title": "Si impersonale",
        "page_id": "it-si-impersonale",
        "word_ids": ["ricordarsi", "occuparsi", "sbagliarsi", "preoccuparsi", "lamentarsi", "ci-vediamo"],
    },
    {
        "title": "Aggettivi ingannevoli",
        "word_ids": ["attuale", "eventuale", "sensibile", "largo", "educato", "morbido"],
    },
    {
        "title": "Come sei?",
        "word_ids": ["solo", "preoccupato", "orgoglioso", "geloso", "generoso", "stupido", "furbo"],
    },
    {
        "title": "Com'è?",
        "word_ids": ["importante", "necessario", "possibile", "dolce", "fresco", "falso", "distrutto"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "feelings": "Sentimenti",
    "expressions": "Espressioni",
}

PACK = pack(
    "it-fluency-v1",
    1,
    "it",
    "Italiano · Scioltezza (B1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Pratica"),
)
