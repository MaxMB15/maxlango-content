"""sv-everyday-v1: A2. The past tenses and strong verbs, the future, reflexive,
particle and s-verbs, the modal verbs, adjective endings and comparison, time
words, and the vocabulary of daily life."""

from common import build_units, interleave, page, pack, topic, topic_labels
from sv_common import adjectives, connectors, nouns, phrases, verb

DELTA = [
    topic("reflexiva-verb", "Reflexiva verb", "reflexive verbs", ["presens"]),
    topic("partikelverb", "Partikelverb", "particle verbs", ["presens"]),
    topic("s-verb", "S-verb", "verbs ending in -s", ["presens"]),
    topic("clothing", "Kläder", "clothing", ["artiklar"]),
    topic("weather", "Väder", "weather", ["artiklar"]),
    topic("travel", "Resor", "travel", ["artiklar"]),
    topic("work", "Arbete", "work and study", ["artiklar"]),
    topic("health", "Hälsa", "health", ["artiklar"]),
    topic("leisure", "Fritid", "free time", ["artiklar"]),
    topic("feelings", "Känslor", "feelings and character", ["adjektiv"]),
    topic("shopping", "Handla", "shopping and money", ["artiklar"]),
    topic("expressions", "Uttryck", "set phrases and idioms", []),
    {
        "id": "conn-consequence",
        "kind": "connective-class",
        "label": "Följd",
        "labelGloss": "the next statement is the result of the last one (så, därför)",
        "order": 4,
        "appliesTo": {"kind": "connective"},
        "dependsOn": [],
    },
]

PAGES = [
    page(
        "sv-perfekt",
        "The perfect: har gjort",
        r"""
The perfect (*perfekt*) is **har** plus a verb form called the **supine** (*supinum*): *jag har ätit* (I have eaten). Unlike Dutch, German and French, Swedish always uses **har**, verbs of movement included: *Hon har kommit* (She has come), *Vi har åkt hem* (We've gone home).

| | arbeta | köpa | bo | skriva |
| --- | --- | --- | --- | --- |
| jag, du, hon, vi, ni, de | har arbetat | har köpt | har bott | har skrivit |

## Building the supine

| Group | Infinitive | Supine | Rule |
| --- | --- | --- | --- |
| 1 | arbeta, tala | arbetat, talat | add -t |
| 2 | köpa, stänga | köpt, stängt | drop -a, add -t |
| 3 | bo, tro | bott, trott | add -tt |
| 4 | skriva, dricka | skrivit, druckit | strong verbs: -it, often with a new vowel |

Every verb card shows the supine in its perfect tense.

## Supine or participle?

The supine is only ever used after *har* or *hade*. To describe a state, Swedish uses another form, the participle, which agrees like an adjective:

- *Jag har stängt dörren.* (I've closed the door.) But: *Dörren är stängd.* (The door is closed.)
- *Hon har skrivit ett brev.* (She has written a letter.) But: *Brevet är skrivet.* (The letter is written.)

English uses *closed* and *written* for both jobs, so *jag har stängd* is a common slip.

## When to use it

Mostly as in English: for something that has happened at some point up to now, or a state that is still going on.

- *Jag har aldrig varit i Norrland.* (I've never been to Norrland.)
- *Vi har bott här i fem år.* (We've lived here for five years.)

Swedes also use it where English prefers the simple past, when the result matters more than the moment: *Vem har gjort det här?* (Who did this?) *Var har du köpt jackan?* (Where did you buy that jacket?)

What the perfect can't do is go with a finished time. *I går har jag ringt* is wrong; with *i går*, *förra veckan* or *när*, use the past tense on the next page.

## Har can disappear

In a subordinate clause, written Swedish often drops *har*: *Jag vet att hon ringt.* You'll see this in newspapers. You don't have to do it yourself.

:::examples
- Jag har redan ätit. — I've already eaten.
- Har du sett min nyckel? — Have you seen my key?
- De har flyttat till Lund. — They've moved to Lund.
:::

:::predict{prompt="hon (städa)" answer="har städat"}
:::

:::cloze{sentence="Vi har ___ i Sverige sedan 2019." blank="bott"}
:::
""",
        ["perfekt"],
        "sv-perfekt",
        explains=["perfekt"],
    ),
    page(
        "sv-preteritum",
        "The past tense",
        r"""
The **preteritum** is the simple past: *I worked, I bought, I lived*. Like every Swedish tense, it has one form for all persons.

| Group | Infinitive | Present | Past | Rule |
| --- | --- | --- | --- | --- |
| 1 | arbeta | arbetar | arbetade | add -de |
| 2 | stänga, höra | stänger, hör | stängde, hörde | drop -a, add -de |
| 2 | köpa, läsa | köper, läser | köpte, läste | after k, p, s, t, x: -te |
| 3 | bo, tro | bor, tror | bodde, trodde | add -dde |
| 4 | skriva, gå | skriver, går | skrev, gick | learn them one by one (next page) |

For group 2, say the stem aloud. If it ends in a voiceless sound (k, p, s, t, x), the past ends in **-te**: *köpte, läste, tyckte*. Otherwise it's **-de**: *stängde, ringde, hörde*.

## Past or perfect?

Use the past tense when you say, or mean, *when*: a finished time in the past.

| Past tense | Perfect |
| --- | --- |
| I går ringde jag mamma. | Jag har ringt mamma. |
| Förra året bodde vi i Malmö. | Vi har bott i Malmö. |
| Filmen började klockan åtta. | Filmen har börjat. |

A question with **när** always takes the past: *När kom du hem?*, never *När har du kommit hem?*

## Where Swedish uses the past and English doesn't

Swedes react to something happening right now in the past tense:

- *Det var gott!* (said while eating: This is good!)
- *Vad hette du nu igen?* (What's your name again?)
- *Det var snällt av dig.* (That's kind of you.)

## Hade and the supine

*Hade* plus the supine is the past perfect, *had done*, used as in English: *När vi kom fram hade filmen redan börjat.* (When we got there, the film had already started.)

:::examples
- I går lagade jag middag. — Yesterday I made dinner.
- Vi tittade på en film i lördags. — We watched a film last Saturday.
- Hon köpte en ny cykel förra veckan. — She bought a new bike last week.
:::

:::predict{prompt="de (prata)" answer="pratade"}
:::

:::predict{prompt="jag (läsa)" answer="läste"}
:::

:::cloze{sentence="Vi ___ till Uppsala för två år sedan." blank="flyttade"}
:::
""",
        ["preteritum"],
        "sv-preteritum",
        explains=["preteritum"],
    ),
    page(
        "sv-strong-verbs",
        "Strong verbs: skriva, skrev, skrivit",
        r"""
About 150 Swedish verbs, many of them the most common in the language, form their past by changing a vowel, the way English has *sing, sang, sung*. These are the **strong verbs**. Their past has no ending at all, and their supine ends in **-it**.

They come in families, so learning one helps with the rest:

| Vowels | Infinitive | Past | Supine | English |
| --- | --- | --- | --- | --- |
| i, e, i | skriva | skrev | skrivit | write |
| i, e, i | bita | bet | bitit | bite |
| i, a, u | dricka | drack | druckit | drink |
| i, a, u | försvinna | försvann | försvunnit | disappear |
| y, ö, u | frysa | frös | frusit | be cold, freeze |
| a, o, a | dra | drog | dragit | pull |
| ä, a, u | skära | skar | skurit | cut |

And a handful that follow no pattern:

| Infinitive | Past | Supine | English |
| --- | --- | --- | --- |
| gå | gick | gått | go, walk |
| få | fick | fått | get |
| se | såg | sett | see |
| ge | gav | gett | give |
| göra | gjorde | gjort | do, make |
| säga | sa | sagt | say |
| veta | visste | vetat | know |

## Classic mistakes

- **Adding -de to a strong verb.** *Jag drack*, never *jag drickade*.
- **Ligga or lägga?** *Ligga* (lie, be lying) goes *låg, legat*. *Lägga* (lay, put) goes *la, lagt*. It's the same pair as English *lie* and *lay*.
- **Sitta or sätta?** *Sitta* (sit) goes *satt, suttit*. *Sätta* (put) goes *satte, satt*. So *satt* is the past of one and the supine of the other.

Some verbs have a long and a short past: *sade* or *sa*, *lade* or *la*. Everyone says the short form, and it's now normal in writing too.

:::examples
- Vi drack kaffe och pratade i två timmar. — We drank coffee and talked for two hours.
- Hon har skrivit tre böcker. — She has written three books.
- Jag frös hela natten i tältet. — I was cold all night in the tent.
:::

:::cloze{sentence="Barnen ___ hela vägen hem från skolan." blank="sprang"}
:::

:::cloze{sentence="Har du ___ min mobil? Den låg här nyss." blank="sett"}
:::
""",
        ["preteritum"],
        "sv-strong-verbs",
    ),
    page(
        "sv-future",
        "Talking about the future",
        r"""
Swedish has no single future tense. It has three ways to talk about what's coming, and the one you pick says why you think it will happen.

| Form | Use | Example |
| --- | --- | --- |
| present + time word | plans and timetables; the everyday choice | Jag åker till Göteborg i morgon. |
| ska + infinitive | a plan, a decision, a promise | Vi ska flytta i vår. |
| kommer att + infinitive | a prediction that is nobody's plan | Det kommer att bli kallt i natt. |

The difference is real. *Jag ska bli läkare* is a plan: I'm going to be a doctor. *Du kommer att bli en bra läkare* is a prediction: you'll make a good doctor.

## More jobs for ska

- A suggestion: *Ska vi gå?* (Shall we go?)
- What someone is supposed to do: *Du ska ta medicinen två gånger om dagen.*
- What you've heard: *Det ska regna i morgon* (It's supposed to rain tomorrow, says the forecast).

In speech the *att* in *kommer att* often disappears: *Det kommer bli bra.* Writing it with *att* is the safe choice.

## Classic mistakes

- **Vill is not *will*.** *Jag vill komma* means "I want to come". For the future, use *ska* or *kommer att*.
- **Kommer att for your own plans.** *Jag kommer att gå på bio i kväll* sounds like a forecast about yourself. Say *Jag ska gå på bio i kväll*, or just *Jag går på bio i kväll*.

One more: **tänker** + infinitive is a firm intention, often a defiant one: *Jag tänker inte betala!* (I'm not paying!)

:::examples
- Vi ska äta middag hos Lisa på lördag. — We're having dinner at Lisa's on Saturday.
- Det kommer att gå bra, ska du se. — It'll be fine, you'll see.
- Tåget går klockan sju i morgon. — The train leaves at seven tomorrow.
:::

:::cloze{sentence="Det ___ att snöa i helgen." blank="kommer"}
:::
""",
        ["futurum"],
        "sv-future",
        explains=["futurum"],
    ),
    page(
        "sv-reflexive-verbs",
        "Reflexive verbs: sätta sig",
        r"""
A reflexive verb has an object that points back to the subject: *Jag tvättar mig* (I wash myself, I have a wash). Swedish has many more of these than English, and most of the time the pronoun has no English translation.

| | sätta sig (sit down) |
| --- | --- |
| jag | sätter mig |
| du | sätter dig |
| han, hon | sätter sig |
| vi | sätter oss |
| ni | sätter er |
| de | sätter sig |

The pronoun is the ordinary object form, except in the third person, which has its own: **sig** (said "sej").

## Sig or honom?

*Han tvättar sig* means he's washing himself. *Han tvättar honom* means he's washing someone else, the baby perhaps. It's the same logic as *sin* and *hans* on the possessives page.

## Reflexive in Swedish, not in English

| Swedish | English |
| --- | --- |
| sätta sig | sit down |
| lägga sig | lie down; go to bed |
| känna sig | feel |
| skynda sig | hurry |
| gifta sig | get married |
| lära sig | learn |
| klä på sig | get dressed |
| bestämma sig | decide |
| ångra sig | change your mind |

Leave out the pronoun and the meaning often changes: *Hon lär mig svenska* means "She teaches me Swedish"; *Jag lär mig svenska* means "I'm learning Swedish".

## Word order

The pronoun comes straight after the verb, or after the subject when the subject follows the verb. *Inte* comes after the pronoun:

- *Nu sätter jag mig.*
- *Han känner sig inte bra.* (He doesn't feel well.)

:::examples
- Jag känner mig lite trött i dag. — I feel a bit tired today.
- Sätt dig, maten är klar! — Sit down, the food's ready!
- De gifte sig i somras. — They got married last summer.
:::

:::cloze{sentence="Vi måste skynda ___, tåget går snart." blank="oss"}
:::
""",
        ["reflexiva-verb"],
        "sv-reflexive-verbs",
        explains=["reflexiva-verb"],
    ),
    page(
        "sv-particle-verbs",
        "Particle verbs: tycka om",
        r"""
Like English, Swedish has verbs that need a small extra word to make their meaning: *ta med* (bring), *stänga av* (switch off), *tycka om* (like). Swedes call the small word a **particle**, and the thing to know is that **the particle takes the stress**, not the verb.

| Verb | On its own | With the particle |
| --- | --- | --- |
| tycka | think (have an opinion) | tycka om: like |
| hälsa | greet | hälsa på: visit |
| ta | take | ta med: bring |
| stänga | close | stänga av: switch off |
| sätta | put | sätta på: switch on; put on |
| komma | come | komma ihåg: remember |
| känna | know, feel | känna igen: recognise |
| hålla | hold | hålla med: agree |

## Stress changes the meaning

Stress the small word and it's a particle verb. Stress the verb and the small word is an ordinary preposition:

- *Jag tycker **om** dig.* (I like you.)
- *Vad **tycker** du om filmen?* (What do you think of the film?)
- *Vi ska hälsa **på** mormor.* (We're going to visit Grandma.)
- *Hon **hälsade** på mig.* (She said hello to me.)

## Where the particle goes

Unlike Dutch and German, Swedish doesn't send the particle to the end of the sentence or glue it to the front of a finite verb. It follows the verb, with *inte* and other short adverbs in between:

- *Jag kommer inte ihåg hans namn.* (I can't remember his name.)

And unlike English, a pronoun object comes after the particle: *Stäng av den!* (Switch it off!) *Sätt på den!* (Turn it on!)

:::examples
- Jag tycker om att laga mat. — I like cooking.
- Kommer du ihåg mig? — Do you remember me?
- Jag håller med dig. — I agree with you.
:::

:::cloze{sentence="Kan du stänga ___ tv:n? Jag ska sova." blank="av"}
:::
""",
        ["partikelverb"],
        "sv-particle-verbs",
        explains=["partikelverb"],
    ),
    page(
        "sv-modal-verbs",
        "Kan, vill, måste, får",
        r"""
Modal verbs add a shade of meaning to another verb: ability, wish, need, permission. The second verb is a plain infinitive, with **no att**: *Jag kan simma*, never *Jag kan att simma*.

| Infinitive | Present | Past | English |
| --- | --- | --- | --- |
| kunna | kan | kunde | can, be able to |
| vilja | vill | ville | want |
| måste | måste | måste | must, have to |
| skola | ska | skulle | shall, will |
| få | får | fick | may; get to |
| böra | bör | borde | should, ought to |

## Får: allowed, or have to

*Får jag låna din cykel?* asks for permission: May I borrow your bike? But *Du får vänta lite* means "You'll have to wait a bit". The context tells you which.

## The måste trap

*Du måste komma* is "you must come". The negative doesn't work the way English speakers expect:

| English | Swedish |
| --- | --- |
| You don't have to come. | Du behöver inte komma. |
| You mustn't come. | Du får inte komma. |

## Six more verbs that work the same way

| Verb | Meaning |
| --- | --- |
| behöva | need |
| bruka | usually do |
| hinna | have time to, make it |
| orka | have the energy to |
| våga | dare |
| slippa | not have to, get out of |

*Brukar* is how Swedes say "usually": *Jag brukar dricka te* is literally "I use to drink tea". *Vanligtvis* is correct too, but it sounds stiff in conversation.

*Orka* and *slippa* have no English match. *Jag orkar inte* is "I can't face it, I'm too tired". *Vi slipper diska* is "We get out of doing the washing-up".

:::examples
- Kan du hjälpa mig? — Can you help me?
- Vi hann inte äta frukost. — We didn't have time for breakfast.
- Jag orkar inte gå ut i kväll. — I can't face going out tonight.
:::

:::sort{groups="Utan att: kan, vill, måste, brukar | Med att: älskar, glömmer, lovar, planerar"}
:::
""",
        ["presens"],
        "sv-modal-verbs",
    ),
    page(
        "sv-adjectives",
        "Adjective endings",
        r"""
A Swedish adjective agrees with its noun. It adds **-t** for an ett-word and **-a** in the plural:

| | en-word | ett-word | plural |
| --- | --- | --- | --- |
| a big ... | en stor bil | ett stort hus | stora bilar |
| the big ... | den stora bilen | det stora huset | de stora bilarna |

After *den, det, de* and after possessives (*min, din, Annas*), the adjective always takes **-a**: *min nya cykel, Annas gamla hus.*

## It agrees after är too

Unlike English, Dutch and German, a Swedish adjective agrees even when it comes after the verb:

- *Bilen är ny.*
- *Köket är nytt.*
- *Bilarna är nya.*

*Köket är ny* is one of the most common learner mistakes in Swedish.

## Spelling the -t form

| The adjective ends in | Example | ett-form |
| --- | --- | --- |
| a long vowel + d | röd, glad | rött, glatt |
| a consonant + t | svart, trött | svart, trött (no change) |
| -en | ledsen, öppen | ledset, öppet |
| a long vowel | ny, blå | nytt, blått |

## Spelling the -a form

- **-al, -el, -en, -er** lose their vowel: *gammal → gamla, enkel → enkla, öppen → öppna, vacker → vackra*.
- **m** after a short vowel doubles: *tom → tomma*.
- *Bra, rosa, extra* and *gratis* never change.

*Liten* is irregular: *en liten bil, ett litet hus, den lilla bilen, små bilar*.

:::examples
- Vi bor i ett gammalt hus. — We live in an old house.
- Mina nya skor är bekväma. — My new shoes are comfortable.
- Den lilla flickan sover. — The little girl is asleep.
:::

:::predict{prompt="huset är (ny)" answer="nytt"}
:::

:::predict{prompt="barnen är (glad)" answer="glada"}
:::
""",
        ["adjektiv"],
        "sv-adjectives",
        explains=["adjektiv"],
    ),
    page(
        "sv-comparatives",
        "Bigger, biggest",
        r"""
Most adjectives add **-are** for *more* and **-ast** for *most*:

| | Comparative | Superlative |
| --- | --- | --- |
| billig | billigare | billigast |
| snabb | snabbare | snabbast |
| varm | varmare | varmast |

A dozen of the most common ones change their vowel and add **-re** and **-st** instead:

| | Comparative | Superlative |
| --- | --- | --- |
| stor | större | störst |
| lång | längre | längst |
| ung | yngre | yngst |
| gammal | äldre | äldst |
| hög | högre | högst |
| låg | lägre | lägst |
| tung | tyngre | tyngst |
| liten | mindre | minst |
| bra | bättre | bäst |
| dålig | sämre | sämst |
| många | fler | flest |
| mycket | mer | mest |

Long adjectives, and those ending in *-isk*, take **mer** and **mest**: *mer intressant, mest praktisk*.

## Than, as ... as

- **än** is *than*: *Stockholm är större än Göteborg.*
- **lika ... som** is *as ... as*: *Hon är lika lång som sin bror.*

## The definite superlative

Before a noun, the superlative adds **-e** (or **-a**): *den största staden, det billigaste rummet, de bästa åren.* After *är*, it doesn't: *Vem är äldst?*

## Classic mistakes

- *Mer stor* for *större*. Short adjectives take the ending.
- *Mer* or *fler*? **Fler** is for things you count: *fler bilar*, *mer kaffe*.

:::examples
- Det är varmare i dag än i går. — It's warmer today than yesterday.
- Vilken är den billigaste biljetten? — Which is the cheapest ticket?
- Min syster är yngst i familjen. — My sister is the youngest in the family.
:::

:::cloze{sentence="Min bror är två år ___ än jag." blank="äldre"}
:::
""",
        ["adjektiv"],
        "sv-comparatives",
    ),
    page(
        "sv-s-verbs",
        "Verbs that end in -s",
        r"""
Some Swedish verbs end in **-s** in every form. You've already met two: *vi ses* (see you) and *det finns* (there is). They come in three kinds.

## Verbs that only exist with -s

They look passive, but they mean something active:

| Infinitive | Present | Past | Supine | English |
| --- | --- | --- | --- | --- |
| hoppas | hoppas | hoppades | hoppats | hope |
| lyckas | lyckas | lyckades | lyckats | succeed, manage |
| andas | andas | andades | andats | breathe |
| minnas | minns | mindes | mints | remember |
| trivas | trivs | trivdes | trivts | like it (somewhere), feel at home |
| finnas | finns | fanns | funnits | exist; there is |

There's no **-r** in the present: *jag hoppas*, never *jag hoppars*. Verbs like *minnas* and *trivas* also drop the **a**: *minns, trivs*.

*Trivas* has no English match. *Jag trivs i Sverige* means "I like living in Sweden, I feel at home here". *Hon trivs bra med sina kollegor* means she gets on well at work.

## Doing something to each other

The -s can also mean *each other*:

| Verb | English |
| --- | --- |
| ses | see each other |
| träffas | meet |
| höras | talk (on the phone) |
| kramas | hug |
| slåss | fight |

That's why Swedes say goodbye with *Vi ses!* and *Vi hörs!*

## The passive

Added to almost any verb, -s also makes a passive: *Huset byggdes 1890* (The house was built in 1890). The B1 pack covers it.

:::examples
- Jag hoppas att du kommer. — I hope you'll come.
- Minns du vår första semester? — Do you remember our first holiday?
- Det finns ingen mjölk kvar. — There's no milk left.
:::

:::cloze{sentence="Hur ___ du på nya jobbet?" blank="trivs"}
:::
""",
        ["s-verb"],
        "sv-s-verbs",
        explains=["s-verb"],
    ),
    page(
        "sv-time-expressions",
        "I, på, om: time words",
        r"""
Swedish uses its small prepositions for time in ways that don't map onto English. A few patterns cover most of it.

## Ago, for, in

| English | Swedish |
| --- | --- |
| two years ago | för två år sedan |
| for two years | i två år |
| in two hours (from now) | om två timmar |
| in two hours (it took that long) | på två timmar |
| since Monday | sedan i måndags |

- *Jag bodde i London i två år.* (I lived in London for two years.)
- *Vi går om en kvart.* (We're leaving in a quarter of an hour.)
- *Jag läste boken på två dagar.* (I read the book in two days.)

*Sedan* is written in full and said **sen**.

## Last, this coming, in general

This is the most Swedish part. For days and seasons, **i** with an old **-s** form means *last*, and plain **på** or **i** means *this coming*:

| Last ... | This coming ... | In general |
| --- | --- | --- |
| i måndags | på måndag | på måndagar |
| i lördags | på lördag | på lördagar |
| i somras | i sommar | på sommaren |
| i vintras | i vinter | på vintern |
| i höstas | i höst | på hösten |
| i våras | i vår | på våren |

## Parts of the day

| Swedish | English |
| --- | --- |
| i morse | this morning (it's over) |
| i eftermiddag | this afternoon |
| i kväll | this evening, tonight |
| i natt | tonight; last night |
| i går kväll | last night, yesterday evening |
| på morgonen | in the morning (in general) |

*I natt* takes its meaning from the verb: *I natt sov jag dåligt* (I slept badly last night), *I natt ska vi sova i tält* (Tonight we're sleeping in a tent).

## Nästa and förra

*Nästa vecka* is next week and *förra veckan* is last week. The noun after *förra* takes the definite ending; after *nästa*, it doesn't.

:::examples
- Vi var i Italien i somras. — We were in Italy last summer.
- Jag ringer dig om en stund. — I'll call you in a bit.
- Affären har varit stängd sedan i fredags. — The shop has been shut since last Friday.
:::

:::cloze{sentence="Vi flyttade hit för tre år ___." blank="sedan"}
:::

:::cloze{sentence="Tåget går ___ tio minuter." blank="om"}
:::
""",
        ["time"],
        "sv-time-expressions",
        explains=["time"],
    ),
]

NOUNS = nouns(
    """
# clothing
tröja | en | tröjan | tröjor | jumper, sweater | clothing | Ta på dig en varm tröja. | Put on a warm jumper.
skjorta | en | skjortan | skjortor | shirt | clothing | Han stryker sin skjorta varje morgon. | He irons his shirt every morning.
klänning | en | klänningen | klänningar | dress | clothing | Hon köpte en ny klänning till bröllopet. | She bought a new dress for the wedding.
kjol | en | kjolen | kjolar | skirt | clothing | Kjolen är för kort för mig. | The skirt is too short for me.
jacka | en | jackan | jackor | jacket | clothing | Glöm inte jackan, det är kallt ute. | Don't forget your jacket, it's cold out.
sko | en | skon | skor | shoe | clothing | Ta av dig skorna i hallen. | Take your shoes off in the hall.
strumpa | en | strumpan | strumpor | sock | clothing | Jag hittar aldrig två likadana strumpor. | I can never find two matching socks.
mössa | en | mössan | mössor | woolly hat, beanie | clothing | På vintern har alla mössa. | In winter everyone wears a woolly hat.
väska | en | väskan | väskor | bag | clothing | Min väska är full av papper. | My bag is full of papers.
paraply | ett | paraplyet | paraplyer | umbrella | clothing | Ta med paraplyet, det ska regna. | Take the umbrella, it's supposed to rain.
# weather
väder | ett | vädret | - | weather | weather | Vädret är fint i dag. | The weather's nice today.
regn | ett | regnet | - | rain | weather | Det kommer mycket regn i november. | There's a lot of rain in November.
snö | en | snön | - | snow | weather | Barnen leker i snön. | The children are playing in the snow.
vind | en | vinden | vindar | wind | weather | Vinden är kall vid havet. | The wind is cold by the sea.
moln | ett | molnet | moln | cloud | weather | Det finns inte ett moln på himlen. | There isn't a cloud in the sky.
grad | en | graden | grader | degree | weather | Det är minus tio grader ute. | It's minus ten outside.
vår | en | våren | vårar | spring | weather | Våren kommer sent i norr. | Spring comes late in the north.
sommar | en | sommaren | somrar | summer | weather | Svenska somrar är korta men ljusa. | Swedish summers are short but light.
höst | en | hösten | höstar | autumn | weather | På hösten blir löven röda och gula. | In autumn the leaves turn red and yellow.
vinter | en | vintern | vintrar | winter | weather | Vintern är lång och mörk. | Winter is long and dark.
# travel
resa | en | resan | resor | trip, journey | travel | Hur var resan? | How was the trip?
tåg | ett | tåget | tåg | train | travel | Tåget är tio minuter försenat. | The train is ten minutes late.
buss | en | bussen | bussar | bus | travel | Jag tar bussen till jobbet. | I take the bus to work.
flygplats | en | flygplatsen | flygplatser | airport | travel | Hur kommer man till flygplatsen? | How do you get to the airport?
biljett | en | biljetten | biljetter | ticket | travel | Jag köper biljetten i appen. | I buy the ticket in the app.
pass | ett | passet | pass | passport | travel | Glöm inte passet! | Don't forget your passport!
hotell | ett | hotellet | hotell | hotel | travel | Hotellet ligger nära stationen. | The hotel is near the station.
resväska | en | resväskan | resväskor | suitcase | travel | Min resväska är för tung. | My suitcase is too heavy.
karta | en | kartan | kartor | map | travel | Kan du visa mig på kartan? | Can you show me on the map?
semester | en | semestern | semestrar | holiday, vacation | travel | Vi har semester hela juli. | We're on holiday all of July.
# work
arbete | ett | arbetet | arbeten | work, job | work | Hon söker ett nytt arbete. | She's looking for a new job.
chef | en | chefen | chefer | boss, manager | work | Min chef är på semester. | My boss is on holiday.
kollega | en | kollegan | kollegor | colleague | work | Jag äter lunch med mina kollegor. | I have lunch with my colleagues.
kontor | ett | kontoret | kontor | office | work | Kontoret ligger i centrum. | The office is in the centre.
möte | ett | mötet | möten | meeting | work | Jag har möte hela förmiddagen. | I'm in a meeting all morning.
lön | en | lönen | löner | pay, salary | work | Lönen kommer den 25:e varje månad. | Pay day is the 25th of every month.
lärare | en | läraren | lärare | teacher | work | Min lärare är från Finland. | My teacher is from Finland.
student | en | studenten | studenter | student | work | Många studenter bor i Lund. | Lots of students live in Lund.
dator | en | datorn | datorer | computer | work | Datorn är för långsam. | The computer is too slow.
utbildning | en | utbildningen | utbildningar | education, training, course | work | Utbildningen tar tre år. | The course takes three years.
# health
läkare | en | läkaren | läkare | doctor | health | Du borde gå till läkaren. | You should go to the doctor.
sjuksköterska | en | sjuksköterskan | sjuksköterskor | nurse | health | Sjuksköterskan ringer dig i eftermiddag. | The nurse will call you this afternoon.
vårdcentral | en | vårdcentralen | vårdcentraler | health centre, GP surgery | health | Jag har en tid på vårdcentralen. | I have an appointment at the health centre.
apotek | ett | apoteket | apotek | pharmacy, chemist's | health | Apoteket stänger klockan sju. | The chemist's closes at seven.
medicin | en | medicinen | mediciner | medicine | health | Ta medicinen efter maten. | Take the medicine after eating.
feber | en | febern | - | fever, temperature | health | Hon har hög feber. | She has a high temperature.
förkylning | en | förkylningen | förkylningar | cold | health | Jag har fått en förkylning. | I've caught a cold.
rygg | en | ryggen | ryggar | back | health | Sitt rak i ryggen! | Sit up straight!
hals | en | halsen | halsar | throat; neck | health | Jag har ont i halsen och hostar. | I have a sore throat and a cough.
tandläkare | en | tandläkaren | tandläkare | dentist | health | Jag ska till tandläkaren i morgon. | I'm going to the dentist tomorrow.
# leisure
fritid | en | fritiden | - | free time | leisure | Vad gör du på fritiden? | What do you do in your free time?
film | en | filmen | filmer | film | leisure | Har du sett den nya filmen? | Have you seen the new film?
konsert | en | konserten | konserter | concert | leisure | Vi ska på konsert i kväll. | We're going to a concert tonight.
musik | en | musiken | - | music | leisure | Vilken musik lyssnar du på? | What music do you listen to?
fotboll | en | fotbollen | fotbollar | football | leisure | Han spelar fotboll två gånger i veckan. | He plays football twice a week.
tidning | en | tidningen | tidningar | newspaper | leisure | Jag läser tidningen på mobilen. | I read the paper on my phone.
museum | ett | museet | museer | museum | leisure | Vasamuseet är Stockholms mest kända museum. | The Vasa Museum is Stockholm's best-known museum.
fest | en | festen | fester | party | leisure | Festen börjar klockan åtta. | The party starts at eight.
stuga | en | stugan | stugor | cottage, summer house | leisure | De har en röd stuga vid sjön. | They have a red cottage by the lake.
bibliotek | ett | biblioteket | bibliotek | library | leisure | Jag lånar böcker på biblioteket. | I borrow books from the library.
# shopping
krona | en | kronan | kronor | krona (Swedish money) | shopping | Det kostar fyrtio kronor. | It costs forty kronor.
pris | ett | priset | priser | price | shopping | Priserna har gått upp i år. | Prices have gone up this year.
plånbok | en | plånboken | plånböcker | wallet | shopping | Jag har tappat min plånbok. | I've lost my wallet.
kvitto | ett | kvittot | kvitton | receipt | shopping | Vill du ha kvittot? | Would you like the receipt?
kassa | en | kassan | kassor | till, checkout | shopping | Betala i kassan, tack. | Please pay at the till.
kö | en | kön | köer | queue | shopping | Det är lång kö till kassan. | There's a long queue for the till.
rea | en | rean | reor | sale | shopping | Jag köpte jackan på rea. | I bought the jacket in a sale.
påse | en | påsen | påsar | carrier bag | shopping | Vill du ha en påse? | Would you like a bag?
present | en | presenten | presenter | present, gift | shopping | Vi köper en present till mormor. | We're buying a present for Grandma.
mataffär | en | mataffären | mataffärer | supermarket, grocery shop | shopping | Mataffären är öppen till tio. | The supermarket is open until ten.
# home
golv | ett | golvet | golv | floor | home | Barnen sitter på golvet och leker. | The children are sitting on the floor, playing.
vägg | en | väggen | väggar | wall | home | Vi målar väggarna vita. | We're painting the walls white.
tak | ett | taket | tak | roof; ceiling | home | Taket är väldigt högt i gamla hus. | Old houses have very high ceilings.
kylskåp | ett | kylskåpet | kylskåp | fridge | home | Ställ in smöret i kylskåpet. | Put the butter in the fridge.
lampa | en | lampan | lampor | lamp, light | home | Kan du tända lampan? | Can you turn on the light?
spis | en | spisen | spisar | cooker, stove | home | Soppan står på spisen. | The soup is on the stove.
tvättmaskin | en | tvättmaskinen | tvättmaskiner | washing machine | home | Tvättmaskinen är trasig igen. | The washing machine is broken again.
# family and friends
bebis | en | bebisen | bebisar | baby | family | De har fått en bebis! | They've had a baby!
kompis | en | kompisen | kompisar | friend, mate | family | Jag ska träffa en kompis i kväll. | I'm meeting a friend tonight.
pojkvän | en | pojkvännen | pojkvänner | boyfriend | family | Hennes pojkvän kommer från Norge. | Her boyfriend is from Norway.
flickvän | en | flickvännen | flickvänner | girlfriend | family | Han bor med sin flickvän i Malmö. | He lives with his girlfriend in Malmö.
sambo | en | sambon | sambor | partner (you live with) | family | Det här är Anna, min sambo. | This is Anna, my partner.
barnbarn | ett | barnbarnet | barnbarn | grandchild | family | Mormor har sex barnbarn. | Grandma has six grandchildren.
# food
kyckling | en | kycklingen | kycklingar | chicken | food | Vi äter kyckling med ris i kväll. | We're having chicken and rice tonight.
soppa | en | soppan | soppor | soup | food | Jag gör en soppa på grönsakerna. | I'm making a soup with the vegetables.
korv | en | korven | korvar | sausage | food | En korv med bröd, tack. | A hot dog, please.
godis | ett | godiset | - | sweets, candy | food | Hur mycket godis har du ätit? | How many sweets have you eaten?
köttbulle | en | köttbullen | köttbullar | meatball | food | Vi äter köttbullar med potatis. | We're having meatballs and potatoes.
lax | en | laxen | laxar | salmon | food | Laxen är färsk i dag. | The salmon is fresh today.
"""
)

ADJECTIVES = (
    adjectives(
        """
ren, rent, rena | clean | Är handduken ren? | Is the towel clean?
smutsig, smutsigt, smutsiga | dirty | Dina skor är smutsiga. | Your shoes are dirty.
tom, tomt, tomma | empty | Kylskåpet är helt tomt. | The fridge is completely empty.
full, fullt, fulla | full; drunk | Tåget är fullt i dag. | The train is full today.
öppen, öppet, öppna | open | Är affären öppen på söndag? | Is the shop open on Sunday?
stängd, stängt, stängda | closed, shut | Banken är stängd i dag. | The bank is closed today.
lång, långt, långa | long; tall | Min bror är väldigt lång. | My brother is very tall.
kort, kort, korta | short | Filmen var ganska kort. | The film was quite short.
tung, tungt, tunga | heavy | Din väska är så tung! | Your bag is so heavy!
hög, högt, höga | high, tall; loud | Musiken är för hög. | The music is too loud.
låg, lågt, låga | low | Priserna är låga på rean. | Prices are low in the sale.
snabb, snabbt, snabba | fast, quick | Tåget till Göteborg är snabbt. | The train to Gothenburg is fast.
sjuk, sjukt, sjuka | ill, sick | Jag är sjuk och stannar hemma. | I'm ill and I'm staying home.
frisk, friskt, friska | healthy, well | Är du frisk igen? | Are you well again?
ledig, ledigt, lediga | free; off work | Är den här platsen ledig? | Is this seat free?
upptagen, upptaget, upptagna | busy, taken | Tyvärr är jag upptagen i kväll. | Unfortunately I'm busy tonight.
tråkig, tråkigt, tråkiga | boring; sad (news) | Mötet var långt och tråkigt. | The meeting was long and boring.
mysig, mysigt, mysiga | cosy | Vilket mysigt kafé! | What a cosy café!
"""
    )
    + adjectives(
        """
arg, argt, arga | angry | Varför är du arg på mig? | Why are you angry with me?
nervös, nervöst, nervösa | nervous | Jag är nervös inför intervjun. | I'm nervous about the interview.
lugn, lugnt, lugna | calm, quiet | Hon är lugn även när det är stressigt. | She stays calm even when it's stressful.
orolig, oroligt, oroliga | worried | Mamma blir orolig när jag kommer hem sent. | Mum gets worried when I come home late.
stolt, stolt, stolta | proud | Vi är så stolta över dig! | We're so proud of you!
lycklig, lyckligt, lyckliga | happy (deeply, lastingly) | De ser så lyckliga ut tillsammans. | They look so happy together.
besviken, besviket, besvikna | disappointed | Jag är lite besviken på resultatet. | I'm a bit disappointed with the result.
blyg, blygt, blyga | shy | Hennes son är lite blyg. | Her son is a bit shy.
""",
        ["feelings"],
    )
)

KA = "kommer att"

VERBS = [
    # perfekt
    verb("glömma", "to forget", [], group="2a", fut=KA,
         example="Jag har glömt min plånbok hemma.", example_en="I've left my wallet at home."),
    verb("använda", "to use", [], group="2a",
         example="Får jag använda din dator?", example_en="Can I use your computer?"),
    verb("städa", "to clean, to tidy", ["home"], group="1",
         example="Vi städar lägenheten på lördagar.", example_en="We clean the flat on Saturdays."),
    verb("tvätta", "to wash", [], group="1",
         example="Jag måste tvätta mina kläder.", example_en="I need to wash my clothes."),
    verb("diska", "to do the washing-up", ["home"], group="1",
         example="Jag lagar mat och du diskar.", example_en="I cook and you do the washing-up."),
    verb("handla", "to shop, to buy food", ["shopping"], group="1",
         example="Jag handlar på vägen hem.", example_en="I'll do the shopping on the way home."),
    # preteritum
    verb("ringa", "to call, to phone", [], group="2a",
         example="Jag ringer dig i kväll.", example_en="I'll call you tonight."),
    verb("höra", "to hear", [], group="2a", fut=KA,
         example="Hör du vad hon säger?", example_en="Can you hear what she's saying?"),
    verb("träffa", "to meet", [], group="1",
         example="Jag träffade min fru på universitetet.", example_en="I met my wife at university."),
    verb("byta", "to change, to swap", [], group="2b",
         example="Vi måste byta tåg i Hallsberg.", example_en="We have to change trains in Hallsberg."),
    verb("låna", "to borrow; to lend", [], group="1",
         example="Kan jag låna din penna?", example_en="Can I borrow your pen?"),
    verb("visa", "to show", [], group="1",
         example="Kan du visa mig vägen?", example_en="Can you show me the way?"),
    # strong verbs
    verb("springa", "to run", [], group="4", pres="springer", pret="sprang", sup="sprungit",
         example="Han springer fem kilometer varje morgon.", example_en="He runs five kilometres every morning."),
    verb("sjunga", "to sing", [], group="4", pres="sjunger", pret="sjöng", sup="sjungit",
         example="Alla sjunger på midsommar.", example_en="Everyone sings at midsummer."),
    verb("flyga", "to fly", ["travel"], group="4", pres="flyger", pret="flög", sup="flugit",
         example="Vi flyger till Luleå i morgon.", example_en="We're flying to Luleå tomorrow."),
    verb("bära", "to carry", [], group="4", pres="bär", pret="bar", sup="burit",
         example="Kan du hjälpa mig att bära väskan?", example_en="Can you help me carry the bag?"),
    verb("vinna", "to win", [], group="4", pres="vinner", pret="vann", sup="vunnit",
         example="Vem vann matchen i går?", example_en="Who won the match yesterday?"),
    verb("bli", "to become, to get", [], group="4", pres="blir", pret="blev", sup="blivit",
         example="Det blir kallt i kväll.", example_en="It's going to get cold tonight."),
    # reflexive
    verb("klä på sig", "to get dressed", ["reflexiva-verb", "partikelverb"], group="3",
         example="Barnen klär på sig själva nu.", example_en="The children dress themselves now."),
    verb("sätta sig", "to sit down", ["reflexiva-verb"], group="4", pres="sätter", pret="satte", sup="satt",
         example="Sätt dig här bredvid mig.", example_en="Sit here next to me."),
    verb("lägga sig", "to lie down; to go to bed", ["reflexiva-verb"], group="4",
         pres="lägger", pret="la", sup="lagt",
         example="Jag lägger mig tidigt i kväll.", example_en="I'm going to bed early tonight."),
    verb("skynda sig", "to hurry", ["reflexiva-verb"], group="1",
         example="Skynda dig, bussen går snart!", example_en="Hurry up, the bus is leaving soon!"),
    verb("gifta sig", "to get married", ["reflexiva-verb"], group="2b",
         example="De ska gifta sig i juni.", example_en="They're getting married in June."),
    verb("lära sig", "to learn", ["reflexiva-verb"], group="2a",
         example="Jag lär mig svenska på kvällarna.", example_en="I'm learning Swedish in the evenings."),
    verb("känna sig", "to feel", ["reflexiva-verb"], group="2a", fut=KA,
         example="Hur känner du dig i dag?", example_en="How are you feeling today?"),
    # particle verbs
    verb("tycka om", "to like", ["partikelverb"], group="2b", fut=KA,
         example="Jag tycker om att läsa.", example_en="I like reading."),
    verb("hälsa på", "to visit (someone)", ["partikelverb"], group="1",
         example="Vi hälsar på mormor i helgen.", example_en="We're visiting Grandma at the weekend."),
    verb("ta med", "to bring, to take along", ["partikelverb"], group="4", pres="tar", pret="tog", sup="tagit",
         example="Ta med en tröja, det blir kallt.", example_en="Bring a jumper, it'll get cold."),
    verb("stänga av", "to switch off", ["partikelverb"], group="2a",
         example="Stäng av telefonen under filmen.", example_en="Switch your phone off during the film."),
    verb("sätta på", "to switch on; to put on", ["partikelverb"], group="4",
         pres="sätter", pret="satte", sup="satt",
         example="Kan du sätta på kaffet?", example_en="Can you put the coffee on?"),
    verb("komma ihåg", "to remember", ["partikelverb"], group="4", pres="kommer", pret="kom", sup="kommit",
         example="Kommer du ihåg hennes namn?", example_en="Do you remember her name?"),
    verb("hålla med", "to agree", ["partikelverb"], group="4", pres="håller", pret="höll", sup="hållit",
         fut=KA,
         example="Jag håller inte med dig.", example_en="I don't agree with you."),
    # modal and helper verbs
    verb("behöva", "to need", [], group="2a", fut=KA,
         example="Behöver du hjälp?", example_en="Do you need any help?"),
    verb("bruka", "to usually (do)", [], group="1", fut=KA,
         example="Vi brukar äta middag klockan sex.", example_en="We usually have dinner at six."),
    verb("hinna", "to have time to, to make it", [], group="4", pres="hinner", pret="hann", sup="hunnit",
         fut=KA,
         example="Hinner vi äta innan filmen?", example_en="Do we have time to eat before the film?"),
    verb("orka", "to have the energy to", [], group="1", fut=KA,
         example="Jag orkar inte städa i dag.", example_en="I can't face cleaning today."),
    verb("våga", "to dare", [], group="1", fut=KA,
         example="Vågar du hoppa i vattnet?", example_en="Do you dare jump into the water?"),
    verb("slippa", "to not have to, to get out of", [], group="4", pres="slipper", pret="slapp",
         sup="sluppit", fut=KA,
         example="I morgon slipper jag jobba.", example_en="Tomorrow I don't have to work."),
    # s-verbs
    verb("hoppas", "to hope", ["s-verb"], group="1", pres="hoppas", pret="hoppades", sup="hoppats", fut=KA,
         example="Jag hoppas att vädret blir fint.", example_en="I hope the weather's nice."),
    verb("minnas", "to remember", ["s-verb"], group="2a", pres="minns", pret="mindes", sup="mints", fut=KA,
         example="Minns du vår första dag här?", example_en="Do you remember our first day here?"),
    verb("trivas", "to like it (somewhere), to feel at home", ["s-verb"], group="2a",
         pres="trivs", pret="trivdes", sup="trivts", fut=KA,
         example="Jag trivs jättebra i Uppsala.", example_en="I really like living in Uppsala."),
    verb("lyckas", "to succeed, to manage", ["s-verb"], group="1",
         pres="lyckas", pret="lyckades", sup="lyckats", fut=KA,
         example="Lyckades du hitta nycklarna?", example_en="Did you manage to find the keys?"),
    verb("andas", "to breathe", ["s-verb"], group="1", pres="andas", pret="andades", sup="andats",
         example="Andas lugnt och djupt.", example_en="Breathe slowly and deeply."),
    verb("finnas", "to exist; there is", ["s-verb"], group="4", pres="finns", pret="fanns", sup="funnits",
         fut=KA,
         example="Finns det en bankomat här i närheten?", example_en="Is there a cash machine near here?"),
]

PHRASES = phrases(
    """
i morgon | tomorrow | Jag börjar mitt nya jobb i morgon. | I start my new job tomorrow.
i övermorgon | the day after tomorrow | Paketet kommer i övermorgon. | The parcel arrives the day after tomorrow.
nästa vecka | next week | Nästa vecka har jag semester. | I'm on holiday next week.
nästa år | next year | Nästa år vill vi resa till Japan. | Next year we want to go to Japan.
om en stund | in a while, in a bit | Maten är klar om en stund. | The food will be ready in a bit.
i framtiden | in the future | I framtiden vill jag bo på landet. | In the future I'd like to live in the country.
i går | yesterday | I går regnade det hela dagen. | It rained all day yesterday.
i förrgår | the day before yesterday | Jag träffade henne i förrgår. | I met her the day before yesterday.
i morse | this morning (it's over) | I morse missade jag bussen. | This morning I missed the bus.
i somras | last summer | I somras badade vi varje dag. | Last summer we swam every day.
förra veckan | last week | Förra veckan var jag sjuk. | I was ill last week.
för länge sedan | a long time ago | Det hände för länge sedan. | It happened a long time ago.
""",
    ["time"],
) + phrases(
    """
det regnar | it's raining | Det regnar, ta med dig ett paraply. | It's raining, take an umbrella.
vad synd | what a pity | Kan du inte komma? Vad synd! | You can't come? What a pity!
det beror på | it depends | Kommer du? Det beror på vädret. | Are you coming? It depends on the weather.
ingen aning | no idea | Var är Erik? Ingen aning. | Where's Erik? No idea.
jag skulle vilja ha | I'd like | Jag skulle vilja ha en kaffe, tack. | I'd like a coffee, please. | I should want to have | The polite way to order. *Jag vill ha* sounds blunt.
kan jag få | could I have | Kan jag få notan, tack? | Could I have the bill, please? | can I get
jag har ont i | my ... hurts | Jag har ont i knät efter löpningen. | My knee hurts after the run. | I have pain in
krya på dig | get well soon | Krya på dig! Vi saknar dig på jobbet. | Get well soon! We miss you at work.
jag mår illa | I feel sick | Stanna bilen, jag mår illa! | Stop the car, I feel sick! | I feel badly
lycka till | good luck | Lycka till på provet i morgon! | Good luck in the test tomorrow! | luck to
det spelar ingen roll | it doesn't matter | Kaffe eller te? Det spelar ingen roll. | Coffee or tea? It doesn't matter. | it plays no role
ta det lugnt | take it easy | Ta det lugnt, vi hinner. | Take it easy, we've got time. | take it calm
hur gick det? | how did it go? | Du hade en intervju i dag. Hur gick det? | You had an interview today. How did it go? | how went it
det låter bra | sounds good | Pizza i kväll? Det låter bra! | Pizza tonight? Sounds good!
tack för senast | thanks for last time | Hej Lisa, tack för senast! | Hi Lisa, thanks for last time! | thanks for latest | Said the next time you see someone who invited you round or spent an evening with you. Leaving it out can seem ungrateful.
gå på bio | to go to the cinema | Ska vi gå på bio i helgen? | Shall we go to the cinema at the weekend? | go on cinema
""",
    ["expressions"],
)

CONNECTIVES = connectors(
    "connective",
    """
så | so | conn-consequence | Bussen var sen, så jag tog en taxi. | The bus was late, so I took a taxi.
därför | so, that's why | conn-consequence | Jag var sjuk och därför stannade jag hemma. | I was ill, so I stayed at home.
i stället | instead | conn-contrast | Vi tog inte bilen utan cyklade i stället. | We didn't take the car; we cycled instead.
förresten | by the way | conn-addition | Förresten, har du sett min telefon? | By the way, have you seen my phone?
till sist | in the end, finally | conn-sequence | Till sist hittade vi hotellet. | In the end we found the hotel.
efteråt | afterwards | conn-sequence | Vi åt middag och efteråt gick vi på bio. | We had dinner and afterwards we went to the cinema.
""",
    ["sambandsord"],
)

CONJUNCTIONS = connectors(
    "conjunction",
    """
medan | while | conj-subordinating | Han lagar mat medan jag dukar bordet. | He cooks while I lay the table. | Medan jag dukar bordet lagar han mat.
innan | before | conj-subordinating | Tvätta händerna innan ni äter. | Wash your hands before you eat.
om | if | conj-subordinating | Om det regnar stannar vi hemma. | If it rains, we'll stay at home. | Vi stannar hemma om det regnar.
tills | until | conj-subordinating | Vänta här tills jag kommer tillbaka. | Wait here until I come back.
""",
    ["konjunktioner"],
)

ITEMS = PAGES + interleave(PHRASES, NOUNS, VERBS, ADJECTIVES, CONNECTIVES + CONJUNCTIONS)

UNITS = [
    {
        "title": "Perfekt",
        "page_id": "sv-perfekt",
        "word_ids": ["glomma", "anvanda", "stada", "tvatta", "diska", "handla"],
    },
    {
        "title": "Preteritum",
        "page_id": "sv-preteritum",
        "word_ids": ["ringa", "hora", "traffa", "byta", "lana", "visa"],
    },
    {
        "title": "Starka verb",
        "page_id": "sv-strong-verbs",
        "word_ids": ["springa", "sjunga", "flyga", "bara", "vinna", "bli"],
    },
    {
        "title": "Framtid",
        "page_id": "sv-future",
        "word_ids": ["i-morgon", "i-overmorgon", "nasta-vecka", "nasta-ar", "om-en-stund", "i-framtiden"],
    },
    {
        "title": "Reflexiva verb",
        "page_id": "sv-reflexive-verbs",
        "word_ids": ["kla-pa-sig", "satta-sig", "lagga-sig", "skynda-sig", "gifta-sig", "lara-sig", "kanna-sig"],
    },
    {
        "title": "Partikelverb",
        "page_id": "sv-particle-verbs",
        "word_ids": ["tycka-om", "halsa-pa", "ta-med", "stanga-av", "satta-pa", "komma-ihag", "halla-med"],
    },
    {
        "title": "Modala verb",
        "page_id": "sv-modal-verbs",
        "word_ids": ["behova", "bruka", "hinna", "orka", "vaga", "slippa"],
    },
    {
        "title": "Adjektivets former",
        "page_id": "sv-adjectives",
        "word_ids": ["ren", "smutsig", "tom", "full", "oppen", "stangd"],
    },
    {
        "title": "Komparation",
        "page_id": "sv-comparatives",
        "word_ids": ["lang", "kort", "tung", "hog", "lag", "snabb"],
    },
    {
        "title": "S-verb",
        "page_id": "sv-s-verbs",
        "word_ids": ["hoppas", "minnas", "trivas", "lyckas", "andas", "finnas"],
    },
    {
        "title": "Tidsuttryck",
        "page_id": "sv-time-expressions",
        "word_ids": ["i-gar", "i-forrgar", "i-morse", "i-somras", "forra-veckan", "for-lange-sedan"],
    },
    {
        "title": "Känslor",
        "word_ids": ["arg", "nervos", "lugn", "orolig", "stolt", "lycklig", "besviken", "blyg"],
    },
    {
        "title": "Sambandsord",
        "word_ids": ["sa", "darfor", "i-stallet", "forresten", "till-sist", "efterat", "medan", "innan", "om", "tills"],
    },
]

LABELS = {
    **topic_labels(DELTA),
    "home": "Hemma",
    "family": "Familj och vänner",
    "food": "Mat",
    "adjektiv": "Adjektiv",
}

PACK = pack(
    "sv-everyday-v1",
    1,
    "sv",
    "Svenska · Vardag (A2)",
    ITEMS,
    DELTA,
    build_units(ITEMS, UNITS, LABELS, "Repetition"),
)
