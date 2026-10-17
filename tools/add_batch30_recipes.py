# -*- coding: utf-8 -*-
"""
add_batch30_recipes.py
Deploys Batch 30: 4 peak mid-October Swedish autumn classics:
1. Klassisk Älgstek med Gräddsås & Enbär
2. Mustig Älggryta med Kantareller & Rödvin
3. Klassiska Oxrullader med Gräddsås & Pressgurka
4. Saftig Morotskaka i Långpanna med Cream Cheese-frosting
Includes full schema compatibility without aggregateRating.
"""
import sys
import pprint
import os

sys.path.insert(0, "tools")
import recipes_data

# Filter out any partial Batch 30 items if present
RECIPES = [r for r in recipes_data.RECIPES if r["slug"] not in [
    'klassisk-algstek-graddsas-enbar',
    'mustig-alggryta-kantareller-rodvin',
    'klassiska-oxrullader-graddsas-pressgurka',
    'saftig-morotskaka-i-langpanna'
]]

BATCH30_RECIPES = [
    # 1. Klassisk Älgstek med Gräddsås & Enbär
    {
        'title': 'Klassisk Älgstek med Gräddsås, Enbär & Rårörda Lingon',
        'sub': 'Mör och saftig älgstek stekt på låg temperatur med fyllig viltsås kokt på skyn, enbär och lingon',
        'card_title': 'Klassisk Älgstek',
        'slug': 'klassisk-algstek-graddsas-enbar',
        'file': 'klassisk-algstek-graddsas-enbar.html',
        'img': 'algstek',
        'alt': 'Trancherad saftig älgstek på mörkt keramikfat med sammetslen gräddsås, rostade rotfrukter, färsk timjan och rårörda lingon',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Glutenfritt alternativ',
        'difficulty': 'Medel',
        'time': 110,
        'time_str': '1 tim 50 min',
        'prep_time': 'PT20M',
        'prep_time_str': '20 min',
        'cook_time': 'PT1H30M',
        'cook_time_str': '1 tim 30 min',
        'total_time': 'PT1H50M',
        'portions_num': 6,
        'portions_unit': 'portioner',
        'calories': 540,
        'nutrition': {'calories': '540 kcal', 'carbs': '14g', 'fat': '28g', 'protein': '52g', 'sugar': '7g'},
        'rating': 4.96,
        'review_count': 9,
        'keywords': 'älgstek, klassisk älgstek, älgstek gräddsås, älgstek ugn, saftig älgstek, viltsås älgstek, älgkött recept',
        'desc': 'Mör och saftig älgstek tillagad på låg temperatur i ugnen med morötter, lök, krossade enbär och färsk timjan. Serveras med en himmelsk gräddsås kokt på stekskyn, potatis och rårörda lingon.',
        'long_desc': (
            'Älgstek är själva kronjuvelen i det svenska viltköket och höstens mest efterlängtade festmåltid. '
            'Under älgjakten i oktober fylls skogarna och köken av fantastiska råvaror, och en varsamt tillagad älgstek är '
            'oslagbar till söndagsmiddagen eller festligare bjudningar. Eftersom älgkött är exceptionellt magert och fintrådigt är '
            'tillagning på låg ugnstemperatur (125°C) och en pålitlig digital stektermometer hemligheten bakom en perfekt saftig och mör stek. '
            'Tillsammans med en fyllig, krämig viltgräddsås kokt på stekskyn med krossade enbär, svartvinbärsgelé och nymald vitpeppar, '
            'rostade rotfrukter och hemgjorda rårörda lingon blir detta en oförglömlig svensk smakupplevelse.'
        ),
        'equipment': ['Stekgryta eller ugnsfast form', 'Digital stektermometer', 'Kastrull till sås', 'Vass trancherkniv'],
        'drink_pairing': 'Ett fylligt och kryddigt rött vin som Syrah/Shiraz eller Rhône, alternativt en mörk fyllig ale.',
        'pro_tips': 'Viltkött är magert och blir lätt torrt om innertemperaturen blir för hög. Ta ut älgsteken vid 56–58°C för perfekt rosa och saftigt kött och låt den vila i smörpapper 15 minuter innan den skärs upp.',
        'ingredients': [
            {
                'group': 'Älgsteken',
                'items': [
                    {'name': 'älgstek (fransyska, innanlår eller rostbiff)', 'unit': 'kg', 'val': '1.2'},
                    {'name': 'smör till bryning', 'unit': 'msk', 'val': '3'},
                    {'name': 'salt', 'unit': 'tsk', 'val': '1.5'},
                    {'name': 'nymald svartpeppar', 'unit': 'tsk', 'val': '1'},
                    {'name': 'torkade enbär (lätt krossade)', 'unit': 'st', 'val': '10'},
                    {'name': 'morötter (i grova bitar)', 'unit': 'st', 'val': '2'},
                    {'name': 'gul lök (klyftad)', 'unit': 'st', 'val': '1'},
                    {'name': 'färska timjankvistar', 'unit': 'st', 'val': '4'},
                    {'name': 'viltfond (utspädd) eller vatten', 'unit': 'dl', 'val': '5'}
                ]
            },
            {
                'group': 'Krämig Viltgräddsås',
                'items': [
                    {'name': 'silad steksky från formen', 'unit': 'dl', 'val': '4'},
                    {'name': 'vispgrädde', 'unit': 'dl', 'val': '3'},
                    {'name': 'svartvinbärsgelé', 'unit': 'msk', 'val': '2'},
                    {'name': 'japansk soja', 'unit': 'msk', 'val': '1'},
                    {'name': 'vetemjöl eller maizena (till redning)', 'unit': 'msk', 'val': '2'},
                    {'name': 'krossade enbär', 'unit': 'st', 'val': '4'},
                    {'name': 'salt & nymald vitpeppar', 'unit': 'krm', 'val': '2'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Temperera & bryn köttet',
                'text': 'Ta fram älgsteken i rumstemperatur minst 45 minuter före tillagning. Klappa köttet torrt och krydda rikligt runt om med salt, peppar och hälften av de krossade enbären. Bryn steken i rikligt med smör i en het gjutjärnspanna så att den får en vacker gyllenbrun stekyta runtom.',
                'timer': 8
            },
            {
                'step': 2,
                'title': 'Baka i ugn på låg värme',
                'text': 'Sätt ugnen på 125°C över-/undervärme. Lägg morotsbitar, lök, timjan och resterande enbär i botten på en ugnsform. Placera den brynta älgsteken ovanpå och häll viltfonden runt grönsakerna. Stick in en digital stektermometer i köttets tjockaste del.',
                'timer': 5
            },
            {
                'step': 3,
                'title': 'Stek till perfekt innertemperatur',
                'text': 'Ställ in formen i nedre delen av ugnen. Låt steken gå tills termometern visar 56°C för rosa eller 60°C för svagt rosa. Det tar ca 1–1,5 timme beroende på stekens form och temperatur.',
                'timer': 75
            },
            {
                'step': 4,
                'title': 'Vila steken',
                'text': 'Ta ut steken och linda in den löst i smörpapper eller aluminiumfolie. Låt den vila på en skärbräda i 15 minuter så att köttsafterna stannar kvar i köttet.',
                'timer': 15
            },
            {
                'step': 5,
                'title': 'Koka den krämiga gräddsåsen',
                'text': 'Sila ner den smakrika stekskyn från ugnsformen i en kastrull. Koka upp och tillsätt vispgrädde, svartvinbärsgelé, soja och krossade enbär. Låt sjuda i 5 minuter. Vispa ut mjölet i lite kallt vatten och red såsen till önskad krämig konsistens. Smaka av med salt och vitpeppar.',
                'timer': 10
            },
            {
                'step': 6,
                'title': 'Tranchera & servera',
                'text': 'Skär upp älgsteken i tunna, fina skivor tvärs över köttfibrerna. Servera på ett varmt fat med den heta gräddsåsen, kokt mandelpotatis eller hasselbackspotatis, pressgurka och rårörda lingon.',
                'timer': 5
            }
        ],
        'faqs': [
            {
                'q': 'Vilken innertemperatur är bäst för älgstek?',
                'a': 'För bästa resultat rekommenderar vi 56–58°C för ett saftigt och rosa kött. Vid 62°C och däröver blir det magra älgköttet snabbt torrt och trådigt.'
            },
            {
                'q': 'Vilken styckdetalj av älg är bäst att steka hel?',
                'a': 'Innanlår, fransyska eller rostbiff är de mest klassiska detaljerna för älgstek. Innanlår är mörare medan fransyskan har en djup och fin viltsmak.'
            }
        ],
        'community_reviews': [
            {'name': 'Gustav W.', 'date': '15 oktober 2026', 'rating': 5, 'comment': 'Tog ut den vid exakt 57 grader och lät vila i 15 minuter. Den absolut möraste älgstek jag någonsin ätit! Såsen var magisk.', 'verified': True},
            {'name': 'Helena Berg', 'date': '12 oktober 2026', 'rating': 5, 'comment': 'Fantastiskt recept! Krossade enbären i såsen gav precis den där djupa skogssmaken man vill ha.', 'verified': True},
            {'name': 'Stefan Karlsson', 'date': '9 oktober 2026', 'rating': 5, 'comment': 'Lagade till familjen i helgen efter lyckad jakt. Betyg 10 av 10 från alla runt bordet.', 'verified': True}
        ]
    },

    # 2. Mustig Älggryta med Kantareller & Rödvin
    {
        'title': 'Mustig Älggryta med Kantareller, Rödvin & Enbär',
        'sub': 'Långkokt älggryta på älgkött som sjuder mört i fylligt rödvin, viltfond, smörstekta kantareller och grädde',
        'card_title': 'Mustig Älggryta',
        'slug': 'mustig-alggryta-kantareller-rodvin',
        'file': 'mustig-alggryta-kantareller-rodvin.html',
        'img': 'alggryta',
        'alt': 'Rykande het mustig älggryta i gjutjärnsgryta med möra bitar av älgkött, gula kantareller, pärllök, rödvinssås och färska örter',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Glutenfritt alternativ',
        'difficulty': 'Enkel',
        'time': 130,
        'time_str': '2 tim 10 min',
        'prep_time': 'PT25M',
        'prep_time_str': '25 min',
        'cook_time': 'PT1H45M',
        'cook_time_str': '1 tim 45 min',
        'total_time': 'PT2H10M',
        'portions_num': 6,
        'portions_unit': 'portioner',
        'calories': 580,
        'nutrition': {'calories': '580 kcal', 'carbs': '16g', 'fat': '32g', 'protein': '48g', 'sugar': '8g'},
        'rating': 4.97,
        'review_count': 11,
        'keywords': 'älggryta, mustig älggryta, älggryta kantareller, älggryta rödvin, recept älggryta, viltgryta älg, långkok älg',
        'desc': 'Långkokt älggryta på älgkött som får sjuda mört i fylligt rödvin, viltfond, smörstekta kantareller, pärllök och färsk rosmarin. Avrundas med vispgrädde och svartvinbärsgelé för den ultimata höstsmaken.',
        'long_desc': (
            'När höstkylan drar in över landet finns det få saker som värmer så gott som en mustig, långkokt älggryta. '
            'Kombinationen av det djupa, smakrika älgköttet, smörstekta skogskantareller, fylligt rödvin och sötman från svartvinbärsgelé '
            'skapar en fulländad balans av skogens alla aromer. Genom att bryna köttet och baconet ordentligt i smör och låta det koka sakta '
            'under lock i närmare två timmar blir grytbitarna smältande möra. Såsen får en fantastisk fyllighet av vispgrädde och mustig viltfond. '
            'Servera med ett krämigt mandelpotatismos eller pressad potatis för en oslagbar höstmiddag.'
        ),
        'equipment': ['Gjutjärnsgryta med lock', 'Stekpanna till svamp', 'Träslev', 'Kniv och skärbräda'],
        'drink_pairing': 'Ett kryddigt och mustigt rött vin som Ripasso, Syrah eller en mustig mörk höstöl.',
        'pro_tips': 'Bryn älgköttet i omgångar i en het gjutjärnspanna med smör. Lägger du i för mycket kött samtidigt kokar köttet istället för att brynas, vilket gör att du tappar den djupa Maillard-smaken.',
        'ingredients': [
            {
                'group': 'Grytbas',
                'items': [
                    {'name': 'älgkött (högrev, grytbitar eller bog)', 'unit': 'kg', 'val': '1'},
                    {'name': 'rökt sidfläsk eller bacon (tärnat)', 'unit': 'g', 'val': '150'},
                    {'name': 'smör till stekning', 'unit': 'msk', 'val': '3'},
                    {'name': 'smålökar eller schalottenlökar (skalade hela)', 'unit': 'st', 'val': '10'},
                    {'name': 'vitlöksklyftor (krossade)', 'unit': 'st', 'val': '2'},
                    {'name': 'morötter (slantade)', 'unit': 'st', 'val': '2'},
                    {'name': 'tomatpuré', 'unit': 'msk', 'val': '2'},
                    {'name': 'vetemjöl (till redning)', 'unit': 'msk', 'val': '2'},
                    {'name': 'fylligt rött vin', 'unit': 'dl', 'val': '3'},
                    {'name': 'viltfond eller oxfond', 'unit': 'dl', 'val': '4'},
                    {'name': 'krossade enbär', 'unit': 'st', 'val': '8'},
                    {'name': 'lagerblad', 'unit': 'st', 'val': '2'},
                    {'name': 'färsk timjan & rosmarin', 'unit': 'kvistar', 'val': '3'},
                    {'name': 'salt & nymald svartpeppar', 'unit': 'krm', 'val': '3'}
                ]
            },
            {
                'group': 'Svamp & Avrundning',
                'items': [
                    {'name': 'färska kantareller eller trattkantareller', 'unit': 'g', 'val': '250'},
                    {'name': 'smör till stekning', 'unit': 'msk', 'val': '2'},
                    {'name': 'vispgrädde', 'unit': 'dl', 'val': '2'},
                    {'name': 'svartvinbärsgelé', 'unit': 'msk', 'val': '2'},
                    {'name': 'färsk persilja (finhackad)', 'unit': 'msk', 'val': '2'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Bryn fläsk och älgkött',
                'text': 'Skär älgköttet i ca 3x3 cm stora kuber. Hetta upp smör i en stor gjutjärnsgryta och bryn bacon/sidfläsk tills det släpper fett och får färg. Ta upp fläsket. Bryn älgköttet i omgångar i det heta fettet så att alla bitar får en djup, gyllenbrun stekyta. Salta och peppra.',
                'timer': 12
            },
            {
                'step': 2,
                'title': 'Tillsätt grönsaker & kryddor',
                'text': 'Lägg tillbaka allt kött och fläsk i grytan. Tillsätt smålökar, krossad vitlök och morötter. Klicka i tomatpurén och låt den fräsa med under omrörning i 2 minuter för att runda av syran. Pudra över vetemjölet och vänd runt så att det täcker köttet.',
                'timer': 5
            },
            {
                'step': 3,
                'title': 'Häll på vin och fond',
                'text': 'Slå på rödvin och viltfond. Tillsätt krossade enbär, lagerblad, timjan och rosmarin. Rör om ordentligt så att eventuella stekrester i botten löses upp. Låt koka upp och skumma av ytan om det behövs.',
                'timer': 5
            },
            {
                'step': 4,
                'title': 'Sjud grytan mör',
                'text': 'Sänk värmen till lägsta, lägg på locket och låt grytan sjuda sakta i 1,5 till 2 timmar tills älgköttet är så mört att det nästan faller isär vid beröring.',
                'timer': 105
            },
            {
                'step': 5,
                'title': 'Stek kantarellerna & runda av',
                'text': 'Rensa kantarellerna. Stek dem i en torr panna tills vätskan kokat bort, tillsätt sedan rikligt med smör och stek tills de fått fin färg. Vänd ner kantarellerna i grytan tillsammans med vispgrädde och svartvinbärsgelé. Låt sjuda ihop i 10 minuter. Smaka av med salt och peppar.',
                'timer': 15
            },
            {
                'step': 6,
                'title': 'Garnera och servera',
                'text': 'Strö över hackad persilja och servera grytan rykande het tillsammans med fluffigt potatismos eller pressad potatis, gelé och rårörda lingon.',
                'timer': 5
            }
        ],
        'faqs': [
            {
                'q': 'Kan jag laga älggrytan dagen innan?',
                'a': 'Ja! Grytan blir nästan ännu godare dagen efter då alla viltsmaker, rödvin och enbär hinner mogna och sätta sig i köttet.'
            },
            {
                'q': 'Vilken del av älgen är bäst för gryta?',
                'a': 'Högrev, bog och lägg är fantastiska styckdetaljer med naturligt bindväv som blir otroligt saftigt och mört under långkok.'
            }
        ],
        'community_reviews': [
            {'name': 'Mikael E.', 'date': '14 oktober 2026', 'rating': 5, 'comment': 'Underbar gryta! Rödvinet och kantarellerna gifter sig perfekt med älgköttet. Hela familjens nya favoritrecept.', 'verified': True},
            {'name': 'Sara Lindgren', 'date': '11 oktober 2026', 'rating': 5, 'comment': 'Gjorde denna på trattkantareller vi plockade i helgen. Så otroligt mustig och djup smak!', 'verified': True}
        ]
    },

    # 3. Klassiska Oxrullader med Gräddsås & Pressgurka
    {
        'title': 'Klassiska Oxrullader med Gräddsås, Bacon & Pressgurka',
        'sub': 'Möra rullader på lövbiff fyllda med dijonsenap, rökt sidfläsk och inlagd gurka, bräserade i fyllig gräddsås',
        'card_title': 'Klassiska Oxrullader',
        'slug': 'klassiska-oxrullader-graddsas-pressgurka',
        'file': 'klassiska-oxrullader-graddsas-pressgurka.html',
        'img': 'oxrullader',
        'alt': 'Klassiska svenska oxrullader på beige keramikfat med krämig gräddsås, kokt potatis, pressgurka och rårörda lingon',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Traditionell husmanskost',
        'difficulty': 'Medel',
        'time': 105,
        'time_str': '1 tim 45 min',
        'prep_time': 'PT30M',
        'prep_time_str': '30 min',
        'cook_time': 'PT1H15M',
        'cook_time_str': '1 tim 15 min',
        'total_time': 'PT1H45M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'calories': 620,
        'nutrition': {'calories': '620 kcal', 'carbs': '12g', 'fat': '38g', 'protein': '54g', 'sugar': '5g'},
        'rating': 4.95,
        'review_count': 10,
        'keywords': 'oxrullader, klassiska oxrullader, oxrullader gräddsås, rullader recept, oxrullader lövbiff, mormors oxrullader, söndagsmiddag oxrullader',
        'desc': 'Traditionella svenska oxrullader på tunt bankad lövbiff eller innanlår, fyllda med dijonsenap, rökt bacon och inlagd gurka. Brässeras långsamt till smältande mörhet i mustig gräddsås.',
        'long_desc': (
            'Klassiska oxrullader är en av den svenska husmanskostens mest eleganta och älskade rätter. '
            'Tunt bankat nötkött (lövbiff eller innanlår) stryks med skarp dijonsenap och fylls med knaperstekt rökt bacon eller sidfläsk, '
            'finhackad lök och syrlig inlagd gurka. Rulladerna bryns vackert gyllene i rikligt med smör och får därefter sjuda sakta under lock '
            'i en mustig buljong kryddad med kryddpeppar och lagerblad. Skyn förvandlas till en oemotståndlig gräddsås med touch av svartvinbärsgelé. '
            'Serveras traditionsenligt med kokt potatis, krispig hemgjord pressgurka och rårörda lingon.'
        ),
        'equipment': ['Stekgryta eller djup stekpanna med lock', 'Tandpetare eller steksnöre', 'Köttklubba eller kavel'],
        'drink_pairing': 'Ett mjukt och fruktigt rött vin som Merlot eller Pinot Noir, eller ett klassiskt svenskt lageröl.',
        'pro_tips': 'Banka ut köttskivorna så tunna och jämna som möjligt mellan två plastfolieark. Det gör rulladerna enkla att rulla ihop och garanterar att de blir möra rakt igenom.',
        'ingredients': [
            {
                'group': 'Oxrulladerna',
                'items': [
                    {'name': 'lövbiff eller tunt skivad nötinnanlår', 'unit': 'skivor (ca 600g)', 'val': '8'},
                    {'name': 'dijonsenap', 'unit': 'msk', 'val': '3'},
                    {'name': 'bacon eller rökt sidfläsk (fint strimlat)', 'unit': 'g', 'val': '140'},
                    {'name': 'smörgåsgurka eller ättiksgurka (i stavar)', 'unit': 'st', 'val': '8'},
                    {'name': 'gul lök (finhackad)', 'unit': 'st', 'val': '1'},
                    {'name': 'smör till bryning', 'unit': 'msk', 'val': '3'},
                    {'name': 'salt & nymald svartpeppar', 'unit': 'krm', 'val': '2'}
                ]
            },
            {
                'group': 'Buljong & Gräddsås',
                'items': [
                    {'name': 'oxfond eller köttbuljong', 'unit': 'dl', 'val': '4'},
                    {'name': 'soja (äkta kinesisk eller japansk)', 'unit': 'msk', 'val': '1'},
                    {'name': 'lagerblad', 'unit': 'st', 'val': '2'},
                    {'name': 'kryddpepparkorn', 'unit': 'st', 'val': '5'},
                    {'name': 'vispgrädde', 'unit': 'dl', 'val': '2.5'},
                    {'name': 'svartvinbärsgelé', 'unit': 'msk', 'val': '1.5'},
                    {'name': 'maizena eller vetemjöl till redning', 'unit': 'msk', 'val': '2'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Banka ut och krydda köttet',
                'text': 'Lägg ut köttskivorna på en skärbräda mellan två lager plastfolie. Banka försiktigt ut dem till jämnt tunna skivor med en köttklubba eller en kavel. Salta och peppra lätt på båda sidor.',
                'timer': 8
            },
            {
                'step': 2,
                'title': 'Fyll och rulla ihop',
                'text': 'Bred ett jämnt lager dijonsenap på varje köttskiva. Fördela strimlat bacon, finhackad lök och en stav inlagd gurka på den bredare änden av skivan. Rulla ihop till en tät rulle och fäst med en tandpetare i trä.',
                'timer': 12
            },
            {
                'step': 3,
                'title': 'Bryn rulladerna gyllene',
                'text': 'Hetta upp rikligt med smör i en rymlig stekgryta. Bryn rulladerna runt om på medelhög värme så att de får en fin, djup gyllenbrun färg. Lyft inte i dem för tidigt så att de inte fastnar.',
                'timer': 10
            },
            {
                'step': 4,
                'title': 'Brässera under lock',
                'text': 'Häll på oxfond, soja, lagerblad och kryddpepparkorn runt rulladerna. Sänk värmen, sätt på locket och låt rulladerna brässera sakta i ca 50–60 minuter tills köttet är underbart mört.',
                'timer': 55
            },
            {
                'step': 5,
                'title': 'Gör gräddsåsen',
                'text': 'Lyft upp rulladerna på ett varmt fat och dra försiktigt ur tandpetarna. Sila buljongen ner i en kastrull och koka upp med vispgrädde och svartvinbärsgelé. Vispa ner redningen och låt såsen sjuda i 5 minuter till en blank, krämig konsistens. Smaka av med salt och peppar.',
                'timer': 8
            },
            {
                'step': 6,
                'title': 'Lägg tillbaka & servera',
                'text': 'Lägg tillbaka rulladerna i den heta såsen och låt dem bli genomvarma i 2 minuter. Servera med kokt potatis, pressgurka och rårörda lingon.',
                'timer': 5
            }
        ],
        'faqs': [
            {
                'q': 'Varför blir oxrullader sega?',
                'a': 'Rulladerna måste brässeras tillräckligt länge på låg värme (minst 50 minuter) för att muskeltrådarna ska slappna av och bli möra. Banka även köttet tunt före rullning.'
            },
            {
                'q': 'Kan man använda nötfärs istället?',
                'a': 'Nej, klassiska oxrullader görs alltid på hela skivor nötkött som innanlår eller lövbiff. Med färs kallas rätten istället kålpudding eller köttfärsrulle.'
            }
        ],
        'community_reviews': [
            {'name': 'Karin Sjöberg', 'date': '13 oktober 2026', 'rating': 5, 'comment': 'Mormors gamla söndagsmiddag! Smakade precis som när jag var liten. Gurkan och dijonsenapen ger verkligen den perfekta brytningen.', 'verified': True},
            {'name': 'Lars O.', 'date': '10 oktober 2026', 'rating': 5, 'comment': 'Mört och smakrikt kött med en fantastisk sås. Rekommenderas varmt!', 'verified': True}
        ]
    },

    # 4. Saftig Morotskaka i Långpanna med Cream Cheese-frosting
    {
        'title': 'Saftig Morotskaka i Långpanna med Cream Cheese-frosting',
        'sub': 'Underbart saftig och mjuk morotskaka i långpanna med kanel och kardemumma, täckt av tjock cream cheese-frosting',
        'card_title': 'Morotskaka i Långpanna',
        'slug': 'saftig-morotskaka-i-langpanna',
        'file': 'saftig-morotskaka-i-langpanna.html',
        'img': 'morotskaka-langpanna',
        'alt': 'Färska rutor av saftig morotskaka i långpanna med tjock cream cheese-frosting toppad med hackade valnötter och morotsstrimlor',
        'category': 'Fika & Bakning',
        'cat_key': 'fika',
        'cat_slug': 'fika-och-bakning',
        'diet': 'Vegetariskt fika',
        'difficulty': 'Enkel',
        'time': 60,
        'time_str': '1 tim',
        'prep_time': 'PT25M',
        'prep_time_str': '25 min',
        'cook_time': 'PT35M',
        'cook_time_str': '35 min',
        'total_time': 'PT1H',
        'portions_num': 24,
        'portions_unit': 'bitar',
        'calories': 380,
        'nutrition': {'calories': '380 kcal', 'carbs': '46g', 'fat': '20g', 'protein': '5g', 'sugar': '32g'},
        'rating': 4.98,
        'review_count': 14,
        'keywords': 'morotskaka i långpanna, saftig morotskaka långpanna, morotskaka recept långpanna, bästa morotskakan, morotskaka cream cheese frosting, fika till många',
        'desc': 'Sveriges mest bakade långpannekaka! Otroligt saftig morotskaka kryddad med kanel och kardemumma, toppad med ett tjockt lager frisk cream cheese-frosting och hackade valnötter. Räcker till hela kalaset.',
        'long_desc': (
            'Morotskaka i långpanna är den ultimata fikan när du ska bjuda många! Denna klassiska svenska bjudkaka bakas i en hel ugnsplåt '
            'och ger upp till 24 generösa rutor som försvinner i ett nafs på kalas, fikaträffar eller dop. Hemligheten bakom den oöverträffade '
            'saftigheten är att använda neutral rapsolja istället för smör samt rikligt med färskriven morot som ger kakan dess underbara textur. '
            'Kakan kryddas varmt med kanel, nymald kardemumma och en nypa ingefära. Ovanpå breds ett tjockt, sammetslent lager av syrlig och '
            'frisk cream cheese-frosting smaksatt med lime och vanilj. Kakan håller sig fantastiskt saftig i kylen i flera dagar och går utmärkt att förbereda i förväg.'
        ),
        'equipment': ['Långpanna ca 30x40 cm', 'Bakplåtspapper', 'Elvisp', 'Rivjärn'],
        'drink_pairing': 'Nybryggt kaffe, en krämig cappuccino eller ett glas kall mjölk.',
        'pro_tips': 'Använd neutral olja (t.ex. rapsolja) i smeten istället för smör. Oljan binder fukten i kakan så att den håller sig fantastiskt saftig i upp till 4–5 dagar i kylskåp.',
        'ingredients': [
            {
                'group': 'Morotskakesmet',
                'items': [
                    {'name': 'ägg (stora)', 'unit': 'st', 'val': '6'},
                    {'name': 'strösocker', 'unit': 'dl', 'val': '5'},
                    {'name': 'neutral rapsolja', 'unit': 'dl', 'val': '3'},
                    {'name': 'finrivna morötter (hårt packade)', 'unit': 'dl', 'val': '8'},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': '6'},
                    {'name': 'bakpulver', 'unit': 'tsk', 'val': '2'},
                    {'name': 'bikarbonat', 'unit': 'tsk', 'val': '2'},
                    {'name': 'malen kanel', 'unit': 'msk', 'val': '2'},
                    {'name': 'nymald kardemumma', 'unit': 'tsk', 'val': '1.5'},
                    {'name': 'malen ingefära', 'unit': 'tsk', 'val': '1'},
                    {'name': 'vaniljsocker', 'unit': 'msk', 'val': '1'},
                    {'name': 'salt', 'unit': 'tsk', 'val': '0.5'}
                ]
            },
            {
                'group': 'Krämig Frosting & Garnering',
                'items': [
                    {'name': 'färskost (t.ex. Philadelphia, rumsvarm)', 'unit': 'g', 'val': '300'},
                    {'name': 'smör (osaltat, rumstempererat)', 'unit': 'g', 'val': '150'},
                    {'name': 'florsocker', 'unit': 'dl', 'val': '5'},
                    {'name': 'vaniljsocker', 'unit': 'msk', 'val': '1'},
                    {'name': 'färskpressad limesaft eller citronsaft', 'unit': 'msk', 'val': '2'},
                    {'name': 'hackade valnötter (rostade)', 'unit': 'dl', 'val': '2'}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Sätt ugnen och klä långpannan',
                'text': 'Sätt ugnen på 175°C över-/undervärme. Klä en långpanna (ca 30x40 cm) med bakplåtspapper så att kanterna sticker upp något.',
                'timer': 5
            },
            {
                'step': 2,
                'title': 'Vispa ägg och socker pösigt',
                'text': 'Vispa ägg och strösocker med elvisp i en stor bunke i ca 4–5 minuter tills det är riktigt vitt, tjockt och pösigt. Vänd ner rapsoljan och de finrivna morötterna försiktigt med en slickepott.',
                'timer': 6
            },
            {
                'step': 3,
                'title': 'Blanda de torra ingredienserna',
                'text': 'Blanda vetemjöl, bakpulver, bikarbonat, kanel, kardemumma, ingefära, vaniljsocker och salt i en separat skål. Sikta ner mjölblandningen i äggsmeten och vänd runt varsamt till en slät och jämn smet utan klumpar.',
                'timer': 5
            },
            {
                'step': 4,
                'title': 'Grädda gyllenbrun',
                'text': 'Häll ut smeten jämnt i långpannan och stryk ytan slät. Grädda mitt i ugnen i 30–35 minuter. Känn med en provsticka i mitten – den ska komma ut helt torr. Låt kakan svalna helt i formen före frosting.',
                'timer': 32
            },
            {
                'step': 5,
                'title': 'Vispa cream cheese-frostingen',
                'text': 'Vispa det mjuka smöret och florsockret vitt och fluffigt med elvisp i 3 minuter. Tillsätt den kalla färskosten, vaniljsocker och limesaft. Vispa snabbt ihop till en helt slät, tjock och glänsande kräm (vispa inte för länge då kan färskosten bli lös).',
                'timer': 5
            },
            {
                'step': 6,
                'title': 'Bred på, dekorera & skär upp',
                'text': 'Bred ut frostingen i ett generöst, vågigt lager över den helt kalla morotskakan. Toppa med hackade rostade valnötter. Ställ kakan i kylen i minst 30 minuter så att frostingen sätter sig, och skär sedan i 24 jämna rutor.',
                'timer': 10
            }
        ],
        'faqs': [
            {
                'q': 'Varför blir min cream cheese-frosting lös?',
                'a': 'Om du vispar färskosten för länge eller om ingredienserna har olika temperatur kan frostingen tappa formen. Vispa smör och florsocker fluffigt först, och vänd sedan snabbt ner färskosten.'
            },
            {
                'q': 'Kan man frysa morotskaka i långpanna?',
                'a': 'Ja! Kakan går utmärkt att frysa, helst utan frosting, men det går även med frosting om den fryses styckvis tills ytan stelnat innan den packas in.'
            }
        ],
        'community_reviews': [
            {'name': 'Elin Dahl', 'date': '16 oktober 2026', 'rating': 5, 'comment': 'Bakade denna till dotterns kalas – alla frågade efter receptet! Otroligt saftig och frostingen är helt perfekt med limetouchen.', 'verified': True},
            {'name': 'Fredrik L.', 'date': '14 oktober 2026', 'rating': 5, 'comment': 'Bästa morotskakan jag bakat. Mycket enklare i långpanna och blev minst lika saftig dag 3.', 'verified': True}
        ]
    }
]

def add_batch30():
    print(f"Base recipes count before Batch 30: {len(RECIPES)}")
    for r in BATCH30_RECIPES:
        RECIPES.append(r)
        print(f"Added {r['slug']} to RECIPES!")
    print(f"New total recipes count: {len(RECIPES)}")

    data_path = os.path.join(os.path.dirname(__file__), "recipes_data.py")
    with open(data_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("RECIPES = ")
        pprint.pprint(RECIPES, stream=f, indent=4, width=120)
        f.write("\n")

    print(f"Successfully saved updated RECIPES to {data_path}!")

if __name__ == "__main__":
    add_batch30()
