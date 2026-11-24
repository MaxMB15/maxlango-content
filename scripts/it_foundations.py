"""it-foundations-v1: A1. The grammar that blocks a beginner first, and the words
needed to talk about yourself, your family, your day and your food."""

from common import build_units, interleave, page, pack, topic, topic_labels
from it_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("pronuncia", "Pronuncia", "pronunciation", []),
    topic("pronomi", "Pronomi", "pronouns", ["presente"]),
    topic("domande", "Domande", "asking questions", ["presente"]),
    topic("preposizioni", "Preposizioni articolate", "prepositions joined to the article", ["articoli"]),
    topic("numeri", "Numeri", "numbers", []),
    topic("family", "Famiglia", "family", ["articoli"]),
    topic("body", "Corpo", "body", ["articoli"]),
    topic("city", "Città", "city and places", ["articoli"]),
    topic("greetings", "Saluti", "greetings and politeness", []),
    topic("colors", "Colori", "colours", ["aggettivi"]),
]

PAGES = [
    page(
        "it-pronunciation",
        "Reading Italian aloud",
        r"""
Italian is spelled almost exactly as it sounds. Learn a handful of rules and you can read any word aloud. The vowels are always pure: *a, e, i, o, u* never glide the way English vowels do, and a final vowel is always pronounced.

## Double consonants

A double consonant is held longer, with a tiny pause before it, and it changes the meaning: *[pala](lango:say)* (shovel) and *[palla](lango:say)* (ball), *[caro](lango:say)* (dear) and *[carro](lango:say)* (cart), *[sete](lango:say)* (thirst) and *[sette](lango:say)* (seven), *[nono](lango:say)* (ninth) and *[nonno](lango:say)* (grandfather). English speakers tend to skip the difference. Italians hear it at once.

## C and g

| Spelling | Sound | Example |
| --- | --- | --- |
| ca, co, cu, chi, che | "k" | *[casa](lango:say)*, *[chi](lango:say)* |
| ci, ce, cia, cio, ciu | "ch" as in church | *[cena](lango:say)*, *[ciao](lango:say)* |
| ga, go, gu, ghi, ghe | "g" as in go | *[gatto](lango:say)*, *[spaghetti](lango:say)* |
| gi, ge, gia, gio, giu | "j" as in jam | *[gelato](lango:say)*, *[giorno](lango:say)* |

The **h** is what keeps c and g hard before i and e: *[chiave](lango:say)*, *[funghi](lango:say)*. The i in *cia*, *cio* and *giu* is usually silent, just a sign that the c or g is soft: *[ciao](lango:say)* sounds like "chow".

## Gli, gn and sc

- **gli** is like the "lli" in "million": *[figlio](lango:say)*, *[famiglia](lango:say)*, *[aglio](lango:say)*.
- **gn** is like the "ny" in "canyon": *[bagno](lango:say)*, *[signora](lango:say)*, *[gnocchi](lango:say)*.
- **sc** before i or e is "sh": *[pesce](lango:say)*, *[uscire](lango:say)*. Before a, o, u, or with an h, it is "sk": *[scuola](lango:say)*, *[schiena](lango:say)*.

## Stress

Most words are stressed on the second-to-last syllable: *[amico](lango:say)*, *[parlare](lango:say)*. A written accent marks a stressed final vowel: *[città](lango:say)*, *[perché](lango:say)*, *[caffè](lango:say)*. Many words put the stress further back with nothing to warn you: *[macchina](lango:say)*, *[telefono](lango:say)*. The -ano of a verb is never stressed: *[parlano](lango:say)*, *[lavorano](lango:say)*.

Accents also tell short words apart: *[e](lango:say)* (and) and *[è](lango:say)* (is), *[si](lango:say)* (oneself) and *[sì](lango:say)* (yes), *[la](lango:say)* (the) and *[là](lango:say)* (there).

## H and r

**H** is always silent: *[ho](lango:say)* sounds like *o*. The **r** is a quick tap of the tongue, rolled longer when it's double: *[Roma](lango:say)*, *[birra](lango:say)*.

:::examples
- Ciao, come ti chiami? — Hi, what's your name?
- Mio figlio ha sette anni. — My son is seven.
- Il bagno è in fondo a destra. — The bathroom is at the end on the right.
:::
""",
        ["pronuncia"],
        "it-pronunciation",
        explains=["pronuncia"],
    ),
    page(
        "it-subject-pronouns",
        "Io, tu and Lei",
        r"""
An Italian verb ending already says who is doing the action, so the subject pronoun is usually left out: *Parlo italiano* (I speak Italian), *Siamo stanchi* (We're tired).

| Person | Pronoun | English |
| --- | --- | --- |
| 1st singular | io | I |
| 2nd singular | tu | you (one person, familiar) |
| 3rd singular | lui / lei | he / she |
| polite | Lei | you (one person, formal) |
| 1st plural | noi | we |
| 2nd plural | voi | you (several people) |
| 3rd plural | loro | they |

## When to say it

Add the pronoun only for emphasis or contrast: *Io lavoro e tu dormi!* (I'm working and you're asleep!), *Paga lui* (He's paying). Saying *io* in every sentence sounds pushy, and it's one of the surest signs of a beginner.

## Tu or Lei?

Use **tu** with friends, family, children and people your own age in relaxed settings. Use **Lei** with strangers, shop staff, colleagues you don't know well, and anyone older or senior. When in doubt, say *Lei*.

**Lei** is the word for "she", used as a polite "you", and it takes the same verb form: *Come sta?* (How are you? to someone you call Lei) against *Come stai?* (to a friend). Moving to *tu* is usually offered: *Possiamo darci del tu?* (Shall we say tu?)

To several people, say **voi**, friends or not: *Voi di dove siete?* (Where are you all from?)

## Loro and "it"

*Loro* is the same for men, women and mixed groups. There's no everyday word for "it" as a subject; it's simply left out: *È bello* (It's beautiful), *Piove* (It's raining).

:::examples
- Tu parli italiano? — Do you speak Italian? (to a friend)
- Lei parla italiano? — Do you speak Italian? (polite)
- Voi siete pronti? — Are you all ready?
:::
""",
        ["pronomi"],
        "it-subject-pronouns",
        explains=["pronomi"],
    ),
    page(
        "it-essere-avere",
        "Essere, avere and c'è",
        r"""
**Essere** (to be) and **avere** (to have) are the two most important verbs in Italian. Both are irregular, and both are also the helper verbs of the past tense, so you'll use them constantly.

| | essere | avere |
| --- | --- | --- |
| io | sono | ho |
| tu | sei | hai |
| lui / lei / Lei | è | ha |
| noi | siamo | abbiamo |
| voi | siete | avete |
| loro | sono | hanno |

The h of *ho*, *hai*, *ha* and *hanno* is silent. It's only there to tell *ho* (I have) from *o* (or), and *ha* (has) from *a* (to).

## Where Italian says "have" and English says "be"

| Italian | Literally | English |
| --- | --- | --- |
| ho fame | I have hunger | I'm hungry |
| ho sete | I have thirst | I'm thirsty |
| ho caldo / freddo | I have heat / cold | I'm hot / cold |
| ho sonno | I have sleep | I'm sleepy |
| ho paura | I have fear | I'm scared |
| ho ragione / torto | I have reason / wrong | I'm right / wrong |
| ho vent'anni | I have twenty years | I'm twenty |
| ho bisogno di... | I have need of | I need... |

Saying *sono vent'anni* for your age is the classic beginner mistake. It means nothing.

## C'è and ci sono

"There is" is **c'è** and "there are" is **ci sono**: *C'è un bar qui vicino?* (Is there a café near here?), *In frigo ci sono le uova* (There are eggs in the fridge).

Don't drop the *ci*. *È un problema* means "It's a problem"; *C'è un problema* means "There's a problem".

:::examples
- Sono di Milano, e tu? — I'm from Milan, and you?
- Abbiamo una casa al mare. — We have a house by the sea.
- Ci sono due bagni nell'appartamento. — There are two bathrooms in the flat.
:::

:::cloze{sentence="Ho ___, mangiamo?" blank="fame"}
:::
""",
        ["presente"],
        "it-essere-avere",
    ),
    page(
        "it-present-tense",
        "The present tense: -are, -ere, -ire",
        r"""
Italian verbs fall into three groups by the ending of the infinitive. Learn the regular patterns and you can conjugate thousands of verbs.

| | parlare | vendere | dormire | finire |
| --- | --- | --- | --- | --- |
| io | parlo | vendo | dormo | finisco |
| tu | parli | vendi | dormi | finisci |
| lui / lei | parla | vende | dorme | finisce |
| noi | parliamo | vendiamo | dormiamo | finiamo |
| voi | parlate | vendete | dormite | finite |
| loro | parlano | vendono | dormono | finiscono |

## -are verbs (parlare)

The biggest group, and nearly every new verb joins it. Remove **-are** and add **-o, -i, -a, -iamo, -ate, -ano**.

## -ere verbs (vendere)

Remove **-ere** and add **-o, -i, -e, -iamo, -ete, -ono**.

## -ire verbs (dormire and finire)

Two kinds. A few, like *dormire*, *partire* and *aprire*, take **-o, -i, -e, -iamo, -ite, -ono**. Most, like *finire*, *capire* and *preferire*, slip **-isc-** in front of the ending in every form except noi and voi: *capisco*, *capisci*, but *capiamo*. Learn which kind each -ire verb is.

Whatever the group, the noi form ends in **-iamo** and the io form in **-o**.

:::examples
- Parlo italiano e inglese. — I speak Italian and English.
- Finiamo alle sei. — We finish at six.
- Vende la sua macchina. — He's selling his car.
- Mangi con noi stasera? — Are you eating with us tonight?
:::

## Spelling changes that keep the sound

- Verbs in **-care** and **-gare** add an h before an i, so the c and g stay hard: *cercare*, *tu cerchi*, *noi cerchiamo*; *pagare*, *tu paghi*.
- Verbs in **-ciare**, **-giare** and **-iare** never write two i's: *mangiare*, *tu mangi*, *noi mangiamo*; *studiare*, *tu studi*.

## One tense for three English ones

*Mangio* is "I eat", "I'm eating" and "I do eat". It also covers plans: *Domani parto* (I'm leaving tomorrow). To stress that something is going on at this very moment, Italian uses *stare* and the gerund: *Sto mangiando* (I'm eating right now).

:::predict{prompt="tu (giocare)" answer="giochi"}
:::
""",
        ["presente"],
        "it-present-tense",
        explains=["presente"],
    ),
    page(
        "it-negation",
        "Saying no: non",
        r"""
Italian negation is simple: put **non** right before the verb.

:::examples
- Non parlo tedesco. — I don't speak German.
- Marco non è qui. — Marco isn't here.
- Non mangiamo carne. — We don't eat meat.
:::

There's no "do" to add. Small object pronouns stay glued to the verb, so *non* goes in front of them: *Non lo so* (I don't know it), *Non mi piace* (I don't like it).

## Double negatives are correct

The other negative words go after the verb, and **non** stays before it. Two negatives make a negative, not a positive.

| Negation | Meaning | Example |
| --- | --- | --- |
| non ... mai | never | Non bevo mai il caffè. |
| non ... più | no longer, not any more | Non abita più qui. |
| non ... niente | nothing | Non vedo niente. |
| non ... nessuno | nobody | Non conosco nessuno. |
| non ... ancora | not yet | Non è ancora pronto. |
| non ... neanche | not even | Non ho neanche un euro. |

When the negative word comes first, there's no *non*: *Nessuno lo sa* (Nobody knows), *Niente è impossibile* (Nothing is impossible).

## No or non?

**No** is the answer to a question: *Vieni? — No.* **Non** negates a verb. *No, non vengo* uses both.

## Nessun before a noun

Before a noun, *nessuno* changes like *uno* and stays singular: *nessun problema* (no problem), *nessuna idea* (no idea).

:::cloze{sentence="Non vado ___ in palestra." blank="mai"}
:::
""",
        ["negazione"],
        "it-negation",
        explains=["negazione"],
    ),
    page(
        "it-questions",
        "Asking questions",
        r"""
An Italian yes/no question uses exactly the same words as the statement. Only your voice changes: it rises at the end.

- *Parli italiano.* (You speak Italian.)
- *Parli italiano?* (Do you speak Italian?)

There's no "do", and no swapping of subject and verb. If you name the subject, it often goes to the end: *È arrivato Marco?* (Has Marco arrived?)

## Question words

| Word | Meaning |
| --- | --- |
| chi | who |
| che cosa, cosa, che | what |
| dove | where |
| quando | when |
| come | how |
| perché | why |
| quanto, quanta, quanti, quante | how much, how many |
| quale, quali | which, what |

After a question word the verb comes next, and the subject after it: *Dove abita tua sorella?* (Where does your sister live?) *Dove* and *come* lose their final vowel before *è*: *Dov'è?*, *Com'è?*

## Quanto and quale agree

*Quanto* agrees with the noun it counts: *quanto tempo*, *quanta pasta*, *quanti anni*, *quante persone*. *Quale* has one form for both genders, *quali* in the plural, and before *è* it shortens to **qual** with no apostrophe: *Qual è il tuo numero?* Writing *qual'è* is a mistake even Italians make.

## Prepositions come first

A preposition can't be left at the end as in English. It goes before the question word: *Di dove sei?* (Where are you from?), *Con chi esci?* (Who are you going out with?)

:::examples
- Dove abiti? — Where do you live?
- Come ti chiami? — What's your name?
- Che ore sono? — What time is it?
- Perché piangi? — Why are you crying?
:::
""",
        ["domande"],
        "it-questions",
        explains=["domande"],
    ),
    page(
        "it-articulated-prepositions",
        "Al, del, nel, sul, dal",
        r"""
Five everyday prepositions merge with the definite article that follows them: **a** (to, at), **di** (of), **da** (from, at someone's place), **in** (in, into) and **su** (on).

| | il | lo | l' | la | i | gli | le |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a | al | allo | all' | alla | ai | agli | alle |
| di | del | dello | dell' | della | dei | degli | delle |
| da | dal | dallo | dall' | dalla | dai | dagli | dalle |
| in | nel | nello | nell' | nella | nei | negli | nelle |
| su | sul | sullo | sull' | sulla | sui | sugli | sulle |

The pattern is regular once you see it: *di* turns into **de-** and *in* into **ne-**, and the forms with lo, la, l', gli and le double the l.

:::examples
- Vado al cinema stasera. — I'm going to the cinema tonight.
- Il libro è sul tavolo. — The book is on the table.
- Le chiavi sono nella borsa. — The keys are in the bag.
- Torno dall'ufficio alle sei. — I get back from the office at six.
- È la macchina dei vicini. — It's the neighbours' car.
:::

## A or in?

Cities take **a**: *a Roma*, *a Milano*. Countries, regions and large islands take **in**, without an article: *in Italia*, *in Toscana*, *in Sicilia*. Many places around town also take a bare *in*: *in banca*, *in ufficio*, *in centro*, *in piazza*, *in cucina*. Others take *al*: *al bar*, *al mare*, *al ristorante*. Learn them in pairs, as Italians do.

## Da: from, and at someone's place

*Da* means "from": *Vengo da Napoli*. With a person it means "at the home or shop of": *Vado da Maria* (I'm going to Maria's), *dal medico* (to the doctor's).

## Del: "some"

*Di* plus the article also means "some": *del pane* (some bread), *dell'acqua* (some water), *degli amici* (some friends). It's optional, and Italians often leave it out: *Compro pane e latte.*

:::cloze{sentence="Domani vado ___ stazione in autobus." blank="alla"}
:::
""",
        ["preposizioni"],
        "it-articulated-prepositions",
        explains=["preposizioni"],
    ),
    page(
        "it-adjectives",
        "Adjectives: agreement and position",
        r"""
Italian adjectives agree with their noun in gender and number, and most go **after** the noun.

## Two families

| | singular | plural |
| --- | --- | --- |
| -o adjectives, masculine | rosso | rossi |
| -o adjectives, feminine | rossa | rosse |
| -e adjectives, both genders | grande | grandi |

*Un libro rosso, una casa rossa, due libri rossi, due case rosse.* An adjective in -e has only two forms: *un cane grande*, *una casa grande*, *due case grandi*.

A few never change, mostly colours named after things: *blu*, *rosa*, *viola*. *Una macchina blu*, *due macchine blu*.

A group of masculine and feminine nouns together takes the masculine plural: *Marco e Anna sono stanchi.*

Adjectives in -co and -go keep the hard sound in the feminine plural, *bianche*, *lunghe*, and usually in the masculine too, *bianchi*, *lunghi*. Some soften instead, like the nouns: *simpatico*, *simpatici*.

## Position

Most adjectives follow the noun, always so for colours, nationalities and shapes: *una macchina rossa*, *un ragazzo italiano*. A few short, common ones usually go before it: *bello*, *buono*, *brutto*, *piccolo*, *grande*, *nuovo*, *vecchio*. *Una bella giornata*, *un piccolo problema*.

## Bello and buono

Before a noun, **bello** changes the way the article does: *un bel ragazzo* (like *il*), *un bello zaino* (like *lo*), *un bell'albero* (like *l'*), *dei bei fiori* (like *i*). **Buono** shortens to **buon** before most masculine nouns, the way *uno* becomes *un*: *un buon amico*, *buon viaggio*.

:::examples
- Ho comprato una macchina rossa. — I bought a red car.
- È un piccolo paese di montagna. — It's a small mountain village.
- Queste scarpe sono troppo care. — These shoes are too expensive.
- Abbiamo visto una bella casa antica. — We saw a beautiful old house.
:::

## Meaning changes with position

A few adjectives mean something different before and after the noun:

- *un caro amico* (a dear friend) / *un ristorante caro* (an expensive restaurant)
- *un grande uomo* (a great man) / *un uomo grande* (a big man)
- *un vecchio amico* (a friend of many years) / *un amico vecchio* (an elderly friend)
- *diversi libri* (several books) / *libri diversi* (different books)
""",
        ["aggettivi"],
        "it-adjectives",
        explains=["aggettivi"],
    ),
    page(
        "it-numbers",
        "Numbers and the time",
        r"""
| | | | |
| --- | --- | --- | --- |
| 1 uno | 6 sei | 11 undici | 16 sedici |
| 2 due | 7 sette | 12 dodici | 17 diciassette |
| 3 tre | 8 otto | 13 tredici | 18 diciotto |
| 4 quattro | 9 nove | 14 quattordici | 19 diciannove |
| 5 cinque | 10 dieci | 15 quindici | 20 venti |

Tens: 30 trenta, 40 quaranta, 50 cinquanta, 60 sessanta, 70 settanta, 80 ottanta, 90 novanta. 100 is *cento*.

## Joining tens and units

Each number is written as one word: 23 *ventitré*, 45 *quarantacinque*, 67 *sessantasette*. Two small rules:

- A ten drops its last vowel before *uno* and *otto*, the two that start with a vowel: 21 *ventuno*, 28 *ventotto*, 31 *trentuno*, 48 *quarantotto*.
- *Tre* at the end of a longer number takes an accent: *ventitré*, *trentatré*.

1000 is *mille*, but 2000 is *duemila*, and the year 2026 is *duemilaventisei*. A million is *un milione*.

## Telling the time

Ask *Che ore sono?* or *Che ora è?* Hours are plural, so the answer is **sono le** and the hour: *Sono le tre* (It's three o'clock). One o'clock, noon and midnight are singular: *È l'una*, *È mezzogiorno*, *È mezzanotte*.

Minutes follow with **e** (past) or **meno** (to): *le tre e dieci* (ten past three), *le quattro meno un quarto* (a quarter to four), *le sette e mezza* (half past seven). "At" a time is **alle**: *alle otto*, but *all'una*. Timetables use the 24-hour clock: *alle diciotto*.

:::examples
- Ho ventotto anni. — I'm twenty-eight.
- Sono le sette e mezza. — It's half past seven.
- Il treno parte all'una. — The train leaves at one.
- Costa trentatré euro. — It costs thirty-three euros.
:::
""",
        ["numeri"],
        "it-numbers",
        explains=["numeri"],
    ),
    page(
        "it-possessives",
        "La mia casa, but mia madre",
        r"""
An Italian possessive agrees with the **thing owned**, not with the owner, and it usually comes with the article: *la mia casa*, *il mio libro*. *Suo* and *sua* both mean "his", "her" and the polite "your". The noun that follows decides which one.

| Owner | masc. sg | fem. sg | masc. pl | fem. pl |
| --- | --- | --- | --- | --- |
| io | il mio | la mia | i miei | le mie |
| tu | il tuo | la tua | i tuoi | le tue |
| lui / lei / Lei | il suo | la sua | i suoi | le sue |
| noi | il nostro | la nostra | i nostri | le nostre |
| voi | il vostro | la vostra | i vostri | le vostre |
| loro | il loro | la loro | i loro | le loro |

*Loro* never changes.

:::examples
- Marco ama sua madre. — Marco loves his mother.
- Anna ama suo padre. — Anna loves her father.
- È la loro casa. — It's their house.
:::

## No article with family

With a singular family noun on its own, the article disappears: *mia madre*, *tuo fratello*, *suo marito*. It comes back:

- in the plural: *i miei fratelli*, *le mie zie*;
- with *loro*: *la loro madre*;
- when an adjective or an ending is added: *la mia sorella maggiore*, *il mio fratellino*;
- usually with the pet names *mamma* and *papà*: *la mia mamma*.

## I miei

*I miei* on its own means "my parents": *Vado dai miei a Natale* (I'm going to my parents' for Christmas).

:::cloze{sentence="___ sorella abita a Milano." blank="Mia"}
:::
""",
        ["pronomi"],
        "it-possessives",
    ),
    page(
        "it-piacere",
        "Mi piace: liking things",
        r"""
Italian has no verb that works like "to like". It says that something **pleases** someone: *Mi piace il caffè* is literally "coffee pleases me". The thing you like is the subject of the verb, and the person who likes it comes first as a small pronoun.

| Italian | Literally | English |
| --- | --- | --- |
| mi piace | pleases me | I like |
| ti piace | pleases you | you like |
| gli piace | pleases him | he likes |
| le piace | pleases her | she likes |
| Le piace | pleases you (polite) | you like |
| ci piace | pleases us | we like |
| vi piace | pleases you all | you like |
| gli piace | pleases them | they like |

## Piace or piacciono?

The verb agrees with the thing liked, not with the person who likes it. One thing, or any activity, takes **piace**. Several things take **piacciono**.

- *Mi piace la pizza.* (I like pizza.)
- *Mi piacciono le fragole.* (I like strawberries.)
- *Mi piace leggere.* (I like reading.)

## With a name

With a name or a noun, use **a**: *A Marco piace il calcio* (Marco likes football). For emphasis there are stressed forms with *a* too: *A me piace, e a te?* "Me too" is **anche a me**, and "me neither" **neanche a me**. Answering *anch'io* here is the classic mistake.

## Mi dispiace

*Non mi piace* means "I don't like it". *Mi dispiace* is something else: it means "I'm sorry".

:::examples
- Mi piace molto questa città. — I really like this city.
- Ci piacciono i film italiani. — We like Italian films.
- A mia madre piace cucinare. — My mother likes cooking.
:::

:::cloze{sentence="Ti ___ i gatti?" blank="piacciono"}
:::
""",
        ["presente"],
        "it-piacere",
    ),
]

NOUNS = nouns(
    """
# family
padre | m | father | family | padri | Mio padre lavora in banca. | My father works at a bank.
madre | f | mother | family | madri | Mia madre fa il medico. | My mother is a doctor.
fratello | m | brother | family | fratelli | Ho un fratello più grande. | I have an older brother.
sorella | f | sister | family | sorelle | Mia sorella studia a Bologna. | My sister studies in Bologna.
figlio | m | son | family | figli | Hanno un figlio di tre anni. | They have a three-year-old son.
figlia | f | daughter | family | figlie | La loro figlia vive a Londra. | Their daughter lives in London.
marito | m | husband | family | mariti | Suo marito cucina molto bene. | Her husband cooks very well.
moglie | f | wife | family | mogli | Ti presento mia moglie, Giulia. | This is my wife, Giulia.
genitore | m | parent | family | genitori | I miei genitori abitano in campagna. | My parents live in the country.
nonno | m | grandfather | family | nonni | Il nonno racconta sempre storie. | Grandpa is always telling stories.
nonna | f | grandmother | family | nonne | La nonna prepara il ragù la domenica. | Grandma makes ragù on Sundays.
zio | m | uncle | family | zii | Mio zio abita in Sicilia. | My uncle lives in Sicily.
zia | f | aunt | family | zie | Domenica pranziamo dalla zia. | On Sunday we're having lunch at our aunt's.
cugino | m | cousin (male) | family | cugini | Mio cugino ha la mia età. | My cousin is my age.
cugina | f | cousin (female) | family | cugine | Mia cugina si sposa a giugno. | My cousin is getting married in June.
# people
uomo | m | man | people | uomini | Quell'uomo è il mio vicino. | That man is my neighbour.
donna | f | woman | people | donne | Chi è quella donna? | Who is that woman?
ragazzo | m | boy, young man; boyfriend | people | ragazzi | Il ragazzo di Sara è simpatico. | Sara's boyfriend is nice.
ragazza | f | girl, young woman; girlfriend | people | ragazze | Le ragazze giocano a pallavolo. | The girls are playing volleyball.
signora | f | lady; Mrs | people | signore | Buongiorno, signora Rossi! | Good morning, Mrs Rossi!
nome | m | name, first name | people | nomi | Qual è il tuo nome? | What's your name?
cognome | m | surname | people | cognomi | Scriva qui il suo cognome. | Write your surname here.
# body
testa | f | head | body | teste | Mi gira la testa. | My head is spinning.
occhio | m | eye | body | occhi | Ha gli occhi azzurri. | She has blue eyes.
bocca | f | mouth | body | bocche | Non parlare con la bocca piena! | Don't talk with your mouth full!
naso | m | nose | body | nasi | Ho il naso chiuso. | My nose is blocked.
orecchio | m | ear | body | orecchie | Mi fa male l'orecchio. | My ear hurts.
mano | f | hand | body | mani | Lavati le mani prima di mangiare. | Wash your hands before eating.
braccio | m | arm | body | braccia | Porta la borsa sotto il braccio. | She carries her bag under her arm.
gamba | f | leg | body | gambe | Mi fanno male le gambe. | My legs hurt.
piede | m | foot | body | piedi | Andiamo a piedi? | Shall we walk?
dito | m | finger | body | dita | Il bambino conta con le dita. | The child counts on his fingers.
schiena | f | back | body | schiene | Ho mal di schiena. | I've got backache.
cuore | m | heart | body | cuori | Ha un cuore d'oro. | He has a heart of gold.
pancia | f | belly, tummy | body | pance | Il bambino ha mal di pancia. | The child has a tummy ache.
dente | m | tooth | body | denti | Mi lavo i denti dopo cena. | I brush my teeth after dinner.
# food
colazione | f | breakfast | food | colazioni | Faccio colazione alle sette. | I have breakfast at seven.
pranzo | m | lunch | food | pranzi | Il pranzo è pronto! | Lunch is ready!
cena | f | dinner | food | cene | A che ora è la cena? | What time is dinner?
formaggio | m | cheese | food | formaggi | Questo formaggio è molto buono. | This cheese is very good.
carne | f | meat | food | | Non mangio carne. | I don't eat meat.
pesce | m | fish | food | pesci | Il venerdì mangiamo pesce. | On Fridays we eat fish.
pollo | m | chicken | food | polli | Stasera c'è pollo arrosto. | Tonight there's roast chicken.
uovo | m | egg | food | uova | Vorrei due uova, per favore. | I'd like two eggs, please.
latte | m | milk | food | | Prendo il caffè con il latte. | I have my coffee with milk.
caffè | m | coffee; café | food | caffè | Prendiamo un caffè? | Shall we get a coffee?
tè | m | tea | food | tè | Bevo il tè con il limone. | I drink tea with lemon.
vino | m | wine | food | vini | Un bicchiere di vino rosso, per favore. | A glass of red wine, please.
birra | f | beer | food | birre | Due birre piccole, per favore. | Two small beers, please.
mela | f | apple | food | mele | Mangio una mela al giorno. | I eat an apple a day.
patata | f | potato | food | patate | Le patate sono nel forno. | The potatoes are in the oven.
verdura | f | vegetables | food | verdure | Compro la verdura al mercato. | I buy vegetables at the market.
frutta | f | fruit | food | | La frutta è fresca oggi. | The fruit is fresh today.
zucchero | m | sugar | food | | Il caffè senza zucchero, grazie. | Coffee without sugar, thanks.
sale | m | salt | food | | Mi passi il sale? | Can you pass me the salt?
riso | m | rice | food | | Stasera faccio il riso con le verdure. | Tonight I'm making rice with vegetables.
marmellata | f | jam | food | marmellate | Mangio pane e marmellata a colazione. | I have bread and jam for breakfast.
torta | f | cake | food | torte | La torta della nonna è buonissima. | Grandma's cake is delicious.
pasta | f | pasta | food | | La pasta è pronta, a tavola! | The pasta's ready, come and eat!
gelato | m | ice cream | food | gelati | Un gelato al cioccolato, per favore. | A chocolate ice cream, please.
# time
giorno | m | day | time | giorni | Lavoro cinque giorni alla settimana. | I work five days a week.
settimana | f | week | time | settimane | La prossima settimana vado a Roma. | Next week I'm going to Rome.
mese | m | month | time | mesi | Ci vediamo il mese prossimo. | See you next month.
anno | m | year | time | anni | Abito qui da un anno. | I've lived here for a year.
ora | f | hour | time | ore | Il viaggio dura un'ora. | The trip takes an hour.
minuto | m | minute | time | minuti | Arrivo tra cinque minuti. | I'll be there in five minutes.
mattina | f | morning | time | mattine | Esco presto la mattina. | I go out early in the morning.
pomeriggio | m | afternoon | time | pomeriggi | Ci vediamo oggi pomeriggio? | Shall we meet this afternoon?
sera | f | evening | time | sere | La sera guardo la TV. | In the evening I watch TV.
lunedì | m | Monday | time | lunedì | Il lunedì vado in palestra. | On Mondays I go to the gym.
martedì | m | Tuesday | time | martedì | Martedì ho un esame. | I have an exam on Tuesday.
mercoledì | m | Wednesday | time | mercoledì | Il negozio è chiuso il mercoledì. | The shop is closed on Wednesdays.
giovedì | m | Thursday | time | giovedì | Giovedì sera ceniamo fuori. | On Thursday evening we're eating out.
venerdì | m | Friday | time | venerdì | Finalmente è venerdì! | At last it's Friday!
sabato | m | Saturday | time | sabati | Sabato andiamo al mare. | On Saturday we're going to the seaside.
domenica | f | Sunday | time | domeniche | La domenica pranziamo dai nonni. | On Sundays we have lunch at our grandparents'.
# city
città | f | city, town | city | città | Roma è una città bellissima. | Rome is a beautiful city.
strada | f | street, road | city | strade | Attento quando attraversi la strada! | Careful when you cross the road!
piazza | f | square | city | piazze | Ci vediamo in piazza alle otto. | See you in the square at eight.
negozio | m | shop | city | negozi | Il negozio apre alle nove. | The shop opens at nine.
mercato | m | market | city | mercati | Il sabato c'è il mercato. | On Saturdays there's a market.
stazione | f | station | city | stazioni | Scusi, dov'è la stazione? | Excuse me, where's the station?
scuola | f | school | city | scuole | I bambini vanno a scuola a piedi. | The children walk to school.
chiesa | f | church | city | chiese | La chiesa è in centro. | The church is in the centre.
banca | f | bank | city | banche | La banca chiude alle quattro. | The bank closes at four.
ospedale | m | hospital | city | ospedali | L'ospedale è qui vicino. | The hospital is near here.
ristorante | m | restaurant | city | ristoranti | Conosco un buon ristorante. | I know a good restaurant.
bar | m | café, bar | city | bar | Il bar sotto casa fa un ottimo caffè. | The café downstairs makes excellent coffee.
museo | m | museum | city | musei | Il museo è chiuso il lunedì. | The museum is closed on Mondays.
# home
stanza | f | room | home | stanze | La casa ha quattro stanze. | The house has four rooms.
cucina | f | kitchen; cooking | home | cucine | Siamo tutti in cucina. | We're all in the kitchen.
bagno | m | bathroom | home | bagni | Il bagno è in fondo al corridoio. | The bathroom is at the end of the corridor.
soggiorno | m | living room | home | soggiorni | Guardiamo la TV in soggiorno. | We watch TV in the living room.
letto | m | bed | home | letti | Stasera vado a letto presto. | Tonight I'm going to bed early.
chiave | f | key | home | chiavi | Hai le chiavi di casa? | Have you got the house keys?
appartamento | m | flat, apartment | home | appartamenti | Il nostro appartamento è al terzo piano. | Our flat is on the third floor.
giardino | m | garden | home | giardini | I bambini giocano in giardino. | The children are playing in the garden.
# objects
telefono | m | telephone | objects | telefoni | Il telefono squilla. | The phone is ringing.
portafoglio | m | wallet | objects | portafogli | Il portafoglio è nella borsa. | The wallet is in the bag.
"""
)

ADJECTIVES = adjectives(
    """
grande, grande, grandi, grandi | big, large; great | Abitano in una casa grande. | They live in a big house.
piccolo, piccola, piccoli, piccole | small, little | È un piccolo paese di montagna. | It's a small mountain village. | before
buono, buona, buoni, buone | good; tasty | Che buono questo gelato! | This ice cream is so good! | before
cattivo, cattiva, cattivi, cattive | bad; nasty, naughty | Il nostro cane non è cattivo. | Our dog isn't nasty.
bello, bella, belli, belle | beautiful, lovely | Che bella giornata! | What a lovely day! | before
carino, carina, carini, carine | pretty, cute; kind | Che carina la tua casa! | What a sweet house you have!
giovane, giovane, giovani, giovani | young | Mia madre è ancora giovane. | My mother is still young.
vecchio, vecchia, vecchi, vecchie | old | Abitiamo in un palazzo vecchio. | We live in an old building.
nuovo, nuova, nuovi, nuove | new | Ho un telefono nuovo. | I've got a new phone.
gentile, gentile, gentili, gentili | kind | Grazie, sei molto gentile. | Thanks, you're very kind.
contento, contenta, contenti, contente | happy, pleased | Sono contento di vederti. | I'm happy to see you.
stanco, stanca, stanchi, stanche | tired | Stasera sono troppo stanca. | I'm too tired tonight.
caldo, calda, caldi, calde | hot, warm | Vorrei un tè caldo. | I'd like a hot tea.
freddo, fredda, freddi, fredde | cold | L'acqua del mare è fredda. | The sea water is cold.
facile, facile, facili, facili | easy | L'esercizio è facile. | The exercise is easy.
difficile, difficile, difficili, difficili | difficult, hard | L'italiano non è difficile. | Italian isn't difficult.
caro, cara, cari, care | expensive; dear | Questo ristorante è caro. | This restaurant is expensive.
simpatico, simpatica, simpatici, simpatiche | nice, likeable | I tuoi amici sono molto simpatici. | Your friends are really nice.
rosso, rossa, rossi, rosse | red | Preferisco il vino rosso. | I prefer red wine.
blu, blu, blu, blu | (dark) blue | Ha una macchina blu. | He has a blue car.
verde, verde, verdi, verdi | green | Ha gli occhi verdi. | She has green eyes.
giallo, gialla, gialli, gialle | yellow | Le banane sono gialle. | Bananas are yellow.
nero, nera, neri, nere | black | Ho un gatto nero. | I have a black cat.
bianco, bianca, bianchi, bianche | white | Il nonno ha i capelli bianchi. | Grandpa has white hair.
grigio, grigia, grigi, grigie | grey | Oggi il cielo è grigio. | The sky is grey today.
"""
)

VERBS = [
    verb("essere", "to be", [], aux="essere", pp="stato",
         present="sono sei è siamo siete sono", imperfetto="ero eri era eravamo eravate erano",
         fut="sar", subj="sia sia sia siamo siate siano",
         example="Sono di Milano, e tu?", example_en="I'm from Milan, and you?"),
    verb("avere", "to have", [], pp="avuto",
         present="ho hai ha abbiamo avete hanno", fut="avr",
         subj="abbia abbia abbia abbiamo abbiate abbiano",
         example="Quanti anni hai?", example_en="How old are you?"),
    verb("fare", "to do, to make", [], pp="fatto",
         present="faccio fai fa facciamo fate fanno", imp="face", fut="far",
         subj="faccia faccia faccia facciamo facciate facciano",
         example="Che tempo fa oggi?", example_en="What's the weather like today?"),
    verb("stare", "to stay; to be (how you feel)", [], aux="essere", pp="stato",
         present="sto stai sta stiamo state stanno", fut="star",
         subj="stia stia stia stiamo stiate stiano",
         example="Oggi sto molto meglio.", example_en="I'm much better today."),
    verb("venire", "to come", [], aux="essere", pp="venuto",
         present="vengo vieni viene veniamo venite vengono", fut="verr",
         subj="venga venga venga veniamo veniate vengano",
         example="Vieni con noi stasera?", example_en="Are you coming with us tonight?"),
    verb("volere", "to want", [], pp="voluto",
         present="voglio vuoi vuole vogliamo volete vogliono", fut="vorr",
         subj="voglia voglia voglia vogliamo vogliate vogliano",
         example="Vuoi qualcosa da bere?", example_en="Do you want something to drink?"),
    verb("potere", "can, to be able to", [], pp="potuto",
         present="posso puoi può possiamo potete possono", fut="potr",
         subj="possa possa possa possiamo possiate possano",
         example="Posso aprire la finestra?", example_en="May I open the window?"),
    verb("dovere", "to have to, must; to owe", [], pp="dovuto",
         present="devo devi deve dobbiamo dovete devono", fut="dovr",
         subj="debba debba debba dobbiamo dobbiate debbano",
         example="Devo partire domani.", example_en="I have to leave tomorrow."),
    verb("sapere", "to know (a fact, how to)", [], pp="saputo",
         present="so sai sa sappiamo sapete sanno", fut="sapr",
         subj="sappia sappia sappia sappiamo sappiate sappiano",
         example="Non so dove abita.", example_en="I don't know where he lives."),
    verb("dire", "to say, to tell", [], pp="detto",
         present="dico dici dice diciamo dite dicono", imp="dice",
         subj="dica dica dica diciamo diciate dicano",
         example="Come si dice in italiano?", example_en="How do you say it in Italian?"),
    verb("dare", "to give", [], pp="dato",
         present="do dai dà diamo date danno", fut="dar",
         subj="dia dia dia diamo diate diano",
         example="Mi dai il tuo numero?", example_en="Will you give me your number?"),
    verb("uscire", "to go out", [], aux="essere", pp="uscito",
         present="esco esci esce usciamo uscite escono",
         subj="esca esca esca usciamo usciate escano",
         example="Stasera usciamo con gli amici.", example_en="Tonight we're going out with friends."),
    verb("prendere", "to take; to have (food, drink)", [], pp="preso",
         example="Prendo il treno delle otto.", example_en="I'm taking the eight o'clock train."),
    verb("mettere", "to put; to put on", [], pp="messo",
         example="Metti il latte in frigo.", example_en="Put the milk in the fridge."),
    verb("vedere", "to see", [], pp="visto", fut="vedr",
         example="Ci vediamo domani!", example_en="See you tomorrow!"),
    verb("abitare", "to live (somewhere)", ["home"], pp="abitato",
         example="Abito a Torino.", example_en="I live in Turin."),
    verb("lavorare", "to work", [], pp="lavorato",
         example="Lavora in un ospedale.", example_en="She works in a hospital."),
    verb("guardare", "to watch, to look at", [], pp="guardato",
         example="Guardiamo un film stasera?", example_en="Shall we watch a film tonight?"),
    verb("ascoltare", "to listen (to)", [], pp="ascoltato",
         example="Ascolto la radio in macchina.", example_en="I listen to the radio in the car."),
    verb("giocare", "to play", [], pp="giocato",
         example="I bambini giocano in cortile.", example_en="The children are playing in the courtyard."),
    verb("cercare", "to look for", [], pp="cercato",
         example="Cerco la fermata dell'autobus.", example_en="I'm looking for the bus stop."),
    verb("trovare", "to find", [], pp="trovato",
         example="Non trovo il telefono.", example_en="I can't find my phone."),
    verb("pensare", "to think", [], pp="pensato",
         example="Penso di sì.", example_en="I think so."),
    verb("arrivare", "to arrive", [], aux="essere", pp="arrivato",
         example="Il treno arriva a mezzogiorno.", example_en="The train arrives at noon."),
    verb("cominciare", "to begin, to start", [], pp="cominciato",
         example="Il film comincia alle nove.", example_en="The film starts at nine."),
    verb("comprare", "to buy", ["food"], pp="comprato",
         example="Compro il pane ogni mattina.", example_en="I buy bread every morning."),
    verb("finire", "to finish", [], pp="finito", isc=True,
         example="Finisco di lavorare alle sei.", example_en="I finish work at six."),
    verb("capire", "to understand", [], pp="capito", isc=True,
         example="Capisci quando parlo veloce?", example_en="Do you understand when I speak fast?"),
    verb("preferire", "to prefer", [], pp="preferito", isc=True,
         example="Preferisco il tè al caffè.", example_en="I prefer tea to coffee."),
    verb("vendere", "to sell", [], pp="venduto",
         example="Vendono frutta al mercato.", example_en="They sell fruit at the market."),
    verb("aspettare", "to wait (for)", [], pp="aspettato",
         example="Aspetto l'autobus alla fermata.", example_en="I'm waiting for the bus at the stop."),
    verb("imparare", "to learn", [], pp="imparato",
         example="Imparo l'italiano per lavoro.", example_en="I'm learning Italian for work."),
    verb("partire", "to leave", [], aux="essere", pp="partito",
         example="Partiamo domani mattina.", example_en="We're leaving tomorrow morning."),
    verb("dormire", "to sleep", [], pp="dormito",
         example="Il bambino dorme ancora.", example_en="The baby is still asleep."),
    verb("leggere", "to read", [], pp="letto",
         example="Leggo il giornale ogni mattina.", example_en="I read the paper every morning."),
    verb("scrivere", "to write", [], pp="scritto",
         example="Scrivo una mail a mia madre.", example_en="I'm writing an email to my mother."),
    verb("studiare", "to study", [], pp="studiato",
         example="Studio medicina a Padova.", example_en="I study medicine in Padua."),
    verb("chiamarsi", "to be called (name)", ["people"], pp="chiamato",
         example="Mi chiamo Giulia.", example_en="My name is Giulia."),
    verb("piacere", "to please; mi piace, I like", [], aux="essere", pp="piaciuto",
         present="piaccio piaci piace piacciamo piacete piacciono",
         subj="piaccia piaccia piaccia piacciamo piacciate piacciano",
         example="Ti piace la pizza?", example_en="Do you like pizza?"),
]

PHRASES = phrases(
    """
buongiorno | hello, good morning | Buongiorno, un caffè per favore. | Good morning, a coffee please. | good day
buonasera | good evening | Buonasera, avete un tavolo per due? | Good evening, do you have a table for two? | good evening | Used from mid-afternoon on.
ciao | hi; bye (informal) | Ciao Marco, come va? | Hi Marco, how's it going?
salve | hello (neutral) | Salve, posso fare una domanda? | Hello, can I ask a question? | | Polite but not stiff, handy when you can't decide between ciao and buongiorno.
arrivederci | goodbye | Arrivederci e grazie di tutto! | Goodbye, and thanks for everything! | until we see each other again
a presto | see you soon | Ciao, a presto! | Bye, see you soon! | until soon
a domani | see you tomorrow | Allora a domani, alle nove. | See you tomorrow then, at nine. | until tomorrow
buonanotte | good night | Buonanotte, dormi bene. | Good night, sleep well.
grazie | thank you | Grazie per l'aiuto. | Thanks for the help.
grazie mille | thanks a lot | Grazie mille, sei gentilissimo. | Thanks a lot, you're very kind. | a thousand thanks
prego | you're welcome; please, go ahead | Prego, si accomodi. | Please, take a seat. | I pray | The answer to grazie, and the word that waves someone in or offers them something.
per favore | please | Un caffè, per favore. | A coffee, please. | for favour
scusa | sorry; excuse me (informal) | Scusa, sono in ritardo. | Sorry, I'm late.
scusi | excuse me (polite) | Scusi, che ore sono? | Excuse me, what time is it?
mi dispiace | I'm sorry | Mi dispiace, non posso venire. | I'm sorry, I can't come. | it displeases me
sì | yes | Sì, mi piace molto. | Yes, I like it a lot.
no | no | No, grazie, sono a posto. | No thanks, I'm fine.
va bene | OK, fine | Alle otto va bene? | Is eight OK? | it goes well
come stai? | how are you? (informal) | Ciao Anna, come stai? | Hi Anna, how are you? | how do you stay?
come sta? | how are you? (polite) | Buongiorno, dottore, come sta? | Good morning, doctor, how are you?
sto bene, grazie | I'm fine, thanks | Sto bene, grazie, e tu? | I'm fine, thanks, and you? | I stay well
piacere di conoscerti | nice to meet you | Io sono Luca. Piacere di conoscerti! | I'm Luca. Nice to meet you! | pleasure of knowing you | Often just Piacere! To someone you call Lei: piacere di conoscerLa.
non capisco | I don't understand | Scusi, non capisco bene. | Sorry, I don't really understand.
può ripetere? | could you repeat that? (polite) | Scusi, può ripetere più lentamente? | Sorry, could you repeat that more slowly?
più piano, per favore | slower, please | Più piano, per favore, sono straniero. | Slower, please, I'm a foreigner. | more softly
non lo so | I don't know | Non lo so, chiedi a Marco. | I don't know, ask Marco. | I don't know it
quanto costa? | how much is it? | Quanto costa questa borsa? | How much is this bag? | how much does it cost?
il conto, per favore | the bill, please | Scusi, il conto, per favore. | Excuse me, the bill, please.
dov'è il bagno? | where's the toilet? | Scusi, sa dov'è il bagno? | Excuse me, do you know where the toilet is?
c'è | there is | C'è una farmacia qui vicino? | Is there a chemist's near here? | there is
ci sono | there are | Ci sono molti turisti in centro. | There are lots of tourists in the centre. | there are
che cos'è? | what is it? | Che cos'è questo? | What's this? | what thing is it?
a che ora? | at what time? | A che ora parte il treno? | What time does the train leave?
buon appetito | enjoy your meal | Buon appetito a tutti! | Enjoy your meal, everyone! | good appetite
cin cin! | cheers! | Cin cin, alla salute! | Cheers, to your health! | | Said as the glasses touch.
buona giornata | have a good day | Grazie e buona giornata! | Thanks, and have a good day! | good day
buon fine settimana | have a good weekend | Ciao a tutti, buon fine settimana! | Bye everyone, have a good weekend! | good end of the week
d'accordo | agreed, OK | D'accordo, ci vediamo alle sette. | OK, see you at seven. | of agreement
benvenuto | welcome | Benvenuti in Italia! | Welcome to Italy! | | It agrees with who you welcome: benvenuta, benvenuti, benvenute.
""",
    ["greetings"],
)

CONNECTIVES = connectors(
    "connective",
    """
prima | first | conn-sequence | Prima studio, dopo guardo la TV. | First I study, then I watch TV.
dopo | afterwards, later | conn-sequence | Adesso lavoro, ci vediamo dopo. | I'm working now, see you later.
anche | also, too | conn-addition | Parlo inglese e anche un po' di francese. | I speak English and a bit of French too.
""",
    ["connettivi"],
)
CONJUNCTIONS = connectors(
    "conjunction",
    """
e | and | conj-coordinating | Ho un fratello e una sorella. | I have a brother and a sister.
o | or | conj-coordinating | Vuoi un tè o un caffè? | Do you want tea or coffee?
quando | when | conj-subordinating | Leggo quando piove. | I read when it rains.
se | if | conj-subordinating | Usciamo se vuoi. | We'll go out if you want.
""",
    ["congiunzioni"],
)

ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

# Each grammar page's Unit carries the words that use or illustrate it, not
# just whatever happens to share its tag: the pronunciation, pronoun and
# question pages draw their phrases from the greetings set without overlap,
# the numbers page pairs with the words for telling the time, possessives
# with the closest family, and piacere with the food people like.
UNITS = [
    {
        "title": "La pronuncia",
        "page_id": "it-pronunciation",
        "word_ids": ["buongiorno", "ciao", "grazie", "arrivederci", "buonanotte", "piacere-di-conoscerti"],
    },
    {
        "title": "Tu o Lei",
        "page_id": "it-subject-pronouns",
        "word_ids": ["come-stai", "come-sta", "scusa", "scusi", "sto-bene-grazie", "salve"],
    },
    {
        "title": "Essere e avere",
        "page_id": "it-essere-avere",
        "word_ids": ["essere", "avere", "c-e", "ci-sono", "fare", "stare"],
    },
    {
        "title": "Il presente",
        "page_id": "it-present-tense",
        "word_ids": ["abitare", "lavorare", "studiare", "finire", "capire", "vendere", "dormire"],
    },
    {
        "title": "La negazione",
        "page_id": "it-negation",
        "word_ids": ["non-capisco", "non-lo-so", "mi-dispiace", "no", "prendere", "mettere", "vedere"],
    },
    {
        "title": "Le domande",
        "page_id": "it-questions",
        "word_ids": [
            "quanto-costa",
            "dov-e-il-bagno",
            "che-cos-e",
            "a-che-ora",
            "puo-ripetere",
            "piu-piano-per-favore",
            "il-conto-per-favore",
        ],
    },
    {
        "title": "Al, del, nel",
        "page_id": "it-articulated-prepositions",
        "word_ids": ["banca", "scuola", "stazione", "ospedale", "ristorante", "mercato", "bar"],
    },
    {
        "title": "Gli aggettivi",
        "page_id": "it-adjectives",
        "word_ids": ["grande", "piccolo", "buono", "bello", "vecchio", "nuovo", "giovane"],
    },
    {
        "title": "I colori",
        "word_ids": ["rosso", "blu", "verde", "giallo", "nero", "bianco", "grigio"],
    },
    {
        "title": "I numeri",
        "page_id": "it-numbers",
        "word_ids": ["ora", "minuto", "giorno", "lunedi", "martedi", "mercoledi"],
    },
    {
        "title": "I possessivi",
        "page_id": "it-possessives",
        "word_ids": ["padre", "madre", "fratello", "sorella", "marito", "moglie"],
    },
    {
        "title": "Mi piace",
        "page_id": "it-piacere",
        "word_ids": ["piacere", "preferire", "gelato", "pasta", "formaggio", "vino"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "food": "Il cibo",
    "home": "La casa",
    "time": "Il tempo",
    "people": "Le persone",
}

PACK = pack(
    "it-foundations-v1",
    1,
    "it",
    "Italiano · Fondamenta (A1)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Pratica"),
)
