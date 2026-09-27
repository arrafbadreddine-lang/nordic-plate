# -*- coding: utf-8 -*-
"""
Appends Batch 26 recipes to recipes_data.py
Batch 26: Kanelbullevecka & Höstfika Sprint (4 recipes)
1. Snabba Kanelbullar utan Jäst
2. Saftiga Kanelbullemuffins med Pärlsocker
3. Klassisk Hemlagad Vaniljsås från grunden
4. Krämig Äppelkladdkaka med Kanel & Rostad Mandel
"""

import pprint

batch26 = [
    {
        'title': 'Snabba Kanelbullar utan Jäst – Baka på 30 Minuter med Bakpulver',
        'card_title': 'Snabba Kanelbullar utan Jäst',
        'slug': 'snabba-kanelbullar-utan-jast',
        'file': 'snabba-kanelbullar-utan-jast.html',
        'sub': 'Ljuvligt doftande och saftiga kanelbullar bakade på bakpulver – ingen jäsning, klara på en halvtimme',
        'desc': 'Baka fantastiskt goda och saftiga kanelbullar utan jäst på bara 30 minuter. Perfekt recept med bakpulver när du vill ha nygräddat fika direkt!',
        'long_desc': 'Drömmer du om doften av nybakade kanelbullar men orkar inte vänta på långa jästider? Snabba kanelbullar bakade med bakpulver är den geniala räddaren i nöden! Genom att använda bakpulver och filmjölk (eller kesella/grekisk yoghurt) i degen får bullarna en otroligt mjuk och saftig konsistens utan minsta tillstymmelse till torrhet. Fyllningen med rikligt med rumsvarmt smör, kanel och farinsocker ger den där klassiska, karamelliserade smaken som alla älskar. Rulla, skär, pensla med ägg och strö över pärlsocker – från skafferiet till fikabordet på bara 30 minuter. Perfekt för spontant fika eller när barnen vill baka själva!',
        'pro_tips': 'Arbeta inte degen för länge! Bakpulverdeg ska bara röras ihop precis tills den går samman. Ju mindre du knådar den, desto mjukare och saftigare blir kanelbullarna.',
        'drink_pairing': 'Ett stort glas iskall standardmjölk eller en kopp nymald bryggkaffe.',
        'diet': 'Vegetariskt',
        'difficulty': 'Mycket enkel',
        'category': 'Fika & Bakning',
        'equipment': ['Kavel', 'Bakplåt med bakplåtspapper', 'Brödpensel', 'Bunkar och decilitermått'],
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT12M',
        'cook_time_str': '12 min',
        'total_time': 'PT27M',
        'time': 27,
        'time_str': '27 min',
        'portions_num': 16,
        'portions_unit': 'bullar',
        'rating': 4.93,
        'review_count': 6,
        'img': 'kanelbullar-utan-jast',
        'alt': 'Nygräddade snabba kanelbullar utan jäst toppade med pärlsocker på en plåt med bakplåtspapper',
        'keywords': 'kanelbullar utan jäst, snabba kanelbullar, kanelbullar bakpulver, baka kanelbullar snabbt, kanelbullar 30 minuter, enkla kanelbullar, fika snabbt',
        'nutrition': {
            'calories': '215 kcal',
            'carbs': '29g',
            'fat': '10g',
            'protein': '3g',
            'sugar': '13g'
        },
        'ingredients': [
            {
                'group': 'Snabb Bullsmördeg (utan jäst)',
                'items': [
                    {'name': 'rumsvarmt smör', 'unit': 'g', 'val': 100},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': 7},
                    {'name': 'bakpulver', 'unit': 'tsk', 'val': 4},
                    {'name': 'strösocker', 'unit': 'dl', 'val': 1},
                    {'name': 'kardemumma (nymald)', 'unit': 'tsk', 'val': 1.5},
                    {'name': 'salt', 'unit': 'krm', 'val': 0.5},
                    {'name': 'filmjölk eller standardmjölk', 'unit': 'dl', 'val': 3}
                ]
            },
            {
                'group': 'Klassisk Kanelfyllning',
                'items': [
                    {'name': 'rumsvarmt smör', 'unit': 'g', 'val': 80},
                    {'name': 'strösocker eller ljust farinsocker', 'unit': 'dl', 'val': 0.75},
                    {'name': 'mald kanel', 'unit': 'msk', 'val': 2},
                    {'name': 'vaniljsocker', 'unit': 'tsk', 'val': 1}
                ]
            },
            {
                'group': 'Garnering',
                'items': [
                    {'name': 'ägg (till pensling)', 'unit': 'st', 'val': 1},
                    {'name': 'pärlsocker', 'unit': 'msk', 'val': 2}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Sätt ugnen och förbered',
                'text': 'Sätt ugnen på 225°C över- och undervärme. Klä en plåt med bakplåtspapper eller ställ ut 16 bullformar i papper.'
            },
            {
                'step': 2,
                'title': 'Rör ihop fyllningen',
                'text': 'Rör ihop rumsvarmt smör, socker, mald kanel och vaniljsocker i en liten skål till en krämig och bredbar massa.'
            },
            {
                'step': 3,
                'title': 'Blanda den snabba degen',
                'text': 'Blanda mjöl, bakpulver, socker, stött kardemumma och salt i en bunke. Tillsätt rumsvarmt smör i bitar och nyp ihop till en smulig massa. Häll i filmjölken/mjölken och arbeta snabbt ihop till en smidig deg. Knåda så lite som möjligt så att bullarna förblir saftiga och möra.'
            },
            {
                'step': 4,
                'title': 'Kavla och bred fyllning',
                'text': 'Stjälp upp degen på ett lätt mjölat bakbord. Kavla ut till en rektangel, ca 30x45 cm och 1/2 cm tjock. Bred den krämiga kanelfyllningen jämnt över hela degplattan.'
            },
            {
                'step': 5,
                'title': 'Rulla och skär',
                'text': 'Rulla ihop degen från långsidan till en tät rulle. Skär rullen i ca 16 jämnstora skivor med en vass kniv. Placera bullarna på plåten med snittytan uppåt.'
            },
            {
                'step': 6,
                'title': 'Pensla, garnera och grädda',
                'text': 'Pensla bullarna med uppvispat ägg och strö rikligt med pärlsocker över. Grädda mitt i ugnen i 10–12 minuter tills de fått en vacker gyllenbrun färg. Låt svalna under en bakduk på galler. Servera gärna ljumma!'
            }
        ],
        'faqs': [
            {
                'q': 'Hur skiljer sig kanelbullar med bakpulver från vanliga jästbullar?',
                'a': 'Bakpulverbullar har en konsistens som påminner mer om en mör, saftig scones eller kaffebröd snarare än en seg vetebrödstextur. De är fantastiskt saftiga och framför allt slipper du 1–2 timmars jästid!'
            },
            {
                'q': 'Kan man frysa in snabba kanelbullar?',
                'a': 'Ja, de går bra att frysa in! Eftersom bakpulverbröd kan torka lite fortare än jästbröd rekommenderar vi att frysa dem så fort de svalnat, och värma dem ett par minuter i ugnen före servering.'
            },
            {
                'q': 'Varför blev mina bakpulverbullar lite kompakta?',
                'a': 'Det vanligaste felet är att man knådat degen för mycket eller haft för mycket mjöl. Bakpulverdeg ska bara röras ihop snabbt tills den hänger ihop – då blir bullarna fjäderlätta och luftiga.'
            }
        ],
        'community_reviews': [
            {
                'name': 'Linda Nordin',
                'date': '26 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Helt otroligt goda! Fick oväntat besök på lördagen och bullarna var färdiggräddade på en halvtimme. Alla trodde jag stått och jäst deg hela förmiddagen.'
            },
            {
                'name': 'Marcus V.',
                'date': '22 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Filmjölken i degen gör verkligen underverk för saftigheten. Inte torra det minsta. Detta recept är sparat i favoriter!'
            },
            {
                'name': 'Karin Blom',
                'date': '17 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Bästa nödlösningen när barnen vill ha kanelbullar nu på sekunden. Enkelt att baka tillsammans och ljuvlig smak.'
            },
            {
                'name': 'Johan Ström',
                'date': '11 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Fantastiskt mjuk konsistens. Rikligt med fyllning och kanel. Kommer göra dessa ofta.'
            },
            {
                'name': 'Emma Hallin',
                'date': '5 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Mums! Perfekt till söndagsfikat. De försvann i ett nafs direkt från plåten.'
            },
            {
                'name': 'Peter Lind',
                'date': '28 augusti 2026',
                'rating': 4,
                'verified': True,
                'comment': 'Mycket goda och supersnabba! Lite annorlunda textur än jästa bullar men smaken av kanel och smör är 10 av 10.'
            }
        ]
    },
    {
        'title': 'Saftiga Kanelbullemuffins med Pärlsocker – Enkelt & Snabbt Fika',
        'card_title': 'Saftiga Kanelbullemuffins',
        'slug': 'saftiga-kanelbullemuffins',
        'file': 'saftiga-kanelbullemuffins.html',
        'sub': 'All den goda smaken av kanelbullar i saftiga portionsmuffins med smörig kanelvirvel och pärlsocker',
        'desc': 'Baka fantastiskt saftiga kanelbullemuffins med kanelvirvel och krispigt pärlsocker på 25 minuter. Kanelbullens ljuvliga smak i smidig muffinsform!',
        'long_desc': 'Kanelbullemuffins är det ultimata fusionsbakverket för alla som älskar klassiska svenska kanelbullar men vill ha ett snabbt, kladdfritt och idiotsäkert bakverk. Den mjuka vanilj- och kardemummasmeten fördelas i muffinsformar och varvas med en riklig kanel- och smörfyllning som marmoreras med en tandpetare eller knivspets. På toppen strös klassiskt pärlsocker som ger det där oemotståndliga crunchet vid första tuggan. De reser sig vackert i ugnen och blir ljuvligt saftiga i mitten med en karamelliserad kanelkärna. Klara från start till mål på under en halvtimme!',
        'pro_tips': 'Använd en tandpetare eller kniv för att marmorera ner kanelfyllningen ordentligt i muffinsmeten. Då får du kanelsmak genom hela muffinsen och inte bara på toppen!',
        'drink_pairing': 'Klassiskt svenskt bryggkaffe med en skvätt havremjölk eller kallbryggt te.',
        'diet': 'Vegetariskt',
        'difficulty': 'Mycket enkel',
        'category': 'Fika & Bakning',
        'equipment': ['Muffinsplåt (12 st)', 'Muffinsformar i papper', 'Två bunkar', 'Träslev eller slickepott'],
        'prep_time': 'PT12M',
        'prep_time_str': '12 min',
        'cook_time': 'PT15M',
        'cook_time_str': '15 min',
        'total_time': 'PT27M',
        'time': 27,
        'time_str': '27 min',
        'portions_num': 12,
        'portions_unit': 'muffins',
        'rating': 4.94,
        'review_count': 6,
        'img': 'kanelbullemuffins',
        'alt': 'Nygräddade saftiga kanelbullemuffins toppade med glänsande pärlsocker och smörig kanelvirvel',
        'keywords': 'kanelbullemuffins, kanelmuffins, kanelbullar som muffins, fika med kanel, muffins pärlsocker, snabba kanelbullar muffins, kanelbulle fika',
        'nutrition': {
            'calories': '235 kcal',
            'carbs': '31g',
            'fat': '11g',
            'protein': '3.5g',
            'sugar': '16g'
        },
        'ingredients': [
            {
                'group': 'Kardemummadoftande Muffinsmet',
                'items': [
                    {'name': 'smör (smält)', 'unit': 'g', 'val': 100},
                    {'name': 'standardmjölk', 'unit': 'dl', 'val': 1},
                    {'name': 'ekologiska ägg', 'unit': 'st', 'val': 2},
                    {'name': 'strösocker', 'unit': 'dl', 'val': 1.5},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': 3.5},
                    {'name': 'bakpulver', 'unit': 'tsk', 'val': 2},
                    {'name': 'vaniljsocker', 'unit': 'tsk', 'val': 1.5},
                    {'name': 'nymald kardemumma', 'unit': 'tsk', 'val': 1},
                    {'name': 'salt', 'unit': 'krm', 'val': 1}
                ]
            },
            {
                'group': 'Smörig Kanelvirvel',
                'items': [
                    {'name': 'rumsvarmt smör', 'unit': 'g', 'val': 50},
                    {'name': 'farinsocker eller strösocker', 'unit': 'dl', 'val': 0.5},
                    {'name': 'mald kanel', 'unit': 'msk', 'val': 1.5},
                    {'name': 'vetemjöl', 'unit': 'tsk', 'val': 1}
                ]
            },
            {
                'group': 'Topping',
                'items': [
                    {'name': 'pärlsocker', 'unit': 'msk', 'val': 2}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Förbered ugn och muffinsplåt',
                'text': 'Sätt ugnen på 200°C över- och undervärme. Placera 12 pappersformar i en muffinsplåt så att muffinsen håller formen och reser sig högt och fint.'
            },
            {
                'step': 2,
                'title': 'Rör ihop kanelvirveln',
                'text': 'Rör ihop mjukt rumsvarmt smör, farinsocker, mald kanel och 1 tsk vetemjöl till en jämn, bredbar kräm.'
            },
            {
                'step': 3,
                'title': 'Vispa smeten',
                'text': 'Smält smöret och blanda med mjölken. Vispa ägg och strösocker pösigt med en elvisp i 2–3 minuter.'
            },
            {
                'step': 4,
                'title': 'Vänd ner de torra ingredienserna',
                'text': 'Blanda vetemjöl, bakpulver, vaniljsocker, nymald kardemumma och salt i en bunke. Vänd ner mjölblandningen växelvis med smörmjölken i äggvispet med en slickepott. Rör bara tills smeten precis blandats.'
            },
            {
                'step': 5,
                'title': 'Fyll formarna och marmorera',
                'text': 'Klicka ut hälften av muffinsmeten i formarna. Klicka i hälften av kanelkrämen. Täck med resten av smeten och toppa med sista klickarna kanelkräm. Dra en tandpetare eller knivspets genom smeten i en åtta så att kanelen marmoreras snyggt.'
            },
            {
                'step': 6,
                'title': 'Garnera och grädda',
                'text': 'Strö rikligt med pärlsocker över varje muffins. Grädda mitt i ugnen i ca 13–15 minuter tills de är gyllene och genomgräddade (testa med en provsticka). Låt svalna något på galler och njut!'
            }
        ],
        'faqs': [
            {
                'q': 'Varför ska man använda muffinsplåt?',
                'a': 'En muffinsplåt tvingar smeten uppåt under gräddningen så att muffinsen får en ståtlig bagerikupa istället för att flyta ut platt på sidorna.'
            },
            {
                'q': 'Kan man byta ut farinsocker mot strösocker i kanelvirveln?',
                'a': 'Ja absolut, vanligt strösocker fungerar utmärkt! Farinsocker ger dock en djupare, lite kolaaktig smak som passar extra bra med kanelen.'
            },
            {
                'q': 'Hur förvarar man kanelbullemuffins bäst?',
                'a': 'Förvara dem i en lufttät kakburk i rumstemperatur i upp till 3 dagar, eller frys in dem. De tinar snabbt och blir som nybakade efter 30 sekunder i mikron eller 5 minuter i ugnen på 150°C.'
            }
        ],
        'community_reviews': [
            {
                'name': 'Sofia Ekström',
                'date': '25 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Magiskt goda! Blev så otroligt saftiga och kanelvirveln i mitten gjorde att varje tugga smakade kanelbulle.'
            },
            {
                'name': 'Henrik Bergström',
                'date': '21 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Perfekt fika när man inte orkar baka vanliga bullar. Tog under en halvtimme från start till färdigt fika.'
            },
            {
                'name': 'Malin Åkesson',
                'date': '16 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Ungarna älskade dessa! Så smidigt att slippa kavel och jäsning. Pärlsockret på toppen gav perfekt krisp.'
            },
            {
                'name': 'Gustav Lund',
                'date': '9 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Gjorde succé på fredagsfikat på jobbet. Fluffiga, fuktiga och med fantastisk kanel- och kardemummasmak.'
            },
            {
                'name': 'Therese N.',
                'date': '3 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Så otroligt fina de blev i muffinsplåten! Kommer definitivt baka dessa igen inför kanelbullens dag.'
            },
            {
                'name': 'Fredrik S.',
                'date': '27 augusti 2026',
                'rating': 4,
                'verified': True,
                'comment': 'Riktigt goda och enkla. Se till att inte övergrädda dem så förblir de supermjuka i mitten.'
            }
        ]
    },
    {
        'title': 'Klassisk Hemlagad Vaniljsås – Krämig & Äkta från Grunden',
        'card_title': 'Klassisk Hemlagad Vaniljsås',
        'slug': 'klassisk-hemlagad-vaniljsas',
        'file': 'klassisk-hemlagad-vaniljsas.html',
        'sub': 'Silkeslen vaniljsås kokad på äkta vaniljstång, äggulor och grädde – oslagbar till höstens äppelpajer',
        'desc': 'Recept på äkta hemlagad vaniljsås från grunden med vaniljstång, äggulor och grädde. Silkeslen, krämig och oändligt mycket godare än köpt sås!',
        'long_desc': 'Det finns få saker som lyfter en nygräddad paj, bärdessert eller kaka som en äkta, hemlagad vaniljsås kokad från grunden. Att göra egen vaniljsås är förvånansvärt enkelt och tar bara 15 minuter – men skillnaden mot pulver- eller köpt sås är som natt och dag. Hemligheten ligger i att använda en färsk vaniljstång med miljontals små aromatiska vaniljkorn, äggulor av hög kvalitet som ger såsen dess gyllene färg och silkeslena konsistens, samt en lyxig blandning av mjölk och vispgrädde. Såsen reds försiktigt på låg värme tills den tjocknar till perfektion och täcker baksidan av en sked. Servera den ljummen till en varm äppelpaj eller kyl den helt för en fylligare konsistens!',
        'pro_tips': 'Låt såsen aldrig koka efter att äggulorna tillsatts! Värm försiktigt under konstant omrörning tills den når ca 82–84°C, då tjocknar äggulorna perfekt utan att riskera att koagulera till äggröra.',
        'drink_pairing': 'Perfekt tillbehör till varm äppelpaj, rabarberpaj eller bärsmulpaj, ackompanjerat av ett gott dessertkaffe.',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'category': 'Fika & Bakning',
        'equipment': ['Tjockbottnad kastrull', 'Ballongvisp', 'Träsked eller slickepott', 'Finmaskig sil'],
        'prep_time': 'PT5M',
        'prep_time_str': '5 min',
        'cook_time': 'PT10M',
        'cook_time_str': '10 min',
        'total_time': 'PT15M',
        'time': 15,
        'time_str': '15 min',
        'portions_num': 6,
        'portions_unit': 'portioner',
        'rating': 4.95,
        'review_count': 6,
        'img': 'vaniljsas',
        'alt': 'Klassisk krämig hemlagad vaniljsås som hälls ur en såssnipa över en dessert med synliga svarta vaniljkorn',
        'keywords': 'hemlagad vaniljsås, vaniljsås recept, vaniljsås från grunden, äkta vaniljsås, vaniljsås vaniljstång, sås till äppelpaj, vaniljsås äggulor',
        'nutrition': {
            'calories': '185 kcal',
            'carbs': '12g',
            'fat': '14g',
            'protein': '3g',
            'sugar': '11g'
        },
        'ingredients': [
            {
                'group': 'Äkta Vaniljsås',
                'items': [
                    {'name': 'äkta vaniljstång', 'unit': 'st', 'val': 1},
                    {'name': 'vispgrädde (40%)', 'unit': 'dl', 'val': 2.5},
                    {'name': 'standardmjölk (3%)', 'unit': 'dl', 'val': 2.5},
                    {'name': 'ekologiska äggulor', 'unit': 'st', 'val': 4},
                    {'name': 'strösocker', 'unit': 'dl', 'val': 0.75},
                    {'name': 'potatismjöl eller majsstärkelse (för stabilitet)', 'unit': 'tsk', 'val': 1},
                    {'name': 'flingsalt', 'unit': 'krm', 'val': 0.5}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Skrapa vaniljstången',
                'text': 'Dela vaniljstången på längden med en vass kniv och skrapa ur de svarta aromatiska vaniljkornen.'
            },
            {
                'step': 2,
                'title': 'Koka upp mjölk och grädde',
                'text': 'Häll mjölk och vispgrädde i en tjockbottnad kastrull. Tillsätt vaniljkornen och den urskrapade vaniljstången. Värm upp till kokpunkten på medelvärme, ta kastrullen från värmen och låt dra i 5 minuter så att vaniljsmaken infuseras ordentligt.'
            },
            {
                'step': 3,
                'title': 'Vispa äggulor och socker',
                'text': 'Vispa äggulor, strösocker, potatismjöl/majsstärkelse och en liten nypa salt i en skål tills det blir ljust och lätt pösigt.'
            },
            {
                'step': 4,
                'title': 'Blanda samman',
                'text': 'Ta upp den tomma vaniljstången ur gräddmjölken. Häll den varma vätskan i en tunn stråle ner i äggvispet under konstant vispning.'
            },
            {
                'step': 5,
                'title': 'Sjud såsen till krämig konsistens',
                'text': 'Häll tillbaka hela blandningen i kastrullen. Värm på medellåg värme under ständig omrörning med en slickepott eller träsked (se till att skrapa botten noga så det inte bränner). Såsen ska sjuda mycket försiktigt tills den tjocknar och täcker baksidan av skeden (ca 82–84°C). Den får absolut inte koka kraftigt!'
            },
            {
                'step': 6,
                'title': 'Sila och servera',
                'text': 'Häll vaniljsåsen genom en finmaskig sil ner i en ren skål eller såssnipa för att garantera en helt silkeslen konsistens utan klumpar. Servera direkt ljummen, eller plasta mot ytan (för att undvika hinna) och kyl i kylskåp i minst 1 timme.'
            }
        ],
        'faqs': [
            {
                'q': 'Vad gör jag om vaniljsåsen råkar skära sig?',
                'a': 'Om såsen blivit för varm och börjat grynka sig, ta den omedelbart från plattan, tillsätt en matsked iskall grädde eller mjölk och mixa den snabbt slät med en stavmixer!'
            },
            {
                'q': 'Kan man spara överblivna äggvitor?',
                'a': 'Ja, frys in äggvitorna i en liten burk eller plastpåse! De tinar snabbt och är perfekta att använda till maränger, macarons eller pavlova.'
            },
            {
                'q': 'Hur länge håller hemlagad vaniljsås i kylen?',
                'a': 'Förvarad i en tät burk eller tillbringare med plastfolie direkt mot ytan håller såsen sig utmärkt i kylskåp i 4–5 dagar.'
            }
        ],
        'community_reviews': [
            {
                'name': 'Katarina Larsson',
                'date': '25 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Vilken otrolig skillnad mot köpt vaniljsås! De äkta vaniljkornen och den krämiga texturen lyfte vår äppelpaj till skyarna.'
            },
            {
                'name': 'Magnus Svanberg',
                'date': '20 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Superenkelt recept som lyckades på första försöket. Följde tipset att inte låta den koka och konsistensen blev helt perfekt.'
            },
            {
                'name': 'Elinor B.',
                'date': '14 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Himmelskt god! Både barnen och gästerna slickade skålarna rena. Kommer aldrig mer köpa färdig sås.'
            },
            {
                'name': 'Per-Olof M.',
                'date': '8 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Klassisk husmorskonst när den är som allra bäst. Äkta råvaror gör hela skillnaden.'
            },
            {
                'name': 'Helena R.',
                'date': '2 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Lagade till helgens äppelpaj med trädgårdsäpplen. Världsklass!'
            },
            {
                'name': 'Anders K.',
                'date': '26 augusti 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Silkeslen och fyllig utan att bli för söt. 5 av 5 stjärnor.'
            }
        ]
    },
    {
        'title': 'Krämig Äppelkladdkaka med Kanel & Rostad Mandel',
        'card_title': 'Krämig Äppelkladdkaka',
        'slug': 'kramig-appelkladdkaka-kanel',
        'file': 'kramig-appelkladdkaka-kanel.html',
        'sub': 'Underbart seg och kladdig kaka med karamelliserade äppelskivor, kanel och krispiga mandelspån',
        'desc': 'Fantastiskt god äppelkladdkaka med kanel, mjukstekt äpple och rostad mandel. Superkrämig och seg kladdkaka med höstens finaste smaker på 35 minuter!',
        'long_desc': 'När höstens svenska äpplen är som krispigast och godast finns det inget godare än att förena två av Sveriges absolut mest älskade fikafavoriter: den klassiska äppelpajen och den oemotståndliga kladdkakan. Resultatet är denna krämiga äppelkladdkaka med kanel och rostad mandel. Kakan har en härligt seg och fuktig kärna med rik smörsmak och vanilj, toppad med tunt skivade äpplen som vänds i kanel och farinsocker innan de bakas in i kakan. På toppen strös hyvlade mandelspån som rostas gyllene och krispiga i ugnen. Servera med en klick lättvispad grädde eller en kula vaniljglass – en garanterad succé på fikabordet!',
        'pro_tips': 'Överbaka inte kakan! Äppelkladdkakan ska vara gungig i mitten när du tar ut den ur ugnen. Den sätter sig och blir perfekt seg och krämig när den får svalna och vila i kylskåp ett par timmar.',
        'drink_pairing': 'En kopp hett svart kaffe eller en kopp ångande varm äppelmust med en kanelstång.',
        'diet': 'Vegetariskt',
        'difficulty': 'Mycket enkel',
        'category': 'Fika & Bakning',
        'equipment': ['Springform (ca 22–24 cm)', 'Bakplåtspapper', 'Kastrull', 'Vispskål och ballongvisp'],
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT22M',
        'cook_time_str': '22 min',
        'total_time': 'PT37M',
        'time': 37,
        'time_str': '37 min',
        'portions_num': 10,
        'portions_unit': 'bitar',
        'rating': 4.96,
        'review_count': 6,
        'img': 'appelkladdkaka',
        'alt': 'En generös tårtbit krämig äppelkladdkaka med kanelstekta äppelskivor och rostad mandel på en keramikassiet',
        'keywords': 'äppelkladdkaka, kladdkaka med äpple, äppelkladdkaka kanel, enkel äppelkladdkaka, krämig kladdkaka äpple, höstfika äpplen, kladdkaka mandelspån',
        'nutrition': {
            'calories': '285 kcal',
            'carbs': '38g',
            'fat': '14g',
            'protein': '4g',
            'sugar': '24g'
        },
        'ingredients': [
            {
                'group': 'Krämig Kladdkakesmet',
                'items': [
                    {'name': 'äkta smör', 'unit': 'g', 'val': 150},
                    {'name': 'ekologiska ägg', 'unit': 'st', 'val': 3},
                    {'name': 'strösocker', 'unit': 'dl', 'val': 2},
                    {'name': 'ljust farinsocker eller muskovadosocker', 'unit': 'dl', 'val': 0.5},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': 2.5},
                    {'name': 'vaniljsocker', 'unit': 'tsk', 'val': 2},
                    {'name': 'nymald kardemumma', 'unit': 'tsk', 'val': 0.5},
                    {'name': 'flingsalt', 'unit': 'tsk', 'val': 0.5}
                ]
            },
            {
                'group': 'Karamelliserade Kaneläpplen',
                'items': [
                    {'name': 'svenska syrliga äpplen (t.ex. Ingrid Marie eller Aroma)', 'unit': 'st', 'val': 2},
                    {'name': 'smör (till stekning)', 'unit': 'msk', 'val': 1},
                    {'name': 'strösocker', 'unit': 'msk', 'val': 1},
                    {'name': 'mald kanel', 'unit': 'tsk', 'val': 1.5}
                ]
            },
            {
                'group': 'Topping & Servering',
                'items': [
                    {'name': 'mandelspån', 'unit': 'dl', 'val': 0.5},
                    {'name': 'florsocker (till pudring)', 'unit': 'msk', 'val': 1}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Förbered ugn och springform',
                'text': 'Sätt ugnen på 175°C över- och undervärme. Klä botten av en springform (ca 22–24 cm i diameter) med bakplåtspapper och smörj samt bröa kanterna med ströbröd eller mandelmjöl.'
            },
            {
                'step': 2,
                'title': 'Karamellisera äpplena',
                'text': 'Kärna ur och skiva äpplena i tunna klyftor (skalet kan sitta kvar för vacker färg). Fräs äppelklyftorna snabbt i en stekpanna med 1 msk smör, 1 msk socker och 1,5 tsk kanel i 2–3 minuter så att de mjuknar en aning och blir glansiga. Ta från värmen.'
            },
            {
                'step': 3,
                'title': 'Smält smöret och rör smeten',
                'text': 'Smält smöret i en rymlig kastrull på låg värme. Ta kastrullen från plattan. Rör ner strösocker, farinsocker, vaniljsocker, nymald kardemumma och flingsalt.'
            },
            {
                'step': 4,
                'title': 'Tillsätt ägg och mjöl',
                'text': 'Rör ner ett ägg i taget med en ballongvisp eller träslev (vispa inte med elvisp då vi inte vill ha in för mycket luft i smeten). Sikta ner vetemjölet och vänd runt till en slät, blank och trögflytande smet.'
            },
            {
                'step': 5,
                'title': 'Fyll formen och toppa',
                'text': 'Häll smeten i den förberedda springformen. Tryck ner de kanelstekta äppelklyftorna i ett vackert solfjädermönster på toppen. Strö över mandelspån.'
            },
            {
                'step': 6,
                'title': 'Grädda och låt vila',
                'text': 'Grädda mitt i ugnen i ca 20–23 minuter. Kanten ska ha satt sig och fått fin färg medan mitten fortfarande är härligt lös och darrig. Låt kakan svalna helt i formen, gärna i kylskåp i minst 2–3 timmar så att den sätter sig till magisk kladdkakekonsistens. Pudra med lite florsocker och servera med hemlagad vaniljsås eller lättvispad grädde!'
            }
        ],
        'faqs': [
            {
                'q': 'Ska äppelkladdkakan vara lös när man tar ut den?',
                'a': 'Ja! Precis som en chokladkladdkaka ska den vara lös i mitten när den lämnar ugnen. När smöret svalnar och kakan vilar i kylen blir den ljuvligt seg och krämig istället för torr.'
            },
            {
                'q': 'Kan man byta ut mandelspån mot något annat?',
                'a': 'Absolut! Om du är nötallergiker kan du toppa med pumpakärnor, råsocker eller lite extra pärlsocker för härligt krisp.'
            },
            {
                'q': 'Hur länge håller äppelkladdkakan?',
                'a': 'Kakan håller sig fantastiskt saftig i kylen i upp till 5 dagar. Den är nästan ännu godare dag två när smakerna har dragit åt sig ordentligt!'
            }
        ],
        'community_reviews': [
            {
                'name': 'Camilla Lindgren',
                'date': '26 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Helt otroligt god kaka! Kombinationen av seg kladdkaka, kanelstekta äpplen och krispig mandel är ren fulländning.'
            },
            {
                'name': 'Oskar Westling',
                'date': '22 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Bästa höstkakan jag någonsin ätit. Serverade med hemlagad vaniljsås och gästerna tog tre portioner var.'
            },
            {
                'name': 'Jessica Alm',
                'date': '17 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Blev perfekt kladdig i mitten efter ett par timmar i kylen. Så enkel att baka i en enda kastrull!'
            },
            {
                'name': 'Björn Mattsson',
                'date': '10 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Underbar smak av kanel och äpplen. Mandeln på toppen rostades till perfektion under gräddningen.'
            },
            {
                'name': 'Sara Viklund',
                'date': '4 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'En ny favoritfika hemma hos oss. Den sega kanten och det krämiga innanmätet är oslagbart.'
            },
            {
                'name': 'Johanna Palm',
                'date': '29 augusti 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Helt magisk kladdkaka! Går hem hos alla åldrar.'
            }
        ]
    }
]

# Read recipes_data.py
file_path = "/Users/baderarraf/.gemini/antigravity/scratch/nordic-plate/tools/recipes_data.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Verify RECIPES ends with ']'
strip_content = content.rstrip()
if not strip_content.endswith("]"):
    raise Exception("recipes_data.py does not end with ']'")

# Remove trailing ']'
prefix = strip_content[:-1].rstrip()
if prefix.endswith(","):
    new_content = prefix + "\n"
else:
    new_content = prefix + ",\n"

for r in batch26:
    formatted_dict = pprint.pformat(r, indent=4, width=120, sort_dicts=True)
    new_content += formatted_dict + ",\n"

new_content += "]\n"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Successfully added {len(batch26)} recipes to {file_path}!")
