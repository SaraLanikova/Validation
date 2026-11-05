from dataclasses import field

from otree.api import *
import time

class C(BaseConstants):
    NAME_IN_URL = 'enviro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession): pass
class Group(BaseGroup): pass

def likert7(label=""):
    return models.IntegerField(
        label=label,
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal,
    )

EC_ITEMS = [
    dict(field="ec_plants", label="rostliny"),
    dict(field="ec_marine", label="mořský život"),
    dict(field="ec_birds",  label="ptáky"),
    dict(field="ec_animals", label="zvířata"),
    dict(field="ec_me", label="mě"),
    dict(field="ec_lifestyle", label="můj životní styl"),
    dict(field="ec_health", label="moje zdraví"),
    dict(field="ec_future", label="moji budoucnost"),
    dict(field="ec_mypeople", label="lidi v mé zemi"),
    dict(field="ec_people", label="všechny lidi"),
    dict(field="ec_children", label="děti"),
    dict(field="ec_mychildren", label="moje děti"),
]

def likert4(label=""):
    return models.StringField(
        label=label,
        choices=["stronglyDisagree", "disagree", "agree", "stronglyAgree"],
        widget=widgets.RadioSelectHorizontal,
    )

AC_SCALE = [
    dict(value="stronglyDisagree", text="rozhodně nesouhlasím"),
    dict(value="disagree", text="nesouhlasím"),
    dict(value="agree", text="souhlasím"),
    dict(value="stronglyAgree", text="rozhodně souhlasím"),
]

AC_ITEMS = [
    dict(field="ac1", label="Ochrana životního prostředí ohrozí pracovní místa lidí, jako jsem já."),
    dict(field="ac2", label="Zákony na ochranu životního prostředí omezují mé možnosti volby a osobní svobodu."),
    dict(field="ac3", label="Čisté životní prostředí mi poskytuje lepší možnosti rekreace."),
    dict(field="ac4", label="O životní prostředí se nemusíme příliš starat, protože budoucí generace se s těmito problémy vypořádá lépe než my."),
    dict(field="ac5", label="Vliv znečištění na veřejné zdraví je horší, než si uvědomujeme."),
    dict(field="ac6", label="Znečištění, které zde vzniká, škodí lidem na celé Zemi."),
    dict(field="ac7", label="Tvrzení, že současná úroveň znečištění mění zemské klima, jsou přehnaná."),
    dict(field="ac8", label="Během několika příštích desetiletí vyhynou tisíce druhů."),
    dict(field="ac9", label="Rovnováha v přírodě je křehká a snadno narušitelná."),
    dict(field="ac10", label="Zúčastnil/a bych se demonstrace proti firmám, které poškozují životní prostředí."),
    dict(field="ac11", label="Finančně bych přispěl/a ekologickým organizacím."),
    dict(field="ac12", label="Podepsal/a bych petici na podporu přísnějších zákonů na ochranu životního prostředí."),
    dict(field="ac13", label="Vzal/a bych práci u firmy, o které bych věděl/a, že poškozuje životní prostředí."),
]

EAI_SCALE = [
    dict(value=1, text="1 (rozhodně nesouhlasím)"),
    dict(value=2, text="2"),
    dict(value=3, text="3"),
    dict(value=4, text="4"),
    dict(value=5, text="5"),
    dict(value=6, text="6"),
    dict(value=7, text="7 (rozhodně souhlasím)"),
]

EAI_ITEMS_1 = [
    dict(field="S1I2", label="Velmi rád/a chodím na výlety do přírody, například do lesů nebo na pole."),
    dict(field="S1I10", label="Myslím si, že trávit čas v přírodě je nudné."),
    dict(field="S2I2", label="Stát by měl kontrolovat míru využívání surovin, aby se zajistila jejich co nejdelší životnost."),
    dict(field="S2I10", label="Jsem proti tomu, aby stát kontroloval a reguloval způsob využívání surovin a snažil se tak prodloužit jejich životnost."),
    dict(field="S3I2", label="Rád/a bych se připojil/a k nějaké ekologické skupině a aktivně se zapojil/a."),
    dict(field="S3I4", label="Nezapojil/a bych se do činnosti ekologické organizace."),
    dict(field="S4I3", label="Jedním z nejdůležitějších důvodů, proč udržovat jezera a řeky čisté, je to, aby se lidé měli kde věnovat vodním sportům."),
    dict(field="S4I9", label="Řeky a jezera musíme udržovat čisté, abychom chránili životní prostředí, ne jako místa, kde si lidé užívají vodní sporty."),
    dict(field="S5I4", label="Moderní věda nedokáže vyřešit naše problémy se životním prostředím."),
    dict(field="S5I10", label="Moderní věda vyřeší naše problémy se životním prostředím."),
    dict(field="S6I5", label="Lidé vážně zneužívají životní prostředí."),
    dict(field="S6I9", label="Nedomnívám se, že by lidé životní prostředí vážně zneužívali."),
]

EAI_ITEMS_2 = [
    dict(field="S7I3", label="Spíše než upravenou a uspořádanou zahradu mám raději divokou a přírodní."),
    dict(field="S7I6", label="Spíše než divokou a přírodní zahradu mám mnohem raději upravenou a uspořádanou."),
    dict(field="S8I8", label="Nepatřím k lidem, kteří se snaží šetřit přírodní zdroje."),
    dict(field="S8I9", label="Kdykoli je to možné, snažím se šetřit přírodní zdroje."),
    dict(field="S9I2", label="Lidé byli stvořeni nebo se vyvinuli, aby ovládali zbytek přírody."),
    dict(field="S9I9", label="Nevěřím, že lidé byli stvořeni nebo se vyvinuli, aby ovládali zbytek přírody."),
    dict(field="S10I2", label="Ochrana pracovních míst lidí je důležitější než ochrana životního prostředí."),
    dict(field="S10I7", label="Ochrana životního prostředí je důležitější než ochrana pracovních míst lidí."),
    dict(field="S11I7", label="Je mi smutno, když vidím, jak se lesy kácejí kvůli zemědělství."),
    dict(field="S11I8", label="Není mi smutno, když vidím, jak se ničí přírodní prostředí."),
    dict(field="S12I3", label="Rodiny by měly být podporovány v tom, aby se omezily na dvě nebo méně dětí."),
    dict(field="S12I4", label="Manželský pár by měl mít tolik dětí, kolik si přeje, pokud je dokáže dostatečně zabezpečit."),
    dict(field="EAIcontrol",label="U tohoto výroku prosím označte možnost dva.")
]

def ssdo_scale(label=""):
    return models.IntegerField(
        label=label,
        choices=[1, 2, 3, 4, 5, 6, 7, 8],
        widget=widgets.RadioSelectHorizontal,
    )

SSDO_SCALE = [
    dict(value=1, text="Naprosto souhlasím"),
    dict(value=2, text="Souhlasím do velké míry"),
    dict(value=3, text="Spíše souhlasím"),
    dict(value=4, text="Tak napůl"),
    dict(value=5, text="Spíše nesouhlasím"),
    dict(value=6, text="Do velké míry nesouhlasím"),
    dict(value=7, text="Naprosto nesouhlasím"),
    dict(value=8, text="Nevím"),
]

SSDO_ITEMS = [
    dict(field="SSDO1", label="Při určování priorit musíme brát v úvahu všechny sociální skupiny."),
    dict(field="SSDO2", label="Neměli bychom usilovat o rovnocennost všech sociálních skupin."),
    dict(field="SSDO3", label="Naším cílem by měla být rovnoprávnost všech sociálních skupin."),
    dict(field="SSDO4", label="Nadřazené sociální skupiny mají dominovat podřadným skupinám."),
]

def GEBscaleA(label=""):
    return models.StringField(
        label=label,
        choices=["never", "seldom", "occasionally", "often", "very often", "NA"],
        widget=widgets.RadioSelectHorizontal,
    )

GEBpartA_SCALE = [
    dict(value="never", text="nikdy"),
    dict(value="seldom", text="zřídka"),
    dict(value="occasionally", text="příležitostně"),
    dict(value="often", text="často"),
        dict(value="very often", text="velmi často"),
    dict(value="NA", text="netýká se mě"),
]

GEBpartA_ITEMS = [
    dict(field="GEB1a", label="Do práce nebo do školy jezdím na kole nebo veřejnou dopravou."),
    dict(field="GEB2a", label="Kupuji maso, ovoce a zeleninu s ekologickou certifikací."),
    dict(field="GEB3a", label="Kupuji nápoje v plechovkách."),
    dict(field="GEB4a", label="K čištění trouby používám čisticí sprej."),
    dict(field="GEB5a", label="S praním prádla čekám, až naplním celou pračku."),
    dict(field="GEB6a", label="Do města nebo po městě jezdím autem."),
    dict(field="GEB7a", label="V zimě větrám tak, že nechávám otevřená okna a zároveň zapnuté topení."),
    dict(field="GEB8a", label="Špinavé prádlo peru bez předpírky."),
    dict(field="GEB9a", label="Po dálnici jezdím rychlostí do 100 km/h."),
    dict(field="GEB10a", label="Pokud mi v obchodě nabídnou plastovou tašku, vezmu si ji."),
    dict(field="GEB11a", label="Do blízkého okolí (okolo 30 km) cestuji veřejnou dopravou nebo na kole."),
    dict(field="GEB12a", label="Použitý papír sbírám a odevzdávám k recyklaci."),
    dict(field="GEB13a", label="Prázdné lahve odnáším do kontejneru na tříděný odpad."),
    dict(field="GEB14a", label="Upozornil/a jsem někoho na jeho neekologické chování."),
    dict(field="GEB15a", label="Finančně přispívám ekologickým organizacím."),
    dict(field="GEB16a", label="Nápoje a jiné tekutiny kupuji ve vratných láhvích."),
    dict(field="GEB17a", label="Kupuji bělený nebo barevný toaletní papír."),
    dict(field="GEB18a", label="Kupuji hotová jídla a polotovary."),
    dict(field="GEB19a", label="Kupuji výrobky v obalech, které lze znovu naplnit."),
    dict(field="GEB20a", label="Kupuji nábytek z tuzemského dřeva."),
    dict(field="GEB21a", label="Bojkotuji společnosti s neekologickým přístupem."),
    dict(field="GEB22a", label="Kupuji sezónní ovoce a zeleninu."),
    dict(field="GEBcontrol", label="U tohoto výroku prosím označte odpověď často."),
    dict(field="GEB23a", label="Používám sušičku prádla."),
    dict(field="GEB24a", label="Čtu si informace o tématech životního prostředí."),
    dict(field="GEB25a", label="Bavím se s přáteli o znečištění životního prostředí, změně klimatu a/nebo spotřebě energie."),
    dict(field="GEB26a", label="Na delší cesty (více než 6 hodin jízdy autem) létám letadlem."),
    dict(field="GEB27a", label="Při čekání před železničním přejezdem nebo v dopravní zácpě nechávám běžet motor."),
    dict(field="GEB28a", label="Když stojím na červenou na semaforu, nechávám běžet motor."),
    dict(field="GEB29a", label="Hubím hmyz chemickými insekticidy."),
    dict(field="GEB30a", label="V zimě ztlumuji topení, pokud odcházím z bytu na více než 4 hodiny."),
    dict(field="GEB31a", label="Na místa, kde začínám pěší túry, dojíždím autem."),
    dict(field="GEB32a", label="Sprchuji se (místo koupání ve vaně)."),
]

def GEBscaleB(label=""):
    return models.StringField(
        label=label,
        choices=["yes", "no", "NA"],
        widget=widgets.RadioSelectHorizontal,
    )
GEBpartB_SCALE = [
    dict(value="yes", text="ano"),
    dict(value="no", text="ne"),
    dict(value="NA", text="netýká se mě"),
]

GEBpartB_ITEMS = [
    dict(field="GEB1b", label="Nákupní tašky používám opakovaně."),
    dict(field="GEB2b", label="V zimě topím natolik, abych nemusel/a nosit svetr."),
    dict(field="GEB3b", label="Při praní prádla používám aviváž."),
    dict(field="GEB4b", label="Vybité baterie vyhazuji do běžného odpadu."),
    dict(field="GEB5b", label="Po jídle splachuji zbytky jídla do záchodu."),
    dict(field="GEB6b", label="V koupelně používám chemické osvěžovače vzduchu."),
    dict(field="GEB7b", label="Jsem členem/členkou ekologické organizace."),
    dict(field="GEB8b", label="V hotelu si nechávám měnit ručníky každý den."),
    dict(field="GEB9b", label="Mám energeticky úspornou myčku nádobí (energetická třída A+ nebo vyšší)."),
    dict(field="GEB10b", label="Po pikniku zanechávám místo stejně čisté, jako bylo původně."),
    dict(field="GEB11b", label="Vlastním solární panely."),
    dict(field="GEB12b", label="Zjišťoval/a jsem si výhody a nevýhody pořízení vlastního solárního zdroje energie."),
    dict(field="GEB13b", label="U svého dodavatele energie mám sjednaný odběr energie z obnovitelných zdrojů."),
    dict(field="GEB14b", label="Záměrně nevlastním auto."),
    dict(field="GEB15b", label="Využívám spolujízdu."),
    dict(field="GEB16b", label="Jezdím tak, aby byla moje spotřeba paliva co nejnižší."),
    dict(field="GEB17b", label="Vlastním auto s nízkou spotřebou (méně než 6 litrů na 100 km)."),
    dict(field="GEB18b", label="Jsem vegetarián/ka."),
]

# ---------- ENVIRONMENTAL FOOTPRINT (Berger & Wyss, 2021; WWF calculator) ----------

def opts(*pairs):
    """turns ('code', 'text') pairs into a list of dicts for the template"""
    return [dict(value=v, text=t) for v, t in pairs]


EF_QUESTIONS = [
    # ---- FP_1: food + car km ----
    dict(field="EF1",
         text="Jak velký podíl ovoce a zeleniny, které kupujete, je sezónní?",
         hint="",
         options=opts(
             ("less_quarter", "Méně než čtvrtina"),
             ("quarter", "Přibližně čtvrtina"),
             ("half", "Přibližně polovina"),
             ("three_quarters", "Přibližně tři čtvrtiny"),
             ("almost_all", "Téměř veškeré ovoce a zelenina, které kupuji, pocházejí z místních zdrojů a jsou sezónní"),
         )),
    dict(field="EF2",
         text="Jak často pijete mléko nebo jíte mléčné výrobky, například jogurty, sýry, máslo či smetanu?",
         hint="Jedna porce odpovídá 2 dl mléka, 180 g jogurtu nebo 50 g sýra.",
         options=opts(
             ("more_4_day", "Více než 4krát denně"),
             ("2_4_day", "2–4krát denně"),
             ("1_2_day", "1–2krát denně"),
             ("4_6_week", "4–6krát týdně"),
             ("1_3_week", "1–3krát týdně"),
             ("less_1_week", "Méně než jednou týdně"),
             ("never", "Nikdy (jsem vegan/veganka nebo mám alergii)"),
         )),
    dict(field="EF3",
         text="Jak často jíte vejce nebo pokrmy obsahující vejce (například zapékaná jídla, dezerty či majonézu)?",
         hint="",
         options=opts(
             ("more_2_day", "Více než 2krát denně"),
             ("1_2_day", "1–2krát denně"),
             ("5_6_week", "5–6krát týdně"),
             ("3_4_week", "3–4krát týdně"),
             ("1_2_week", "1–2krát týdně"),
             ("never", "Nikdy (jsem vegan/veganka nebo mám alergii)"),
         )),
    dict(field="EF4",
         text="Jak často jíte pokrmy obsahující maso nebo ryby (například boloňské špagety nebo lososové závitky)?",
         hint="",
         options=opts(
             ("more_3_day", "Více než 3krát denně"),
             ("2_3_day", "2–3krát denně"),
             ("daily", "1krát denně"),
             ("4_6_week", "4–6krát týdně"),
             ("1_3_week", "1–3krát týdně"),
             ("less_1_week", "Méně než jednou týdně"),
             ("never", "Nikdy (jsem vegan/veganka nebo mám alergii)"),
         )),
    dict(field="EF5",
         text="Jaký podíl ze všech potravin, které kupujete, tvoří výrobky s certifikací, například bio, organické, MSC nebo Fairtrade?",
         hint="",
         options=opts(
             ("none", "Prakticky žádný"),
             ("quarter", "Přibližně čtvrtinu"),
             ("half", "Přibližně polovinu"),
             ("three_quarters", "Přibližně tři čtvrtiny"),
             ("all", "Vařím téměř výhradně z certifikovaných potravin"),
         )),
    dict(field="EF6",
         text="Jak často vyhazujete potraviny, protože se zkazily nebo jim uplynula trvanlivost?",
         hint="",
         options=opts(
             ("often", "Často (vyhazuji potraviny při každém nákupu)"),
             ("sometimes", "Čas od času"),
             ("never", "Prakticky nikdy"),
         )),
    dict(field="EF7",
         text="Kolik kilometrů ročně urazíte při soukromých cestách autem nebo na motocyklu (jako řidič či spolujezdec)?",
         hint="Soukromými cestami se rozumějí všechny cesty mimo pracovní dobu. "
              "Patří mezi ně dojíždění do práce a zpět, dovolené i víkendové výlety. "
              "Započítává se celková vzdálenost ujetá autem (včetně cest jako spolujezdec nebo při jízdě taxíkem). "
              "Příklady: Pokud denně dojíždíte 20 km (10 km do práce a 10 km zpět), urazíte za rok 4 700 km. "
              "Při každodenním dojíždění na vzdálenost 100 km (50 km do práce a 50 km zpět) urazíte za rok 23 500 km.",
         options=opts(
             ("more_30k", "Více než 30 000 km"),
             ("12.5k_30k", "12 500–30 000 km"),
             ("7.5k_12.5k", "7 500–12 500 km"),
             ("2k_7.5k", "2 000–7 500 km"),
             ("less_2k", "Méně než 2 000 km"),
             ("never", "Nikdy nepoužívám auto nebo motocykl"),
         )),

    # ---- FP_2: car (only if fp_car_km != 'never') ----
    dict(field="EF8",
         text="Jaký druh pohonu má auto, kterým obvykle jezdíte?",
         hint="",
         options=opts(
             ("petrol_diesel_hybrid", "Benzínový/naftový/hybridní"),
             ("natural_gas", "Zemní plyn"),
             ("biogas", "Bioplyn"),
             ("electric", "Běžná elektřina"),
             ("green_electricity", "„Zelená“ elektřina"),
         )),
    dict(field="EF9",
         text="Kolik paliva na 100 km spotřebuje auto, které obvykle používáte k soukromým cestám?",
         hint="Běžná, o něco starší auta střední třídy spotřebují přibližně 6 až 9 litrů benzinu na 100 km. Větší auta "
              "spotřebují o něco více, menší o něco méně. Méně než 4,5 l / 100 km spotřebují pouze nejúspornější "
              "současná auta střední třídy, malá auta a minivozy.",
         options=opts(
             ("more_12", "Více než 12 l (více než 32 kWh v elektrickém autě)/100 km"),
             ("9_12", "9–12 l (kolem 28 kWh v elektrickém autě)/100 km"),
             ("6_9", "6–9 l (kolem 20 kWh v elektrickém autě)/100 km"),
             ("4.5_6", "4,5–6 l (kolem 14 kWh v elektrickém autě)/100 km"),
             ("less_4.5", "Méně než 4,5 l (méně než 12 kWh v elektrickém autě)/100 km"),
             ("NA", "Nevím"),
         )),

    # ---- FP_3: public transport, travel, housing, consumption ----
    dict(field="EF10",
         text="Kolik kilometrů týdně urazíte veřejnou dopravou (vlakem, autobusem či tramvají) nebo na elektrokole? "
              "Sečtěte všechny cesty za volnočasovými aktivitami, nákupy a do práce či školy. Nezapočítávejte pracovní cesty.",
         hint="Zahrňte všechny cesty mimo práci, včetně dojíždění do práce nebo školy a zpět.",
         options=opts(
             ("more_600", "Více než 600 km"),
             ("360_600", "360–600 km"),
             ("240_359", "240–359 km"),
             ("80_239", "80–239 km"),
             ("60_79", "60–79 km"),
             ("less_60", "Méně než 60 km"),
             ("never", "Nikdy nevyužívám veřejnou dopravu"),
         )),
    dict(field="EF11",
         text="Kolik hodin strávíte v běžném roce cestováním letadlem?",
         hint="Pokud jste například před třemi lety strávil(a) deset hodin v letadle, ale v ostatních čtyřech letech jste "
              "neletěl(a), vychází Vám průměrně dvě hodiny letu ročně.",
         options=opts(
             ("more_50", "Celkem více než 50 hodin"),
             ("25_50", "Celkem 25–50 hodin"),
             ("15_24", "Celkem 15–24 hodin"),
             ("8_14", "Celkem 8–14 hodin"),
             ("2_7", "Celkem 2–7 hodin"),
             ("less_2", "Celkem méně než 2 hodiny"),
             ("never", "V posledních letech jsem letadlem necestoval(a)"),
         )),
    dict(field="EF12",
         text="Kolik dní jste v posledních pěti letech v průměru strávil(a) na výletní lodi?",
         hint="Plavbou na výletní lodi se rozumí dovolená na lodi s motorovým pohonem, která několik dní pluje po moři "
              "a cestujícím nabízí určitou úroveň pohodlí (jídlo připravované profesionálními kuchaři, zábavní program apod.).",
         options=opts(
             ("more_2_weeks", "Více než 2 týdny"),
             ("1_2_weeks", "1–2 týdny"),
             ("4_6_days", "4–6 dní"),
             ("1_3_days", "1–3 dny"),
             ("none", "V posledních pěti letech jsem nebyl(a) na výletní lodi"),
         )),

    dict(field="EFcontrol",
         text="U této otázky prosím označte možnost „1–3krát týdně“.",
         hint="",
         options=opts(
             ("several_day", "Několikrát denně"),
             ("1_day", "Jednou denně"),
             ("4_6_week", "4–6krát týdně"),
             ("1_3_week", "1–3krát týdně"),  # ← correct answer
             ("less_1_week", "Méně než jednou týdně"),
             ("never", "Nikdy"),
         )),

    dict(field="EF13",
         text="Jaký je v zimě hlavní zdroj vytápění Vašeho domu?",
         hint="",
         options=opts(
             ("oil", "Topný olej"),
             ("gas", "Zemní plyn"),
             ("oil_solar", "Topný olej v kombinaci se solárními panely"),
             ("gas_solar", "Zemní plyn v kombinaci se solárními panely"),
             ("district", "Dálkové vytápění"),
             ("electric", "Elektrické vytápění"),
             ("heat_pump", "Tepelné čerpadlo (využívající energii vzduchu, vody nebo země)"),
             ("wood_solar", "Dřevo v kombinaci se solárními panely"),
             ("wood", "Dřevo (pelety, štěpka nebo polena)"),
             ("NA", "Nevím"),
         )),
    dict(field="EF14",
         text="Jakému energetickému standardu odpovídá Váš dům?",
         hint="Pokud bylo zateplení fasády a oken vašeho domu obnoveno po roce 1980, uveďte místo roku výstavby rok renovace.",
         options=opts(
             ("before_1980", "Postaveno nebo renovováno před rokem 1980"),
             ("1980_1990", "Postaveno nebo renovováno v letech 1980–1990"),
             ("1991_2008", "Postaveno nebo renovováno v letech 1991–2008"),
             ("after_2009", "Postaveno nebo renovováno po roce 2009"),
             ("low_energy", "Nízkoenergetický dům"),
             ("passive", "Pasivní dům (dům s nejnižší spotřebou energie)"),
             ("zero_plus", "Energeticky nulový nebo energeticky plusový dům"),
             ("NA", "Nevím"),
         )),
    dict(field="EF15",
         text="Jak velký je Váš byt/dům (vytápěná obytná plocha bytu nebo domu a případného rekreačního bytu bez garáže, sklepa a půdy)?",
         hint="",
         options=opts(
             ("more_300", "Více než 300 m²"),
             ("201_300", "201–300 m²"),
             ("151_200", "151–200 m²"),
             ("126_150", "126–150 m²"),
             ("101_125", "101–125 m²"),
             ("76_100", "76–100 m²"),
             ("51_75", "51–75 m²"),
             ("30_50", "30–50 m²"),
             ("less_30", "Méně než 30 m²"),
             ("NA", "Nevím"),
         )),
    dict(field="EF16",
         text="Kolik lidí žije ve Vaší domácnosti včetně Vás?",
         hint="",
         options=opts(
             (1, "1 člověk"),
             (2, "2 osoby"),
             (3, "3 osoby"),
             (4, "4 osoby"),
             (5, "5 osob"),
             (6, "6 osob"),
             (7, "7 osob nebo více"),
         )),
    dict(field="EF17",
         text="Jaké lednice a mrazáky máte?",
         hint="",
         options=opts(
             ("multiple", "Více lednic a/nebo mrazáků"),
             ("combi", "Kombinovaná lednice s mrazákem (dvoudveřová) nebo lednice s malým mrazicím prostorem v kombinaci se samostatným mrazákem"),
             ("fridge_small_freezer", "Lednice s malým mrazicím prostorem"),
         )),
    dict(field="EF18",
         text="Jaký podíl elektřiny využívané ve vaší domácnosti tvoří „zelená“ elektřina?",
         hint="„Zelenou“ elektřinou se zde rozumí elektřina z obnovitelných zdrojů (např. ze slunce, větru či vody), "
              "kterou dodavatelé obvykle nabízejí v rámci samostatného „zeleného“ tarifu.",
         options=opts(
             ("none", "„Zelenou“ elektřinu nevyužíváme"),
             ("part", "Část elektřiny, kterou naše domácnost využívá, je „zelená“, například ze solárních panelů"),
             ("all", "Naše domácnost využívá 100 % „zelené“ elektřiny"),
             ("NA", "Nevím"),
         )),
    dict(field="EF19",
         text="Kolik měsíčně utratíte za oblečení a obuv?",
         hint="Uveďte své osobní výdaje, nebo průměrné výdaje domácnosti, pokud kupujete oblečení a obuv také dalším členům rodiny.",
         options=opts(
             ("more_5k", "Více než 5 000 Kč měsíčně"),
             ("2.5k", "Přibližně 2 500 Kč měsíčně"),
             ("2k", "Přibližně 2 000 Kč měsíčně"),
             ("1k", "Přibližně 1 000 Kč měsíčně"),
             ("less_400", "Méně než 400 Kč měsíčně"),
         )),
    dict(field="EF20",
         text="Kolik měsíčně utratíte za volný čas a kulturu (například za domácí mazlíčky, permanentku do fitness, "
              "časopisy, kino, zábavní elektroniku, předplatné či koníčky)?",
         hint="",
         options=opts(
             ("more_8k", "Více než 8 000 Kč měsíčně"),
             ("5k", "Přibližně 5 000 Kč měsíčně"),
             ("3.5k", "Přibližně 3 500 Kč měsíčně"),
             ("2k", "Přibližně 2 000 Kč měsíčně"),
             ("less_700", "Méně než 700 Kč měsíčně"),
         )),
    dict(field="EF21",
         text="Kolik měsíčně utratíte za nábytek a domácí spotřebiče?",
         hint="Odhadněte, jak dlouho budete svůj nábytek a domácí spotřebiče používat. Poté vydělte pořizovací cenu "
              "veškerého nábytku a domácích spotřebičů jejich odhadovanou životností v měsících. Větší běžné domácí "
              "spotřebiče, například lednice a pračky, by měly v průměru vydržet asi 15 let, tedy 180 měsíců.",
         options=opts(
             ("more_6k", "Více než 6 000 Kč měsíčně"),
             ("4k", "Přibližně 4 000 Kč měsíčně"),
             ("2.5k", "Přibližně 2 500 Kč měsíčně"),
             ("1.5k", "Přibližně 1 500 Kč měsíčně"),
             ("less_500", "Méně než 500 Kč měsíčně"),
         )),
    dict(field="EF22",
         text="Kolik měsíčně utratíte za jídlo v restauracích a jídelnách, jídlo s sebou a ubytování mimo domov?",
         hint="",
         options=opts(
             ("more_7k", "Více než 7 000 Kč měsíčně"),
             ("4.5k", "Přibližně 4 500 Kč měsíčně"),
             ("3k", "Přibližně 3 000 Kč měsíčně"),
             ("1k", "Přibližně 1 000 Kč měsíčně"),
             ("less_600", "Méně než 600 Kč měsíčně"),
         )),
]

EF_BY_FIELD = {q["field"]: q for q in EF_QUESTIONS}


def ef_field(name):
    """creates a Player field whose choices exactly match the options above"""
    q = EF_BY_FIELD[name]
    choices = [[o["value"], o["text"]] for o in q["options"]]
    # numeric codes (e.g. EF16) -> IntegerField, text codes -> StringField
    if all(isinstance(o["value"], int) for o in q["options"]):
        return models.IntegerField(
            label=q["text"],
            choices=choices,
            widget=widgets.RadioSelect,
        )
    return models.StringField(
        label=q["text"],
        choices=choices,
        widget=widgets.RadioSelect,
    )

class Player(BasePlayer):
    # ---- Socio ----
    participantID = models.IntegerField(label='Jaké je číslo Vašeho místa, které jste si vylosoval/a při příchodu?')
    sex = models.StringField(label='Jaké je Vaše pohlaví (úřední v okamžiku narození)?',
                             choices=[
                                ["female", "Žena"],
                                ["male", "Muž"],
                             ],
                             widget=widgets.RadioSelect,)
    age = models.IntegerField(label='Jaký je Váš věk?', min=18)
    education = models.StringField(
        label='Jaké je Vaše nejvyšší dosažené vzdělání?',
        choices=[
            ["primary", 'Základní'],
            ["secondary_without_diploma",'Střední bez maturity'],
            ["secondary_with_diploma",'Střední s maturitou'],
            ["vocational",'Vyšší odborné'],
            ["bachelor",'Vysokoškolské - bakalářské'],
            ["master",'Vysokoškolské - magisterské'],
            ["phd",'Vysokoškolské - doktorské'],
        ],
        widget=widgets.RadioSelect
    )

    region = models.StringField(
        label='V jakém kraji máte trvalé bydliště?',
        choices=[
            ["praha",'hl. m. Praha'],
            ["ustecky",'Ústecký'],
            ["stedocesky", 'Středočeský'],
            ["liberecky", 'Liberecký'],
            ["karlovasrky", 'Karlovarský'],
            ["plzensky", 'Plzeňský'],
            ["kralovehradecky", 'Královéhradecký'],
            ["pardubicky", 'Pardubický'],
            ["jihocesky", 'Jihočeský'],
            ["vysocina", 'Vysočina'],
            ["olomoucky", 'Olomoucký'],
            ["jihomoravsky", 'Jihomoravský'],
            ["zlinsky", 'Zlínský'],
            ["moravskoslezsky", 'Moravskoslezský'],
            ["out", 'mimo ČR'],
        ],
        widget=widgets.RadioSelect
    )

    economic_PO = models.IntegerField(min=-50, max=50)
    cultural_PO = models.IntegerField(min=-50, max=50)

    income = models.StringField(
        label="Kolik peněz Vám měsíčně obvykle zůstane po zaplacení pravidelných výdajů"
              " (trvalé příkazy a inkasa; typicky náklady spojené s bydlením, "
              "telefon/internet/televize, spoření, předplatné a splátky)?",
        choices=[
            ["5k","méně než 5 000 Kč"],
            ["10k", "5 001–10 000 Kč"],
            ["15k", "10 001–15 000 Kč"],
            ["20k", "15 001–20 000 Kč"],
            ["25k", "20 001–25 000 Kč"],
            ["30k", "25 001–30 000 Kč"],
            ["35k", "30 001–35 000 Kč"],
            ["m35k", "více než 35 000 Kč"],
            ["NA", "Nechci uvést"],
        ],
        widget=widgets.RadioSelect
    )

    occupation = models.StringField(
        label="Jaké je Vaše pracovní zařazení?",
        choices=[
            ["fulltime","zaměstnanec na plný úvazek"],
            ["parttime", "zaměstnanec na částečný úvazek"],
            ["entrepreneur", "podnikatel/OSVČ"],
            ["student", "student"],
            ["unemployed", "nezaměstnaný"],
            ["maternityleave", "na mateřské/rodičovské dovolené"],
            ["retiree", "důchodce"],
            ["other", "jiné"],
        ],
        widget=widgets.RadioSelect
    )

    time_socio = models.FloatField()

    # EC (2)
    ec_plants = likert7()
    ec_marine = likert7()
    ec_birds = likert7()
    ec_animals = likert7()
    ec_me = likert7()
    ec_lifestyle = likert7()
    ec_health = likert7()
    ec_future = likert7()
    ec_mypeople= likert7()
    ec_people = likert7()
    ec_children = likert7()
    ec_mychildren = likert7()

    time_EC = models.FloatField()

    # ---- AC ----
    ac1 = likert4()
    ac2 = likert4()
    ac3 = likert4()
    ac4 = likert4()
    ac5 = likert4()
    ac6 = likert4()
    ac7 = likert4()
    ac8 = likert4()
    ac9 = likert4()
    ac10 = likert4()
    ac11 = likert4()
    ac12 = likert4()
    ac13 = likert4()

    time_AC = models.FloatField()

    # ---- EAI ----
    S1I2 = likert7()
    S1I10 = likert7()
    S2I2 = likert7()
    S2I10 = likert7()
    S3I2 = likert7()
    S3I4 = likert7()
    S4I3 = likert7()
    S4I9 = likert7()
    S5I4 = likert7()
    S5I10 = likert7()
    S6I5 = likert7()
    S6I9 = likert7()
    S7I3 = likert7()
    S7I6 = likert7()
    S8I8 = likert7()
    S8I9 = likert7()
    S9I2 = likert7()
    S9I9 = likert7()
    S10I2 = likert7()
    S10I7 = likert7()
    S11I7 = likert7()
    S11I8 = likert7()
    S12I3 = likert7()
    S12I4 = likert7()
    EAIcontrol = likert7()

    time_EAI_1 = models.FloatField()
    time_EAI_2 = models.FloatField()

    # ---- GEB - part A ----
    GEB1a = GEBscaleA()
    GEB2a = GEBscaleA()
    GEB3a = GEBscaleA()
    GEB4a = GEBscaleA()
    GEB5a = GEBscaleA()
    GEB6a = GEBscaleA()
    GEB7a = GEBscaleA()
    GEB8a = GEBscaleA()
    GEB9a = GEBscaleA()
    GEB10a = GEBscaleA()
    GEB11a = GEBscaleA()
    GEB12a = GEBscaleA()
    GEB13a = GEBscaleA()
    GEB14a = GEBscaleA()
    GEB15a = GEBscaleA()
    GEB16a = GEBscaleA()
    GEB17a = GEBscaleA()
    GEB18a = GEBscaleA()
    GEB19a = GEBscaleA()
    GEB20a = GEBscaleA()
    GEB21a = GEBscaleA()
    GEB22a = GEBscaleA()
    GEBcontrol = GEBscaleA()
    GEB23a = GEBscaleA()
    GEB24a = GEBscaleA()
    GEB25a = GEBscaleA()
    GEB26a = GEBscaleA()
    GEB27a = GEBscaleA()
    GEB28a = GEBscaleA()
    GEB29a = GEBscaleA()
    GEB30a = GEBscaleA()
    GEB31a = GEBscaleA()
    GEB32a = GEBscaleA()

    time_GEBpartA = models.FloatField()

    # ---- GEB - part B ----
    GEB1b = GEBscaleB()
    GEB2b = GEBscaleB()
    GEB3b = GEBscaleB()
    GEB4b = GEBscaleB()
    GEB5b = GEBscaleB()
    GEB6b = GEBscaleB()
    GEB7b = GEBscaleB()
    GEB8b = GEBscaleB()
    GEB9b = GEBscaleB()
    GEB10b = GEBscaleB()
    GEB11b = GEBscaleB()
    GEB12b = GEBscaleB()
    GEB13b = GEBscaleB()
    GEB14b = GEBscaleB()
    GEB15b = GEBscaleB()
    GEB16b = GEBscaleB()
    GEB17b = GEBscaleB()
    GEB18b = GEBscaleB()

    time_GEBpartB = models.FloatField()

    # ---- SSDO ----
    SSDO1 = ssdo_scale()
    SSDO2 = ssdo_scale()
    SSDO3 = ssdo_scale()
    SSDO4 = ssdo_scale()

    time_SSDO = models.FloatField()

    # Enviro Footprint
    EF1 = ef_field("EF1")
    EF2 = ef_field("EF2")
    EF3 = ef_field("EF3")
    EF4 = ef_field("EF4")
    EF5 = ef_field("EF5")
    EF6 = ef_field("EF6")
    EF7 = ef_field("EF7")
    EF8 = models.StringField(blank=True)  # shown only if EF7 != "never"
    EF9 = models.StringField(blank=True)  # shown only if EF7 != "never"
    EF10 = ef_field("EF10")
    EF11 = ef_field("EF11")
    EF12 = ef_field("EF12")
    EFcontrol = ef_field("EFcontrol")
    EF13 = ef_field("EF13")
    EF14 = ef_field("EF14")
    EF15 = ef_field("EF15")
    EF16 = ef_field("EF16")
    EF17 = ef_field("EF17")
    EF18 = ef_field("EF18")
    EF19 = ef_field("EF19")
    EF20 = ef_field("EF20")
    EF21 = ef_field("EF21")
    EF22 = ef_field("EF22")

    time_EF = models.FloatField()

    # dodOtazky
    lifespan = models.IntegerField(
            label="Jakou odhadujete celkovou délku svého života?",
            choices=[
                [1, "méně než 60 let"],
                [2, "60–69 let"],
                [3, "70–79 let"],
                [4, "80–89 let"],
                [5, "90–99 let"],
                [6, "více než 99 let"],
            ],
            widget=widgets.RadioSelect,
        )

    kids = models.StringField(
        label="Kolik máte dětí?",
        choices=[
            ["0", "0"],
            ["1", "1"],
            ["2", "2"],
            ["3", "3"],
            ["4", "4"],
            ["5", "5"],
            ["6", "více než 5"],
            ["NA", "nechci uvést"],
        ],
        widget=widgets.RadioSelect,
    )

    language = models.StringField(
        label="Jaký je Váš mateřský jazyk?",
        choices=[
            ["cz", "čeština"],
            ["sk", "slovenština"],
            ["uk", "ukrajinština"],
            ["pl", "polština"],
            ["ru", "ruština"],
            ["other", "jiný"],
        ],
        widget=widgets.RadioSelect,
    )

    time_other = models.FloatField()

# PAGES
class Intro(Page): pass

class ObecneInstrukce(Page): pass

class Socio(Page):
    form_model = 'player'
    form_fields = ["participantID",'sex','age', 'education',"region","economic_PO","cultural_PO","income","occupation"]          # add all 10

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_socio = time.time()

class EC(Page):
        form_model = "player"
        form_fields = [item["field"] for item in EC_ITEMS]

        @staticmethod
        def vars_for_template(player):
            return dict(items=EC_ITEMS, scale=[1, 2, 3, 4, 5, 6, 7])

        @staticmethod
        def before_next_page(player, timeout_happened):
            player.time_EC = time.time()

class AC(Page):
    form_model = "player"
    form_fields = [item["field"] for item in AC_ITEMS]

    @staticmethod
    def vars_for_template(player):
        return dict(items=AC_ITEMS, scale=AC_SCALE)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_AC = time.time()

class EAI_Intro(Page): pass

class EAI_1(Page):
    form_model = "player"
    form_fields = [item["field"] for item in EAI_ITEMS_1]
    template_name = "enviro/EAI.html"

    @staticmethod
    def vars_for_template(player):
        return dict(items=EAI_ITEMS_1, scale=EAI_SCALE, screen=1)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_EAI_1 = time.time()


class EAI_2(Page):
    form_model = "player"
    form_fields = [item["field"] for item in EAI_ITEMS_2]
    template_name = "enviro/EAI.html"

    @staticmethod
    def vars_for_template(player):
        return dict(items=EAI_ITEMS_2, scale=EAI_SCALE, screen=2)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_EAI_2 = time.time()

class GEB_1(Page):
    form_model = "player"
    form_fields = [item["field"] for item in GEBpartA_ITEMS]
    template_name = "enviro/GEB.html"

    @staticmethod
    def vars_for_template(player):
        return dict(items=GEBpartA_ITEMS, scale=GEBpartA_SCALE, part="A", screen=1)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_GEBpartA = time.time()


class GEB_2(Page):
    form_model = "player"
    form_fields = [item["field"] for item in GEBpartB_ITEMS]
    template_name = "enviro/GEB.html"

    @staticmethod
    def vars_for_template(player):
        return dict(items=GEBpartB_ITEMS, scale=GEBpartB_SCALE, part="B", screen=2)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_GEBpartB = time.time()

class SSDO(Page):
    form_model = "player"
    form_fields = [item["field"] for item in SSDO_ITEMS]

    @staticmethod
    def vars_for_template(player):
        return dict(items=SSDO_ITEMS, scale=SSDO_SCALE)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_SSDO = time.time()

class EF_1(Page):
    form_model = "player"
    form_fields = [q["field"] for q in EF_QUESTIONS[0:9]]      # questions 1–9
    template_name = "enviro/EF.html"

    @staticmethod
    def vars_for_template(player):
        return dict(questions=EF_QUESTIONS[0:9], first=True, screen=1)

    @staticmethod
    def error_message(player, values):
        # EF8 and EF9 are required only for people who travel by car
        if values["EF7"] != "never":
            for f in ["EF8", "EF9"]:
                codes = [o["value"] for q in EF_QUESTIONS if q["field"] == f for o in q["options"]]
                if values[f] not in codes:
                    return "Odpovězte prosím na všechny otázky."

    @staticmethod
    def before_next_page(player, timeout_happened):
        # no car -> EF8 and EF9 stay empty
        if player.EF7 == "never":
            player.EF8 = None
            player.EF9 = None

class EF_3(Page):
    form_model = "player"
    form_fields = [q["field"] for q in EF_QUESTIONS[9:23]]     # questions 10–22
    template_name = "enviro/EF.html"

    @staticmethod
    def vars_for_template(player):
        return dict(questions=EF_QUESTIONS[9:23], first=False, screen=2)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_EF = time.time()

class DodOtazky(Page):
    form_model = 'player'
    form_fields = ["lifespan","kids","language"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_other = time.time()

class End(Page): pass

page_sequence = [Socio, EC, AC, EAI_1, EAI_2,
                 GEB_1, GEB_2, SSDO, EF_1, EF_3, DodOtazky]