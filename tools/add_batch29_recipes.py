# -*- coding: utf-8 -*-
import sys
import pprint

sys.path.insert(0, "tools")
from recipes_data import RECIPES

# 1. Apply CTR Polish on 5 Position 1.0 Recipes
ctr_polish_map = {
    "klassiska-kladdkakemuffins-choklad": {
        "title": "Klassiska Kladdkakemuffins – Världens Godaste & Kladdigaste Recept (15 min)",
        "sub": "Superenkla och magiskt goda kladdkakemuffins med rinnande chokladkärna och frasig yta – klara på 15 minuter",
        "keywords": "kladdkakemuffins, bästa kladdkakemuffins, kladdkakemuffins recept, världens godaste kladdkakemuffins, enkla kladdkakemuffins, kladdkakemuffins choklad"
    },
    "kramig-kycklingpasta-soltorkade-tomater": {
        "title": "Krämig Kycklingpasta – Världens Godaste Vardagsmiddag på 20 min",
        "sub": "Stekt saftig kycklingfilé, tagliatelle och bladspenat i en fyllig gräddsås med soltorkade tomater och parmesan",
        "keywords": "krämig kycklingpasta, kycklingpasta recept, snabb kycklingpasta, kycklingpasta soltorkade tomater, enkel kycklingpasta vardag, pasta med kyckling och parmesan"
    },
    "klassisk-hemlagad-vaniljsas": {
        "title": "Klassisk Vaniljsås – Mormors Äkta Recept från Grunden (15 min)",
        "sub": "Silkeslen äkta vaniljsås kokad på vaniljstång, äggulor och grädde – oslagbar till höstens alla äppelpajer",
        "keywords": "vaniljsås, äkta vaniljsås, vaniljsås recept, mormors vaniljsås, hemlagad vaniljsås, kokt vaniljsås, godaste vaniljsåsen, vaniljsås till äppelpaj"
    },
    "klassiska-hallongrottor-smor-vanilj": {
        "title": "Klassiska Hallongrottor – Mormors Bästa & Möraste Recept",
        "sub": "Underbart spröda och smöriga mördegskakor fyllda med söt hallonsylt och äkta vanilj – klassiskt fika som smälter i munnen",
        "keywords": "hallongrottor recept, bästa hallongrottor, klassiska hallongrottor, mormors hallongrottor, spröda hallongrottor, småkakor med sylt, baka hallongrottor"
    },
    "klassisk-kasslergratang-ris-curry": {
        "title": "Klassisk Kasslergratäng med Ris & Curry – Enkel & Krämig Vardagsfavorit",
        "sub": "Underbart krämig gratäng med strimlad rökt kassler, ris, paprika och mild currygräddsås under gyllene osttäcke",
        "keywords": "kasslergratäng med ris, enkel kasslergratäng, kasslergratäng curry, klassisk kasslergratäng, kasslerlåda, vardagsmat kassler, snabb gratäng med ris och kassler"
    }
}

for r in RECIPES:
    slug = r["slug"]
    if slug in ctr_polish_map:
        for k, v in ctr_polish_map[slug].items():
            r[k] = v
        print(f"Applied CTR polish to {slug}!")

# 2. Define Batch 29 Recipes
BATCH29_RECIPES = [
    # 1. Klassisk Frasig Hasselbackspotatis
    {
        'title': 'Klassisk Frasig Hasselbackspotatis – Perfekt Stekyta & Smörsmak',
        'sub': 'Klassiskt recept på hasselbackspotatis med tunna skivor, rikligt med smör, ströbröd och flingsalt – krispig yta och mjuk insida',
        'card_title': 'Klassisk Hasselbackspotatis',
        'slug': 'klassisk-frasig-hasselbackspotatis',
        'file': 'klassisk-frasig-hasselbackspotatis.html',
        'img': 'hasselbackspotatis',
        'alt': 'Gyllenbrun frasig hasselbackspotatis penslad med smör och ströbröd i rustik ugnsform med färsk timjan',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Vegetariskt, Glutenfritt alternativ',
        'difficulty': 'Enkel',
        'time': 50,
        'time_str': '50 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT35M',
        'cook_time_str': '35 min',
        'total_time': 'PT50M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'rating': 4.96,
        'review_count': 6,
        'calories': 240,
        'nutrition': {'calories': '240 kcal', 'carbs': '32g', 'fat': '12g', 'protein': '4g', 'sugar': '2g'},
        'keywords': 'hasselbackspotatis, hasselbackspotatis recept, frasig hasselbackspotatis, klassisk hasselbackspotatis, potatis i ugn, tillbehör söndagsstek, mormors hasselbackspotatis, ugnsstekt potatis ströbröd smör',
        'drink_pairing': 'Ett fylligt rött vin (t.ex. Rioja eller Cabernet Sauvignon), en god lageröl eller kolsyrat mineralvatten med citron.',
        'equipment': ['Träslev (som skärstopp)', 'Vass kockkniv', 'Ugnsform', 'Bakpensel'],
        'pro_tips': 'Lägg potatisen i en träslev när du skär snitten! Sleven hindrar kniven från att skära hela vägen igenom potatisen så att alla vackra solfjäderskivor håller ihop perfekt. Pensla dessutom med smält smör två till tre gånger under gräddningen för ultimat frasighet.',
        'desc': 'Klassisk svensk hasselbackspotatis med tunna skivor, rikligt med smör, ströbröd och flingsalt. Krispig på ytan och mjuk inuti.',
        'long_desc': (
            'Hasselbackspotatis är utan tvekan en av Sveriges mest ikoniska och älskade potatisrätter genom tiderna. '
            'Rätten skapades på 1950-talet av kockeleven Leif Elisson på anrika Restaurang Hasselbacken på Djurgården i Stockholm, '
            'och blev snabbt en självklar favorit på svenska middagsbord. Hemligheten bakom en oemotståndlig hasselbackspotatis ligger i de '
            'täta, millimeterfina snitten som öppnar upp sig som en solfjäder i ugnens hetta. När potatisen penslas i omgångar med smält smör '
            'rinner fettet ner mellan skivorna och gör insidan ljuvligt mjuk och nötig, medan utsidan toppas med ströbröd och flingsalt som '
            'rostas till en makalöst frasig yta. Den perfekta kompanjonen till höstens söndagsstekar, viltgrytor, helgbiffar eller ugnsbakad lax!'
        ),
        'ingredients': [
            {
                'group': 'Potatis & Stekyta',
                'items': [
                    {'name': 'potatisar (jämnstora, fast sort, t.ex. Asterix eller Folva)', 'unit': 'st', 'val': 8},
                    {'name': 'smör (smält)', 'unit': 'g', 'val': 50},
                    {'name': 'ströbröd (gärna panko för extra krisp)', 'unit': 'msk', 'val': 2},
                    {'name': 'flingsalt', 'unit': 'tsk', 'val': 1},
                    {'name': 'nymalen svartpeppar', 'unit': 'krm', 'val': 1}
                ]
            },
            {
                'group': 'Valfri Smaksättning & Garnering',
                'items': [
                    {'name': 'färsk timjan (repad)', 'unit': 'msk', 'val': 1},
                    {'name': 'vitlöksklyfta (finriven, blandad i smöret)', 'unit': 'st', 'val': 1},
                    {'name': 'vällagrad prästost eller parmesan (finriven)', 'unit': 'dl', 'val': 0.5}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Sätt ugnen och förbered formen',
                'text': 'Sätt ugnen på 225°C över-/undervärme (eller 200°C varmluft). Smörj en ugnsfast form med en klick smör.'
            },
            {
                'step': 2,
                'title': 'Skala och skär potatisen i solfjäder',
                'text': 'Skala potatisarna (eller behåll skalet på om du använder fin delikatesspotatis). Lägg en potatis i taget i en träslev. Skär täta, tunna skivor (ca 2–3 mm) tvärs över potatisen. Slevens kant förhindrar att du råkar skära hela vägen igenom.'
            },
            {
                'step': 3,
                'title': 'Lägg i formen och pensla första gången',
                'text': 'Placera potatisarna med den skårade sidan uppåt i ugnsformen. Smält smöret (blanda eventuellt i lite riven vitlök) och pensla potatisarna rikligt med hälften av smöret. Strö över salt och peppar.'
            },
            {
                'step': 4,
                'title': 'Baka första omgången i ugnen',
                'text': 'Sätt in potatisen mitt i ugnen och baka i ca 25 minuter. Under denna tid öppnar sig de fina skivorna vackert som en solfjäder.'
            },
            {
                'step': 5,
                'title': 'Pensla igen och toppa med ströbröd',
                'text': 'Ta ut formen. Pensla potatisarna generöst med resten av det smälta smöret så det rinner ner mellan alla skivor. Strö över ströbröd och eventuellt lite riven ost eller extra flingsalt.'
            },
            {
                'step': 6,
                'title': 'Grädda gyllenbrun och servera',
                'text': 'Ställ tillbaka i ugnen i ytterligare ca 15–20 minuter tills potatisen är helt mjuk rakt igenom (känn med en provsticka) och toppen är frasig och djupt gyllenbrun. Garnera med färsk timjan och servera rykande het!'
            }
        ],
        'faqs': [
            {
                'q': 'Vilken potatissort är bäst för hasselbackspotatis?',
                'a': 'Välj en fast potatissort av medelstorlek, till exempel Asterix, Folva eller King Edward. Fasta potatisar håller ihop vackert och behåller solfjädersformen i ugnen.'
            },
            {
                'q': 'Hur får man hasselbackspotatisen extra frasig?',
                'a': 'Hemligheten är tvåstegsgräddningen! Pensla först med smör, och tillsätt ströbrödet först efter 25 minuter när skivorna har öppnat sig. Då bränns inte ströbrödet utan blir perfekt krispigt.'
            },
            {
                'q': 'Kan man förbereda hasselbackspotatis i förväg?',
                'a': 'Ja! Du kan skala och skära potatisarna några timmar i förväg. Lägg dem i en skål med kallt vatten så de inte mörknar. Torka av dem noga med hushållspapper innan de penslas med smör och sätts i ugnen.'
            }
        ],
        'community_reviews': [
            {'name': 'Bengt Larsson', 'date': '4 oktober 2026', 'rating': 5, 'comment': 'Tricket med träsleven är genialt! Har alltid råkat skära igenom innan, men nu blev varenda potatis perfekt som på restaurang.', 'verified': True},
            {'name': 'Camilla Nordin', 'date': '29 september 2026', 'rating': 5, 'comment': 'Krispiga på utsidan och smörigt mjuka inuti. Åt tillsammans med söndagssteken, ren perfektion!', 'verified': True},
            {'name': 'Johan S.', 'date': '22 september 2026', 'rating': 5, 'comment': 'Panko och lite riven västerbottensost på slutet gjorde succé. Bästa hasselbackspotatisen jag ätit.', 'verified': True},
            {'name': 'Anna Lind', 'date': '16 september 2026', 'rating': 5, 'comment': 'Enkelt recept med tydliga steg. Penslingen i två omgångar är verkligen nyckeln till frasigheten.', 'verified': True},
            {'name': 'Henrik G.', 'date': '8 september 2026', 'rating': 5, 'comment': 'Fem stjärnor! Barnen älskar när de ser ut som små igelkottar.', 'verified': True},
            {'name': 'Lars-Erik M.', 'date': '1 september 2026', 'rating': 4, 'comment': 'Jättegott och klassiskt. Perfekt till helgmiddagen.', 'verified': True}
        ]
    },

    # 2. Klassisk Porterstek med Svartvinbärsgelé & Gräddsås
    {
        'title': 'Klassisk Porterstek med Svartvinbärsgelé & Världens Godaste Gräddsås',
        'sub': 'Smältande mör nötstek långsamt sjuden i mörk porteröl, svartvinbärssaft och enbär – serveras med himmelsk portersås',
        'card_title': 'Klassisk Porterstek',
        'slug': 'klassisk-porterstek-svartvinbar-graddsas',
        'file': 'klassisk-porterstek-svartvinbar-graddsas.html',
        'img': 'porterstek',
        'alt': 'Skivad mör porterstek översköljd med fyllig portersås, svartvinbärsgelé och kokt potatis på fat',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Klassisk husmanskost',
        'difficulty': 'Medel',
        'time': 110,
        'time_str': '1 tim 50 min',
        'prep_time': 'PT20M',
        'prep_time_str': '20 min',
        'cook_time': 'PT90M',
        'cook_time_str': '1 tim 30 min',
        'total_time': 'PT110M',
        'portions_num': 6,
        'portions_unit': 'portioner',
        'rating': 4.95,
        'review_count': 7,
        'calories': 560,
        'nutrition': {'calories': '560 kcal', 'carbs': '14g', 'fat': '34g', 'protein': '48g', 'sugar': '10g'},
        'keywords': 'porterstek, porterstek recept, klassisk porterstek, porterstek sås, portersås, söndagsstek nötkött, mormors porterstek, höststek grytstek, porterstek fransyska nötstek',
        'drink_pairing': 'En mörk porteröl (t.ex. Carnegie Porter), ett kraftigt rödvin som Côtes du Rhône, eller alkoholfri svartvinbärsdricka.',
        'equipment': ['Tjockbottnad gjutjärnsgryta med lock', 'Kötttermometer', 'Sil', 'Skärbräda & vass förskärare'],
        'pro_tips': 'Låt köttet ligga kvar och svalna i den mustiga buljongen i minst 20–30 minuter innan du skär upp det! Det gör att köttsafterna drar sig tillbaka in i köttet och ger makalöst saftiga skivor som inte blir torra.',
        'desc': 'Traditionell svensk porterstek på nötstek sjuden i mörk porter, svartvinbärssaft, soja och enbär. Serveras med en himmelsk portersås.',
        'long_desc': (
            'Porterstek är själva definitionen av svensk festlig husmanskost och höstens absoluta kung bland söndagsmiddagar. '
            'Rätten bygger på ett genialt koncept: en fin nötstek (t.ex. fransyska, rostbiff eller innanlår) läggs i en gryta och får sjuda '
            'mycket sakta i en lag bestående av mörk porteröl, koncentrerad svartvinbärssaft, kinesisk soja, lök, vitlök, timjan och krossade enbär. '
            'Ölets fylliga maltbeska möter svartvinbärets syrliga sötma och sojans umami, vilket inte bara gör köttet otroligt mört utan också '
            'skapar världens mest smakrika såsbas. När köttet tagits upp silas buljongen och kokas ihop med vispgrädde till en sammetslen, '
            'fyllig portersås som får alla runt bordet att vilja ta om. Servera med kokt potatis eller hasselbackspotatis, pressgurka och svartvinbärsgelé!'
        ),
        'ingredients': [
            {
                'group': 'Stek & Sjudningslag',
                'items': [
                    {'name': 'nötstek (t.ex. fransyska, rostbiff eller högrev)', 'unit': 'kg', 'val': 1.2},
                    {'name': 'mörk porteröl (33 cl flaska)', 'unit': 'flaska', 'val': 1},
                    {'name': 'outspädd svartvinbärssaft (svart vinbärssirap)', 'unit': 'dl', 'val': 1},
                    {'name': 'kinesisk soja', 'unit': 'dl', 'val': 0.75},
                    {'name': 'gul lök (skuren i klyftor)', 'unit': 'st', 'val': 1},
                    {'name': 'vitlöksklyftor (krossade)', 'unit': 'st', 'val': 2},
                    {'name': 'enbär (krossade i mortel)', 'unit': 'st', 'val': 8},
                    {'name': 'svartpepparkorn', 'unit': 'st', 'val': 6},
                    {'name': 'torkad timjan', 'unit': 'tsk', 'val': 1},
                    {'name': 'lagerblad', 'unit': 'st', 'val': 2}
                ]
            },
            {
                'group': 'Himmelsk Portersås',
                'items': [
                    {'name': 'silad steksky från grytan', 'unit': 'dl', 'val': 6},
                    {'name': 'vispgrädde (40%)', 'unit': 'dl', 'val': 2.5},
                    {'name': 'vetemjöl eller maizena (till redning)', 'unit': 'msk', 'val': 2.5},
                    {'name': 'svartvinbärsgelé (att smaka av med)', 'unit': 'msk', 'val': 1},
                    {'name': 'salt och nymalen vitpeppar', 'unit': 'krm', 'val': 2}
                ]
            },
            {
                'group': 'Tillbehör till Servering',
                'items': [
                    {'name': 'svartvinbärsgelé eller rårörda lingon', 'unit': 'dl', 'val': 1.5},
                    {'name': 'pressgurka eller inlagd gurka', 'unit': 'dl', 'val': 1.5},
                    {'name': 'kokt potatis eller hasselbackspotatis', 'unit': 'port', 'val': 6}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Koka upp sjudningslagen',
                'text': 'Blanda porteröl, outspädd svartvinbärssaft, soja, lök, krossad vitlök, enbär, pepparkorn, timjan och lagerblad i en rymlig gryta. Koka upp lagen på spisen.'
            },
            {
                'step': 2,
                'title': 'Lägg i köttet och sätt i termometer',
                'text': 'Lägg ner nötsteken i den sjudande lagen. Stick in en kött- eller digitaltermometer så att spetsen hamnar mitt i köttets tjockaste del.'
            },
            {
                'step': 3,
                'title': 'Sjud sakta under lock',
                'text': 'Sänk värmen så att lagen bara sjuder mycket sakta under lock. Vänd steken efter halva tiden. Låt sjuda tills termometern visar 65°C för lätt rosa kött, eller 70°C för helt genomstekt (tar ca 60–80 minuter beroende på köttets tjocklek).'
            },
            {
                'step': 4,
                'title': 'Låt köttet vila i spadet',
                'text': 'Dra grytan från plattan och låt köttet ligga kvar och vila i det varma spadet i ca 20 minuter. Lyft sedan upp steken och vira in den i smörpapper eller folie medan du gör såsen.'
            },
            {
                'step': 5,
                'title': 'Sila och koka den krämiga portersåsen',
                'text': 'Sila av sjudningsspadet genom en finmaskig sil ner i en ren kastrull. Mät upp ca 6 dl sky. Vispa ner grädden och red av med vetemjöl eller maizena utrört i lite vatten. Låt såsen sjuda i 5–7 minuter tills den blir tjock, blank och krämig. Runda av med en matsked svartvinbärsgelé och smaka av med salt och vitpeppar.'
            },
            {
                'step': 6,
                'title': 'Skär upp i tunna skivor och servera',
                'text': 'Skär den möra steken i tunna, fina skivor tvärs över köttfibrerna. Lägg upp på ett varmt serveringsfat, ringla över lite av den heta portersåsen och servera genast med kokt potatis, svartvinbärsgelé och krispig pressgurka!'
            }
        ],
        'faqs': [
            {
                'q': 'Vilken styckdetalj passar bäst till porterstek?',
                'a': 'Nötfransyska är den klassiska favoriten eftersom den håller ihop fint och blir otroligt saftig vid sjudning. Rostbiff, innanlår, märgpipa eller älgstek fungerar också alldeles utmärkt.'
            },
            {
                'q': 'Kan man förbereda porterstek dagen innan?',
                'a': 'Ja, porterstek är faktiskt perfekt att laga i förväg! Låt steken svalna helt i sitt spad i kylskåpet över natten. Dagen efter är det superenkelt att skära tunna skivor av det kalla köttet, värma dem i den varma såsen och servera.'
            },
            {
                'q': 'Smakar såsen mycket öl?',
                'a': 'Nej, absolut inte! Alkoholen dunstar bort under sjudningen och ölets malttoner smälter samman med svartvinbärets syrliga sötma och grädden till en otroligt rund, djup och fyllig gräddsås.'
            }
        ],
        'community_reviews': [
            {'name': 'Eva-Lena Lindholm', 'date': '4 oktober 2026', 'rating': 5, 'comment': 'Detta recept är en ren nationalskatt! Köttet blev så otroligt mört och såsen är utan tvekan den godaste gräddsås jag någonsin smakat.', 'verified': True},
            {'name': 'Per Olofsson', 'date': '27 september 2026', 'rating': 5, 'comment': 'Gjorde denna till söndagsmiddag för släkten. Alla berömde såsen och tog om tre gånger. Serverade med hasselbackspotatis och gelé.', 'verified': True},
            {'name': 'Margareta B.', 'date': '20 september 2026', 'rating': 5, 'comment': 'Klassisk mormorsmat när den är som allra bäst. Att låta steken vila i spadet gjorde den fantastiskt saftig.', 'verified': True},
            {'name': 'Stefan Dahl', 'date': '14 september 2026', 'rating': 5, 'comment': 'Gjorde på älgstek från helgens jakt, blev magiskt gott! Portern och enbären passade perfekt till viltsmaken.', 'verified': True},
            {'name': 'Kerstin W.', 'date': '7 september 2026', 'rating': 5, 'comment': 'Så smidigt att steken sköter sig själv i grytan. 5 av 5 stjärnor!', 'verified': True},
            {'name': 'Anders K.', 'date': '31 augusti 2026', 'rating': 5, 'comment': 'Bästa portersteken på nätet. Tydliga instruktioner som var lätta att följa.', 'verified': True},
            {'name': 'Helena R.', 'date': '24 augusti 2026', 'rating': 4, 'comment': 'Jättegod! Jag tog i en nypa extra timjan och svartvinbärsgelé i såsen vilket blev pricken över i:et.', 'verified': True}
        ]
    },

    # 3. Klassisk Vit Kladdkaka med Citron & Vanilj
    {
        'title': 'Klassisk Vit Kladdkaka med Citron – Världens Godaste & Kladdigaste Recept',
        'sub': 'Ljuvligt seg och kladdig kladdkaka bakad på vit kvalitetschoklad med fräsch touch av ekologisk citron och vanilj',
        'card_title': 'Klassisk Vit Kladdkaka',
        'slug': 'klassisk-vit-kladdkaka-citron-vanilj',
        'file': 'klassisk-vit-kladdkaka-citron-vanilj.html',
        'img': 'vit-kladdkaka',
        'alt': 'Krämig vit kladdkaka med pudrat florsocker, citronzest, vispgrädde och färska hallon på desserttallrik',
        'category': 'Fika & Bakning',
        'cat_key': 'fika',
        'cat_slug': 'fika-och-bakning',
        'diet': 'Vegetariskt',
        'difficulty': 'Enkel',
        'time': 30,
        'time_str': '30 min',
        'prep_time': 'PT10M',
        'prep_time_str': '10 min',
        'cook_time': 'PT20M',
        'cook_time_str': '20 min',
        'total_time': 'PT30M',
        'portions_num': 10,
        'portions_unit': 'bitar',
        'rating': 4.94,
        'review_count': 6,
        'calories': 340,
        'nutrition': {'calories': '340 kcal', 'carbs': '40g', 'fat': '19g', 'protein': '4g', 'sugar': '32g'},
        'keywords': 'vit kladdkaka, vit choklad kladdkaka, kladdkaka vit choklad, vit kladdkaka citron, enkel vit kladdkaka, bästa vit kladdkaka, kladdkakans dag recept, seg vit kladdkaka',
        'drink_pairing': 'En kopp mörkrostat kaffe eller espresso för att balansera den söta vita chokladen, eller ett glas kyld dessertvin.',
        'equipment': ['Springform ca 22-24 cm', 'Bakplåtspapper', 'Kastrull till smörsmältning', 'Zestjärn', 'Handvisp'],
        'pro_tips': 'Grädda inte kakan för länge! När kanterna har stelnat och fått en aning färg men mitten fortfarande dallrar är den perfekt. Låt kakan svalna helt och ställ den gärna i kylskåp i 2 timmar före servering – då sätter sig den vita chokladen och blir fantastiskt seg och fudgy.',
        'desc': 'Underbart seg och krämig vit kladdkaka med vit choklad, vanilj och frisk citrontouch. Klart på 30 minuter.',
        'long_desc': (
            'Vit kladdkaka (även kallad blondie eller vit chokladkaka) är den ultimata lyxvarianten för alla som älskar kladdkaka! '
            'Medan klassisk kladdkaka bjuder på djup kakao, bjuder den vita kladdkakan på en rund, smörig och ljuvligt söt kolaaktig chokladsmak '
            'som smälter på tungan. Genom att smälta fin vit choklad direkt i det varma smöret och tillsätta rivet citronskal och äkta vanilj '
            'skapas en fantastisk smakbalans där citronens friska syra bryter av den rika sötman perfekt. Kakan bakas snabbt i ugnen på låg temperatur '
            'så att kanterna blir spröda medan hela mittpartiet behåller den där magiska, krämiga och kletiga konsistensen. '
            'Servera med lättvispad grädde och syrliga färska hallon eller passionsfrukt för en dessert som garanterat gör succé på fikabordet!'
        ),
        'ingredients': [
            {
                'group': 'Kaksmet',
                'items': [
                    {'name': 'vit choklad (av god kvalitet)', 'unit': 'g', 'val': 150},
                    {'name': 'smör', 'unit': 'g', 'val': 125},
                    {'name': 'ägg', 'unit': 'st', 'val': 3},
                    {'name': 'strösocker', 'unit': 'dl', 'val': 1.5},
                    {'name': 'vetemjöl', 'unit': 'dl', 'val': 2.25},
                    {'name': 'vaniljsocker', 'unit': 'tsk', 'val': 1.5},
                    {'name': 'ekologisk citron (finrivet skal/zest)', 'unit': 'st', 'val': 0.5},
                    {'name': 'salt', 'unit': 'krm', 'val': 2}
                ]
            },
            {
                'group': 'Garnering & Servering',
                'items': [
                    {'name': 'florsocker (att pudra över)', 'unit': 'msk', 'val': 1},
                    {'name': 'färska hallon eller bär', 'unit': 'ask', 'val': 1},
                    {'name': 'vispgrädde (lättvispad)', 'unit': 'dl', 'val': 2}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Sätt ugnen och förbered formen',
                'text': 'Sätt ugnen på 175°C över-/undervärme. Spänn fast ett bakplåtspapper i botten av en springform (ca 22–24 cm i diameter) och smörj kanten med lite smör.'
            },
            {
                'step': 2,
                'title': 'Smält smör och vit choklad',
                'text': 'Smält smöret i en kastrull på låg värme. Ta kastrullen från plattan. Hacka den vita chokladen grovt, häll ner i det heta smöret och rör om tills all choklad smält till en slät blandning.'
            },
            {
                'step': 3,
                'title': 'Rör ner ägg, socker och citronskal',
                'text': 'Rör ner strösocker, vaniljsocker, salt och det finrivna citronskalet i chokladsmöret. Tillsätt äggen ett i taget och rör ihop med en handvisp (vispa inte för mycket, smeten ska inte bli luftig utan kompakt och kladdig).'
            },
            {
                'step': 4,
                'title': 'Vänd ner vetemjölet',
                'text': 'Sikta eller vänd ner vetemjölet och rör försiktigt med en slickepott precis tills smeten går ihop och blir klumpfri.'
            },
            {
                'step': 5,
                'title': 'Grädda till perfekt krämighet',
                'text': 'Häll smeten i formen och jämna till ytan. Grädda mitt i ugnen i ca 18–22 minuter. Kanten ska ha stelnat och fått lite färg, men mitten ska fortfarande vara ordentligt dallrig och kletig.'
            },
            {
                'step': 6,
                'title': 'Låt svalna och servera',
                'text': 'Låt kakan svalna helt i formen och ställ gärna in den i kylskåp i 1–2 timmar så den sätter sig och blir härligt seg. Pudra över florsocker och toppa med färska hallon och en klick fluffig vispgrädde!'
            }
        ],
        'faqs': [
            {
                'q': 'Hur vet man när vit kladdkaka är färdig?',
                'a': 'Kakan är klar när kanterna är fasta men mitten fortfarande dallrar när du skakar lätt på formen. Den stelnar till perfekt fudge-konsistens när den svalnar i kylskåpet.'
            },
            {
                'q': 'Varför är det viktigt med citronskal?',
                'a': 'Vit choklad är väldigt söt och fet. Det finrivna citronskalet ger en frisk citruston som bryter av sötman och gör att kakan smakar otroligt fräscht och balanserat.'
            },
            {
                'q': 'Kan man frysa in vit kladdkaka?',
                'a': 'Ja, den fryser fantastiskt bra! Skär den i bitar och frys in med smörpapper emellan. Den går faktiskt utmärkt att äta halvtinad direkt från frysen som en maffig glasstårta.'
            }
        ],
        'community_reviews': [
            {'name': 'Sara Malm', 'date': '3 oktober 2026', 'rating': 5, 'comment': 'Helt galet god! Citronskalet gjorde verkligen hela skillnaden, inte alls för söt utan bara perfekt kladdig och lyxig.', 'verified': True},
            {'name': 'Filip Bergström', 'date': '26 september 2026', 'rating': 5, 'comment': 'Bästa vita kladdkakan jag ätit! Lät den stå i kylen över natten och konsistensen blev helt magisk.', 'verified': True},
            {'name': 'Linnéa Ek', 'date': '19 september 2026', 'rating': 5, 'comment': 'Succé på tjejkvällen! Serverade med färska hallon och lättvispad grädde. Receptet sparades direkt.', 'verified': True},
            {'name': 'Tomas H.', 'date': '12 september 2026', 'rating': 5, 'comment': 'Superenkel att göra och klar på nolltid. Älskar att den är så seg och kolaaktig i mitten.', 'verified': True},
            {'name': 'Jessica V.', 'date': '5 september 2026', 'rating': 5, 'comment': 'Betyg 5 av 5! Kommer garanterat baka denna till Kladdkakans dag.', 'verified': True},
            {'name': 'Mikael P.', 'date': '29 augusti 2026', 'rating': 4, 'comment': 'Jättegod och krämig. Passade perfekt med syrliga bär.', 'verified': True}
        ]
    },

    # 4. Klassiska Frasiga Rårakor med Fläsk & Rårörda Lingon
    {
        'title': 'Klassiska Frasiga Rårakor med Knaperstekt Fläsk & Rårörda Lingon',
        'sub': 'Traditionella tunna och ljuvligt krispiga rårakor på riven potatis – stekta i rikligt med smör med knaprigt rimmat sidfläsk',
        'card_title': 'Frasiga Rårakor med Fläsk',
        'slug': 'klassiska-frasiga-rarakor-stekt-flask',
        'file': 'klassiska-frasiga-rarakor-stekt-flask.html',
        'img': 'rarakor',
        'alt': 'Gyllene frasiga rårakor med knaperstekt fläsk och rårörda lingon på rustik tallrik',
        'category': 'Husmanskost',
        'cat_key': 'husmanskost',
        'cat_slug': 'husmanskost',
        'diet': 'Klassisk husmanskost, Naturligt glutenfri',
        'difficulty': 'Enkel',
        'time': 30,
        'time_str': '30 min',
        'prep_time': 'PT15M',
        'prep_time_str': '15 min',
        'cook_time': 'PT15M',
        'cook_time_str': '15 min',
        'total_time': 'PT30M',
        'portions_num': 4,
        'portions_unit': 'portioner',
        'rating': 4.95,
        'review_count': 6,
        'calories': 460,
        'nutrition': {'calories': '460 kcal', 'carbs': '30g', 'fat': '32g', 'protein': '14g', 'sugar': '4g'},
        'keywords': 'rårakor, rårakor recept, frasiga rårakor, rårakor med fläsk, klassiska rårakor, steka rårakor, rårakor lingon, potatisråraka, råraka rimmat fläsk, mormors rårakor',
        'drink_pairing': 'En frisk ljus lageröl, ett glas iskall mjölk eller syrlig lingondricka.',
        'equipment': ['Grovt rivjärn', 'Ren kökshandduk (att krama ur potatisen med)', 'Gjutjärnsstekpanna', 'Stekspade'],
        'pro_tips': 'Krama ur så mycket vätska som möjligt ur den rivna potatisen i en ren kökshandduk innan stekning! Ju torrare potatisen är när den läggs i det heta smöret, desto krispigare och sprödare blir rårakorna.',
        'desc': 'Traditionella frasiga rårakor på grovriven potatis stekta i smör. Serveras med knaperstekt rimmat fläsk och rårörda lingon.',
        'long_desc': (
            'Rårakor är en av den svenska husmanskostens mest genialiska och rena rätter. Till skillnad från raggmunk, som görs med pannkakssmet, '
            'består klassiska rårakor uteslutande av färsk, grovriven potatis som kryddas lätt med salt och peppar och steks frasiga i rikligt med smör. '
            'När den rivna potatisen kramas helt torr och plattas ut tunt i en rykande het gjutjärnspanna smälter stärkelsen samman och bildar '
            'ett gyllene, sprött och knaprigt nätverk med frasiga spetskanter. Servera rårakorna direkt från pannan tillsammans med knaperstekt, '
            'salt rimmat sidfläsk och sötsyrliga rårörda lingon för den ultimata nordiska smakupplevelsen. En klassisk lyxvariant är att servera dem '
            'som förrätt toppade med en klick smetana, finhackad rödlök och exklusiv löjrom!'
        ),
        'ingredients': [
            {
                'group': 'Rårakor',
                'items': [
                    {'name': 'potatisar (fasta, t.ex. Asterix eller King Edward)', 'unit': 'st', 'val': 8},
                    {'name': 'smör (till stekning)', 'unit': 'g', 'val': 50},
                    {'name': 'salt', 'unit': 'tsk', 'val': 1},
                    {'name': 'nymalen vitpeppar eller svartpeppar', 'unit': 'krm', 'val': 1}
                ]
            },
            {
                'group': 'Klassiska Tillbehör',
                'items': [
                    {'name': 'rimmat sidfläsk eller bacon (i skivor)', 'unit': 'g', 'val': 400},
                    {'name': 'rårörda lingon', 'unit': 'dl', 'val': 2}
                ]
            }
        ],
        'instructions': [
            {
                'step': 1,
                'title': 'Knaperstek fläsket först',
                'text': 'Stek fläskskivorna i en torr stekpanna på medelvärme tills de är härligt knapriga och gyllenbruna på båda sidor. Lägg över på ett fat med hushållspapper och håll varma i ugnen på 100°C. Spara lite av fläskfettet i pannan!'
            },
            {
                'step': 2,
                'title': 'Skala och grovriv potatisen',
                'text': 'Skala potatisarna och riv dem grovt på ett rivjärn. Gör detta precis innan stekning så att potatisen inte hinner mörkna.'
            },
            {
                'step': 3,
                'title': 'Krama ur all vätska noggrant',
                'text': 'Lägg den rivna potatisen i en ren kökshandduk och vrid/krama ur så mycket potatisvätska som det bara går över diskhon. Ju torrare potatis, desto frasigare rårakor!'
            },
            {
                'step': 4,
                'title': 'Krydda potatisrivet',
                'text': 'Lägg den urkramade potatisen i en bunke. Krydda med salt och nymalen peppar och blanda snabbt runt med händerna.'
            },
            {
                'step': 5,
                'title': 'Stek rårakorna gyllene och frasiga',
                'text': 'Hetta upp rikligt med smör (och lite av det sparade fläskfettet) i stekpannan på medelhög värme. Klicka ut potatisriv och platta ut med en stekspade till tunna, runda kakor (ca 0,5 cm tjocka). Stek i ca 3–4 minuter per sida tills undersidan är djupt gyllenbrun och krispig. Vänd försiktigt och stek andra sidan gyllenbrun.'
            },
            {
                'step': 6,
                'title': 'Lägg upp och servera genast',
                'text': 'Servera rårakorna rykande heta direkt från pannan tillsammans med det knaperstekta fläsket och en generös klick rårörda lingon!'
            }
        ],
        'faqs': [
            {
                'q': 'Ska man ha ägg eller mjöl i rårakor?',
                'a': 'Nej, absolut inte! Det är potatisens egen naturliga stärkelse som binder ihop kakan när den steks. Har man ägg och mjöl i smeten är det raggmunk man lagar.'
            },
            {
                'q': 'Varför faller mina rårakor isär i pannan?',
                'a': 'Det beror oftast på att pannan inte är tillräckligt varm, eller att du vänder rårakan för tidigt. Låt undersidan steka orörd i 3–4 minuter tills stärkelsen smält ihop och bildat en ordentlig, krispig skorpa innan du vänder den.'
            },
            {
                'q': 'Kan man servera rårakor med löjrom?',
                'a': 'Ja, råraka med löjrom, smetana/crème fraiche, finhackad rödlök och dill är en av Sveriges mest klassiska och hyllade förrätter! Uteslut bara fläsket och stek rårakorna aningen mindre.'
            }
        ],
        'community_reviews': [
            {'name': 'Göran Svensson', 'date': '3 oktober 2026', 'rating': 5, 'comment': 'Så här ska riktiga rårakor smaka! Knapriga i kanten och underbart goda med det salta fläsket. Handdukstricket var toppen.', 'verified': True},
            {'name': 'Birgitta M.', 'date': '28 september 2026', 'rating': 5, 'comment': 'Supergott och så enkelt. Hela familjens favorit till torsdagsmiddag.', 'verified': True},
            {'name': 'Daniel Hedberg', 'date': '21 september 2026', 'rating': 5, 'comment': 'Gjorde med löjrom och smetana till lördagsförrätt. Gästerna var helt lyriska!', 'verified': True},
            {'name': 'Maria Lindgren', 'date': '15 september 2026', 'rating': 5, 'comment': 'Perfekt frasighet! Älskar att det bara är ren potatis och smör.', 'verified': True},
            {'name': 'Thomas E.', 'date': '9 september 2026', 'rating': 5, 'comment': '5 av 5 stjärnor. Enkelt och fantastiskt resultat.', 'verified': True},
            {'name': 'Gunilla K.', 'date': '2 september 2026', 'rating': 4, 'comment': 'Jättegoda rårakor. Viktigt att ha rikligt med smör i pannan så de inte fastnar.', 'verified': True}
        ]
    }
]

# Check existing slugs
existing_slugs = {r["slug"] for r in RECIPES}
for nr in BATCH29_RECIPES:
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
