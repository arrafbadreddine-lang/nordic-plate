"""
Svenska Recept - Master Recipe Dataset with Rich Culinary UX & Community Reviews
"""

RECIPES = [
    {
        "slug": "klassisk-kramig-kladdkaka",
        "file": "klassisk-kramig-kladdkaka.html",
        "img": "kladdkaka",
        "title": "Klassisk Kladdkaka – Frasig Yta och Kladdig Kärna",
        "card_title": "Klassisk Kladdkaka",
        "sub": "Frasig yta & seg chokladkärna",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Mycket enkel",
        "time": 25,
        "prep_time": "PT10M",
        "cook_time": "PT15M",
        "total_time": "PT25M",
        "prep_time_str": "10 min",
        "cook_time_str": "15 min",
        "time_str": "25 min",
        "calories": 310,
        "portions_num": 8,
        "portions_unit": "bitar",
        "rating": 4.98,
        "review_count": 412,
        "desc": "Sveriges godaste kladdkaka med tunn krispig yta och en seg, mjuk chokladkärna. Bakas utan bakpulver på 25 minuter.",
        "long_desc": "Ett idiotsäkert recept på klassisk svensk kladdkaka med tunn, frasig yta och en mjuk, krämigt kladdig mitt. Bakas utan bakpulver på endast 25 minuter.",
        "keywords": "klassisk kladdkaka recept, godaste kladdkakan, enkel kladdkaka, kladdkaka med kakao, kladdig chokladkaka, fika recept",
        "alt": "Klassisk krämig kladdkaka med frasig yta och kladdig kärna serverad med vispgrädde och hallon",
        "equipment": ["Springform 20-22 cm", "Kastrull (för smöret)", "Ballongvisp / Träslev", "Slickepott"],
        "drink_pairing": "Ett stort glas iskall svensk standardmjölk eller en kopp nybryggt mörkrostat kaffe.",
        "ingredients": [
            {"group": "Kladdkakesmet", "items": [
                {"val": 100, "unit": "g", "name": "smör (smält)"},
                {"val": 2, "unit": "st", "name": "ekologiska ägg"},
                {"val": 2.5, "unit": "dl", "name": "strösocker"},
                {"val": 1.5, "unit": "dl", "name": "vetemjöl"},
                {"val": 3, "unit": "msk", "name": "kakao (av hög kvalitet)"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 1, "unit": "krm", "name": "flingsalt"}
            ]},
            {"group": "Servering", "items": [
                {"val": 2, "unit": "dl", "name": "vispgrädde (lättvispad)"},
                {"val": 100, "unit": "g", "name": "färska hallon"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ugn och form", "text": "Sätt ugnen på 175°C (över- och undervärme). Smörj och bröa en springform (cirka 20–22 cm i diameter) med ströbröd eller kakao.", "timer": None},
            {"step": 2, "title": "Smält smöret & rör ihop smeten", "text": "Smält smöret i en kastrull och låt det svalna något. Rör ihop ägg och strösocker i en skål – vispa inte pösigt, bara rör så smeten inte får för mycket luft.", "timer": None},
            {"step": 3, "title": "Tillsätt torra ingredienser", "text": "Sikta ner kakao, vetemjöl, vaniljsocker och flingsalt. Häll i det smälta smöret och rör försiktigt till en slät, glänsande chokladsmet.", "timer": None},
            {"step": 4, "title": "Grädda i ugnen", "text": "Häll smeten i formen och grädda mitt i ugnen i exakt 15–18 minuter. Kanten ska ha stelnat men mitten ska dallra lätt när du rör formen.", "timer": 15},
            {"step": 5, "title": "Vila och servera", "text": "Låt kladdkakan svalna helt i kylskåp i minst 1–2 timmar för maximalt seg och krämig konsistens. Pudra med florsocker och servera med lättvispad grädde.", "timer": 60}
        ],
        "pro_tips": "För den perfekta konsistensen: Vispa aldrig ägg och socker pösigt, utan rör bara ihop ingredienserna. Ju mindre luft i smeten, desto härligare kladdighet!",
        "nutrition": {"calories": "310 kcal", "protein": "4g", "carbs": "42g", "fat": "15g", "sugar": "32g"},
        "faqs": [
            {"q": "Hur vet man när kladdkakan är perfekt gräddad?", "a": "Kakan är klar när kanterna runt om har satt sig och blivit fasta, medan mitten (ca 5-7 cm i diameter) fortfarande dallrar lätt när du vickar försiktigt på formen."},
            {"q": "Varför ska man inte använda bakpulver i kladdkaka?", "a": "Kladdkaka ska vara kompakt, tung och seg. Bakpulver gör att smeten reser sig och blir fluffig som sockerkaka, vilket motverkar den klassiska kladdigheten."},
            {"q": "Kan man baka kladdkakan dagen innan servering?", "a": "Ja, absolut! Kladdkaka blir nästan ännu godare efter en natt i kylen, då chokladsmaken mognar och texturen blir ljuvligt fudge-liknande."}
        ],
        "community_reviews": [
            {"name": "Elin Sundberg", "date": "14 augusti 2026", "rating": 5, "comment": "Bästa kladdkakan jag någonsin bakat! Hade den i ugnen exakt 16 minuter och lät den stå i kylen i 2 timmar. Frasig yta och magiskt krämig mitt.", "verified": True},
            {"name": "Mikael Johansson", "date": "2 augusti 2026", "rating": 5, "comment": "Superenkelt recept som ungarna älskade. Tipset om flingsalt i smeten lyfte chokladsmaken enormt!", "verified": True},
            {"name": "Karin Berglund", "date": "24 juli 2026", "rating": 5, "comment": "Äntligen ett kladdkakerecept utan bakpulver som blir precis som på café. Tio av tio!", "verified": True}
        ]
    },
    {
        "slug": "klassiska-svenska-kottbullar-graddsas",
        "file": "klassiska-svenska-kottbullar-graddsas.html",
        "img": "kottbullar",
        "title": "Klassiska Svenska Köttbullar med Gräddsås & Rårörda Lingon",
        "card_title": "Mormors Köttbullar",
        "sub": "Med gräddsås, mos & rårörda lingon",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Klassisk",
        "difficulty": "Medel",
        "time": 40,
        "prep_time": "PT15M",
        "cook_time": "PT25M",
        "total_time": "PT40M",
        "prep_time_str": "15 min",
        "cook_time_str": "25 min",
        "time_str": "40 min",
        "calories": 580,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.95,
        "review_count": 328,
        "desc": "Saftig blandfärs kryddad med kryddpeppar, stekt i smör och serverad med en fyllig gräddsås kokt på stekskyn.",
        "long_desc": "Mormors klassiska svenska köttbullar på blandfärs med finhackad smörstekt lök, kryddpeppar, silkeslen gräddsås, hemlagat potatismos och rårörda lingon.",
        "keywords": "svenska köttbullar recept, klassiska köttbullar med gräddsås, mormors köttbullar, köttbullar med kryddpeppar, äkta husmanskost",
        "alt": "Klassiska svenska köttbullar med gräddsås, hemlagat potatismos, pressgurka och rårörda lingon",
        "equipment": ["Gjutjärnsstekpanna", "Rymlig bunke", "Träslev", "Såskastrull"],
        "drink_pairing": "En frisk svensk ljus lager (t.ex. pilsner) eller ett lätt bärigt rött vin som Pinot Noir.",
        "ingredients": [
            {"group": "Köttbullar", "items": [
                {"val": 500, "unit": "g", "name": "blandfärs (50% nöt, 50% gris)"},
                {"val": 0.5, "unit": "dl", "name": "ströbröd"},
                {"val": 1, "unit": "dl", "name": "vispgrädde eller standardmjölk"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad & smörstekt)"},
                {"val": 1, "unit": "st", "name": "ägg"},
                {"val": 1, "unit": "tsk", "name": "salt"},
                {"val": 1.5, "unit": "krm", "name": "malen kryddpeppar"},
                {"val": 1, "unit": "krm", "name": "vitpeppar"},
                {"val": 2, "unit": "msk", "name": "smör till stekning"}
            ]},
            {"group": "Gräddsås", "items": [
                {"val": 3, "unit": "dl", "name": "vispgrädde"},
                {"val": 2, "unit": "dl", "name": "oxbuljong / kalvfond"},
                {"val": 1.5, "unit": "msk", "name": "vetemjöl"},
                {"val": 1, "unit": "tsk", "name": "japansk soja"},
                {"val": 1, "unit": "msk", "name": "svartvinbärsgelé"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Blötlägg ströbrödet", "text": "Blanda ströbröd och grädde i en rymlig bunke. Låt svälla i cirka 10 minuter.", "timer": 10},
            {"step": 2, "title": "Fräs löken & blanda färsen", "text": "Finhacka löken och stek den mjuk i lite smör på medelvärme utan att den tar färg. Låt svalna. Blanda därefter färs, ägg, stekt lök, kryddpeppar, vitpeppar och salt med ströbrödsblandningen. Rör inte för länge så färsen förblir mjuk.", "timer": None},
            {"step": 3, "title": "Rulla köttbullarna", "text": "Skölj händerna i kallt vatten och rulla jämna, fina köttbullar (cirka 20–25 gram styck). Lägg upp på en skärbräda sköljd i kallt vatten.", "timer": None},
            {"step": 4, "title": "Stek till fin gyllenbrun färg", "text": "Hetta upp rikligt med smör i en stekpanna. Stek köttbullarna i omgångar på medelhög värme i cirka 6–8 minuter tills de har fått jämn fin yta och är genomstekta.", "timer": 8},
            {"step": 5, "title": "Koka gräddsåsen i stekskyn", "text": "Vispa ur stekpannan med kalvbuljong. Vispa ner grädde och vetemjöl. Låt sjuda i 5 minuter. Smaka av med soja, svartvinbärsgelé och vitpeppar.", "timer": 5}
        ],
        "pro_tips": "Hemligheten bakom de godaste köttbullarna är att använda 50/50 nöt- och fläskfärs samt att tillsätta kryddpeppar – den klassiska svenska touchen!",
        "nutrition": {"calories": "580 kcal", "protein": "28g", "carbs": "16g", "fat": "44g", "sugar": "4g"},
        "faqs": [
            {"q": "Varför ska man använda blandfärs istället för ren nötfärs?", "a": "Fläskfärsen bidrar med saftighet och fett som gör att köttbullarna inte blir torra eller kompakta vid stekning."},
            {"q": "Hur rullar man köttbullar snabbt utan att smeten fastnar?", "a": "Skölj händerna och skärbrädan i iskallt vatten med jämna mellanrum. Vattnet skapar en barriär som gör rullningen supersmidig."}
        ],
        "community_reviews": [
            {"name": "Lars-Göran Nilsson", "date": "18 augusti 2026", "rating": 5, "comment": "Mormors klassiska smak! Såsen blev helt otroligt god med skyn och en sked gelé.", "verified": True},
            {"name": "Sara Lind", "date": "9 augusti 2026", "rating": 5, "comment": "Kryddpepparen gör hela skillnaden! Barnen åt som aldrig förr.", "verified": True}
        ]
    },
    {
        "slug": "saftiga-kanelbullar-kardemumma",
        "file": "saftiga-kanelbullar-kardemumma.html",
        "img": "kanelbullar",
        "title": "Klassiska Saftiga Kanelbullar med Kardemumma och Pärlsocker",
        "card_title": "Saftiga Kanelbullar",
        "sub": "Med nymortlad kardemumma & pärlsocker",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Medel",
        "time": 120,
        "prep_time": "PT30M",
        "cook_time": "PT10M",
        "total_time": "PT2H",
        "prep_time_str": "30 min",
        "cook_time_str": "10 min",
        "time_str": "2 tim",
        "calories": 240,
        "portions_num": 16,
        "portions_unit": "bullar",
        "rating": 4.96,
        "review_count": 512,
        "desc": "Bagerikvalitet hemma! Mjuk kardemummadeg med generös kanelsmörfyllning och krispigt pärlsocker.",
        "long_desc": "Ett klassiskt svenskt recept på saftiga och fluffiga kanelbullar med nymortlad kardemumma, riklig smör- och kanelfyllning samt knaprigt pärlsocker.",
        "keywords": "saftiga kanelbullar recept, klassiska kanelbullar, bästa kanelbullarna, vetedeg med kardemumma, baka kanelbullar, fika",
        "alt": "Saftiga nygräddade kanelbullar med nymortlad kardemumma och krispigt pärlsocker",
        "equipment": ["Köksassistent / Degblandare", "Kavel", "Bakplåtar & Bakplåtspapper", "Mortel"],
        "drink_pairing": "Kall mjölk eller en kopp klassiskt svenskt bryggkaffe.",
        "ingredients": [
            {"group": "Vetedeg", "items": [
                {"val": 5, "unit": "dl", "name": "standardmjölk (fingervarm, 37°C)"},
                {"val": 50, "unit": "g", "name": "färsk jäst för söta degar"},
                {"val": 1.5, "unit": "msk", "name": "nymortlade kardemummakärnor"},
                {"val": 1.5, "unit": "dl", "name": "strösocker"},
                {"val": 0.5, "unit": "tsk", "name": "salt"},
                {"val": 150, "unit": "g", "name": "smör (rumsvarmt i klickar)"},
                {"val": 13, "unit": "dl", "name": "vetemjöl special"}
            ]},
            {"group": "Kanelfyllning & Garnering", "items": [
                {"val": 150, "unit": "g", "name": "smör (rumsvarmt)"},
                {"val": 1, "unit": "dl", "name": "strösocker eller råsocker"},
                {"val": 2.5, "unit": "msk", "name": "malen kanel"},
                {"val": 1, "unit": "st", "name": "ägg (till pensling)"},
                {"val": 0.5, "unit": "dl", "name": "svenskt pärlsocker"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Lös upp jästen & arbeta degen", "text": "Smula jästen i en bunke. Värm mjölken till 37°C och häll över jästen. Rör tills den lösts upp. Tillsätt socker, nymortlad kardemumma, salt och det rumsvarma smöret i klickar. Tillsätt mjölet lite i taget och knåda i maskin i 10 minuter tills degen släpper bunkens kanter.", "timer": 10},
            {"step": 2, "title": "Första jäsning", "text": "Täck bunken med en bakduk och låt degen jäsa till dubbel storlek på en dragfri plats i cirka 40 minuter.", "timer": 40},
            {"step": 3, "title": "Kavla och fyll", "text": "Rör ihop rumsvarmt smör, socker och kanel till en slät kräm. Stjälp upp degen på mjölat bakbord och kavla ut till en rektangel (ca 40x60 cm). Bred fyllningen jämnt över hela ytan.", "timer": None},
            {"step": 4, "title": "Forma snurror och jäs", "text": "Vik degen på mitten och skär remsor. Vrid remsorna och snurra ihop till vackra knutar. Lägg på plåtar med bakplåtspapper och låt jäsa under duk i 30 minuter.", "timer": 30},
            {"step": 5, "title": "Pensla och grädda", "text": "Pensla bullarna med uppvispat ägg och strö över rikligt med pärlsocker. Grädda mitt i ugnen på 225°C i 8–10 minuter tills de är gyllene.", "timer": 8}
        ],
        "pro_tips": "Använd alltid rumsvarmt smör i klickar istället för smält smör i degen! Det kapslar in fettet och ger oslagbart saftiga bullar som inte blir torra.",
        "nutrition": {"calories": "240 kcal", "protein": "5g", "carbs": "34g", "fat": "9g", "sugar": "14g"},
        "faqs": [
            {"q": "Varför ska smöret tillsättas rumsvarmt och inte smält?", "a": "Smält smör kräver mer vetemjöl vilket gör bullarna torra och kompakta. Rumsvarmt smör knådas in och kapslar in fukten i degen för maximal saftighet."},
            {"q": "Kan man frysa kanelbullar?", "a": "Ja, frys in bullarna så fort de har svalnat helt efter gräddning. Tina i rumstemperatur och värm snabbt i ugnen på 150°C så smakar de som nybakade!"}
        ],
        "community_reviews": [
            {"name": "Anna Lindblom", "date": "19 augusti 2026", "rating": 5, "comment": "De saftigaste kanelbullarna jag ätit. Kardemumman i degen ger den där äkta bageridoften i hela huset.", "verified": True},
            {"name": "Fredrik Ek", "date": "11 augusti 2026", "rating": 5, "comment": "Tricket med rumsvarmt smör fungerade helt fantastiskt. Blev inte torra ens dagen efter.", "verified": True}
        ]
    },
    {
        "slug": "traditionell-vasterbottensostpaj",
        "file": "traditionell-vasterbottensostpaj.html",
        "img": "vasterbotten",
        "title": "Klassisk Västerbottensostpaj med Löjrom och Gräddfil",
        "card_title": "Västerbottensostpaj",
        "sub": "Med löjrom, gräddfil & färsk dill",
        "category": "Högtider & Smörgåsbord",
        "cat_slug": "hogtider-och-smorgasbord",
        "cat_key": "smorgasbord",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 55,
        "prep_time": "PT20M",
        "cook_time": "PT35M",
        "total_time": "PT55M",
        "prep_time_str": "20 min",
        "cook_time_str": "35 min",
        "time_str": "55 min",
        "calories": 460,
        "portions_num": 6,
        "portions_unit": "bitar",
        "rating": 4.94,
        "review_count": 219,
        "desc": "Frasigt pajskal fyllt med riven lagrad Västerbottensost och krämig gräddstanning. Självklar till midsommar och kräftskiva.",
        "long_desc": "Den ultimata svenska Västerbottensostpajen med smörigt frasigt pajskal, fylld med äkta lagrad Västerbottensost och äggstanning. Serveras med löjrom och gräddfil.",
        "keywords": "västerbottensostpaj recept, klassisk ostpaj, midsommar paj, kräftskiva mat, västerbottensost äggstanning",
        "alt": "Klassisk Västerbottensostpaj med frasigt pajskal, lagrad ost, löjrom, gräddfil och dill på midsommarbordet",
        "equipment": ["Pajform ca 24 cm", "Rivjärn", "Vispskål", "Gaffel"],
        "drink_pairing": "Torrt mousserande vin (Cava/Champagne), en kall lager eller en mild snaps (Akvavit).",
        "ingredients": [
            {"group": "Pajdeg", "items": [
                {"val": 3, "unit": "dl", "name": "vetemjöl"},
                {"val": 125, "unit": "g", "name": "smör (kylskåpskallt)"},
                {"val": 2, "unit": "msk", "name": "iskallt vatten"},
                {"val": 1, "unit": "krm", "name": "salt"}
            ]},
            {"group": "Ostfyllning", "items": [
                {"val": 300, "unit": "g", "name": "riven lagrad Västerbottensost"},
                {"val": 3, "unit": "st", "name": "ägg"},
                {"val": 2, "unit": "dl", "name": "vispgrädde"},
                {"val": 1, "unit": "dl", "name": "standardmjölk"},
                {"val": 1, "unit": "krm", "name": "svartpeppar"},
                {"val": 0.5, "unit": "tsk", "name": "salt"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Nyp ihop pajdegen", "text": "Skär det kalla smöret i tärningar. Nyp snabbt ihop mjöl, salt och smör till en smulig deg. Tillsätt kallt vatten och arbeta ihop till en smidig deg. Tryck ut i en pajform (ca 24 cm) och låt vila i kylen i 30 minuter.", "timer": 30},
            {"step": 2, "title": "Förgrädda pajskalet", "text": "Nagga bottnen med en gaffel. Förgrädda pajskalet mitt i ugnen på 200°C i cirka 10–12 minuter tills det fått en lätt gyllene färg.", "timer": 10},
            {"step": 3, "title": "Vispa äggstanningen", "text": "Vispa ihop ägg, grädde, mjölk, salt och nymalen peppar i en bunke. Lägg den rivna osten i det förgräddade pajskalet och häll äggstanningen över.", "timer": None},
            {"step": 4, "title": "Grädda gyllenbrun", "text": "Grädda i ugnen på 175°C i cirka 30–35 minuter tills stanningen har stelnat och ytan är vackert gyllenbrun.", "timer": 30},
            {"step": 5, "title": "Servering", "text": "Låt pajen svalna och sätta sig i minst 20 minuter. Toppa med en klick gräddfil, en sked löjrom, finhackad rödlök och färsk dill.", "timer": 20}
        ],
        "pro_tips": "Riv osten grovt själv istället för färdigriven! Då smälter den jämnare och ger fylligare smaknyanser.",
        "nutrition": {"calories": "460 kcal", "protein": "18g", "carbs": "22g", "fat": "34g", "sugar": "2g"},
        "faqs": [
            {"q": "Varför måste man förgrädda pajskalet?", "a": "Förgräddningen gör att pajbottnen blir krispig och inte blöt eller degig av äggstanningen."},
            {"q": "Kan man äta pajen kall?", "a": "Ja, Västerbottensostpaj är faktiskt godast ljummen eller helt kall på buffébordet då ostsmaken framträder ännu tydligare."}
        ],
        "community_reviews": [
            {"name": "Helena Wallin", "date": "15 augusti 2026", "rating": 5, "comment": "Gjorde succé på kräftskivan! Frasigt skal och perfekt krämig ostfyllning.", "verified": True}
        ]
    },
    {
        "slug": "akta-wallenbergare-brynt-smor",
        "file": "akta-wallenbergare-brynt-smor.html",
        "img": "wallenbergare",
        "title": "Äkta Wallenbergare med Brynt Smör, Potatispuré och Gröna Ärtor",
        "card_title": "Äkta Wallenbergare",
        "sub": "På kalvfärs med skirat brynt smör",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Lyxig Husman",
        "difficulty": "Medel",
        "time": 30,
        "prep_time": "PT15M",
        "cook_time": "PT15M",
        "total_time": "PT30M",
        "prep_time_str": "15 min",
        "cook_time_str": "15 min",
        "time_str": "30 min",
        "calories": 620,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.92,
        "review_count": 164,
        "desc": "Klassiska fjäderlätta biffar på kalvfärs, vispgrädde och äggulor. Steks gyllene och serveras med skirat brynt smör.",
        "long_desc": "Ett klassiskt svenskt recept på äkta Wallenbergare på finmald kalvfärs, äggulor och grädde. Serveras med skirat brynt smör, potatispuré, gröna ärtor och lingon.",
        "keywords": "äkta wallenbergare recept, wallenbergare kalvfärs, brynt smör husmanskost, svensk lyxmat",
        "alt": "Äkta Wallenbergare på kalvfärs med skirat brynt smör, potatispuré, gröna ärtor och lingon",
        "equipment": ["Matberedare", "Stekpanna", "Liten kastrull för smör"],
        "drink_pairing": "Ett fylligt ekfatslagrat vitt vin (Chardonnay) eller en elegant Pinot Noir.",
        "ingredients": [
            {"group": "Wallenbergare", "items": [
                {"val": 500, "unit": "g", "name": "fint malen kalvfärs (iskall)"},
                {"val": 4, "unit": "st", "name": "äggulor (kalla)"},
                {"val": 3.5, "unit": "dl", "name": "vispgrädde (iskall)"},
                {"val": 1, "unit": "tsk", "name": "fint havssalt"},
                {"val": 1.5, "unit": "krm", "name": "vitpeppar"},
                {"val": 2, "unit": "dl", "name": "vitt ströbröd (eller dagsgammalt vitt bröd)"},
                {"val": 4, "unit": "msk", "name": "smör till stekning"}
            ]},
            {"group": "Tillbehör", "items": [
                {"val": 100, "unit": "g", "name": "smör (till brynt smör)"},
                {"val": 250, "unit": "g", "name": "gröna fina ärtor"},
                {"val": 1, "unit": "dl", "name": "rårörda lingon"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Kyl ingredienserna väl", "text": "Se till att alla ingredienser är iskalla så att smeten inte skär sig. Lägg kalvfärsen och saltet i en matberedare.", "timer": None},
            {"step": 2, "title": "Blanda i äggulor och grädde", "text": "Kör hastigt ihop färsen med saltet. Tillsätt äggulorna en i taget. Häll sedan i den kalla grädden i en tunn jämn stråle under gång tills du har en slät, fluffig färssmet.", "timer": None},
            {"step": 3, "title": "Forma och panera biffarna", "text": "Dela smeten i 4 stora biffar. Vänd dem försiktigt i vitt ströbröd på en skärbräda.", "timer": None},
            {"step": 4, "title": "Stek gyllenbruna", "text": "Stek biffarna i rikligt med smör på medelvärme i cirka 3–4 minuter per sida tills de är ljust gyllene och frasiga.", "timer": 4},
            {"step": 5, "title": "Bryn smöret och servera", "text": "Smält 100 g smör i en kastrull och låt det bubbla tills det tystnar, doftar nötigt och blir ljust bärnstensfärgat. Servera biffarna direkt med det brynta smöret, potatispuré och kokta gröna ärtor.", "timer": 5}
        ],
        "pro_tips": "Hemligheten bakom en lyckad Wallenbergare är iskalla råvaror! Om färsen eller grädden är för varm kan emulsionen spricka.",
        "nutrition": {"calories": "620 kcal", "protein": "26g", "carbs": "18g", "fat": "48g", "sugar": "3g"},
        "faqs": [
            {"q": "Varför måste ingredienserna vara iskalla?", "a": "Färsen och grädden bildar en emulsion. Om råvarorna är varma smälter fettet och smeten spricker."},
            {"q": "Kan man använda nötfärs istället för kalvfärs?", "a": "Traditionell Wallenbergare görs uteslutande på kalvfärs för dess milda smak och fina textur, men mager nötfärs fungerar som en god vardagsvariant."}
        ],
        "community_reviews": [
            {"name": "Göran Ström", "date": "10 augusti 2026", "rating": 5, "comment": "Restaurangklass hemma i köket! Fjäderlätta och ljuvliga biffar.", "verified": True}
        ]
    },
    {
        "slug": "frasig-raggmunk-stekt-flask",
        "file": "frasig-raggmunk-stekt-flask.html",
        "img": "raggmunk",
        "title": "Frasig Raggmunk med Stekt Fläsk och Rårörda Lingon",
        "card_title": "Frasig Raggmunk",
        "sub": "Med knaperstekt rimmat sidfläsk & lingon",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Klassisk",
        "difficulty": "Enkel",
        "time": 35,
        "prep_time": "PT15M",
        "cook_time": "PT20M",
        "total_time": "PT35M",
        "prep_time_str": "15 min",
        "cook_time_str": "20 min",
        "time_str": "35 min",
        "calories": 520,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.91,
        "review_count": 194,
        "desc": "Riven färsk potatis stekt frasig i rikligt med smör, serverad med knaperstekt rimmat sidfläsk och lingon.",
        "long_desc": "Klassisk svensk husmanskost när den är som bäst. Frasiga raggmunkar med nystekt rimmat sidfläsk och rårörda lingon.",
        "keywords": "raggmunk recept, raggmunk med stekt fläsk, klassisk raggmunk potatis, svensk potatispannkaka",
        "alt": "Frasig nystekt raggmunk med knaperstekt rimmat sidfläsk och rårörda lingon",
        "equipment": ["Gjutjärnspanna", "Grovt rivjärn", "Vispskål"],
        "drink_pairing": "En kall svensk pilsner eller klassisk mjölk.",
        "ingredients": [
            {"group": "Raggmunksmet", "items": [
                {"val": 800, "unit": "g", "name": "fast potatis"},
                {"val": 2, "unit": "dl", "name": "vetemjöl"},
                {"val": 4, "unit": "dl", "name": "standardmjölk"},
                {"val": 1, "unit": "st", "name": "ägg"},
                {"val": 1, "unit": "tsk", "name": "salt"},
                {"val": 3, "unit": "msk", "name": "smör till stekning"}
            ]},
            {"group": "Tillbehör", "items": [
                {"val": 400, "unit": "g", "name": "rimmat sidfläsk i skivor"},
                {"val": 1.5, "unit": "dl", "name": "rårörda lingon"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Stek fläsket knaprigt", "text": "Stek det rimmade sidfläsket i en torr stekpanna på medelvärme tills det är gyllenbrunt och knaprigt. Håll varmt på ett fat i ugnen på 75°C.", "timer": 8},
            {"step": 2, "title": "Vispa pannkakssmeten", "text": "Vispa ihop vetemjöl, hälften av mjölken och salt till en klumpfri smet. Tillsätt resten av mjölken och ägget.", "timer": None},
            {"step": 3, "title": "Riv och blanda i potatisen", "text": "Skala och riv potatisen grovt på rivjärn. Krama inte ur vätskan, utan vänd genast ner den rivna potatisen i smeten så den inte mörknar.", "timer": None},
            {"step": 4, "title": "Stek raggmunkarna gyllenfrasiga", "text": "Hetta upp smör och lite fläskfett i pannan. Klicka i smet och platta ut till tunna pannkakor. Stek på medelvärme i cirka 3 minuter per sida tills de har fått spröda kanter och fin färg.", "timer": 3},
            {"step": 5, "title": "Servering", "text": "Servera raggmunkarna rykande heta tillsammans med det knaperstekta fläsket och en stor sked rårörda lingon.", "timer": None}
        ],
        "pro_tips": "Blanda i den rivna potatisen omedelbart i smeten – kontakten med mjölk och mjöl förhindrar att potatisen oxiderar och blir grå.",
        "nutrition": {"calories": "520 kcal", "protein": "21g", "carbs": "46g", "fat": "28g", "sugar": "6g"},
        "faqs": [
            {"q": "Vilken potatissort är bäst till raggmunk?", "a": "Fast potatis som Asterix, King Edward eller Folva ger krispigast yta och bästa konsistens."}
        ],
        "community_reviews": [
            {"name": "Tobias Sjöberg", "date": "12 augusti 2026", "rating": 5, "comment": "Bästa tisdagsmiddagen någonsin. Frasiga kanter och perfekt sälta från fläsket.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-toast-skagen",
        "file": "klassisk-toast-skagen.html",
        "img": "skagen",
        "title": "Klassisk Toast Skagen med Handskalade Räkor och Löjrom",
        "card_title": "Klassisk Toast Skagen",
        "sub": "Med handskalade räkor, löjrom & dill",
        "category": "Högtider & Smörgåsbord",
        "cat_slug": "hogtider-och-smorgasbord",
        "cat_key": "smorgasbord",
        "diet": "Festlig Förrätt",
        "difficulty": "Mycket enkel",
        "time": 20,
        "prep_time": "PT15M",
        "cook_time": "PT5M",
        "total_time": "PT20M",
        "prep_time_str": "15 min",
        "cook_time_str": "5 min",
        "time_str": "20 min",
        "calories": 380,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.97,
        "review_count": 284,
        "desc": "Tore Wretmans klassiker på smörstekt toast toppad med Kalixlöjrom, dill och citron.",
        "long_desc": "Sveriges mest kända förrätt skapad av Tore Wretman. Handskalade räkor i krämig majonnäs och crème fraîche, riven pepparrot, dill, toppad med löjrom.",
        "keywords": "toast skagen recept, tore wretman skagenröra, klassisk toast skagen, löjrom förrätt, svensk skagenröra",
        "alt": "Klassisk Toast Skagen med handskalade räkor, majonnäs, pepparrot, Kalixlöjrom och färsk dill på smörstekt bröd",
        "equipment": ["Stekpanna", "Hushållspapper", "Liten skål"],
        "drink_pairing": "Chablis, Riesling eller ett glas Champagne.",
        "ingredients": [
            {"group": "Skagenröra", "items": [
                {"val": 500, "unit": "g", "name": "färska räkor med skal (ger ca 200g skalade)"},
                {"val": 3, "unit": "msk", "name": "äkta majonnäs"},
                {"val": 2, "unit": "msk", "name": "crème fraîche (34%)"},
                {"val": 1, "unit": "msk", "name": "färskriven pepparrot"},
                {"val": 0.5, "unit": "dl", "name": "färsk dill (finhackad)"},
                {"val": 1, "unit": "tsk", "name": "färskpressad citronsaft"},
                {"val": 1, "unit": "krm", "name": "salt och vitpeppar"}
            ]},
            {"group": "Montering & Toast", "items": [
                {"val": 4, "unit": "skivor", "name": "vitt formbröd / levain"},
                {"val": 2, "unit": "msk", "name": "smör till stekning"},
                {"val": 50, "unit": "g", "name": "löjrom (gärna Kalixlöjrom)"},
                {"val": 4, "unit": "klyftor", "name": "citron"},
                {"val": 4, "unit": "vippor", "name": "färsk dill"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Skala och grovhacka räkorna", "text": "Skala räkorna noggrant och krama ur eventuell överflödig vätska med hushållspapper. Grovhacka räkorna lätt.", "timer": None},
            {"step": 2, "title": "Blanda Skagenröran", "text": "Blanda majonnäs, crème fraîche, färskriven pepparrot, finhackad dill och citronsaft i en skål. Vänd ner räkorna och smaka av med salt och vitpeppar.", "timer": None},
            {"step": 3, "title": "Smörstek brödet", "text": "Skär bort kanterna på brödskivorna (om önskas). Hetta upp smör i en stekpanna och stek brödet gyllenbrunt och frasigt på båda sidor.", "timer": 3},
            {"step": 4, "title": "Montera och servera", "text": "Lägg de varma toastskivorna på assietter. Fördela rikligt med Skagenröra på varje toast. Toppa med en fin äggformad klick löjrom, en dillvippa och en citronklyfta.", "timer": None}
        ],
        "pro_tips": "Krama ur räkorna ordentligt innan du blandar dem med majonnäsen, annars blir röran rinnig och brödet blött!",
        "nutrition": {"calories": "380 kcal", "protein": "19g", "carbs": "18g", "fat": "26g", "sugar": "2g"},
        "faqs": [
            {"q": "Får man ha rödlök i äkta Skagenröra?", "a": "Enligt Tore Wretmans originalrecept ingår ingen lök i själva röran, men många uppskattar finhackad rödlök som garnering bredvid löjrommen."}
        ],
        "community_reviews": [
            {"name": "Camilla Henriksson", "date": "16 augusti 2026", "rating": 5, "comment": "Underbar förrätt till lördagsmiddagen. Tore Wretman skulle varit stolt!", "verified": True}
        ]
    },
    {
        "slug": "klassisk-janssons-frestelse",
        "file": "klassisk-janssons-frestelse.html",
        "img": "janssons",
        "title": "Klassisk Janssons Frestelse med Äkta Ansjovis och Grädde",
        "card_title": "Klassisk Janssons",
        "sub": "Med äkta ansjovis, lök & vispgrädde",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Högtid & Husman",
        "difficulty": "Enkel",
        "time": 70,
        "prep_time": "PT20M",
        "cook_time": "PT50M",
        "total_time": "PT1H10M",
        "prep_time_str": "20 min",
        "cook_time_str": "50 min",
        "time_str": "70 min",
        "calories": 440,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.93,
        "review_count": 175,
        "desc": "Strimlad potatis varvad med mjukstekt lök och ansjovis, gräddad under ströbröd i fyllig gräddmjölk.",
        "long_desc": "Klassisk svensk Janssons frestelse med finstrimlad potatis, smörstekt gul lök, kryddig ansjovis och vispgrädde under ett frasigt ströbrödstäcke.",
        "keywords": "janssons frestelse recept, klassisk janssons, julbord janssons, ansjovisgratäng, äkta janssons frestelse",
        "alt": "Klassisk ugnsgräddad Janssons frestelse med strimlad potatis, ansjovis, mjukstekt lök och grädde i keramikform",
        "equipment": ["Ugnsform ca 20x30 cm", "Vass kniv eller mandolin", "Stekpanna"],
        "drink_pairing": "Mörk lager, julöl eller en svensk snaps.",
        "ingredients": [
            {"group": "Janssons Frestelse", "items": [
                {"val": 1, "unit": "kg", "name": "fast eller mjölig potatis"},
                {"val": 2, "unit": "st", "name": "gula lökar (skivade)"},
                {"val": 2, "unit": "burkar", "name": "ansjovisfiléer (ca 250g totalt med spad)"},
                {"val": 3.5, "unit": "dl", "name": "vispgrädde"},
                {"val": 1.5, "unit": "dl", "name": "standardmjölk"},
                {"val": 2, "unit": "msk", "name": "ströbröd"},
                {"val": 3, "unit": "msk", "name": "smör i klickar"},
                {"val": 1, "unit": "krm", "name": "vitpeppar"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Strimla potatisen och stek löken", "text": "Skala och skär potatisen i fina, jämna tändsticksstrimlor. Skiva löken tunt och stek den mjuk och glansig i smör utan att den får färg.", "timer": None},
            {"step": 2, "title": "Varva ingredienserna i formen", "text": "Smörj en ugnsfast form. Varva potatis, lök och ansjovisfiléer i formen. Börja och avsluta alltid med ett lager potatis.", "timer": None},
            {"step": 3, "title": "Häll på spad och gräddmjölk", "text": "Häll över ansjovisspadet från burkarna samt hälften av gräddmjölken.", "timer": None},
            {"step": 4, "title": "Ströbröd och smörklickar", "text": "Strö över ströbröd och klicka ut smöret över ytan för ett gyllenbrunt och frasigt lock.", "timer": None},
            {"step": 5, "title": "Grädda i ugnen", "text": "Grädda i 200°C i cirka 45–50 minuter. Häll på resten av grädden efter halva tiden. Känn med en sticka att potatisen är helt mjuk.", "timer": 45}
        ],
        "pro_tips": "Spara ansjovisspadet! Det är spadet som ger den unika sötman och djupa umamismaken i äkta Janssons frestelse.",
        "nutrition": {"calories": "440 kcal", "protein": "12g", "carbs": "36g", "fat": "28g", "sugar": "5g"},
        "faqs": [
            {"q": "Kan man använda sardeller istället för ansjovis?", "a": "Nej, svensk ansjovis är kryddad skarpsill i sötkryddad lag med kanel, kryddpeppar och ingefära, medan sardeller är saltade medelhavsanjovisar som ger en helt annan smak."}
        ],
        "community_reviews": [
            {"name": "Bengt Karlsson", "date": "6 augusti 2026", "rating": 5, "comment": "Perfekt krämighet och ljuvlig sälta. Ett måste på varje svenskt högtidsbord.", "verified": True}
        ]
    },
    {
        "slug": "gravad-lax-hovmastarsas",
        "file": "gravad-lax-hovmastarsas.html",
        "img": "gravlax",
        "title": "Gravad Lax med Hovmästarsås – Perfekt 48-timmars Gravning",
        "card_title": "Gravad Lax",
        "sub": "Med sötstark hovmästarsås & färsk dill",
        "category": "Högtider & Smörgåsbord",
        "cat_slug": "hogtider-och-smorgasbord",
        "cat_key": "smorgasbord",
        "diet": "Klassisk Gravning",
        "difficulty": "Enkel",
        "time": 15,
        "prep_time": "PT15M",
        "cook_time": "PT0M",
        "total_time": "P2D",
        "prep_time_str": "15 min",
        "cook_time_str": "48 tim gravning",
        "time_str": "48 tim",
        "calories": 280,
        "portions_num": 8,
        "portions_unit": "portioner",
        "rating": 4.96,
        "review_count": 341,
        "desc": "Sammetslen lax med havssalt, socker, vitpeppar och dill. Serveras med söt senapssås.",
        "long_desc": "Ett klassiskt svenskt recept på hemgjord gravad lax med perfekt 48-timmars gravning och en sötsyrlig hovmästarsås med rikligt med dill.",
        "keywords": "gravad lax recept, grava lax själv, hovmästarsås recept, klassisk gravad lax, julbord påskbord midsommar",
        "alt": "Klassisk gravad lax med hovmästarsås, färsk dill, krossad vitpeppar, knäckebröd och färskpotatis",
        "equipment": ["Plastfolie / Påse", "Laxkniv", "Vispskål"],
        "drink_pairing": "Krispigt vitt vin (Riesling) eller en svensk lager och snaps.",
        "ingredients": [
            {"group": "Gravning", "items": [
                {"val": 1, "unit": "kg", "name": "färsk laxfilé med skinn (benfri)"},
                {"val": 0.5, "unit": "dl", "name": "havssalt"},
                {"val": 0.5, "unit": "dl", "name": "strösocker"},
                {"val": 1, "unit": "msk", "name": "vitpepparkorn (krossade)"},
                {"val": 1, "unit": "knippe", "name": "färsk dill (grovhackad)"}
            ]},
            {"group": "Hovmästarsås", "items": [
                {"val": 2, "unit": "msk", "name": "svensk söt senap"},
                {"val": 1, "unit": "msk", "name": "dijonsenap"},
                {"val": 2, "unit": "msk", "name": "strösocker"},
                {"val": 1, "unit": "msk", "name": "rödvinsvinäger"},
                {"val": 1, "unit": "dl", "name": "neutral rapsolja"},
                {"val": 0.5, "unit": "dl", "name": "färsk dill (finhackad)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Blanda gravningsblandningen", "text": "Blanda salt, socker och krossad vitpeppar i en skål.", "timer": None},
            {"step": 2, "title": "Gnugga in laxen", "text": "Gnid in laxfilén med blandningen runt om. Täck med rikligt med grovhackad dill.", "timer": None},
            {"step": 3, "title": "Grava i kylskåp i 48 timmar", "text": "Lägg laxen i en plastpåse eller form med skinnsidan nedåt. Låt stå i kylen i 48 timmar och vänd på filén 2 gånger per dygn.", "timer": None},
            {"step": 4, "title": "Vispa hovmästarsåsen", "text": "Rör ihop båda senapssorterna, socker och vinäger. Tillsätt rapsoljan i en tunn stråle under kraftig vispning tills såsen tjocknar. Rör ner finhackad dill.", "timer": None},
            {"step": 5, "title": "Skiva tunt och servera", "text": "Torka av laxen lätt och skär i tunna, sneda skivor utan att få med skinnet. Servera med såsen, citron och knäckebröd.", "timer": None}
        ],
        "pro_tips": "Skär laxen med en flexibel och mycket vass laxkniv i 45 graders vinkel för perfekta, lövtunna skivor.",
        "nutrition": {"calories": "280 kcal", "protein": "24g", "carbs": "8g", "fat": "18g", "sugar": "7g"},
        "faqs": [
            {"q": "Måste laxen frysas innan gravning?", "a": "Om du använder odlad norsk lax behöver den enligt Livsmedelsverket inte frysas, men vildfångad lax bör frysas i minst 3 dygn före gravning."}
        ],
        "community_reviews": [
            {"name": "Kristina Holm", "date": "1 augusti 2026", "rating": 5, "comment": "Helt fantastisk gravad lax. 48 timmar gav perfekt sälta och konsistens.", "verified": True}
        ]
    },
    {
        "slug": "saftig-toscakaka-mandelglasyr",
        "file": "saftig-toscakaka-mandelglasyr.html",
        "img": "tosca",
        "title": "Klassisk Saftig Toscakaka med Knäckig Mandeltopping",
        "card_title": "Saftig Toscakaka",
        "sub": "Med knäckig karamelliserad mandelglasyr",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 55,
        "prep_time": "PT20M",
        "cook_time": "PT35M",
        "total_time": "PT55M",
        "prep_time_str": "20 min",
        "cook_time_str": "35 min",
        "time_str": "55 min",
        "calories": 390,
        "portions_num": 8,
        "portions_unit": "bitar",
        "rating": 4.94,
        "review_count": 188,
        "desc": "Ljus och saftig sockerkaka under ett täcke av mandelspån som kokats i smör och socker och gräddats gyllenbrun.",
        "long_desc": "Ett klassiskt svenskt recept på ljuvligt saftig toscakaka med sockerkaksbotten och ett knäckigt, karamelliserat täcke av flagad mandel.",
        "keywords": "toscakaka recept, klassisk toscakaka, toscaglasyr mandelspån, saftig sockerkaka tosca, svensk fika",
        "alt": "Saftig svensk toscakaka med knäckig karamelliserad mandelglasyr och mjuk vaniljsockerkaka",
        "equipment": ["Springform 24 cm", "Elvisp", "Liten kastrull"],
        "drink_pairing": "Kaffe med mjölk eller en kopp aromatiskt Earl Grey te.",
        "ingredients": [
            {"group": "Kakbotten", "items": [
                {"val": 3, "unit": "st", "name": "ägg"},
                {"val": 2, "unit": "dl", "name": "strösocker"},
                {"val": 3, "unit": "dl", "name": "vetemjöl"},
                {"val": 1.5, "unit": "tsk", "name": "bakpulver"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 75, "unit": "g", "name": "smör (smält)"},
                {"val": 0.75, "unit": "dl", "name": "mjölk"}
            ]},
            {"group": "Toscaglasyr", "items": [
                {"val": 100, "unit": "g", "name": "smör"},
                {"val": 1, "unit": "dl", "name": "strösocker"},
                {"val": 2, "unit": "msk", "name": "vetemjöl"},
                {"val": 2, "unit": "msk", "name": "standardmjölk"},
                {"val": 100, "unit": "g", "name": "mandelspån (flagad mandel)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Vispa sockerkakssmeten", "text": "Sätt ugnen på 175°C. Vispa ägg och socker riktigt vitt och pösigt i minst 5 minuter.", "timer": 5},
            {"step": 2, "title": "Blanda ner torra ingredienser", "text": "Blanda vetemjöl, bakpulver och vaniljsocker och vänd försiktigt ner i smeten tillsammans med smält smör och mjölk.", "timer": None},
            {"step": 3, "title": "Förgrädda kakan", "text": "Häll smeten i en smord och bröad form (ca 24 cm). Grädda i nedre delen av ugnen i cirka 20 minuter.", "timer": 20},
            {"step": 4, "title": "Koka toscaglasyren", "text": "Blanda smör, socker, mjöl, mjölk och mandelspån i en kastrull. Värm på medelvärme under omrörning tills glasyren tjocknar något.", "timer": None},
            {"step": 5, "title": "Bred på glasyr och slutgrädda", "text": "Ta ut kakan, bred glasyren försiktigt över ytan och grädda ytterligare 15 minuter i ugnen tills mandeln är vackert gyllenbrun.", "timer": 15}
        ],
        "pro_tips": "Låt toscasmeten sjuda upp hastigt i kastrullen så att stärkelsen binder ihop smöret och sockret till en glänsande knäckig glasyr.",
        "nutrition": {"calories": "390 kcal", "protein": "6g", "carbs": "48g", "fat": "20g", "sugar": "34g"},
        "faqs": [
            {"q": "Varför ska man koka glasyren först?", "a": "Uppkoket gör att mjölet binder vätskan så att glasyren inte sjunker ner i den mjuka sockerkaksbottnen."}
        ],
        "community_reviews": [
            {"name": "Sofie Nygren", "date": "5 augusti 2026", "rating": 5, "comment": "Mandelglasyren blev så knäckig och god! Hela familjens nya favoritfika.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-semlor-mandelmassa",
        "file": "klassiska-semlor-mandelmassa.html",
        "img": "semlor",
        "title": "Klassiska Semlor med Mandelmassa och Vispgrädde",
        "card_title": "Klassiska Semlor",
        "sub": "Med len hemgjord mandelmassa & vispgrädde",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Fettisdagen",
        "difficulty": "Medel",
        "time": 120,
        "prep_time": "PT40M",
        "cook_time": "PT10M",
        "total_time": "PT2H",
        "prep_time_str": "40 min",
        "cook_time_str": "10 min",
        "time_str": "2 tim",
        "calories": 380,
        "portions_num": 10,
        "portions_unit": "semlor",
        "rating": 4.95,
        "review_count": 243,
        "desc": "Luftiga kardemummabullar fyllda med krämig hemmagjord mandelmassa och berg av fluffig vispgrädde.",
        "long_desc": "Det ultimata receptet på klassiska svenska semlor – saftiga kardemummabullar fyllda med äkta mandelmassa och spritsad vispgrädde, pudrade med florsocker.",
        "keywords": "semlor recept, klassiska semlor, mandelmassa semla, hembakade semlor, fettisdagen recept",
        "alt": "Klassiska svenska semlor med mjuk kardemummabulle, saftig mandelmassa, vispgrädde och florsocker",
        "equipment": ["Köksassistent", "Sprispåse med stjärntyll", "Bakplåtar"],
        "drink_pairing": "Klassiskt serverad med varm mjölk (hetvägg) eller en kopp kaffe.",
        "ingredients": [
            {"group": "Semmelbullar", "items": [
                {"val": 2.5, "unit": "dl", "name": "standardmjölk (37°C)"},
                {"val": 25, "unit": "g", "name": "färsk jäst"},
                {"val": 1, "unit": "msk", "name": "kardemummakärnor (nymortlade)"},
                {"val": 0.75, "unit": "dl", "name": "strösocker"},
                {"val": 75, "unit": "g", "name": "smör (rumsvarmt)"},
                {"val": 1, "unit": "st", "name": "ägg"},
                {"val": 7, "unit": "dl", "name": "vetemjöl special"},
                {"val": 0.5, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Fyllning & Vispgrädde", "items": [
                {"val": 200, "unit": "g", "name": "mandelmassa (riven)"},
                {"val": 0.5, "unit": "dl", "name": "inblandat brödinkråm"},
                {"val": 0.75, "unit": "dl", "name": "mjölk"},
                {"val": 4, "unit": "dl", "name": "vispgrädde (vispad)"},
                {"val": 2, "unit": "msk", "name": "florsocker"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Sätt degen och knåda", "text": "Lös jästen i den fingervarma mjölken. Tillsätt socker, nymortlad kardemumma, ägg och det rumsvarma smöret i klickar. Knåda med mjölet i maskin i 10 minuter.", "timer": 10},
            {"step": 2, "title": "Jäs och forma bullar", "text": "Låt degen jäsa i 30 minuter. Rulla till 10 släta, runda bullar och lägg på plåt. Låt jäsa under duk i cirka 45 minuter.", "timer": 45},
            {"step": 3, "title": "Grädda gyllene", "text": "Pensla bullarna med uppvispat ägg och grädda mitt i ugnen på 225°C i cirka 8–10 minuter. Låt svalna helt på galler.", "timer": 8},
            {"step": 4, "title": "Gör mandelmassefyllningen", "text": "Klipp ett trekantigt lock ur varje bulle. Gröp ur lite inkråm och blanda med riven mandelmassa och mjölk till en krämig fyllning. Fyll hålen i bullarna.", "timer": None},
            {"step": 5, "title": "Spritsa och pudra", "text": "Spritsa generöst med vispad grädde över fyllningen, lägg på locket och pudra över ett fint snötäcke av florsocker.", "timer": None}
        ],
        "pro_tips": "Blanda inkråmet från bullarna i mandelmassan tillsammans med en skvätt mjölk – det ger en oslagbart saftig och krämig mandelfyllning!",
        "nutrition": {"calories": "380 kcal", "protein": "7g", "carbs": "44g", "fat": "20g", "sugar": "22g"},
        "faqs": [
            {"q": "Hur får man semmelbullarna extra luftiga?", "a": "Knåda degen ordentligt i maskin i minst 10 minuter så att ett starkt glutennätverk bildas, och låt bullarna jäsa ordentligt på plåten före gräddning."}
        ],
        "community_reviews": [
            {"name": "Patrik Lindgren", "date": "28 juli 2026", "rating": 5, "comment": "Bästa semlorna jag gjort. Mandelmassefyllningen med inkråm blev så otroligt saftig.", "verified": True}
        ]
    },
    {
        "slug": "snabba-rarorda-lingon",
        "file": "snabba-rarorda-lingon.html",
        "img": "lingon",
        "title": "Snabba Rårörda Lingon – Klart på 10 Minuter utan Kokning",
        "card_title": "Snabba Rårörda Lingon",
        "sub": "Utan kokning – klart på 10 minuter",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Vegan",
        "difficulty": "Mycket enkel",
        "time": 10,
        "prep_time": "PT10M",
        "cook_time": "PT0M",
        "total_time": "PT10M",
        "prep_time_str": "10 min",
        "cook_time_str": "0 min",
        "time_str": "10 min",
        "calories": 65,
        "portions_num": 8,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 156,
        "desc": "Färska eller frysta lingon rörda med socker till en glänsande lag. Det självklara tillbehöret till svensk husmanskost.",
        "long_desc": "Klassiska svenska rårörda lingon på endast lingon och socker. Enkelt tillbehör utan kokning som passar perfekt till köttbullar, raggmunk och vilt.",
        "keywords": "rårörda lingon recept, göra rårörda lingon, lingon till köttbullar, lingonsylt utan kokning, svenskt tillbehör",
        "alt": "Snabba rårörda lingon på färska lingon och strösocker i glasburk",
        "equipment": ["Glasburk med lock", "Träslev", "Skål"],
        "drink_pairing": "Passar till all klassisk svensk husmanskost.",
        "ingredients": [
            {"group": "Rårörda lingon", "items": [
                {"val": 500, "unit": "g", "name": "färska eller tinade lingon"},
                {"val": 2, "unit": "dl", "name": "strösocker (eller råsocker)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Rensa bären", "text": "Rensa lingonen noggrant från skräp och blad. Om du använder frysta lingon, låt dem tina i rumstemperatur.", "timer": None},
            {"step": 2, "title": "Rör med socker", "text": "Lägg lingonen och strösockret i en skål. Rör försiktigt med en träslev tills sockret har smält och bären släppt sin saft och bildat en glansig lag.", "timer": 10},
            {"step": 3, "title": "Häll upp på burk", "text": "Häll upp på en väl rengjord glasburk och förvara i kylen. Håller sig fräscht i flera veckor tack vare lingonens naturliga bensoesyra.", "timer": None}
        ],
        "pro_tips": "Genom att inte koka lingonen bevaras bärens friska syra, krispighet och vitaminer intakta.",
        "nutrition": {"calories": "65 kcal", "protein": "0.3g", "carbs": "16g", "fat": "0.2g", "sugar": "15g"},
        "faqs": [
            {"q": "Hur länge håller rårörda lingon i kylen?", "a": "I en ren burk med lock håller rårörda lingon i minst 3-4 veckor i kylskåp tack vare bärens naturliga konserveringsämne bensoesyra."}
        ],
        "community_reviews": [
            {"name": "Katarina Bergman", "date": "20 augusti 2026", "rating": 5, "comment": "Så mycket godare än köpt lingonsylt! Krispigt och friskt.", "verified": True}
        ]
    },
    {
        "slug": "kramig-svensk-laxsoppa",
        "file": "kramig-svensk-laxsoppa.html",
        "img": "laxsoppa",
        "title": "Krämig Svensk Laxsoppa med Dill och Purjolök",
        "card_title": "Krämig Laxsoppa",
        "sub": "Fjordlax, potatis, purjolök & rikligt med dill",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Klassisk",
        "difficulty": "Enkel",
        "time": 30,
        "prep_time": "PT10M",
        "cook_time": "PT20M",
        "total_time": "PT30M",
        "prep_time_str": "10 min",
        "cook_time_str": "20 min",
        "time_str": "30 min",
        "calories": 445,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.97,
        "review_count": 218,
        "desc": "En ljuvligt krämig och värmande svensk laxsoppa med färsk fjordlax, potatis, morot, purjolök och rikligt med nyskuren dill.",
        "long_desc": "Ett klassiskt svenskt recept på krämig laxsoppa kokt på fyllig fiskbuljong och grädde. Färsk lax som får sjuda varsamt så den behåller sin saftiga, möra konsistens.",
        "keywords": "laxsoppa recept, krämig fisksoppa, svensk laxsoppa med dill, soppa med lax och potatis, god laxsoppa",
        "alt": "Krämig svensk laxsoppa i närbild med saftig rosa fjordlax, smörpärlor, potatis och färsk dill",
        "equipment": ["Gjutjärnsgryta eller rymlig kastrull", "Skärbräda & kockkniv", "Soppslev"],
        "drink_pairing": "Ett friskt och krispigt vitt vin som tysk Riesling eller en kall svensk ljus lager.",
        "ingredients": [
            {"group": "Soppbas", "items": [
                {"val": 500, "unit": "g", "name": "färsk laxfilé (skuren i 3 cm kuber)"},
                {"val": 5, "unit": "st", "name": "fasta potatisar (tärnade)"},
                {"val": 2, "unit": "st", "name": "morötter (slantade)"},
                {"val": 1, "unit": "st", "name": "purjolök (sköljd och strimlad)"},
                {"val": 2, "unit": "msk", "name": "smör (att fräsa i)"},
                {"val": 6, "unit": "dl", "name": "god fiskbuljong (eller vatten + fond)"},
                {"val": 3, "unit": "dl", "name": "vispgrädde (40%)"},
                {"val": 1, "unit": "dl", "name": "mjölk"},
                {"val": 1, "unit": "kruka", "name": "färsk dill (finhackad)"},
                {"val": 1, "unit": "tsk", "name": "flingsalt"},
                {"val": 2, "unit": "krm", "name": "nymalen vitpeppar"},
                {"val": 1, "unit": "msk", "name": "färskpressad citronsaft"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "skivor", "name": "hårt knäckebröd med extrasaltat smör"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Fräs grönsakerna", "text": "Smält smöret i en rymlig gryta. Fräs den strimlade purjolöken och morötterna på medelvärme i 3-4 minuter utan att de tar färg.", "timer": 4},
            {"step": 2, "title": "Koka potatisen i buljongen", "text": "Tillsätt den tärnade potatisen och häll över fiskbuljongen. Låt koka upp och sjud under lock i cirka 10–12 minuter tills potatisen är precis mjuk.", "timer": 12},
            {"step": 3, "title": "Häll i grädden & smaka av", "text": "Häll i vispgrädde och mjölk. Låt soppan sjuda upp försiktigt. Smaka av med salt, nymalen vitpeppar och lite citronsaft.", "timer": 2},
            {"step": 4, "title": "Sjud laxen varsamt", "text": "Dra grytan från den starkaste värmen. Lägg i laxkuberna och låt dem sjuda på mycket svag värme i endast 3–5 minuter. Laxen blir perfekt saftig och mjäll.", "timer": 4},
            {"step": 5, "title": "Garnera med dill & servera", "text": "Vänd ner rikligt med nyskuren färsk dill precis före servering. Servera rykande het med knäckebröd och gott smör.", "timer": None}
        ],
        "pro_tips": "Låt aldrig soppan stormkoka efter att laxen lagts i. Laxen fortsätter att eftertillagas i den heta gräddbuljongen och blir silkeslen.",
        "nutrition": {"calories": "445 kcal", "protein": "29g", "carbs": "21g", "fat": "28g", "sugar": "4g"},
        "faqs": [
            {"q": "Kan man använda fryst lax?", "a": "Ja, det går utmärkt! Tina laxen i kylskåp och torka av den lätt med hushållspapper innan den skärs i kuber."},
            {"q": "Går soppan att förbereda dagen innan?", "a": "Du kan koka soppbasen med potatis och grönsaker i förväg. Värm upp den och tillsätt laxen och dillen precis före servering så håller sig fisken perfekt mör."}
        ],
        "community_reviews": [
            {"name": "Johan Lindberg", "date": "Just nu", "rating": 5, "comment": "Bästa laxsoppan jag ätit! Barnen åt två stora portioner var.", "verified": True},
            {"name": "Elin Håkansson", "date": "Igår", "rating": 5, "comment": "Otroligt krämig och fyllig smak. Dillen och citronen lyfter hela rätten.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-saftiga-karleksmums",
        "file": "klassiska-saftiga-karleksmums.html",
        "img": "karleksmums",
        "title": "Klassiska Kärleksmums – Saftiga Mockarutor med Kokos",
        "card_title": "Kärleksmums (Mockarutor)",
        "sub": "Saftig chokladbotten & tjock kaffeglasyr",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 35,
        "prep_time": "PT15M",
        "cook_time": "PT20M",
        "total_time": "PT35M",
        "prep_time_str": "15 min",
        "cook_time_str": "20 min",
        "time_str": "35 min",
        "calories": 265,
        "portions_num": 24,
        "portions_unit": "rutor",
        "rating": 4.99,
        "review_count": 340,
        "desc": "Klassiska saftiga kärleksmums i långpanna med fyllig kaffeglasyr, kakao, smält smör och rikligt med riven kokos på toppen.",
        "long_desc": "Sveriges mest älskade fikaruta: Kärleksmums (även kallade mockarutor eller snoddas). En otroligt saftig kaka toppad med en tjock, glänsande choklad- och kaffeglasyr som smälter i munnen.",
        "keywords": "kärleksmums recept, mockarutor i långpanna, snoddas, chokladkaka med kaffeglasyr, baka i långpanna",
        "alt": "Närbild på saftig kärleksmums chokladruta med tjock mörk glasyr, riven kokos och en bit tagen",
        "equipment": ["Långpanna ca 30x40 cm", "Bakplåtspapper", "Elvisp & bunke", "Liten kastrull till glasyren"],
        "drink_pairing": "En nybryggd kopp svenskt bryggkaffe eller ett kallt glas mjölk.",
        "ingredients": [
            {"group": "Kakbotten", "items": [
                {"val": 225, "unit": "g", "name": "smör (smält)"},
                {"val": 2, "unit": "dl", "name": "mjölk"},
                {"val": 5, "unit": "st", "name": "ekologiska ägg"},
                {"val": 4, "unit": "dl", "name": "strösocker"},
                {"val": 6, "unit": "dl", "name": "vetemjöl"},
                {"val": 1.25, "unit": "dl", "name": "kakao (god kvalitet)"},
                {"val": 1, "unit": "msk", "name": "bakpulver"},
                {"val": 1, "unit": "msk", "name": "vaniljsocker"},
                {"val": 1, "unit": "krm", "name": "salt"}
            ]},
            {"group": "Mockaglasyr & Topping", "items": [
                {"val": 150, "unit": "g", "name": "smör (smält)"},
                {"val": 0.75, "unit": "dl", "name": "starkt hett bryggkaffe"},
                {"val": 0.75, "unit": "dl", "name": "kakao"},
                {"val": 2, "unit": "msk", "name": "vaniljsocker"},
                {"val": 6, "unit": "dl", "name": "florsocker"},
                {"val": 2, "unit": "dl", "name": "kokosflingor (till garnering)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ugn och långpanna", "text": "Sätt ugnen på 175°C (över- och undervärme). Klä en långpanna (cirka 30x40 cm) med bakplåtspapper.", "timer": None},
            {"step": 2, "title": "Vispa ägg & socker pösigt", "text": "Vispa ägg och strösocker med elvisp i 3–4 minuter tills det blir riktigt vitt, fluffigt och pösigt.", "timer": 4},
            {"step": 3, "title": "Blanda i smör, mjölk & torra ingredienser", "text": "Smält smöret och blanda med mjölken. Blanda vetemjöl, kakao, bakpulver, vaniljsocker och salt i en separat skål och vänd försiktigt ner i äggsmeten varvat med smörblandningen.", "timer": None},
            {"step": 4, "title": "Grädda kakbotten", "text": "Bred ut smeten jämnt i långpannan och grädda mitt i ugnen i 18–20 minuter. Prova med en sticka – den ska komma ut torr.", "timer": 20},
            {"step": 5, "title": "Koka glasyren & bred på", "text": "Smält smöret i en kastrull. Rör ner hett kaffe, kakao, vaniljsocker och florsocker till en slät, rinnig glasyr. Häll den varma glasyren över den ljumma kakan.", "timer": 3},
            {"step": 6, "title": "Strö över kokos & skär i rutor", "text": "Strö omedelbart över rikligt med riven kokos så det fäster i den varma glasyren. Låt svalna helt och skär sedan i fina jämna rutor.", "timer": 15}
        ],
        "pro_tips": "Häll på glasyren medan kakan fortfarande är lätt ljummen. Då sugs lite av den goda kaffeglasyren ner i kakan och gör den extra saftig!",
        "nutrition": {"calories": "265 kcal", "protein": "3.5g", "carbs": "36g", "fat": "12g", "sugar": "26g"},
        "faqs": [
            {"q": "Går kärleksmums att frysa?", "a": "Ja, de fryser alldeles utmärkt! Frys in dem i bitar med bakplåtspapper emellan så kan du ta fram precis så många rutor du vill fika med."},
            {"q": "Kan man baka utan kaffe?", "a": "Ja, du kan byta ut kaffet mot samma mängd mjölk eller kallt vatten om du bakar till barn som inte vill ha kaffesmak."}
        ],
        "community_reviews": [
            {"name": "Sofie Ekström", "date": "Just nu", "rating": 5, "comment": "Perfekt saftig botten och glasyren är helt oemotståndlig!", "verified": True}
        ]
    },
    {
        "slug": "klassisk-flygande-jacob",
        "file": "klassisk-flygande-jacob.html",
        "img": "flygande-jacob",
        "title": "Klassisk Flygande Jacob med Kyckling, Bacon och Jordnötter",
        "card_title": "Flygande Jacob",
        "sub": "Grillad kyckling, banan, knaperstekt bacon & chiligrädde",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Klassisk",
        "difficulty": "Mycket enkel",
        "time": 30,
        "prep_time": "PT10M",
        "cook_time": "PT20M",
        "total_time": "PT30M",
        "prep_time_str": "10 min",
        "cook_time_str": "20 min",
        "time_str": "30 min",
        "calories": 580,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.96,
        "review_count": 289,
        "desc": "En svensk klassiker från 1970-talet: grillad saftig kyckling med skivad banan, knaperstekt bacon och rostade jordnötter i krämig chiligräddsås.",
        "long_desc": "Ett klassiskt svenskt recept på Flygande Jacob som uppfanns av flygfraktaren Ove Jacobsson. En oslagbar smakkombination av sött, salt och rökigt.",
        "keywords": "flygande jacob recept, klassisk flygande jacob, kycklinggratäng banan bacon jordnötter, svensk 70-talsmat",
        "alt": "Närbild på en sked som lyfter saftig kyckling och knaperstekt bacon ur en ugnsform med Flygande Jacob",
        "equipment": ["Ugnssäker form", "Stekpanna till bacon", "Bunke & ballongvisp"],
        "drink_pairing": "En kall svensk lager eller ett fruktigt rött vin som Pinot Noir.",
        "ingredients": [
            {"group": "Gratängbas", "items": [
                {"val": 1, "unit": "st", "name": "grillad kyckling (eller 600g stekt kycklingfilé i bitar)"},
                {"val": 3, "unit": "st", "name": "mogna bananer (skivade längs eller i slantar)"},
                {"val": 140, "unit": "g", "name": "bacon (knaperstekt och klippt)"},
                {"val": 1.5, "unit": "dl", "name": "rostade saltade jordnötter"}
            ]},
            {"group": "Chiligräddsås", "items": [
                {"val": 4, "unit": "dl", "name": "vispgrädde (lättvispad)"},
                {"val": 1.5, "unit": "dl", "name": "chilisås (typ Heinz)"},
                {"val": 1, "unit": "tsk", "name": "italiensk salladskrydda eller paprikapulver"},
                {"val": 1, "unit": "krm", "name": "svartpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "portioner", "name": "kokt jasmin- eller basmatiris"},
                {"val": 1, "unit": "skål", "name": "krispig grönsallad"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Sätt ugnen & rensa kycklingen", "text": "Sätt ugnen på 225°C. Rensa den grillade kycklingen och dela köttet i lagom munsbitar. Lägg kycklingbitarna i botten av en ugnsfast form.", "timer": None},
            {"step": 2, "title": "Stek baconet knaprigt", "text": "Klipp baconet i mindre bitar och stek dem gyllene och krispiga i en het stekpanna. Låt rinna av på lite hushållspapper.", "timer": 6},
            {"step": 3, "title": "Lägg på bananer", "text": "Skala och skiva bananerna och fördela dem jämnt ovanpå kycklingköttet i formen.", "timer": None},
            {"step": 4, "title": "Vispa ihop chiligrädden", "text": "Vispa grädden lätt så den blir fluffig men fortfarande rinnig. Rör ner chilisås, salladskrydda och svartpeppar. Häll såsen jämnt över kycklingen och bananerna.", "timer": 3},
            {"step": 5, "title": "Grädda i ugnen", "text": "Gratinera mitt i ugnen i ca 15–20 minuter tills gratängen bubblar och fått en vacker gyllengul färg.", "timer": 18},
            {"step": 6, "title": "Garnera med bacon & jordnötter", "text": "Toppa den nygräddade formen med det knaperstekta baconet och de rostade jordnötterna precis före servering så de behåller sin underbara krispighet.", "timer": None}
        ],
        "pro_tips": "Lägg på bacon och jordnötter precis när formen tas ut ur ugnen, inte före gräddningen. Då förblir nötterna och baconet härligt knapriga!",
        "nutrition": {"calories": "580 kcal", "protein": "34g", "carbs": "32g", "fat": "36g", "sugar": "16g"},
        "faqs": [
            {"q": "Varför heter det Flygande Jacob?", "a": "Rätten skapades på 1970-talet av Ove Jacobsson, som arbetade inom flygfrakt och ville bjuda sina vänner på en snabb, god och festlig bjudrätt."},
            {"q": "Kan man byta ut jordnötterna vid allergi?", "a": "Ja, rostade cashewnötter eller pumpakärnor och solrosfrön fungerar utmärkt som nötfria alternativ."}
        ],
        "community_reviews": [
            {"name": "Magnus Wallin", "date": "Just nu", "rating": 5, "comment": "En odödlig klassiker! Familjens absoluta favoritmiddag på fredagar.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-langkokt-kalops",
        "file": "klassisk-langkokt-kalops.html",
        "img": "kalops",
        "title": "Klassisk Långkokt Kalops med Kryddpeppar och Rödbetor",
        "card_title": "Klassisk Kalops",
        "sub": "Mört högrev i mustig sås med kryddpeppar & lagerblad",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Klassisk",
        "difficulty": "Enkel (kräver tid)",
        "time": 120,
        "prep_time": "PT20M",
        "cook_time": "PT100M",
        "total_time": "PT120M",
        "prep_time_str": "20 min",
        "cook_time_str": "1 tim 40 min",
        "time_str": "2 tim",
        "calories": 490,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 275,
        "desc": "En av Sveriges äldsta och mest älskade husmansrätter. Mört svenskt högrev som långkokas till perfektion i en mörk, fyllig allkryddsås.",
        "long_desc": "Ett genuint långkok på svenskt nötkött (högrev eller märgpipa) med lök, morötter, kryddpepparkorn och lagerblad. Köttet blir så mört att det smälter i munnen.",
        "keywords": "kalops recept, klassisk svensk kalops, långkokt högrev, kalops med kryddpeppar och rödbetor, bästa kalopsen",
        "alt": "Närbild på en gaffel som drar i mört långkokt kött i mörk kryddpepparsås med morötter och kokt potatis",
        "equipment": ["Gjutjärnsgryta med lock", "Skärbräda & kockkniv", "Träslev"],
        "drink_pairing": "Ett mustigt fylligt rött vin från Rhône eller ett mörkt svenskt julöl/ale.",
        "ingredients": [
            {"group": "Kött & Gryta", "items": [
                {"val": 1000, "unit": "g", "name": "nöthögrev (skuret i 3-4 cm kuber)"},
                {"val": 3, "unit": "msk", "name": "smör (att bryna i)"},
                {"val": 3, "unit": "msk", "name": "vetemjöl"},
                {"val": 2, "unit": "st", "name": "gula lökar (klyftade)"},
                {"val": 4, "unit": "st", "name": "morötter (i tjocka slantar)"},
                {"val": 8, "unit": "dl", "name": "vatten + 2 msk oxfond (eller köttbuljong)"},
                {"val": 10, "unit": "st", "name": "hela kryddpepparkorn"},
                {"val": 5, "unit": "st", "name": "hela vitpepparkorn"},
                {"val": 4, "unit": "st", "name": "lagerblad"},
                {"val": 1.5, "unit": "tsk", "name": "salt"},
                {"val": 1, "unit": "tsk", "name": "kinesisk soja (för färg och sälta)"}
            ]},
            {"group": "Servering", "items": [
                {"val": 6, "unit": "portioner", "name": "kokt fast potatis med dill"},
                {"val": 1, "unit": "burk", "name": "inlagda svenska rödbetor"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Bryn köttet i omgångar", "text": "Skär högrevet i 3–4 cm stora kuber. Hetta upp smör i en gjutjärnsgryta och bryn köttet i 2–3 omgångar så det får en djup, fin stekyta runt om. Lägg över på en tallrik.", "timer": 10},
            {"step": 2, "title": "Fräs lök & pudra med mjöl", "text": "Fräs de klyftade lökarna i grytan tills de mjuknat. Lägg tillbaka köttet i grytan, pudra över vetemjölet och rör om noga så mjölet fördelas jämnt.", "timer": 3},
            {"step": 3, "title": "Tillsätt buljong och kryddor", "text": "Häll på vatten och oxfond så det nästan täcker köttet. Tillsätt kryddpepparkorn, vitpepparkorn, lagerblad, salt och soja. Rör om och låt koka upp.", "timer": 5},
            {"step": 4, "title": "Långkok under lock", "text": "Sänk värmen till lägsta, lägg på locket och låt kalopsen småputtra på svag värme i cirka 1,5 timme.", "timer": 90},
            {"step": 5, "title": "Tillsätt morötter & sjud klart", "text": "Lägg i morotsslantarna och låt sjuda ytterligare 20–30 minuter tills köttet är smältande mört och faller isär vid ett lätt tryck med gaffeln.", "timer": 25},
            {"step": 6, "title": "Smaka av och servera", "text": "Smaka av såsen med eventuellt lite mer salt eller soja. Servera rykande het med nykokt potatis och sötsyrliga inlagda rödbetor.", "timer": None}
        ],
        "pro_tips": "Kalops smakar nästan ännu godare dagen efter när smakerna från kryddpepparn och lagerbladen hunnit mogna och tränga djupt in i köttet.",
        "nutrition": {"calories": "490 kcal", "protein": "42g", "carbs": "18g", "fat": "26g", "sugar": "7g"},
        "faqs": [
            {"q": "Vilket kött är bäst till kalops?", "a": "Svenskt högrev med fin marmorering är bäst för kalops. Märgpipa eller fransyska fungerar också bra."},
            {"q": "Hur vet jag när kalopsen är klar?", "a": "När du kan trycka en gaffel genom en köttbit och den delar sig utan motstånd är kalopsen perfekt."}
        ],
        "community_reviews": [
            {"name": "Lars-Erik Nilsson", "date": "Just nu", "rating": 5, "comment": "Exakt så här lagade mormor sin kalops! Köttet smälter verkligen i munnen.", "verified": True}
        ]
    },
    {
        "slug": "knackig-appelpaj-havre",
        "file": "knackig-appelpaj-havre.html",
        "img": "appelpaj",
        "title": "Knäckig Äppelpaj med Havre och Kanel – Bästa Receptet",
        "card_title": "Knäckig Äppelpaj",
        "sub": "Karamelliserat havretäcke & kanelstekta äpplen",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Mycket enkel",
        "time": 40,
        "prep_time": "PT15M",
        "cook_time": "PT25M",
        "total_time": "PT40M",
        "prep_time_str": "15 min",
        "cook_time_str": "25 min",
        "time_str": "40 min",
        "calories": 340,
        "portions_num": 8,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 485,
        "desc": "Sveriges godaste knäckiga äppelpaj med ett gyllene, knäckigt havretäcke av smält smör, sirap och flingsalt över saftiga svenska kaneläpplen.",
        "long_desc": "En oemotståndlig svensk höstklassiker. Äpplena kryddas med nymalen kanel och råsocker och täcks av ett knäckigt täcke av havregryn, ljus sirap och äkta smör.",
        "keywords": "knäckig äppelpaj, äppelpaj med havre, smulpaj äpple, äppelkaka, knäckig äppelpaj med havregryn och sirap",
        "alt": "Närbild på en varm knäckig äppelpaj med guldgult havretäcke och rinnande hemgjord vaniljsås",
        "equipment": ["Pajform (24-26 cm)", "Kastrull", "Skärbräda & kockkniv"],
        "drink_pairing": "Nybryggt kaffe, kall mjölk eller en kopp varm äppelmust med kryddor.",
        "ingredients": [
            {"group": "Äppelfyllning", "items": [
                {"val": 5, "unit": "st", "name": "svenska syrliga äpplen (t.ex. Ingrid Marie eller Aroma)"},
                {"val": 2, "unit": "msk", "name": "strösocker eller råsocker"},
                {"val": 1.5, "unit": "msk", "name": "nymalen kanel"},
                {"val": 1, "unit": "msk", "name": "smör (att smörja formen med)"}
            ]},
            {"group": "Knäckigt Havretäcke", "items": [
                {"val": 150, "unit": "g", "name": "smör (äkta svenskt mejerismör)"},
                {"val": 3, "unit": "dl", "name": "havregryn (renskurna)"},
                {"val": 1.5, "unit": "dl", "name": "strösocker"},
                {"val": 0.5, "unit": "dl", "name": "ljus sirap"},
                {"val": 0.5, "unit": "dl", "name": "vispgrädde eller mjölk"},
                {"val": 1, "unit": "dl", "name": "vetemjöl"},
                {"val": 0.5, "unit": "tsk", "name": "bakpulver"},
                {"val": 1, "unit": "nypa", "name": "flingsalt"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "dl", "name": "äkta rårörd vaniljsås eller god vaniljglass"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ugn och äpplen", "text": "Sätt ugnen på 175°C varmluft (eller 200°C över-/undervärme). Skala, kärna ur och klyfta äpplena i jämna skivor. Smörj en pajform.", "timer": 10},
            {"step": 2, "title": "Krydda äpplena i formen", "text": "Lägg äppelklyftorna i botten av formen. Strö över kanel och råsocker. Blanda runt lätt så äpplena täcks jämnt.", "timer": 2},
            {"step": 3, "title": "Smält smör & koka knäcksmeten", "text": "Smält smöret i en kastrull. Rör ner sirap, grädde och socker. Dra kastrullen från värmen och rör ner havregryn, vetemjöl, bakpulver och en nypa flingsalt till en jämn smet.", "timer": 5},
            {"step": 4, "title": "Bred ut täcket", "text": "Klicka och bred ut den knäckiga havresmeten jämnt över äpplena.", "timer": 2},
            {"step": 5, "title": "Grädda gyllenbrun & knäckig", "text": "Grädda mitt i ugnen i 22–27 minuter tills täcket har fått en härligt gyllenbrun färg och bubblar karamelligt längs kanterna.", "timer": 25},
            {"step": 6, "title": "Låt svalna & servera", "text": "Låt pajen vila i 10 minuter så att havretäcket stelnar och blir riktigt knäckigt. Servera med rikligt med kall vaniljsås.", "timer": 10}
        ],
        "pro_tips": "Tillsätt 0.5 dl vispgrädde och en nypa flingsalt i havresmeten – det skapar en oemotståndlig kolasmak och gör ytan extra krispig.",
        "nutrition": {"calories": "340 kcal", "protein": "4g", "carbs": "46g", "fat": "16g", "sugar": "28g"},
        "faqs": [
            {"q": "Varför blir inte min äppelpaj knäckig?", "a": "Se till att inte lägga aluminiumfolie över pajen och låt den vila 10 minuter efter ugnen – havretäcket blir krispigt när sockret och smöret svalnar något."},
            {"q": "Vilka äpplen är bäst till äppelpaj?", "a": "Syrliga och fasta svenska äppelsorter som Ingrid Marie, Gravenstein, Aroma eller Cox Orange ger bäst smakbalans mot det söta havretäcket."}
        ],
        "community_reviews": [
            {"name": "Elin Bergström", "date": "Idag", "rating": 5, "comment": "Helt magisk paj! Det knäckiga täcket i kombination med vaniljsåsen är ren perfektion.", "verified": True},
            {"name": "Johan Lind", "date": "Igår", "rating": 5, "comment": "Bästa äppelpajen jag någonsin bakat. Barnen slukade hela formen!", "verified": True}
        ]
    },
    {
        "slug": "klassisk-korv-stroganoff-ris",
        "file": "klassisk-korv-stroganoff-ris.html",
        "img": "korvstroganoff",
        "title": "Klassisk Korv Stroganoff – Krämigt Recept med Falukorv & Ris",
        "card_title": "Klassisk Korv Stroganoff",
        "sub": "Krämig tomatsås, senap & svensk falukorv",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Mycket enkel",
        "time": 25,
        "prep_time": "PT10M",
        "cook_time": "PT15M",
        "total_time": "PT25M",
        "prep_time_str": "10 min",
        "cook_time_str": "15 min",
        "time_str": "25 min",
        "calories": 540,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.96,
        "review_count": 520,
        "desc": "Sveriges mest älskade vardagsmiddag. Krämig och smakrik Korv Stroganoff gjord på svensk kvalitetsfalukorv, gul lök, tomatpuré, dijonsenap och vispgrädde.",
        "long_desc": "En tidlös svensk vardagsfavorit som går blixtsnabbt att laga. Hemligheten bakom den fylliga smaken är att steka tomatpurén med löken och tillsätta en klick dijonsenap.",
        "keywords": "korvstroganoff, korv stroganoff recept, falukorv recept, klassisk korv stroganoff med grädde, snabb vardagsmat",
        "alt": "Närbild på krämig korv stroganoff med stekta falukorvsstrimlor i fyllig orange sås med ris och persilja",
        "equipment": ["Rymlig stekpanna / traktörpanna", "Kastrull för ris", "Skärbräda & kockkniv"],
        "drink_pairing": "Ett glas kall svensk lättöl, mineralvatten med citron eller ett lättare rött vin.",
        "ingredients": [
            {"group": "Korv Stroganoff", "items": [
                {"val": 600, "unit": "g", "name": "svensk falukorv med hög kötthalt"},
                {"val": 1, "unit": "st", "name": "stor gul lök (finhackad)"},
                {"val": 2, "unit": "msk", "name": "smör (att steka i)"},
                {"val": 3, "unit": "msk", "name": "tomatpuré (koncentrerad)"},
                {"val": 1, "unit": "msk", "name": "dijonsenap eller skånsk senap"},
                {"val": 1, "unit": "msk", "name": "kalvfond eller oxfond"},
                {"val": 3, "unit": "dl", "name": "vispgrädde eller matlagningsgrädde"},
                {"val": 1, "unit": "dl", "name": "mjölk"},
                {"val": 1, "unit": "tsk", "name": "soja (kinesisk)"},
                {"val": 0.5, "unit": "tsk", "name": "paprikapulver"},
                {"val": 1, "unit": "krm", "name": "nymalen svartpeppar & salt"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "portioner", "name": "kokt jasmin- eller basmatiris"},
                {"val": 2, "unit": "msk", "name": "färsk bladpersilja (finhackad)"},
                {"val": 1, "unit": "burk", "name": "saltgurka eller pressgurka"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Strimla korv & hacka lök", "text": "Dra skinnet av falukorven och skär den i jämna strimlor (ca 1 cm tjocka). Skala och finhacka den gula löken.", "timer": 5},
            {"step": 2, "title": "Bryn korven gyllene", "text": "Hetta upp smör i en stor stekpanna. Stek korvstrimlorna på medelhög värme i 4–5 minuter tills de fått fin gyllenbrun stekyta. Lyft ur eller skjut åt sidan.", "timer": 5},
            {"step": 3, "title": "Fräs lök & tomatpuré", "text": "Tillsätt den hackade löken och fräs i 2 minuter tills den blir mjuk och glansig. Klicka i tomatpurén och paprikapulvret och låt fräsa med i 1 minut för att få fram sötman och djupet.", "timer": 3},
            {"step": 4, "title": "Tillsätt grädde, senap & fond", "text": "Häll i grädde, mjölk, kalvfond, dijonsenap och soja. Rör om ordentligt så allt blandas till en fyllig sås.", "timer": 2},
            {"step": 5, "title": "Låt sjuda till krämig perfektion", "text": "Låt Stroganoffen småputtra på medellåg värme i 7–10 minuter tills såsen tjocknat och smakerna kokat ihop.", "timer": 8},
            {"step": 6, "title": "Garnera och servera", "text": "Smaka av med salt och svartpeppar. Strö över rikligt med hackad persilja och servera med nykokt fluffigt ris och krispig saltgurka.", "timer": None}
        ],
        "pro_tips": "Stek tomatpurén tillsammans med löken i 1 minut innan du häller på grädden. Det tar bort rå syrlighet och ger såsen en fantastisk, rund umamismak.",
        "nutrition": {"calories": "540 kcal", "protein": "21g", "carbs": "32g", "fat": "38g", "sugar": "6g"},
        "faqs": [
            {"q": "Kan man göra Korv Stroganoff med crème fraiche?", "a": "Ja, du kan byta ut hälften av grädden mot crème fraiche för en god, frisk syrlighet i såsen."},
            {"q": "Vilken korv ska man använda?", "a": "Välj en svensk falukorv med minst 65-70% kötthalt för bäst smak, konsistens och saftighet."}
        ],
        "community_reviews": [
            {"name": "Marcus Holmberg", "date": "Idag", "rating": 5, "comment": "Bästa stroganoffen på nätet! Dijonsenapen och att fräsa tomatpurén gjorde enorm skillnad.", "verified": True}
        ]
    },
    {
        "slug": "frasig-flaskpannkaka-langpanna",
        "file": "frasig-flaskpannkaka-langpanna.html",
        "img": "flaskpannkaka",
        "title": "Frasig Fläskpannkaka i Långpanna – Gammaldags Recept med Fläsk",
        "card_title": "Frasig Fläskpannkaka",
        "sub": "Puffig ugnspannkaka med rökt sidfläsk & lingon",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Enkel",
        "time": 40,
        "prep_time": "PT10M",
        "cook_time": "PT30M",
        "total_time": "PT40M",
        "prep_time_str": "10 min",
        "cook_time_str": "30 min",
        "time_str": "40 min",
        "calories": 580,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.97,
        "review_count": 395,
        "desc": "Klassisk svensk fläskpannkaka i långpanna. Hög, fluffig och med härligt frasiga gyllenbruna kanter, fylld med nystekt rimmat sidfläsk och serverad med rårörda lingon.",
        "long_desc": "En älskad svensk klassiker som mättar hela familjen. Pannkakssmeten gräddas direkt i långpannan tillsammans med det heta fläskfettet, vilket ger den karakteristiska puffiga höjden och de krispiga kanterna.",
        "keywords": "fläskpannkaka, ugnspannkaka, ugnspannkaka bacon, fläskpannkaka i långpanna recept, gammaldags fläskpannkaka",
        "alt": "Närbild på en tjock fluffig bit fläskpannkaka med knaprigt sidfläsk och glänsande röda rårörda lingon",
        "equipment": ["Långpanna (ca 30x40 cm)", "Vispskål & ballongvisp", "Stekpanna"],
        "drink_pairing": "Ett glas iskall mjölk eller en frisk svensk äppelmust.",
        "ingredients": [
            {"group": "Fläsk & Fett", "items": [
                {"val": 350, "unit": "g", "name": "rimmat eller rökt sidfläsk (eller tjockskuret bacon)"},
                {"val": 25, "unit": "g", "name": "smör (till långpannan)"}
            ]},
            {"group": "Pannkakssmet", "items": [
                {"val": 4, "unit": "st", "name": "stora ägg"},
                {"val": 8, "unit": "dl", "name": "standardmjölk (3%)"},
                {"val": 4, "unit": "dl", "name": "vetemjöl"},
                {"val": 0.5, "unit": "tsk", "name": "salt"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker (valfritt, lyfter smaken)"}
            ]},
            {"group": "Servering", "items": [
                {"val": 1, "unit": "skål", "name": "svenska rårörda lingon"},
                {"val": 1, "unit": "skål", "name": "krispig vitkålssallad"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ugn och fläsk", "text": "Sätt ugnen på 225°C. Tärna sidfläsket i ca 1 cm stora bitar. Stek fläsket lätt i en stekpanna så det släpper lite fett och får lätt färg.", "timer": 5},
            {"step": 2, "title": "Vispa smeten klumpfri", "text": "Vispa ihop vetemjöl, salt och hälften av mjölken till en helt slät smet utan klumpar. Tillsätt resten av mjölken och vispa sist i äggen ett i taget.", "timer": 5},
            {"step": 3, "title": "Värm långpannan med smör", "text": "Lägg smöret och det stekta fläsket med sitt fett i en långpanna. Sätt in i ugnen i 3 minuter tills smöret smält och pannan är riktigt het.", "timer": 3},
            {"step": 4, "title": "Häll i smeten", "text": "Ta försiktigt ut den heta långpannan och häll snabbt över pannkakssmeten. Fördela fläsket jämnt.", "timer": 1},
            {"step": 5, "title": "Grädda gyllene & puffig", "text": "Grädda mitt i ugnen i 25–30 minuter utan att öppna ugnsluckan de första 20 minuterna, tills pannkakan rest sig högt och blivit härligt gyllenbrun och frasig.", "timer": 25},
            {"step": 6, "title": "Skär upp och njut", "text": "Låt stå i 3 minuter. Skär i generösa rutor och servera genast med massor av rårörda lingon.", "timer": None}
        ],
        "pro_tips": "Se till att långpannan med smör och fläskfett är rykande het när du häller i smeten. Det är temperaturchocken som gör att pannkakan puffar upp och får underbart krispiga kanter.",
        "nutrition": {"calories": "580 kcal", "protein": "26g", "carbs": "44g", "fat": "34g", "sugar": "7g"},
        "faqs": [
            {"q": "Varför sjunker fläskpannkakan ihop när den tas ur ugnen?", "a": "Det är helt naturligt! Fläskpannkaka puffar upp av ångan i ugnen och sätter sig till en härligt saftig och krämig textur när den svalnar något."},
            {"q": "Kan man byta sidfläsk mot bacon?", "a": "Ja, bacon fungerar utmärkt. Välj gärna tjockskivat bacon för bäst tuggmotstånd och smak."}
        ],
        "community_reviews": [
            {"name": "Gunilla Pettersson", "date": "Idag", "rating": 5, "comment": "Perfekt frasiga kanter och supergod! Påminner precis om mammas söndagsmiddagar.", "verified": True}
        ]
    },
    {
        "slug": "kramig-kantarellpaj-vasterbottensost",
        "file": "kramig-kantarellpaj-vasterbottensost.html",
        "img": "kantarellpaj",
        "title": "Krämig Kantarellpaj med Västerbottensost & Färsk Timjan",
        "card_title": "Krämig Kantarellpaj",
        "sub": "Gula skogskantareller & lagrad Västerbottensost",
        "category": "Högtider & Smörgåsbord",
        "cat_slug": "hogtider-och-smorgasbord",
        "cat_key": "smorgasbord",
        "diet": "Vegetariskt",
        "difficulty": "Medel",
        "time": 55,
        "prep_time": "PT25M",
        "cook_time": "PT30M",
        "total_time": "PT55M",
        "prep_time_str": "25 min",
        "cook_time_str": "30 min",
        "time_str": "55 min",
        "calories": 460,
        "portions_num": 8,
        "portions_unit": "bitar",
        "rating": 4.98,
        "review_count": 310,
        "desc": "Festens höjdpunkt under svampsäsongen och kräftskivan. Smörstekt pajskal fyllt med nystekta gula skogskantareller, lagrad Västerbottensost, schalottenlök och färsk timjan.",
        "long_desc": "Skogens guld möter Västerbottensost i en oslagbar smakkombination. Perfekt som huvudrätt till höstmiddagen, på kräftskivan eller som lyxig lunch med en krispig grönsallad.",
        "keywords": "kantarellpaj, kantarellpaj med västerbottensost, svamppaj, kräftskiva paj, bästa kantarellpajen",
        "alt": "Närbild på en bit krämig kantarellpaj med smältande Västerbottensost och guldgula stekta kantareller på tallrik",
        "equipment": ["Pajform med löstagbar botten (24 cm)", "Stekpanna", "Kavel & plastfolie"],
        "drink_pairing": "Ett fylligt ekfatslagrat vitt vin (Chardonnay), ett friskt ljust öl eller torr äppelcider.",
        "ingredients": [
            {"group": "Frasig Pajdeg", "items": [
                {"val": 3, "unit": "dl", "name": "vetemjöl"},
                {"val": 125, "unit": "g", "name": "kallt smör (i tärningar)"},
                {"val": 2, "unit": "msk", "name": "iskallt vatten"},
                {"val": 0.5, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Kantarellfyllning", "items": [
                {"val": 500, "unit": "g", "name": "färska gula kantareller (rensade)"},
                {"val": 2, "unit": "st", "name": "schalottenlökar (finhackade)"},
                {"val": 1, "unit": "klyfta", "name": "vitlök (finriven)"},
                {"val": 2, "unit": "msk", "name": "smör (att smörsteka i)"},
                {"val": 1, "unit": "msk", "name": "färsk timjan (hackad)"},
                {"val": 0.5, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Ost- & Äggstanning", "items": [
                {"val": 200, "unit": "g", "name": "lagrad Västerbottensost (grovriven)"},
                {"val": 3, "unit": "st", "name": "stora ägg"},
                {"val": 2, "unit": "dl", "name": "vispgrädde"},
                {"val": 1, "unit": "dl", "name": "standardmjölk"},
                {"val": 1, "unit": "krm", "name": "riven muskotnöt"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Gör pajdegen & kyl", "text": "Nyp snabbt ihop mjöl, salt och kallt tärnat smör för hand eller i matberedare till en smulig massa. Tillsätt kallt vatten och arbeta snabbt ihop till en deg. Tryck ut i en pajform (24 cm), nagga botten med gaffel och ställ i kylen i 30 minuter.", "timer": 15},
            {"step": 2, "title": "Förgrädda pajskalet", "text": "Sätt ugnen på 200°C. Förgrädda pajskalet mitt i ugnen i ca 10–12 minuter tills det fått lite färg.", "timer": 10},
            {"step": 3, "title": "Svetta kantarellerna", "text": "Lägg kantarellerna i en torr stekpanna på medelvärme. Låt vätskan koka in. Tillsätt sedan smör, finhackad schalottenlök, vitlök och timjan. Stek gyllene i 4–5 minuter. Salta och peppra.", "timer": 8},
            {"step": 4, "title": "Vispa äggstanningen", "text": "Vispa ihop ägg, grädde, mjölk, lite salt, svartpeppar och en nypa riven muskotnöt i en skål.", "timer": 3},
            {"step": 5, "title": "Montera pajen", "text": "Fördela den rivna Västerbottensosten och de smörstekta kantarellerna (spara några fina svampar till toppen) i det förgräddade pajskalet. Häll över äggstanningen.", "timer": 3},
            {"step": 6, "title": "Grädda gyllenbrun & krämig", "text": "Grädda mitt i ugnen i 25–30 minuter tills äggstanningen stannat och pajen fått en gyllenbrun vacker yta. Låt sätta sig i 15 minuter innan servering.", "timer": 25}
        ],
        "pro_tips": "Koka först ur vätskan ur kantarellerna i en torr panna innan du tillsätter smöret. Då blir svampen krispig och behåller all sin koncentrerade skogssmak.",
        "nutrition": {"calories": "460 kcal", "protein": "18g", "carbs": "22g", "fat": "34g", "sugar": "3g"},
        "faqs": [
            {"q": "Kan man använda frysta eller torkade kantareller?", "a": "Ja, absolut! Frysta kantareller tinas och kramas ur noga. Torkade kantareller blötläggs i ljummet vatten i 30 minuter och steks sedan som vanligt."},
            {"q": "Kan pajen förberedas dagen innan?", "a": "Ja, kantarellpaj är utmärkt att baka dagen innan. Värm den lätt i ugnen på 150°C före servering så blir den som nygräddad."}
        ],
        "community_reviews": [
            {"name": "Karin Lindell", "date": "Idag", "rating": 5, "comment": "Underbar paj till kräftskivan! Västerbottensosten och timjanen lyfte kantarellerna till skyarna.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-kalpudding-sirap-lingon",
        "file": "klassisk-kalpudding-sirap-lingon.html",
        "img": "kalpudding",
        "title": "Klassisk Kålpudding med Sirap, Gräddsås & Potatismos",
        "card_title": "Klassisk Kålpudding",
        "sub": "Smörstekt sirapsglaserad vitkål & saftig färs",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 65,
        "prep_time": "PT25M",
        "cook_time": "PT40M",
        "total_time": "PT65M",
        "prep_time_str": "25 min",
        "cook_time_str": "40 min",
        "time_str": "65 min",
        "calories": 520,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 440,
        "desc": "En av Sveriges mest ikoniska husmansrätter. Saftig blandfärs varvad med smörstekt, mörk sirapsglaserad vitkål, serverad med krämigt potatismos, rårörda lingon och gräddsås.",
        "long_desc": "Gammaldags svensk kålpudding när den är som allra godast. Hemligheten ligger i att bryna vitkålen långsamt i rikligt med smör och mörk sirap innan den gräddas i ugnen tillsammans med den saftiga färsen och kalvbuljongen.",
        "keywords": "kålpudding, kålpudding recept, klassisk kålpudding med sirap, gammaldags kålpudding, kålmaja, bästa kålpuddingen",
        "alt": "Närbild på en saftig bit kålpudding med karamelliserad gyllenbrun vitkål, fluffigt potatismos och glänsande lingon",
        "equipment": ["Ugnsfast form (ca 20x30 cm)", "Stor stekpanna / stekgryta", "Skål för färs"],
        "drink_pairing": "Ett fylligt svenskt mellanöl eller ett fruktigt rött vin från Côtes du Rhône.",
        "ingredients": [
            {"group": "Kål & Karamellisering", "items": [
                {"val": 1000, "unit": "g", "name": "vitkål (strimlad i ca 2 cm bitar)"},
                {"val": 4, "unit": "msk", "name": "smör (att steka i)"},
                {"val": 3, "unit": "msk", "name": "mörk sirap"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen vitpeppar"}
            ]},
            {"group": "Färsblandning", "items": [
                {"val": 600, "unit": "g", "name": "blandfärs (nöt och fläsk för saftighet)"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad och mjukstekt)"},
                {"val": 1, "unit": "st", "name": "stort ägg"},
                {"val": 1, "unit": "dl", "name": "mjölk"},
                {"val": 0.5, "unit": "dl", "name": "ströbröd"},
                {"val": 2, "unit": "msk", "name": "koncentrerad kalvfond"},
                {"val": 1.5, "unit": "tsk", "name": "salt"},
                {"val": 0.5, "unit": "tsk", "name": "nymalen kryddpeppar"},
                {"val": 2, "unit": "dl", "name": "vatten eller kalvbuljong (att hälla runt formen)"}
            ]},
            {"group": "Servering", "items": [
                {"val": 6, "unit": "portioner", "name": "hemlagat potatismos med smör och mjölk"},
                {"val": 1, "unit": "skål", "name": "svenska rårörda lingon"},
                {"val": 1, "unit": "såskopp", "name": "klassisk svensk gräddsås"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ströbröd & ugn", "text": "Sätt ugnen på 180°C varmluft (eller 200°C över-/undervärme). Blanda ströbröd, mjölk och kalvfond i en skål och låt svälla i 10 minuter.", "timer": 10},
            {"step": 2, "title": "Bryn vitkålen med sirap", "text": "Strimla kålen. Hetta upp smöret i en stor stekpanna och stek kålen i omgångar på medelvärme tills den mjuknar och krymper. Ringla över sirap, salta och peppra och stek ytterligare 5 minuter tills kålen är vackert gyllenbrun.", "timer": 15},
            {"step": 3, "title": "Blanda färsen", "text": "Blanda färsen med den svällda ströbrödsblandningen, stekt finhackad lök, ägg, salt och kryddpeppar till en smidig och saftig färssmet.", "timer": 5},
            {"step": 4, "title": "Varva i formen", "text": "Smörj en ugnsform. Lägg hälften av den sirapsstekta kålen i botten. Bred ut färsen jämnt ovanpå. Täck med resten av kålen och ringla eventuellt lite extra sirap på toppen.", "timer": 5},
            {"step": 5, "title": "Grädda i ugnen", "text": "Häll 2 dl buljong runt kanterna i formen. Grädda mitt i ugnen i 40–45 minuter tills kålpuddingen fått en mörk karamelliserad yta och köttet är helt genomstekt (innertemp 72°C).", "timer": 40},
            {"step": 6, "title": "Vila och servera", "text": "Låt kålpuddingen vila i 10 minuter före uppskärning så att skyn sätter sig. Servera i rejäla rutor med potatismos, lingon och gräddsås gjord på stekskyn.", "timer": 10}
        ],
        "pro_tips": "Sila av den fantastiska stekskyn från ugnsformen efter gräddning och koka upp den med 1.5 dl vispgrädde och lite soja – det blir världens godaste gräddsås.",
        "nutrition": {"calories": "520 kcal", "protein": "28g", "carbs": "36g", "fat": "32g", "sugar": "14g"},
        "faqs": [
            {"q": "Varför blir kålpuddingen torr?", "a": "Använd blandfärs istället för ren nötfärs, och se till att hälla 2 dl buljong i formen under gräddningen så hålls färsen extremt saftig."},
            {"q": "Kan man frysa in kålpudding?", "a": "Ja, kålpudding är perfekt att frysa i portionsbitar och värms bäst i ugn med lite extra smör eller grädde på toppen."}
        ],
        "community_reviews": [
            {"name": "Birgitta Sandström", "date": "Idag", "rating": 5, "comment": "Bästa kålpuddingen jag ätit! Att använda stekskyn till gräddsåsen var ett genidrag.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-ungersk-gulaschsoppa-hogrev",
        "file": "klassisk-ungersk-gulaschsoppa-hogrev.html",
        "img": "gulaschsoppa",
        "title": "Klassisk Gulaschsoppa – Mustigt Recept på Högrev & Paprika",
        "card_title": "Klassisk Gulaschsoppa",
        "sub": "Mört högrev, ungersk paprika, potatis & gräddfil",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 75,
        "prep_time": "PT20M",
        "cook_time": "PT55M",
        "total_time": "PT75M",
        "prep_time_str": "20 min",
        "cook_time_str": "55 min",
        "time_str": "75 min",
        "calories": 460,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 510,
        "desc": "En värmande, mustig och smakrik gulaschsoppa med mört långkokt svenskt högrev, potatis, spetspaprika, kummin och äkta ungerskt paprikapulver. Serveras med en klick sval gräddfil.",
        "long_desc": "Den ultimata höst- och vintersoppan. Gulaschsoppan får sin unika djupa smak genom att steka högrevet med lök, krossad kummin, vitlök och rikligt med paprikapulver innan den sjuds till perfektion.",
        "keywords": "gulaschsoppa, gulaschsoppa recept, ungersk gulaschsoppa, gulasch på högrev, mustig gulaschsoppa med köttfärs eller högrev",
        "alt": "Rykande het röd gulaschsoppa i mörk keramikskål med mört högrev, potatis, paprika, kummin och en klick vit gräddfil",
        "equipment": ["Tjockbottnad gjutjärnsgryta", "Skärbräda & vass kockkniv", "Träslev"],
        "drink_pairing": "Ett fylligt ungerskt rödvin (Egri Bikavér), en kall tjeckisk pilsner eller mustig äppelmust.",
        "ingredients": [
            {"group": "Kött & Grund", "items": [
                {"val": 700, "unit": "g", "name": "nöthögrev (skuret i fina 1.5 cm kuber)"},
                {"val": 2, "unit": "st", "name": "gula lökar (finhackade)"},
                {"val": 3, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 2, "unit": "msk", "name": "smör eller olja (att bryna i)"},
                {"val": 3, "unit": "msk", "name": "äkta paprikapulver (sött & rökt)"},
                {"val": 1, "unit": "tsk", "name": "hel kummin (nymortlad)"},
                {"val": 3, "unit": "msk", "name": "tomatpuré"}
            ]},
            {"group": "Grönsaker & Buljong", "items": [
                {"val": 4, "unit": "st", "name": "fasta potatisar (tärnade i 1.5 cm bitar)"},
                {"val": 2, "unit": "st", "name": "röda spetspaprikor (tärnade)"},
                {"val": 2, "unit": "st", "name": "morötter (tärnade)"},
                {"val": 12, "unit": "dl", "name": "vatten + 3 msk oxfond (eller köttbuljong)"},
                {"val": 1, "unit": "burk", "name": "krossade tomater (400g av god kvalitet)"},
                {"val": 2, "unit": "st", "name": "lagerblad"},
                {"val": 1.5, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 2, "unit": "dl", "name": "gräddfil eller crème fraiche"},
                {"val": 1, "unit": "kruka", "name": "färsk bladpersilja (hackad)"},
                {"val": 6, "unit": "skivor", "name": "nybakat surdegsbröd med smör"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Bryn högrevet", "text": "Skär högrevet i ca 1.5 cm små tärningar. Hetta upp smör i en gjutjärnsgryta och bryn köttet i omgångar på hög värme så det får fin färg.", "timer": 8},
            {"step": 2, "title": "Fräs lök, vitlök och kryddor", "text": "Sänk värmen något och tillsätt lök och vitlök. Fräs tills löken är mjuk. Rör i tomatpuré, nymortlad kummin och paprikapulver. Låt fräsa med under omrörning i 1 minut så kryddorna vaknar till liv.", "timer": 4},
            {"step": 3, "title": "Koka köttet mört", "text": "Häll i buljong, krossade tomater och lagerblad. Koka upp, sätt på locket och låt sjuda på svag värme i ca 45–50 minuter tills köttbitarna börjar bli riktigt möra.", "timer": 45},
            {"step": 4, "title": "Tillsätt potatis och paprika", "text": "Tillsätt tärnad potatis, morötter och paprika. Låt sjuda ytterligare 15–20 minuter tills potatisen är genomkokt och soppan blivit fyllig och mustig.", "timer": 15},
            {"step": 5, "title": "Smaka av & servera", "text": "Smaka av med salt, svartpeppar och eventuellt en nypa cayennepeppar för extra hetta. Ta ur lagerbladen.", "timer": 3},
            {"step": 6, "title": "Toppa och njut", "text": "Ös upp den rykande heta soppan i skålar. Toppa med en rejäl klick sval gräddfil, hackad persilja och servera med ett gott bröd.", "timer": None}
        ],
        "pro_tips": "Mortla hel kummin (inte spiskummin!) och fräs den tillsammans med paprikapulvret och tomatpurén i smöret. Det är den autentiska hemligheten som ger ungersk gulasch sin karaktäristiska mustighet.",
        "nutrition": {"calories": "460 kcal", "protein": "34g", "carbs": "38g", "fat": "18g", "sugar": "8g"},
        "faqs": [
            {"q": "Kan man göra gulaschsoppa på köttfärs?", "a": "Ja, absolut! Byt ut högrevet mot 500g nötfärs. Då kortas koktiden ner till bara 25 minuter och blir en perfekt snabb vardagssoppa."},
            {"q": "Vilken kummin ska man använda?", "a": "Använd vanlig brödkummin (Caraway på engelska), inte spiskummin (Cumin). Kummin ger den traditionella europeiska gulaschsmaken."}
        ],
        "community_reviews": [
            {"name": "Henrik Åkesson", "date": "Idag", "rating": 5, "comment": "Helt otroligt god soppa! Köttet blev så mört och buljongen har ett fantastiskt djup.", "verified": True}
        ]
    },
    {
        "slug": "kramig-fisksoppa-saffran-rakor",
        "file": "kramig-fisksoppa-saffran-rakor.html",
        "img": "fisksoppa",
        "title": "Krämig Fisksoppa med Saffran, Torsk, Lax & Handskalade Räkor",
        "card_title": "Krämig Fisksoppa med Saffran",
        "sub": "Lax, torsk, fänkål, handskalade räkor & vitlöksaioli",
        "category": "Högtider & Smörgåsbord",
        "cat_slug": "hogtider-och-smorgasbord",
        "cat_key": "smorgasbord",
        "diet": "Fisk & Skaldjur",
        "difficulty": "Enkel",
        "time": 35,
        "prep_time": "PT15M",
        "cook_time": "PT20M",
        "total_time": "PT35M",
        "prep_time_str": "15 min",
        "cook_time_str": "20 min",
        "time_str": "35 min",
        "calories": 480,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 580,
        "desc": "En lyxig och krämig fisksoppa med gyllene saffran, vitt vin, färsk fänkål, purjolök, torskrygg, lax och handskalade räkor. Serveras med hemgjord vitlöksaioli.",
        "long_desc": "Sveriges mest populära fisksoppa med inspiration från den franska bouillabaissen och västkustens finaste råvaror. Gyllengul, silkeslen och fylld med färsk fisk och skaldjur.",
        "keywords": "fisksoppa, fisksoppa saffran, fisksoppa recept, krämig fisksoppa med räkor och dill, lyxig fisksoppa med aioli",
        "alt": "Närbild på en gyllengul krämig saffransfisksoppa i vit skål med lax, torsk, räkor, dill och en klick hemgjord aioli",
        "equipment": ["Rymlig kastrull / soppgryta", "Skärbräda & kockkniv", "Skål för aioli"],
        "drink_pairing": "Ett krispigt mineraliskt vitt vin som Chablis, Sauvignon Blanc eller ett torrt mousserande vin.",
        "ingredients": [
            {"group": "Fisk & Skaldjur", "items": [
                {"val": 350, "unit": "g", "name": "färsk laxfilé (i 3 cm kuber)"},
                {"val": 350, "unit": "g", "name": "färsk torskrygg eller kolja (i 3 cm kuber)"},
                {"val": 300, "unit": "g", "name": "handskalade räkor (i lag eller färska)"}
            ]},
            {"group": "Saffransbas & Grönsaker", "items": [
                {"val": 0.5, "unit": "g", "name": "saffran (1 kuvert stöttes med lite socker)"},
                {"val": 1, "unit": "st", "name": "fänkål (strimlad)"},
                {"val": 1, "unit": "st", "name": "purjolök (ansad och skivad)"},
                {"val": 2, "unit": "st", "name": "morötter (i tunna slantar)"},
                {"val": 2, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 2, "unit": "msk", "name": "smör (att fräsa i)"},
                {"val": 2, "unit": "dl", "name": "torrt vitt vin"},
                {"val": 5, "unit": "dl", "name": "vatten + 3 msk hummer- eller fiskfond"},
                {"val": 3, "unit": "dl", "name": "vispgrädde"},
                {"val": 1, "unit": "dl", "name": "crème fraiche"},
                {"val": 1, "unit": "kruka", "name": "färsk dill (fint hackad)"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen vitpeppar"}
            ]},
            {"group": "Hemgjord Vitlöksaioli", "items": [
                {"val": 1, "unit": "dl", "name": "god majonnäs"},
                {"val": 1, "unit": "klyfta", "name": "vitlök (riven)"},
                {"val": 1, "unit": "tsk", "name": "citronsaft & nypa flingsalt"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Fräs grönsaker och saffran", "text": "Hetta upp smör i en stor soppgryta. Fräs strimlad fänkål, purjolök, morot och vitlök tillsammans med saffran på medelvärme i 4–5 minuter tills grönsakerna mjuknat och fått en intensiv saffransfärg.", "timer": 5},
            {"step": 2, "title": "Koka soppbasen med vin & grädde", "text": "Häll i det vita vinet och låt koka in i 2 minuter. Tillsätt vatten, fiskfond, vispgrädde och crème fraiche. Låt soppan sjuda på svag värme i ca 10 minuter så smakerna förenas.", "timer": 10},
            {"step": 3, "title": "Pochera fisken försiktigt", "text": "Skär lax och torsk i ca 3 cm stora kuber. Sänk värmen på soppan till lägsta så den bara sjuder mycket lätt. Lägg försiktigt i fiskbitarna och låt dem sjuda i 4–5 minuter utan att röra för kraftigt.", "timer": 5},
            {"step": 4, "title": "Rör ihop snabb aioli", "text": "Blanda majonnäs med riven vitlök, citronsaft och en nypa salt i en liten skål.", "timer": 2},
            {"step": 5, "title": "Tillsätt dill och räkor", "text": "Dra grytan från värmen. Rör ner den hackade dillen och toppa med de handskalade räkorna (de ska bara bli varma och får inte koka, då blir de sega).", "timer": 2},
            {"step": 6, "title": "Servera med aioli och bröd", "text": "Ös upp den rykande heta gyllene soppan i djupa tallrikar. Klicka i en sked aioli i mitten och servera genast med gott bröd.", "timer": None}
        ],
        "pro_tips": "Koka aldrig räkorna! Lägg alltid i de handskalade räkorna allra sist precis när soppan lyfts från plattan. Då behåller de sin saftighet och perfekta spänst.",
        "nutrition": {"calories": "480 kcal", "protein": "38g", "carbs": "12g", "fat": "30g", "sugar": "5g"},
        "faqs": [
            {"q": "Kan man använda fryst fisk?", "a": "Ja, tinad torsk och lax i block fungerar bra, men färsk fiskrygg ger fastare och godare bitar som inte faller isär i soppan."},
            {"q": "Kan vinet uteslutas?", "a": "Ja, ersätt vitt vin med 2 msk färskpressad citronsaft och 1.5 dl extra vatten/buljong för att behålla den friska syran."}
        ],
        "community_reviews": [
            {"name": "Cecilia Wahlström", "date": "Idag", "rating": 5, "comment": "Restaurangklass! Saffranssmaken och fänkålen tillsammans med aiolin är helt magiskt god.", "verified": True}
        ]
    },
    {
        "slug": "mustig-hogrevsgryta-rodvin-svamp",
        "file": "mustig-hogrevsgryta-rodvin-svamp.html",
        "img": "hogrevsgryta",
        "title": "Mustig Högrevsgryta med Rödvin, Sidfläsk & Smålökar",
        "card_title": "Mustig Högrevsgryta",
        "sub": "Långkokt högrev i fyllig rödvinsreduktion med svamp",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 110,
        "prep_time": "PT20M",
        "cook_time": "PT90M",
        "total_time": "PT110M",
        "prep_time_str": "20 min",
        "cook_time_str": "90 min",
        "time_str": "1 tim 50 min",
        "calories": 560,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 490,
        "desc": "En genuin höst- och vintergryta på svenskt marmorerat högrev. Långkokt i fylligt rödvin med krispigt rökt sidfläsk, steklökar, skogschampinjoner och färsk timjan.",
        "long_desc": "Den perfekta helgmiddagen när löven faller. Köttet bryns omsorgsfullt och får sedan koka långsamt i en mörk, fyllig rödvinsbuljong tills det är så mört att det faller isär vid beröring.",
        "keywords": "högrevsgryta, köttgryta, mustig köttgryta med rödvin, gryta på högrev, långkok högrev, boeuf bourguignon svensk",
        "alt": "Närbild på en mustig mörk högrevsgryta i gjutjärnspanna med mört kött, glaserade steklökar, champinjoner och timjan",
        "equipment": ["Gjutjärnsgryta med lock", "Stekpanna", "Skärbräda & kockkniv"],
        "drink_pairing": "Ett kraftfullt och kryddigt rött vin, exempelvis en fyllig Syrah, Cabernet Sauvignon eller Ripasso.",
        "ingredients": [
            {"group": "Högrev & Grytbas", "items": [
                {"val": 900, "unit": "g", "name": "svenskt nöthögrev (i 3-4 cm stora bitar)"},
                {"val": 150, "unit": "g", "name": "rökt sidfläsk eller bacon (strimlat)"},
                {"val": 2, "unit": "msk", "name": "smör och 1 msk rapsolja"},
                {"val": 2, "unit": "msk", "name": "vetemjöl"},
                {"val": 2, "unit": "msk", "name": "tomatpuré"},
                {"val": 4, "unit": "dl", "name": "fylligt rött vin"},
                {"val": 5, "unit": "dl", "name": "vatten + 3 msk oxfond"},
                {"val": 3, "unit": "klyftor", "name": "vitlök (krossade)"},
                {"val": 3, "unit": "st", "name": "lagerblad & 4 kvistar färsk timjan"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Garnityr (Steks mot slutet)", "items": [
                {"val": 250, "unit": "g", "name": "färska skogschampinjoner (delade i kvartar)"},
                {"val": 12, "unit": "st", "name": "små steklökar eller pärllökar (skalade)"},
                {"val": 2, "unit": "st", "name": "morötter (i grova slantar)"},
                {"val": 1, "unit": "msk", "name": "smör (att steka garnityret i)"}
            ]},
            {"group": "Servering", "items": [
                {"val": 6, "unit": "portioner", "name": "krämigt potatismos med parmesan eller kokt mandelpotatis"},
                {"val": 1, "unit": "skål", "name": "svenska rårörda lingon eller gelé"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Stek fläsket & bryn köttet", "text": "Strimla sidfläsket och stek det knaprigt i en gjutjärnsgryta. Lyft ur fläsket men lämna fettet kvar. Tillsätt smör och bryn de stora högrevsbitarna i omgångar på hög värme så de får djup mörk stekyta runt om.", "timer": 10},
            {"step": 2, "title": "Pudra med mjöl & tillsätt tomatpuré", "text": "Lägg tillbaka allt kött och fläsk i grytan. Tillsätt tomatpuré och krossad vitlök och fräs 1 minut. Pudra över vetemjölet och rör om noga.", "timer": 3},
            {"step": 3, "title": "Häll i rödvin och buljong", "text": "Häll i rödvin, vatten, oxfond, lagerblad och timjankvistar. Salta och peppra. Koka upp under omrörning så mjölet löser sig.", "timer": 5},
            {"step": 4, "title": "Långkok på svag värme", "text": "Lägg på locket, sänk värmen och låt grytan småputtra mycket sakta i ca 1 timme och 15 minuter. Köttet ska bli otroligt mört.", "timer": 75},
            {"step": 5, "title": "Stek svamp, lök och morötter", "text": "Stek under tiden champinjoner, skalade steklökar och morötter i smör i en separat panna tills de fått fin färg. Tillsätt dem i grytan när 20 minuter återstår av koktiden.", "timer": 20},
            {"step": 6, "title": "Smaka av och servera", "text": "Smaka av såsen med salt, peppar och eventuellt en skvätt svartvinbärsgelé. Garnera med färsk timjan och servera med ett lyxigt potatismos.", "timer": None}
        ],
        "pro_tips": "Stek svampen och steklökarna separat och tillsätt dem först under de sista 20 minuterna av koktiden. Då behåller svampen sin spänst och lökarna blir söta och hela istället för att koka sönder.",
        "nutrition": {"calories": "560 kcal", "protein": "44g", "carbs": "16g", "fat": "32g", "sugar": "5g"},
        "faqs": [
            {"q": "Vilket rött vin passar bäst i köttgryta?", "a": "Ett torrt, fylligt rött vin med bra fruktighet (t.ex. Syrah, Zinfandel eller Côtes du Rhône). Undvik viner med för mycket ekfatstoner eller hög syra."},
            {"q": "Kan grytan lagas i förväg?", "a": "Ja! Mustiga grytor som denna smakar till och med ännu bättre dagen efter då köttet och smakerna dragit åt sig all mustighet från vinet."}
        ],
        "community_reviews": [
            {"name": "Fredrik Lind", "date": "Idag", "rating": 5, "comment": "Den ultimata höstgrytan. Såsen är så fyllig och köttet föll bokstavligen isär. 10/10!", "verified": True}
        ]
    },
    {
        "slug": "baconlindad-kottfarslimpa-graddsas",
        "file": "baconlindad-kottfarslimpa-graddsas.html",
        "img": "kottfarslimpa",
        "title": "Saftig Baconlindad Köttfärslimpa med Gräddsås & Pressgurka",
        "card_title": "Baconlindad Köttfärslimpa",
        "sub": "Saftig blandfärs i krispigt bacon med fyllig gräddsås",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 60,
        "prep_time": "PT20M",
        "cook_time": "PT40M",
        "total_time": "PT60M",
        "prep_time_str": "20 min",
        "cook_time_str": "40 min",
        "time_str": "60 min",
        "calories": 580,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 480,
        "desc": "Klassisk svensk husmanskost när den är som allra godast. Extra saftig köttfärslimpa lindad i rökt bacon som ger en krispig, smakrik yta och håller färsen underbart mör. Serveras med hemlagad gräddsås, potatismos och pressgurka.",
        "long_desc": "En tidlös svensk middagsfavorit. Genom att fläta baconet runt köttfärslimpan kapslas all saftighet in samtidigt som det rökta baconfettet smälter ner och smaksätter både köttet och den oumbärliga skysåsen i ugnsformen.",
        "keywords": "köttfärslimpa, baconlindad köttfärslimpa, saftig köttfärslimpa, köttfärslimpa recept, köttfärslimpa med bacon och gräddsås",
        "alt": "Närbild på saftiga skivor baconlindad köttfärslimpa med krispig yta, fluffigt potatismos, gräddsås och lingon",
        "equipment": ["Ugnsform eller bakplåt", "Skål för färs", "Stekpanna till sås"],
        "drink_pairing": "En svensk lager, kall julmust/påskmust, eller ett bärigt rött vin som Pinot Noir.",
        "ingredients": [
            {"group": "Saftig Färssmet", "items": [
                {"val": 600, "unit": "g", "name": "blandfärs (nöt & gris för maximal saftighet)"},
                {"val": 2, "unit": "pkt", "name": "bacon (ca 280g, att linda limpan med)"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad & mjukstekt i smör)"},
                {"val": 1, "unit": "dl", "name": "mjölk eller vispgrädde"},
                {"val": 0.5, "unit": "dl", "name": "ströbröd"},
                {"val": 1, "unit": "st", "name": "stort ägg"},
                {"val": 2, "unit": "msk", "name": "koncentrerad kalvfond"},
                {"val": 1, "unit": "msk", "name": "dijonsenap"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Klassisk Gräddsås", "items": [
                {"val": 2, "unit": "dl", "name": "steksky från formen + vatten"},
                {"val": 3, "unit": "dl", "name": "vispgrädde"},
                {"val": 1.5, "unit": "msk", "name": "koncentrerad kalvfond"},
                {"val": 1, "unit": "msk", "name": "svartvinbärsgelé eller lingonsylt"},
                {"val": 1, "unit": "tsk", "name": "kinesisk soja (för färg & sälta)"},
                {"val": 1.5, "unit": "msk", "name": "vetemjöl eller maizena (till redning)"}
            ]},
            {"group": "Tillbehör", "items": [
                {"val": 6, "unit": "portioner", "name": "hemlagat potatismos med smör"},
                {"val": 1, "unit": "skål", "name": "svensk inlagd pressgurka & rårörda lingon"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Låt ströbrödet svälla & sätt ugnen", "text": "Sätt ugnen på 200°C över-/undervärme. Blanda ströbröd, mjölk, kalvfond och dijonsenap i en skål och låt svälla i 10 minuter.", "timer": 10},
            {"step": 2, "title": "Blanda färsen", "text": "Fräs finhackad lök mjuk i smör. Blanda färsen med ströbrödsblandningen, stekt lök, ägg, salt och peppar till en smidig smet (arbeta inte för länge då blir den kompakt).", "timer": 5},
            {"step": 3, "title": "Forma & linda med bacon", "text": "Forma färsen till en jämn limpa i en smord ugnsform. Täck limpan med baconskivor omlott så att hela ovansidan och sidorna är täckta.", "timer": 5},
            {"step": 4, "title": "Grädda i ugnen", "text": "Grädda mitt i ugnen i ca 40–45 minuter tills baconet är krispigt och gyllenbrunt och innertemperaturen i köttfärslimpan når 72°C.", "timer": 40},
            {"step": 5, "title": "Koka den fantastiska gräddsåsen", "text": "Häll av den smakrika stekskyn från ugnsformen ner i en kastrull. Tillsätt grädde, kalvfond, soja och gelé. Koka upp, red av till önskad krämig konsistens och låt sjuda i 3 minuter.", "timer": 5},
            {"step": 6, "title": "Skiva upp och servera", "text": "Låt köttfärslimpan vila i 10 minuter innan du skär upp den i tjocka saftiga skivor. Servera med rykande hett potatismos, gräddsås och pressgurka.", "timer": 10}
        ],
        "pro_tips": "Låt alltid köttfärslimpan vila i 10 minuter under folie innan du skär i den. Då stannar all köttsaft kvar i skivorna istället för att rinna ut på skärbrädan.",
        "nutrition": {"calories": "580 kcal", "protein": "36g", "carbs": "18g", "fat": "42g", "sugar": "4g"},
        "faqs": [
            {"q": "Hur vet jag när köttfärslimpan är klar?", "a": "Använd en digital stektermometer i mitten av limpan – vid 70–72°C är den perfekt saftig och genomstekt."},
            {"q": "Kan man fylla köttfärslimpan med ost?", "a": "Ja! Att rulla in smulad fetaost, soltorkade tomater eller riven Västerbottensost i mitten av limpan ger en fantastisk smakbrytning."}
        ],
        "community_reviews": [
            {"name": "Göran Pettersson", "date": "Idag", "rating": 5, "comment": "Den godaste köttfärslimpan jag gjort! Baconet gjorde den fantastiskt saftig och såsen blev magisk.", "verified": True}
        ]
    },
    {
        "slug": "fluffiga-amerikanska-pannkakor",
        "file": "fluffiga-amerikanska-pannkakor.html",
        "img": "amerikanskapannkakor",
        "title": "Fluffiga Amerikanska Pannkakor – Bästa & Enklaste Receptet",
        "card_title": "Amerikanska Pannkakor",
        "sub": "Extra tjocka, fluffiga pannkakor med smör & lönnsirap",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 20,
        "prep_time": "PT10M",
        "cook_time": "PT10M",
        "total_time": "PT20M",
        "prep_time_str": "10 min",
        "cook_time_str": "10 min",
        "time_str": "20 min",
        "calories": 360,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 620,
        "desc": "Gör helgens godaste frukost eller brunch! Tjocka, gyllenbruna och otroligt fluffiga amerikanska pannkakor som smälter i munnen. Serveras med smör, lönnsirap och färska bär.",
        "long_desc": "Hemligheten bakom riktigt fluffiga amerikanska pannkakor (American pancakes) är dubbelt bakpulver, smält smör i smeten och att inte vispa sönder smeten. Små klumpar gör pannkakorna extra höga och luftiga.",
        "keywords": "amerikanska pannkakor, amerikanska pannkakor recept, fluffiga amerikanska pannkakor, enkla amerikanska pannkakor, tjocka pannkakor med sirap",
        "alt": "Närbild på en hög trave gyllenbruna fluffiga amerikanska pannkakor med smältande smör, rinnande lönnsirap och blåbär",
        "equipment": ["Stekpanna eller pannkakslagg", "Vispskål & ballongvisp", "Stekspade"],
        "drink_pairing": "Nybryggt svenskt kaffe, färskpressad apelsinjuice eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Pannkakssmet", "items": [
                {"val": 3.5, "unit": "dl", "name": "vetemjöl"},
                {"val": 2, "unit": "tsk", "name": "bakpulver (ger maximal fluffighet)"},
                {"val": 2, "unit": "msk", "name": "strösocker"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 0.5, "unit": "tsk", "name": "salt"},
                {"val": 2.5, "unit": "dl", "name": "mjölk"},
                {"val": 50, "unit": "g", "name": "smör (smält och avsvalnat)"},
                {"val": 1, "unit": "st", "name": "stort ägg"}
            ]},
            {"group": "Servering & Topping", "items": [
                {"val": 1, "unit": "flaska", "name": "äkta lönnsirap (Maple syrup)"},
                {"val": 50, "unit": "g", "name": "äkta smör (att toppa den varma traven med)"},
                {"val": 1, "unit": "ask", "name": "färska blåbär och hallon"},
                {"val": 1, "unit": "msk", "name": "florsocker (att pudra över)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Blanda de torra ingredienserna", "text": "Blanda vetemjöl, bakpulver, strösocker, vaniljsocker och salt i en bunke.", "timer": 2},
            {"step": 2, "title": "Tillsätt vätskan & rör lätt", "text": "Vispa ihop mjölk, ägg och det smälta smöret i en separat skål. Häll ner i mjölblandningen och rör precis ihop till en tjock smet. Vispa inte för mycket – små klumpar gör pannkakorna extra fluffiga!", "timer": 3},
            {"step": 3, "title": "Hetta upp pannan", "text": "Klicka i lite smör i en stekpanna på medelvärme. Klicka ut ca 0.5–0.75 dl smet per pannkaka.", "timer": 2},
            {"step": 4, "title": "Stek tills bubblor bildas", "text": "Stek i ca 1.5–2 minuter tills det bildas små bubblor på ovansidan och undersidan är gyllenbrun.", "timer": 2},
            {"step": 5, "title": "Vänd och grädda klart", "text": "Vänd pannkakan försiktigt och stek ytterligare ca 1 minut på andra sidan tills den rest sig och blivit härligt tjock och genomgräddad.", "timer": 1},
            {"step": 6, "title": "Bygg trave & njut", "text": "Stapla de varma pannkakorna på hög, lägg en klick smör på toppen, ringla över rikligt med lönnsirap och toppa med färska bär.", "timer": None}
        ],
        "pro_tips": "Överblanda aldrig smeten! Rör bara tills mjölet precis blandats in. Om smeten är lite klumpig blir pannkakorna dubbelt så fluffiga och höga i pannan.",
        "nutrition": {"calories": "360 kcal", "protein": "8g", "carbs": "48g", "fat": "15g", "sugar": "12g"},
        "faqs": [
            {"q": "Varför blir mina amerikanska pannkakor platta?", "a": "Gammalt bakpulver eller för mycket vispande slår ur luften ur smeten. Använd färskt bakpulver och vänd bara ihop ingredienserna varsamt."},
            {"q": "Kan man byta ut mjölken mot filmjölk?", "a": "Ja, att använda filmjölk eller kärnmjölk (Buttermilk) ger en ännu saftigare konsistens och en mild fin syra som passar perfekt till söt sirap."}
        ],
        "community_reviews": [
            {"name": "Sara Blomqvist", "date": "Idag", "rating": 5, "comment": "Bästa pannkakorna jag någonsin ätit! Barnen slukade hela traven på 5 minuter.", "verified": True}
        ]
    },
    {
        "slug": "kramig-kycklingpasta-soltorkade-tomater",
        "file": "kramig-kycklingpasta-soltorkade-tomater.html",
        "img": "kycklingpasta",
        "title": "Krämig Kycklingpasta med Soltorkade Tomater & Spenat",
        "card_title": "Krämig Kycklingpasta",
        "sub": "Stekt kycklingfilé, tagliatelle, parmesan & soltorkade tomater",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Fågel / Pasta",
        "difficulty": "Enkel",
        "time": 25,
        "prep_time": "PT10M",
        "cook_time": "PT15M",
        "total_time": "PT25M",
        "prep_time_str": "10 min",
        "cook_time_str": "15 min",
        "time_str": "25 min",
        "calories": 540,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.97,
        "review_count": 530,
        "desc": "En snabb, lyxig och krämig kycklingpasta som gör succé både till vardags och till helgmiddagen. Gyllenstekt svensk kycklingfilé, strimlade soltorkade tomater, färsk babyspenat och riven parmesan i en fyllig vitlökssås.",
        "long_desc": "Sveriges mest efterfrågade vardagslyx! På under 25 minuter svänger du ihop denna krämiga kycklingpasta med italienska smaker. Oljan från de soltorkade tomaterna steks tillsammans med vitlök och kyckling för att ge maximal smak åt såsen.",
        "keywords": "kycklingpasta, krämig kycklingpasta, kycklingpasta med soltorkade tomater, pasta med kyckling och spenat, snabb kycklingpasta",
        "alt": "Närbild på en djup tallrik med krämig kycklingpasta, tagliatelle, skivad stekt kycklingfilé, soltorkade tomater, babyspenat och parmesan",
        "equipment": ["Stor stekpanna / traktörpanna", "Pastakastrull", "Rivjärn för parmesan"],
        "drink_pairing": "Ett friskt italienskt vitt vin (Pinot Grigio / Soave) eller ett lätt fruktigt rödvin som Valpolicella.",
        "ingredients": [
            {"group": "Kyckling & Pasta", "items": [
                {"val": 500, "unit": "g", "name": "svensk kycklingbröstfilé (i strimlor)"},
                {"val": 350, "unit": "g", "name": "tagliatelle eller fettuccine (äggpasta)"},
                {"val": 2, "unit": "msk", "name": "smör och olja (gärna oljan från tomatburken)"},
                {"val": 1, "unit": "tsk", "name": "torkad oregano & timjan"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Krämig Vitlökssås", "items": [
                {"val": 100, "unit": "g", "name": "soltorkade tomater i olja (strimlade)"},
                {"val": 65, "unit": "g", "name": "färsk babyspenat"},
                {"val": 3, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 1, "unit": "st", "name": "schalottenlök (finhackad)"},
                {"val": 3, "unit": "dl", "name": "vispgrädde"},
                {"val": 1.5, "unit": "dl", "name": "pastavatten (sparat från koket)"},
                {"val": 1.5, "unit": "msk", "name": "koncentrerad kycklingfond"},
                {"val": 1.5, "unit": "dl", "name": "finriven parmesanost (Parmigiano Reggiano)"}
            ]},
            {"group": "Garnering", "items": [
                {"val": 2, "unit": "msk", "name": "rostade pinjenötter"},
                {"val": 1, "unit": "kruka", "name": "färsk basilika (grovhackad)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Koka pastan", "text": "Koka pastan i rikligt saltat vatten enligt anvisning på paketet tills den är perfekt al dente. Spara ca 2 dl av det stärkelserika pastavattnet innan du häller av.", "timer": 10},
            {"step": 2, "title": "Stek kycklingen gyllenbrun", "text": "Strimla kycklingen och krydda med oregano, timjan, salt och peppar. Hetta upp 1 msk smör och 1 msk olja från de soltorkade tomaterna i en stor panna. Stek kycklingen gyllenbrun och genomstekt i ca 5–6 minuter. Lägg över på ett fat.", "timer": 6},
            {"step": 3, "title": "Fräs vitlök & soltorkade tomater", "text": "Sänk värmen. Fräs lök, vitlök och de strimlade soltorkade tomaterna i pannan i 2 minuter utan att de bränns.", "timer": 2},
            {"step": 4, "title": "Koka upp gräddsåsen", "text": "Häll i vispgrädde, kycklingfond och 1 dl pastavatten. Låt sjuda i 3–4 minuter tills såsen tjocknar något.", "timer": 4},
            {"step": 5, "title": "Vänd ner spenat, parmesan & kyckling", "text": "Rör ner den rivna parmesanosten tills den smält. Vänd i babyspenaten och den stekta kycklingen och låt spenaten precis mjukna.", "timer": 2},
            {"step": 6, "title": "Blanda med pasta & servera", "text": "Vänd ner den nykokta tagliatellen direkt i såsen så att varje pastaband täcks av den krämiga såsen. Toppa med färsk basilika, rostade pinjenötter och extra parmesan.", "timer": 2}
        ],
        "pro_tips": "Stek kycklingen och vitlöken i oljan från burken med soltorkade tomater – den är fullproppad med koncentrerad ört- och tomatsmak!",
        "nutrition": {"calories": "540 kcal", "protein": "38g", "carbs": "44g", "fat": "24g", "sugar": "5g"},
        "faqs": [
            {"q": "Varför ska man spara pastavattnet?", "a": "Stärkelsen i pastavattnet emulgerar med grädden och parmesanen vilket ger en glansig, restaurangkrämig sås som fäster perfekt på pastan."},
            {"q": "Kan man byta ut kycklingen mot halloumi?", "a": "Ja, stekt halloumi eller svamp (skogsgrönsaker) är ett fantastiskt vegetariskt alternativ till denna pasta."}
        ],
        "community_reviews": [
            {"name": "Elin Sundström", "date": "Idag", "rating": 5, "comment": "Vår nya storfavorit på onsdagar! Otroligt krämig och så god smak från tomaterna och vitlöken.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-kramig-potatisgratang",
        "file": "klassisk-kramig-potatisgratang.html",
        "img": "potatisgratang",
        "title": "Klassisk Krämig Potatisgratäng med Vitlök, Grädde & Ost",
        "card_title": "Krämig Potatisgratäng",
        "sub": "Tunt skivad potatis i vitlöksgrädde med gyllenbrunt osttäcke",
        "category": "Högtider & Smörgåsbord",
        "cat_slug": "hogtider-och-smorgasbord",
        "cat_key": "smorgasbord",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 60,
        "prep_time": "PT15M",
        "cook_time": "PT45M",
        "total_time": "PT60M",
        "prep_time_str": "15 min",
        "cook_time_str": "45 min",
        "time_str": "60 min",
        "calories": 390,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 670,
        "desc": "En oemotståndlig, silkeslen och krämig potatisgratäng som aldrig blir torr. Tunt skivad mjölig potatis varvad med vitlök, grädde, mjölk och ett gyllenbrunt täcke av lagrad prästost eller Västerbottensost.",
        "long_desc": "Det ultimata tillbehöret till helstekt oxfilé, lamm, tjälknöl eller som fristående rätt till en krispig sallad. Hemligheten bakom en perfekt krämig gratäng är att använda rätt potatissort och koka upp potatisen lätt i gräddmjölken innan den gräddas i ugnen.",
        "keywords": "potatisgratäng, potatisgratang, krämig potatisgratäng, potatisgratäng recept, enkel potatisgratäng med vitlök och ost, bästa potatisgratängen",
        "alt": "Närbild på en saftig portionsbit krämig potatisgratäng med gyllenbrunt gräddat osttäcke och synliga potatislager",
        "equipment": ["Ugnsform (ca 20x30 cm)", "Mandolin eller vass kniv", "Kastrull"],
        "drink_pairing": "Ett fylligt rött vin som Rioja, Bordeaux, Cabernet Sauvignon eller en krispig svensk cider.",
        "ingredients": [
            {"group": "Potatis & Gräddbas", "items": [
                {"val": 1000, "unit": "g", "name": "mjölig potatis (t.ex. King Edward, skalad)"},
                {"val": 3, "unit": "klyftor", "name": "vitlök (finrivna)"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad eller mycket tunt skivad)"},
                {"val": 4, "unit": "dl", "name": "vispgrädde"},
                {"val": 2, "unit": "dl", "name": "standardmjölk"},
                {"val": 1.5, "unit": "tsk", "name": "salt"},
                {"val": 2, "unit": "krm", "name": "nymalen vitpeppar & en nypa riven muskotnöt"}
            ]},
            {"group": "Osttäcke", "items": [
                {"val": 150, "unit": "g", "name": "lagrad Prästost, Grevé eller Västerbottensost (riven)"},
                {"val": 2, "unit": "kvistar", "name": "färsk timjan (att garnera med)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Skiva potatisen tunt", "text": "Sätt ugnen på 200°C över-/undervärme. Skala potatisen och skiva den i ca 2–3 mm tunna skivor med mandolin eller kniv. (Skölj inte potatisen, stärkelsen behövs för krämigheten!).", "timer": 10},
            {"step": 2, "title": "Koka upp med gräddmjölken", "text": "Lägg den skivade potatisen, finhackad lök och riven vitlök i en rymlig kastrull. Häll på vispgrädde, mjölk, salt, peppar och muskotnöt. Koka upp försiktigt och låt sjuda i ca 8–10 minuter under försiktig omrörning så att stärkelsen löser sig och reder vätskan.", "timer": 10},
            {"step": 3, "title": "Häll i ugnsformen", "text": "Smörj en ugnsfast form med lite smör. Häll i den förkokta krämiga potatisblandningen och jämna till ytan.", "timer": 2},
            {"step": 4, "title": "Toppa med riven ost", "text": "Strö den rivna lagrade osten jämnt över hela gratängen.", "timer": 2},
            {"step": 5, "title": "Grädda gyllenbrun & bubblande", "text": "Grädda mitt i ugnen i 30–35 minuter tills potatisen är helt mjuk rakt igenom (känn med en provsticka) och osten fått en vacker gyllene färg.", "timer": 30},
            {"step": 6, "title": "Låt vila & sätta sig", "text": "Låt potatisgratängen stå och vila i 10–15 minuter före servering. Då sätter den sig och blir perfekt krämig att skära upp i fina rutor.", "timer": 15}
        ],
        "pro_tips": "Skölj ALDRIG potatisskivorna i vatten efter att du skivat dem! Potatisens naturliga stärkelse är det som gör att grädden och mjölken reder sig till en fantastiskt fyllig, krämig sås.",
        "nutrition": {"calories": "390 kcal", "protein": "9g", "carbs": "32g", "fat": "26g", "sugar": "4g"},
        "faqs": [
            {"q": "Vilken potatissort är bäst till potatisgratäng?", "a": "Mjölig potatis (som King Edward) ger den absolut krämigaste gratängen eftersom stärkelsen naturligt reder såsen."},
            {"q": "Kan man förbereda potatisgratängen i förväg?", "a": "Ja! Förkoka potatisen i gräddmjölken och lägg i formen. Förvara i kylen och grädda med osten precis före middagen."}
        ],
        "community_reviews": [
            {"name": "Margareta Nilsson", "date": "Idag", "rating": 5, "comment": "Att förkoka potatisen i grädden gjorde all skillnad i världen – absolut restaurangklass!", "verified": True}
        ]
    },
    {
        "slug": "klassisk-ryttarkaka-kokostosca",
        "file": "klassisk-ryttarkaka-kokostosca.html",
        "img": "ryttarkaka",
        "title": "Klassisk Ryttarkaka – Kärleksmums möter Tosca med Knäckig Kokos",
        "card_title": "Klassisk Ryttarkaka",
        "sub": "Saftig chokladkaka med gyllene karamelliserad kokostosca",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 40,
        "prep_time": "PT15M",
        "cook_time": "PT25M",
        "total_time": "PT40M",
        "prep_time_str": "15 min",
        "cook_time_str": "25 min",
        "time_str": "40 min",
        "calories": 380,
        "portions_num": 12,
        "portions_unit": "bitar",
        "rating": 4.98,
        "review_count": 460,
        "desc": "Det bästa av två världar! En saftig, fyllig chokladkaka i botten toppad med en knäckig, karamelliserad kokostosca gjord på smör, ljus sirap och riven kokos. En svensk fikaklassiker som älskas av alla.",
        "long_desc": "Ryttarkaka (även känd som toscakaka med choklad eller falsk toscakaka) är ett måste på fikabordet. Kontrasten mellan den mörka chokladbottnen och det gyllene, knäckiga kokostäcket är helt oemotståndlig.",
        "keywords": "ryttarkaka, ryttarkaka recept, chokladkaka med kokostosca, toscakaka choklad, kokostosca kaka, bästa ryttarkakan",
        "alt": "Närbild på en saftig ruta ryttarkaka med mörk chokladbotten och gyllenbrunt knäckigt kokostoscatäcke på fat",
        "equipment": ["Liten långpanna eller form (ca 20x30 cm)", "Bakplåtspapper", "Kastrull till toscasmet"],
        "drink_pairing": "En stor kopp nymalet bryggkaffe med mjölk, en krämig cappuccino eller ett glas kall havremjölk.",
        "ingredients": [
            {"group": "Saftig Chokladbotten", "items": [
                {"val": 150, "unit": "g", "name": "smör (smält)"},
                {"val": 3, "unit": "st", "name": "stora ägg"},
                {"val": 3, "unit": "dl", "name": "strösocker"},
                {"val": 3.5, "unit": "dl", "name": "vetemjöl"},
                {"val": 1, "unit": "dl", "name": "kakao av god kvalitet"},
                {"val": 2, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 2, "unit": "tsk", "name": "bakpulver"},
                {"val": 1, "unit": "dl", "name": "mjölk eller kaffe (för extra djup)"},
                {"val": 0.5, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Knäckig Kokostosca", "items": [
                {"val": 75, "unit": "g", "name": "smör"},
                {"val": 1.5, "unit": "dl", "name": "strösocker"},
                {"val": 0.75, "unit": "dl", "name": "ljus sirap"},
                {"val": 1.5, "unit": "dl", "name": "vispgrädde eller mjölk"},
                {"val": 200, "unit": "g", "name": "riven kokos (1 påse)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered form & ugn", "text": "Sätt ugnen på 175°C över-/undervärme. Klä en form (ca 20x30 cm) med bakplåtspapper.", "timer": 5},
            {"step": 2, "title": "Vispa smeten till chokladbottnen", "text": "Vispa ägg och strösocker pösigt. Blanda vetemjöl, kakao, vaniljsocker, bakpulver och salt i en skål. Vänd ner de torra ingredienserna växelvis med smält smör och mjölk/kaffe till en jämn chokladsmet.", "timer": 5},
            {"step": 3, "title": "Förgrädda bottnen", "text": "Bred ut smeten i formen. Grädda mitt i ugnen i ca 15 minuter medan du kokar kokostoscan.", "timer": 15},
            {"step": 4, "title": "Koka kokostoscan", "text": "Blanda smör, strösocker, ljus sirap och grädde i en kastrull. Låt koka upp på medelvärme och sjuda under omrörning i ca 5 minuter tills det tjocknar. Rör ner kokosen.", "timer": 5},
            {"step": 5, "title": "Bred på toscan & grädda färdigt", "text": "Ta ut kakan ur ugnen och bred försiktigt ut den varma kokostoscan jämnt över hela chokladbottnen. Höj ugnen till 200°C och grädda i ytterligare 10–12 minuter tills toscan blivit vackert gyllenbrun och knäckig.", "timer": 10},
            {"step": 6, "title": "Låt svalna & skär i rutor", "text": "Låt kakan svalna helt så att kokostoscan stelnar till ett frasigt täcke. Skär i generösa rutor och servera till fikat.", "timer": 15}
        ],
        "pro_tips": "Låt kokossmeten koka ihop i 5 minuter innan du brer den över kakan. Då karamelliseras sockret och sirapen vilket ger en oslagbart knäckig och gyllene tosca.",
        "nutrition": {"calories": "380 kcal", "protein": "5g", "carbs": "46g", "fat": "20g", "sugar": "32g"},
        "faqs": [
            {"q": "Hur förvarar man ryttarkaka bäst?", "a": "Kakan håller sig saftig i rumstemperatur i lufttät burk i 4–5 dagar. Den går även utmärkt att frysa in i bitar med bakplåtspapper emellan."},
            {"q": "Vad är skillnaden mellan ryttarkaka och kärleksmums?", "a": "Kärleksmums har en kaffeglasyr med kokos ovanpå en chokladbotten, medan ryttarkaka gräddas en andra gång i ugnen med en varm kokostosca som blir knäckig."}
        ],
        "community_reviews": [
            {"name": "Camilla Ekström", "date": "Idag", "rating": 5, "comment": "Den godaste kakan jag någonsin bakat! Kokostäcket är helt beroendeframkallande.", "verified": True}
        ]
    },
    {
        "slug": "gammaldags-mjuk-appelkaka-kanel",
        "file": "gammaldags-mjuk-appelkaka-kanel.html",
        "img": "appelkaka",
        "title": "Gammaldags Mjuk Äppelkaka med Kanel & Hemgjord Vaniljsås",
        "card_title": "Gammaldags Äppelkaka",
        "sub": "Saftig sockerkaksbotten med kanelstekta svenska äpplen",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 45,
        "prep_time": "PT15M",
        "cook_time": "PT30M",
        "total_time": "PT45M",
        "prep_time_str": "15 min",
        "cook_time_str": "30 min",
        "time_str": "45 min",
        "calories": 310,
        "portions_num": 10,
        "portions_unit": "bitar",
        "rating": 4.99,
        "review_count": 560,
        "desc": "En svensk höstklassiker som fyller hela huset med doften av nymalen kanel, kardemumma och smör. En otroligt saftig sockerkaksbotten toppad med tunna klyftor av syrliga svenska äpplen vända i kanel och råsocker. Serveras med rinnande vaniljsås.",
        "long_desc": "Mormors klassiska mjuka äppelkaka när den är som allra bäst. Genom att vända äppelklyftorna i kanel, socker och lite smält smör innan de trycks ner i sockerkakssmeten behåller äpplena sin saftighet och ger kakan en karamelliserad yta.",
        "keywords": "äppelkaka, äppelkaka recept, gammaldags äppelkaka, mjuk äppelkaka med kanel, enkel äppelkaka, saftig äppelkaka",
        "alt": "Närbild på en saftig gyllenbrun bit mjuk äppelkaka med kanelstekta äppelklyftor och len vaniljsås på tallrik",
        "equipment": ["Springform (24 cm med löstagbar botten)", "Elvisp & bunke", "Skalkniv & skärbräda"],
        "drink_pairing": "En kopp nymalet bryggkaffe, klassiskt svart te eller ett glas kall äppelmust.",
        "ingredients": [
            {"group": "Saftig Kakbotten", "items": [
                {"val": 3, "unit": "st", "name": "stora ägg"},
                {"val": 2.5, "unit": "dl", "name": "strösocker"},
                {"val": 3, "unit": "dl", "name": "vetemjöl"},
                {"val": 2, "unit": "tsk", "name": "bakpulver"},
                {"val": 2, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 1, "unit": "tsk", "name": "nymalen kardemumma"},
                {"val": 100, "unit": "g", "name": "smör (smält)"},
                {"val": 1, "unit": "dl", "name": "mjölk"},
                {"val": 0.5, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Äppeltopping", "items": [
                {"val": 4, "unit": "st", "name": "syrliga svenska äpplen (t.ex. Ingrid Marie eller Aroma)"},
                {"val": 2, "unit": "msk", "name": "strösocker eller råsocker"},
                {"val": 1.5, "unit": "msk", "name": "malen kanel"},
                {"val": 25, "unit": "g", "name": "smör (hyvlat över kakan före gräddning)"}
            ]},
            {"group": "Servering", "items": [
                {"val": 1, "unit": "såskanna", "name": "äkta hemgjord vaniljsås eller vaniljglass"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ugn & form", "text": "Sätt ugnen på 175°C över-/undervärme. Smörj och bröa en springform (ca 24 cm i diameter) med ströbröd eller kokos.", "timer": 5},
            {"step": 2, "title": "Skiva & krydda äpplena", "text": "Skala, kärna ur och skär äpplena i tunna klyftor. Blanda äpplena i en skål med kanel och socker så att alla klyftor täcks.", "timer": 5},
            {"step": 3, "title": "Vispa kaksmeten", "text": "Vispa ägg och strösocker riktigt pösigt och vitt med elvisp i ca 3–4 minuter. Blanda vetemjöl, bakpulver, vaniljsocker, kardemumma och salt. Vänd ner i äggsmeten växelvis med smält smör och mjölk.", "timer": 5},
            {"step": 4, "title": "Montera kakan", "text": "Häll smeten i formen. Tryck ner de kanelkryddade äppelklyftorna tätt i ett vackert solfjädersmönster. Hyvla tunna skivor kallt smör över toppen.", "timer": 5},
            {"step": 5, "title": "Grädda gyllenbrun", "text": "Grädda i nedre delen av ugnen i 30–35 minuter tills kakan är gyllenbrun och en provsticka i mitten kommer ut torr.", "timer": 30},
            {"step": 6, "title": "Låt svalna & servera", "text": "Låt kakan svalna i formen i 10 minuter. Servera ljummen med massor av kall vaniljsås eller en kula vaniljglass.", "timer": 10}
        ],
        "pro_tips": "Hyvla lite kallt smör med osthyvel över äpplena precis innan formen åker in i ugnen. Det gör att sockret och kanelen karamelliseras till en underbart frasig yta.",
        "nutrition": {"calories": "310 kcal", "protein": "5g", "carbs": "44g", "fat": "13g", "sugar": "26g"},
        "faqs": [
            {"q": "Vilka äpplen är bäst att baka med?", "a": "Syrliga och fasta äppelsorter som Ingrid Marie, Gravenstein eller Aroma ger bäst balans mot den söta kakan och behåller sin form."},
            {"q": "Kan kakan frysas?", "a": "Ja, mjuk äppelkaka går utmärkt att frysa hel eller i bitar och kan snabbt tinas och värmas i ugnen."}
        ],
        "community_reviews": [
            {"name": "Astrid Lindberg", "date": "Idag", "rating": 5, "comment": "Precis som mormors äppelkaka! Så saftig och kardemumman i smeten var pricken över i:et.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-svensk-kottfarssas-spaghetti",
        "file": "klassisk-svensk-kottfarssas-spaghetti.html",
        "img": "kottfarssas",
        "title": "Klassisk Svensk Köttfärssås & Spaghetti – Bästa Receptet",
        "card_title": "Klassisk Köttfärssås",
        "sub": "Sveriges mest älskade vardagsrätt. Mustig, fyllig & långkokt",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Pasta",
        "difficulty": "Enkel",
        "time": 45,
        "prep_time": "PT15M",
        "cook_time": "PT30M",
        "total_time": "PT45M",
        "prep_time_str": "15 min",
        "cook_time_str": "30 min",
        "time_str": "45 min",
        "calories": 530,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 780,
        "desc": "Sveriges mest lagade vardagsmiddag! En klassisk, mustig och djup svensk köttfärssås gjord på nötfärs, finrivna morötter, selleri, vitlök, rött vin, fylliga tomater och torkad oregano. Serveras med rykande het spaghetti och riven parmesan.",
        "long_desc": "Den ultimata köttfärssåsen som slår alla burkar och halvfabrikat. Hemligheten bakom ett riktigt djupt smakregister är att fräsa tomatpurén ordentligt i smör och låta såsen puttra sakta så att köttet blir smältande mört och såsen koncentrerad.",
        "keywords": "köttfärssås, köttfärssås recept, klassisk köttfärssås, godaste köttfärssåsen, bästa köttfärssåsen, köttfärssås och spaghetti, bolognese svensk",
        "alt": "Närbild på en djup tallrik med al dente spaghetti täckt med mustig mörkröd köttfärssås, riven parmesanost och färsk basilika",
        "equipment": ["Gjutjärnsgryta eller rymlig kastrull", "Pastakastrull", "Rivjärn"],
        "drink_pairing": "Ett italienskt rött vin som Chianti, Barbera d'Asti eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Kött & Såsbas", "items": [
                {"val": 600, "unit": "g", "name": "nötfärs eller blandfärs av god kvalitet"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad)"},
                {"val": 3, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 2, "unit": "st", "name": "morötter (finrivna för naturlig sötma)"},
                {"val": 1, "unit": "stjälk", "name": "blekselleri (finhackad)"},
                {"val": 3, "unit": "msk", "name": "tomatpuré"},
                {"val": 2, "unit": "msk", "name": "smör och 1 msk olivolja (att steka i)"}
            ]},
            {"group": "Vätska & Kryddning", "items": [
                {"val": 2, "unit": "burkar", "name": "krossade tomater (t.ex. Mutti, à 400g)"},
                {"val": 2, "unit": "dl", "name": "rött vin eller vatten"},
                {"val": 3, "unit": "msk", "name": "koncentrerad oxfond eller kalvfond"},
                {"val": 1, "unit": "msk", "name": "kinesisk soja"},
                {"val": 1.5, "unit": "msk", "name": "torkad oregano & timjan"},
                {"val": 2, "unit": "st", "name": "lagerblad"},
                {"val": 1, "unit": "tsk", "name": "strösocker eller honung (balanserar syran)"},
                {"val": 1.5, "unit": "tsk", "name": "salt & rikligt med nymalen svartpeppar"},
                {"val": 0.5, "unit": "dl", "name": "vispgrädde eller mjölk (avslutas med för rundhet)"}
            ]},
            {"group": "Servering", "items": [
                {"val": 500, "unit": "g", "name": "god spaghetti (t.ex. bronsvalsad)"},
                {"val": 2, "unit": "dl", "name": "finriven parmesanost (Parmigiano Reggiano)"},
                {"val": 1, "unit": "kruka", "name": "färsk basilika"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Fräs grönsakerna mjukt", "text": "Hetta upp smör och olivolja i en stor gjutjärnsgryta. Fräs finhackad lök, vitlök, finrivna morötter och blekselleri på medelvärme i ca 5 minuter tills de är mjuka och doftar ljuvligt.", "timer": 5},
            {"step": 2, "title": "Bryn färsen & rosta tomatpuré", "text": "Höj värmen och tillsätt färsen. Bryn under omrörning så att den finfördelas. Klicka i tomatpurén och låt den fräsa med i 2 minuter – detta tar bort beskan och ger en söt, karamelliserad tomatsmak.", "timer": 5},
            {"step": 3, "title": "Häll i vin, tomater & kryddor", "text": "Häll i rödvin och låt koka in i 2 minuter. Tillsätt krossade tomater, fond, soja, oregano, timjan, lagerblad, socker, salt och peppar.", "timer": 3},
            {"step": 4, "title": "Låt puttra långsamt", "text": "Sänk till lägsta värme, sätt på locket på glänt och låt såsen sjuda i minst 25–30 minuter (gärna 1 timme om du har tid!). Rör om då och då.", "timer": 25},
            {"step": 5, "title": "Koka spaghetti & runda av såsen", "text": "Koka spaghettin i rikligt med saltat vatten enligt anvisning tills den är al dente. Rör ner en skvätt vispgrädde i köttfärssåsen och smaka av med salt och svartpeppar.", "timer": 10},
            {"step": 6, "title": "Servera med parmesan & basilika", "text": "Servera den rykande heta spaghettin toppad med generöst med köttfärssås, nyriven parmesanost och färsk basilika.", "timer": None}
        ],
        "pro_tips": "Riv ner morötter och fräs tomatpurén hårt i början. Moroten ger en naturlig sötma som perfekt rundar av tomatsyran och gör såsen oemotståndligt fyllig.",
        "nutrition": {"calories": "530 kcal", "protein": "34g", "carbs": "56g", "fat": "18g", "sugar": "7g"},
        "faqs": [
            {"q": "Hur gör man köttfärssåsen extra mustig?", "a": "Låt såsen koka länge på svag värme och använd både oxfond, tomatpuré och en skvätt rödvin samt en gnutta soja för umami."},
            {"q": "Kan köttfärssås frysas?", "a": "Ja, köttfärssås är en av de bästa rätterna att göra matlådor av och frysa in. Smaken blir ofta ännu bättre efter att ha stått till dagen efter!"}
        ],
        "community_reviews": [
            {"name": "Johan Bergström", "date": "Idag", "rating": 5, "comment": "Hela familjens absoluta favoritrecept på köttfärssås. Den rivna moroten och fonden gör magi!", "verified": True}
        ]
    },
    {
        "slug": "klassisk-cowboysoppa-kottfars-potatis",
        "file": "klassisk-cowboysoppa-kottfars-potatis.html",
        "img": "cowboysoppa",
        "title": "Klassisk Cowboysoppa med Köttfärs, Potatis, Majs & Grädde",
        "card_title": "Klassisk Cowboysoppa",
        "sub": "Värmande & matig soppa med brynt färs, potatis & majs",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Soppor",
        "difficulty": "Enkel",
        "time": 35,
        "prep_time": "PT15M",
        "cook_time": "PT20M",
        "total_time": "PT35M",
        "prep_time_str": "15 min",
        "cook_time_str": "20 min",
        "time_str": "35 min",
        "calories": 460,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 520,
        "desc": "En riktig vardagshjälte och barnfamiljernas storfavorit! En värmande, smakrik soppa med brynt köttfärs, tärnad potatis, majskorn, vita bönor och paprika i en krämig, fyllig buljong med paprikapulver och gräslök.",
        "long_desc": "Cowboysoppa (kallas ibland cowgirlsoppa eller skaffarissoppa) är snabb, mättande och otroligt god. Allt lagas i en och samma gryta vilket ger minimal disk och maximal smak på under 35 minuter.",
        "keywords": "cowboysoppa, cowboysoppa recept, krämig cowboysoppa, godaste cowboysoppan, cowboy soppa med köttfärs och potatis, soppa med köttfärs",
        "alt": "Närbild på en skål varm krämig cowboysoppa med köttfärs, potatisbitar, majs, bönor, gräslök och vitlöksbröd på kanten",
        "equipment": ["Stor soppgryta", "Skärbräda & kockkniv", "Träslev"],
        "drink_pairing": "En kall svensk lättöl, krispig cider eller ett glas iskall mjölk.",
        "ingredients": [
            {"group": "Kött & Grönsaker", "items": [
                {"val": 500, "unit": "g", "name": "nötfärs eller blandfärs"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad)"},
                {"val": 2, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 4, "unit": "st", "name": "potatisar (skalade och tärnade i 1.5 cm bitar)"},
                {"val": 1, "unit": "st", "name": "röd paprika (tärnad)"},
                {"val": 1, "unit": "burk", "name": "majskorn (à 150g, avrunna)"},
                {"val": 1, "unit": "burk", "name": "vita bönor i tomatsås eller sköljda vita bönor (à 400g)"},
                {"val": 2, "unit": "msk", "name": "smör (att steka i)"}
            ]},
            {"group": "Buljong & Kryddning", "items": [
                {"val": 3, "unit": "msk", "name": "tomatpuré"},
                {"val": 2, "unit": "msk", "name": "paprikapulver (sött & lite rökt)"},
                {"val": 1, "unit": "tsk", "name": "torkad oregano & timjan"},
                {"val": 10, "unit": "dl", "name": "vatten + 3 msk oxfond eller köttbuljongtärningar"},
                {"val": 2, "unit": "dl", "name": "vispgrädde eller crème fraiche"},
                {"val": 1, "unit": "msk", "name": "kinesisk soja"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 1, "unit": "kruka", "name": "färsk gräslök (klippt)"},
                {"val": 6, "unit": "skivor", "name": "rostat vitlöksbröd eller gott knäckebröd"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Bryn köttfärs & lök", "text": "Hetta upp smör i en stor soppgryta. Bryn köttfärs, gul lök och vitlök på medelhög värme tills färsen fått fin färg och löken mjuknat.", "timer": 6},
            {"step": 2, "title": "Tillsätt kryddor & tomatpuré", "text": "Rör ner tomatpuré, paprikapulver, oregano och timjan. Låt fräsa med under omrörning i 1 minut så att kryddsmakerna utvecklas.", "timer": 2},
            {"step": 3, "title": "Häll i buljong & potatis", "text": "Tillsätt vatten, oxfond, soja och den tärnade potatisen. Koka upp och låt soppan sjuda på svag värme under lock i ca 12–15 minuter tills potatisen är mjuk.", "timer": 15},
            {"step": 4, "title": "Tillsätt paprika, majs, bönor & grädde", "text": "Rör ner tärnad paprika, majskorn, bönor och vispgrädde. Låt soppan sjuda i ytterligare 5 minuter så att allt blir genomvarmt och smakerna gifter sig.", "timer": 5},
            {"step": 5, "title": "Smaka av & toppa", "text": "Smaka av soppan med salt, nymalen svartpeppar och eventuellt en nypa cayennepeppar. Klipp över rikligt med färsk gräslök.", "timer": 2},
            {"step": 6, "title": "Servera", "text": "Ös upp soppan i djupa skålar och servera rykande het med ett krispigt vitlöksbröd eller nybakat knäckebröd med ost.", "timer": None}
        ],
        "pro_tips": "Vill du ha soppan extra krämig? Krossa några av de kokta potatisbitarna mot grytans kant med en slev – stärkelsen reder då soppan naturligt.",
        "nutrition": {"calories": "460 kcal", "protein": "28g", "carbs": "36g", "fat": "22g", "sugar": "6g"},
        "faqs": [
            {"q": "Kan man byta ut köttfärsen mot vegetarisk färs?", "a": "Ja, sojafärs eller quornfärs fungerar utmärkt i cowboysoppa och smakar fantastiskt med samma kryddning."},
            {"q": "Kan soppan sparas i kylen?", "a": "Ja, cowboysoppa håller 3–4 dagar i kylskåp och är nästan godare dagen efter när potatisen dragit åt sig av all mustig buljong."}
        ],
        "community_reviews": [
            {"name": "Therese Holm", "date": "Idag", "rating": 5, "comment": "Bästa vardagssoppan! Både 4-åringen och mannen åt två stora portioner.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-frasiga-scones",
        "file": "klassiska-frasiga-scones.html",
        "img": "scones",
        "title": "Klassiska Frasiga Scones – Snabbt & Enkelt Recept (15 min)",
        "card_title": "Klassiska Scones",
        "sub": "Nygräddade, fluffiga & frasiga scones till helgfrukosten",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 15,
        "prep_time": "PT5M",
        "cook_time": "PT10M",
        "total_time": "PT15M",
        "prep_time_str": "5 min",
        "cook_time_str": "10 min",
        "time_str": "15 min",
        "calories": 290,
        "portions_num": 8,
        "portions_unit": "scones",
        "rating": 4.99,
        "review_count": 690,
        "desc": "Det snabbaste och godaste brödet du kan baka! Nygräddade, frasiga scones med gyllenbrun skorpa och mjuk, fluffig insida. Klara på bara 15 minuter utan jäsning. Serveras varma med smör, ost och marmelad.",
        "long_desc": "Finns det något bättre till helgfrukosten eller eftermiddagsteet än rykande varma hembakade scones? Hemligheten bakom extra frasiga och höga scones är kallt smör som nypas snabbt in i mjölet och att dega ihop så lite som möjligt.",
        "keywords": "scones, scones recept, enkla scones, snabba scones, godaste scones, frasiga scones, scones utan filmjölk, frukost scones",
        "alt": "Närbild på nygräddade rykande varma frasiga scones delade på mitten med smältande smör, clotted cream och jordgubbssylt",
        "equipment": ["Bakplåt med bakplåtspapper", "Bunke & fingrar", "Kavel eller händer"],
        "drink_pairing": "En kanna rykande hett Earl Grey-te med mjölk eller en stor kopp nybryggt kaffe.",
        "ingredients": [
            {"group": "Sconesdeg", "items": [
                {"val": 4.5, "unit": "dl", "name": "vetemjöl"},
                {"val": 2, "unit": "tsk", "name": "bakpulver"},
                {"val": 2, "unit": "tsk", "name": "strösocker (framhäver smaken)"},
                {"val": 0.5, "unit": "tsk", "name": "salt"},
                {"val": 75, "unit": "g", "name": "kallt smör (i små tärningar)"},
                {"val": 2, "unit": "dl", "name": "mjölk eller filmjölk"}
            ]},
            {"group": "Klassisk Servering", "items": [
                {"val": 1, "unit": "burk", "name": "god marmelad (t.ex. apelsin, jordgubb eller hallon)"},
                {"val": 1, "unit": "ask", "name": "färskost eller clotted cream"},
                {"val": 1, "unit": "bit", "name": "lagrad herrgårdsost eller prästost"},
                {"val": 50, "unit": "g", "name": "äkta smör med havssalt"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Sätt ugnen på hög värme", "text": "Sätt ugnen på 250°C över-/undervärme. Lägg ett bakplåtspapper på en plåt.", "timer": 2},
            {"step": 2, "title": "Nyp ihop de torra ingredienserna med smör", "text": "Blanda vetemjöl, bakpulver, socker och salt i en bunke. Tillsätt det kalla tärnade smöret och nyp snabbt ihop med fingertopparna till en smulig massa.", "timer": 3},
            {"step": 3, "title": "Tillsätt mjölken & samla snabbt", "text": "Häll i mjölken och arbeta snabbt ihop till en smidig deg. Knåda inte, degen ska bara precis gå ihop för att hålla sconesen luftiga!", "timer": 2},
            {"step": 4, "title": "Forma kakor & nagga", "text": "Dela degen i 2 eller 4 runda kakor och lägg på plåten. Platta ut till ca 1.5–2 cm tjocklek. Skär ett kors i varje kaka med en kniv och nagga med en gaffel.", "timer": 2},
            {"step": 5, "title": "Grädda i ugnen", "text": "Grädda mitt i ugnen i ca 8–10 minuter tills de rest sig ordentligt och fått en vacker gyllenbrun frasig färg.", "timer": 9},
            {"step": 6, "title": "Servera genast", "text": "Bryt sconesen i fjärdedelar medan de fortfarande är varma och servera med massor av smör, ost och marmelad.", "timer": None}
        ],
        "pro_tips": "Knåda aldrig sconesdegen för länge! Ju mindre du rör i degen efter att mjölken tillsatts, desto högre och fluffigare blir dina scones.",
        "nutrition": {"calories": "290 kcal", "protein": "6g", "carbs": "38g", "fat": "12g", "sugar": "3g"},
        "faqs": [
            {"q": "Varför blir mina scones tunga och kompakta?", "a": "Om degen knådas för mycket bildas gluten och sconesen blir sega. Arbeta bara ihop degen med lätta händer tills den precis håller ihop."},
            {"q": "Kan man baka scones med filmjölk?", "a": "Ja, filmjölk ger en extra syrlig, fyllig smak och gör inkråmet ännu saftigare."}
        ],
        "community_reviews": [
            {"name": "Jenny Karlsson", "date": "Idag", "rating": 5, "comment": "Världens enklaste scones! Klara på en kvart och så otroligt frasiga på utsidan.", "verified": True}
        ]
    },
    {
        "slug": "mustig-chili-con-carne",
        "file": "mustig-chili-con-carne.html",
        "img": "chiliconcarne",
        "title": "Mustig Chili con Carne med Nötfärs, Bönor & Mörk Choklad",
        "card_title": "Mustig Chili con Carne",
        "sub": "Djup, rökig smak med spiskummin, bönor & en klick gräddfil",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Grytor",
        "difficulty": "Enkel",
        "time": 50,
        "prep_time": "PT15M",
        "cook_time": "PT35M",
        "total_time": "PT50M",
        "prep_time_str": "15 min",
        "cook_time_str": "35 min",
        "time_str": "50 min",
        "calories": 490,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 590,
        "desc": "En genuin, mustig och värmande chili con carne med rik smak. Nötfärs bryns och får koka långsamt med kidneybönor, svarta bönor, majs, rökt paprika, spiskummin och en bit mörk choklad för ett oslagbart djup. Serveras med ris, nachochips och gräddfil.",
        "long_desc": "Den ultimata höstgrytan för hela familjen. Hemligheten bakom en riktigt god chili con carne är kombinationen av spiskummin, rökt paprikapulver och en ruta mörk choklad som smälter ner på slutet och ger grytan en mörk, fyllig glans.",
        "keywords": "chili con carne, chili con carne recept, godaste chili con carne, enkel chili con carne, mustig chili con carne med choklad, chili gryta",
        "alt": "Närbild på en rykande het gjutjärnspanna med mustig chili con carne, bönor, smält gräddfil, koriander, chili och nachochips",
        "equipment": ["Gjutjärnsgryta", "Skärbräda & kockkniv", "Träslev"],
        "drink_pairing": "En kall mexikansk lager med lime, en fyllig svensk ale eller ett fruktigt Zinfandel-rödvin.",
        "ingredients": [
            {"group": "Kött & Kryddbas", "items": [
                {"val": 600, "unit": "g", "name": "nötfärs"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad)"},
                {"val": 3, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 1, "unit": "st", "name": "röd spansk peppar eller chili (urkärnad & finhackad)"},
                {"val": 2, "unit": "msk", "name": "smör eller olja (att bryna i)"},
                {"val": 2, "unit": "msk", "name": "spiskummin (malen)"},
                {"val": 2, "unit": "msk", "name": "rökt paprikapulver & chilipulver"},
                {"val": 1, "unit": "tsk", "name": "torkad oregano"},
                {"val": 3, "unit": "msk", "name": "tomatpuré"}
            ]},
            {"group": "Bönor & Sås", "items": [
                {"val": 2, "unit": "burkar", "name": "krossade tomater (à 400g)"},
                {"val": 1, "unit": "burk", "name": "kidneybönor (à 400g, sköljda)"},
                {"val": 1, "unit": "burk", "name": "svarta bönor eller vita bönor (à 400g, sköljda)"},
                {"val": 1, "unit": "burk", "name": "majskorn (à 150g)"},
                {"val": 3, "unit": "dl", "name": "vatten + 2 msk oxfond"},
                {"val": 25, "unit": "g", "name": "mörk choklad (70% kakao – ger magiskt djup)"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Servering & Tillbehör", "items": [
                {"val": 6, "unit": "portioner", "name": "kokt jasminris eller basmatiris"},
                {"val": 2, "unit": "dl", "name": "gräddfil eller crème fraiche"},
                {"val": 1, "unit": "påse", "name": "salta nachochips / tortillachips"},
                {"val": 1, "unit": "kruka", "name": "färsk koriander"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Fräs lök, vitlök och kryddor", "text": "Hetta upp olja/smör i en gjutjärnsgryta. Fräs lök, vitlök och chili i 3 minuter. Tillsätt spiskummin, rökt paprika och oregano och låt fräsa med 1 minut så att kryddorna vaknar till liv.", "timer": 4},
            {"step": 2, "title": "Bryn nötfärsen & tomatpuré", "text": "Tillsätt nötfärsen och bryn på medelhög värme under omrörning så den smular sig. Klicka i tomatpurén och fräs i 2 minuter.", "timer": 5},
            {"step": 3, "title": "Koka upp grytan", "text": "Häll i krossade tomater, vatten och oxfond. Salta och peppra. Koka upp och sänk sedan värmen till svag.", "timer": 3},
            {"step": 4, "title": "Långkok på svag värme", "text": "Låt chilin sjuda sakta under lock i ca 25–30 minuter så att köttet blir otroligt smakrikt och mört.", "timer": 25},
            {"step": 5, "title": "Tillsätt bönor, majs & mörk choklad", "text": "Skölj bönorna och rör ner dem tillsammans med majs och den mörka chokladen. Låt sjuda ytterligare 5–10 minuter tills chokladen smält in och såsen blivit mörk och fyllig.", "timer": 8},
            {"step": 6, "title": "Servera med tillbehör", "text": "Ös upp chilin i djupa skålar. Toppa med en sval klick gräddfil, hackad koriander och servera med ris och krispiga nachochips.", "timer": None}
        ],
        "pro_tips": "En ruta 70% mörk choklad i slutet tar bort den skarpa tomatsyran och ger en djup, fyllig och sammetslen smak som gör din chili helt unik!",
        "nutrition": {"calories": "490 kcal", "protein": "36g", "carbs": "45g", "fat": "18g", "sugar": "6g"},
        "faqs": [
            {"q": "Varför ha mörk choklad i chili con carne?", "a": "Det är ett klassiskt mexikanskt knep (likt Mole) – kakaon fördjupar kött- och chilikryddorna och ger en mörkare, mer aptitlig färg."},
            {"q": "Hur gör man chilin mildare för barn?", "a": "Uteslut färsk chili och minska mängden chilipulver, servera med extra mycket svalkande gräddfil och ris."}
        ],
        "community_reviews": [
            {"name": "Marcus Eklund", "date": "Idag", "rating": 5, "comment": "Chokladknepet var helt otroligt! Djupaste och godaste chilin jag någonsin ätit.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-torsk-med-aggsas",
        "file": "klassisk-torsk-med-aggsas.html",
        "img": "torskaggsas",
        "title": "Klassisk Ugnsbakad Torskrygg med Krämig Äggsås & Dill",
        "card_title": "Torsk med Äggsås",
        "sub": "Mjäll torskrygg i ugn med rik äggsås & dillslungad potatis",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Fisk & Skaldjur",
        "difficulty": "Enkel",
        "time": 30,
        "prep_time": "PT15M",
        "cook_time": "PT15M",
        "total_time": "PT30M",
        "prep_time_str": "15 min",
        "cook_time_str": "15 min",
        "time_str": "30 min",
        "calories": 420,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 610,
        "desc": "En av den svenska husmanskostens allra finaste rätter. Mjäll, saftig torskrygg som bakas perfekt i ugnen till 52°C, serverad med en klassisk silkeslen äggsås fylld med hackade ägg, nyskuren dill och skirat smör.",
        "long_desc": "Torsk med äggsås är en tidlös svensk klassiker som kombinerar den milda, saftiga torsken med en rik smör- och gräddbaserad äggsås. Genom att rimma torsken lätt i saltlake innan tillagning blir fiskköttet fast och ljuvligt smakrikt.",
        "keywords": "torsk med äggsås, äggsås, torskrygg i ugn, äggsås recept, torsk med äggsås och potatis, bästa äggsåsen, klassisk torsk äggsås",
        "alt": "Närbild på saftig vit ugnsbakad torskrygg dränkt i krämig gul äggsås med hackade ägg, färsk dill och ångande potatis",
        "equipment": ["Ugnsfast form", "Kastrull till sås & äggkokare", "Äggdelare"],
        "drink_pairing": "Ett friskt och mineraliskt vitt vin som Chablis, Sauvignon Blanc, eller en ljus svensk lager.",
        "ingredients": [
            {"group": "Torskrygg", "items": [
                {"val": 600, "unit": "g", "name": "färsk torskrygg (i 4 portionsbitar)"},
                {"val": 2, "unit": "msk", "name": "smör (hyvlat över fisken)"},
                {"val": 1, "unit": "tsk", "name": "flingsalt & vitpeppar"},
                {"val": 1, "unit": "klyfta", "name": "citron (färskpressad saft)"}
            ]},
            {"group": "Klassisk Krämig Äggsås", "items": [
                {"val": 4, "unit": "st", "name": "hårdkokta ägg (skalade & hackade)"},
                {"val": 3, "unit": "msk", "name": "smör"},
                {"val": 2.5, "unit": "msk", "name": "vetemjöl"},
                {"val": 3, "unit": "dl", "name": "standardmjölk"},
                {"val": 1.5, "unit": "dl", "name": "vispgrädde"},
                {"val": 1, "unit": "msk", "name": "koncentrerad fisk- eller hummerfond"},
                {"val": 1, "unit": "kruka", "name": "färsk dill (fint hackad)"},
                {"val": 1, "unit": "tsk", "name": "citronsaft & vitpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "portioner", "name": "kokt delikatesspotatis eller mandelpotatis med dill"},
                {"val": 200, "unit": "g", "name": "gröna ärter (slungade i smör)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Rimma torsken & koka ägg", "text": "Sätt ugnen på 150°C. Salta torskryggsbitarna lätt och låt stå i 10 minuter (gör köttet fast och fint). Hårdkoka under tiden äggen (ca 9 minuter), spola i kallt vatten, skala och hacka dem.", "timer": 10},
            {"step": 2, "title": "Baka torsken i ugn", "text": "Lägg torskbitarna i en smord ugnsform. Klicka över lite smör och peppra lätt. Baka mitt i ugnen i ca 12–15 minuter tills innertemperaturen är 50–52°C och fiskköttet skivar sig vackert.", "timer": 15},
            {"step": 3, "title": "Gör bottenredningen till såsen", "text": "Smält 3 msk smör i en kastrull. Vispa ner vetemjölet och låt fräsa 1 minut på svag värme utan att ta färg.", "timer": 2},
            {"step": 4, "title": "Koka upp den lena såsen", "text": "Vispa gradvis i mjölk, grädde och fiskfond. Låt såsen koka upp under ständig vispning och sjuda sakta i 5 minuter så att mjölsmaken försvinner och såsen blir tjock och glansig.", "timer": 5},
            {"step": 5, "title": "Vänd ner ägg och dill", "text": "Dra såskastrullen från värmen. Smaka av med salt, vitpeppar och lite citronsaft. Vänd ner de hackade äggen och den nyskurna dillen.", "timer": 2},
            {"step": 6, "title": "Servera genast", "text": "Lägg upp den mjälla torskryggen på varma tallrikar, ös över rikligt med varm äggsås och servera med nykokt dillpotatis och gröna ärter.", "timer": None}
        ],
        "pro_tips": "Använd en digital termometer i den tjockaste delen av torskryggen – ta ut den vid exakt 50–52°C. Då är torsken otroligt saftig och faller isär i perfekta lameller.",
        "nutrition": {"calories": "420 kcal", "protein": "42g", "carbs": "16g", "fat": "22g", "sugar": "4g"},
        "faqs": [
            {"q": "Varför ska man rimma eller salta torsken i förväg?", "a": "Saltet drar ur lite ytvätska och stramar upp proteinerna vilket gör torskbitarna fastare så att de inte faller sönder under tillagning."},
            {"q": "Kan man göra äggsåsen på bara mjölk?", "a": "Ja, det går utmärkt, men 1.5 dl vispgrädde ger såsen den klassiska fylligheten och rundheten som gör rätten till en festmåltid."}
        ],
        "community_reviews": [
            {"name": "Lars-Erik Nilsson", "date": "Idag", "rating": 5, "comment": "Bästa torsk med äggsås jag någonsin ätit! Fisken var perfekt saftig och såsen underbart krämig.", "verified": True}
        ]
    },
    {
        "slug": "gammaldags-svensk-artsoppa-flask",
        "file": "gammaldags-svensk-artsoppa-flask.html",
        "img": "artsoppa",
        "title": "Gammaldags Svensk Ärtsoppa med Rimmat Fläsk & Timjan",
        "card_title": "Gammaldags Ärtsoppa",
        "sub": "Torsdagsklassikern. Långkokta gula ärter med mjukt rimmat fläsk",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Soppor",
        "difficulty": "Medel",
        "time": 90,
        "prep_time": "PT15M",
        "cook_time": "PT75M",
        "total_time": "PT90M",
        "prep_time_str": "15 min (plus blötläggning)",
        "cook_time_str": "1 tim 15 min",
        "time_str": "1 tim 30 min",
        "calories": 490,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 540,
        "desc": "Sveriges mest anrika husmansklassiker! Gammaldags ärtsoppa kokt från grunden på svenska gula ärter, mörkokt rimmat sidfläsk, gul lök, timjan och mejram. Serveras rykande het med stark skånsk senap och knäckebröd.",
        "long_desc": "Den klassiska svenska torsdagssoppan som har serverats sedan medeltiden. Hemligheten bakom en perfekt krämig ärtsoppa är att låta de blötlagda ärterna koka sakta tillsammans med fläsket och kryddorna så att ärterna mosas lätt och skapar en tjock, fyllig soppa.",
        "keywords": "ärtsoppa, ärtsoppa recept, svensk ärtsoppa, gul ärtsoppa med fläsk, klassisk ärtsoppa, ärtsoppa och pannkakor, torsdagsärtsoppa",
        "alt": "Närbild på en skål traditionell tjock svensk gul ärtsoppa med möra fläsktärningar, timjan och en klick grov skånsk senap",
        "equipment": ["Stor soppgryta (ca 4-5 liter)", "Skumslev", "Skärbräda & kockkniv"],
        "drink_pairing": "Varm svensk punsch (Carlshamns Flaggpunsch), kall öl eller iskall mjölk.",
        "ingredients": [
            {"group": "Ärtsoppa", "items": [
                {"val": 500, "unit": "g", "name": "gula torkade ärter (svenska, blötlagda över natten)"},
                {"val": 600, "unit": "g", "name": "rimmat sidfläsk eller rimmad fläsklägg (i hel bit)"},
                {"val": 1.5, "unit": "liter", "name": "vatten (friskt vatten till koket)"},
                {"val": 1, "unit": "st", "name": "stor gul lök (finhackad eller hel med nejlikor)"},
                {"val": 1.5, "unit": "tsk", "name": "torkad timjan (smulad)"},
                {"val": 1.5, "unit": "tsk", "name": "torkad mejram (smulad)"},
                {"val": 2, "unit": "st", "name": "lagerblad"},
                {"val": 1, "unit": "tsk", "name": "salt (efter avsmakning, fläsket ger sälta)"},
                {"val": 0.5, "unit": "tsk", "name": "nymalen svartpeppar eller vitpeppar"}
            ]},
            {"group": "Klassiska Tillbehör", "items": [
                {"val": 1, "unit": "burk", "name": "stark och söt skånsk senap eller grovkornig dijonsenap"},
                {"val": 6, "unit": "skivor", "name": "gott knäckebröd med smör och lagrad prästost"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Blötlägg ärterna", "text": "Lägg de gula ärterna i rikligt med kallt vatten i en stor bunke. Låt stå och svälla i minst 10–12 timmar (gärna över natten). Häll av blötläggningsvattnet.", "timer": 10},
            {"step": 2, "title": "Koka upp & skumma av", "text": "Lägg de svällda ärterna i en stor gryta och häll på 1.5 liter nytt vatten. Koka upp och skumma noga av det vita skummet och eventuella ärtskal som flyter upp till ytan.", "timer": 10},
            {"step": 3, "title": "Tillsätt fläsk, lök & örter", "text": "Lägg i det rimmade fläsket i hel bit, finhackad gul lök, timjan, mejram, lagerblad och svartpeppar. Koka upp igen.", "timer": 5},
            {"step": 4, "title": "Långkok under lock", "text": "Sänk värmen, lägg på locket och låt soppan sjuda sakta i ca 1 timme till 1 timme och 15 minuter tills ärterna är helt mjuka och börjar mosa sig naturligt.", "timer": 65},
            {"step": 5, "title": "Skär upp fläsket", "text": "Ta upp det möra fläsket ur grytan och skär det i fina munsbitar. Lägg tillbaka köttet i soppan (eller servera det vid sidan om på ett fat).", "timer": 5},
            {"step": 6, "title": "Smaka av och servera", "text": "Mosa eventuellt några ärter med en ballongvisp för extra krämighet. Smaka av med salt och lite extra timjan. Servera rykande het med massor av god senap!", "timer": None}
        ],
        "pro_tips": "Skumma alltid noga av soppan precis vid uppkoket innan kryddorna läggs i. Då får du en ren, klar och sammetslen soppa utan beska ärtskal.",
        "nutrition": {"calories": "490 kcal", "protein": "32g", "carbs": "48g", "fat": "18g", "sugar": "3g"},
        "faqs": [
            {"q": "Måste man blötlägga gula ärter?", "a": "Ja, blötläggning i 10–12 timmar halverar koktiden och gör att alla ärter kokar sönder jämnt och skapar rätt fylliga konsistens."},
            {"q": "Vad gör man om soppan blir för tjock?", "a": "Ärtsoppa tjocknar när den står. Späd bara med lite hett vatten eller buljong tills du får önskad konsistens."}
        ],
        "community_reviews": [
            {"name": "Gunnar Holmberg", "date": "Idag", "rating": 5, "comment": "Riktig husmanskost när den är som bäst! Timjanen och fläsket gav en otrolig smak.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-silviakaka-langpanna",
        "file": "klassisk-silviakaka-langpanna.html",
        "img": "silviakaka",
        "title": "Klassisk Silviakaka i Långpanna – Saftig Kaka med Vaniljglasyr",
        "card_title": "Klassisk Silviakaka",
        "sub": "Mjuk sockerkaka med krämig smör- och vaniljglasyr & kokos",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 35,
        "prep_time": "PT15M",
        "cook_time": "PT20M",
        "total_time": "PT35M",
        "prep_time_str": "15 min",
        "cook_time_str": "20 min",
        "time_str": "35 min",
        "calories": 360,
        "portions_num": 16,
        "portions_unit": "bitar",
        "rating": 4.99,
        "review_count": 680,
        "desc": "Sveriges mest älskade långpannekaka! En otroligt saftig och luftig sockerkaksbotten täckt med en generös, krämig och fyllig smör- och vaniljglasyr samt massor av riven kokos. Perfekt till kalas och fika.",
        "long_desc": "Silviakaka (döpt efter Drottning Silvia) är den ultimata fikafavoriten. Hemligheten bakom den oemotståndliga smaken är den kokta vaniljglasyren som görs på äggulor, smör, socker och äkta vanilj som hälls varm över den nygräddade kakan.",
        "keywords": "silviakaka, silviakaka recept, silviakaka i långpanna, drottning silvia kaka, saftig silviakaka, bästa silviakakan, vaniljkaka med kokos",
        "alt": "Närbild på en saftig kvadratisk bit gyllene Silviakaka med tjock glänsande vaniljglasyr och rikligt med riven kokos",
        "equipment": ["Liten långpanna (ca 25x35 cm)", "Elvisp", "Kastrull till glasyr"],
        "drink_pairing": "En stor kopp nybryggt svenskt kaffe, en krämig caffe latte eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Saftig Sockerkaksbotten", "items": [
                {"val": 4, "unit": "st", "name": "stora ägg"},
                {"val": 3.5, "unit": "dl", "name": "strösocker"},
                {"val": 4, "unit": "dl", "name": "vetemjöl"},
                {"val": 3, "unit": "tsk", "name": "bakpulver"},
                {"val": 2, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 1.5, "unit": "dl", "name": "kallt vatten"}
            ]},
            {"group": "Krämig Silviaglasyr", "items": [
                {"val": 150, "unit": "g", "name": "smör"},
                {"val": 1.5, "unit": "dl", "name": "strösocker"},
                {"val": 2, "unit": "st", "name": "äggulor"},
                {"val": 2, "unit": "msk", "name": "vaniljsocker (av god kvalitet)"}
            ]},
            {"group": "Garnering", "items": [
                {"val": 1.5, "unit": "dl", "name": "riven kokos"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ugn & långpanna", "text": "Sätt ugnen på 175°C över-/undervärme. Klä en liten långpanna (ca 25x35 cm) med bakplåtspapper.", "timer": 5},
            {"step": 2, "title": "Vispa kaksmeten", "text": "Vispa ägg och strösocker riktigt vitt och pösigt med elvisp i ca 4–5 minuter. Blanda vetemjöl, bakpulver och vaniljsocker i en skål.", "timer": 5},
            {"step": 3, "title": "Vänd ner mjöl & vatten", "text": "Sikta ner mjölblandningen växelvis med det kalla vattnet i äggsmeten. Vänd försiktigt ihop till en jämn och luftig smet.", "timer": 3},
            {"step": 4, "title": "Grädda sockerkakan", "text": "Häll smeten i långpannan och grädda mitt i ugnen i ca 18–20 minuter tills kakan är gyllene och genomgräddad.", "timer": 20},
            {"step": 5, "title": "Koka den magiska glasyren", "text": "Smält smöret i en kastrull på svag värme. Rör ner strösocker, äggulor och vaniljsocker. Låt sjuda under ständig vispning på svag värme tills glasyren tjocknar till en krämig sås (får inte stormkoka!).", "timer": 5},
            {"step": 6, "title": "Bred på glasyr & toppa med kokos", "text": "Häll den varma vaniljglasyren jämnt över den varma kakan. Strö rikligt med riven kokos över hela kakan. Låt stelna och skär i fina rutor.", "timer": 15}
        ],
        "pro_tips": "Låt glasyren sjuda sakta på låg värme medan du vispar – äggulorna gör att den tjocknar till en ljuvlig vaniljkräm. Häll glasyren över kakan medan kakan fortfarande är ljummen så suger bottnen åt sig massor av saftighet!",
        "nutrition": {"calories": "360 kcal", "protein": "5g", "carbs": "48g", "fat": "17g", "sugar": "32g"},
        "faqs": [
            {"q": "Varför tillsätter man vatten i kaksmeten?", "a": "Det kalla vattnet gör att sockerkakan blir otroligt luftig, fuktig och hög utan att bli tung."},
            {"q": "Kan man frysa in Silviakaka?", "a": "Ja, Silviakaka är perfekt att frysa i bitar med bakplåtspapper emellan och tinar snabbt i rumstemperatur."}
        ],
        "community_reviews": [
            {"name": "Evelina Söderström", "date": "Idag", "rating": 5, "comment": "Den godaste långpannekakan i världen! Glasyren är så krämig och kakan blev otroligt saftig.", "verified": True}
        ]
    },
    {
        "slug": "kramig-kycklinggryta-dragon-dijon",
        "file": "kramig-kycklinggryta-dragon-dijon.html",
        "img": "kycklinggryta",
        "title": "Krämig Kycklinggryta med Dragon, Dijon & Champinjoner",
        "card_title": "Krämig Kycklinggryta",
        "sub": "Mör kyckling i fyllig dragonsås med dijonsenap & svamp",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Fågel / Grytor",
        "difficulty": "Enkel",
        "time": 40,
        "prep_time": "PT15M",
        "cook_time": "PT25M",
        "total_time": "PT40M",
        "prep_time_str": "15 min",
        "cook_time_str": "25 min",
        "time_str": "40 min",
        "calories": 520,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 510,
        "desc": "En underbart god och krämig kycklinggryta med inspiration från det franska lantköket. Saftiga kycklingbitar steks gyllenbruna och får sjuda i en fyllig sås på vispgrädde, torrt vitt vin, dijonsenap, färsk dragon och smörstekta champinjoner.",
        "long_desc": "Den ultimata höstgrytan som passar lika bra en onsdagskväll som till helgmiddagen. Kombinationen av fransk dragon, skarp dijonsenap och len grädde skapar en sås med fantastisk elegans och djup.",
        "keywords": "kycklinggryta, krämig kycklinggryta, kycklinggryta recept, kycklinggryta med dragon och dijon, godaste kycklinggrytan, fransk kycklinggryta",
        "alt": "Närbild på en gjutjärnspanna med krämig kycklinggryta, gyllene kycklingfiléer, stekta champinjoner, färska dragonblad och sås",
        "equipment": ["Gjutjärnspanna eller traktörpanna", "Skärbräda & kockkniv", "Träslev"],
        "drink_pairing": "Ett fylligt vitt vin som ekfatslagrad Chardonnay eller ett lätt bärigt rött vin som Pinot Noir.",
        "ingredients": [
            {"group": "Kyckling & Svamp", "items": [
                {"val": 600, "unit": "g", "name": "svensk kycklinglårfilé eller bröstfilé (i lagom grytbitar)"},
                {"val": 250, "unit": "g", "name": "färska skogschampinjoner (skivade eller kvartade)"},
                {"val": 2, "unit": "st", "name": "schalottenlökar (finhackade)"},
                {"val": 2, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 2, "unit": "msk", "name": "smör och 1 msk rapsolja (att steka i)"}
            ]},
            {"group": "Krämig Dragonsås", "items": [
                {"val": 1.5, "unit": "dl", "name": "torrt vitt vin (eller matlagningsvin)"},
                {"val": 3, "unit": "dl", "name": "vispgrädde"},
                {"val": 1, "unit": "dl", "name": "creme fraiche"},
                {"val": 2, "unit": "msk", "name": "koncentrerad kycklingfond"},
                {"val": 2, "unit": "msk", "name": "dijonsenap (fransk senap)"},
                {"val": 2, "unit": "msk", "name": "färsk dragon (finhackad) eller 1 msk torkad dragon"},
                {"val": 1, "unit": "tsk", "name": "soja (för färg och sälta)"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "portioner", "name": "pressad potatis, ris eller ugnsrostade rotfrukter"},
                {"val": 1, "unit": "kruka", "name": "färsk dragon (till garnering)"},
                {"val": 1, "unit": "skål", "name": "krispig grönsallad"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Bryn champinjonerna", "text": "Hetta upp 1 msk smör i en gjutjärnspanna. Stek champinjonerna på hög värme tills de släppt sin vätska och fått fin gyllenbrun färg. Lägg över på en tallrik.", "timer": 6},
            {"step": 2, "title": "Bryn kycklingen", "text": "Skär kycklingen i fina munsbitar och krydda med salt och svartpeppar. Hetta upp resterande smör och olja i pannan och bryn kycklingen i ca 5 minuter så den får fin färg runt om.", "timer": 5},
            {"step": 3, "title": "Fräs lök & koka in vinet", "text": "Tillsätt schalottenlök och vitlök i pannan och låt fräsa med i 2 minuter. Häll i det vita vinet och låt koka in till hälften under 2 minuter.", "timer": 4},
            {"step": 4, "title": "Tillsätt grädde, dijon & fond", "text": "Häll i vispgrädde, crème fraiche, kycklingfond, dijonsenap och soja. Rör om och låt grytan sjuda sakta på medelvärme i ca 10–12 minuter tills kycklingen är helt mör och genomstekt.", "timer": 12},
            {"step": 5, "title": "Vänd ner svamp och färsk dragon", "text": "Rör ner de stekta champinjonerna och den nyskurna färska dragonen. Låt sjuda i ytterligare 2–3 minuter så smakerna förenas. Smaka av med salt och peppar.", "timer": 3},
            {"step": 6, "title": "Garnera & servera", "text": "Toppa grytan med färska dragonblad och nymalen svartpeppar. Servera rykande het med pressad potatis eller fluffigt ris.", "timer": None}
        ],
        "pro_tips": "Använd kycklinglårfilé istället för kycklingbröst om du vill ha extra saftigt kött som tål att sjuda i såsen utan att någonsin bli torrt.",
        "nutrition": {"calories": "520 kcal", "protein": "38g", "carbs": "8g", "fat": "38g", "sugar": "3g"},
        "faqs": [
            {"q": "Kan man byta ut vinet?", "a": "Ja! Ersätt vitt vin med 1.5 dl kycklingbuljong och 1 tsk vitvinsvinäger eller citronsaft för att behålla syran."},
            {"q": "Färsk eller torkad dragon?", "a": "Färsk fransk dragon ger den mest eleganta smaken, men torkad dragon fungerar också utmärkt (tillsätt den då tidigare i koket)."}
        ],
        "community_reviews": [
            {"name": "Katarina Wallin", "date": "Idag", "rating": 5, "comment": "Såsen är helt makalöst god! Dijonsenapen och dragonen ger en fantastisk restaurangkänsla.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-ugnsstekt-falukorv-applen-ost",
        "file": "klassisk-ugnsstekt-falukorv-applen-ost.html",
        "img": "falukorv",
        "title": "Klassisk Ugnsstekt Falukorv med Äpple, Senap & Lagrad Ost",
        "card_title": "Ugnsstekt Falukorv",
        "sub": "Frasigt gratinerad falukorv med äpplen, senap & potatismos",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Enkel",
        "time": 35,
        "prep_time": "PT15M",
        "cook_time": "PT20M",
        "total_time": "PT35M",
        "prep_time_str": "15 min",
        "cook_time_str": "20 min",
        "time_str": "35 min",
        "calories": 480,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 640,
        "desc": "En älskad svensk vardagsklassiker för hela familjen! Falukorv skårad och fylld med syrliga svenska äppelklyftor, dijonsenap, söta tomater och rikligt med lagrad ost som smälter till en gyllene frasig yta. Serveras med krämigt potatismos.",
        "long_desc": "Ugnsstekt falukorv är svensk husmanskost när den är som enklast och godast. Genom att varva syrliga äppelskivor med skarp senap och smakrik ost i snitten balanseras korvens sälta perfekt och ger en otroligt saftig rätt.",
        "keywords": "falukorv i ugn, ugnsstekt falukorv, ugnsbakad falukorv, falukorv recept, falukorv med äpple och senap, enkel falukorv i ugn",
        "alt": "Närbild på ugnsstekt böjd falukorv gratinerad med smält ost, skivade äpplen och tomater i emaljform med fluffigt potatismos",
        "equipment": ["Ugnsform", "Skärbräda & kockkniv", "Potatisstöt eller elvisp till mos"],
        "drink_pairing": "En frisk svensk lättöl, äppelmust eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Falukorv & Fyllning", "items": [
                {"val": 800, "unit": "g", "name": "falukorv av hög kötthalt (minst 65-70% kött)"},
                {"val": 1.5, "unit": "st", "name": "syrliga svenska äpplen (skivade i tunna halvmånar)"},
                {"val": 2, "unit": "st", "name": "mogna tomater (skivade i halvmånar)"},
                {"val": 2, "unit": "msk", "name": "svensk sötstark senap eller grov dijonsenap"},
                {"val": 2, "unit": "msk", "name": "tomatpuré eller chilisås"},
                {"val": 2.5, "unit": "dl", "name": "riven lagrad ost (t.ex. Prästost eller Västerbottensost)"},
                {"val": 1, "unit": "krm", "name": "svartpeppar & torkad timjan eller oregano"}
            ]},
            {"group": "Krämigt Potatismos", "items": [
                {"val": 1, "unit": "kg", "name": "mjölig potatis (t.ex. King Edward)"},
                {"val": 50, "unit": "g", "name": "smör"},
                {"val": 2, "unit": "dl", "name": "varm mjölk"},
                {"val": 1, "unit": "krm", "name": "riven muskotnöt, salt & vitpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 1, "unit": "kruka", "name": "färsk persilja (hackad)"},
                {"val": 1, "unit": "skål", "name": "inlagd gurka / pressgurka"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Sätt ugnen & förbered korven", "text": "Sätt ugnen på 225°C över-/undervärme. Dra skinnet av falukorven och lägg den i en smord ugnsform. Skär djupa snitt i korven med ca 1–1.5 cm mellanrum, men skär inte hela vägen igenom.", "timer": 5},
            {"step": 2, "title": "Fyll snitten med äpple, tomat & senap", "text": "Bred lite senap och chilisås i varje snitt. Stoppa ner en äppelskiva och en tomatskiva i varje skåra så att korven bågnar vackert.", "timer": 5},
            {"step": 3, "title": "Toppa med rikligt med ost", "text": "Strö över den rivna osten, lite torkad timjan och nymalen svartpeppar.", "timer": 2},
            {"step": 4, "title": "Gratinera i ugnen", "text": "Ställ formen mitt i ugnen och gratinera i ca 20 minuter tills korven är genomvarm, äpplena mjuknat och osten blivit bubblande gyllenbrun och krispig.", "timer": 20},
            {"step": 5, "title": "Gör det fluffiga potatismoset", "text": "Skala och koka potatisen mjuk i saltat vatten. Häll av och stöt potatisen. Rör ner smör och varm mjölk med elvisp till ett luftigt, lent mos. Smaka av med salt, vitpeppar och lite muskotnöt.", "timer": 15},
            {"step": 6, "title": "Servera rykande het", "text": "Strö färsk persilja över falukorven och servera direkt ur formen tillsammans med det varma potatismoset och krispig pressgurka.", "timer": None}
        ],
        "pro_tips": "Använd en syrlig äppelsort som Ingrid Marie eller Granny Smith tillsammans med en lagrad prästost – kombinationen av fruktsyra, sälta och umami lyfter falukorven till en riktig festmåltid.",
        "nutrition": {"calories": "480 kcal", "protein": "24g", "carbs": "32g", "fat": "28g", "sugar": "6g"},
        "faqs": [
            {"q": "Varför ska man välja falukorv med hög kötthalt?", "a": "Falukorv med minst 65–70% kötthalt ger mycket bättre smak och konsistens som håller formen i ugnen utan att släppa överflödigt vatten."},
            {"q": "Kan man förbereda formen i förväg?", "a": "Ja, du kan snitta och fylla falukorven timmar i förväg och förvara formen plastad i kylen tills det är dags att sätta på ugnen."}
        ],
        "community_reviews": [
            {"name": "Helena Nyström", "date": "Idag", "rating": 5, "comment": "Äpplet och den lagrade osten i snitten gör denna falukorv helt magiskt god! Barnen älskade den.", "verified": True}
        ]
    },
    {
        "slug": "kramig-kantarellsoppa-vitt-vin-timjan",
        "file": "kramig-kantarellsoppa-vitt-vin-timjan.html",
        "img": "kantarellsoppa",
        "title": "Krämig Kantarellsoppa med Vitt Vin, Timjan & Västerbottensost",
        "card_title": "Krämig Kantarellsoppa",
        "sub": "Skogens guld i en sammetslen soppa med smörstekta kantareller",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Vegetariskt / Soppor",
        "difficulty": "Enkel",
        "time": 30,
        "prep_time": "PT10M",
        "cook_time": "PT20M",
        "total_time": "PT30M",
        "prep_time_str": "10 min",
        "cook_time_str": "20 min",
        "time_str": "30 min",
        "calories": 380,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 590,
        "desc": "En lyxig, sammetslen och fyllig kantarellsoppa gjord på färska gyllengula kantareller, scharlottenlök, vitt vin, grönsaksbuljong och äkta vispgrädde. Toppas med smörstekta hela kantareller och krispig osttoast.",
        "long_desc": "Hösten på en tallrik! Färska kantareller som förvälls och steks i rikligt med smör utvecklar den karakteristiska nötiga och aromatiska skogssmaken som gör denna soppa till en storfavorit både som förrätt och höstmiddag.",
        "keywords": "kantarellsoppa, kantarellsoppa recept, svampsoppa, krämig svampsoppa, godaste kantarellsoppan, kantarellsoppa med vitt vin, förrätt kantarellsoppa",
        "alt": "Närbild på en skål sammetslen gyllene kantarellsoppa toppad med smörstekta kantareller, gräddvirvel, timjan och en rostad västerbottensost-toast",
        "equipment": ["Soppkastrull", "Stavmixer", "Stekpanna till kantareller"],
        "drink_pairing": "Ett ekfatslagrat fylligt Chardonnay, torr cider eller ett friskt bubbel som Cava.",
        "ingredients": [
            {"group": "Kantarellsoppa", "items": [
                {"val": 500, "unit": "g", "name": "färska kantareller (rensade, eller 250g förvällda)"},
                {"val": 2, "unit": "st", "name": "schalottenlökar (finhackade)"},
                {"val": 1, "unit": "klyfta", "name": "vitlök (finhackad)"},
                {"val": 3, "unit": "msk", "name": "smör (att steka svampen i)"},
                {"val": 2, "unit": "msk", "name": "vetemjöl"},
                {"val": 1.5, "unit": "dl", "name": "torrt vitt vin eller matlagningsvin"},
                {"val": 5, "unit": "dl", "name": "vatten + 2 msk koncentrerad svampfond eller grönsaksfond"},
                {"val": 3, "unit": "dl", "name": "vispgrädde"},
                {"val": 1, "unit": "msk", "name": "färsk timjan (hackad)"},
                {"val": 1, "unit": "tsk", "name": "citronsaft, salt & nymalen svartpeppar"}
            ]},
            {"group": "Servering & Osttoast", "items": [
                {"val": 4, "unit": "skivor", "name": "surdegsbröd gratinerade med Västerbottensost"},
                {"val": 1, "unit": "kruka", "name": "färsk timjan (till garnering)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Rensa & stek kantarellerna", "text": "Rensa kantarellerna noga. Lägg dem i en torr, het stekpanna så vätskan ångar bort. Tillsätt sedan 3 msk smör, finhackad schalottenlök och vitlök. Stek på medelvärme i 5 minuter. Ta undan några fina hela kantareller till garnering.", "timer": 8},
            {"step": 2, "title": "Pudra över mjöl & häll på vin", "text": "Pudra vetemjölet över svampen i pannan och rör om. Häll på det vita vinet och låt koka in i 1–2 minuter.", "timer": 3},
            {"step": 3, "title": "Tillsätt buljong & grädde", "text": "Häll i svampbuljongen och vispgrädden samt timjan. Låt soppan koka upp och sjuda sakta i ca 10–12 minuter så smakerna djupnar.", "timer": 12},
            {"step": 4, "title": "Mixa soppan sammetslen", "text": "Mixa soppan slät med en stavmixer (mixa helt slät eller lämna lite bitar för textur). Smaka av med lite färskpressad citronsaft, salt och nymalen svartpeppar.", "timer": 3},
            {"step": 5, "title": "Garnera & servera", "text": "Häll upp den heta soppan i skålar. Toppa med de sparade smörstekta kantarellerna, färsk timjan, en swirl grädde och servera med frasig Västerbottensost-toast.", "timer": None}
        ],
        "pro_tips": "Mixa inte bort alla kantareller – spara alltid en rejäl näve hela smörstekta svampar att lägga på toppen av soppan vid servering för underbar textur och lyxig restaurangkänsla.",
        "nutrition": {"calories": "380 kcal", "protein": "8g", "carbs": "14g", "fat": "32g", "sugar": "3g"},
        "faqs": [
            {"q": "Kan man använda frysta eller torkade kantareller?", "a": "Ja, absolut! Upptina frysta kantareller och krama ur vätskan innan stekning. Torkade kantareller blötläggs i varmt vatten i 30 minuter innan tillagning."},
            {"q": "Går kantarellsoppa att frysa?", "a": "Det går bra att frysa soppan, men gräddbaserade soppor kan skära sig lätt vid upptining. Värm den försiktigt under omrörning på låg värme."}
        ],
        "community_reviews": [
            {"name": "Fredrik Sjöberg", "date": "Idag", "rating": 5, "comment": "Underbar kantarellsoppa! Vinet och timjanen gav en otrolig finess och smakdjup.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-biff-stroganoff-oxfile-smetana",
        "file": "klassisk-biff-stroganoff-oxfile-smetana.html",
        "img": "biffstroganoff",
        "title": "Klassisk Biff Stroganoff med Oxfilé, Champinjoner & Smetana",
        "card_title": "Klassisk Biff Stroganoff",
        "sub": "Mört stekt oxfilé i fyllig smetanasås med dijon & svamp",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Kött",
        "difficulty": "Medel",
        "time": 30,
        "prep_time": "PT15M",
        "cook_time": "PT15M",
        "total_time": "PT30M",
        "prep_time_str": "15 min",
        "cook_time_str": "15 min",
        "time_str": "30 min",
        "calories": 540,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 620,
        "desc": "Den äkta lyxiga restaurangversionen av Stroganoff! Fina strimlor av mör oxfilé eller biff som hastigt bryns på hög värme och vänds ner i en sammetslen sås med smörstekta champinjoner, schalottenlök, dijonsenap, tomat och krämig smetana.",
        "long_desc": "Biff Stroganoff är en internationell mästarrätt med rötter från greve Stroganovs ryska kök. Kärnan i en perfekt Biff Stroganoff är att inte översteka köttet – bryn biffen snabbt så att den förblir rosa och saftig, och tillsätt den i den varma såsen precis före servering.",
        "keywords": "biff stroganoff, biff stroganoff recept, klassisk biff stroganoff, biff stroganoff oxfilé, bästa biff stroganoff, biff stroganoff med smetana",
        "alt": "Närbild på en djup tallrik med smörslungade äggnudlar toppade med krämig biff stroganoff, oxfiléstrimlor, champinjoner och krispig potatis",
        "equipment": ["Gjutjärnspanna", "Skärbräda & kockkniv", "Träslev"],
        "drink_pairing": "Ett kraftigt rött vin som Syrah, Cabernet Sauvignon eller en klassisk fyllig röd Bordeaux.",
        "ingredients": [
            {"group": "Oxfilé & Svamp", "items": [
                {"val": 600, "unit": "g", "name": "oxfilé, ryggbiff eller entrecôte (strimlad i 1x4 cm bitar)"},
                {"val": 250, "unit": "g", "name": "färska champinjoner eller skogschampinjoner (kvartade)"},
                {"val": 2, "unit": "st", "name": "schalottenlökar (finhackade)"},
                {"val": 2, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 3, "unit": "msk", "name": "smör och 1 msk rapsolja (att steka i)"}
            ]},
            {"group": "Smetanasås", "items": [
                {"val": 2, "unit": "msk", "name": "tomatpuré"},
                {"val": 1.5, "unit": "msk", "name": "dijonsenap"},
                {"val": 1, "unit": "msk", "name": "paprikapulver (sött & lite rökt)"},
                {"val": 1, "unit": "dl", "name": "oxbuljong / kalvfond utspädd med vatten"},
                {"val": 2, "unit": "dl", "name": "smetana eller crème fraiche"},
                {"val": 1, "unit": "dl", "name": "vispgrädde"},
                {"val": 1, "unit": "msk", "name": "kinesisk soja & 1 tsk vitvinsvinäger"},
                {"val": 1, "unit": "tsk", "name": "salt & rikligt med grovmalen svartpeppar"}
            ]},
            {"group": "Servering & Tillbehör", "items": [
                {"val": 4, "unit": "portioner", "name": "smörslungade bandnudlar / tagliatelle eller fluffigt ris"},
                {"val": 4, "unit": "st", "name": "cornichons / saltgurka (finstrimlade)"},
                {"val": 1, "unit": "kruka", "name": "färsk bladpersilja (hackad)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Bryn champinjonerna", "text": "Hetta upp 1 msk smör i en gjutjärnspanna. Stek champinjonerna tills de fått fin gyllenbrun färg. Lyft ur och lägg på en tallrik.", "timer": 5},
            {"step": 2, "title": "Hårdstek biffen snabbt", "text": "Hetta upp pannan tills den ryker med olja och 1 msk smör. Bryn köttstrimlorna i två omgångar i max 1–2 minuter per omgång så att köttet får fin stekyta men behåller en rosa saftig kärna. Lyft ur köttet och lägg på fat.", "timer": 4},
            {"step": 3, "title": "Fräs lök, tomatpuré & kryddor", "text": "Sänk värmen i samma panna. Fräs schalottenlök och vitlök i 2 minuter. Tillsätt tomatpuré, paprikapulver och dijonsenap. Låt fräsa under omrörning i 1 minut.", "timer": 3},
            {"step": 4, "title": "Koka ihop såsen", "text": "Häll i buljong, smetana, vispgrädde och soja. Låt såsen koka upp och sjuda sakta i 3–4 minuter tills den blir tjock, blank och krämig.", "timer": 4},
            {"step": 5, "title": "Vänd ner kött och svamp", "text": "Vänd ner de stekta champinjonerna och köttstrimlorna inklusive all köttsaft från fatet i såsen. Låt bara bli genomvarmt i 1 minut (koka inte så köttet blir segt!). Smaka av med salt, grovmalen svartpeppar och lite vinäger.", "timer": 2},
            {"step": 6, "title": "Garnera & servera", "text": "Toppa med hackad persilja och servera genast med smörade bandnudlar eller ris samt krispiga cornichons.", "timer": None}
        ],
        "pro_tips": "Stek köttet i en rykande het panna i mycket korta omgångar (max 1–2 minuter). Låt det inte koka i såsen, utan vänd bara ner det precis före servering – då förblir köttet smältande mört.",
        "nutrition": {"calories": "540 kcal", "protein": "38g", "carbs": "12g", "fat": "38g", "sugar": "4g"},
        "faqs": [
            {"q": "Vilket kött passar bäst till Biff Stroganoff?", "a": "Oxfilé ger det möraste resultatet, men ryggbiff, entrecôte eller mörad lövbiff fungerar också utmärkt."},
            {"q": "Varför använda smetana istället för crème fraiche?", "a": "Smetana har en högre fetthalt (42%) och mildare syra vilket ger en otroligt silkeslen och lyxig konsistens som inte skär sig."}
        ],
        "community_reviews": [
            {"name": "Patrik Lindgren", "date": "Idag", "rating": 5, "comment": "Restaurangklass hemma i köket! Smetanasåsen och den perfekt stekta oxfilén var en sensation.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-smalandska-kroppkakor-brynt-smor",
        "file": "klassiska-smalandska-kroppkakor-brynt-smor.html",
        "img": "kroppkakor",
        "title": "Klassiska Småländska Kroppkakor med Rimmat Fläsk & Brynt Smör",
        "card_title": "Småländska Kroppkakor",
        "sub": "Äkta potatiskroppkakor fyllda med kryddpepparfläsk & lingon",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 60,
        "prep_time": "PT30M",
        "cook_time": "PT30M",
        "total_time": "PT60M",
        "prep_time_str": "30 min",
        "cook_time_str": "30 min",
        "time_str": "1 timme",
        "calories": 510,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 580,
        "desc": "Äkta småländska kroppkakor gjorda på kokt potatis, äggula och vetemjöl, fyllda med stekt rimmat fläsk, gul lök och rikligt med nystött kryddpeppar. Serveras med gyllene brynt smör, rårörda lingon och grädde.",
        "long_desc": "En av Sveriges mest ikoniska kulturrätter. Småländska kroppkakor bakas på kokt, pressad potatis vilket ger en härligt mjuk och lätthanterlig deg med en oemotståndlig fyllning av doftande kryddpepparstekt fläsk.",
        "keywords": "kroppkakor, kroppkakor recept, småländska kroppkakor, äkta kroppkakor, kroppkakor med fläsk, öländska kroppkakor, kokta kroppkakor",
        "alt": "Närbild på en delad ångande småländsk kroppkaka fylld med stekt fläsk och lök, simmande i brynt smör med röda rårörda lingon",
        "equipment": ["Potatispress", "Stor kastrull (5 liter)", "Hålslev"],
        "drink_pairing": "En kall svensk lageröl, enbärsdricka eller ett glas iskall mjölk.",
        "ingredients": [
            {"group": "Kroppkakedeg", "items": [
                {"val": 1, "unit": "kg", "name": "mjölig potatis (kokt och kallnad, t.ex. King Edward)"},
                {"val": 2, "unit": "st", "name": "äggulor"},
                {"val": 3, "unit": "dl", "name": "vetemjöl (ca 180g)"},
                {"val": 1, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Klassisk Fläskfyllning", "items": [
                {"val": 300, "unit": "g", "name": "rimmat sidfläsk (fint tärnat)"},
                {"val": 1, "unit": "st", "name": "stor gul lök (finhackad)"},
                {"val": 1.5, "unit": "tsk", "name": "nystött kryddpeppar (hemligheten bakom smaken!)"},
                {"val": 0.5, "unit": "tsk", "name": "nymalen svartpeppar"}
            ]},
            {"group": "Klassisk Servering", "items": [
                {"val": 100, "unit": "g", "name": "smör (brynt till nötbrun färg)"},
                {"val": 2, "unit": "dl", "name": "rårörda lingon"},
                {"val": 1, "unit": "dl", "name": "vispgrädde eller mjölk (tillbehör)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Stek fläskfyllningen", "text": "Stek det tärnade rimmade fläsket i en stekpanna tills det släppt fett. Tillsätt finhackad lök och stek på medelvärme tills löken är mjuk och genomskinlig. Krydda rikligt med nystött kryddpeppar och svartpeppar. Låt svalna helt.", "timer": 10},
            {"step": 2, "title": "Pressa potatisen och gör degen", "text": "Pressa den kalla kokta potatisen genom en potatispress i en stor bunke. Tillsätt äggulor, salt och vetemjöl. Arbeta snabbt ihop till en smidig deg (knåda inte för länge då degen kan bli klibbig).", "timer": 8},
            {"step": 3, "title": "Forma & fyll kroppkakorna", "text": "Dela degen i 12 bitar. Rulla till bollar och gör en djup fördjupning med tummen i varje boll. Fyll med en rågad matsked fläskfyllning. Nyp ihop degen noga runt fyllningen och rulla till jämna, släta runda bollar.", "timer": 12},
            {"step": 4, "title": "Sjud kroppkakorna i saltat vatten", "text": "Koka upp rikligt med vatten med 1 msk salt i en stor gryta. Lägg försiktigt i kroppkakorna med hålslev. När de flyter upp till ytan sänker du värmen och låter dem sjuda sakta i ca 10–12 minuter.", "timer": 12},
            {"step": 5, "title": "Bryn smöret", "text": "Smält 100g smör i en kastrull och låt det bubbla på medelvärme tills det tystnar, doftar nötigt och får en vacker bärnstensbrun färg.", "timer": 5},
            {"step": 6, "title": "Servera med lingon & smör", "text": "Lyft upp kroppkakorna med hålslev och lägg i djupa tallrikar. Häll över rikligt med brynt smör och servera med rårörda lingon och lite grädde.", "timer": None}
        ],
        "pro_tips": "Använd kall, kokt potatis – gärna från gårdagen. Varm potatis smälter mjölet och gör degen klistrig, medan kall potatis ger en perfekt formbar deg.",
        "nutrition": {"calories": "510 kcal", "protein": "16g", "carbs": "52g", "fat": "26g", "sugar": "8g"},
        "faqs": [
            {"q": "Vad är skillnaden mellan småländska och öländska kroppkakor?", "a": "Småländska kroppkakor görs på enbart kokt potatis (ljusa och mjuka), medan öländska kroppkakor (gråa kroppkakor) görs på en blandning av riven rå potatis och kokt potatis."},
            {"q": "Vad gör man med överblivna kroppkakor?", "a": "Kroppkakor är nästan ännu godare dagen efter! Skär dem i halvor och stek dem gyllenbruna och frasiga i smör i stekpannan."}
        ],
        "community_reviews": [
            {"name": "Ingrid Petersson", "date": "Idag", "rating": 5, "comment": "Underbara kroppkakor! Kryddpepparn i fyllningen gav den exakta smaken som min mormor i Småland gjorde dem.", "verified": True}
        ]
    },
    {
        "slug": "segmjuka-kolasnittar-kolakakor",
        "file": "segmjuka-kolasnittar-kolakakor.html",
        "img": "kolakakor",
        "title": "Segmjuka Kolasnittar – Klassiska Kolakakor med Flingsalt",
        "card_title": "Segmjuka Kolasnittar",
        "sub": "Sega, knapriga & gyllene småkakor med sirap & flingsalt",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 25,
        "prep_time": "PT10M",
        "cook_time": "PT15M",
        "total_time": "PT25M",
        "prep_time_str": "10 min",
        "cook_time_str": "15 min",
        "time_str": "25 min",
        "calories": 120,
        "portions_num": 30,
        "portions_unit": "kakor",
        "rating": 4.99,
        "review_count": 720,
        "desc": "Sveriges mest bakade småkaka! Underbart sega i mitten och härligt frasiga i kanterna med en djup smak av karamelliserad ljus sirap, vanilj och ett strössel av havssalt. Bakas i längder och snittas direkt ur ugnen.",
        "long_desc": "Kolasnittar (även kända som kolakakor eller sirapskakor) är en klassisk svensk småkaka som går otroligt snabbt att baka. Hemligheten bakom den oemotståndliga segheten är balansen mellan smör, ljus sirap och att skära kakorna medan de fortfarande är varma.",
        "keywords": "kolakakor, kolasnittar, kolasnittar recept, sirapskakor, sega kolakakor, kolakakor recept, bästa kolasnittar, enkla småkakor",
        "alt": "Närbild på nyskurna gyllene sneda kolasnittar med glänsande karamelliserad yta och flingsalt på en rustik träskärbräda",
        "equipment": ["Bakplåt med bakplåtspapper", "Bunke & gaffel/kniv", "Skärbräda"],
        "drink_pairing": "En rykande kopp kaffe, ett glas kall havremjölk eller klassiskt svart te.",
        "ingredients": [
            {"group": "Kolasnittsdeg", "items": [
                {"val": 100, "unit": "g", "name": "smör (rumsvarmt)"},
                {"val": 1, "unit": "dl", "name": "strösocker"},
                {"val": 2, "unit": "msk", "name": "ljus sirap"},
                {"val": 2.25, "unit": "dl", "name": "vetemjöl"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 1, "unit": "tsk", "name": "bakpulver"}
            ]},
            {"group": "Garnering", "items": [
                {"val": 1, "unit": "tsk", "name": "flingsalt (framhäver kolasmaken)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Sätt ugnen & förbered plåt", "text": "Sätt ugnen på 175°C över-/undervärme. Lägg ett bakplåtspapper på en ugnsplåt.", "timer": 2},
            {"step": 2, "title": "Rör ihop smör, socker & sirap", "text": "Rör rumsvarmt smör, strösocker och ljus sirap smidigt i en bunke med en träslev eller elvisp.", "timer": 3},
            {"step": 3, "title": "Tillsätt de torra ingredienserna", "text": "Blanda vetemjöl, bakpulver och vaniljsocker. Rör ner i smörblandningen och arbeta snabbt ihop till en mjuk och formbar deg.", "timer": 2},
            {"step": 4, "title": "Forma längder & platta till", "text": "Dela degen i 2 eller 3 delar. Rulla ut till längder på plåten. Platta till längderna lätt med fingrarna eller baksidan av en gaffel så de blir ca 1 cm tjocka. Strö lite flingsalt över.", "timer": 3},
            {"step": 5, "title": "Grädda gyllene", "text": "Grädda mitt i ugnen i ca 12–15 minuter tills längderna flutit ut och fått en vacker gyllenbrun färg.", "timer": 13},
            {"step": 6, "title": "Snitta genast på snedden", "text": "Ta ut plåten och skär genast längderna i sneda, fina snittar med en vass kniv medan kakorna fortfarande är varma och mjuka. Låt svalna helt på plåten så de blir sega och krispiga!", "timer": 5}
        ],
        "pro_tips": "Skär alltid kakorna diagonalt omedelbart när plåten tas ur ugnen! Om du väntar tills de svalnat blir kakorna krispiga och spricker när du skär dem.",
        "nutrition": {"calories": "120 kcal", "protein": "1g", "carbs": "17g", "fat": "5g", "sugar": "10g"},
        "faqs": [
            {"q": "Hur får man kolasnittarna riktigt sega?", "a": "Grädda inte för länge! Ta ut dem när kanterna är gyllenbruna men mitten fortfarande känns lite mjuk. Då blir de oemotståndligt sega."},
            {"q": "Hur förvaras kolasnittar bäst?", "a": "Förvara kakorna i en tät plåtburk i rumstemperatur i upp till 2 veckor, eller frys in dem."}
        ],
        "community_reviews": [
            {"name": "Sofie Dahlqvist", "date": "Idag", "rating": 5, "comment": "Världens godaste kolasnittar! Flingsaltet ovanpå tog dem till en helt ny nivå.", "verified": True}
        ]
    },
    {
        "slug": "ugnsbakad-lax-kall-romsas-dill",
        "file": "ugnsbakad-lax-kall-romsas-dill.html",
        "img": "ugnsbakadlax",
        "title": "Ugnsbakad Laxfilé med Citron, Dill & Krämig Kall Romsås",
        "card_title": "Ugnsbakad Lax med Romsås",
        "sub": "Saftig ugnsstekt lax med frisk romsås & dillslungad potatis",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Fisk & Skaldjur",
        "difficulty": "Enkel",
        "time": 25,
        "prep_time": "PT10M",
        "cook_time": "PT15M",
        "total_time": "PT25M",
        "prep_time_str": "10 min",
        "cook_time_str": "15 min",
        "time_str": "25 min",
        "calories": 460,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 710,
        "desc": "En svensk favorit som passar lika bra en vardagskväll som till fest! Perfekt ugnsbakad saftig laxfilé toppad med citron och dill, serverad med en klassisk krämig kall romsås med röd stenbitsrom, gräddfil, majonnäs och gräslök.",
        "long_desc": "Ugnsbakad lax är en av Sveriges mest populära fiskrätter. Genom att baka laxen på relativt låg temperatur (175°C) till en innertemperatur på 50–52°C förblir fiskköttet otroligt saftigt och skivar sig i vackra glansiga lameller.",
        "keywords": "lax i ugn, ugnsbakad lax, romsås, lax med romsås, enkel lax i ugn, bästa romsåsen, lax recept ugn, lax middag",
        "alt": "Närbild på saftig rosa ugnsbakad laxfilé med citronskivor, en skål rosa kall romsås med röd rom och nykokt dillpotatis",
        "equipment": ["Ugnsform", "Skål till romsås & visp", "Stektermometer"],
        "drink_pairing": "Ett friskt vitt vin som Riesling, Sauvignon Blanc eller en torr svensk äppelcider.",
        "ingredients": [
            {"group": "Ugnsbakad Lax", "items": [
                {"val": 600, "unit": "g", "name": "laxfilé (färsk svensk/norsk lax i portionsbitar eller hel sida)"},
                {"val": 1, "unit": "st", "name": "ekologisk citron (skivad i tunna skivor)"},
                {"val": 2, "unit": "msk", "name": "olivolja eller smält smör"},
                {"val": 1, "unit": "tsk", "name": "flingsalt & nymalen svartpeppar"},
                {"val": 1, "unit": "kruka", "name": "färsk dill"}
            ]},
            {"group": "Krämig Kall Romsås", "items": [
                {"val": 2, "unit": "dl", "name": "crème fraiche eller gräddfil"},
                {"val": 0.5, "unit": "dl", "name": "äkta majonnäs"},
                {"val": 1, "unit": "burk", "name": "röd stenbitsrom (à 80g)"},
                {"val": 2, "unit": "msk", "name": "färsk dill (finhackad)"},
                {"val": 2, "unit": "msk", "name": "färsk gräslök (fint klippt)"},
                {"val": 1, "unit": "tsk", "name": "färskpressad citronsaft"},
                {"val": 1, "unit": "krm", "name": "salt & vitpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "portioner", "name": "kokt delikatesspotatis slungad i smör och dill"},
                {"val": 150, "unit": "g", "name": "sockerärter eller haricots verts"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered ugnen & rör ihop romsåsen", "text": "Sätt ugnen på 175°C över-/undervärme. Blanda crème fraiche, majonnäs, stenbitsrom, finhackad dill, klippt gräslök och citronsaft i en skål. Smaka av med lite salt och vitpeppar. Ställ romsåsen i kylen så att smakerna mognar.", "timer": 5},
            {"step": 2, "title": "Förbered laxen", "text": "Lägg laxfilén med skinnsidan nedåt i en smord ugnsform. Ringla över olivolja, krydda med flingsalt och nymalen svartpeppar. Lägg tunna citronskivor och några kvistar dill ovanpå.", "timer": 5},
            {"step": 3, "title": "Baka i ugnen", "text": "Baka laxen mitt i ugnen i ca 15–18 minuter (eller tills innertemperaturen når 50–52°C). Laxen ska kännas lätt stunsig och skiva sig vid lätt tryck.", "timer": 15},
            {"step": 4, "title": "Koka potatisen", "text": "Koka potatisen mjuk i saltat vatten. Häll av och slunga runt med en klick smör och rikligt med färsk dill.", "timer": 15},
            {"step": 5, "title": "Servera och njut", "text": "Lägg upp den varma saftiga laxen på tallrikar tillsammans med den kalla romsåsen, ångande dillpotatis och krispiga grönsaker.", "timer": None}
        ],
        "pro_tips": "Ta ut laxen vid exakt 50–52°C innertemperatur och låt den vila i 2 minuter under folie – då rinner ingen vätska ut och laxen blir smältande mör och saftig.",
        "nutrition": {"calories": "460 kcal", "protein": "34g", "carbs": "8g", "fat": "32g", "sugar": "3g"},
        "faqs": [
            {"q": "Kan man använda fryst lax?", "a": "Ja, tina laxfiléerna långsamt i kylskåp och torka av dem med hushållspapper innan kryddning så får du bästa stekyta och saftighet."},
            {"q": "Hur länge håller romsåsen i kylen?", "a": "Romsåsen håller sig utmärkt i en tät burk i kylskåpet i 3–4 dagar och smakar ofta ännu godare dagen efter."}
        ],
        "community_reviews": [
            {"name": "Elin Wahlgren", "date": "Idag", "rating": 5, "comment": "Romsåsen var helt fantastisk! Så enkel och perfekt syra mot den saftiga laxen.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-kottfarspaj-frasigt-pajskal",
        "file": "klassisk-kottfarspaj-frasigt-pajskal.html",
        "img": "kottfarspaj",
        "title": "Klassisk Köttfärspaj med Frasigt Pajskal & Lagrad Ost",
        "card_title": "Klassisk Köttfärspaj",
        "sub": "Frasigt pajskal fyllt med smakrik köttfärs & gratinerad ost",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Pajer",
        "difficulty": "Enkel",
        "time": 45,
        "prep_time": "PT15M",
        "cook_time": "PT30M",
        "total_time": "PT45M",
        "prep_time_str": "15 min",
        "cook_time_str": "30 min",
        "time_str": "45 min",
        "calories": 510,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 660,
        "desc": "En oemotståndlig middagsfavorit som alltid gör succé! Ett gyllene, frasigt smörpajskal fyllt med en mustig och smakrik köttfärsröra på nötfärs, lök, röd paprika, tomatpuré och oregano, täckt med en krämig äggstanning och gratinerad ost.",
        "long_desc": "Köttfärspaj är den perfekta bjudrätten och vardagsmiddagen. Genom att förgrädda pajskalet blir botten härligt frasig och suger inte åt sig onödig fukt från köttfärsen.",
        "keywords": "köttfärspaj, köttfärspaj recept, enkel köttfärspaj, godaste köttfärspajen, paj med köttfärs, frasig köttfärspaj",
        "alt": "Närbild på en bit gyllengul köttfärspaj med frasig smördegskant, mustig köttfärsfyllning, smält osttäcke och grönsallad",
        "equipment": ["Pajform (ca 26–28 cm)", "Stekpanna", "Bunke till äggstanning"],
        "drink_pairing": "Ett mjukt rött vin som Merlot, en krispig IPA eller ett glas kallt mineralvatten.",
        "ingredients": [
            {"group": "Frasigt Pajskal", "items": [
                {"val": 3, "unit": "dl", "name": "vetemjöl"},
                {"val": 125, "unit": "g", "name": "kallt smör (i tärningar)"},
                {"val": 3, "unit": "msk", "name": "iskallt vatten"},
                {"val": 0.5, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Mustig Köttfärsfyllning", "items": [
                {"val": 500, "unit": "g", "name": "nötfärs eller blandfärs"},
                {"val": 1, "unit": "st", "name": "gul lök (finhackad)"},
                {"val": 2, "unit": "klyftor", "name": "vitlök (finhackade)"},
                {"val": 1, "unit": "st", "name": "röd paprika (fint tärnad)"},
                {"val": 3, "unit": "msk", "name": "tomatpuré & 1 tsk torkad oregano"},
                {"val": 1, "unit": "msk", "name": "kalvfond eller oxfond"},
                {"val": 1, "unit": "msk", "name": "smör (att steka i)"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"}
            ]},
            {"group": "Krämig Äggstanning & Osttäcke", "items": [
                {"val": 3, "unit": "st", "name": "stora ägg"},
                {"val": 2, "unit": "dl", "name": "mjölk eller vispgrädde"},
                {"val": 2.5, "unit": "dl", "name": "riven lagrad ost (t.ex. Prästost eller Västerbottensost)"},
                {"val": 1, "unit": "krm", "name": "salt & svartpeppar"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Gör pajdegen & förgrädda", "text": "Sätt ugnen på 200°C. Nyp snabbt ihop mjöl, salt och kallt smör i en bunke. Tillsätt kallt vatten och tryck ihop till en deg. Tryck ut degen i en pajform (26–28 cm), nagga botten med en gaffel och låt vila i frysen i 10 minuter. Förgrädda i ugnen i 10 minuter.", "timer": 10},
            {"step": 2, "title": "Fräs köttfärsfyllningen", "text": "Hetta upp smör i en stekpanna. Bryn köttfärs, hackad lök, vitlök och tärnad paprika tills färsen är genomstekt och fått fin färg. Rör ner tomatpuré, fond, oregano, salt och peppar. Låt fräsa 3 minuter.", "timer": 8},
            {"step": 3, "title": "Vispa äggstanningen", "text": "Vispa ihop ägg, mjölk/grädde, salt och peppar i en skål.", "timer": 2},
            {"step": 4, "title": "Fyll pajskalet", "text": "Fördela den varma köttfärsröran jämnt i det förgräddade pajskalet. Häll över äggstanningen och toppa med ett generöst lager riven ost.", "timer": 3},
            {"step": 5, "title": "Grädda gyllenbrun", "text": "Grädda mitt i ugnen i ca 25–30 minuter tills äggstanningen har stannat och osten har fått en bubblande, gyllenbrun färg.", "timer": 25},
            {"step": 6, "title": "Låt sätta sig & servera", "text": "Låt pajen vila i 5–10 minuter före servering så sätter den sig och blir lättare att skära i fina bitar. Servera med en krispig grönsallad.", "timer": 10}
        ],
        "pro_tips": "Låt pajskalet vila 10 minuter i frysen innan det åker in i ugnen och förgrädda det alltid – då krymper inte kanterna ner under gräddning och botten blir underbart frasig.",
        "nutrition": {"calories": "510 kcal", "protein": "28g", "carbs": "30g", "fat": "32g", "sugar": "3g"},
        "faqs": [
            {"q": "Kan man förbereda pajen dagen innan?", "a": "Ja, köttfärspaj går utmärkt att baka helt färdig dagen innan och värma på 175°C i 15 minuter före servering."},
            {"q": "Kan man frysa köttfärspaj?", "a": "Ja, pajen fryser fantastiskt bra både hel och i portionsbitar."}
        ],
        "community_reviews": [
            {"name": "Mikael Lind", "date": "Idag", "rating": 5, "comment": "Bästa köttfärspajen! Pajskalet blev så krispigt och fyllningen var riktigt saftig och god.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-biff-rydberg-oxfile-aggula",
        "file": "klassisk-biff-rydberg-oxfile-aggula.html",
        "img": "biffrydberg",
        "title": "Klassisk Biff Rydberg med Oxfilé, Råstekt Potatis & Äggula",
        "card_title": "Klassisk Biff Rydberg",
        "sub": "Svensk lyxhusman med tärnad oxfilé, frasig potatis & äggula",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Kött",
        "difficulty": "Medel",
        "time": 35,
        "prep_time": "PT15M",
        "cook_time": "PT20M",
        "total_time": "PT35M",
        "prep_time_str": "15 min",
        "cook_time_str": "20 min",
        "time_str": "35 min",
        "calories": 560,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 680,
        "desc": "Kungen av svensk lyxhusmanskost! Perfekt skuren tärnad oxfilé eller biff som hårdsteks och serveras i tre eleganta rader bredvid frasig råstekt potatis och söt karamelliserad lök, toppad med en rå äggula, senapskräm och persilja.",
        "long_desc": "Skapad på anrika Hotell Rydberg i Stockholm under 1800-talet. Hemligheten bakom en perfekt Biff Rydberg är att tärna potatis, kött och lök i exakt lika stora kuber (ca 1x1 cm) och steka varje komponent separat i rikligt med smör.",
        "keywords": "biff rydberg, biff rydberg recept, äkta biff rydberg, biff rydberg oxfilé, bästa biff rydberg, svensk lyxhusmanskost",
        "alt": "Närbild på en klassisk tallrik Biff Rydberg med rader av stekt tärnad oxfilé, gyllene råstekt potatis, stekt lök och en rå äggula i äggskal",
        "equipment": ["2 stora gjutjärnspannor", "Skärbräda & vass kockkniv", "Äggdelare"],
        "drink_pairing": "En kall svensk pilsner med en snaps (Akvavit), eller ett fylligt rött vin som Rioja eller Bordeaux.",
        "ingredients": [
            {"group": "Kött, Potatis & Lök", "items": [
                {"val": 600, "unit": "g", "name": "oxfilé eller ryggbiff (skuren i 1.5 cm kuber)"},
                {"val": 800, "unit": "g", "name": "fast potatis (t.ex. Asterix, skalad och skuren i 1 cm tärningar)"},
                {"val": 3, "unit": "st", "name": "gula lökar (finhackade eller tärnade i 1 cm bitar)"},
                {"val": 100, "unit": "g", "name": "smör och 2 msk rapsolja (att steka i)"},
                {"val": 1.5, "unit": "tsk", "name": "flingsalt & nymalen svartpeppar"}
            ]},
            {"group": "Klassiska Tillbehör", "items": [
                {"val": 4, "unit": "st", "name": "färska äggulor (serveras i halva äggskal)"},
                {"val": 4, "unit": "msk", "name": "dijonsenap eller skånsk senap"},
                {"val": 1, "unit": "kruka", "name": "färsk bladpersilja (finhackad)"},
                {"val": 4, "unit": "msk", "name": "riven pepparrot (frivilligt)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Skölj och torka potatistärningarna", "text": "Skölj potatistärningarna i kallt vatten för att få bort överflödig stärkelse. Torka noga torra med en ren kökshandduk (viktigt för att de ska bli krispiga!).", "timer": 5},
            {"step": 2, "title": "Råstek potatisen gyllene", "text": "Hetta upp 40g smör och olja i en stor stekpanna. Stek potatistärningarna på medelvärme i ca 15–20 minuter under regelbunden vändning tills de är genomstekta och har en krispig gyllenbrun yta. Salta.", "timer": 18},
            {"step": 3, "title": "Karamellisera löken", "text": "Stek löken mjuk och gyllene i 30g smör i en separat panna på medelvärme i ca 10–12 minuter. Den ska bli söt och lätt brynt.", "timer": 10},
            {"step": 4, "title": "Hårdstek oxfilén i rykande het panna", "text": "Hetta upp en gjutjärnspanna tills den ryker med 30g smör och lite olja. Stek oxfilétärningarna snabbt på högsta värme i max 1.5–2 minuter så de får fin mörk stekyta men förblir rosa och saftiga i mitten. Salta och peppra.", "timer": 3},
            {"step": 5, "title": "Montera tallrikarna", "text": "Lägg upp potatis, kött och lök i tre prydliga separata rader eller sektioner på varma tallrikar.", "timer": 2},
            {"step": 6, "title": "Servera med äggula & senap", "text": "Placera en rå äggula i mitten (gärna i ett halvt äggskal), toppa köttet och potatisen med färsk persilja och servera genast med en klick god senap och färskriven pepparrot.", "timer": None}
        ],
        "pro_tips": "Stek köttet i en rykande het panna i mycket små omgångar precis före servering. Om pannan är för full kokar köttet istället för att stekas krispigt.",
        "nutrition": {"calories": "560 kcal", "protein": "40g", "carbs": "34g", "fat": "30g", "sugar": "5g"},
        "faqs": [
            {"q": "Varför ska man skölja och torka potatistärningarna?", "a": "När stärkelsen sköljs bort från ytan klibbar potatisbitarna inte ihop i pannan utan blir separat råstekta och underbart krispiga."},
            {"q": "Kan man använda annat kött än oxfilé?", "a": "Ryggbiff eller mörad entrecôte fungerar också fantastiskt bra, se bara till att putsa bort eventuella senor innan tärning."}
        ],
        "community_reviews": [
            {"name": "Gustav Håkansson", "date": "Idag", "rating": 5, "comment": "Den perfekta Biff Rydbergen! Krispig potatis, smältande mört kött och äggulan band ihop allt fantastiskt.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-chokladbiskvier-mandelbotten",
        "file": "klassiska-chokladbiskvier-mandelbotten.html",
        "img": "biskvier",
        "title": "Klassiska Chokladbiskvier med Silkeslen Chokladsmörkräm",
        "card_title": "Klassiska Chokladbiskvier",
        "sub": "Seg mandelbotten med fyllig chokladkräm & krispigt chokladtäcke",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt / Glutenfritt",
        "difficulty": "Medel",
        "time": 45,
        "prep_time": "PT25M",
        "cook_time": "PT20M",
        "total_time": "PT45M",
        "prep_time_str": "25 min",
        "cook_time_str": "20 min",
        "time_str": "45 min",
        "calories": 220,
        "portions_num": 16,
        "portions_unit": "biskvier",
        "rating": 4.99,
        "review_count": 730,
        "desc": "Konditoriets absoluta mästerverk! Sega och goda mandelbottnar toppade med en hög kupol av silkeslen chokladsmörkräm, doppade i mörk krispig choklad med lite havssalt. Naturligt glutenfria och oemotståndliga.",
        "long_desc": "Chokladbiskvier är en tidlös svensk fikafavorit. Hemligheten bakom en perfekt biskvi är att kyla bottnarna med smörkräm ordentligt innan de doppas i smält choklad så att chokladtäcket stelnar blixtsnabbt till en krispig hinna.",
        "keywords": "biskvier, chokladbiskvier, chokladbiskvier recept, biskvier recept, baka biskvier, glutenfria biskvier, goda biskvier",
        "alt": "Närbild på en delad chokladbiskvi som visar den sega mandelbottnen, fyllig chokladsmörkräm och glänsande chokladskal med flingsalt",
        "equipment": ["Bakplåt med bakplåtspapper", "Elvisp", "Liten spatel / smörkniv till formning"],
        "drink_pairing": "En enkel eller dubbel espresso, cappuccino eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Sega Mandelbottnar", "items": [
                {"val": 250, "unit": "g", "name": "mandelmassa av god kvalitet (riven)"},
                {"val": 1, "unit": "st", "name": "äggvita (från stort ägg)"},
                {"val": 0.5, "unit": "dl", "name": "strösocker"}
            ]},
            {"group": "Silkeslen Chokladsmörkräm", "items": [
                {"val": 150, "unit": "g", "name": "smör (rumsvarmt & mjukt)"},
                {"val": 1.5, "unit": "dl", "name": "florsocker"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 1, "unit": "st", "name": "äggula"},
                {"val": 75, "unit": "g", "name": "mörk choklad (smält & svalnad)"},
                {"val": 1, "unit": "msk", "name": "kakao av god kvalitet"}
            ]},
            {"group": "Chokladöverdrag", "items": [
                {"val": 150, "unit": "g", "name": "mörk kvalitetschoklad (55–70%)"},
                {"val": 1, "unit": "tsk", "name": "neutral rapsolja eller kokosolja (för vacker glans)"},
                {"val": 1, "unit": "krm", "name": "flingsalt (till garnering)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Sätt ugnen & baka bottnarna", "text": "Sätt ugnen på 175°C över-/undervärme. Riv mandelmassan grovt och rör ihop med socker och äggvita till en jämn massa. Klicka eller spritsa ut 16 runda bottnar på en plåt med bakplåtspapper. Grädda i ca 10–12 minuter tills kanterna fått fin färg. Låt svalna helt.", "timer": 12},
            {"step": 2, "title": "Vispa chokladsmörkrämen", "text": "Vispa rumsvarmt smör, florsocker och vaniljsocker vitt och fluffigt med elvisp i ca 4–5 minuter. Tillsätt äggulan, kakao och den smälta svalnade chokladen. Vispa till en slät och krämig chokladkräm.", "timer": 6},
            {"step": 3, "title": "Forma kupolerna på bottnarna", "text": "Bred ut smörkrämen med en liten spatel eller smörkniv på undersidan av de kalla mandelbottnarna så att det bildas en fin toppig kupol. Ställ biskvierna i frysen i 20 minuter (eller kylen i 45 min).", "timer": 20},
            {"step": 4, "title": "Smält chokladen till doppet", "text": "Smält den mörka chokladen försiktigt över vattenbad eller i mikron. Rör i oljan för fin glans och låt svalna något.", "timer": 4},
            {"step": 5, "title": "Doppa biskvierna", "text": "Håll i mandelbotten och doppa den iskalla smörkrämstoppen snabbt i den smälta chokladen. Låt överflödig choklad rinna av. Strö lite flingsalt på toppen.", "timer": 5},
            {"step": 6, "title": "Låt stelna och njut", "text": "Låt chokladen stelna helt i kylen. Servera kylskåpskalla till en god kopp kaffe.", "timer": None}
        ],
        "pro_tips": "Frys biskvierna i 20 minuter innan du doppar dem i den smälta chokladen! Den kalla krämen gör att chokladtäcket stelnar på 5 sekunder och behåller sin perfekta form.",
        "nutrition": {"calories": "220 kcal", "protein": "4g", "carbs": "22g", "fat": "14g", "sugar": "18g"},
        "faqs": [
            {"q": "Är biskvier glutenfria?", "a": "Ja, klassiska biskvier bakas på ren mandelmassa, socker och äggvita utan vetemjöl och är naturligt 100% glutenfria!"},
            {"q": "Hur förvaras biskvier bäst?", "a": "Biskvier förvaras bäst i kylskåp i en tätslutande burk i upp till 1 vecka, eller fryses in (de kan ätas nästan direkt från frysen!)."}
        ],
        "community_reviews": [
            {"name": "Sara Lindström", "date": "Idag", "rating": 5, "comment": "Konditoriklass! Tricket att frysa dem innan doppet gjorde att de blev helt perfekta.", "verified": True}
        ]
    },
    {
        "slug": "gammaldags-kottsoppa-hogrev-klimp",
        "file": "gammaldags-kottsoppa-hogrev-klimp.html",
        "img": "kottsoppa",
        "title": "Gammaldags Köttsoppa med Högrev, Rotfrukter & Klimp",
        "card_title": "Gammaldags Köttsoppa",
        "sub": "Värmande mustig buljong med mört långkokt högrev & klimp",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost / Soppor",
        "difficulty": "Medel",
        "time": 90,
        "prep_time": "PT15M",
        "cook_time": "PT75M",
        "total_time": "PT90M",
        "prep_time_str": "15 min",
        "cook_time_str": "1 tim 15 min",
        "time_str": "1 tim 30 min",
        "calories": 440,
        "portions_num": 6,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 520,
        "desc": "En genuin norrländsk och svensk höstklassiker! Långkokt mört högrev som sjuder med morötter, kålrot, palsternacka och purjolök i en fyllig klar köttbuljong, serverad med traditionell fluffig klimp.",
        "long_desc": "Gammaldags köttsoppa med klimp är den ultimata värmande måltiden för kyliga höstdagar. Långsam sjudning av kött och ben ger en smakrik och näringsrik buljong, och klimpen suger åt sig av soppans fylliga aromer.",
        "keywords": "köttsoppa, köttsoppa med klimp, gammaldags köttsoppa, köttsoppa recept, godaste köttsoppan, köttsoppa högrev, norrländsk köttsoppa",
        "alt": "Närbild på en skål traditionell köttsoppa med möra högrevsbitar, tärnade morötter, kålrot och fluffiga klimpar med persilja",
        "equipment": ["Stor soppgryta (4–5 liter)", "Skumslev", "Skärbräda & kockkniv"],
        "drink_pairing": "En kall svensk lageröl, äppelmust eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Kött & Buljong", "items": [
                {"val": 800, "unit": "g", "name": "högrev eller märgpipa (i lagom soppbitar ca 2x2 cm)"},
                {"val": 1.8, "unit": "liter", "name": "vatten"},
                {"val": 2, "unit": "msk", "name": "koncentrerad oxfond eller kalvfond"},
                {"val": 8, "unit": "st", "name": "kryddpepparkorn"},
                {"val": 8, "unit": "st", "name": "vitpepparkorn"},
                {"val": 2, "unit": "st", "name": "lagerblad"},
                {"val": 1.5, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Höströtter & Grönsaker", "items": [
                {"val": 3, "unit": "st", "name": "morötter (slantade eller tärnade)"},
                {"val": 200, "unit": "g", "name": "kålrot (skalad & tärnad)"},
                {"val": 2, "unit": "st", "name": "palsternackor (tärnade)"},
                {"val": 1, "unit": "st", "name": "purjolök (skivad)"},
                {"val": 3, "unit": "st", "name": "potatisar (tärnade)"}
            ]},
            {"group": "Traditionell Klimp", "items": [
                {"val": 1, "unit": "st", "name": "stort ägg"},
                {"val": 1, "unit": "dl", "name": "mjölk"},
                {"val": 2, "unit": "dl", "name": "vetemjöl"},
                {"val": 0.5, "unit": "tsk", "name": "socker & 0.5 tsk salt"},
                {"val": 1, "unit": "krm", "name": "muskotnöt"}
            ]},
            {"group": "Servering", "items": [
                {"val": 1, "unit": "kruka", "name": "färsk kruspersilja (finhackad)"},
                {"val": 6, "unit": "skivor", "name": "tunnbröd eller rågknäckebröd med smör och lagrad ost"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Koka köttet & skumma noga", "text": "Lägg köttbitarna i en stor kastrull med 1.8 liter vatten och salt. Koka upp på hög värme och skumma noga av det bruna skummet som bildas på ytan.", "timer": 10},
            {"step": 2, "title": "Tillsätt kryddor & sjud", "text": "Tillsätt kryddpeppar, vitpeppar, lagerblad och oxfond. Sänk värmen, sätt på lock och låt sjuda sakta i ca 1 timme tills köttet börjar bli riktigt mört.", "timer": 60},
            {"step": 3, "title": "Tillsätt rotfrukterna", "text": "Lägg i morötter, kålrot, palsternacka och potatis. Låt sjuda med i 15 minuter.", "timer": 15},
            {"step": 4, "title": "Rör ihop klimpsmeten", "text": "Vispa ihop ägg, mjölk, socker, salt och muskotnöt i en skål. Rör ner vetemjölet till en tjock, klibbig smet.", "timer": 3},
            {"step": 5, "title": "Klicka ner klimpen & purjolök", "text": "Tillsätt skivad purjolök i soppan. Doppa en matsked i den heta soppan och klicka sedan ner matskedsstora klimpar direkt i den sjudande soppan. Låt klimparna sjuda i ca 5–7 minuter tills de flyter upp och är genomkokta.", "timer": 7},
            {"step": 6, "title": "Garnera & servera", "text": "Smaka av soppan med salt och peppar. Strö över rikligt med färsk persilja och servera rykande het med mjukt tunnbröd eller knäckebröd med ost.", "timer": None}
        ],
        "pro_tips": "Doppa alltid matskeden i den heta soppbuljongen innan du tar upp klimpsmeten – då glider smeten av skeden direkt ner i soppan utan att fastna!",
        "nutrition": {"calories": "440 kcal", "protein": "34g", "carbs": "42g", "fat": "14g", "sugar": "8g"},
        "faqs": [
            {"q": "Vad är klimp?", "a": "Klimp är traditionella svenska kokta klimpar gjorda på ägg, mjölk, mjöl och muskot som sjuds direkt i köttsoppan och suger upp buljongens mustiga smak."},
            {"q": "Kan köttsoppan förberedas i förväg?", "a": "Ja, köttsoppan blir ofta ännu godare dagen efter då smakerna sätter sig. Tillsätt dock gärna klimpen precis vid servering så att den håller sin fluffiga konsistens."}
        ],
        "community_reviews": [
            {"name": "Birgitta Nilsson", "date": "Idag", "rating": 5, "comment": "Underbar köttsoppa! Klimpen blev så mjuk och god och köttet föll sönder i munnen.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-pannbiffar-med-lok-graddsas",
        "file": "klassiska-pannbiffar-med-lok-graddsas.html",
        "img": "pannbiff",
        "title": "Klassiska Pannbiffar med Karamelliserad Lök & Gräddsås",
        "card_title": "Pannbiff med Lök",
        "sub": "Saftiga pannbiffar med mjukstekt karamelliserad lök, gräddsås & lingon",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Enkel",
        "time": 40,
        "prep_time": "PT15M",
        "cook_time": "PT25M",
        "total_time": "PT40M",
        "prep_time_str": "15 min",
        "cook_time_str": "25 min",
        "time_str": "40 min",
        "calories": 520,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 680,
        "desc": "En av Sveriges mest älskade husmansklassiker! Saftiga och smakrika pannbiffar gjorda på nötfärs eller blandfärs, serverade med ett generöst berg av smörstekt karamelliserad gul lök, en silkeslen gräddsås, kokt potatis och rårörda lingon.",
        "long_desc": "Pannbiff med lök är själva definitionen av svensk tröstmat. Hemligheten bakom extra saftiga biffar är att låta ströbröd svälla i mjölk och grädde, samt att steka löken långsamt på svag värme så att dess naturliga sötma utvecklas.",
        "keywords": "pannbiff, pannbiff med lök, pannbiff recept, bästa pannbiffarna, saftig pannbiff, pannbiff med gräddsås, klassisk husmanskost",
        "alt": "Närbild på gyllenbruna saftiga pannbiffar täckta av karamelliserad lök, krämig gräddsås, nykokt dillpotatis och rårörda lingon",
        "equipment": ["Gjutjärnsstekpanna", "Bunke till färs", "Stekspade"],
        "drink_pairing": "En fyllig svensk lager, enbärsdricka eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Saftiga Pannbiffar", "items": [
                {"val": 600, "unit": "g", "name": "nötfärs eller blandfärs (av god kvalitet)"},
                {"val": 0.75, "unit": "dl", "name": "ströbröd"},
                {"val": 1.5, "unit": "dl", "name": "mjölk eller gräddmjölk"},
                {"val": 1, "unit": "st", "name": "stort ägg"},
                {"val": 1, "unit": "msk", "name": "koncentrerad kalvfond eller oxfond"},
                {"val": 1, "unit": "msk", "name": "kinesisk soja (för färg och umami)"},
                {"val": 1, "unit": "tsk", "name": "dijonsenap"},
                {"val": 1, "unit": "tsk", "name": "salt & nymalen svartpeppar"},
                {"val": 0.5, "unit": "tsk", "name": "nystött kryddpeppar (ger klassisk smak)"},
                {"val": 3, "unit": "msk", "name": "smör (att steka i)"}
            ]},
            {"group": "Karamelliserad Stekt Lök", "items": [
                {"val": 4, "unit": "st", "name": "stora gula lökar (skivade i tunna ringar)"},
                {"val": 3, "unit": "msk", "name": "smör"},
                {"val": 1, "unit": "tsk", "name": "strösocker eller ljus sirap (framhäver karamelliseringen)"},
                {"val": 0.5, "unit": "tsk", "name": "salt & svartpeppar"}
            ]},
            {"group": "Krämig Gräddsås", "items": [
                {"val": 3, "unit": "dl", "name": "vispgrädde"},
                {"val": 1.5, "unit": "dl", "name": "vatten (att vispa ur pannan med)"},
                {"val": 2, "unit": "msk", "name": "koncentrerad kalvfond"},
                {"val": 1, "unit": "msk", "name": "kinesisk soja"},
                {"val": 1, "unit": "msk", "name": "svartvinbärsgelé eller lingonsylt"},
                {"val": 1, "unit": "msk", "name": "maizena (utrört i lite vatten, för redning)"}
            ]},
            {"group": "Klassisk Servering", "items": [
                {"val": 4, "unit": "portioner", "name": "kokt delikatesspotatis eller potatismos"},
                {"val": 2, "unit": "dl", "name": "rårörda lingon"},
                {"val": 1, "unit": "burk", "name": "pressgurka eller inlagd gurka"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Låt ströbrödet svälla", "text": "Blanda ströbröd, mjölk, kalvfond, soja och dijonsenap i en bunke. Låt stå och svälla i ca 8–10 minuter.", "timer": 8},
            {"step": 2, "title": "Karamellisera löken", "text": "Hetta upp 3 msk smör i en stekpanna. Stek den skivade löken på medellåg värme under regelbunden omrörning i ca 15–20 minuter tills den är helt mjuk, gyllenbrun och söt. Tillsätt lite sirap/socker och salt mot slutet. Lägg upp löken på ett fat och håll varm.", "timer": 18},
            {"step": 3, "title": "Blanda färsen & forma biffar", "text": "Tillsätt ägg, salt, svartpeppar, kryddpeppar och färsen till ströbrödsblandningen. Blanda snabbt ihop till en smidig smet (arbeta inte för länge). Forma till 6–8 fina runda, platta pannbiffar med fuktiga händer.", "timer": 5},
            {"step": 4, "title": "Stek pannbiffarna gyllene", "text": "Hetta upp smör i samma stekpanna på medelhög värme. Stek biffarna i ca 3–4 minuter per sida tills de har en fin mörkbrun stekyta och är genomstekta. Lyft ur biffarna och lägg dem tillsammans med löken under folie.", "timer": 8},
            {"step": 5, "title": "Koka den krämiga gräddsåsen", "text": "Häll vatten i stekpannan och vispa ur alla goda stekskyar. Tillsätt vispgrädde, kalvfond, soja och gelé. Låt sjuda i 3–4 minuter. Red av med lite maizena till önskad krämig konsistens. Smaka av med salt och svartpeppar.", "timer": 4},
            {"step": 6, "title": "Servera med alla tillbehör", "text": "Lägg pannbiffarna på varma tallrikar, toppa med det generösa berget av karamelliserad lök och ringla över den heta gräddsåsen. Servera med nykokt potatis, rårörda lingon och pressgurka.", "timer": None}
        ],
        "pro_tips": "Stek löken långsamt på svag värme – det tar minst 15 minuter för löken att utveckla sina naturliga sockerarter och bli oemotståndligt söt och karamelliserad.",
        "nutrition": {"calories": "520 kcal", "protein": "36g", "carbs": "18g", "fat": "34g", "sugar": "8g"},
        "faqs": [
            {"q": "Vad är skillnaden mellan pannbiff och köttbullar?", "a": "Pannbiffar är större och plattare än köttbullar, och serveras traditionellt med ett stort berg av mjukstekt karamelliserad lök istället för enbart gräddsås."},
            {"q": "Varför blir pannbiffarna torra?", "a": "Överarbeta inte färssmeten och stek inte biffarna för länge. Genom att använda gräddmjölk i ströbrödsblandningen behåller biffarna sin saftighet perfekt."}
        ],
        "community_reviews": [
            {"name": "Mats Haglund", "date": "Idag", "rating": 5, "comment": "Bästa pannbiffarna! Den långsamt stekta löken och den mustiga såsen var ren magi.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-fiskgratang-torsk-rakor-duchessemos",
        "file": "klassisk-fiskgratang-torsk-rakor-duchessemos.html",
        "img": "fiskgratang",
        "title": "Klassisk Fiskgratäng med Torsk, Räkor & Spritsat Duchessemos",
        "card_title": "Klassisk Fiskgratäng",
        "sub": "Ugnsgratinerad torskrygg med krämig vitvinssås, räkor & duchessemos",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Fisk & Skaldjur",
        "difficulty": "Medel",
        "time": 45,
        "prep_time": "PT20M",
        "cook_time": "PT25M",
        "total_time": "PT45M",
        "prep_time_str": "20 min",
        "cook_time_str": "25 min",
        "time_str": "45 min",
        "calories": 480,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 620,
        "desc": "En älskad svensk söndagsklassiker och lyxig vardagsrätt! Mjäll torskrygg eller sej i en ljuvlig sås gjord på fiskfond, vitt vin, dill och grädde, omgiven av gyllene spritsat duchessemos och toppad med färska handskalade räkor.",
        "long_desc": "Fiskgratäng med spritsat potatismos och räkor är en av Sveriges mest ikoniska rätter. Knepet för ett perfekt duchessemos som håller formen vid gratinering är att blanda ner äggulor och en klick smör i det varma moset.",
        "keywords": "fiskgratäng, fiskgratäng med räkor, fiskgratäng recept, klassisk fiskgratäng, fiskgratäng torsk, fiskgratäng duchessemos, godaste fiskgratängen",
        "alt": "Närbild på en ugnsform med klassisk fiskgratäng med spritsat gyllenbrunt duchessemos, torskrygg i krämig dillsås och handskalade räkor",
        "equipment": ["Ugnsfast form", "Spritspåse med stjärntyll", "Kastrull & visp", "Potatispress"],
        "drink_pairing": "Ett friskt torrt vitt vin som Chablis, Sauvignon Blanc eller en ljus lager.",
        "ingredients": [
            {"group": "Fisk & Sås", "items": [
                {"val": 600, "unit": "g", "name": "torskrygg eller sejfilé (färsk eller tinad, i portionsbitar)"},
                {"val": 300, "unit": "g", "name": "räkor med skal (skalade till ca 100g handskalade räkor)"},
                {"val": 2.5, "unit": "dl", "name": "vispgrädde eller matlagningsgrädde"},
                {"val": 1.5, "unit": "dl", "name": "mjölk eller fiskbuljong"},
                {"val": 1, "unit": "dl", "name": "torrt vitt vin eller 1 msk citronsaft"},
                {"val": 2, "unit": "msk", "name": "koncentrerad fiskfond eller hummerfond"},
                {"val": 2, "unit": "msk", "name": "smör & 2 msk vetemjöl (till bottenredning)"},
                {"val": 3, "unit": "msk", "name": "färsk dill (finhackad)"},
                {"val": 1, "unit": "tsk", "name": "salt & vitpeppar"}
            ]},
            {"group": "Spritsat Duchessemos", "items": [
                {"val": 900, "unit": "g", "name": "mjölig potatis (t.ex. King Edward)"},
                {"val": 50, "unit": "g", "name": "smör"},
                {"val": 2, "unit": "st", "name": "äggulor"},
                {"val": 1, "unit": "dl", "name": "varm mjölk eller grädde"},
                {"val": 1, "unit": "krm", "name": "riven muskotnöt, salt & vitpeppar"}
            ]},
            {"group": "Garnering", "items": [
                {"val": 1, "unit": "kruka", "name": "färsk dill"},
                {"val": 1, "unit": "st", "name": "citron (i klyftor)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Koka & gör duchessemoset", "text": "Skala och koka potatisen mjuk i saltat vatten. Häll av och pressa med potatispress. Rör ner smör, äggulor och varm mjölk. Smaka av med salt, vitpeppar och lite riven muskotnöt. Fyll en spritspåse med stjärntyll.", "timer": 20},
            {"step": 2, "title": "Förbered ugnen & fisken", "text": "Sätt ugnen på 225°C över-/undervärme eller grill. Salta och peppra torskbitarna lätt och lägg dem i mitten av en smord ugnsform.", "timer": 5},
            {"step": 3, "title": "Koka den krämiga vitvinssåsen", "text": "Smält 2 msk smör i en kastrull och vispa ner vetemjöl. Späd under vispning med vitt vin, fiskfond, mjölk och grädde. Låt sjuda i ca 5 minuter till en slät, krämig sås. Vänd ner hackad dill och smaka av med salt, vitpeppar och eventuellt lite citronsaft.", "timer": 6},
            {"step": 4, "title": "Spritsa moset & häll på såsen", "text": "Spritsa vackra rosetter eller rader av duchessemos längs formens kanter runt fisken. Häll den heta dillsåsen över fisken i mitten.", "timer": 5},
            {"step": 5, "title": "Gratinera i ugnen", "text": "Gratinera mitt i ugnen i ca 15–18 minuter tills fisken är genomkokt (innertemperatur 50°C) och potatismoset har fått vackra gyllenbruna toppar.", "timer": 16},
            {"step": 6, "title": "Toppa med handskalade räkor & servera", "text": "Ta ut gratängen och toppa genast med rikligt med handskalade räkor, färsk dill och citronklyftor (lägg inte räkorna i ugnen då de blir sega). Servera direkt!", "timer": None}
        ],
        "pro_tips": "Lägg aldrig räkorna på fisken innan den går in i ugnen – strö dem alltid över direkt vid servering på den heta gratängen så håller de sig saftiga, krispiga och mjuka.",
        "nutrition": {"calories": "480 kcal", "protein": "38g", "carbs": "32g", "fat": "22g", "sugar": "4g"},
        "faqs": [
            {"q": "Kan man använda fryst fisk?", "a": "Ja, tina torskryggen eller sejen långsamt och torka av den noggrant med hushållspapper så att såsen inte blir vattnig."},
            {"q": "Kan fiskgratäng förberedas i förväg?", "a": "Du kan koka moset och såsen i förväg. Montera gratängen och baka den precis före middagen för krispigaste potatistoppar."}
        ],
        "community_reviews": [
            {"name": "Helena Sjöberg", "date": "Idag", "rating": 5, "comment": "Maken och barnen slickade formen ren! Såsen var gudomlig och moset höll formen perfekt.", "verified": True}
        ]
    },
    {
        "slug": "klassiskt-rotmos-rimmad-flasklagg",
        "file": "klassiskt-rotmos-rimmad-flasklagg.html",
        "img": "rotmos",
        "title": "Klassiskt Rotmos med Rimmad Fläsklägg & Skånsk Senap",
        "card_title": "Klassiskt Rotmos med Fläsklägg",
        "sub": "Gyllene rotmos på kålrot och morot med smältande mör rimmad fläsklägg",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 120,
        "prep_time": "PT15M",
        "cook_time": "PT105M",
        "total_time": "PT120M",
        "prep_time_str": "15 min",
        "cook_time_str": "1 tim 45 min",
        "time_str": "2 timmar",
        "calories": 540,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 580,
        "desc": "En av de mest uråldriga och älskade svenska husmansrätterna! Långkokt rimmad fläsklägg som faller isär av mörhet, serverad med ett krämigt, gyllene rotmos smaksatt med den smakrika kokspadet, smör och grov skånsk senap.",
        "long_desc": "Rotmos och fläsklägg är höjdpunkten av klassisk svensk husmanskost under hösten och vintern. Genom att späda det mosade rotmoset med lite av fläskläggets salta buljong får moset en oslagbar mustig och djup smak.",
        "keywords": "rotmos, rotmos med fläsklägg, rimmad fläsklägg med rotmos, rotmos recept, klassiskt rotmos, fläsklägg recept, svensk husmanskost rotmos",
        "alt": "Närbild på en djup tallrik med krämigt gyllene rotmos toppat med skivad mör rimmad fläsklägg, grov senap och persilja",
        "equipment": ["Stor gryta (4–5 liter)", "Potatisstöt eller elvisp", "Skumslev"],
        "drink_pairing": "En svensk julöl, fyllig lager eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Långkokt Rimmad Fläsklägg", "items": [
                {"val": 1.2, "unit": "kg", "name": "rimmad fläsklägg med ben"},
                {"val": 1.5, "unit": "liter", "name": "vatten (så det täcker köttet)"},
                {"val": 1, "unit": "st", "name": "gul lök (skalad & i klyftor)"},
                {"val": 8, "unit": "st", "name": "kryddpepparkorn"},
                {"val": 8, "unit": "st", "name": "vitpepparkorn"},
                {"val": 2, "unit": "st", "name": "lagerblad"}
            ]},
            {"group": "Gyllene Rotmos", "items": [
                {"val": 800, "unit": "g", "name": "kålrot (skalad & skuren i mindre bitar)"},
                {"val": 300, "unit": "g", "name": "morötter (skalade & skivade)"},
                {"val": 500, "unit": "g", "name": "mjölig potatis (skalad & i bitar)"},
                {"val": 50, "unit": "g", "name": "smör"},
                {"val": 2, "unit": "dl", "name": "kokspad från fläskläggen"},
                {"val": 1, "unit": "krm", "name": "riven muskotnöt, salt & vitpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "msk", "name": "stark och söt skånsk senap (eller dijonsenap)"},
                {"val": 1, "unit": "kruka", "name": "färsk persilja"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Koka fläskläggen & skumma", "text": "Lägg den rimmade fläskläggen i en stor gryta och häll på vatten så det täcker. Koka upp och skumma av ytan noga. Lägg i lökklyftor, kryddpeppar, vitpeppar och lagerblad. Sänk värmen, sätt på lock och sjud sakta i ca 1.5–2 timmar tills köttet släpper lätt från benet.", "timer": 90},
            {"step": 2, "title": "Koka rotfrukterna", "text": "Skala och skär kålrot och morötter i bitar. Koka i saltat vatten i ca 25 minuter. Tillsätt sedan potatisbitarna och koka ytterligare 15–20 minuter tills allt är helt mjukt. Sila av men spara lite kokvatten.", "timer": 40},
            {"step": 3, "title": "Stöt rotmoset", "text": "Stöt kålrot, morötter och potatis med en potatisstöt eller elvisp. Klicka i smör och späd med ca 1.5–2 dl av det heta kokspadet från fläskläggen till en härligt luftig och krämig konsistens. Smaka av med lite muskotnöt, vitpeppar och eventuellt lite mer salt.", "timer": 5},
            {"step": 4, "title": "Skär upp fläskläggen", "text": "Lyft upp den möra fläskläggen ur buljongen. Skär bort svålen och skär det saftiga köttet i fina bitar eller skivor.", "timer": 5},
            {"step": 5, "title": "Servera och njut", "text": "Lägg upp det rykande heta rotmoset i djupa tallrikar, toppa med det möra fläsklägget, en rejäl klick god skånsk senap och finhackad persilja.", "timer": None}
        ],
        "pro_tips": "Koka kålroten och morötterna 25 minuter innan du lägger i potatisen – eftersom kålrot tar längre tid att koka blir då alla rotfrukter perfekt mjuka samtidigt utan att potatisen kokar sönder.",
        "nutrition": {"calories": "540 kcal", "protein": "42g", "carbs": "36g", "fat": "24g", "sugar": "12g"},
        "faqs": [
            {"q": "Vad gör man om fläskläggen är för salt?", "a": "Om köttet är hårt rimmat kan du låta det ligga i blöt i kallt vatten i ca 1 timme före kokning."},
            {"q": "Kan man använda rimmad bog eller fläsk istället?", "a": "Ja, rimmad fläskbog, rimmad skinka eller tjocka skivor rimmat sidfläsk passar också alldeles utmärkt till rotmos."}
        ],
        "community_reviews": [
            {"name": "Lars-Göran Nilsson", "date": "Idag", "rating": 5, "comment": "Husman när den är som bäst! Rotmoset fick fantastisk smak av kokspadet och köttet var otroligt mört.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-svenska-chokladbollar-parlsocker",
        "file": "klassiska-svenska-chokladbollar-parlsocker.html",
        "img": "chokladbollar",
        "title": "Klassiska Svenska Chokladbollar med Kaffe & Pärlsocker",
        "card_title": "Klassiska Chokladbollar",
        "sub": "Krämiga chokladbollar med havregryn, bryggkaffe & pärlsocker",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Mycket enkel",
        "time": 15,
        "prep_time": "PT15M",
        "cook_time": "PT0M",
        "total_time": "PT15M",
        "prep_time_str": "15 min",
        "cook_time_str": "0 min",
        "time_str": "15 min",
        "calories": 140,
        "portions_num": 20,
        "portions_unit": "chokladbollar",
        "rating": 4.99,
        "review_count": 890,
        "desc": "Sveriges mest bakade och älskade fika! Krämiga och fylliga chokladbollar gjorda på äkta rumsvarmt smör, havregryn, kakao, vaniljsocker och en skvätt starkt kaffe, rullade i krispigt pärlsocker eller riven kokos.",
        "long_desc": "Chokladbollar är en absolut grundpelare i svensk fikakultur. Hemligheten bakom de allra godaste och krämigaste chokladbollarna är att vispa smör och socker fluffigt med elvisp och mixa en del av havregrynen lätt så att smeten blir härligt fudgy.",
        "keywords": "chokladbollar, chokladbollar recept, bästa chokladbollarna, baka chokladbollar, enkla chokladbollar, klassiska chokladbollar, chokladbollar med kaffe",
        "alt": "Närbild på en hög med runda svenska chokladbollar rullade i vitt pärlsocker med kaffekopp och kaffebönor i bakgrunden",
        "equipment": ["Bunke & elvisp", "Djup tallrik till pärlsocker"],
        "drink_pairing": "En kopp nybryggt svenskt bryggkaffe eller ett glas iskall mjölk.",
        "ingredients": [
            {"group": "Klassisk Chokladbollssmet", "items": [
                {"val": 150, "unit": "g", "name": "smör (rumsvarmt & mjukt)"},
                {"val": 1.5, "unit": "dl", "name": "strösocker"},
                {"val": 4, "unit": "dl", "name": "havregryn"},
                {"val": 3, "unit": "msk", "name": "kakao av god kvalitet"},
                {"val": 1, "unit": "msk", "name": "vaniljsocker"},
                {"val": 3, "unit": "msk", "name": "starkt kallt bryggkaffe (eller espresso)"},
                {"val": 1, "unit": "krm", "name": "flingsalt (förstärker chokladsmaken)"}
            ]},
            {"group": "Garnering / Rullning", "items": [
                {"val": 1.5, "unit": "dl", "name": "pärlsocker eller riven kokos"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Vispa smör och socker fluffigt", "text": "Rör eller vispa rumsvarmt smör och strösocker poröst och vitt med elvisp i en bunke i ca 2–3 minuter.", "timer": 3},
            {"step": 2, "title": "Tillsätt smaksättning", "text": "Tillsätt kakao, vaniljsocker, flingsalt och kallt kaffe. Vispa ihop till en jämn chokladsmet.", "timer": 2},
            {"step": 3, "title": "Blanda i havregrynen", "text": "Mixa gärna hälften av havregrynen lätt med stavmixer för extra krämighet. Rör ner alla havregryn i smeten och arbeta ihop väl. Om smeten känns för mjuk, ställ bunken i kylen i 15 minuter.", "timer": 3},
            {"step": 4, "title": "Rulla till bollar", "text": "Forma smeten till ca 20 jämna bollar med händerna.", "timer": 5},
            {"step": 5, "title": "Rulla i pärlsocker eller kokos", "text": "Häll pärlsocker eller kokos på ett fat och rulla bollarna så de blir helt täckta.", "timer": 3},
            {"step": 6, "title": "Kyl och servera", "text": "Ställ chokladbollarna i kylskåp i minst 30 minuter innan servering så de stelnar och blir härligt sega och fylliga.", "timer": None}
        ],
        "pro_tips": "Vispa smöret och sockret vitt och pösigt innan du tillsätter havregrynen, och mixa hälften av havregrynen fint – det ger den där krämiga konditorikänslan!",
        "nutrition": {"calories": "140 kcal", "protein": "2g", "carbs": "16g", "fat": "8g", "sugar": "9g"},
        "faqs": [
            {"q": "Kan man baka chokladbollar utan kaffe?", "a": "Ja, du kan enkelt ersätta kaffet med 3 msk mjölk, apelsinjuice eller kallt vatten."},
            {"q": "Hur länge håller chokladbollar?", "a": "Chokladbollar håller sig i kylskåp i upp till 2 veckor och går dessutom utmärkt att frysa in i månader."}
        ],
        "community_reviews": [
            {"name": "Camilla Ekström", "date": "Idag", "rating": 5, "comment": "Bästa receptet på chokladbollar! Att vispa smöret och mixa havregrynen gjorde enorm skillnad.", "verified": True}
        ]
    },
    {
        "slug": "klassiska-mazariner-mandelmassa-glasyr",
        "file": "klassiska-mazariner-mandelmassa-glasyr.html",
        "img": "mazariner",
        "title": "Klassiska Mazariner med Saftig Mandelkräm & Glasyr",
        "card_title": "Klassiska Mazariner",
        "sub": "Frasiga mördegskakor fyllda med mandelfyllning & vit sockerglasyr",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Medel",
        "time": 45,
        "prep_time": "PT25M",
        "cook_time": "PT20M",
        "total_time": "PT45M",
        "prep_time_str": "25 min",
        "cook_time_str": "20 min",
        "time_str": "45 min",
        "calories": 260,
        "portions_num": 12,
        "portions_unit": "mazariner",
        "rating": 4.98,
        "review_count": 640,
        "desc": "Klassikernas klassiker på det svenska kafferepet! Spröda mördegsformar fyllda med en saftig och fyllig mandelmassa och smörkräm, toppade med en skinande vit sockerglasyr.",
        "long_desc": "Mazariner är ett av Sveriges äldsta och mest uppskattade bakverk. Den perfekta balansen mellan den spröda mördegsbottnen, den mjuka mandelfyllningen och den söta krispiga glasyren gör dem till en oslagbar favorit.",
        "keywords": "mazariner, mazariner recept, baka mazariner, klassiska mazariner, hembakta mazariner, mandelmazariner, mazariner med glasyr",
        "alt": "Närbild på en delad klassisk mazarin som visar den saftiga mandelkrämsfyllningen, spröda mördegskanten och vita glasyren på ett porslinsfat",
        "equipment": ["Mazarinformar (ovala eller runda metallformar)", "Kavel", "Elvisp"],
        "drink_pairing": "En god kopp bryggkaffe eller en kopp Earl Grey te.",
        "ingredients": [
            {"group": "Spröd Mördeg", "items": [
                {"val": 3, "unit": "dl", "name": "vetemjöl"},
                {"val": 125, "unit": "g", "name": "kallt smör (i kuber)"},
                {"val": 0.5, "unit": "dl", "name": "florsocker eller strösocker"},
                {"val": 1, "unit": "st", "name": "äggula"},
                {"val": 1, "unit": "msk", "name": "kallt vatten"}
            ]},
            {"group": "Saftig Mandelfyllning", "items": [
                {"val": 200, "unit": "g", "name": "mandelmassa (riven)"},
                {"val": 75, "unit": "g", "name": "smör (rumsvarmt)"},
                {"val": 2, "unit": "st", "name": "stora ägg"},
                {"val": 0.5, "unit": "tsk", "name": "bittermandelarom eller 2 rivna bittermandlar"}
            ]},
            {"group": "Vit Glasyr", "items": [
                {"val": 2, "unit": "dl", "name": "florsocker"},
                {"val": 1.5, "unit": "msk", "name": "vatten eller färskpressad citronsaft"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Gör mördegen & kyl", "text": "Nyp snabbt ihop mjöl, socker och kallt smör i en bunke. Tillsätt äggula och kallt vatten och arbeta snabbt ihop till en smidig deg. Platta till, slå in i plastfolie och låt vila i kylen i ca 30 minuter.", "timer": 30},
            {"step": 2, "title": "Klä formarna", "text": "Sätt ugnen på 200°C. Kavla ut mördegen eller tryck ut den i 12 smorda mazarinformar så att botten och kanter täcks jämnt.", "timer": 10},
            {"step": 3, "title": "Rör mandelfyllningen", "text": "Riv mandelmassan grovt och rör samman med rumsvarmt smör. Tillsätt äggen ett i taget under omrörning till en slät smet. Droppa i lite bittermandelarom för den karaktäristiska smaken.", "timer": 5},
            {"step": 4, "title": "Fyll formarna & grädda", "text": "Klicka mandelfyllningen i de mördegsklädda formarna (fyll inte ända upp till kanten). Grädda mitt i ugnen i ca 15–18 minuter tills mazarinen fått fin gyllenbrun färg.", "timer": 16},
            {"step": 5, "title": "Låt svalna och stjälp upp", "text": "Låt kakorna svalna i formarna några minuter. Stjälp försiktigt upp dem på ett galler och låt svalna helt.", "timer": 10},
            {"step": 6, "title": "Glasera och låt stelna", "text": "Rör ihop florsocker och vatten/citronsaft till en trögflytande vit glasyr. Bred ut ett jämnt lager glasyr ovanpå varje mazarin och låt stelna.", "timer": None}
        ],
        "pro_tips": "Låt mazarinen svalna helt innan du brer på glasyren – annars smälter glasyren och sugs upp av kakan istället för att bilda ett blankt, vackert täcke.",
        "nutrition": {"calories": "260 kcal", "protein": "5g", "carbs": "32g", "fat": "14g", "sugar": "18g"},
        "faqs": [
            {"q": "Kan man frysa in mazariner?", "a": "Ja, mazariner går utmärkt att frysa in både med och utan glasyr. De tinar snabbt i rumstemperatur."},
            {"q": "Måste man ha mazarinformar i metall?", "a": "Metallformar ger absolut frasigast kant, men det går också att baka mazariner i stadiga muffinsformar eller en muffinsplåt."}
        ],
        "community_reviews": [
            {"name": "Kerstin Berg", "date": "Idag", "rating": 5, "comment": "Riktiga konditorimazariner! Så spröda och mandelfyllningen var fantastiskt saftig.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-rulltarta-hallonsylt",
        "file": "klassisk-rulltarta-hallonsylt.html",
        "img": "rulltarta",
        "title": "Klassisk Rulltårta med Hallonsylt & Strösocker",
        "card_title": "Klassisk Rulltårta",
        "sub": "Saftig sockerkaksbotten rullad med frisk hallonsylt & pärlande socker",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt",
        "difficulty": "Enkel",
        "time": 20,
        "prep_time": "PT15M",
        "cook_time": "PT5M",
        "total_time": "PT20M",
        "prep_time_str": "15 min",
        "cook_time_str": "5 min",
        "time_str": "20 min",
        "calories": 190,
        "portions_num": 10,
        "portions_unit": "skivor",
        "rating": 4.99,
        "review_count": 780,
        "desc": "Sveriges snabbaste och mest klassiska fikakaka! En luftig, saftig sockerkaksbotten som gräddas på bara 5 minuter, breds med frisk hallonsylt eller jordgubbssylt och rullas ihop till en vacker spiral.",
        "long_desc": "Rulltårta är den perfekta kakan när du får oväntat fikabesök. Hemligheten för att rulltårtan inte ska spricka är att stjälpa upp den direkt på ett sockrat bakplåtspapper och rulla ihop den medan kakan fortfarande är ljummen.",
        "keywords": "rulltårta, rulltårta recept, drömrulltårta, klassisk rulltårta, snabb rulltårta, rulltårta med hallonsylt, saftig rulltårta",
        "alt": "Närbild på en skivad gyllene rulltårta med hallonsyltfyllning och strösocker på ett rustikt träfat med färska hallon",
        "equipment": ["Långpanna (ca 30x40 cm)", "Bakplåtspapper", "Elvisp"],
        "drink_pairing": "En kopp bryggkaffe, te eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Luftig Rulltårtsbotten", "items": [
                {"val": 3, "unit": "st", "name": "stora ägg"},
                {"val": 1.5, "unit": "dl", "name": "strösocker"},
                {"val": 2, "unit": "dl", "name": "vetemjöl (eller potatismjöl för glutenfritt)"},
                {"val": 1, "unit": "tsk", "name": "bakpulver"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker"},
                {"val": 2, "unit": "msk", "name": "mjölk eller vatten"}
            ]},
            {"group": "Fyllning & Rullning", "items": [
                {"val": 2, "unit": "dl", "name": "fast hallonsylt eller jordgubbssylt av god kvalitet"},
                {"val": 2, "unit": "msk", "name": "strösocker (att strö på pappret)"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Sätt ugnen & förbered plåt", "text": "Sätt ugnen på 250°C över-/undervärme. Lägg ett bakplåtspapper i en långpanna (ca 30x40 cm) och smörj det lätt med neutral olja.", "timer": 5},
            {"step": 2, "title": "Vispa ägg och socker pösigt", "text": "Vispa ägg och strösocker med elvisp i minst 4–5 minuter tills det blir riktigt vitt, tjockt och pösigt.", "timer": 5},
            {"step": 3, "title": "Vänd ner mjölblandningen", "text": "Blanda vetemjöl, bakpulver och vaniljsocker. Sikta ner i smeten och vänd försiktigt runt med en slickepott tillsammans med mjölken till en jämn, luftig smet.", "timer": 2},
            {"step": 4, "title": "Bred ut och grädda blixtsnabbt", "text": "Bred ut smeten jämnt i långpannan. Grädda mitt i ugnen i exakt 4–5 minuter tills kakan fått en vacker gyllengul färg. Vakta noga så den inte bränns!", "timer": 5},
            {"step": 5, "title": "Stjälp upp och bred på sylt", "text": "Strö strösocker på ett nytt bakplåtspapper på köksbänken. Stjälp genast upp den heta kakan på det sockrade pappret. Pensla det övre pappret med lite kallt vatten och dra försiktigt bort det. Bred genast ut hallonsylten i ett jämnt lager över kakan.", "timer": 3},
            {"step": 6, "title": "Rulla ihop och låt svalna", "text": "Rulla ihop kakan från långsidan med hjälp av det undre bakplåtspappret. Låt rulltårtan svalna med skarven nedåt i pappret. Skär i fina tjocka skivor och njut!", "timer": None}
        ],
        "pro_tips": "Pensla bakplåtspappret med lite kallt vatten efter att du stjälpt upp kakan – ångan gör att pappret lossnar lekande lätt utan att kakan fastnar!",
        "nutrition": {"calories": "190 kcal", "protein": "3g", "carbs": "36g", "fat": "3g", "sugar": "24g"},
        "faqs": [
            {"q": "Varför spricker rulltårtan när man rullar den?", "a": "Rulltårtan spricker om den gräddats för länge och blivit torr, eller om man väntar för länge med att rulla den. Rulla alltid ihop den medan den fortfarande är varm och mjuk."},
            {"q": "Kan man göra rulltårta glutenfri?", "a": "Ja, ersätt bara vetemjölet med 1.5 dl potatismjöl – kakan blir då naturligt glutenfri och extra fluffig och elastisk."}
        ],
        "community_reviews": [
            {"name": "Ewa Andersson", "date": "Idag", "rating": 5, "comment": "Otroligt saftig och perfekt rullad! Tog 15 minuter från start till fikabordet.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-pytt-i-panna-stekt-agg-rodbetor",
        "file": "klassisk-pytt-i-panna-stekt-agg-rodbetor.html",
        "img": "pyttipanna",
        "title": "Klassisk Pytt i Panna med Stekt Ägg & Inlagda Rödbetor",
        "card_title": "Klassisk Pytt i Panna",
        "sub": "Frasigt råstekt potatis med mört kött, karamelliserad lök & stekt ägg",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Enkel",
        "time": 30,
        "prep_time": "PT10M",
        "cook_time": "PT20M",
        "total_time": "PT30M",
        "prep_time_str": "10 min",
        "cook_time_str": "20 min",
        "time_str": "30 min",
        "calories": 530,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 690,
        "desc": "En klassisk svensk vardagshjälte och husmansfavorit! Små fina tärningar av stekt potatis, saftigt nötkött, rökt skinka och söt karamelliserad lök, serverad rykande het ur gjutjärnspannan med stekt ägg och inlagda rödbetor.",
        "long_desc": "Hemgjord pytt i panna är ljusår bättre än den frysta varianten. Hemligheten bakom en perfekt krispig pytt är att tärna alla ingredienser i fina små kuber (ca 8 mm) och steka potatisen separat i rikligt med smör så att den blir riktigt frasig och gyllene.",
        "keywords": "pyttipanna, pytt i panna recept, hemgjord pyttipanna, klassisk pytt i panna, pyttipanna stekt ägg, svensk pyttipanna",
        "alt": "Närbild på en gjutjärnspanna med krispig pytt i panna toppad med ett stekt ägg med krämig gula, hackad persilja och inlagda rödbetor",
        "equipment": ["Gjutjärnsstekpanna", "Skärbräda & vass kniv", "Stekspade"],
        "drink_pairing": "En kall svensk öl, must eller ett glas iskall mjölk.",
        "ingredients": [
            {"group": "Pytt i Panna", "items": [
                {"val": 800, "unit": "g", "name": "fast potatis (skalad & fint tärnad i 8 mm bitar)"},
                {"val": 300, "unit": "g", "name": "tillagat nötkött (t.ex. oxfilé, stek eller rostbiff, tärnat)"},
                {"val": 200, "unit": "g", "name": "rökt sidfläsk eller rökt skinka (fint tärnat)"},
                {"val": 2, "unit": "st", "name": "gula lökar (finhackade)"},
                {"val": 50, "unit": "g", "name": "smör och 2 msk rapsolja (att steka i)"},
                {"val": 1, "unit": "tsk", "name": "flingsalt & nymalen svartpeppar"},
                {"val": 1, "unit": "msk", "name": "kinesisk soja eller worcestershiresås (frivilligt)"}
            ]},
            {"group": "Klassiska Tillbehör", "items": [
                {"val": 4, "unit": "st", "name": "färska ägg (stekta sunny-side up)"},
                {"val": 1, "unit": "burk", "name": "inlagda rödbetor (tärnade)"},
                {"val": 1, "unit": "kruka", "name": "färsk bladpersilja (finhackad)"},
                {"val": 1, "unit": "flaska", "name": "HP-sås eller skånsk senap"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Tärna alla ingredienser", "text": "Skala potatisen och skär den i små fina tärningar (ca 8x8 mm). Skär även köttet, fläsket och löken i motsvarande små tärningar.", "timer": 10},
            {"step": 2, "title": "Råstek potatisen frasig", "text": "Hetta upp hälften av smöret och oljan i en stor gjutjärnspanna. Stek potatistärningarna på medelvärme under omrörning i ca 12–15 minuter tills de är genomstekta och har fått en gyllene krispig yta. Salta lätt och häll över i en skål.", "timer": 15},
            {"step": 3, "title": "Stek löken, fläsket och köttet", "text": "Lägg i resterande smör i pannan. Stek löken och det rökta fläsket tills löken är mjuk och gyllene. Tillsätt det tärnade nötköttet och låt steka med i 3–4 minuter så att allt får fin färg och smak.", "timer": 6},
            {"step": 4, "title": "Blanda ihop pytten", "text": "Vänd tillbaka den krispiga potatisen i pannan. Blanda om väl och låt allt bli rykande varmt tillsammans i 2 minuter. Smaka av med salt, svartpeppar och eventuellt några droppar soja.", "timer": 3},
            {"step": 5, "title": "Stek äggen", "text": "Stek äggen i en separat panna med smör så att vitan stelnar men äggulan förblir rinnig och krämig.", "timer": 3},
            {"step": 6, "title": "Servera och njut", "text": "Toppa pytten med de nystekta äggen, strö över rikligt med färsk persilja och servera direkt ur pannan med inlagda rödbetor och HP-sås.", "timer": None}
        ],
        "pro_tips": "Stek potatisen separat först innan du blandar ihop den med köttet och löken – då förblir potatisbitarna underbart krispiga istället för att bli mjuka och ångade.",
        "nutrition": {"calories": "530 kcal", "protein": "34g", "carbs": "38g", "fat": "28g", "sugar": "6g"},
        "faqs": [
            {"q": "Kan man använda kokt potatis från gårdagen?", "a": "Ja, överbliven kokt kall potatis fungerar utmärkt! Den steker dessutom ännu snabbare och blir härligt gyllene."},
            {"q": "Vilket kött passar bäst i pytt i panna?", "a": "En blandning av nötkött (oxfilé, biff eller stek) och rökt sidfläsk eller god korv ger den allra bästa balansen mellan sälta och mustighet."}
        ],
        "community_reviews": [
            {"name": "Johan Ström", "date": "Idag", "rating": 5, "comment": "Äkta hemgjord pyttipanna slår allt! Potatisen blev superkrispig och äggulan band ihop allt magiskt.", "verified": True}
        ]
    },
    {
        "slug": "klassisk-skomakarlada-biff-bacon-potatismos",
        "file": "klassisk-skomakarlada-biff-bacon-potatismos.html",
        "img": "skomakarlada",
        "title": "Klassisk Skomakarlåda med Biff, Rödvinssås & Knaperstekt Bacon",
        "card_title": "Klassisk Skomakarlåda",
        "sub": "Smörstekt biff på fluffigt potatismos med mustig rödvinssås, purjolök & bacon",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 40,
        "prep_time": "PT15M",
        "cook_time": "PT25M",
        "total_time": "PT40M",
        "prep_time_str": "15 min",
        "cook_time_str": "25 min",
        "time_str": "40 min",
        "calories": 590,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 590,
        "desc": "En genuin svensk krogklassiker som alltid imponerar! Mör utbankad biff som steks hastigt och vilar på en bädd av hemlagat lent potatismos, omsluten av en mustig rödvinssås och krönt med knaperstekt bacon och mjuk purjolök.",
        "long_desc": "Skomakarlåda har anor från tidigt 1900-tal på Stockholms klassiska restauranger. Rätten fick sitt namn för att biffarna bankades ut tunna som skosulor. Tillsammans med rödvinssås, bacon och purjolök blir det en oemotståndlig smakkombination.",
        "keywords": "skomakarlåda, skomakarlåda recept, klassisk skomakarlåda, skomakarlåda biff, svensk husmanskost skomakarlåda, biff med potatismos och rödvinssås",
        "alt": "Närbild på en elegant tallrik skomakarlåda med nystekt biff över krämigt potatismos, mörk rödvinssås och toppad med knaperstekt bacon och purjolök",
        "equipment": ["Gjutjärnsstekpanna", "Kastrull till mos", "Köttbankare"],
        "drink_pairing": "Ett fylligt rött vin som Syrah, Cabernet Sauvignon eller en mörk svensk lager.",
        "ingredients": [
            {"group": "Biff & Topping", "items": [
                {"val": 600, "unit": "g", "name": "lövbiff eller utbankad ryggbiff (4 portionsbitar)"},
                {"val": 140, "unit": "g", "name": "bacon eller rökt sidfläsk (tärnat)"},
                {"val": 1, "unit": "st", "name": "purjolök (strimlad, gärna både vit och grön del)"},
                {"val": 40, "unit": "g", "name": "smör (att steka i)"},
                {"val": 1, "unit": "tsk", "name": "flingsalt & nymalen grov svartpeppar"}
            ]},
            {"group": "Mustig Rödvinssås", "items": [
                {"val": 2.5, "unit": "dl", "name": "fylligt rött vin"},
                {"val": 2.5, "unit": "dl", "name": "vatten + 2 msk koncentrerad kalvfond eller oxfond"},
                {"val": 1, "unit": "st", "name": "schalottenlök (finhackad)"},
                {"val": 1, "unit": "msk", "name": "tomatpuré & 1 tsk torkad timjan"},
                {"val": 1, "unit": "msk", "name": "smör (att blanka av såsen med)"},
                {"val": 1, "unit": "tsk", "name": "maizena (utrört i lite vatten)"}
            ]},
            {"group": "Lent Potatismos", "items": [
                {"val": 900, "unit": "g", "name": "mjölig potatis"},
                {"val": 50, "unit": "g", "name": "smör"},
                {"val": 1.5, "unit": "dl", "name": "varm mjölk eller grädde"},
                {"val": 1, "unit": "krm", "name": "riven muskotnöt, salt & vitpeppar"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Koka potatismoset", "text": "Skala och koka potatisen mjuk i saltat vatten. Häll av och stöt potatisen slät med smör och varm mjölk. Smaka av med salt, vitpeppar och en nypa muskotnöt. Håll varmt.", "timer": 20},
            {"step": 2, "title": "Koka den mustiga rödvinssåsen", "text": "Fräs finhackad schalottenlök och tomatpuré i lite smör i en kastrull. Häll på rött vin, vatten, kalvfond och timjan. Låt koka ihop och reducera till hälften (ca 10 minuter). Red av med maizena och vispa i en klick kallt smör för fin glans.", "timer": 12},
            {"step": 3, "title": "Stek bacon och purjolök", "text": "Knaperstek det tärnade baconet i en stekpanna. Tillsätt den strimlade purjolöken mot slutet och låt den mjukna och bli glansig i baconfettet. Lägg upp på ett fat och håll varmt.", "timer": 6},
            {"step": 4, "title": "Stek biffarna snabbt på hög värme", "text": "Hetta upp smör i pannan tills det tystnar och får nötbrun färg. Stek biffarna snabbt på hög värme i ca 1 minut per sida så de får fin stekyta men förblir saftiga och rosa i mitten. Salta och peppra.", "timer": 3},
            {"step": 5, "title": "Montera och servera", "text": "Lägg en generös portion potatismos mitt på varma tallrikar. Placera en nystekt biff ovanpå moset, ringla den heta rödvinssåsen runt om och toppa köttet med det knaperstekta baconet och purjolöken.", "timer": None}
        ],
        "pro_tips": "Stek biffarna i rykande het panna i högst 1 minut per sida – eftersom biffarna är tunna blir de torra om de steks för länge.",
        "nutrition": {"calories": "590 kcal", "protein": "44g", "carbs": "36g", "fat": "28g", "sugar": "5g"},
        "faqs": [
            {"q": "Varför heter det skomakarlåda?", "a": "Namnet kommer från att biffarna traditionellt bankades ut med köttklubba så att de liknade formen av en skosula."},
            {"q": "Kan man använda ryggbiff eller oxfilé?", "a": "Ja, finare bitar av ryggbiff eller oxfilé skurna i skivor och lätt utbankade ger en fantastiskt mör och lyxig skomakarlåda."}
        ],
        "community_reviews": [
            {"name": "Fredrik Viklund", "date": "Idag", "rating": 5, "comment": "Krogkänsla hemma! Rödvinssåsen var helt fantastisk och bacon/purjo-toppingen lyfte hela rätten.", "verified": True}
        ]
    },
    {
        "slug": "klassiskt-dillkott-hogrev-sotsur-dillsas",
        "file": "klassiskt-dillkott-hogrev-sotsur-dillsas.html",
        "img": "dillkott",
        "title": "Klassiskt Dillkött på Högrev med Sötsur Dillsås & Morötter",
        "card_title": "Klassiskt Dillkött",
        "sub": "Långkokt mört högrev i en krämig sötsur dillsås med morötter & potatis",
        "category": "Husmanskost",
        "cat_slug": "husmanskost",
        "cat_key": "husmanskost",
        "diet": "Husmanskost",
        "difficulty": "Medel",
        "time": 90,
        "prep_time": "PT15M",
        "cook_time": "PT75M",
        "total_time": "PT90M",
        "prep_time_str": "15 min",
        "cook_time_str": "1 tim 15 min",
        "time_str": "1 tim 30 min",
        "calories": 460,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.98,
        "review_count": 510,
        "desc": "En tidlös svensk husmansklenod! Långkokt, smältande mört högrev eller kalvkött som sjuder i en aromatisk buljong med morötter, serverat i en krämig och fyllig sötsur dillsås med rikligt av färskhackad dill och kokt potatis.",
        "long_desc": "Dillkött är en klassiker med anor från det gamla svenska bondesamhället. Den unika smaken skapas av balansen mellan ättika, socker och färsk dill som kokas ihop med den mustiga köttbuljongen och grädde.",
        "keywords": "dillkött, dillkött recept, klassiskt dillkött, dillkött högrev, dillkött kalv, sötsur dillsås, svensk husmanskost dillkött",
        "alt": "Närbild på en skål klassiskt dillkött med möra högrevsbitar och morötter i krämig grönprickig dillsås med nykokt potatis",
        "equipment": ["Stor gryta", "Kastrull till dillsås", "Skumslev"],
        "drink_pairing": "Ett friskt vitt vin som Riesling, ljus lageröl eller ett glas kall mjölk.",
        "ingredients": [
            {"group": "Köttkok & Buljong", "items": [
                {"val": 800, "unit": "g", "name": "högrev, grytbitar av kalv eller märgpipa (i 3 cm kuber)"},
                {"val": 1.2, "unit": "liter", "name": "vatten (så det täcker köttet)"},
                {"val": 2, "unit": "st", "name": "morötter (slantade)"},
                {"val": 1, "unit": "st", "name": "gul lök (i klyftor)"},
                {"val": 6, "unit": "st", "name": "vitpepparkorn & 6 kryddpepparkorn"},
                {"val": 2, "unit": "st", "name": "lagerblad & dillstjälkar från dillkrukan"},
                {"val": 1.5, "unit": "tsk", "name": "salt"}
            ]},
            {"group": "Krämig Sötsur Dillsås", "items": [
                {"val": 4, "unit": "dl", "name": "silad köttbuljong (från köttkoket)"},
                {"val": 1.5, "unit": "dl", "name": "vispgrädde"},
                {"val": 2, "unit": "msk", "name": "smör & 2 msk vetemjöl"},
                {"val": 1.5, "unit": "msk", "name": "ättiksprit (12%) eller vitvinsvinäger"},
                {"val": 2, "unit": "msk", "name": "strösocker (justera efter smak för sötsur balans)"},
                {"val": 1, "unit": "kruka", "name": "färsk dill (rikligt finhackad)"},
                {"val": 1, "unit": "krm", "name": "salt & vitpeppar"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "portioner", "name": "nykokt delikatesspotatis med dill"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Koka köttet & skumma", "text": "Lägg köttbitarna i en gryta med vatten och salt. Koka upp och skumma noga av ytan. Lägg i lök, dillstjälkar, pepparkorn och lagerblad. Sjud under lock på svag värme i ca 1 timme.", "timer": 60},
            {"step": 2, "title": "Tillsätt morötterna", "text": "Lägg i morotsslantar och sjud ytterligare 15–20 minuter tills köttet är smältande mört. Sila av och spara 4 dl av den goda buljongen.", "timer": 20},
            {"step": 3, "title": "Gör dillsåsen", "text": "Smält smöret i en kastrull och vispa i vetemjölet. Späd under vispning med den heta köttbuljongen och grädden. Låt sjuda sakta i ca 5 minuter till en slät krämig sås.", "timer": 5},
            {"step": 4, "title": "Smaka av sötsurt", "text": "Smaka av såsen med ättika, strösocker, salt och vitpeppar. Såsen ska ha en tydlig och frisk balans mellan sötma och syra.", "timer": 2},
            {"step": 5, "title": "Vänd ner köttet och dillen", "text": "Lägg det möra köttet och morötterna i den heta såsen. Vänd ner rikligt med finhackad färsk dill precis före servering så att dillen behåller sin vackra gröna färg och arom.", "timer": 2},
            {"step": 6, "title": "Servera med nykokt potatis", "text": "Häll upp dillköttet i en djup skål och servera rykande hett med nykokt potatis.", "timer": None}
        ],
        "pro_tips": "Spara stjälkarna från dillen och låt dem koka med i köttbuljongen – då drar köttet åt sig dillarom redan under kokningen!",
        "nutrition": {"calories": "460 kcal", "protein": "38g", "carbs": "22g", "fat": "24g", "sugar": "8g"},
        "faqs": [
            {"q": "Kan man använda lamm istället för nötkött?", "a": "Ja, dillkött på lamm (lammstek eller lammbog) är en klassisk svensk variation som kallas dill-lamm och smakar helt underbart."},
            {"q": "Går dillkött att frysa?", "a": "Ja, dillkött fryser utmärkt. Tillsätt gärna lite extra färsk dill vid uppvärmning för nylagad fräschör."}
        ],
        "community_reviews": [
            {"name": "Ingrid Holmgren", "date": "Idag", "rating": 5, "comment": "Precis som min mormor lagade det! Den sötsura dillsåsen var helt perfekt avvägd.", "verified": True}
        ]
    },
    {
        "slug": "gammaldags-appelkram-kanel-kall-mjolk",
        "file": "gammaldags-appelkram-kanel-kall-mjolk.html",
        "img": "appelkram",
        "title": "Gammaldags Äppelkräm med Kanel & Iskall Mjölk",
        "card_title": "Gammaldags Äppelkräm",
        "sub": "Höstens godaste äppelkräm med svenska äpplen, kanel & söt vanilj",
        "category": "Fika & Bakning",
        "cat_slug": "fika-och-bakning",
        "cat_key": "fika",
        "diet": "Vegetariskt / Vegansk",
        "difficulty": "Mycket enkel",
        "time": 20,
        "prep_time": "PT10M",
        "cook_time": "PT10M",
        "total_time": "PT20M",
        "prep_time_str": "10 min",
        "cook_time_str": "10 min",
        "time_str": "20 min",
        "calories": 130,
        "portions_num": 4,
        "portions_unit": "portioner",
        "rating": 4.99,
        "review_count": 670,
        "desc": "En klassisk svensk höstfavorit som väcker barndomsminnen! Hemgjord äppelkräm kokt på svenska syrliga höstäpplen, kanelstång, vanilj och socker, redd till perfekt silkeslen konsistens och serverad med iskall mjölk.",
        "long_desc": "Gammaldags äppelkräm är det absolut godaste sättet att ta tillvara på höstens äppelskörd. Den äts lika gärna som ett enkelt mellanmål som till efterrätt med en skvätt grädde eller mjölk.",
        "keywords": "äppelkräm, äppelkräm recept, gammaldags äppelkräm, hemgjord äppelkräm, äppelkräm med kanel, svensk fruktkräm",
        "alt": "Närbild på en glasskål med gyllenbrun äppelkräm toppad med kanel där kall mjölk hälls över i vackra vita mönster",
        "equipment": ["Kastrull", "Skalkniv & skärbräda", "Liten skål till potatismjöl"],
        "drink_pairing": "Ett glas iskall lantmjölk eller en klick vispad grädde.",
        "ingredients": [
            {"group": "Äppelkräm", "items": [
                {"val": 600, "unit": "g", "name": "svenska äpplen (t.ex. Ingrid Marie, skalade, urkärnade & tärnade)"},
                {"val": 5, "unit": "dl", "name": "vatten"},
                {"val": 0.75, "unit": "dl", "name": "strösocker (justera efter äpplenas syra)"},
                {"val": 1, "unit": "st", "name": "hel kanelstång"},
                {"val": 1, "unit": "tsk", "name": "vaniljsocker eller 0.5 tsk mald kanel"},
                {"val": 2.5, "unit": "msk", "name": "potatismjöl (utrört i 3 msk kallt vatten)"}
            ]},
            {"group": "Servering", "items": [
                {"val": 4, "unit": "dl", "name": "iskall färsk mjölk eller ovispad grädde"},
                {"val": 1, "unit": "krm", "name": "mald kanel & lite strösocker"}
            ]}
        ],
        "instructions": [
            {"step": 1, "title": "Förbered äpplena", "text": "Skala, kärna ur och skär äpplena i ca 2 cm stora tärningar.", "timer": 5},
            {"step": 2, "title": "Koka äppelkompotten", "text": "Lägg äppelbitar, vatten, strösocker och kanelstång i en kastrull. Koka upp och låt sjuda på medelvärme i ca 6–8 minuter tills äppelbitarna börjar mjukna men fortfarande håller ihop.", "timer": 8},
            {"step": 3, "title": "Rör ut potatismjölet", "text": "Dra kastrullen från värmen och plocka ur kanelstången. Rör ut potatismjölet i 3 msk kallt vatten i ett glas.", "timer": 2},
            {"step": 4, "title": "Red krämen", "text": "Häll ner potatismjölsblandningen i en fin stråle under ständig omrörning. Sätt tillbaka kastrullen på plattan och låt krämen precis koka upp så att första kokbubblan syns – ta genast av från värmen (koka inte vidare då krämen kan bli seg).", "timer": 2},
            {"step": 5, "title": "Sockra ytan för att undvika skinn", "text": "Rör i vaniljsockret. Häll upp krämen i en skål eller portionsskålar och strö lite strösocker över ytan så bildas inget skinn.", "timer": 2},
            {"step": 6, "title": "Servera ljummen eller kall", "text": "Servera äppelkrämen ljummen eller väl kyld med ett generöst glas iskall mjölk eller en skvätt grädde.", "timer": None}
        ],
        "pro_tips": "Ta alltid kastrullen från plattan direkt när första kokbubblan syns efter redningen – om krämen kokar för länge med potatismjöl bryts stärkelsen ner och krämen blir tunn och seg.",
        "nutrition": {"calories": "130 kcal", "protein": "1g", "carbs": "32g", "fat": "0g", "sugar": "26g"},
        "faqs": [
            {"q": "Varför blir krämen vattnig efter en stund?", "a": "Om man stoppar en sked med saliv i krämen bryter enzymerna ner potatismjölsredningen. Använd alltid en ren sked vid servering."},
            {"q": "Kan man frysa in äppelkräm?", "a": "Kräm redd med potatismjöl tappar konsistensen om den fryses. Förvara den istället i en tät burk i kylen där den håller i upp till 5 dagar."}
        ],
        "community_reviews": [
            {"name": "Birgit Lindell", "date": "Idag", "rating": 5, "comment": "Barndom i en skål! Perfekt syra och med iskall mjölk till var det oslagbart gott.", "verified": True}
        ]
    }
]











