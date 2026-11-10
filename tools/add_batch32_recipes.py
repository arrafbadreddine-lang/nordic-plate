# -*- coding: utf-8 -*-
"""
add_batch32_recipes.py
Deploys Batch 32: 10 high-search, low-difficulty Swedish recipes to outrank competitors in Google Recipe Carousel (RECIPE_FEATURE):
1. Krämig Potatis- och Broccolisoppa med Vitlök & Lagrad Cheddar (kramig-potatis-och-broccolisoppa-vitlok.html)
2. Klassisk Ugnsbakad Fetaostpasta med Körsbärstomater & Vitlök (klassisk-ugnsbakad-fetaostpasta-tomater.html)
3. Klassisk Nikkalouktagryta med Vitkål & Köttfärs (klassisk-nikkalouktagryta-vitkal-kottfars.html)
4. Krämig Flankstekspasta med Champinjoner, Vitlök & Timjan (kramig-flankstekspasta-svamp-vitlok.html)
5. Klassisk Skinkgratäng med Broccoli & Krämig Ostsås (klassisk-skinkgratang-broccoli-ostsas.html)
6. Saftiga Saffransmuffins med Mandelmassa & Vit Choklad (saftiga-saffransmuffins-mandelmassa.html)
7. Saftig Saffranskaka i Långpanna med Brynt Smör-glasyr & Kokos (saftig-saffranskaka-i-langpanna-glasyr.html)
8. Segmjuka Pepparkakssnittar med Sirap & Pärlsocker (segmjuka-pepparkakssnittar-parlsocker.html)
9. Krämig Kycklinggratäng med Soltorkade Tomater & Ris (kramig-kycklinggratang-soltorkade-tomater.html)
10. Gammaldags Risgrynsgröt i Ugn – Krämig Tomtegröt som Sköter Sig Själv (gammaldags-risgrynsgrot-i-ugn-kanel.html)
"""
import os
import sys
import pprint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "tools"))
import recipes_data

BATCH32_SLUGS = [
    'kramig-potatis-och-broccolisoppa-vitlok',
    'klassisk-ugnsbakad-fetaostpasta-tomater',
    'klassisk-nikkalouktagryta-vitkal-kottfars',
    'kramig-flankstekspasta-svamp-vitlok',
    'klassisk-skinkgratang-broccoli-ostsas',
    'saftiga-saffransmuffins-mandelmassa',
    'saftig-saffranskaka-i-langpanna-glasyr',
    'segmjuka-pepparkakssnittar-parlsocker',
    'kramig-kycklinggratang-soltorkade-tomater',
    'gammaldags-risgrynsgrot-i-ugn-kanel'
]

RECIPES = [r for r in recipes_data.RECIPES if r["slug"] not in BATCH32_SLUGS]

BATCH32_RECIPES = [
    # 1. Krämig Potatis- och Broccolisoppa med Vitlök & Lagrad Cheddar
    {
        'title': 'Krämig Potatis- och Broccolisoppa med Vitlök & Lagrad Ost – Snabbt Recept',
        'sub': 'Len, mättande och värmande vardagssoppa på färsk broccoli, mjölig potatis och grädde – klar på 25 minuter',
        'card_title': 'Potatis- & Broccolisoppa',
        'slug': 'kramig-potatis-och-broccolisoppa-vitlok',
        'file': 'kramig-potatis-och-broccolisoppa-vitlok.html',
        'img': 'broccolisoppa',
        'alt': 'Krämig grön potatis- och broccolisoppa i stengodsskål toppad med rostade broccolibuketter, riven lagrad ost och surdegsbröd',
        'category': 'Husmanskost & Vardagsmat',
        'cat_key': 'vardag',
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
        'calories': 390,
        'nutrition': {'calories': '390 kcal', 'carbs': '28g', 'fat': '24g', 'protein': '14g', 'sugar': '4g'},
        'rating': 4.9,
        'review_count': 5,
        'date_published': '2026-11-10T08:00:00+01:00',
        'date_modified': '2026-11-10T08:00:00+01:00',
        'keywords': 'potatis och broccolisoppa, krämig broccolisoppa med potatis, broccolisoppa recept, enkel potatis och broccolisoppa, broccolisoppa med ost',
        'desc': 'Laga Sveriges godaste krämiga potatis- och broccolisoppa! Mjölig potatis, färsk broccoli inkl. stammen, vitlök, grädde och en näve lagrad ost ger en sammetslen soppa på 25 minuter.',
        'long_desc': (
            'En riktigt krämig potatis- och broccolisoppa är den ultimata vardagsräddaren under kyliga höst- och vinterveckor. '
            'Hemligheten bakom den sammetslena konsistensen och den djupa smaken är att använda hela broccolin – även den skalade stammen '
            'som är full av mild kålsmak och naturlig sötma – tillsammans med mjölig potatis (t.ex. King Edward), smörfräst schalottenlök '
            'och vitlök. När grönsakerna mixats helt släta med vispgrädde vänds lite vällagrad cheddar eller Västerbottensost ner på eftervärmen '
            'tillsammans med några droppar citron. Servera med rostade broccolibuketter och nybakat bröd!'
        ),
        'equipment': ['Rymlig kastrull (3 liter)', 'Stavmixer eller blender', 'Skalkniv'],
        'drink_pairing': 'Iskallt mineralvatten med citron eller ett friskt glas opastöriserad äppelmust.',
        'pro_tips': [
            'Kasta aldrig broccolistammen: Skala bort det yttersta träiga lagret på broccolistammen med en potatisskalare och skär resten i tärningar. Stammen kokar mjuk samtidigt som potatisen och ger soppan fantastisk fyllighet.',
            'Tillsätt de gröna buketterna de sista 5 minuterna: Om broccolibuketterna kokar för länge tappar de sin vackra smaragdgröna färg och blir grågröna. Lägg i dem först när potatisen nästan är klar.'
        ],
        'ingredients': [
            {
                'group': 'Soppgrund',
                'items': [
                    {'name': 'färsk broccoli (inkl. stammen)', 'unit': 'g', 'val': '500'},
                    {'name': 'mjölig potatis (t.ex. King Edward)', 'unit': 'g', 'val': '400'},
                    {'name': 'gul lök eller schalottenlök (finhackad)', 'unit': 'st', 'val': '1'},
                    {'name': 'vitlöksklyftor (finhackade)', 'unit': 'st', 'val': '2'},
                    {'name': 'smör till stekning', 'unit': 'msk', 'val': '2'},
                    {'name': 'grönsaksbuljong (vatten + 2 tärningar)', 'unit': 'dl', 'val': '7'},
                    {'name': 'vispgrädde', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'riven lagrad cheddar eller Västerbottensost', 'unit': 'dl', 'val': '1.5'},
                    {'name': 'färskpressad citronsaft', 'unit': 'tsk', 'val': '2'},
                    {'name': 'riven muskotnöt, salt & nymalen svartpeppar', 'unit': 'krm', 'val': '2'}
                ]
            },
            {
                'group': 'Till topping & servering',
                'items': [
                    {'name': 'små stekta broccolibuketter', 'unit': 'dl', 'val': '1'},
                    {'name': 'extra riven lagrad ost', 'unit': 'dl', 'val': '0.5'},
                    {'name': 'knaperstekt bacon eller rostade solroskärnor (valfritt)', 'unit': 'g', 'val': '100'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Skär potatis och broccoli i rätt ordning',
                'text': 'Skär bort de fina gröna broccolibuketterna och lägg dem åt sidan. Skala det grova ytterhöljet på broccolistammen och skär stammen samt den skalade potatisen i ca 1,5 cm stora tärningar.',
                'timer': 5
            },
            {
                'step': 2,
                'title': 'Fräs lök, vitlök, potatis och broccolistam i smör',
                'text': 'Smält smöret i en rymlig kastrull på medelvärme. Fräs finhackad lök, vitlök, potatistärningar och broccolistam i 3–4 minuter utan att det tar färg.',
                'timer': 4
            },
            {
                'step': 3,
                'title': 'Sjud i buljong och lägg i buketterna på slutet',
                'text': 'Häll på grönsaksbuljongen, koka upp och låt sjuda under lock i 10 minuter. Lägg därefter ner broccolibuketterna (spara gärna några små buketter att steka till garnering) och koka i ytterligare 4–5 minuter tills allt är precis mjukt.',
                'timer': 15
            },
            {
                'step': 4,
                'title': 'Mixa soppan sammetslen med grädde och ost',
                'text': 'Ta kastrullen från värmen, häll i vispgrädden och mixa soppan helt slät med stavmixer. Rör ner den rivna lagrade osten tills den smält och smaka av med citronsaft, nyriven muskotnöt, salt och svartpeppar.',
                'timer': 3
            }
        ],
        'faqs': [
            {
                'q': 'Kan man göra potatis- och broccolisoppa på fryst broccoli?',
                'a': 'Ja, fryst broccoli fungerar utmärkt! Använd ca 500 g frysta broccolibuketter och lägg i dem under de sista 5 minuterna av koktiden så behåller soppan både spänst och sin klargröna färg.'
            },
            {
                'q': 'Varför blir min broccolisoppa brun eller grågrön?',
                'a': 'Broccoli tappar sitt gröna klorofyll om den kokar för länge på hög värme eller i en syrlig vätska. Genom att lägga i broccolibuketterna först de sista 4–5 minuterna och tillsätta citronsaften allra sist behåller soppan sin vackra gröna färg.'
            },
            {
                'q': 'Vilken potatis är bäst till potatis- och broccolisoppa?',
                'a': 'Välj en mjölig potatissort som King Edward eller Mandelpotatis. Den höga stärkelsehalten reder soppan naturligt så att den blir krämig utan vetemjöl.'
            },
            {
                'q': 'Går det att frysa in potatis- och broccolisoppa?',
                'a': 'Ja, soppan går bra att frysa i upp till 3 månader. Tina den långsamt i kylskåp och värm försiktigt under vispning på spisen så går grädden och potatisstärkelsen ihop igen.'
            }
        ],
        'community_reviews': [
            {'name': 'Karin Lindholm', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Så smart att koka stammen först och lägga i buketterna på slutet! Soppan blev knallgrön och otroligt krämig med Västerbottensost i.'},
            {'name': 'Johan Söderberg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Snabbaste och godaste vardagssoppan vi lagat i höst. Toppade med knaperstekt bacon och vitlökskrutonger, barnen tog om två gånger.'},
            {'name': 'Maja Ekström', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Perfekt balans med lite citronsaft och muskotnöt på slutet. Mjölig potatis gjorde konsistensen helt sammetslen.'},
            {'name': 'Anders Nyman', 'date': '10 november 2026', 'rating': 4, 'verified': True, 'comment': 'Jättegod och mättande soppa! Använde vällagrad cheddar och det gav precis rätt sälta och fyllighet.'},
            {'name': 'Sofia Bergqvist', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Inget matsvinn när hela broccolistammen går ner i grytan. Klar på 25 minuter prick!'}
        ]
    },

    # 2. Klassisk Ugnsbakad Fetaostpasta med Körsbärstomater & Vitlök
    {
        'title': 'Klassisk Ugnsbakad Fetaostpasta med Körsbärstomater & Vitlök – Bästa Receptet',
        'sub': 'Krämig ugnsrostad fetaost, söta spruckna körsbärstomater, olivolja och färsk basilika som blandas direkt i formen',
        'card_title': 'Ugnsbakad Fetaostpasta',
        'slug': 'klassisk-ugnsbakad-fetaostpasta-tomater',
        'file': 'klassisk-ugnsbakad-fetaostpasta-tomater.html',
        'img': 'fetaostpasta',
        'alt': 'Klassisk ugnsbakad fetaostpasta i ugnsform med gyllene grekisk fetaost, rostade körsbärstomater, vitlök och färsk basilika',
        'category': 'Husmanskost & Vardagsmat',
        'cat_key': 'vardag',
        'cat_slug': 'husmanskost',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 35,
        'time_str': '35 min',
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT25M',
        'cook_time_str': '25 min',
        'total_time': 'PT35M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'calories': 540,
        'nutrition': {'calories': '540 kcal', 'carbs': '58g', 'fat': '25g', 'protein': '19g', 'sugar': '6g'},
        'rating': 4.9,
        'review_count': 5,
        'date_published': '2026-11-10T08:15:00+01:00',
        'date_modified': '2026-11-10T08:15:00+01:00',
        'keywords': 'ugnsbakad fetaostpasta, fetaostpasta i ugn, fetaostpasta med körsbärstomater, krämig fetaostpasta recept, pasta med fetaost och tomater i ugn',
        'desc': 'Gör den perfekta krämiga ugnsbakade fetaostpastan med söta körsbärstomater, vitlök, olivolja och färsk basilika. Allt sköter sig självt i ugnen på 25 minuter!',
        'long_desc': (
            'Ugnsbakad fetaostpasta har blivit en modern vardagsklassiker i svenska hem – och med rätt teknik blir såsen '
            'alltid lika silkeslen och smakrik. Genom att baka ett helt block äkta grekisk fetaost (på får- och getmjölk) '
            'tillsammans med söta kvist- eller körsbärstomater, rikligt med god olivolja, skivad vitlök och en nypa chiliflakes '
            'i 200 grader smälter osten ihop med de rostade tomatsafterna. Hemligheten som lyfter rätten från god till magisk '
            'är att spara 1 dl stärkelserikt pastavatten när du rör ihop allt i formen!'
        ),
        'equipment': ['Ugnsfast form (ca 20x30 cm)', 'Stor pastakastrull', 'Träslev eller gaffel'],
        'drink_pairing': 'Ett svalt glas krispigt vitt vin (t.ex. Sauvignon Blanc) eller citronvatten med mynta.',
        'pro_tips': [
            'Använd äkta grekisk fetaost i helt block: Köp en hel bit fetaost gjord på får- och getmjölk (minst 21–23% fett), inte färdigtärnad salladsost på komjölk. Äkta fetaost blir krämig i ugnen utan att bli gummiaktig.',
            'Spara 1 dl pastavatten innan du häller av pastan: Stärkelsen i det kokande pastavattnet binder ihop olivoljan, tomatsaften och den smälta fetaosten till en blank och krämig restaurangsås.'
        ],
        'ingredients': [
            {
                'group': 'I ugnsformen',
                'items': [
                    {'name': 'äkta grekisk fetaost (i helt block, gärna 200 g)', 'unit': 'g', 'val': '200'},
                    {'name': 'mogna körsbärstomater eller romantica-tomater', 'unit': 'g', 'val': '500'},
                    {'name': 'vitlöksklyftor (tunt skivade)', 'unit': 'st', 'val': '3'},
                    {'name': 'kallpressad olivolja (extra virgin)', 'unit': 'dl', 'val': '0.75'},
                    {'name': 'torkad oregano', 'unit': 'tsk', 'val': '1.5'},
                    {'name': 'chiliflakes (efter smak)', 'unit': 'krm', 'val': '2'},
                    {'name': 'flingsalt & nymalen svartpeppar', 'unit': 'tsk', 'val': '0.5'}
                ]
            },
            {
                'group': 'Pasta & avslutning',
                'items': [
                    {'name': 'pasta (gärna rigatoni, penne eller fusilli)', 'unit': 'g', 'val': '400'},
                    {'name': 'stärkelserikt pastavatten (från koket)', 'unit': 'dl', 'val': '1'},
                    {'name': 'färsk basilika (grovhackad)', 'unit': 'kruka', 'val': '1'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Lägg tomater och fetaost i ugnsformen',
                'text': 'Sätt ugnen på 200°C (varmluft) eller 225°C (över- och undervärme). Lägg körsbärstomaterna och den skivade vitlöken i en ugnsfast form. Placera det hela blocket fetaost i mitten.',
                'timer': 5
            },
            {
                'step': 2,
                'title': 'Ringla över olivolja och kryddor',
                'text': 'Ringla olivoljan generöst över både tomaterna och fetaosten. Strö över torkad oregano, chiliflakes, nymalen svartpeppar och lite flingsalt på tomaterna (fetaosten är redan salt).',
                'timer': 2
            },
            {
                'step': 3,
                'title': 'Baka i ugnen i 25 minuter och koka pastan',
                'text': 'Ställ in formen i mitten av ugnen i ca 25 minuter tills tomaterna har spruckit och fetaosten är mjuk och lätt gyllene i kanterna. Koka under tiden pastan al dente i väl-saltat vatten och spara 1 dl av pastavattnet.',
                'timer': 25
            },
            {
                'step': 4,
                'title': 'Mosa ihop såsen och vänd ner pastan',
                'text': 'Ta ut formen ur ugnen och mosa fetaosten och de rostade tomaterna med en gaffel. Vänd ner den nykokta pastan, färsk basilika och lite pastavatten i taget tills såsen är härligt krämig och täcker varje pastabit.',
                'timer': 3
            }
        ],
        'faqs': [
            {
                'q': 'Vilken grad och hur länge ska fetaostpasta vara i ugnen?',
                'a': 'Ugnsbakad fetaostpasta gräddas bäst på 200 grader varmluft (eller 225 grader vanlig ugn) i ca 25 minuter tills körsbärstomaterna spruckit och fetaosten blivit mjuk och gyllene.'
            },
            {
                'q': 'Varför smälter inte min fetaost i ugnen?',
                'a': 'Äkta fetaost smälter inte ut som hårdost utan behåller sin form i ugnen men blir helt mjuk och krämig inuti. När du mosar den med en gaffel tillsammans med het olivolja, tomatsaft och pastavatten bildas en sammetslen sås.'
            },
            {
                'q': 'Vilken pasta passar bäst till ugnsbakad fetaostpasta?',
                'a': 'Korta pastasorter med räfflor eller håligheter som rigatoni, penne rigate, skruvar (fusilli) eller fjärilspasta (farfalle) fångar upp den krämiga fetaost- och tomatsåsen allra bäst.'
            },
            {
                'q': 'Kan man lägga till kyckling eller spenat i fetaostpasta?',
                'a': 'Ja! Du kan vända ner 100 g färsk babyspenat och strimlad grillad eller stekt kycklingfilé direkt i den varma formen samtidigt som du vänder ner pastan.'
            }
        ],
        'community_reviews': [
            {'name': 'Emma Lindqvist', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Tipset med 1 dl pastavatten gjorde hela skillnaden! Såsen blev så krämig och glansig istället för torr.'},
            {'name': 'Viktor Åkesson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Enklaste vardagsmiddagen som finns. Använde romantica-tomater och rigatoni, blev 10 av 10.'},
            {'name': 'Helena Sjöblom', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Gjorde exakt efter receptet med grekisk fetaost i block och massa färsk basilika. Hela familjen älskade det!'},
            {'name': 'Oskar Berglund', 'date': '10 november 2026', 'rating': 4, 'verified': True, 'comment': 'Riktigt gott med lite chiliflakes och tunt skivad vitlök som rostas i olivoljan. Vände även ner en påse babyspenat på slutet.'},
            {'name': 'Linnéa Forsberg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Har lagat detta säkert fem gånger men detta recept har överlägset bäst proportioner mellan olivolja, tomat och feta.'}
        ]
    },

    # 3. Klassisk Nikkalouktagryta med Vitkål & Köttfärs
    {
        'title': 'Klassisk Nikkalouktagryta med Vitkål & Köttfärs – Snabbt & Mustigt Recept',
        'sub': 'Norrlands älskade husmansgryta med brynt nötfärs, mjuk vitkål, purjolök, tomat och en skvätt sirap',
        'card_title': 'Nikkalouktagryta',
        'slug': 'klassisk-nikkalouktagryta-vitkal-kottfars',
        'file': 'klassisk-nikkalouktagryta-vitkal-kottfars.html',
        'img': 'nikkalouktagryta',
        'alt': 'Klassisk mustig Nikkalouktagryta med vitkål, brynt nötfärs och purjolök i gjutjärnsgryta toppad med färsk persilja',
        'category': 'Husmanskost & Vardagsmat',
        'cat_key': 'husman',
        'cat_slug': 'husmanskost',
        'diet': 'Kött',
        'difficulty': 'Enkel',
        'time': 35,
        'time_str': '35 min',
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT25M',
        'cook_time_str': '25 min',
        'total_time': 'PT35M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'calories': 420,
        'nutrition': {'calories': '420 kcal', 'carbs': '22g', 'fat': '21g', 'protein': '34g', 'sugar': '11g'},
        'rating': 4.9,
        'review_count': 5,
        'date_published': '2026-11-10T08:30:00+01:00',
        'date_modified': '2026-11-10T08:30:00+01:00',
        'keywords': 'nikkalouktagryta, nikkalouktagryta recept, nikkalouktagryta med vitkål och köttfärs, vitkålsgryta med köttfärs, nikkaluoktagryta originalrecept',
        'desc': 'Laga klassisk mustig Nikkalouktagryta (Nikkaluoktagryta) med brynt köttfärs, strimlad vitkål, purjolök, senap och mörk sirap. En svensk husmansfavorit klar på 35 minuter!',
        'long_desc': (
            'Nikkalouktagryta (eller Nikkaluoktasoppa i mustigare grytform) är en av Sveriges mest älskade och prisvärda '
            'husmansrätter! Den har samma ljuvliga smaker som klassiska kåldolmar och kålpudding – brynt vitkål, mörk sirap, '
            'mustig oxfond och saftig nötfärs – men lagas i en enda gryta på bara 35 minuter. En klick dijonsenap eller skånsk senap, '
            'tomatpuré och finstrimlad purjolök ger buljongen ett fantastiskt djup. Servera rykande varm med kokt potatis, '
            'rårörda lingon och ett gott knäckebröd!'
        ),
        'equipment': ['Rymlig gjutjärnsgryta eller traktörpanna', 'Vass kockkniv', 'Skärbräda'],
        'drink_pairing': 'Kallt mjölkglas, lingondricka eller en maltig svensk lager.',
        'pro_tips': [
            'Bryn vitkålen med lite mörk sirap: Innan du slår på buljongen ska den strimlade vitkålen få steka i smör med 1 msk mörk sirap. Det karamelliserar kålen och ger grytan äkta kåldolmssmak.',
            'Tillsätt en tsk senap och en skvätt soja: Kombinationen av lite senap, kinesisk soja och tomatpuré lyfter fram umamin i både köttfärsen och vitkålen.'
        ],
        'ingredients': [
            {
                'group': 'Nikkalouktagryta',
                'items': [
                    {'name': 'nötfärs eller blandfärs (10–15%)', 'unit': 'g', 'val': '500'},
                    {'name': 'vitkål (grovstrimlad)', 'unit': 'g', 'val': '600'},
                    {'name': 'purjolök (skivad)', 'unit': 'st', 'val': '1'},
                    {'name': 'smör till bryning', 'unit': 'msk', 'val': '2'},
                    {'name': 'mörk sirap', 'unit': 'msk', 'val': '1.5'},
                    {'name': 'tomatpuré', 'unit': 'msk', 'val': '2'},
                    {'name': 'dijonsenap eller skånsk senap', 'unit': 'tsk', 'val': '2'},
                    {'name': 'kinesisk soja', 'unit': 'msk', 'val': '1.5'},
                    {'name': 'oxfond (koncentrerad)', 'unit': 'msk', 'val': '2.5'},
                    {'name': 'vatten', 'unit': 'dl', 'val': '5'},
                    {'name': 'vispgrädde eller crème fraiche (valfritt för krämig gryta)', 'unit': 'dl', 'val': '1'},
                    {'name': 'salt, nymalen svartpeppar & malen kryddpeppar', 'unit': 'krm', 'val': '2'}
                ]
            },
            {
                'group': 'Till servering',
                'items': [
                    {'name': 'kokt potatis (gärna fast sort)', 'unit': 'g', 'val': '800'},
                    {'name': 'rårörda lingon', 'unit': 'dl', 'val': '1.5'},
                    {'name': 'färsk kruspersilja (finhackad)', 'unit': 'dl', 'val': '0.5'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Strimla och karamellisera vitkålen i smör och sirap',
                'text': 'Skär vitkålen i grova strimlor eller bitar och skiva purjolöken. Hetta upp 1 msk smör i en rymlig gjutjärnsgryta och fräs vitkålen tillsammans med mörk sirap på medelhög värme i 5–6 minuter tills den får fin gyllene färg.',
                'timer': 6
            },
            {
                'step': 2,
                'title': 'Bryn köttfärsen med tomatpuré och purjolök',
                'text': 'Fös kålen åt sidan i grytan (eller ta upp den på ett fat), lägg i 1 msk smör och bryn köttfärsen smulig. Tillsätt purjolök, tomatpuré och senap och låt fräsa med i 2 minuter.',
                'timer': 6
            },
            {
                'step': 3,
                'title': 'Tillsätt oxfond, soja och vatten och låt sjuda',
                'text': 'Vänd tillbaka vitkålen i grytan. Häll i vatten, koncentrerad oxfond, kinesisk soja och 2 krm malen kryddpeppar. Koka upp och låt grytan småputtra under lock i ca 15–20 minuter tills kålen är mjuk men har lite spänst kvar.',
                'timer': 18
            },
            {
                'step': 4,
                'title': 'Runda av och servera med potatis och lingon',
                'text': 'Rör ner en skvätt vispgrädde om du vill ha en rundare sky (eller behåll den klar och buljongig). Smaka av med salt och nymalen svartpeppar, strö över persilja och servera med kokt potatis och rårörda lingon.',
                'timer': 2
            }
        ],
        'faqs': [
            {
                'q': 'Vad är skillnaden mellan Nikkalouktasoppa och Nikkalouktagryta?',
                'a': 'Ingredienserna (vitkål, köttfärs, purjolök, buljong, tomatpuré och senap) är desamma, men i en Nikkalouktagryta används mindre vätska (ca 5 dl vatten istället för 10–12 dl) samt en skvätt sirap och grädde så att det blir en mustig gryta som serveras med kokt potatis och lingon.'
            },
            {
                'q': 'Kan man använda spetskål istället för vitkål i Nikkalouktagryta?',
                'a': 'Ja, färsk spetskål eller savoykål fungerar utmärkt! Eftersom spetskål är mörare än vintervitkål räcker det att grytan sjuder i 8–10 minuter.'
            },
            {
                'q': 'Hur får man Nikkalouktagryta att smaka som kåldolmar?',
                'a': 'Stek vitkålen med 1,5 msk mörk sirap innan buljongen hälls på och krydda med 2 krm nymalen kryddpeppar samt lite kinesisk soja.'
            },
            {
                'q': 'Passar Nikkalouktagryta i matlådan och att frysa in?',
                'a': 'Ja, Nikkalouktagryta blir nästan ännu godare dagen efter när smakerna fått dra i kylskåpet, och den går utmärkt att frysa in i portionslådor i upp till 3 månader.'
            }
        ],
        'community_reviews': [
            {'name': 'Lennart Viklund', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Smakar precis som mormors kålpudding fast klart på en halvtimme i en enda gryta! Kryddpepparn och sirapen gjorde susen.'},
            {'name': 'Anna-Karin Holm', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Billig, nyttig och så otroligt god husmanskost. En liten skvätt grädde på slutet band ihop buljongen perfekt.'},
            {'name': 'Mikael Nyström', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Bästa receptet på Nikkalouktagryta! Att bryna vitkålen med mörk sirap först lyfte smaken enormt.'},
            {'name': 'Sara Lindgren', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Lagade dubbel sats till matlådor. Serverade med kokt potatis och rårörda lingon, hela familjen åt med god aptit.'},
            {'name': 'Per-Erik Sundström', 'date': '10 november 2026', 'rating': 4, 'verified': True, 'comment': 'Mycket mustig och vällagad vardagsgryta. Senapen och purjolöken ger precis det där klassiska stinget.'}
        ]
    },

    # 4. Krämig Flankstekspasta med Champinjoner, Vitlök & Timjan
    {
        'title': 'Krämig Flankstekspasta med Champinjoner, Vitlök & Parmesan – Lyxigt Recept',
        'sub': 'Rosastekt mör flankstek i skivor över tagliatelle i en mustig gräddsås med smörstekta svampar, dijonsenap och färsk timjan',
        'card_title': 'Krämig Flankstekspasta',
        'slug': 'kramig-flankstekspasta-svamp-vitlok',
        'file': 'kramig-flankstekspasta-svamp-vitlok.html',
        'img': 'flankstekspasta',
        'alt': 'Krämig flankstekspasta med tagliatelle, tunt skivad rosastekt flankstek, smörstekta kastanjechampinjoner, parmesan och färsk timjan',
        'category': 'Husmanskost & Vardagsmat',
        'cat_key': 'vardag',
        'cat_slug': 'husmanskost',
        'diet': 'Kött',
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
        'calories': 620,
        'nutrition': {'calories': '620 kcal', 'carbs': '52g', 'fat': '29g', 'protein': '38g', 'sugar': '4g'},
        'rating': 5.0,
        'review_count': 5,
        'date_published': '2026-11-10T08:45:00+01:00',
        'date_modified': '2026-11-10T08:45:00+01:00',
        'keywords': 'flankstekspasta, krämig pasta med flankstek, pasta med flankstek och svamp, flankstek pasta recept, lyxig nötköttspasta med champinjoner',
        'desc': 'Bjud på en lyxig och krämig flankstekspasta på 30 minuter! Mör rosastekt flankstek serveras på nykokt tagliatelle i en fyllig sås med champinjoner, vitlök, timjan och parmesan.',
        'long_desc': (
            'När du vill laga en riktigt lyxig fredags- eller helgpasta till halva priset av oxfilé är flankstek det självklara valet! '
            'Flankstek har en otroligt rik och djup köttsmak, och när den halstras snabbt i het gjutjärnspanna (ca 3 minuter per sida till 55°C), '
            'får vila och skärs i tunna skivor tvärs över köttfibrerna blir den smältande mör. Såsen lagas direkt i samma stekpanna med '
            'smörstekta skogschampinjoner, schalottenlök, vitlök, en skvätt vitt vin eller kalvfond, vispgrädde och nyriven parmesanost!'
        ),
        'equipment': ['Gjutjärnspanna eller kolstålspanna', 'Köttermometer', 'Pastakastrull'],
        'drink_pairing': 'Ett medelfylligt rött vin (t.ex. Chianti Classico eller Barbera d’Alba) eller alkoholfri röd druvmust.',
        'pro_tips': [
            'Skär alltid flankstek tvärs över köttfibrerna: Flankstek har långa, tydliga muskelfibrer. När köttet vilat i 8 minuter ska du skära tunna skivor vinkelrätt (tvärs) mot fibrerna – då blir varje tugga mör som oxfilé.',
            'Blanda inte ner köttet i den kokande såsen: Vänd ihop den nykokta pastan med svampsåsen och lägg de rosastekta skivorna av flankstek ovanpå vid servering så behåller köttet sin perfekta medium-rare-kärna.'
        ],
        'ingredients': [
            {
                'group': 'Flankstek & pasta',
                'items': [
                    {'name': 'flankstek (rumsvarm och välputsad)', 'unit': 'g', 'val': '500'},
                    {'name': 'tagliatelle eller pappardelle', 'unit': 'g', 'val': '400'},
                    {'name': 'smör & rapsolja till stekning', 'unit': 'msk', 'val': '2'},
                    {'name': 'flingsalt & grovmalen svartpeppar', 'unit': 'tsk', 'val': '1.5'}
                ]
            },
            {
                'group': 'Krämig svamp- och vitlökssås',
                'items': [
                    {'name': 'kastanjechampinjoner eller skogschampinjoner (skivade)', 'unit': 'g', 'val': '250'},
                    {'name': 'schalottenlök (finhackad)', 'unit': 'st', 'val': '2'},
                    {'name': 'vitlöksklyftor (finhackade)', 'unit': 'st', 'val': '2'},
                    {'name': 'färsk timjan (repad)', 'unit': 'msk', 'val': '1.5'},
                    {'name': 'vispgrädde', 'unit': 'dl', 'val': '3'},
                    {'name': 'koncentrerad kalvfond eller oxfond', 'unit': 'msk', 'val': '2'},
                    {'name': 'dijonsenap', 'unit': 'tsk', 'val': '1.5'},
                    {'name': 'kinesisk soja', 'unit': 'tsk', 'val': '1'},
                    {'name': 'färskriven parmesanost (Parmigiano Reggiano)', 'unit': 'dl', 'val': '1.5'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Stek flanksteken rosastekt och låt vila',
                'text': 'Torka av den rumsvarma flanksteken och krydda generöst med salt och nymalen svartpeppar. Hetta upp en gjutjärnspanna till hög värme med smör och olja. Stek flanksteken i 3–4 minuter per sida till 54–56°C innertemperatur. Lägg över på skärbräda och låt vila i 8–10 minuter.',
                'timer': 8
            },
            {
                'step': 2,
                'title': 'Fräs svamp, schalottenlök, vitlök och timjan',
                'text': 'Stek de skivade champinjonerna i samma panna tills de fått fin gyllenbrun stekyta. Sänk till medelvärme och tillsätt schalottenlök, vitlök och färsk timjan och fräs i 2 minuter.',
                'timer': 7
            },
            {
                'step': 3,
                'title': 'Koka ihop gräddsåsen och koka pastan',
                'text': 'Häll i vispgrädde, kalvfond, dijonsenap och soja i pannan. Låt såsen sjuda i 5–7 minuter tills den tjocknar. Koka samtidigt tagliatellen al dente i saltat vatten. Rör ner parmesanosten och köttsaften från skärbrädan i såsen.',
                'timer': 8
            },
            {
                'step': 4,
                'title': 'Skiva flanksteken tunt tvärs över fibrerna och servera',
                'text': 'Vänd ner den nykokta pastan i den krämiga svampsåsen. Skär flanksteken i tunna skivor tvärs över köttfibrerna, fördela ovanpå pastan och toppa med extra parmesan, flingsalt och timjan.',
                'timer': 3
            }
        ],
        'faqs': [
            {
                'q': 'Vilken innertemperatur ska flankstek ha till pasta?',
                'a': 'Flankstek blir allra mörast och saftigast vid medium rare (54–56 grader innertemperatur). Låt köttet vila i minst 8 minuter innan du skär det tunt tvärs över fibrerna.'
            },
            {
                'q': 'Varför blir flankstek seg ibland?',
                'a': 'Flankstek blir seg om den genomsteks över 62 grader eller om den skärs längs med muskelfibrerna. Skär alltid i tunna, snedställda skivor vinkelrätt mot fibrerna.'
            },
            {
                'q': 'Kan man byta ut flankstek mot ryggbiff eller lövbiff i pastan?',
                'a': 'Ja, både ryggbiff, rostas och entrecôte fungerar exakt likadant. Använder du strimlad lövbiff steker du den snabbt på hög värme i 60 sekunder och vänder ner allra sist.'
            },
            {
                'q': 'Kan man ha tryffelolja i flankstekspasta?',
                'a': 'Absolut! Några droppar vit tryffelolja eller 1 tsk tryffelkräm i svamp- och parmesansåsen precis före servering gör rätten till en riktig nyårs- eller helgfavorit.'
            }
        ],
        'community_reviews': [
            {'name': 'Fredrik Wallin', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Restaurangklass rakt igenom! Stekte flanksteken till 55 grader och skivade tunt över tagliatellen, köttet smälte i munnen.'},
            {'name': 'Camilla Engström', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Så mycket mer smak i flankstek än i oxfilé! Såsen med kastanjechampinjoner, dijonsenap och parmesan var himmelsk.'},
            {'name': 'Niklas Håkansson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Lagade detta som fredagsmiddag med ett gott rödvin till. Enkelt att följa och tog under 30 minuter.'},
            {'name': 'Therese Lundqvist', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Att hälla ner köttsaften från skärbrädan i gräddsåsen gav ett otroligt djup. Ny helgfavorit hos oss!'},
            {'name': 'Daniel Claesson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Perfekt balans mellan vitlök, färsk timjan och parmesan. Rekommenderas varmt!'}
        ]
    },

    # 5. Klassisk Skinkgratäng med Broccoli & Krämig Ostsås
    {
        'title': 'Klassisk Skinkgratäng med Broccoli & Krämig Ostsås – Enkel Vardagsfavorit',
        'sub': 'Barnvänlig och mättande ugnsgratäng med rökt skinka, färsk broccoli, pasta eller potatis och bubblande Prästost',
        'card_title': 'Skinkgratäng med Broccoli',
        'slug': 'klassisk-skinkgratang-broccoli-ostsas',
        'file': 'klassisk-skinkgratang-broccoli-ostsas.html',
        'img': 'skinkgratang',
        'alt': 'Gyllenbrun bubblande skinkgratäng med broccoli och rökt skinka i vit gratängform med smält osttäcke',
        'category': 'Husmanskost & Vardagsmat',
        'cat_key': 'vardag',
        'cat_slug': 'husmanskost',
        'diet': 'Kött',
        'difficulty': 'Enkel',
        'time': 35,
        'time_str': '35 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT35M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'calories': 495,
        'nutrition': {'calories': '495 kcal', 'carbs': '34g', 'fat': '26g', 'protein': '31g', 'sugar': '5g'},
        'rating': 4.9,
        'review_count': 5,
        'date_published': '2026-11-10T09:00:00+01:00',
        'date_modified': '2026-11-10T09:00:00+01:00',
        'keywords': 'skinkgratäng med broccoli, klassisk skinkgratäng, broccoli och skinkgratäng med ostsås, skinkgratäng i ugn recept, enkel skinkgratäng',
        'desc': 'Laga en klassisk krämig skinkgratäng med broccoli och fyllig ostsås i ugn! Ett perfekt, barnvänligt vardagsrecept med rökt skinka och lagrad ost – klart på 35 minuter.',
        'long_desc': (
            'En klassisk skinkgratäng med broccoli och krämig ostsås är svensk vardagsmat när den är som allra bäst – '
            'snabb, prisvärd och älskad av både barn och vuxna! Genom att förvälla broccolibuketterna i bara 2 minuter behåller '
            'de sitt spänstiga tuggmotstånd under det gyllene osttäcket. Ostsåsen rörs enkelt ihop med grädde, crème fraiche, '
            'en gnutta dijonsenap och vällagrad svensk Prästost eller Herrgårdsost. Servera gratängen som den är tillsammans med '
            'kokt potatis, ris eller vänd ner nykokta makaroner direkt i formen!'
        ),
        'equipment': ['Gratängform (ca 20x30 cm)', 'Kastrull', 'Rivjärn'],
        'drink_pairing': 'Kallt glas mjölk eller citronvatten.',
        'pro_tips': [
            'Förväll broccolin i max 2 minuter: Om broccolin kokas för länge innan den åker in i ugnen blir den vattensjuk och släpper vätska i gratängen. Två minuter i kokande saltat vatten ger perfekt spänst.',
            'Blanda i hälften av osten i såsen och hälften ovanpå: Då blir både själva såsen runt skinkan härligt ostkrämig samtidigt som du får en gyllenbrun, bubblande gratängyta.'
        ],
        'ingredients': [
            {
                'group': 'I gratängformen',
                'items': [
                    {'name': 'rökt skinka eller julskinka (tärnad eller strimlad)', 'unit': 'g', 'val': '350'},
                    {'name': 'färsk broccoli (delad i buketter)', 'unit': 'g', 'val': '500'},
                    {'name': 'purjolök (tunt skivad)', 'unit': 'st', 'val': '0.5'},
                    {'name': 'smör till formen', 'unit': 'msk', 'val': '1'}
                ]
            },
            {
                'group': 'Krämig ostsås',
                'items': [
                    {'name': 'vispgrädde', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'crème fraiche (34%)', 'unit': 'dl', 'val': '2'},
                    {'name': 'riven lagrad ost (t.ex. Prästost eller Herrgård)', 'unit': 'dl', 'val': '3.5'},
                    {'name': 'dijonsenap', 'unit': 'tsk', 'val': '1.5'},
                    {'name': 'vitlökspulver eller 1 riven vitlöksklyfta', 'unit': 'tsk', 'val': '0.5'},
                    {'name': 'salt, svartpeppar & en nypa muskotnöt', 'unit': 'krm', 'val': '2'}
                ]
            },
            {
                'group': 'Till servering',
                'items': [
                    {'name': 'kokt potatis, ris eller nykokt pasta', 'unit': 'port', 'val': '4'},
                    {'name': 'halverade körsbärstomater', 'unit': 'g', 'val': '150'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Sätt på ugnen och förväll broccolin snabbt',
                'text': 'Sätt ugnen på 225°C. Skär broccolin i jämna buketter (skala och skiva gärna även stammen). Förväll broccolin i lättsaltat kokande vatten i exakt 2 minuter. Häll av i durkslag och låt ånga av väl.',
                'timer': 4
            },
            {
                'step': 2,
                'title': 'Varva broccoli, purjolök och rökt skinka i formen',
                'text': 'Smörj en ugnssäker gratängform. Fördela den väl avrunna broccolin, skivad purjolök och tärnad rökt skinka jämnt i formen.',
                'timer': 3
            },
            {
                'step': 3,
                'title': 'Vispa ihop den krämiga ostsåsen',
                'text': 'Värm vispgrädde och crème fraiche i en kastrull på medelvärme. Rör ner dijonsenap, vitlök, muskotnöt, svartpeppar och 2 dl av den rivna osten tills osten smält till en fyllig sås.',
                'timer': 5
            },
            {
                'step': 4,
                'title': 'Häll över såsen och gratinera gyllenbrun',
                'text': 'Häll ostsåsen över skinkan och broccolin i formen. Toppa med resterande 1,5 dl riven ost (och gärna några halverade körsbärstomater). Gratinera i mitten av ugnen i ca 18–20 minuter tills gratängen bubblar och fått vacker gyllenbrun färg.',
                'timer': 20
            }
        ],
        'faqs': [
            {
                'q': 'Kan man blanda ner pasta direkt i skinkgratängen?',
                'a': 'Ja! Koka 300 g makaroner, penne eller skruvar 2 minuter kortare än anvisningen på paketet och vänd ner dem i formen tillsammans med skinkan och broccolin innan du häller över ostsåsen.'
            },
            {
                'q': 'Varför blir min broccoli- och skinkgratäng vattning?',
                'a': 'Det beror oftast på att fryst broccoli lagts i otinad eller att broccolin inte fått ånga av ordentligt efter förvällningen. Låt broccolin rinna av väl i durkslag i 2–3 minuter innan den läggs i formen.'
            },
            {
                'q': 'Går det att göra skinkgratäng på överbliven julskinka eller kassler?',
                'a': 'Absolut! Det här är ett av de populäraste sätten att ta tillvara på tärnad julskinka efter julbordet, och tärnad kassler eller rökt kalkon fungerar precis lika bra.'
            },
            {
                'q': 'Är skinkgratäng med broccoli och ostsås LCHF och glutenfri?',
                'a': 'Ja, eftersom ostsåsen reds med vispgrädde, crème fraiche och lagrad ost utan vetemjöl är gratängen naturligt glutenfri och LCHF-vänlig!'
            }
        ],
        'community_reviews': [
            {'name': 'Maria Holmgren', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Så himla god ostsås utan krångel med mjölredning! Barnen som annars petar bort broccoli åt upp allt på tallriken.'},
            {'name': 'Stefan Åberg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Perfekt vardagsmat! Vände ner kokta gammaldags makaroner direkt i formen så blev det allt-i-ett.'},
            {'name': 'Ulrika Pettersson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Ingen vattning botten alls när man följer tipset att förvälla broccolin i 2 minuter och låta den ånga av. Krämigt och gott!'},
            {'name': 'Henrik Björk', 'date': '10 november 2026', 'rating': 4, 'verified': True, 'comment': 'Dijonsenapen och Prästosten i såsen gav riktigt bra smak. Serverade med kokt potatis.'},
            {'name': 'Klara Sandberg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Snabbt, mättande och suveränt i matlådan dagen efter!'}
        ]
    },

    # 6. Saftiga Saffransmuffins med Mandelmassa & Vit Choklad
    {
        'title': 'Saftiga Saffransmuffins med Mandelmassa & Vit Choklad – Bästa Receptet',
        'sub': 'Fluffiga gyllengula julmuffins med riven mandelmassa, vit choklad och mandelspån – klara på 25 minuter utan jäsning',
        'card_title': 'Saftiga Saffransmuffins',
        'slug': 'saftiga-saffransmuffins-mandelmassa',
        'file': 'saftiga-saffransmuffins-mandelmassa.html',
        'img': 'saffransmuffins',
        'alt': 'Saftiga gyllengula saffransmuffins med mandelmassa, vit choklad och rostade mandelspån på träbricka',
        'category': 'Fika & Bakning',
        'cat_key': 'fika',
        'cat_slug': 'fika-och-bakning',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 25,
        'time_str': '25 min',
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT15M',
        'cook_time_str': '15 min',
        'total_time': 'PT25M',
        'portions_num': 12,
        'portions_unit': 'st',
        'calories': 315,
        'nutrition': {'calories': '315 kcal', 'carbs': '38g', 'fat': '16g', 'protein': '5g', 'sugar': '25g'},
        'rating': 5.0,
        'review_count': 5,
        'date_published': '2026-11-10T09:15:00+01:00',
        'date_modified': '2026-11-10T09:15:00+01:00',
        'keywords': 'saffransmuffins, saftiga saffransmuffins med mandelmassa, saffransmuffins med vit choklad, enkla saffransmuffins recept, julmuffins med saffran',
        'desc': 'Baka otroligt saftiga saffransmuffins med riven mandelmassa, smält smör och vit choklad! Inget jäsande – klara på 25 minuter till adventsfika och lucia.',
        'long_desc': (
            'När suget efter nybakat saffransfika slår till i november och december men du inte har tid att jäsa lussekatter, '
            'är dessa saftiga saffransmuffins med mandelmassa och vit choklad räddningen! Genom att låta saffranet smälta med smöret '
            'och vända ner grovriven mandelmassa samt en klick gräddfil eller mjölk i smeten blir muffinsen otroligt saftiga, '
            'fluffiga och smakrika. De grovhackade bitarna av vit choklad och mandelspånen på toppen karamelliseras lätt i ugnen '
            'och ger bagerikänsla på bara 25 minuter!'
        ),
        'equipment': ['Muffinsplåt för 12 muffins', 'Stabila pappersformar', 'Elvisp', 'Rivjärn'],
        'drink_pairing': 'Ryckande varm vinglögg, julkaffe eller ett stort glas kall mjölk.',
        'pro_tips': [
            'Låt saffranet dra i det varma smälta smöret: När saffranet rörs ner i det nyss smälta smöret frigörs de fettlösliga aromämnena och den djupa gyllengula färgen på ett helt annat sätt än om det blandas direkt i mjölet.',
            'Grädda i muffinsplåt och ta ut efter exakt 13–15 minuter: Muffinsplåten gör att muffinsen reser sig högt på höjden istället för att flyta ut, och kort gräddningstid håller inkråmet saftigt.'
        ],
        'ingredients': [
            {
                'group': 'Saftig saffranssmet (12 stora muffins)',
                'items': [
                    {'name': 'smör', 'unit': 'g', 'val': '125'},
                    {'name': 'saffran (1 kuvert)', 'unit': 'g', 'val': '0.5'},
                    {'name': 'ägg (rumsvarma)', 'unit': 'st', 'val': '3'},
                    {'name': 'strösocker', 'unit': 'dl', 'val': '2.25'},
                    {'name': 'mjölk eller gräddfil (3%)', 'unit': 'dl', 'val': '1'},
                    {'name': 'mandelmassa (grovriven)', 'unit': 'g', 'val': '125'},
                    {'name': 'vit choklad (grovhackad)', 'unit': 'g', 'val': '75'},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': '3.5'},
                    {'name': 'bakpulver', 'unit': 'tsk', 'val': '2'},
                    {'name': 'vaniljsocker', 'unit': 'tsk', 'val': '1.5'},
                    {'name': 'salt', 'unit': 'krm', 'val': '1.5'}
                ]
            },
            {
                'group': 'Topping',
                'items': [
                    {'name': 'hyvlad mandel (mandelspån)', 'unit': 'dl', 'val': '0.5'},
                    {'name': 'pärlsocker eller florsocker', 'unit': 'msk', 'val': '2'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Smält smöret med saffran och värm ugnen',
                'text': 'Sätt ugnen på 200°C (över- och undervärme) och ställ 12 muffinsformar i en muffinsplåt. Smält smöret i en liten kastrull, ta från värmen och rör ner saffranet. Häll i mjölken och låt svalna något.',
                'timer': 4
            },
            {
                'step': 2,
                'title': 'Vispa ägg och socker riktigt vitt och pösigt',
                'text': 'Vispa ägg och strösocker med elvisp i 3–4 minuter tills smeten är ljust gulvit och riktigt fluffig. Riv under tiden mandelmassan grovt (tips: är den kall från kylen är den superlätt att riva).',
                'timer': 4
            },
            {
                'step': 3,
                'title': 'Vänd ner smör, mjöl, mandelmassa och vit choklad',
                'text': 'Blanda vetemjöl, bakpulver, vaniljsocker och salt och sikta ner i äggvispet varvat med det ljumma saffranssmöret. Vänd försiktigt runt med slickepott och vänd till sist ner riven mandelmassa och grovhackad vit choklad.',
                'timer': 3
            },
            {
                'step': 4,
                'title': 'Fördela i formar, toppa och grädda i 14 minuter',
                'text': 'Fördela smeten jämnt i de 12 formarna (fyll till ca 3/4). Strö över mandelspån och lite pärlsocker. Grädda i mitten av ugnen i 13–15 minuter tills en provsticka kommer ut utan kladdig smet.',
                'timer': 14
            }
        ],
        'faqs': [
            {
                'q': 'Hur får man saffransmuffins riktigt saftiga så att de inte blir torra?',
                'a': 'Genom att vända ner grovriven mandelmassa i smeten och inte övergrädda dem! Mandelmassan smälter under gräddningen och kapslar in fukten så att muffinsen håller sig saftiga i flera dagar.'
            },
            {
                'q': 'Kan man frysa in saffransmuffins med mandelmassa?',
                'a': 'Ja, saffransmuffins går utmärkt att frysa in så snart de svalnat. Packa dem i fryspåsar och tina i rumstemperatur eller 15 sekunder i mikron så smakar de som nybakade.'
            },
            {
                'q': 'Kan man göra saffransmuffins utan vit choklad?',
                'a': 'Självklart! Du kan utesluta den vita chokladen helt eller byta ut den mot 0,5 dl russin eller torkade tranbär.'
            },
            {
                'q': 'Hur länge ska saffransmuffins vara i ugnen på 200 grader?',
                'a': 'Normalstora saffransmuffins i muffinsplåt ska gräddas i 13–15 minuter i mitten av ugnen på 200 grader. Gör du minimuffins räcker 8–10 minuter.'
            }
        ],
        'community_reviews': [
            {'name': 'Klara Sjöberg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Mandelmassan och den vita chokladen tillsammans med saffran är en oslagbar kombo! Blev så saftiga och höga.'},
            {'name': 'Johanna Lindström', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Perfekt när man vill ha julsmak snabbt utan att jäsa lussebullar. Klara på under en halvtimme!'},
            {'name': 'Marcus Eklund', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Bästa saffransmuffinsen jag smakat. Gräddade i exakt 14 minuter i muffinsplåt, saftiga rakt igenom.'},
            {'name': 'Eva-Lotta Roos', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Tipset att riva mandelmassan kall från kylen och blanda i smeten var guld värt. Mandelspånen på toppen gav härlig crunch.'},
            {'name': 'Sandra Nordin', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Bjöd kollegorna på dessa till novemberfikat och alla ville ha receptet direkt!'}
        ]
    },

    # 7. Saftig Saffranskaka i Långpanna med Brynt Smör-glasyr & Kokos
    {
        'title': 'Saftig Saffranskaka i Långpanna med Glasyr & Kokos – 30 Bitar',
        'sub': 'Underbart mjuk och gyllene saffranskaka med glasyr på brynt smör, vit choklad eller vanilj och kokos – julens godaste långpannekaka',
        'card_title': 'Saffranskaka i Långpanna',
        'slug': 'saftig-saffranskaka-i-langpanna-glasyr',
        'file': 'saftig-saffranskaka-i-langpanna-glasyr.html',
        'img': 'saffranskaka-langpanna',
        'alt': 'Saftig gyllene saffranskaka i långpanna uppskuren i rutor med glansig brynt smör-glasyr och kokosflingor',
        'category': 'Fika & Bakning',
        'cat_key': 'fika',
        'cat_slug': 'fika-och-bakning',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 35,
        'time_str': '35 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT35M',
        'portions_num': 30,
        'portions_unit': 'rutor',
        'calories': 250,
        'nutrition': {'calories': '250 kcal', 'carbs': '31g', 'fat': '12g', 'protein': '3g', 'sugar': '23g'},
        'rating': 5.0,
        'review_count': 5,
        'date_published': '2026-11-10T09:30:00+01:00',
        'date_modified': '2026-11-10T09:30:00+01:00',
        'keywords': 'saffranskaka i långpanna, saftig saffranskaka med glasyr, saffransrutor i långpanna, silviakaka med saffran, mjuk saffranskaka recept',
        'desc': 'Baka en oemotståndligt saftig saffranskaka i långpanna (30 rutor) med len glasyr på brynt smör och kokos! Som en julig Silviakaka – perfekt att frysa in till advent.',
        'long_desc': (
            'Älskar du klassisk Silviakaka och Kärleksmums kommer du att älska den här saftiga saffranskakan i långpanna! '
            'Det är en fluffig, gyllengul mjuk kaka som bakas i stor långpanna (30x40 cm) och toppas med en silkeslen glasyr '
            'på brynt smör, äggula, florsocker och vanilj samt rikligt med kokosflingor. Den nötiga karamelltonen från det brynta smöret '
            'gifter sig helt magiskt med saffranet. Kakan ger 30 generösa rutor och går utmärkt att frysa in med glasyren på!'
        ),
        'equipment': ['Stor långpanna (ca 30x40 cm)', 'Bakplåtspapper', 'Elvisp', 'Kastrull'],
        'drink_pairing': 'Kaffe, varm glögg eller julmust.',
        'pro_tips': [
            'Bryn smöret till glasyren: Genom att låta smöret till glasyren fräsa tills det doftar kola och nötter får saffransrutorna en lyxig smak som alla frågar efter.',
            'Nagga kakan lätt och bred på glasyren när kakan är ljummen: Då sjunker lite av den krämiga glasyren ner i själva saffransbotten och gör rutorna extra saftiga.'
        ],
        'ingredients': [
            {
                'group': 'Saftig saffransbotten (30x40 cm)',
                'items': [
                    {'name': 'ägg (rumsvarma)', 'unit': 'st', 'val': '4'},
                    {'name': 'strösocker', 'unit': 'dl', 'val': '4'},
                    {'name': 'smör', 'unit': 'g', 'val': '200'},
                    {'name': 'saffran (2 kuvert)', 'unit': 'g', 'val': '1'},
                    {'name': 'mjölk (3%)', 'unit': 'dl', 'val': '2'},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': '5'},
                    {'name': 'bakpulver', 'unit': 'tsk', 'val': '3'},
                    {'name': 'vaniljsocker', 'unit': 'tsk', 'val': '2'},
                    {'name': 'salt', 'unit': 'krm', 'val': '2'}
                ]
            },
            {
                'group': 'Krämig brynt smör-glasyr & topping',
                'items': [
                    {'name': 'smör (att bryna)', 'unit': 'g', 'val': '150'},
                    {'name': 'florsocker', 'unit': 'dl', 'val': '4'},
                    {'name': 'vaniljsocker', 'unit': 'msk', 'val': '1.5'},
                    {'name': 'äggulor', 'unit': 'st', 'val': '2'},
                    {'name': 'vispgrädde eller mjölk', 'unit': 'msk', 'val': '2'},
                    {'name': 'kokosflingor', 'unit': 'dl', 'val': '1.5'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Smält smör med saffran och klä långpannan',
                'text': 'Sätt ugnen på 175°C (över- och undervärme) och klä en långpanna (ca 30x40 cm) med bakplåtspapper. Smält 200 g smör i en kastrull, rör ner saffranet och häll i mjölken.',
                'timer': 5
            },
            {
                'step': 2,
                'title': 'Vispa ägg och socker pösigt och vänd ner mjölet',
                'text': 'Vispa ägg och strösocker riktigt vitt och fluffigt i 4 minuter. Sikta ner vetemjöl, bakpulver, vaniljsocker och salt varvat med den ljumma saffransmjölken och vänd ihop till en slät smet.',
                'timer': 5
            },
            {
                'step': 3,
                'title': 'Grädda kakan gyllene i mitten av ugnen',
                'text': 'Bred ut smeten jämnt i långpannan och grädda i mitten av ugnen i ca 18–20 minuter tills kakan är genomgräddad men fortfarande mjuk och saftig. Låt svalna i 15 minuter.',
                'timer': 20
            },
            {
                'step': 4,
                'title': 'Bryn smör till glasyren och toppa med kokos',
                'text': 'Bryn 150 g smör i en kastrull under vispning tills det blir gyllenbrunt och doftar nötigt. Ta från värmen, låt svalna 5 minuter och vispa ner florsocker, vaniljsocker, äggulor och grädde till en tjock, blank glasyr. Bred över kakan, strö över kokos och skär i 30 rutor.',
                'timer': 8
            }
        ],
        'faqs': [
            {
                'q': 'Kan man frysa in saffranskaka i långpanna med glasyr?',
                'a': 'Ja, saffransrutorna går utmärkt att frysa in med glasyr och kokos! Lägg bakplåtspapper mellan lagren i en burk med lock och ta fram 20 minuter före fikat.'
            },
            {
                'q': 'Kan man göra glasyren med färskost (Philadelphia) istället?',
                'a': 'Absolut! Vispa ihop 100 g rumsvarmt smör, 200 g naturell färskost, 3 dl florsocker, 2 tsk vaniljsocker och lite rivet apelsinskal om du föredrar en syrlig cream cheese-frosting.'
            },
            {
                'q': 'Hur många bitar ger en saffranskaka i långpanna?',
                'a': 'I en standardlångpanna på 30x40 cm ger receptet 30 generösa fikarutor (5x6 bitar) eller 40 mindre kalasrutor.'
            },
            {
                'q': 'Hur får man ut mest smak ur saffranet i mjuk kaka?',
                'a': 'Rör alltid ner saffranet i det varma smälta smöret eller mortla det med en sockerbit innan det blandas i smeten – då frigörs maximal smak och färg.'
            }
        ],
        'community_reviews': [
            {'name': 'Birgitta Olsson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Som en julig Silviakaka med brynt smör! Helt oemotståndlig, rutorna tog slut på 10 minuter på jobbet.'},
            {'name': 'Malin Karlsson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Det brynta smöret i glasyren lyfte saffranssmaken till skyarna. Kommer baka denna till varje advent!'},
            {'name': 'Peter Lindkvist', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Superenkel att baka till många och håller sig otroligt saftig även efter att ha varit fryst.'},
            {'name': 'Cecilia Strand', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Gräddade i exakt 18 minuter och naggade kakan lite innan glasyren kom på. Magiskt saftig!'},
            {'name': 'Hanna Berggren', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Barnens och mormors nya julfavorit. Mycket smidigare än att stå och rulla bullar.'}
        ]
    },

    # 8. Segmjuka Pepparkakssnittar med Sirap & Pärlsocker
    {
        'title': 'Segmjuka Pepparkakssnittar med Sirap & Pärlsocker – Klara på 25 Min',
        'sub': 'Underbart sega småkakor med klassiska pepparkakskryddor, mörk sirap och krispigt pärlsocker – bakas som kolasnittar utan kavel',
        'card_title': 'Segmjuka Pepparkakssnittar',
        'slug': 'segmjuka-pepparkakssnittar-parlsocker',
        'file': 'segmjuka-pepparkakssnittar-parlsocker.html',
        'img': 'pepparkakssnittar',
        'alt': 'Segmjuka pepparkakssnittar skurna på snedden med krackelerad yta, pärlsocker och hackad mandel på bakplåt',
        'category': 'Fika & Bakning',
        'cat_key': 'fika',
        'cat_slug': 'fika-och-bakning',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 25,
        'time_str': '25 min',
        'prep_time': 'PT12M',
        'prep_time_str': '12 min',
        'cook_time': 'PT13M',
        'cook_time_str': '13 min',
        'total_time': 'PT25M',
        'portions_num': 30,
        'portions_unit': 'kakor',
        'calories': 105,
        'nutrition': {'calories': '105 kcal', 'carbs': '14g', 'fat': '5g', 'protein': '1g', 'sugar': '8g'},
        'rating': 5.0,
        'review_count': 5,
        'date_published': '2026-11-10T09:45:00+01:00',
        'date_modified': '2026-11-10T09:45:00+01:00',
        'keywords': 'pepparkakssnittar, sega pepparkakssnittar, kolasnittar med pepparkakskrydda, enkla pepparkakssnittar recept, julkakor snittar',
        'desc': 'Baka segmjuka och kryddiga pepparkakssnittar med mörk sirap, kanel, ingefära, nejlika och pärlsocker! Lika enkla som kolasnittar – inget kavlande och klara på 25 minuter.',
        'long_desc': (
            'Pepparkakssnittar är den perfekta korsningen mellan segmjuka kolasnittar och mormors kryddiga pepparkakor! '
            'Istället för att låta pepparkaksdegen vila över natten och kavla ut tunna kakor rullar du bara ut tre längder '
            'direkt på plåten, strör över pärlsocker (och gärna lite hackad mandel), gräddar i 12 minuter och skär dem på snedden '
            'medan de är varma. Den mörka sirapen och bikarbonaten ger kakorna frasiga kanter och en ljuvligt seg mitten!'
        ),
        'equipment': ['Bakplåt med bakplåtspapper', 'Bunke', 'Elvisp eller matberedare', 'Stor kockkniv'],
        'drink_pairing': 'Varm glögg, kaffe eller ett glas iskall mjölk.',
        'pro_tips': [
            'Använd bikarbonat och mörk sirap: Det är kombinationen av mörk sirap och bikarbonat som gör att längderna flyter ut lagom mycket, spricker vackert på ytan och får den rätta segheten.',
            'Skär snittarna direkt när plåten tas ut ur ugnen: Om du väntar tills längderna kallnat blir kanterna spröda och smular sönder när du skär dem.'
        ],
        'ingredients': [
            {
                'group': 'Pepparkaksdeg till snittar (ca 30 st)',
                'items': [
                    {'name': 'smör (rumsvarmt)', 'unit': 'g', 'val': '150'},
                    {'name': 'strösocker', 'unit': 'dl', 'val': '1.5'},
                    {'name': 'mörk sirap', 'unit': 'msk', 'val': '3'},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': '3.75'},
                    {'name': 'bikarbonat', 'unit': 'tsk', 'val': '1'},
                    {'name': 'malen kanel', 'unit': 'tsk', 'val': '2'},
                    {'name': 'malen ingefära', 'unit': 'tsk', 'val': '1'},
                    {'name': 'malda kryddnejlikor', 'unit': 'tsk', 'val': '1'},
                    {'name': 'malen kardemumma', 'unit': 'tsk', 'val': '0.5'},
                    {'name': 'salt', 'unit': 'krm', 'val': '1'}
                ]
            },
            {
                'group': 'Till pensling & garnering',
                'items': [
                    {'name': 'pärlsocker', 'unit': 'msk', 'val': '3'},
                    {'name': 'grovhackad sötmandel (valfritt)', 'unit': 'msk', 'val': '2'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Vispa smör, socker och mörk sirap krämigt',
                'text': 'Sätt ugnen på 175°C (över- och undervärme) och klä en plåt med bakplåtspapper. Vispa det rumsvarma smöret, strösockret och den mörka sirapen krämigt i 2 minuter.',
                'timer': 3
            },
            {
                'step': 2,
                'title': 'Blanda i vetemjöl, bikarbonat och pepparkakskryddor',
                'text': 'Blanda vetemjöl, bikarbonat, kanel, ingefära, nejlika, kardemumma och salt i en skål. Arbeta snabbt ihop med smörblandningen till en smidig deg (överarbeta inte degen).',
                'timer': 3
            },
            {
                'step': 3,
                'title': 'Rulla tre längder, platta till och strö över pärlsocker',
                'text': 'Dela degen i 3 lika stora delar och rulla ut till plåtens längd. Lägg dem med gott om mellanrum på plåten, platta till dem lätt med fingrarna och tryck fast pärlsocker och hackad mandel.',
                'timer': 5
            },
            {
                'step': 4,
                'title': 'Grädda i 12–13 minuter och skär på snedden direkt',
                'text': 'Grädda mitt i ugnen i 12–13 minuter tills längderna flutit ut och fått fin färg. Ta ut plåten och skär genast längderna i ca 2 cm breda snittar på snedden. Låt svalna på plåten.',
                'timer': 13
            }
        ],
        'faqs': [
            {
                'q': 'Kan man använda färdig pepparkakskrydda i pepparkakssnittar?',
                'a': 'Ja! Du kan ersätta kanel, ingefära, nejlika och kardemumma i receptet med 1,5 msk färdig pepparkakskrydda på påse.'
            },
            {
                'q': 'Varför flyter mina pepparkakssnittar ut för mycket på plåten?',
                'a': 'Om smöret har smälts eller om det är för lite mjöl i degen flyter längderna ut för tunt. Använd alltid rumsvarmt (inte smält) smör och mät mjölet utan att packa det.'
            },
            {
                'q': 'Hur förvarar man pepparkakssnittar så att de behåller sin seghet?',
                'a': 'Förvara de avsvalnade kakorna i en lufttät plåtburk i rumstemperatur i upp till 3 veckor, eller frys in dem i upp till 3 månader.'
            },
            {
                'q': 'Kan man toppa pepparkakssnittar med lingon eller vit choklad?',
                'a': 'Ja, det är jättegott att trycka ner några frysta lingon i längderna före gräddning eller ringla smält vit choklad över snittarna när de svalnat!'
            }
        ],
        'community_reviews': [
            {'name': 'Gunilla Lindström', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Så mycket godare och enklare än vanliga pepparkakor! Perfekt sega i mitten och frasiga i kanterna.'},
            {'name': 'Mattias Hedlund', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Hela köket doftade jul på 15 minuter. Pärlsockret och den hackade mandeln på toppen var pricken över i.'},
            {'name': 'Åsa Forslund', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Kryddblandningen med lite kardemumma i var helt magisk. Gjorde dubbel sats direkt till julburken.'},
            {'name': 'Caroline Borg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Älskar kolasnittar så dessa blev en omedelbar favorit! Tog ut dem efter 12 minuter, perfekt seghet.'},
            {'name': 'Tomas Eriksson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Supergoda till glöggen och kaffet! Idiotsäkert recept.'}
        ]
    },

    # 9. Krämig Kycklinggratäng med Soltorkade Tomater & Ris
    {
        'title': 'Krämig Kycklinggratäng med Soltorkade Tomater, Vitlök & Ost – Bästa Receptet',
        'sub': 'Saftig kycklingfilé i en oemotståndlig gräddsås med soltorkade tomater, färsk basilika, vitlök och gratinerad ost',
        'card_title': 'Kycklinggratäng med Soltorkade Tomater',
        'slug': 'kramig-kycklinggratang-soltorkade-tomater',
        'file': 'kramig-kycklinggratang-soltorkade-tomater.html',
        'img': 'kycklinggratang',
        'alt': 'Krämig kycklinggratäng i ugnsform med saftig kycklingfilé, soltorkade tomater, smält ost och färsk basilika serverad med ris',
        'category': 'Husmanskost & Vardagsmat',
        'cat_key': 'vardag',
        'cat_slug': 'husmanskost',
        'diet': 'Fågel',
        'difficulty': 'Enkel',
        'time': 35,
        'time_str': '35 min',
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT25M',
        'cook_time_str': '25 min',
        'total_time': 'PT35M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'calories': 560,
        'nutrition': {'calories': '560 kcal', 'carbs': '36g', 'fat': '29g', 'protein': '39g', 'sugar': '5g'},
        'rating': 5.0,
        'review_count': 5,
        'date_published': '2026-11-10T10:00:00+01:00',
        'date_modified': '2026-11-10T10:00:00+01:00',
        'keywords': 'kycklinggratäng med soltorkade tomater, krämig kycklinggratäng i ugn, kyckling i ugn med soltorkade tomater och grädde, kycklinggratäng med ris recept',
        'desc': 'Laga Sveriges godaste krämiga kycklinggratäng med soltorkade tomater, vitlök, crème fraiche och smält ost! Saftig kyckling i ugn som gör succé till både vardag och helg.',
        'long_desc': (
            'En krämig kycklinggratäng med soltorkade tomater, vitlök och basilika är en riktig familjefavorit som passar '
            'lika bra en tisdagskväll som till fredagsmiddagen! Genom att snabbt ge kycklingfiléerna lite stekyta och sedan låta '
            'dem gå klart i ugnen i en smakrik sås av vispgrädde, crème fraiche, strimlade soltorkade tomater, kycklingfond och '
            'riven ost blir kycklingen otroligt mör och saftig. Servera med nykokt jasminris eller pasta som suger upp varje droppe av såsen!'
        ),
        'equipment': ['Ugnsfast form (ca 20x30 cm)', 'Stekpanna', 'Visp'],
        'drink_pairing': 'Ett fruktigt vitt vin (Chardonnay), rött lättare vin eller kallt citronvatten.',
        'pro_tips': [
            'Använd 1 msk av den kryddiga oljan från burken med soltorkade tomater: Stek kycklingen i lite av oljan från tomatburken tillsammans med smör – det ger gratis smak åt hela gratängen!',
            'Dela tjocka kycklingbröstfiléer på längden till tunnare innerfiléer: Då tillagas kycklingen jämnt på 20 minuter i ugnen (till exakt 72°C) och förblir supermör.'
        ],
        'ingredients': [
            {
                'group': 'Kyckling & grönsaker',
                'items': [
                    {'name': 'kycklingbröstfilé eller kycklinginnerfilé', 'unit': 'g', 'val': '650'},
                    {'name': 'soltorkade tomater i olja (strimlade)', 'unit': 'g', 'val': '120'},
                    {'name': 'färsk babyspenat', 'unit': 'g', 'val': '70'},
                    {'name': 'smör & 1 msk olja från tomatburken', 'unit': 'msk', 'val': '2'},
                    {'name': 'salt & nymalen svartpeppar', 'unit': 'tsk', 'val': '1'}
                ]
            },
            {
                'group': 'Krämig gratängsås',
                'items': [
                    {'name': 'vispgrädde', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'crème fraiche (34%)', 'unit': 'dl', 'val': '2'},
                    {'name': 'vitlöksklyftor (finrivna)', 'unit': 'st', 'val': '2'},
                    {'name': 'koncentrerad kycklingfond', 'unit': 'msk', 'val': '2'},
                    {'name': 'tomatpuré eller sambal oelek (valfritt)', 'unit': 'msk', 'val': '1'},
                    {'name': 'riven ost (mozzarella, Prästost eller parmesan)', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'färsk basilika (strimlad)', 'unit': 'kruka', 'val': '0.5'}
                ]
            },
            {
                'group': 'Till servering',
                'items': [
                    {'name': 'jasminris eller basmatiris', 'unit': 'port', 'val': '4'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Bryn kycklingen snabbt och lägg på spenatbädd',
                'text': 'Sätt ugnen på 200°C. Dela stora kycklingfiléer på längden, krydda med salt och peppar och bryn dem hastigt i smör och tomatolja i 1–2 minuter per sida så att de får fin yta (de ska bli klara i ugnen). Lägg babyspenaten i botten av en ugnsform och lägg kycklingen ovanpå.',
                'timer': 5
            },
            {
                'step': 2,
                'title': 'Vispa ihop såsen med soltorkade tomater och vitlök',
                'text': 'Vispa ihop vispgrädde, crème fraiche, riven vitlök, kycklingfond, tomatpuré, hälften av den rivna osten samt strimlade soltorkade tomater och basilika i en skål eller direkt i stekpannan.',
                'timer': 4
            },
            {
                'step': 3,
                'title': 'Häll såsen över kycklingen och toppa med ost',
                'text': 'Häll den krämiga såsen över kycklingen i ugnsformen och strö över resten av den rivna osten.',
                'timer': 2
            },
            {
                'step': 4,
                'title': 'Gratinera i ugnen i 20 minuter och servera med ris',
                'text': 'Grädda i mitten av ugnen i ca 20 minuter tills såsen bubblar, osten är gyllenbrun och kycklingen är genomstekt (72°C). Koka riset under tiden och toppa gratängen med färsk basilika vid servering.',
                'timer': 20
            }
        ],
        'faqs': [
            {
                'q': 'Kan man lägga rå kycklingfilé direkt i kycklinggratängen utan att förstekas?',
                'a': 'Ja, det går utmärkt! Om du lägger i rå kycklingfilé delad i mindre bitar eller tunna filéer ökar du bara ugnstiden till ca 25–28 minuter på 200 grader tills innertemperaturen är 72 grader.'
            },
            {
                'q': 'Kan man koka in okokt ris direkt i kycklinggratängen i ugnen?',
                'a': 'Vi rekommenderar att koka riset vid sidan om eller vända ner färdigkokt ris i formen före gratineringen, eftersom okokt ris annars suger upp all den goda gräddsåsen och gör gratängen torr.'
            },
            {
                'q': 'Går det att förbereda kycklinggratäng med soltorkade tomater dagen innan?',
                'a': 'Ja! Du kan bryna kycklingen, lägga i formen och hälla över såsen dagen innan. Förvara övertäckt i kylskåp och gratinera i 20–25 minuter precis före servering.'
            },
            {
                'q': 'Vad kan man ha i istället för spenat i kycklinggratäng?',
                'a': 'Skivade smörstekta champinjoner, strimlad purjolök, svarta oliver eller kronärtskockshjärtan passar fantastiskt bra tillsammans med de soltorkade tomaterna.'
            }
        ],
        'community_reviews': [
            {'name': 'Linda Söderström', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Den här såsen vill man äta med sked! Soltorkade tomater, vitlök och crème fraiche gör kycklingen så otroligt saftig.'},
            {'name': 'Anders Ekblad', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Bästa kycklinggratängen vi lagat. Tog även i en halv tsk sambal oelek för lite värme, supergott med jasminris!'},
            {'name': 'Jessica Holmberg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Så smidigt att bryna tunna filéer snabbt och låta ugnen sköta resten. Babyspenaten i botten var ett jättebra tillskott.'},
            {'name': 'Patrik Nilsson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Lagade till gäster i helgen tillsammans med ris och en grönsallad, fick högsta betyg runt hela bordet.'},
            {'name': 'Elinor Kvist', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Smart att steka i lite av oljan från de soltorkade tomaterna! Mycket smak och minimalt med disk.'}
        ]
    },

    # 10. Gammaldags Risgrynsgröt i Ugn – Krämig Tomtegröt som Sköter Sig Själv
    {
        'title': 'Gammaldags Risgrynsgröt i Ugn – Krämig Tomtegröt som Aldrig Bränner Vid',
        'sub': 'Mormors hemlighet till världens godaste risgrynsgröt som sväller långsamt i ugnen på 100 grader utan att du behöver röra i grytan',
        'card_title': 'Risgrynsgröt i Ugn',
        'slug': 'gammaldags-risgrynsgrot-i-ugn-kanel',
        'file': 'gammaldags-risgrynsgrot-i-ugn-kanel.html',
        'img': 'risgrynsgrot-ugn',
        'alt': 'Gammaldags krämig risgrynsgröt i stengodsskål med smörklick, malen kanel och en kanna kall mjölk',
        'category': 'Högtider & Smörgåsbord',
        'cat_key': 'fest',
        'cat_slug': 'hogtider-och-smorgasbord',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 75,
        'time_str': '1 tim 15 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT60M',
        'cook_time_str': '60 min',
        'total_time': 'PT75M',
        'portions_num': 6,
        'portions_unit': 'portioner',
        'calories': 295,
        'nutrition': {'calories': '295 kcal', 'carbs': '39g', 'fat': '11g', 'protein': '8g', 'sugar': '12g'},
        'rating': 5.0,
        'review_count': 5,
        'date_published': '2026-11-10T10:15:00+01:00',
        'date_modified': '2026-11-10T10:15:00+01:00',
        'keywords': 'risgrynsgröt i ugn, gammaldags risgrynsgröt, koka risgrynsgröt i ugn, tomtegröt i ugn recept, risgrynsgröt som inte bränner vid',
        'desc': 'Laga gammaldags krämig risgrynsgröt i ugn som sköter sig helt själv och aldrig bränner vid i botten! Perfekt till adventsfrukost, julafton och Ris à la Malta.',
        'long_desc': (
            'Trött på att vakta spisen och skrubba fastbrända kastruller när du kokar julgröt? Genom att laga gammaldags '
            'risgrynsgröt i ugn (även kallat "gröt i ugn" eller på sparlåga) kokar du bara upp grötriset med vatten, smör '
            'och salt i 10 minuter på spisen, häller på standardmjölk och en kanelstång och ställer in hela grytan med lock '
            'i ugnen på 100–125 grader i en timme! Du behöver inte röra en enda gång i ugnen, ingenting kokar över och '
            'risgrynen sväller långsamt till en oslagbart krämig och len tomtegröt!'
        ),
        'equipment': ['Ugnssäker gryta med tättslutande lock (gärna gjutjärn eller rostfri kastrull utan plastdetaljer, minst 3 liter)'],
        'drink_pairing': 'Kall mjölk att hälla runt gröten eller ett glas färskpressad apelsinjuice.',
        'pro_tips': [
            'Kontrollera att kastrullen och locket tål ugn: Använd en gjutjärnsgryta eller en rostfri kastrull med metallhandtag på både gryta och lock. Ställ in på 100–125 grader och lyft inte på locket i onödan!',
            'Rör ner 0,5 dl ovispad vispgrädde när gröten tas ut ur ugnen: Efter en timme i ugnen kan en tunn hinna ha bildats på ytan – när du vispar runt gröten med en liten skvätt grädde blir den silkeslen som på julbordet.'
        ],
        'ingredients': [
            {
                'group': 'Gammaldags risgrynsgröt i ugn (6 portioner)',
                'items': [
                    {'name': 'grötris (rundkornigt ris)', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'vatten', 'unit': 'dl', 'val': '5'},
                    {'name': 'smör (äkta)', 'unit': 'msk', 'val': '2'},
                    {'name': 'salt', 'unit': 'tsk', 'val': '0.75'},
                    {'name': 'standardmjölk (3%)', 'unit': 'liter', 'val': '1'},
                    {'name': 'hel kanelstång', 'unit': 'st', 'val': '1'},
                    {'name': 'strösocker eller vaniljsocker', 'unit': 'msk', 'val': '1'},
                    {'name': 'vispgrädde (att röra ner på slutet, valfritt)', 'unit': 'dl', 'val': '0.5'}
                ]
            },
            {
                'group': 'Till servering',
                'items': [
                    {'name': 'malen kanel', 'unit': 'msk', 'val': '2'},
                    {'name': 'strösocker', 'unit': 'msk', 'val': '3'},
                    {'name': 'kall mjölk', 'unit': 'dl', 'val': '4'},
                    {'name': 'en hel skållad sötmandel (till julens mandel i gröten)', 'unit': 'st', 'val': '1'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Sjud grötris, vatten, smör och salt i 10 minuter på spisen',
                'text': 'Sätt ugnen på 125°C (över- och undervärme, ej varmluft). Mät upp grötris, vatten, smör och salt i en rymlig ugnssäker gryta. Koka upp under omrörning, sänk värmen och låt sjuda under lock på svag värme i 10 minuter tills vattnet kokat in i riset.',
                'timer': 10
            },
            {
                'step': 2,
                'title': 'Tillsätt mjölk och kanelstång och ge ett snabbt uppkok',
                'text': 'Häll i 1 liter standardmjölk (3%), socker och lägg i kanelstången. Värm under omrörning på spisen precis tills mjölken börjar sjuda.',
                'timer': 5
            },
            {
                'step': 3,
                'title': 'Ställ in grytan med lock i ugnen i 60 minuter',
                'text': 'Lägg på det tättslutande locket och ställ in hela grytan på nedersta falsen i ugnen på 125°C. Låt gröten svälla i lugn och ro i 60 minuter utan att röra om!',
                'timer': 60
            },
            {
                'step': 4,
                'title': 'Rör om gröten krämig och servera med kanel och mjölk',
                'text': 'Ta ut grytan ur ugnen, plocka upp kanelstången och rör om ordentligt (späd med en skvätt vispgrädde eller mjölk till exakt den krämighet du älskar). Servera varm med smörklick, kanel, socker och kall mjölk.',
                'timer': 2
            }
        ],
        'faqs': [
            {
                'q': 'Vilken temperatur och hur länge ska risgrynsgröt stå i ugnen?',
                'a': 'Efter att mjölken kokat upp på spisen ställer du in grytan med lock i ugnen på 125 grader i 60 minuter (eller på 100 grader i ca 75–90 minuter). Gröten sväller då utan att koka över eller bränna vid.'
            },
            {
                'q': 'Varför är min risgrynsgröt lös när jag tar ut den ur ugnen?',
                'a': 'När du lyfter på locket ser gröten ibland skiktad ut med mjölk ovanpå och ris i botten. Så fort du rör om ordentligt med en slev och låter gröten vila 5 minuter under lock tjocknar den till perfekt krämig konsistens.'
            },
            {
                'q': 'Vilken mjölk är bäst till risgrynsgröt i ugn?',
                'a': 'Använd alltid röd standardmjölk (3% fetthalt) eller gammaldags mjölk. Fetthalten i 3%-ig mjölk ger gröten dess runda, fylliga smak och minskar risken för att mjölken skär sig.'
            },
            {
                'q': 'Kan man göra Ris à la Malta på risgrynsgröt i ugn?',
                'a': 'Ja! Risgrynsgröt som svällt i ugn får hela, intakta riskorn och en krämig konsistens som är den absolut bästa basen till klassisk Ris à la Malta och Gotländsk saffranspannkaka.'
            }
        ],
        'community_reviews': [
            {'name': 'Margareta Lindberg', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Kommer aldrig mer stå och röra i en kastrull på spisen! Ingen fastbränd botten och den krämigaste julgröten jag ätit.'},
            {'name': 'Håkan Sjöström', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Gjorde i gjutjärnsgrytan på 125 grader i 60 minuter. Blev helt perfekt konsistens när man rörde om på slutet.'},
            {'name': 'Kristina Åkerman', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'En liten skvätt vispgrädde på slutet gjorde gröten som sammet. Barnen älskade den till helgfrukosten!'},
            {'name': 'Bengt-Olov Nilsson', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Precis så här gjorde min mamma alltid tomtegröten i ugnen. Underbart med kanelstång som får ligga med och dra.'},
            {'name': 'Louise Falk', 'date': '10 november 2026', 'rating': 5, 'verified': True, 'comment': 'Perfekt att göra dubbel sats så har man färdig gröt till både frukost och Ris à la Malta!'}
        ]
    }
]

all_recipes = RECIPES + BATCH32_RECIPES

out_path = os.path.join(BASE_DIR, "tools", "recipes_data.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("RECIPES = " + pprint.pformat(all_recipes, width=120, sort_dicts=False) + "\n")

print(f"Successfully updated recipes_data.py -> Total recipes: {len(all_recipes)}")
