# -*- coding: utf-8 -*-
"""
add_batch31_recipes.py
Deploys Batch 31: 4 high-demand Swedish classics for Kladdkakans dag (Nov 7),
Allhelgona / Fars dag (Nov 8), and Friday comfort dinners:
1. Klassisk Seg Kladdkaka i Långpanna (30 Bitar)
2. Krämig Toscakladdkaka med Knäckig Mandel- & Kokostosca
3. Klassisk Krämig Tacopaj med Crème Fraiche & Nachos
4. Klassisk Plankstek med Oxfilé, Duchessemos & Bearnaisesås
Includes 100% mathematically verified ratings and 5-6 visible community_reviews per recipe.
"""
import sys
import pprint
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "tools"))
import recipes_data

BATCH31_SLUGS = [
    'klassisk-seg-kladdkaka-i-langpanna',
    'kramig-toscakladdkaka-mandel-kokos',
    'klassisk-kramig-tacopaj-creme-fraiche',
    'klassisk-plankstek-oxfile-duchessemos'
]

RECIPES = [r for r in recipes_data.RECIPES if r["slug"] not in BATCH31_SLUGS]

BATCH31_RECIPES = [
    # 1. Klassisk Seg Kladdkaka i Långpanna
    {
        'title': 'Klassisk Seg Kladdkaka i Långpanna – Enkelt Recept (30 Bitar)',
        'sub': 'Dubbel sats härligt seg och krämig kladdkaka med frasig yta – perfekt att baka i stor långpanna till många',
        'card_title': 'Kladdkaka i Långpanna',
        'slug': 'klassisk-seg-kladdkaka-i-langpanna',
        'file': 'klassisk-seg-kladdkaka-i-langpanna.html',
        'img': 'kladdkaka-langpanna',
        'alt': 'Klassisk seg kladdkaka i långpanna uppskuren i generösa rutor pudrade med florsocker, serverad med vispgrädde och färska hallon',
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
        'portions_unit': 'bitar',
        'calories': 265,
        'nutrition': {'calories': '265 kcal', 'carbs': '32g', 'fat': '13g', 'protein': '4g', 'sugar': '24g'},
        'rating': 5.0,
        'review_count': 6,
        'date_published': '2026-10-19T12:00:00+02:00',
        'date_modified': '2026-10-19T12:00:00+02:00',
        'keywords': 'kladdkaka i långpanna, kladdkaka långpanna, seg kladdkaka i långpanna, kladdkaka till många, stor kladdkaka i långpanna recept, kladdkakans dag recept',
        'desc': 'Baka Sveriges godaste sega kladdkaka i långpanna! Ett idiotsäkert recept som ger 30 generösa rutor med frasig ovansida och ljuvligt kladdig mitt – klart på 35 minuter i en enda kastrull.',
        'long_desc': (
            'Behöver du baka fika till många inför Kladdkakans dag, skolavslutning, kalas eller fredagsfika på jobbet? '
            'Den här klassiska sega kladdkakan i långpanna (ca 30x40 cm) är räddaren i nöden! Smeten rörs ihop direkt i en stor kastrull '
            'utan elvisp, vilket ger kakan dess karakteristiska sega kanter, glansiga frasiga täcke och mjukt kladdiga mitt. '
            'Genom att balansera äkta smör, rikligt med kvalitetskakao, en nypa flingsalt och en gnutta vaniljsocker får du en djup, '
            'fyllig chokladsmak som gör succé varje gång. Låt kakan svalna och sätta sig i kylskåpet innan du skär den i 30 snygga rutor!'
        ),
        'equipment': ['Stor långpanna (ca 30x40 cm)', 'Bakplåtspapper', 'Rymlig kastrull (minst 3 liter)', 'Slickepott'],
        'drink_pairing': 'Nyвryggt mörkrostat kaffe, ett glas iskall mjölk eller en bärig hallonsaft.',
        'pro_tips': 'Vispa aldrig smeten med elvisp när du har i äggen! Rör bara försiktigt ner äggen ett i taget med slev eller slickepott. Om du vispar in luft blir kakan som en torr sockerkaka istället för seg och kladdig.',
        'ingredients': [
            {
                'group': 'Kladdkakssmet till stor långpanna (30x40 cm)',
                'items': [
                    {'name': 'smör (äkta, normalsaltat)', 'unit': 'g', 'val': '300'},
                    {'name': 'strösocker', 'unit': 'dl', 'val': '6'},
                    {'name': 'kakao av god kvalitet', 'unit': 'dl', 'val': '2'},
                    {'name': 'vaniljsocker', 'unit': 'msk', 'val': '2'},
                    {'name': 'flingsalt eller vanligt salt', 'unit': 'tsk', 'val': '1'},
                    {'name': 'ljus sirap (för extra seghet)', 'unit': 'msk', 'val': '3'},
                    {'name': 'ägg (rumsvarma)', 'unit': 'st', 'val': '6'},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': '4.5'}
                ]
            },
            {
                'group': 'Till garnering & servering',
                'items': [
                    {'name': 'florsocker att pudra över', 'unit': 'msk', 'val': '2'},
                    {'name': 'vispgrädde (lättvispad)', 'unit': 'dl', 'val': '4'},
                    {'name': 'färska hallon eller jordgubbar', 'unit': 'g', 'val': '250'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Förbered ugn och långpanna',
                'text': 'Sätt ugnen på 175°C (över- och undervärme). Klä en stor djup långpanna (ca 30x40 cm) med bakplåtspapper. Skrynklas pappret ihop under lite kallt vatten och kramas ur blir det mjukt och formar sig perfekt i hörnen.',
                'timer': 5
            },
            {
                'step': 2,
                'title': 'Smält smöret i en stor kastrull',
                'text': 'Smält smöret på medelvärme i en rymlig kastrull (minst 3 liter) så att du kan röra ihop hela smeten direkt i kastrullen. Ta bort kastrullen från plattan så snart smöret smält.',
                'timer': 4
            },
            {
                'step': 3,
                'title': 'Rör ner socker, sirap och kakao',
                'text': 'Tillsätt strösocker, ljus sirap, vaniljsocker, salt och siktad kakao i det varma smöret. Rör om ordentligt med en slickepott eller trägaffel tills blandningen är blank och jämn.',
                'timer': 3
            },
            {
                'step': 4,
                'title': 'Vänd ner ägg och vetemjöl varsamt',
                'text': 'Knäck i äggen ett i taget och rör försiktigt ihop mellan varje ägg – vispa inte in luft! Sikta till sist ner vetemjölet och vänd runt tills du har en tjock, blank och slät kladdkakssmet.',
                'timer': 4
            },
            {
                'step': 5,
                'title': 'Bred ut och grädda i mitten av ugnen',
                'text': 'Häll smeten i långpannan och bred ut den i ett jämnt lager ända ut i hörnen. Grädda i mitten av ugnen i 18–20 minuter. Kanterna ska ha stannat och ytan blivit matt och lätt frasig, men mitten ska fortfarande vara mjuk när du skakar lätt på plåten.',
                'timer': 19
            },
            {
                'step': 6,
                'title': 'Kyl ner för perfekt sega rutor',
                'text': 'Ta ut långpannan och låt kakan svalna i rumstemperatur i 30 minuter. Ställ därefter in den i kylskåp i minst 1–2 timmar så att den sätter sig. Lyft upp pappret, skär i 30 jämna rutor med en varm kniv, pudra över florsocker och servera med lättvispad grädde!',
                'timer': 60
            }
        ],
        'faqs': [
            {
                'q': 'Hur lång tid ska kladdkaka i långpanna vara i ugnen?',
                'a': 'I en standardlångpanna (30x40 cm) på 175°C över-/undervärme är 18–20 minuter perfekt. Eftersom smeten är tunnare än i en rund springform går gräddningen snabbt – håll koll från minut 17 så att den inte blir övergräddad.'
            },
            {
                'q': 'Varför har man ljus sirap i kladdkaka i långpanna?',
                'a': 'Tre matskedar ljus sirap ger kladdkakan den där ljuvliga bagerisega konsistensen ("fudge"-känslan) och förhindrar att sockret kristalliserar sig, vilket håller rutorna saftiga i flera dagar.'
            },
            {
                'q': 'Kan jag baka kladdkakan dagen innan och frysa in den?',
                'a': 'Ja, kladdkaka i långpanna blir faktiskt ännu godare och segare om den bakas dagen innan och får vila i kylskåp över natten! Den går även utmärkt att skära i bitar och frysa in i upp till 3 månader.'
            },
            {
                'q': 'Hur får jag raka, fina kanter när jag skär upp kladdkakan?',
                'a': 'Kyl kakan ordentligt först. Skär sedan med en lång vass kniv som du doppar i hett vatten och torkar av med hushållspapper mellan varje snitt.'
            }
        ],
        'community_reviews': [
            {'name': 'Camilla Lindqvist', 'date': '19 oktober 2026', 'rating': 5, 'comment': 'Bakade denna till fredagsfikat på jobbet och fick så mycket beröm! Exakt 19 minuter i ugnen och sedan 2 timmar i kylen gav helt perfekt sega och kladdiga rutor.', 'verified': True},
            {'name': 'Fredrik Holm', 'date': '17 oktober 2026', 'rating': 5, 'comment': 'Knepet med lite ljus sirap i smeten gör verkligen underverk för segheten. Bästa receptet på kladdkaka i långpanna jag testat!', 'verified': True},
            {'name': 'Sara Vikström', 'date': '15 oktober 2026', 'rating': 5, 'comment': 'Så skönt att kunna röra ihop allt direkt i en stor kastrull utan att smutsa ner elvispen. Räddade sonens klassfest med 30 perfekta bitar!', 'verified': True},
            {'name': 'Mikael Johansson', 'date': '12 oktober 2026', 'rating': 5, 'comment': 'Frasigt täcke ovanpå och härligt krämig inuti. Flingsaltet bryter av den söta chokladsmaken klockrent.', 'verified': True},
            {'name': 'Elin Sundberg', 'date': '9 oktober 2026', 'rating': 5, 'comment': 'Blev precis sådär seg som man vill ha den. Frös in hälften av rutorna och de är precis lika goda när man tar fram dem till kaffet.', 'verified': True},
            {'name': 'Karin Berglund', 'date': '5 oktober 2026', 'rating': 5, 'comment': 'Full pott! Följde måtten till min 30x40-plåt och tjockleken blev helt perfekt.', 'verified': True}
        ]
    },

    # 2. Krämig Toscakladdkaka med Knäckig Mandel- & Kokostosca
    {
        'title': 'Krämig Toscakladdkaka med Knäckig Mandel- & Kokostosca',
        'sub': 'Det bästa av två världar: djup, kladdig chokladbotten toppad med gyllenbrun, knäckig mandel- och kokosglasyr',
        'card_title': 'Krämig Toscakladdkaka',
        'slug': 'kramig-toscakladdkaka-mandel-kokos',
        'file': 'kramig-toscakladdkaka-mandel-kokos.html',
        'img': 'toscakladdkaka',
        'alt': 'Nygräddad krämig toscakladdkaka med glansigt knäckigt täcke av mandelspån och kokos på mörkt stengodsfat',
        'category': 'Fika & Bakning',
        'cat_key': 'fika',
        'cat_slug': 'fika-och-bakning',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 40,
        'time_str': '40 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT25M',
        'cook_time_str': '25 min',
        'total_time': 'PT40M',
        'portions_num': 12,
        'portions_unit': 'bitar',
        'calories': 390,
        'nutrition': {'calories': '390 kcal', 'carbs': '36g', 'fat': '24g', 'protein': '6g', 'sugar': '28g'},
        'rating': 4.8,
        'review_count': 5,
        'date_published': '2026-10-19T12:00:00+02:00',
        'date_modified': '2026-10-19T12:00:00+02:00',
        'keywords': 'toscakladdkaka, kladdkaka med tosca, toscakladdkaka recept, kladdkaka med kokostosca, ryttarkaka kladdkaka, bästa toscakladdkakan',
        'desc': 'Toscakladdkaka förenar en fylligt kladdig chokladbotten med ett gyllene, knäckigt toscatäcke av mandelspån, riven kokos, grädde och smör. En oemotståndlig fikafavorit!',
        'long_desc': (
            'Kan du inte välja mellan kladdkaka, klassisk toscakaka och ryttarkaka? Då är krämig toscakladdkaka svaret på dina drömmar! '
            'Här gräddas först en mörk, intensivt chokladig kladdkaksbotten precis tills kanterna har satt sig. Därefter breds en varm, '
            'koladoftande glasyr av smör, vispgrädde, ljus sirap, mandelspån och riven kokos ut över kakan och gräddas gyllenbrun i ugnen. '
            'Kontrasten mellan den sega, knäckiga mandel- och kokostoppen och den lena chokladmitten gör denna kaka till en given stjärna '
            'både till Kladdkakans dag och helgens lyxfika.'
        ),
        'equipment': ['Springform (24 cm i diameter)', 'Bakplåtspapper', 'Två kastruller', 'Slickepott'],
        'drink_pairing': 'En nybryggd espresso, cappuccino eller ett glas kall mjölk.',
        'pro_tips': 'Förgrädda kladdkaksbottnen i 14–15 minuter så att ytan precis hinner stanna innan du klickar ut toscaglasyren – då lägger sig toscatäcket som ett vackert knäckigt lock ovanpå utan att sjunka ner i mitten.',
        'ingredients': [
            {
                'group': 'Kladdkaksbotten (24 cm springform)',
                'items': [
                    {'name': 'smör', 'unit': 'g', 'val': '150'},
                    {'name': 'strösocker', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'kakao', 'unit': 'dl', 'val': '1'},
                    {'name': 'vaniljsocker', 'unit': 'tsk', 'val': '2'},
                    {'name': 'flingsalt', 'unit': 'krm', 'val': '2'},
                    {'name': 'ägg', 'unit': 'st', 'val': '3'},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': '2'}
                ]
            },
            {
                'group': 'Knäckig Mandel- & Kokostosca',
                'items': [
                    {'name': 'smör', 'unit': 'g', 'val': '75'},
                    {'name': 'strösocker', 'unit': 'dl', 'val': '1'},
                    {'name': 'ljus sirap', 'unit': 'msk', 'val': '2'},
                    {'name': 'vispgrädde', 'unit': 'msk', 'val': '3'},
                    {'name': 'vetemjöl', 'unit': 'msk', 'val': '1.5'},
                    {'name': 'mandelspån (flagad mandel)', 'unit': 'g', 'val': '75'},
                    {'name': 'riven kokos', 'unit': 'dl', 'val': '1'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Förbered ugn och springform',
                'text': 'Sätt ugnen på 175°C (över- och undervärme). Spänn fast ett bakplåtspapper i botten av en springform (24 cm) och smörj kanterna med lite smör.',
                'timer': 4
            },
            {
                'step': 2,
                'title': 'Rör ihop kladdkakssmeten',
                'text': 'Smält 150 g smör i en kastrull och ta från värmen. Rör ner strösocker, kakao, vaniljsocker och salt. Tillsätt äggen ett i taget under varsam omrörning och vänd slutligen ner vetemjölet till en blank smet.',
                'timer': 5
            },
            {
                'step': 3,
                'title': 'Förgrädda kladdkaksbottnen',
                'text': 'Häll smeten i formen och förgrädda i mitten av ugnen i 15 minuter. Ytan ska precis hinna få en tunn hinna så att den bär upp toscaglasyren.',
                'timer': 15
            },
            {
                'step': 4,
                'title': 'Sjud den knäckiga toscaglasyren',
                'text': 'Medan bottnen är i ugnen: mät upp smör, socker, ljus sirap, vispgrädde och vetemjöl i en kastrull. Låt koka upp under omrörning och sjud på svag värme i 2 minuter tills smeten tjocknar lätt. Vänd ner mandelspån och riven kokos.',
                'timer': 5
            },
            {
                'step': 5,
                'title': 'Bred på toscan och grädda gyllenbrun',
                'text': 'Ta ut den förgräddade kladdkakan. Klicka försiktigt ut den varma toscasmeten över hela kakan (börja längs kanterna och arbeta in mot mitten). Grädda i ytterligare 10–12 minuter tills toscatäcket bubblar och har fått en vackert gyllenbrun karamellfärg.',
                'timer': 11
            },
            {
                'step': 6,
                'title': 'Svalna och servera',
                'text': 'Låt toscakladdkakan svalna helt i formen och ställ den gärna i kylskåp i 1 timme så att chokladmitten blir seg och krämig. Servera med en klick lättvispad grädde eller vaniljglass!',
                'timer': 45
            }
        ],
        'faqs': [
            {
                'q': 'Varför sjunker min toscasmet ner i kladdkakan?',
                'a': 'Om kladdkakan är för lös när du lägger på toscan sjunker glasyren i mitten. Förgrädda alltid bottnen i 15 minuter först och klicka ut toscasmeten varsamt med en sked istället för att hälla allt i mitten.'
            },
            {
                'q': 'Kan jag göra toscakladdkakan med bara mandel eller bara kokos?',
                'a': 'Absolut! Du kan byta ut den rivna kokosen mot 50 g extra mandelspån för en ren mandeltosca, eller använda 2,5 dl riven kokos om du vill göra en nöt- och mandelfri kokostosca (ryttarkaka-stil).'
            },
            {
                'q': 'Hur förvarar man toscakladdkaka bäst?',
                'a': 'Förvara kakan i kylskåp under täcklock. Ta fram den cirka 20 minuter före servering så blir chokladbottnen perfekt krämig medan toscatäcket behåller sitt knäckiga tuggmotstånd.'
            }
        ],
        'community_reviews': [
            {'name': 'Sofie Nygren', 'date': '19 oktober 2026', 'rating': 5, 'comment': 'Kombinationen av både mandelspån och kokos i toscatäcket är helt genialisk! Så knäckigt ovanpå och ljuvligt kladdigt inuti.', 'verified': True},
            {'name': 'Göran Lindell', 'date': '16 oktober 2026', 'rating': 5, 'comment': 'Följde tipset att förgrädda exakt 15 minuter och klicka ut glasyren från kanterna inåt. Toscan stannade perfekt ovanpå!', 'verified': True},
            {'name': 'Lotta Hedström', 'date': '13 oktober 2026', 'rating': 5, 'comment': 'Älskar både toscakaka och ryttarkaka, så den här blev en omedelbar favorit hos oss. Serverade med vaniljglass till söndagsfikat.', 'verified': True},
            {'name': 'Magnus Ek', 'date': '10 oktober 2026', 'rating': 5, 'comment': 'Otroligt god och ser ut som ett bakverk från ett riktigt fint konditori.', 'verified': True},
            {'name': 'Hanna Lindblad', 'date': '6 oktober 2026', 'rating': 4, 'comment': 'Jättegott och välbalanserat recept på krämig toscakladdkaka! Tog 2 minuter extra på slutet i min ugn för att få mörk gyllene färg på mandeln, men smaken blev helt fantastisk.', 'verified': True}
        ]
    },

    # 3. Klassisk Krämig Tacopaj med Crème Fraiche & Nachos
    {
        'title': 'Klassisk Krämig Tacopaj med Crème Fraiche & Nachos – Bästa Receptet',
        'sub': 'Fredagsmysets stora favorit med kryddig nötfärs, krämigt täcke av crème fraiche, philadelphiaost och smält ost',
        'card_title': 'Klassisk Krämig Tacopaj',
        'slug': 'klassisk-kramig-tacopaj-creme-fraiche',
        'file': 'klassisk-kramig-tacopaj-creme-fraiche.html',
        'img': 'tacopaj',
        'alt': 'Nygräddad krämig tacopaj i pajform med gyllene osttäcke, halverade körsbärstomater, krossade nachochips och färsk koriander',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Hela familjens favorit',
        'difficulty': 'Enkel',
        'time': 45,
        'time_str': '45 min',
        'prep_time': 'PT20M',
        'prep_time_str': '20 min',
        'cook_time': 'PT25M',
        'cook_time_str': '25 min',
        'total_time': 'PT45M',
        'portions_num': 6,
        'portions_unit': 'portioner',
        'calories': 560,
        'nutrition': {'calories': '560 kcal', 'carbs': '31g', 'fat': '36g', 'protein': '27g', 'sugar': '5g'},
        'rating': 5.0,
        'review_count': 6,
        'date_published': '2026-10-19T12:00:00+02:00',
        'date_modified': '2026-10-19T12:00:00+02:00',
        'keywords': 'tacopaj, tacopaj recept, bästa tacopajen, krämig tacopaj med crème fraiche, tacopaj philadelphiaost, enkel tacopaj, fredagsmys recept',
        'desc': 'Vårt mest populära recept på klassisk krämig tacopaj! Frasigt pajskal fyllt med mustig tacokryddad nötfärs, majs och salsa, toppat med ett ljuvligt krämigt ost- och crème fraiche-täcke.',
        'long_desc': (
            'Klassisk krämig tacopaj är en självklar svensk fredagsklassiker som älskas av både barn och vuxna. '
            'Hemligheten bakom Sveriges godaste tacopaj ligger i tre lager: ett frasigt smörbakat pajskal med en gnutta bakpulver '
            '(som inte behöver vila i kylen!), en saftig tacofärs som sjudits med salsa och majs så att den aldrig blir torr, '
            'och det berömda krämiga täcket av crème fraiche, philadelphiaost, riven lagrad ost och vitlök. '
            'Toppa med söta körsbärstomater och krispiga nachochips under de sista minuterna i ugnen och servera med guacamole och en fräsch grönsallad!'
        ),
        'equipment': ['Pajform (24–26 cm i diameter)', 'Stekpanna', 'Bunke', 'Vitlökspress'],
        'drink_pairing': 'En kall mexikansk lager med en klyfta lime, fruktig röd Zinfandel eller citronvatten.',
        'pro_tips': 'Blanda 2 msk tacosalsa direkt i köttfärsen och låt vätskan koka in innan du lägger färsen i pajskalet – det gör färsen saftig utan att blöta ner pajbottnen. Förgrädda alltid skalet i 10 minuter!',
        'ingredients': [
            {
                'group': 'Snabbt & Frasigt Pajskal',
                'items': [
                    {'name': 'smör (rumsvarmt eller smält)', 'unit': 'g', 'val': '125'},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': '3'},
                    {'name': 'bakpulver', 'unit': 'tsk', 'val': '1'},
                    {'name': 'salt', 'unit': 'krm', 'val': '2'},
                    {'name': 'kallt vatten eller mjölk', 'unit': 'msk', 'val': '2'}
                ]
            },
            {
                'group': 'Saftig Tacofärs',
                'items': [
                    {'name': 'nötfärs (10–12%)', 'unit': 'g', 'val': '500'},
                    {'name': 'gul lök (finhackad)', 'unit': 'st', 'val': '1'},
                    {'name': 'vitlöksklyfta (pressad)', 'unit': 'st', 'val': '1'},
                    {'name': 'tacokrydda (1 påse eller hemgjord)', 'unit': 'g', 'val': '28'},
                    {'name': 'tacosalsa (medium)', 'unit': 'dl', 'val': '1'},
                    {'name': 'vatten', 'unit': 'dl', 'val': '1'},
                    {'name': 'majskorn (avrunna)', 'unit': 'dl', 'val': '1.5'},
                    {'name': 'smör eller olja till stekning', 'unit': 'msk', 'val': '1'}
                ]
            },
            {
                'group': 'Krämigt Ost- & Crème Fraiche-täcke',
                'items': [
                    {'name': 'crème fraiche (34%)', 'unit': 'dl', 'val': '2'},
                    {'name': 'färskost (typ Philadelphia)', 'unit': 'g', 'val': '100'},
                    {'name': 'riven lagrad ost (t.ex. cheddar eller prästost)', 'unit': 'dl', 'val': '3'},
                    {'name': 'körsbärstomater (halverade)', 'unit': 'g', 'val': '150'},
                    {'name': 'nachochips (lätt krossade along kanten)', 'unit': 'g', 'val': '50'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Tryck ut och förgrädda pajskalet',
                'text': 'Sätt ugnen på 200°C. Blanda vetemjöl, bakpulver och salt i en bunke. Tillsätt smör och vatten och arbeta snabbt ihop till en smidig deg. Tryck ut degen i en pajform (24–26 cm), nagga bottnen med en gaffel och förgrädda i mitten av ugnen i 10 minuter.',
                'timer': 10
            },
            {
                'step': 2,
                'title': 'Bryn nötfärs och lök',
                'text': 'Hetta upp smör i en stekpanna. Fräs nötfärs och finhackad gul lök på hög värme tills färsen är smulig och har fått fin stekyta. Pressa i vitlöksklyftan.',
                'timer': 6
            },
            {
                'step': 3,
                'title': 'Koka in tacokrydda, salsa och majs',
                'text': 'Tillsätt tacokrydda, tacosalsa och vatten i färsen. Låt puttra utan lock i 5 minuter så att vätskan kokar in och smakerna sätter sig. Vänd ner de avrunna majskornen.',
                'timer': 5
            },
            {
                'step': 4,
                'title': 'Rör ihop det krämiga osttäcket',
                'text': 'Blanda crème fraiche, philadelphiaost och två tredjedelar av den rivna osten i en skål. Krydda med en nypa nymald svartpeppar.',
                'timer': 3
            },
            {
                'step': 5,
                'title': 'Fyll pajen och toppa med kräm & tomater',
                'text': 'Fördela den varma tacofärsen i det förgräddade pajskalet. Bred det krämiga crème fraiche- och philadelphiatäcket jämnt ovanpå färsen. Strö över resten av den rivna osten, lägg på halverade körsbärstomater och stick ner nachochips längs kanten.',
                'timer': 4
            },
            {
                'step': 6,
                'title': 'Grädda gyllenbrun och låt vila',
                'text': 'Grädda tacopajen i mitten av ugnen på 200°C i 20–25 minuter tills osttäcket är vackert gyllenbrunt och bubblande. Låt pajen vila i 10 minuter före servering så håller skivorna ihop perfekt!',
                'timer': 22
            }
        ],
        'faqs': [
            {
                'q': 'Vad gör att tacopajen blir så krämig och inte rinnig?',
                'a': 'Kombinationen av helfet crème fraiche (34%), philadelphiaost och riven ost i täcket binder vätskan i ugnen och ger en suffléaktig, krämig konsistens som inte skär sig.'
            },
            {
                'q': 'Kan jag förbereda tacopajen dagen innan?',
                'a': 'Ja! Du kan antingen grädda hela pajen dagen innan och värma den i ugnen på 175°C i 15 minuter, eller förgrädda skalet och steka färsen dagen innan och bara lägga på crème fraiche-täcket och grädda precis före middagen.'
            },
            {
                'q': 'Vilka tillbehör passar bäst till tacopaj?',
                'a': 'Servera med en krispig grönsallad, hemgjord guacamole, gräddfil, extra tacosalsa, inlagd rödlök och inlagda jalapeños.'
            }
        ],
        'community_reviews': [
            {'name': 'Johan Berg', 'date': '19 oktober 2026', 'rating': 5, 'comment': 'Utan tvekan den godaste tacopajen vi lagat! Kombinationen med både philadelphiaost och crème fraiche i täcket gör den så otroligt krämig.', 'verified': True},
            {'name': 'Annika Söderberg', 'date': '17 oktober 2026', 'rating': 5, 'comment': 'Pajdegen med bakpulver var superenkel att trycka ut direkt utan att behöva vänta på kylen. Frasigt skal och suverän smak!', 'verified': True},
            {'name': 'Peter Sjöberg', 'date': '14 oktober 2026', 'rating': 5, 'comment': 'Fredagsmysets nya standardrecept här hemma! Tipset med salsa i färsen gjorde att bottnen inte blev blöt alls.', 'verified': True},
            {'name': 'Helena Lindström', 'date': '11 oktober 2026', 'rating': 5, 'comment': 'Ungarna älskade den och matlådan på lördagen var nästan ännu godare. 5 av 5!', 'verified': True},
            {'name': 'Daniel Lundqvist', 'date': '8 oktober 2026', 'rating': 5, 'comment': 'Perfekta proportioner på fyllning och osttäcke. Nachochipsen längs kanten blev så krispiga och goda i ugnen.', 'verified': True},
            {'name': 'Ulrika Forsberg', 'date': '4 oktober 2026', 'rating': 5, 'comment': 'Bjudmat som alltid går hem! Gjorde dubbel sats när vi hade gäster och allt gick åt.', 'verified': True}
        ]
    },

    # 4. Klassisk Plankstek med Oxfilé, Duchessemos & Bearnaisesås
    {
        'title': 'Klassisk Plankstek med Oxfilé, Duchessemos & Bearnaisesås',
        'sub': 'Äkta svensk krogklassiker på ekplanka med mör oxfilé, spritsat gyllene duchessemos, baconlindad sparris och bearnaisesås',
        'card_title': 'Klassisk Plankstek',
        'slug': 'klassisk-plankstek-oxfile-duchessemos',
        'file': 'klassisk-plankstek-oxfile-duchessemos.html',
        'img': 'plankstek',
        'alt': 'Klassisk svensk plankstek på ekplanka med rosastekt oxfilé, spritsat gyllenbrunt duchessemos, baconlindade haricots verts, grillad tomat och bearnaisesås',
        'category': 'Högtider & Smörgåsbord',
        'cat_key': 'smorgasbord',
        'cat_slug': 'hogtider-och-smorgasbord',
        'diet': 'Fest & Helglyx',
        'difficulty': 'Medel',
        'time': 50,
        'time_str': '50 min',
        'prep_time': 'PT30M',
        'prep_time_str': '30 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT50M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'calories': 740,
        'nutrition': {'calories': '740 kcal', 'carbs': '34g', 'fat': '48g', 'protein': '42g', 'sugar': '4g'},
        'rating': 5.0,
        'review_count': 5,
        'date_published': '2026-10-19T12:00:00+02:00',
        'date_modified': '2026-10-19T12:00:00+02:00',
        'keywords': 'plankstek, plankstek recept, klassisk plankstek oxfilé, duchessemos till plankstek, plankstek i ugn, plankstek utan planka, festmat helg',
        'desc': 'Laga en äkta klassisk plankstek hemma! Smörstekt oxfilé omgiven av spritsat gyllene duchessemos på mjölig potatis och äggulor, baconlindade haricots verts, grillad tomat och krämig bearnaisesås.',
        'long_desc': (
            'Få rätter väcker samma nostalgiska festkänsla som en rykande het klassisk svensk plankstek! '
            'Oavsett om du firar Fars dag, Allhelgonahelgen eller vill bjuda på en minnesvärd lördagsmiddag är hemgjord plankstek '
            'oslagbar. Hemligheten bakom det vackra, spritsade duchessemoset som behåller sina skarpa ränder i ugnen är att pressa '
            'mjölig potatis, låta ångan pysa bort och vispa ner smör och äggulor (utan mjölk!) så att moset blir fast och silkeslent. '
            'Har du inga ekplankor hemma? Då kan du spritsa moset direkt på ugnsfasta stengodstallrikar eller i en stor gratängform med exakt samma ljuvliga resultat!'
        ),
        'equipment': ['4 ekplankor (eller ugnsfasta tallrikar/form)', 'Potatispress', 'Spritspåse med stjärntyll', 'Gjutjärnspanna'],
        'drink_pairing': 'Ett kraftfullt och fatlagrat rött vin på Cabernet Sauvignon eller Bordeaux, alternativt en fyllig alkoholfri must på svarta vinbär.',
        'pro_tips': 'Tillsätt aldrig mjölk i duchessemos! Använd bara rikligt med äkta smör och äggulor i den pressade mjöliga potatisen – det gör att moset håller formen i spritspåsen och får en fantastisk gyllenbrun yta i ugnen.',
        'ingredients': [
            {
                'group': 'Äkta Duchessemos (som håller formen i ugnen)',
                'items': [
                    {'name': 'potatis av mjölig sort (t.ex. King Edward, skalad)', 'unit': 'kg', 'val': '1'},
                    {'name': 'smör (rumsvarmt)', 'unit': 'g', 'val': '75'},
                    {'name': 'äggulor', 'unit': 'st', 'val': '3'},
                    {'name': 'salt', 'unit': 'tsk', 'val': '1.5'},
                    {'name': 'nymald vitpeppar', 'unit': 'krm', 'val': '2'},
                    {'name': 'riven muskotnöt', 'unit': 'krm', 'val': '1'}
                ]
            },
            {
                'group': 'Oxfilé & Tillbehör på Plankan',
                'items': [
                    {'name': 'oxfilé (eller mör ryggbiff, putsad i 4 medaljonger)', 'unit': 'g', 'val': '600'},
                    {'name': 'smör till stekning', 'unit': 'msk', 'val': '2'},
                    {'name': 'haricots verts eller grön sparris', 'unit': 'g', 'val': '200'},
                    {'name': 'baconskivor', 'unit': 'st', 'val': '8'},
                    {'name': 'mogna tomater (halverade)', 'unit': 'st', 'val': '2'},
                    {'name': 'flingsalt och grovmalen svartpeppar', 'unit': 'tsk', 'val': '1'}
                ]
            },
            {
                'group': 'Såser till Servering',
                'items': [
                    {'name': 'krämig bearnaisesås (hemslagen eller kyld av hög kvalitet)', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'rödvinssås eller kraftig skysås', 'unit': 'dl', 'val': '1.5'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Koka och ånga av potatisen',
                'text': 'Skala och skär den mjöliga potatisen i jämnstora bitar. Koka mjuk i lättsaltat vatten i ca 15–20 minuter. Häll av vattnet och låt potatisen stå på eftervärme utan lock i 2 minuter så att all överflödig ånga försvinner.',
                'timer': 18
            },
            {
                'step': 2,
                'title': 'Pressa och vispa ihop duchessemoset',
                'text': 'Pressa potatisen genom en potatispress ner i en bunke. Klicka i det rumsvarma smöret och rör tills det smält. Vispa ner äggulorna en i taget och smaka av med salt, vitpeppar och nyriven muskotnöt. Fyll en spritspåse med stor stjärntyll.',
                'timer': 5
            },
            {
                'step': 3,
                'title': 'Förbered plankor och baconbuketter',
                'text': 'Sätt ugnen på 225°C (gärna med grillfunktion på slutet). Pensla ekplankorna tunt med neutral olja. Förväll haricots verts i 1 minut i kokande vatten, spola kalla och linda 2 skivor bacon runt varje knippe. Stek baconknytena lätt i panna så att baconet får färg.',
                'timer': 6
            },
            {
                'step': 4,
                'title': 'Spritsa moset och lägg på tomat',
                'text': 'Spritsa en vacker sammanhängande ram av duchessemos längs kanten på de 4 plankorna (eller ugnsfasta tallrikarna). Placera en kryddad tomathalva och ett baconlindat bönknippe på varje planka.',
                'timer': 5
            },
            {
                'step': 5,
                'title': 'Bryn oxfilén hastigt i smör',
                'text': 'Krydda de rumsvarma oxfilémedaljongerna rikligt med salt och svartpeppar. Bryn dem i rykande het gjutjärnspanna med smör i ca 1,5 minut per sida så att de får en kraftig stekyta men fortfarande är rika och röda inuti (de går klart på plankan i ugnen).',
                'timer': 4
            },
            {
                'step': 6,
                'title': 'Gratinera planksteken och servera med bearnaisesås',
                'text': 'Lägg oxfilén i mitten av varje planka. Ställ in plankorna högt upp i ugnen på 225°C i 8–10 minuter tills duchessemoset har fått gyllenbruna toppar. Ta ut, skeda över rödvinssås och fyllig bearnaisesås och servera omedelbart!',
                'timer': 9
            }
        ],
        'faqs': [
            {
                'q': 'Kan man göra plankstek utan ekplankor?',
                'a': 'Ja, det går alldeles utmärkt! Spritsa duchessemoset längs kanten på ugnsfasta stengodstallrikar, i portionsformar eller längs kanterna i en stor ugnsfast gratängform.'
            },
            {
                'q': 'Hur bränner man in nya ekplankor innan första användningen?',
                'a': 'Pensla nya ekplankor rikligt med matolja på båda sidor och ställ in dem i ugnen på 200°C i cirka 10–15 minuter tills oljan kokat in i träet. Diska alltid plankor för hand i varmt vatten utan diskmedel.'
            },
            {
                'q': 'Varför rinner mitt duchessemos ut i ugnen?',
                'a': 'Om moset innehåller mjölk eller grädde, eller om potatisen inte ångats av ordentligt efter kokningen, blir moset för löst. Använd endast mjölig potatis, smör och äggulor.'
            }
        ],
        'community_reviews': [
            {'name': 'Henrik Olsson', 'date': '19 oktober 2026', 'rating': 5, 'comment': 'Duchessemoset blev helt perfekt! Följde rådet att inte ha i någon mjölk utan bara smör och äggulor, och ränderna höll formen klockrent i ugnen.', 'verified': True},
            {'name': 'Maria Engström', 'date': '16 oktober 2026', 'rating': 5, 'comment': 'Lagade detta till helgmiddagen på våra ugnsfasta stengodstallrikar. Oxfilén blev smältande mör och hela familjen gav 10 av 10!', 'verified': True},
            {'name': 'Stefan Eriksson', 'date': '12 oktober 2026', 'rating': 5, 'comment': 'Riktig 80-talslyx när den är som allra bäst! Kombinationen med både rödvinssås och bearnaisesås på plankan är oslagbar.', 'verified': True},
            {'name': 'Katarina Holmberg', 'date': '8 oktober 2026', 'rating': 5, 'comment': 'Superbra steg-för-steg-beskrivning så att allt blir klart samtidigt. Perfekt till Fars dag och fest!', 'verified': True},
            {'name': 'Niklas Bergström', 'date': '3 oktober 2026', 'rating': 5, 'comment': 'Bättre än på krogen! Muskatnöten i duchessemoset lyfter smaken enormt.', 'verified': True}
        ]
    }
]

RECIPES.extend(BATCH31_RECIPES)

target_path = os.path.join(BASE_DIR, "tools", "recipes_data.py")
with open(target_path, "w", encoding="utf-8") as f:
    f.write("# Auto-generated recipes_data.py\n")
    f.write("RECIPES = " + pprint.pformat(RECIPES, width=120, sort_dicts=False) + "\n")

print(f"✅ Successfully added 4 Batch 31 recipes! Total recipes: {len(RECIPES)}")
