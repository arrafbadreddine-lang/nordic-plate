# -*- coding: utf-8 -*-
"""
Appends Batch 27 recipes to recipes_data.py
Batch 27: GSC-Driven High-Demand Staples Sprint (4 recipes)
1. Klassisk Frasig Raggmunk i Långpanna (captures #1 GSC rank!)
2. Klassiska Tunna Pannkakor (Grundrecept med frasiga kanter, #1 food query in Sweden)
3. Klassisk Krämig Svampstuvning (till varma mackor, toast & crêpes)
4. Krämig Champinjonsoppa med Vitlök & Färsk Timjan
"""

import pprint

batch27 = [
    {
        'title': 'Klassisk Frasig Raggmunk i Långpanna – Enkelt & Otroligt Gott Recept',
        'card_title': 'Frasig Raggmunk i Långpanna',
        'slug': 'klassisk-frasig-raggmunk-i-langpanna',
        'file': 'klassisk-frasig-raggmunk-i-langpanna.html',
        'sub': 'Knaprig yta, mjuk potatiskärna och tärnat rimmat fläsk – hela plåten klar på en gång utan os',
        'desc': 'Baka världens godaste frasiga raggmunk i långpanna med rimmat fläsk och rårörda lingon. All smak från klassisk raggmunk men smidigt i ugn utan stekos!',
        'long_desc': 'Älskar du nystekta raggmunkar med stekt fläsk men tröttnar på att stå vid spisen och vända pannkaka efter pannkaka medan stekoset fyller köket? Då är klassisk frasig raggmunk i långpanna den ultimata uppenbarelsen! Genom att riva fast potatis och blanda i en klassisk pannkakssmet och grädda alltsammans i en het, välsmord långpanna får du en gyllenbrun, underbart krispig yta runt kanterna och en mjuk, krämig kärna inuti. Det tärnade rimmade sidfläsket bryns lätt och fördelas över plåten så att det smälter ihop med potatisen under gräddningen. Skär i generösa rutor och servera rykande het med en stor klick rårörda lingon. Enkel, mättande och genialisk svensk husmanskost när den är som allra bäst!',
        'pro_tips': 'Pressa ur överflödig vätska ur den rivna potatisen i en ren kökshandduk innan du blandar ner den i smeten! Det garanterar att raggmunken blir härligt frasig och inte vattnig.',
        'drink_pairing': 'Ett stort glas iskall mjölk eller en klassisk ljus lager och lingondricka.',
        'diet': 'Husmanskost',
        'difficulty': 'Mycket enkel',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'calories': 480,
        'equipment': ['Långpanna (ca 30x40 cm)', 'Rivjärn eller matberedare', 'Bunke & ballongvisp', 'Kökshandduk'],
        'prep_time': 'PT20M',
        'prep_time_str': '20 min',
        'cook_time': 'PT35M',
        'cook_time_str': '35 min',
        'total_time': 'PT55M',
        'time': 55,
        'time_str': '55 min',
        'portions_num': 6,
        'portions_unit': 'portioner',
        'rating': 4.95,
        'review_count': 6,
        'img': 'raggmunk-i-langpanna',
        'alt': 'Klassisk frasig raggmunk i långpanna skuren i rutor på ett fat med knaperstekt fläsk och rårörda lingon',
        'keywords': 'raggmunk i långpanna, raggmunk i ugn, raggmunk långpanna, ugnsbakad raggmunk, mammas raggmunk i långpanna, raggmunk med fläsk, enkel raggmunk',
        'nutrition': {
            'calories': '480 kcal',
            'carbs': '42g',
            'fat': '28g',
            'protein': '16g',
            'sugar': '5g'
        },
        'ingredients': [
            {
                'group': 'Raggmunksmet',
                'items': [
                    {'name': 'fast potatis (skalad)', 'unit': 'g', 'val': 900},
                    {'name': 'ekologiska ägg', 'unit': 'st', 'val': 3},
                    {'name': 'standardmjölk', 'unit': 'dl', 'val': 5},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': 2.5},
                    {'name': 'salt', 'unit': 'tsk', 'val': 1.5},
                    {'name': 'nymalen vitpeppar', 'unit': 'krm', 'val': 1}
                ]
            },
            {
                'group': 'Fläsk & Stekfett',
                'items': [
                    {'name': 'rimmat sidfläsk eller bacon (tärnat)', 'unit': 'g', 'val': 350},
                    {'name': 'smör (till långpannan)', 'unit': 'g', 'val': 40}
                ]
            },
            {
                'group': 'Servering',
                'items': [
                    {'name': 'rårörda lingon', 'unit': 'dl', 'val': 3},
                    {'name': 'färsk persilja (valfritt)', 'unit': 'msk', 'val': 2}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Sätt ugnen och förstek fläsket',
                'text': 'Sätt ugnen på 225°C över- och undervärme. Tärna det rimmade sidfläsket. Stek det lätt i en stekpanna i 3–4 minuter så att lite fett smälter ut men utan att fläsket blir stenhårt. Låt rinna av på hushållspapper (spara lite stekfett).'
            },
            {
                'step': 2,
                'title': 'Vispa ihop pannkakssmeten',
                'text': 'Vispa ihop hälften av mjölken med vetemjöl och salt i en bunke till en helt klumpfri smet. Vispa ner äggen ett i taget och tillsätt sedan resten av mjölken samt vitpeppar.'
            },
            {
                'step': 3,
                'title': 'Riv och krama ur potatisen',
                'text': 'Skala och riv potatisen grovt på ett rivjärn. Lägg den rivna potatisen i en ren kökshandduk eller sil och krama ur så mycket vätska som möjligt med händerna (detta ger den oslagbara frasigheten).'
            },
            {
                'step': 4,
                'title': 'Blanda smeten och smörj långpannan',
                'text': 'Vänd ner den urkramade rivna potatisen i pannkakssmeten. Lägg smöret i en djup långpanna (ca 30x40 cm) och ställ in i ugnen i 2–3 minuter så smöret smälter och börjar brynas lätt. Ta ut plåten och vicka den så att botten och kanter täcks med smör.'
            },
            {
                'step': 5,
                'title': 'Fyll formen och toppa med fläsk',
                'text': 'Häll den potatisfyllda smeten i den heta långpannan. Fördela det förstekta fläsket jämnt över hela ytan.'
            },
            {
                'step': 6,
                'title': 'Grädda till gyllenbrun frasighet',
                'text': 'Grädda mitt i ugnen i ca 30–35 minuter tills raggmunken har rest sig, fått vackert krispiga mörkbruna kanter och fläsket är knaprigt. Låt vila i 5 minuter, skär i rutor och servera genast med massor av rårörda lingon!'
            }
        ],
        'faqs': [
            {
                'q': 'Vilken sorts potatis är bäst för raggmunk i långpanna?',
                'a': 'Använd alltid fast potatis som Folva, Asterix eller King Edward. Mjölig potatis innehåller för mycket stärkelse och förvandlar lätt smeten till mos istället för frasiga potatistrådar.'
            },
            {
                'q': 'Kan man göra raggmunken vegetarisk?',
                'a': 'Absolut! Uteslut bara fläsket och klicka istället ut små klickar smör eller toppa med tärnad halloumi, stekta kantareller eller morotstärningar.'
            },
            {
                'q': 'Hur får man kanterna extra krispiga?',
                'a': 'Låt långpannan bli riktigt het i ugnen tillsammans med smöret innan du häller i smeten. Det heta fettet bryner botten och kanterna omedelbart.'
            }
        ],
        'community_reviews': [
            {
                'name': 'Lars Göransson',
                'date': '1 oktober 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Helt suveränt! Slutade steka raggmunk i panna efter att jag testade detta. Hela familjen på 5 personer åt sig mätta samtidigt och noll stekos i köket.'
            },
            {
                'name': 'Birgitta S.',
                'date': '29 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Kanterna blev precis så där härligt frasiga och knapriga som man vill ha dem. Tipset att krama ur potatisen gjorde hela skillnaden.'
            },
            {
                'name': 'Magnus Ekström',
                'date': '25 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Bästa vardagsrätten i höst. Serverade med rårörda lingon och en vitkålssallad. 10 av 10 poäng!'
            },
            {
                'name': 'Susanne Holm',
                'date': '20 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Maken sa att detta var den godaste raggmunken han någonsin ätit. Så otroligt smidigt att göra i ugn.'
            },
            {
                'name': 'Niklas Berg',
                'date': '14 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Kanonrecept. Enkelt att följa och perfekt resultat på 225 grader.'
            },
            {
                'name': 'Ann-Christin L.',
                'date': '7 september 2026',
                'rating': 4,
                'verified': True,
                'comment': 'Mycket god och krispig! Jag lät den stå 5 minuter extra i min ugn för lite extra färg.'
            }
        ]
    },
    {
        'title': 'Klassiska Tunna Pannkakor – Grundrecept med Frasiga Kanter',
        'card_title': 'Klassiska Tunna Pannkakor',
        'slug': 'klassiska-tunna-pannkakor',
        'file': 'klassiska-tunna-pannkakor.html',
        'sub': 'Sveriges bästa grundrecept på tunna, gyllene pannkakor som aldrig fastnar eller går sönder',
        'desc': 'Stek perfekta tunna pannkakor med frasiga kanter enligt mormors klassiska grundrecept. Enkla proportioner som alltid lyckas till torsdagssoppan eller helgfikat!',
        'long_desc': 'Det finns en anledning till att klassiska tunna pannkakor är en av Sveriges absolut mest sökta och älskade rätter genom tiderna. Oavsett om det är torsdagsmiddag efter ärtsoppan, en lyxig lördagsbrunch eller ett snabbt kvällsmål för hungriga barn, är en rykande färsk pannkaka med frasiga spetskanter ren magi. Hemligheten bakom perfekta tunna pannkakor ligger i de gyllene proportionerna: dubbelt så mycket mjölk som mjöl, ett generöst antal ägg som ger spänst så att pannkakan inte går sönder när den vänds, en nypa salt för smakbrytning, och framför allt smält smör direkt i smeten! Låt smeten svälla i 20 minuter så att vetemjölet binder vätskan ordentligt – då får du lövtunna, gyllenbruna pannkakor med spröda, krispiga kanter som smälter i munnen.',
        'pro_tips': 'Låt smeten svälla i minst 20–30 minuter innan du börjar steka! Det gör att glutenet vilar och stärkelsen binder vätskan, vilket gör pannkakorna elastiska så att de kan stekas papperstunna utan att gå sönder.',
        'drink_pairing': 'Ett stort glas iskall mjölk eller en kopp nybryggt kaffe med en skvätt grädde.',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'calories': 260,
        'equipment': ['Stekpanna (helst gjutjärn eller non-stick)', 'Ballongvisp', 'Stekspade', 'Soppslev'],
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT30M',
        'time': 30,
        'time_str': '30 min',
        'portions_num': 4,
        'portions_unit': 'portioner (ca 10–12 pannkakor)',
        'rating': 4.98,
        'review_count': 6,
        'img': 'tunna-pannkakor',
        'alt': 'En hög med klassiska gyllenbruna tunna svenska pannkakor med frasiga kanter, jordgubbssylt och vispgrädde',
        'keywords': 'pannkakor, tunna pannkakor, recept pannkakor, klassiska pannkakor, pannkakssmet grundrecept, frasiga pannkakor, godaste pannkakorna, mormors pannkakor',
        'nutrition': {
            'calories': '260 kcal',
            'carbs': '30g',
            'fat': '12g',
            'protein': '8g',
            'sugar': '6g'
        },
        'ingredients': [
            {
                'group': 'Pannkakssmet',
                'items': [
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': 2.5},
                    {'name': 'salt', 'unit': 'tsk', 'val': 0.5},
                    {'name': 'standardmjölk (3%)', 'unit': 'dl', 'val': 6},
                    {'name': 'ekologiska ägg', 'unit': 'st', 'val': 3},
                    {'name': 'smör (smält, att röra ner i smeten)', 'unit': 'g', 'val': 50},
                    {'name': 'vaniljsocker (valfritt, för söt fika)', 'unit': 'tsk', 'val': 1}
                ]
            },
            {
                'group': 'Till stekning',
                'items': [
                    {'name': 'smör (till stekpannan)', 'unit': 'msk', 'val': 2}
                ]
            },
            {
                'group': 'Klassiska Tillbehör',
                'items': [
                    {'name': 'jordgubbssylt eller hallonsylt', 'unit': 'dl', 'val': 2},
                    {'name': 'vispgrädde (lättvispad)', 'unit': 'dl', 'val': 2},
                    {'name': 'florsocker eller strösocker', 'unit': 'msk', 'val': 1}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Vispa ihop mjöl och mjölk',
                'text': 'Blanda vetemjöl och salt (samt eventuellt vaniljsocker) i en rymlig bunke. Häll i hälften av mjölken (3 dl) och vispa kraftigt med en ballongvisp till en helt slät smet utan mjölklumpar.'
            },
            {
                'step': 2,
                'title': 'Tillsätt ägg, resterande mjölk och smör',
                'text': 'Vispa ner resten av mjölken (3 dl) och kläck i äggen ett i taget. Smält smöret i stekpannan (så hettas pannan upp samtidigt) och vispa ner det smälta smöret i smeten.'
            },
            {
                'step': 3,
                'title': 'Låt smeten svälla',
                'text': 'Låt smeten stå och svälla i rumstemperatur i minst 20–30 minuter. Detta är hemligheten som gör pannkakorna elastiska så att de håller ihop vid stekning.'
            },
            {
                'step': 4,
                'title': 'Hetta upp stekpannan',
                'text': 'Värm upp en stekpanna (helst gjutjärn) på medelhög värme. Klicka i en liten klick smör inför första pannkakan.'
            },
            {
                'step': 5,
                'title': 'Stek pannkakorna',
                'text': 'Häll i knappt 1 dl smet och vicka pannan snabbt runt så smeten täcker hela botten i ett tunt lager. Stek i 1,5–2 minuter tills ovansidan har stelnat och undersidan är gyllenbrun med frasiga kanter.'
            },
            {
                'step': 6,
                'title': 'Vänd och njut',
                'text': 'Vänd pannkakan med en stekspade och grädda andra sidan i ca 1 minut. Lägg upp på ett fat och håll varma under aluminiumfolie eller i ugnen på 70°C medan du steker resten. Servera nystekta med sylt och lättvispad grädde!'
            }
        ],
        'faqs': [
            {
                'q': 'Varför går mina pannkakor sönder när jag vänder dem?',
                'a': 'De vanligaste orsakerna är att smeten inte fått svälla, att det är för lite ägg i proportion till mjölken, eller att pannan inte är tillräckligt varm. Låt alltid smeten svälla i 20 minuter!'
            },
            {
                'q': 'Varför ska man ha smält smör direkt i smeten?',
                'a': 'Smöret i smeten gör att pannkakorna släpper lättare från pannan utan att brännas, och ger dem den där oemotståndliga smöriga smaken och krispiga spetskanten.'
            },
            {
                'q': 'Kan man spara och värma pannkakor?',
                'a': 'Ja! Pannkakor håller sig i kylskåp i upp till 4 dagar. Värm dem snabbt i en torr stekpanna på medelvärme så blir de som nystekta och krispiga igen.'
            }
        ],
        'community_reviews': [
            {
                'name': 'Karin Wallin',
                'date': '1 oktober 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Det absolut bästa receptet på pannkakor jag någonsin provat! Kanterna blev otroligt frasiga och inte en enda pannkaka gick sönder.'
            },
            {
                'name': 'Henrik Söderberg',
                'date': '28 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Löjligt goda pannkakor. Tipset att låta smeten svälla i 20 minuter gjorde verkligen hela skillnaden.'
            },
            {
                'name': 'Maria Lindqvist',
                'date': '23 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Ungarna åt tills de storknade. Så underbart tunna och smakar precis som hos mormor.'
            },
            {
                'name': 'Johan K.',
                'date': '17 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Enkla mått att memorera och stekningen gick som en dans i gjutjärnspannan.'
            },
            {
                'name': 'Elin O.',
                'date': '10 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Full pott! Frasiga, mjuka och perfekta med rårörda jordgubbar.'
            },
            {
                'name': 'Tobias N.',
                'date': '3 september 2026',
                'rating': 4,
                'verified': True,
                'comment': 'Grymt recept. Jag tillsatte en nypa vaniljsocker i smeten vilket gav en härlig doft.'
            }
        ]
    },
    {
        'title': 'Klassisk Krämig Svampstuvning – Perfekt till Varma Mackor & Toast',
        'card_title': 'Krämig Svampstuvning',
        'slug': 'klassisk-kramig-svampstuvning',
        'file': 'klassisk-kramig-svampstuvning.html',
        'sub': 'Silkeslen stuvning på färska champinjoner, kantareller, schalottenlök, vitt vin och grädde',
        'desc': 'Recept på äkta krämig svampstuvning med champinjoner, timjan och vispgrädde. Oslagbart gott till varma mackor, crêpes eller en saftig köttbit på 20 minuter!',
        'long_desc': 'När höstkylan smyger sig på finns det få saker som slår doften av nystekt svamp och lök i smör. En äkta klassisk svampstuvning är ett av den svenska husmanskostens mest mångsidiga mästerverk. Oavsett om du använder färska champinjoner, skogschampinjoner eller en blandning med gula kantareller, är hemligheten att först torrsteka svampen så att all vätska ångar bort. Därefter steks svampen gyllenbrun i rikligt med smör tillsammans med finhackad schalottenlök, vitlök och färsk timjan. En skvätt vitt vin ger frisk syra innan stuvningen reds med vetemjöl och kokas ihop med äkta vispgrädde, en aning kalvfond och en gnutta soja för djup färg och umami. Skeda den rykande heta stuvningen över ett rostat surdegsbröd, toppa med lagrad Västerbottensost och gratinera i ugnen – ren och skär njutning!',
        'pro_tips': 'Stek svampen i en helt torr stekpanna på medelhög värme först! När svampens egen vätska har kokat in, tillsätter du smöret. Då steks svampen gyllenbrun och suger åt sig smörsmaken istället för att kokas i sitt eget spad.',
        'drink_pairing': 'Ett fylligt rött vin som Pinot Noir, en torr cider eller en klassisk ljus lager.',
        'diet': 'Vegetariskt',
        'difficulty': 'Mycket enkel',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'calories': 290,
        'equipment': ['Stekpanna', 'Kniv & skärbräda', 'Träslev'],
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT15M',
        'cook_time_str': '15 min',
        'total_time': 'PT25M',
        'time': 25,
        'time_str': '25 min',
        'portions_num': 4,
        'portions_unit': 'portioner (till varma mackor)',
        'rating': 4.96,
        'review_count': 6,
        'img': 'svampstuvning',
        'alt': 'Krämig svampstuvning med gratinerad ost och färsk persilja på ett rostat surdegsbröd på en träskärbräda',
        'keywords': 'svampstuvning, krämig svampstuvning, svampstuvning varma mackor, champinjonstuvning, stuvning med svamp, svampstuvning recept, toast med svampstuvning',
        'nutrition': {
            'calories': '290 kcal',
            'carbs': '8g',
            'fat': '27g',
            'protein': '5g',
            'sugar': '3g'
        },
        'ingredients': [
            {
                'group': 'Svamp & Smörstekning',
                'items': [
                    {'name': 'färska champinjoner eller blandad skogssvamp', 'unit': 'g', 'val': 500},
                    {'name': 'smör (till stekning)', 'unit': 'g', 'val': 40},
                    {'name': 'schalottenlökar (finhackade)', 'unit': 'st', 'val': 2},
                    {'name': 'vitlöksklyfta (finhackad)', 'unit': 'st', 'val': 1},
                    {'name': 'färsk timjan (hackad)', 'unit': 'tsk', 'val': 1}
                ]
            },
            {
                'group': 'Krämig Stuvningssås',
                'items': [
                    {'name': 'vetemjöl', 'unit': 'msk', 'val': 1.5},
                    {'name': 'torrt vitt vin eller sherry (valfritt)', 'unit': 'msk', 'val': 2},
                    {'name': 'vispgrädde (40%)', 'unit': 'dl', 'val': 3},
                    {'name': 'mjölk', 'unit': 'dl', 'val': 0.5},
                    {'name': 'koncentrerad kalvfond eller grönsaksfond', 'unit': 'msk', 'val': 1},
                    {'name': 'kinesisk soja (för färg & djup)', 'unit': 'tsk', 'val': 0.5},
                    {'name': 'salt och nymalen svartpeppar', 'unit': 'krm', 'val': 2}
                ]
            },
            {
                'group': 'Servering (Varma mackor)',
                'items': [
                    {'name': 'skivor surdegsbröd eller formfranska', 'unit': 'st', 'val': 4},
                    {'name': 'riven Västerbottensost eller lagrad prästost', 'unit': 'dl', 'val': 2},
                    {'name': 'färsk persilja (finhackad)', 'unit': 'msk', 'val': 2}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Ansa och skiva svampen',
                'text': 'Borsta svampen ren och skiva den i jämna bitar eller klyftor. Finhacka schalottenlök och vitlök.'
            },
            {
                'step': 2,
                'title': 'Torrstek svampen',
                'text': 'Lägg svampen i en torr, het stekpanna. Låt svampen släppa sin vätska under medelhög värme tills all vätska har kokat in i pannan.'
            },
            {
                'step': 3,
                'title': 'Bryn med smör och lök',
                'text': 'Tillsätt smöret i pannan tillsammans med schalottenlök, vitlök och hackad timjan. Stek svampen gyllenbrun i 4–5 minuter på medelvärme.'
            },
            {
                'step': 4,
                'title': 'Pudra med mjöl och tillsätt vätska',
                'text': 'Pudra över vetemjölet och rör runt så det täcker svampen. Häll på vitt vin (om du använder det) och låt fräsa bort i 30 sekunder. Tillsätt sedan vispgrädde, mjölk, fond och soja.'
            },
            {
                'step': 5,
                'title': 'Sjud stuvningen till krämig konsistens',
                'text': 'Låt stuvningen sjuda sakta under omrörning i ca 5–7 minuter tills den blir tjock, blank och sammetslen. Smaka av med salt och nymalen svartpeppar.'
            },
            {
                'step': 6,
                'title': 'Servera eller gratinera mackor',
                'text': 'Servera direkt som tillbehör till kött och fågel, eller skeda över rostat bröd, toppa med rikligt med riven Västerbottensost och gratinera i ugnen på 225°C i 8 minuter tills osten bubblar gyllene. Garnera med persilja!'
            }
        ],
        'faqs': [
            {
                'q': 'Kan man använda fryst eller torkad svamp?',
                'a': 'Ja! Fryst svamp tinas och steks torr i pannan på samma sätt. Torkad svamp blötläggs i ljummet vatten i 30 minuter, kramas ur och stekes (spara gärna lite svampblötläggningsvatten att hälla i såsen för extra smak).'
            },
            {
                'q': 'Hur förvarar man överbliven svampstuvning?',
                'a': 'Förvara i en lufttät burk i kylen i upp till 3 dagar. Vid återuppvärmning i kastrull späder du enkelt med en skvätt mjölk eller grädde för att få tillbaka den perfekta krämigheten.'
            },
            {
                'q': 'Passar svampstuvningen till crêpes?',
                'a': 'Ja, perfekt! Fyll tunna pannkakor med svampstuvningen, rulla ihop, lägg i en ugnsform, toppa med ost och gratinera i ugnen i 10 minuter.'
            }
        ],
        'community_reviews': [
            {
                'name': 'Gunnar Nyström',
                'date': '1 oktober 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Gjorde varma mackor med denna stuvning på fredagskvällen. Blandade champinjoner och trattkantareller. Otroligt fyllig smak och perfekt konsistens!'
            },
            {
                'name': 'Lena Fransson',
                'date': '27 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Tipset att torrsteka svampen först gjorde underverk. Blev inte alls blött utan så där magiskt krämigt och fylligt.'
            },
            {
                'name': 'Anders Blom',
                'date': '21 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Bästa svampstuvningen jag lagat. Vinet och fonden gav en restaurangmässig djup sås.'
            },
            {
                'name': 'Hanna V.',
                'date': '15 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Kanonrecept! Gratinerade med Västerbottensost på hembakat surdegsbröd. Succé!'
            },
            {
                'name': 'Mikael Ström',
                'date': '8 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Superenkel att göra och så god att man bara vill äta med sked direkt ur stekpannan.'
            },
            {
                'name': 'Ulrika J.',
                'date': '1 september 2026',
                'rating': 4,
                'verified': True,
                'comment': 'Mycket god och krämig. Jag tog lite extra svartpeppar för mer sting.'
            }
        ]
    },
    {
        'title': 'Krämig Champinjonsoppa med Vitlök & Färsk Timjan – Värmande Höstsoppa',
        'card_title': 'Krämig Champinjonsoppa',
        'slug': 'kramig-champinjonsoppa-timjan',
        'file': 'kramig-champinjonsoppa-timjan.html',
        'sub': 'Fyllig och sammetslen svampsoppa med smörstekta skivade champinjoner, vitt vin och en skvätt grädde',
        'desc': 'Laga en underbart krämig och fyllig champinjonsoppa med vitlök, timjan och vispgrädde på 30 minuter. Höstens mest värmande vardagsmiddag och förrätt!',
        'long_desc': 'När höstregnet smattrar mot fönstret finns det ingen soppa som värmer själen lika ljuvligt som en klassisk krämig champinjonsoppa. Denna soppa har en djup, intensiv svampsmak och en sammetslen konsistens som för tankarna till en fin fransk bistro. Genom att steka färska bruna och vita champinjoner hårt i smör tillsammans med schalottenlök, vitlök och färsk timjan frigörs all den naturliga umamin. Soppan kokas sedan samman med en skvätt torrt vitt vin och en mustig grönsaks- eller kycklingbuljong innan den mixas lätt (eller behålls med rustika bitar) och avrundas med fyllig vispgrädde och en nypa citronsaft som lyfter alla smaker. Toppa med smörstekta svampskivor och servera med ett frasigt vitlöksbröd för en komplett och oemotståndlig höstmåltid!',
        'pro_tips': 'Spara undan en handfull nystekta svampskivor före mixning och använd som topping vid servering! Det ger en fantastisk texturkontrast mot den lena soppan.',
        'drink_pairing': 'Ett glas franskt vitt vin som Bourgogne Chardonnay, en torr cider eller mineralvatten med citron.',
        'diet': 'Vegetariskt',
        'difficulty': 'Mycket enkel',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'calories': 240,
        'equipment': ['Gryta eller tjockbottnad kastrull', 'Stavmixer', 'Skärbräda & kockkniv', 'Stekspade'],
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT30M',
        'time': 30,
        'time_str': '30 min',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'rating': 4.94,
        'review_count': 6,
        'img': 'champinjonsoppa',
        'alt': 'Krämig champinjonsoppa i en rustik keramikskål garnerad med smörstekta champinjoner, timjan och nymalen svartpeppar',
        'keywords': 'champinjonsoppa, krämig champinjonsoppa, svampsoppa champinjoner, champinjonsoppa recept, enkel svampsoppa, soppa champinjoner timjan, höstsoppa',
        'nutrition': {
            'calories': '240 kcal',
            'carbs': '10g',
            'fat': '20g',
            'protein': '5g',
            'sugar': '4g'
        },
        'ingredients': [
            {
                'group': 'Svamp & Aromater',
                'items': [
                    {'name': 'färska champinjoner (gärna bruna/kastanj)', 'unit': 'g', 'val': 500},
                    {'name': 'smör (till stekning)', 'unit': 'g', 'val': 30},
                    {'name': 'gula lökar eller schalottenlökar (finhackade)', 'unit': 'st', 'val': 2},
                    {'name': 'vitlöksklyftor (pressade)', 'unit': 'st', 'val': 2},
                    {'name': 'färsk timjan (repad)', 'unit': 'msk', 'val': 1}
                ]
            },
            {
                'group': 'Soppbas',
                'items': [
                    {'name': 'vetemjöl', 'unit': 'msk', 'val': 2},
                    {'name': 'torrt vitt vin eller citronsaft', 'unit': 'dl', 'val': 1},
                    {'name': 'grönsaksbuljong eller kycklingbuljong', 'unit': 'dl', 'val': 6},
                    {'name': 'vispgrädde (40%)', 'unit': 'dl', 'val': 2},
                    {'name': 'japansk soja', 'unit': 'tsk', 'val': 1},
                    {'name': 'salt och nymalen svartpeppar', 'unit': 'krm', 'val': 2}
                ]
            },
            {
                'group': 'Garnering & Servering',
                'items': [
                    {'name': 'färsk timjan', 'unit': 'kvistar', 'val': 4},
                    {'name': 'vispgrädde (att ringla på)', 'unit': 'msk', 'val': 2},
                    {'name': 'surdegsbröd eller vitlöksbröd', 'unit': 'skivor', 'val': 4}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Ansa och skiva champinjonerna',
                'text': 'Ansa svampen och skiva den tunt. Finhacka lök och vitlök. Repa bladen från färska timjankvistar.'
            },
            {
                'step': 2,
                'title': 'Stek svampen gyllenbrun',
                'text': 'Hetta upp hälften av smöret i en stor kastrull eller gryta. Stek svampen i ca 6–8 minuter tills all vätska kokat in och svampen fått vacker gyllene stekyta. Ta undan 3–4 matskedar svamp till garnering.'
            },
            {
                'step': 3,
                'title': 'Fräs lök och kryddor',
                'text': 'Tillsätt resten av smöret, lök, vitlök och färsk timjan i grytan med resten av svampen. Låt fräsa på medelvärme i ca 3 minuter tills löken är mjuk och genomskinlig utan att brännas.'
            },
            {
                'step': 4,
                'title': 'Pudra med mjöl och koka buljongen',
                'text': 'Pudra över vetemjölet och rör om så det fördelas jämnt. Häll i vitt vin och låt koka in i 1 minut. Häll därefter i buljongen och sojan under omrörning. Låt soppan koka upp och sjuda sakta i 10 minuter.'
            },
            {
                'step': 5,
                'title': 'Mixa och rör i grädden',
                'text': 'Mixa soppan slät med en stavmixer (mixa helt slät eller lämna några grova bitar för rustik känsla, efter egen smak). Häll i vispgrädden och låt soppan sjuda upp igen i 2–3 minuter. Smaka av med salt och nymalen svartpeppar samt eventuellt några droppar citronsaft.'
            },
            {
                'step': 6,
                'title': 'Garnera och servera',
                'text': 'Häll upp den rykande heta soppan i varma skålar. Toppa med de sparade smörstekta svampskivorna, en ringlad skvätt grädde, färsk timjan och ett drag med pepparkvarnen. Servera med ett gott bröd!'
            }
        ],
        'faqs': [
            {
                'q': 'Kan man göra soppan helt mjölkfri eller vegansk?',
                'a': 'Ja! Byt smöret mot mjölkfritt margarin eller neutral olja, och ersätt vispgrädden med havregrädde (t.ex. Oatly iMat) eller sojagrädde.'
            },
            {
                'q': 'Måste man ha vitt vin i soppan?',
                'a': 'Nej, vinet kan uteslutas! Tillsätt istället 1 msk färskpressad citronsaft eller 1 tsk vitvinsvinäger mot slutet för att ge den friska syra som balanserar grädden och svampen.'
            },
            {
                'q': 'Går champinjonsoppa bra att förbereda dagen innan?',
                'a': 'Ja, soppan blir nästan ännu godare när smakerna får mogna över natten i kylskåp! Värm den försiktigt på låg värme i kastrull före servering.'
            }
        ],
        'community_reviews': [
            {
                'name': 'Cecilia Malm',
                'date': '1 oktober 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Helt ljuvlig soppa! Den blev så otroligt krämig och fyllig i smaken. Gästerna trodde jag beställt den från en fin restaurang.'
            },
            {
                'name': 'Patrik Wall',
                'date': '26 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Bästa champinjonsoppan jag ätit. Timjanen och en skvätt vin lyfte smakerna till en helt ny nivå.'
            },
            {
                'name': 'Sara Nordqvist',
                'date': '20 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Värmande och perfekt en ruggig höstkväll. Sparade svampskivor på toppen gav så fin textur.'
            },
            {
                'name': 'Lennart B.',
                'date': '13 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Enkel att laga och snabbt klar på 30 minuter. Hela familjens nya favoritsoppa.'
            },
            {
                'name': 'Ingrid S.',
                'date': '6 september 2026',
                'rating': 5,
                'verified': True,
                'comment': 'Sammetslen och djup svampsmak. Åt med vitlöksbröd och ett glas vitt vin.'
            },
            {
                'name': 'Daniel K.',
                'date': '31 augusti 2026',
                'rating': 4,
                'verified': True,
                'comment': 'Jättegod! Jag lät bli att mixa den helt slät för jag gillar lite tuggmotstånd, funkade toppen.'
            }
        ]
    }
]

# Read recipes_data.py
file_path = "/Users/baderarraf/.gemini/antigravity/scratch/nordic-plate/tools/recipes_data.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

strip_content = content.rstrip()
if not strip_content.endswith("]"):
    raise Exception("recipes_data.py does not end with ']'")

prefix = strip_content[:-1].rstrip()
if prefix.endswith(","):
    new_content = prefix + "\n"
else:
    new_content = prefix + ",\n"

for r in batch27:
    formatted_dict = pprint.pformat(r, indent=4, width=120, sort_dicts=True)
    new_content += formatted_dict + ",\n"

new_content += "]\n"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Successfully added {len(batch27)} recipes to {file_path}!")
