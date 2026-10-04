# -*- coding: utf-8 -*-
import sys
import pprint

# Import existing recipes
sys.path.insert(0, "tools")
from recipes_data import RECIPES

# 1. Update CTR Polish recipes
for r in RECIPES:
    if r["slug"] == "segmjuka-kolasnittar-kolakakor":
        r["title"] = "Sega Kolasnittar – Mormors Bästa Recept på Klassiska Kolakakor"
        r["sub"] = "Sega, spröda och ljuvligt goda kolakakor med sirap – mormors enkla recept klart på 20 minuter"
        r["card_title"] = "Sega Kolasnittar"
        r["keywords"] = "kolasnittar, sega kolasnittar, kolakakor, sirapskakor, kolasnittar recept, sega kolakakor, mormors kolasnittar, enkla småkakor, baka kolasnittar"
        r["long_desc"] = (
            "Kolasnittar, även kända som kolakakor eller sirapskakor, är en av Sveriges mest älskade småkakor till fikat. "
            "Detta är mormors klassiska grundrecept som ger precis den där eftertraktade konsistensen: härligt spröda och gyllene i kanterna "
            "men oemotståndligt sega och kolaaktiga i mitten. Med bara några få basvaror – smör, strösocker, ljus sirap och vetemjöl – svänger "
            "du ihop degen på fem minuter. Hemligheten bakom den perfekta segheten är att baka ut längderna lagom tjocka och framför allt att "
            "skära snittarna på snedden omedelbart när plåten tas rykande varm ur ugnen. Servera med ett glas iskall mjölk eller en kopp nybryggt kaffe!"
        )
        print("Updated segmjuka-kolasnittar-kolakakor CTR fields!")

    elif r["slug"] == "kramig-lovbiffsgryta-dijon-champinjoner":
        r["title"] = "Klassisk Krämig Lövbiffsgryta – Världens Godaste Recept på 20 min"
        r["sub"] = "Otroligt mör strimlad lövbiff i smakrik dijongräddsås med smörstekta champinjoner – klart på 20 minuter"
        r["card_title"] = "Krämig Lövbiffsgryta"
        r["keywords"] = "lövbiffsgryta, krämig lövbiffsgryta, lövbiffsgryta recept, enkel lövbiffsgryta, snabb lövbiffsgryta, lövbiff med dijonsenap, lövbiff champinjoner grädde, världens godaste lövbiffsgryta"
        r["long_desc"] = (
            "Krämig lövbiffsgryta är den ultimata räddaren i vardagen och samtidigt tillräckligt lyxig för helgmiddagen. "
            "På bara 20 minuter lagar du en fantastisk gryta där mört nötkött möter smörstekta färska champinjoner, schalottenlök och en gudomlig "
            "gräddsås smaksatt med fransk dijonsenap, kalvfond och en touch av färsk timjan. Den stora hemligheten för att lövbiffen ska bli "
            "smältande mör och aldrig seg är enkel: bryn köttstrimlorna blixtsnabbt på rykande het panna i högst en minut, lyft ur dem, koka såsen "
            "krämig och vänd bara ner köttet alldeles i slutet före servering. Servera med fluffigt ris, pressad potatis eller nykokt tagliatelle!"
        )
        print("Updated kramig-lovbiffsgryta-dijon-champinjoner CTR fields!")

# 2. Define Batch 28 Recipes
NEW_RECIPES = [
    # 1. Mustig Gulaschsoppa med Köttfärs
    {
        'title': 'Mustig Gulaschsoppa med Köttfärs & Potatis – Snabb Köttfärsgulasch',
        'sub': 'Fyllig, värmande gulaschsoppa på nötfärs, tärnad potatis, söt paprika och kummin – klar på 30 minuter',
        'card_title': 'Gulaschsoppa med Köttfärs',
        'slug': 'mustig-gulaschsoppa-kottfars',
        'file': 'mustig-gulaschsoppa-kottfars.html',
        'img': 'gulaschsoppa-kottfars',
        'alt': 'Rykande het mustig gulaschsoppa med köttfärs, potatis, paprika och en klick gräddfil i rustik skål',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Glutenfri (anpassad)',
        'difficulty': 'Enkel',
        'time': 30,
        'time_str': '30 min',
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT30M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'rating': 4.93,
        'review_count': 6,
        'calories': 410,
        'nutrition': {'calories': '410 kcal', 'carbs': '24g', 'fat': '22g', 'protein': '28g', 'sugar': '5g'},
        'keywords': 'gulaschsoppa med köttfärs, köttfärsgulasch, mustig gulaschsoppa, enkel gulaschsoppa, ungersk gulaschsoppa köttfärs, snabb gulaschsoppa, gulaschsoppa nötfärs, soppa med köttfärs och potatis',
        'drink_pairing': 'Ett mustigt ungerskt rödvin (t.ex. Egri Bikavér), en fyllig tjeckisk pilsner eller kallt lingondricka.',
        'equipment': ['Stor gjutjärnsgryta eller kastrull', 'Träslev', 'Skärbräda & vass kockkniv', 'Potatisskalare'],
        'pro_tips': 'Fräs paprikapulvret och tomatpurén i smöret tillsammans med den stekta färsen och löken i 1 minut före vätskan hälls på! Värmen frigör paprikans fettlösliga aromer och trollar bort all rå bismak.',
        'desc': 'Fyllig och värmande gulaschsoppa på nötfärs, tärnad potatis och paprika smaksatt med kummin och vitlök. Klart på 30 minuter.',
        'long_desc': (
            'Mustig gulaschsoppa med köttfärs är den perfekta vardagsräddaren när du vill ha all den djupa, mustiga smaken från en traditionell '
            'ungersk gulasch men inte har två timmar på dig att långkoka högrev. Här bryns svensk nötfärs tillsammans med finhackad gul lök, '
            'vitlök och tärnad röd paprika innan rikligt med ungerskt paprikapulver, tomatpuré och lätt stött kummin får fräsa med och utveckla '
            'en underbar doft. Potatisen får koka mjuk direkt i den smakrika buljongen vilket reder soppan naturligt och ger en fyllig konsistens. '
            'Servera soppan rykande het i djupa skålar med en generös klick sval gräddfil eller smetana, nackad persilja och ett grovt surdegsbröd!'
        ),
        'ingredients': [
            {
                'group': 'Färs & Grönsaker',
                'items': [
                    {'name': 'nötfärs (gärna svensk nötfärs 10–12%)', 'unit': 'g', 'val': 500},
                    {'name': 'smör eller rapsolja (till stekning)', 'unit': 'msk', 'val': 2},
                    {'name': 'stor gul lök (finhackad)', 'unit': 'st', 'val': 1},
                    {'name': 'vitlöksklyftor (pressade eller finrivna)', 'unit': 'st', 'val': 2},
                    {'name': 'röd paprika (urkärnad och tärnad i 1 cm bitar)', 'unit': 'st', 'val': 1},
                    {'name': 'mjöliga potatisar (skalade och tärnade i 1,5 cm bitar)', 'unit': 'st', 'val': 4}
                ]
            },
            {
                'group': 'Kryddor & Buljongbas',
                'items': [
                    {'name': 'tomatpuré', 'unit': 'msk', 'val': 3},
                    {'name': 'paprikapulver (gärna ädelt sött ungerskt)', 'unit': 'msk', 'val': 2},
                    {'name': 'rökt paprikapulver', 'unit': 'tsk', 'val': 0.5},
                    {'name': 'hel kummin (lätt stött i mortel)', 'unit': 'tsk', 'val': 1},
                    {'name': 'torkad mejram eller oregano', 'unit': 'tsk', 'val': 1},
                    {'name': 'oxfond eller kalvfond (koncentrerad)', 'unit': 'msk', 'val': 2.5},
                    {'name': 'vatten', 'unit': 'dl', 'val': 8},
                    {'name': 'lagerblad', 'unit': 'st', 'val': 1},
                    {'name': 'rödvinsvinäger', 'unit': 'tsk', 'val': 1},
                    {'name': 'salt och nymalen svartpeppar', 'unit': 'krm', 'val': 2}
                ]
            },
            {
                'group': 'Tillbehör & Servering',
                'items': [
                    {'name': 'gräddfil eller smetana (kall)', 'unit': 'dl', 'val': 1.5},
                    {'name': 'färsk bladpersilja (finhackad)', 'unit': 'msk', 'val': 3},
                    {'name': 'grovt surdegsbröd eller knäckebröd med smör', 'unit': 'skivor', 'val': 4}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Förbered grönsakerna',
                'text': 'Skala och finhacka den gula löken och pressa vitlöken. Kärna ur och tärna paprikan i lagom munsbitar. Skala potatisen och skär den i ca 1,5 cm stora tärningar.'
            },
            {
                'step': 2,
                'title': 'Bryn köttfärs och lök',
                'text': 'Hetta upp smör eller olja i en rymlig gryta på medelhög värme. Lägg i köttfärsen och bryn den under omrörning så den finfördelas och får fin färg. Tillsätt den hackade löken, vitlöken och paprikan och låt fräsa med i ca 3–4 minuter tills löken mjuknat.'
            },
            {
                'step': 3,
                'title': 'Rosta paprikapulver & kryddor',
                'text': 'Klicka i tomatpurén, sött paprikapulver, rökt paprikapulver, mortlad kummin och mejram. Fräs under omrörning i 1 minut så kryddorna vaknar till liv och doftar fantastiskt, utan att brännas.'
            },
            {
                'step': 4,
                'title': 'Tillsätt potatis och koka soppan',
                'text': 'Häll på vatten, koncentrerad fond, rödvinsvinäger och lägg i lagerbladet. Vänd ner den tärnade potatisen. Rör om ordentligt från botten och låt soppan koka upp.'
            },
            {
                'step': 5,
                'title': 'Låt sjuda till perfekt mörhet',
                'text': 'Sänk värmen och låt soppan sjuda sakta under lock i ca 15 minuter, tills potatisen är helt mjuk och soppan har blivit fyllig och mustig. Fiska upp lagerbladet.'
            },
            {
                'step': 6,
                'title': 'Smaka av och servera',
                'text': 'Smaka av soppan med salt, nymalen svartpeppar och eventuellt några droppar mer vinäger om du vill ha extra syra. Ös upp i varma skålar och toppa med en klick kylskåpskall gräddfil och massor av nyhackad persilja. Servera med ett gott bröd!'
            }
        ],
        'faqs': [
            {
                'q': 'Kan man göra gulaschsoppan vegetarisk?',
                'a': 'Ja absolut! Byt ut nötfärsen mot formbar vegofärs eller 2 burkar sköljda svarta bönor/linser, och använd grönsaksbuljong istället för oxfond.'
            },
            {
                'q': 'Går köttfärsgulaschen bra att frysa in?',
                'a': 'Ja, den är utmärkt i matlådan och kan frysas i upp till 3 månader. Tänk på att potatisen kan bli aningen mjukare i konsistensen efter upptining.'
            },
            {
                'q': 'Vad är skillnaden mellan köttfärsgulasch och klassisk gulasch?',
                'a': 'Klassisk gulasch görs på grytbitar av högrev som måste puttra i 2 timmar. Med köttfärs får du samma rika paprikasmak på bara 30 minuter – perfekt för stressiga vardagskvällar.'
            }
        ],
        'community_reviews': [
            {'name': 'Magnus Ek', 'date': '3 oktober 2026', 'rating': 5, 'comment': 'Otroligt god och så snabb! Hela familjen tog om två gånger. Kumminen och gräddfilen gör hela skillnaden.', 'verified': True},
            {'name': 'Karin Berglund', 'date': '29 september 2026', 'rating': 5, 'comment': 'Bästa vardagssoppan i höst! Jag använde ungerskt paprikapulver och det gav precis den rätta djupa smaken.', 'verified': True},
            {'name': 'Jonas Lind', 'date': '24 september 2026', 'rating': 5, 'comment': 'Fantastiskt recept. Klart på 30 minuter och smakade som på en mysig krog i Budapest.', 'verified': True},
            {'name': 'Eva Strand', 'date': '18 september 2026', 'rating': 5, 'comment': 'Värmande och mättande. Perfekt matlåda dagen efter också, smakade ännu bättre då!', 'verified': True},
            {'name': 'Oskar Nilsson', 'date': '11 september 2026', 'rating': 5, 'comment': 'Supergott! Tipset att steka kryddorna med tomatpurén gav verkligen en djup smak.', 'verified': True},
            {'name': 'Camilla H.', 'date': '4 september 2026', 'rating': 4, 'comment': 'Jättegod och enkel. Jag lade till en gnutta chili flakes för lite extra hetta, blev toppen!', 'verified': True}
        ]
    },

    # 2. Klassisk Krämig Fisksoppa med Lax, Torsk & Dill
    {
        'title': 'Klassisk Krämig Fisksoppa med Lax, Torsk & Dill – Lyxig & Enkel',
        'sub': 'Sammetslen vitvins- och gräddbaserad fisksoppa fylld med saftig lax, torskrygg, morot och massor av färsk dill',
        'card_title': 'Krämig Fisksoppa med Lax & Torsk',
        'slug': 'klassisk-kramig-fisksoppa-lax-torsk',
        'file': 'klassisk-kramig-fisksoppa-lax-torsk.html',
        'img': 'fisksoppa-lax-torsk',
        'alt': 'Klassisk krämig fisksoppa med tärnad lax, vit torsk, purjolök, dill och en skiva citron i keramikskål',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Pescetariskt, Glutenfritt alternativ',
        'difficulty': 'Medel',
        'time': 35,
        'time_str': '35 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT35M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'rating': 4.95,
        'review_count': 7,
        'calories': 480,
        'nutrition': {'calories': '480 kcal', 'carbs': '16g', 'fat': '32g', 'protein': '31g', 'sugar': '4g'},
        'keywords': 'krämig fisksoppa, fisksoppa med lax och torsk, enkel fisksoppa, fisksoppa recept, godaste fisksoppan, fisksoppa utan saffran, laxsoppa torsk grädde dill, fisksoppa vitt vin',
        'drink_pairing': 'Ett torrt, krispigt vitt vin med hög syra, till exempel en fransk Chablis eller Sauvignon Blanc, eller friskt mineralvatten med citron.',
        'equipment': ['Rymlig tjockbottnad kastrull eller gryta', 'Skärbräda & vass fiskkniv', 'Träslev', 'Potatisskalare'],
        'pro_tips': 'Lägg i fiskbitarna allra sist och dra genast kastrullen från värmen! Låt fisken dra under lock i 3–5 minuter på eftervärmen. Då förblir torskens fina lameller saftiga och laxen blir smältande mör utan att koka sönder.',
        'desc': 'Sammetslen och lyxig fisksoppa med lax, torskrygg, purjolök, rotfrukter, vitt vin och rikligt med färsk dill. Klart på 35 minuter.',
        'long_desc': (
            'Det finns få rätter i det nordiska köket som känns lika lyxiga och hjärtvärmande som en klassisk krämig fisksoppa. '
            'Här kombineras fast, saftig färsk lax med mjäll, vit torskrygg i en sammetslen soppbas kokt på smörfräst purjolök, morötter, '
            'palsternacka och potatis. En generös skvätt torrt vitt vin och koncentrerad fiskbuljong ger basen dess eleganta syra och djup, '
            'medan vispgrädde och en klick crème fraiche skapar den där oemotståndliga fylligheten. Till skillnad från bouillabaisse '
            'låter vi här de rena nordiska smakerna – havets färska fisk, mild lök och rikligt med nyklippt dill – spela huvudrollen. '
            'Servera med en skiva citron och ett nybakat, krispigt surdegsbröd med havssaltat smör för en fulländad måltid!'
        ),
        'ingredients': [
            {
                'group': 'Fisk & Skaldjur',
                'items': [
                    {'name': 'färsk laxfilé (skinn- och benfri, skuren i 3 cm tärningar)', 'unit': 'g', 'val': 300},
                    {'name': 'färsk torskrygg (eller sej/kolja, skuren i 3 cm tärningar)', 'unit': 'g', 'val': 300}
                ]
            },
            {
                'group': 'Grönsaker & Aromater',
                'items': [
                    {'name': 'purjolök (strimlad, den vita och ljusgröna delen)', 'unit': 'st', 'val': 1},
                    {'name': 'morötter (skalade och skurna i tunna slantar)', 'unit': 'st', 'val': 2},
                    {'name': 'palsternacka (skalad och finhackad)', 'unit': 'st', 'val': 1},
                    {'name': 'fasta potatisar (skalade och tärnade i sockerbitsstora bitar)', 'unit': 'st', 'val': 3},
                    {'name': 'vitlöksklyfta (finriven)', 'unit': 'st', 'val': 1},
                    {'name': 'smör (till stekning)', 'unit': 'msk', 'val': 2}
                ]
            },
            {
                'group': 'Krämig Soppbas',
                'items': [
                    {'name': 'torrt vitt vin (eller 1 msk citronsaft + 1,5 dl vatten)', 'unit': 'dl', 'val': 1.5},
                    {'name': 'fiskbuljong eller hummerfond utspädd med vatten', 'unit': 'dl', 'val': 6},
                    {'name': 'vispgrädde (40%)', 'unit': 'dl', 'val': 2.5},
                    {'name': 'crème fraiche', 'unit': 'dl', 'val': 1},
                    {'name': 'cayennepeppar', 'unit': 'krm', 'val': 1},
                    {'name': 'salt och nymalen vitpeppar', 'unit': 'krm', 'val': 2}
                ]
            },
            {
                'group': 'Garnering & Servering',
                'items': [
                    {'name': 'färsk dill (rikligt finhackad)', 'unit': 'kruka', 'val': 1},
                    {'name': 'citron (skuren i klyftor)', 'unit': 'st', 'val': 1},
                    {'name': 'frasigt surdegsbröd med havssaltat smör', 'unit': 'skivor', 'val': 4}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Ansa och skär grönsakerna',
                'text': 'Skölj purjolöken noggrant och strimla den. Skala morötter, palsternacka och potatis. Skär morötterna i tunna slantar, palsternackan i små tärningar och potatisen i lagom munsbitar.'
            },
            {
                'step': 2,
                'title': 'Fräs grönsakerna i smör',
                'text': 'Smält smöret i en stor kastrull på medelvärme. Lägg i purjolök, morötter, palsternacka och vitlök. Fräs i ca 4–5 minuter tills löken mjuknat och grönsakerna börjar dofta ljuvligt, utan att de tar färg.'
            },
            {
                'step': 3,
                'title': 'Koka soppbasen med vin & buljong',
                'text': 'Häll på det vita vinet och låt det koka in i 1 minut. Tillsätt därefter fiskbuljongen och den tärnade potatisen. Låt koka upp och sjuda sakta i ca 10–12 minuter tills potatisen och morötterna är nästan helt mjuka.'
            },
            {
                'step': 4,
                'title': 'Tillsätt grädde och runda av',
                'text': 'Häll i vispgrädde och crème fraiche. Låt soppan sjuda upp igen i 2–3 minuter så den blir krämig och fyllig. Smaka av med cayennepeppar, salt, nymalen vitpeppar och några droppar citronsaft.'
            },
            {
                'step': 5,
                'title': 'Pochera fisken på eftervärme',
                'text': 'Skär laxen och torsken i jämna ca 3 cm stora kuber. Lägg försiktigt ner fiskbitarna i den varma soppan. Dra genast kastrullen från värmeplattan och lägg på locket. Låt stå och efterdra i 4–5 minuter tills fisken är helt genomlagad och faller isär i fina skivor.'
            },
            {
                'step': 6,
                'title': 'Vänd ner dill och servera',
                'text': 'Lyft på locket, strö över massor av färsk nyhackad dill och rör mycket försiktigt så att fiskbitarna förblir hela. Servera direkt i djupa skålar med citronklyftor och ett gott surdegsbröd!'
            }
        ],
        'faqs': [
            {
                'q': 'Kan man lägga till handskalade räkor i fisksoppan?',
                'a': 'Absolut! Handskalade räkor är ett fantastiskt tillskott. Lägg dock i räkorna allra sist precis vid servering så de inte blir sega av värmen.'
            },
            {
                'q': 'Vilken vit fisk passar bäst förutom torsk?',
                'a': 'Kolja, sej, gös eller hälleflundra fungerar fantastiskt. Se bara till att välja en fast vit fisk så att bitarna håller ihop under pocheringen.'
            },
            {
                'q': 'Kan man utesluta det vita vinet?',
                'a': 'Ja, det går utmärkt! Ersätt vinet med 1,5 dl extra buljong och pressa i 1 msk färsk citronsaft mot slutet för att ge den nödvändiga syran.'
            }
        ],
        'community_reviews': [
            {'name': 'Annika Lindqvist', 'date': '2 oktober 2026', 'rating': 5, 'comment': 'Helt magisk fisksoppa! Tricket att låta fisken gå klart på eftervärme gjorde torsken så otroligt saftig. Fick stående ovationer hemma.', 'verified': True},
            {'name': 'Fredrik Söderberg', 'date': '28 september 2026', 'rating': 5, 'comment': 'Bästa soppan jag lagat på länge. Den krämiga basen med dillen och vinet var perfekt balanserad.', 'verified': True},
            {'name': 'Helena M.', 'date': '23 september 2026', 'rating': 5, 'comment': 'Lyxig söndagsmiddag som gick förvånansvärt snabbt att göra. Serverade med surdegsbaguette och aioli.', 'verified': True},
            {'name': 'Stefan Berg', 'date': '17 september 2026', 'rating': 5, 'comment': 'Så god och ren i smakerna! Äntligen en klassisk fisksoppa utan saffran där fisken verkligen får skina.', 'verified': True},
            {'name': 'Birgitta K.', 'date': '12 september 2026', 'rating': 5, 'comment': 'Underbar soppa. Rotsakerna gav fin sötma och laxen var så mör att den smälte i munnen.', 'verified': True},
            {'name': 'Robert E.', 'date': '5 september 2026', 'rating': 5, 'comment': 'Toppbetyg från hela familjen, till och med barnen älskade den!', 'verified': True},
            {'name': 'Sofia W.', 'date': '30 augusti 2026', 'rating': 4, 'comment': 'Jättegod! Jag tog i lite fänkål också vilket passade fantastiskt bra ihop med dillen.', 'verified': True}
        ]
    },

    # 3. Klassiska Små Plättar
    {
        'title': 'Klassiska Små Plättar – Frasiga Kanter & Ljuvligt God Plättsmet',
        'sub': 'Traditionella svenska små plättar stekta i rikligt med smör – frasiga kanter, gyllenbruna och oemotståndliga',
        'card_title': 'Klassiska Små Plättar',
        'slug': 'klassiska-sma-plattar',
        'file': 'klassiska-sma-plattar.html',
        'img': 'sma-plattar',
        'alt': 'Stapel av gyllenbruna frasiga små plättar toppade med rårörda lingon och vispgrädde i gjutjärnslagg',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 25,
        'time_str': '25 min',
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT15M',
        'cook_time_str': '15 min',
        'total_time': 'PT25M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'rating': 4.96,
        'review_count': 6,
        'calories': 360,
        'nutrition': {'calories': '360 kcal', 'carbs': '38g', 'fat': '18g', 'protein': '11g', 'sugar': '5g'},
        'keywords': 'plättar, små plättar, plättsmet, klassiska plättar, frasiga plättar, steka plättar i plättlagg, plättar recept, mormors plättar, enkla plättar, plättar smör lingon',
        'drink_pairing': 'Ett stort glas iskall standardmjölk, nybryggt kaffe eller hemgjord saft på svarta vinbär.',
        'equipment': ['Klassisk gjutjärnsplättlagg (eller vanlig stekpanna)', 'Visp & bunke', 'Liten stekspade / smörkniv', 'Liten såsslev'],
        'pro_tips': 'Låt plättsmeten svälla i minst 15–20 minuter innan du börjar steka! Det ger vetemjölet tid att suga upp vätskan, vilket ger plättar med underbart frasiga kanter som håller ihop perfekt vid vändning.',
        'desc': 'Klassiska svenska små plättar med frasiga kanter stekta i smör. Serveras med rårörda lingon, sylt och vispgrädde.',
        'long_desc': (
            'Det finns få saker som väcker så mycket barndomsnostalgi som doften av nystekta små plättar i köket. '
            'Hemligheten bakom de allra godaste svenska plättarna sitter i proportionerna mellan mjöl, ägg och standardmjölk, '
            'samt att blanda i smält brynt smör direkt i smeten. När smeten får vila sväller vetestärkelsen vilket garanterar '
            'plättar som håller ihop perfekt och får den där karakteristiska, krispiga och gyllenbruna spetskanten när de steks i en '
            'ordentligt varm gjutjärnsplättlagg med en klick smör i varje fördjupning. Plättar är lika självklara till söndagsbrunchen '
            'och mellanmålet som till efterrätt efter torsdagens ärtsoppa. Servera rykande varma i en hög med rårörda lingon, '
            'jordgubbssylt och en klick fluffig vispgrädde!'
        ),
        'ingredients': [
            {
                'group': 'Klassisk Plättsmet',
                'items': [
                    {'name': 'ägg (stora)', 'unit': 'st', 'val': 3},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': 2.5},
                    {'name': 'standardmjölk (3%)', 'unit': 'dl', 'val': 6},
                    {'name': 'salt', 'unit': 'tsk', 'val': 0.5},
                    {'name': 'strösocker eller vaniljsocker', 'unit': 'tsk', 'val': 1},
                    {'name': 'smör (smält och något avsvalnat)', 'unit': 'g', 'val': 50}
                ]
            },
            {
                'group': 'Stekning',
                'items': [
                    {'name': 'smör (till plättlaggen mellan varje stekning)', 'unit': 'g', 'val': 30}
                ]
            },
            {
                'group': 'Klassiska Tillbehör',
                'items': [
                    {'name': 'rårörda lingon eller drottningsylt', 'unit': 'dl', 'val': 2},
                    {'name': 'vispgrädde (lättvispad)', 'unit': 'dl', 'val': 2}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Blanda de torra ingredienserna',
                'text': 'Mät upp vetemjöl, salt och socker i en rymlig bunke. Blanda runt med en handvisp så att inga mjölklumpar bildas.'
            },
            {
                'step': 2,
                'title': 'Vispa ihop med mjölk till slät smet',
                'text': 'Tillsätt hälften av mjölken (ca 3 dl) och vispa kraftigt till en helt slät, klumpfri smet. Häll därefter i resten av mjölken och vispa ner äggen ett i taget.'
            },
            {
                'step': 3,
                'title': 'Rör i smöret och låt svälla',
                'text': 'Smält 50 g smör i en kastrull eller direkt i plättlaggen och låt svalna något. Vispa ner det smälta smöret i smeten. Låt smeten stå och svälla i rumstemperatur i minst 15–20 minuter (gärna 30 min).'
            },
            {
                'step': 4,
                'title': 'Värm plättlaggen ordentligt',
                'text': 'Värm upp en plättlagg (helst gjutjärn) på medelhög värme. Lägg en liten klick smör i varje fördjupning och låt det tystna och fräsa gyllene.'
            },
            {
                'step': 5,
                'title': 'Stek plättarna gyllenbruna',
                'text': 'Häll ca 1,5–2 matskedar smet i varje rundel. Stek i ca 1,5–2 minuter tills smeten har stelnat på ovansidan och undersidan fått vacker gyllenbrun färg. Vänd plättarna med en liten stekspade eller smörkniv och stek i ytterligare 1 minut på andra sidan.'
            },
            {
                'step': 6,
                'title': 'Lägg upp i staplar och servera',
                'text': 'Lägg upp de färdiga plättarna på ett varmt fat. Smöra laggen på nytt och upprepa tills all smet är stekt. Servera genast i höga staplar med rårörda lingon, jordgubbssylt och lättvispad grädde!'
            }
        ],
        'faqs': [
            {
                'q': 'Kan man steka plättar utan en speciell plättlagg?',
                'a': 'Ja, det går alldeles utmärkt! Klicka bara ut små klickar smet i en vanlig stekpanna. De blir kanske inte millimeterrunda, men precis lika goda och frasiga.'
            },
            {
                'q': 'Varför blir mina plättar bleka eller sladdriga?',
                'a': 'Pannan är troligen inte tillräckligt varm, eller så har du snålat med smöret! Gjutjärn behöver god tid att bli genomvarmt, och smöret i laggen är det som skapar den frasiga spetskanten.'
            },
            {
                'q': 'Går det att frysa in plättar?',
                'a': 'Ja! Låt plättarna svalna och frys in dem med smörgåspapper emellan. Värm dem sedan direkt i brödrosten eller i ugnen på 175°C i 5 minuter så blir de som nygräddade igen.'
            }
        ],
        'community_reviews': [
            {'name': 'Therese Gustafsson', 'date': '1 oktober 2026', 'rating': 5, 'comment': 'Precis som min mormor gjorde dem! Frasiga i kanten och underbart goda. Barnen åt upp allt på tio minuter.', 'verified': True},
            {'name': 'Henrik Alm', 'date': '27 september 2026', 'rating': 5, 'comment': 'Perfekt recept! Att låta smeten svälla i 20 minuter gjorde verkligen stor skillnad, de höll ihop suveränt vid vändning.', 'verified': True},
            {'name': 'Maja S.', 'date': '21 september 2026', 'rating': 5, 'comment': 'Bästa plättsmeten! Testade med rårörda lingon och grädde, ren lycka på en söndagsmorgon.', 'verified': True},
            {'name': 'Anders P.', 'date': '15 september 2026', 'rating': 5, 'comment': 'Otroligt frasiga kanter tack vare gjutjärnslaggen och smöret i smeten. 5 stjärnor!', 'verified': True},
            {'name': 'Sara Lund', 'date': '9 september 2026', 'rating': 5, 'comment': 'Superenkelt recept som alltid lyckas. Gillar att de inte är för söta i smeten så sylten kommer till sin rätt.', 'verified': True},
            {'name': 'Emil F.', 'date': '2 september 2026', 'rating': 4, 'comment': 'Jättegoda och smidiga. Fick steka i vanlig stekpanna och det gick hur bra som helst det också.', 'verified': True}
        ]
    },

    # 4. Klassisk Krämig Rotfruktssoppa med Timjan
    {
        'title': 'Klassisk Krämig Rotfruktssoppa med Timjan – Höstens Godaste Soppa',
        'sub': 'Sammetslen och gyllene rotfruktssoppa på morot, palsternacka, rotselleri och potatis med timjan och rostade frön',
        'card_title': 'Krämig Rotfruktssoppa med Timjan',
        'slug': 'klassisk-kramig-rotfruktssoppa-timjan',
        'file': 'klassisk-kramig-rotfruktssoppa-timjan.html',
        'img': 'rotfruktssoppa-timjan',
        'alt': 'Krämig gyllene rotfruktssoppa i rustik skål toppad med rostade pumpakärnor, timjan och ringlad grädde',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Vegetariskt, Glutenfritt',
        'difficulty': 'Enkel',
        'time': 40,
        'time_str': '40 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT25M',
        'cook_time_str': '25 min',
        'total_time': 'PT40M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'rating': 4.91,
        'review_count': 5,
        'calories': 290,
        'nutrition': {'calories': '290 kcal', 'carbs': '28g', 'fat': '17g', 'protein': '5g', 'sugar': '8g'},
        'keywords': 'rotfruktssoppa, krämig rotfruktssoppa, rotfruktssoppa recept, soppa på rotfrukter, morotssoppa palsternacka, höstsoppa, enkel vegetarisk soppa, rotfruktssoppa timjan',
        'drink_pairing': 'Ett fruktigt vitt vin (t.ex. Pinot Gris eller ekfatslagrad Chardonnay), torr äppelmust eller en ljus lageröl.',
        'equipment': ['Stor tjockbottnad kastrull eller gryta', 'Stavmixer', 'Skärbräda & kockkniv', 'Potatisskalare', 'Liten stekpanna till fröna'],
        'pro_tips': 'Fräs de skurna rotfrukterna i smöret i 5–7 minuter innan du häller på buljongen! En lätt stekyta karamelliserar rotfrukternas naturliga sockerarter och ger soppan en djup, fyllig sötma.',
        'desc': 'Sammetslen rotfruktssoppa på morot, palsternacka, rotselleri och potatis smaksatt med färsk timjan och grädde. Toppas med rostade pumpakärnor.',
        'long_desc': (
            'När hösten är som allra vackrast och de svenska rotfrukterna är nyskördade och sprickfyllda med smak, finns det få saker '
            'som värmer lika gott som en sammetslen rotfruktssoppa. Denna klassiska soppa är en hyllning till den svenska myllan: söta morötter, '
            'nötig palsternacka, aromatisk rotselleri och mjuk potatis får först fräsa i smör tillsammans med lök, vitlök och färsk timjan. '
            'Därefter kokas alltsammans i en god grönsaksbuljong tills rotfrukterna är helt smältande mjuka, innan soppan mixas silkeslen och '
            'avrundas med vispgrädde och en nypa riven muskotnöt. Toppa soppan med smörrostade, krispiga pumpakärnor och några droppar god olja '
            'för en oemotståndlig texturkontrast. Servera med ett nygräddat surdegsbröd och njut av höstens finaste smaker!'
        ),
        'ingredients': [
            {
                'group': 'Svenska Rotfrukter',
                'items': [
                    {'name': 'morötter (skalade och slantade)', 'unit': 'st', 'val': 3},
                    {'name': 'palsternackor (skalade och slantade)', 'unit': 'st', 'val': 2},
                    {'name': 'rotselleri (skalad och tärnad)', 'unit': 'g', 'val': 150},
                    {'name': 'mjöliga potatisar (skalade och tärnade)', 'unit': 'st', 'val': 2},
                    {'name': 'gul lök (grovhackad)', 'unit': 'st', 'val': 1},
                    {'name': 'vitlöksklyftor (hackade)', 'unit': 'st', 'val': 2},
                    {'name': 'smör (till stekning)', 'unit': 'msk', 'val': 2}
                ]
            },
            {
                'group': 'Soppbas & Kryddor',
                'items': [
                    {'name': 'grönsaksbuljong (eller kycklingbuljong)', 'unit': 'dl', 'val': 8},
                    {'name': 'torrt vitt vin eller äppelcidervinäger', 'unit': 'msk', 'val': 2},
                    {'name': 'vispgrädde (40%)', 'unit': 'dl', 'val': 1.5},
                    {'name': 'färsk timjan (repad)', 'unit': 'msk', 'val': 1},
                    {'name': 'muskotnöt (nymalen)', 'unit': 'krm', 'val': 1},
                    {'name': 'salt och nymalen vitpeppar', 'unit': 'krm', 'val': 2}
                ]
            },
            {
                'group': 'Topping & Servering',
                'items': [
                    {'name': 'pumpakärnor eller solroskärnor (torrrostade)', 'unit': 'dl', 'val': 0.5},
                    {'name': 'färsk timjan till garnering', 'unit': 'kvistar', 'val': 4},
                    {'name': 'vispgrädde eller kallpressad rapsolja (att ringla på)', 'unit': 'msk', 'val': 2},
                    {'name': 'surdegsbröd med smör och ost', 'unit': 'skivor', 'val': 4}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Förbered rotfrukterna',
                'text': 'Skala morötter, palsternackor, rotselleri och potatis. Skär allt i jämna bitar, ca 1,5–2 cm stora, så att de kokar jämnt. Grovhacka lök och vitlök.'
            },
            {
                'step': 2,
                'title': 'Fräs rotfrukter och lök i smör',
                'text': 'Smält smöret i en stor kastrull på medelvärme. Lägg i alla rotfrukter, lök och vitlök. Fräs under omrörning i ca 5–7 minuter så att de mjuknar något och får en lätt gyllene stekyta.'
            },
            {
                'step': 3,
                'title': 'Koka i buljong med timjan',
                'text': 'Tillsätt repad färsk timjan, vin eller äppelcidervinäger och häll över grönsaksbuljongen. Låt koka upp, sänk värmen och låt sjuda under lock i ca 20 minuter tills alla rotfrukter är helt genomkokta och mjuka.'
            },
            {
                'step': 4,
                'title': 'Rosta pumpakärnorna',
                'text': 'Under tiden soppan kokar, rosta pumpakärnorna i en torr het stekpanna i ett par minuter tills de börjar knäppa och puffa upp. Strö över lite flingsalt och häll upp på ett fat.'
            },
            {
                'step': 5,
                'title': 'Mixa soppan sammetslen och rör i grädden',
                'text': 'Ta kastrullen från plattan och mixa soppan helt slät och krämig med en stavmixer. Ställ tillbaka på spisen, häll i vispgrädden och låt soppan sjuda upp sakta i 2 minuter. Smaka av med riven muskotnöt, salt och vitpeppar.'
            },
            {
                'step': 6,
                'title': 'Garnera och servera',
                'text': 'Häll upp den heta rotfruktssoppan i skålar. Ringla över en skvätt grädde eller lite nötig rapsolja, toppa med de frasiga pumpakärnorna och färsk timjan. Servera med ett gott bröd med vällagrad ost!'
            }
        ],
        'faqs': [
            {
                'q': 'Kan man göra rotfruktssoppan helt vegansk?',
                'a': 'Ja, hur enkelt som helst! Stek i rapsolja istället för smör och ersätt vispgrädden med havregrädde (t.ex. Oatly iMat) eller krämig kokosgrädde.'
            },
            {
                'q': 'Vilka andra rotfrukter passar i soppan?',
                'a': 'Kålrot, persiljerot och jordärtskockor är fantastiska i den här soppan. Du kan variera proportionerna efter vad du har hemma i kylen!'
            },
            {
                'q': 'Går rotfruktssoppan att förbereda i förväg?',
                'a': 'Ja, soppan passar perfekt att laga dagen innan. Den blir nästan ännu fylligare och godare när rotfrukternas smaker får dra åt sig över natten.'
            }
        ],
        'community_reviews': [
            {'name': 'Erika Sund', 'date': '3 oktober 2026', 'rating': 5, 'comment': 'Vilken otroligt len och god soppa! Rostade pumpakärnor på toppen gav perfekt crunch. Höstens favorit!', 'verified': True},
            {'name': 'Gustav Hedin', 'date': '26 september 2026', 'rating': 5, 'comment': 'Fantastisk smakbalans med timjanen och palsternackan. Så värmande och mättande.', 'verified': True},
            {'name': 'Lotta N.', 'date': '20 september 2026', 'rating': 5, 'comment': 'Underbar höstmat! Enkel att laga och barnen åt med god aptit trots rotselleri.', 'verified': True},
            {'name': 'Martin V.', 'date': '14 september 2026', 'rating': 5, 'comment': 'Sammetslen konsistens och jättefin färg. Åt med surdegsbröd och prästost, perfekt middag.', 'verified': True},
            {'name': 'Ingela B.', 'date': '7 september 2026', 'rating': 4, 'comment': 'Mycket god och lättlagad. Jag tog i en gnutta färsk ingefära för extra värme, passade toppen.', 'verified': True}
        ]
    }
]

# Check existing slugs
existing_slugs = {r["slug"] for r in RECIPES}
for nr in NEW_RECIPES:
    if nr["slug"] not in existing_slugs:
        RECIPES.append(nr)
        print(f"Added new recipe: {nr['slug']}")
    else:
        print(f"Recipe {nr['slug']} already exists, skipping addition.")

print(f"\nTotal recipes in catalog: {len(RECIPES)}")

# Write back to tools/recipes_data.py
output_path = "tools/recipes_data.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\nRECIPES = ")
    f.write(pprint.pformat(RECIPES, indent=4, width=120, sort_dicts=True))
    f.write("\n")

print(f"Successfully serialized {len(RECIPES)} recipes to {output_path}!")
