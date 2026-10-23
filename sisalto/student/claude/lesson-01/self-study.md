# Osio 01: Agentti ei ole chat: ensimmäinen tehtävä ja tallennuspiste

> Ajattelukysymys: Mitä agentti teki koneellasi juuri nyt, ja mistä sen näet?

Olet ehkä käyttänyt chat-palvelua. Kirjoitat kysymyksen, ja saat vastauksen tekstinä. Agentti toimii eri tavalla. Se lukee ja muuttaa tiedostoja koneellasi ja ajaa komentoja. Siksi sitä myös valvotaan eri tavalla.

Tässä osiossa annat agentille ensimmäisen rajatun tehtävän. Opit lukemaan lupapyynnön ja tarkistamaan, mitä muuttui. Teet ensimmäisen tallennuspisteen (commit) ja kokeilet palata siihen. Lopuksi kirjaat ensimmäiset päätökset päätöslokiin.

Osion jälkeen projektikansiossa on neljä uutta asiaa: työkortti, kehotepohjat, päätösloki ja Git. Käytät niitä koko työpajan ajan.

## Chat-palvelu vastaa, agentti tekee

**Chat-palvelu** vastaa tekstillä. Se ei muuta tiedostoja koneellasi. Jos haluat vastauksen tiedostoon, kopioit sen itse.

Agentti lukee ja muokkaa tiedostoja ja ajaa komentoja projektikansiossa. Kun pyydät siltä jotain, lopputulos voi olla uusi tiedosto, muuttunut tiedosto tai ajettu ohjelma.

Ero näkyy samalla pyynnöllä. Pyydät: "Tee lista Wilmaan täytettävistä kokonaisuuksista kuvauspaketin osan 6 mukaan." Chat-palvelussa liität ensin kuvauspaketin tekstin keskusteluun. Saat vastauksen ruudulle. Koneellasi ei muutu mitään. Agentti lukee kuvauspaketin itse kansiosta `maarittely`. Se voi kirjoittaa listan uuteen tiedostoon projektikansioon. Näet tiedoston Resurssienhallinnassa.

Tämä on agentin hyöty ja riski. Se tekee työn puolestasi. Se voi myös muuttaa jotain, mitä et pyytänyt.

Viestiä, jolla annat agentille tehtävän, kutsutaan kehotteeksi. Työpajassa käytät kehotepohjia. Kehotepohja on valmis kehote, jossa on hakasulkeissa aukkoja. Täytät aukot itse, koska niihin tarvitaan sinun tietoasi. Esimerkiksi kehotepohjaan K1 kirjoitat, mitä haluat ohjelmasta erityisesti tietää.

**Pysähdy hetkeksi:** Mitä agentti voi tehdä koneellasi, mitä chat-palvelu ei voi?

## Projektikansio on agentin työalue

Valitsit osiossa 00 projektikansioksi `C:\dev\oppisopimustayttaja`. Se on agentin työalue. Kaikki, mitä agentti työpajassa tekee, tapahtuu sen sisällä. Kansion ulkopuoli ei kuulu agentille. Muut kansiosi, sähköpostisi ja Wilma ovat sen ulkopuolella.

Raja auttaa myös tarkistamaan. Kun agentti haluaa tehdä jotain kansion ulkopuolella, se on aina syy pysähtyä.

Agentti näkee kaiken, mitä kansiossa on. Se lukee kuvauspaketin ja oman kokemuksesi, jos pyydät. Siksi kansioon ei tuoda mitään, mitä agentti ei saa nähdä.

Agentin työn näet kolmesta paikasta. Ennen muutosta näet lupapyynnön. Muutoksen jälkeen näet muutosnäkymän ja tiedostot Resurssienhallinnassa. Tallennuspisteistä näet, mitä on tehty aiemmin. Kun joku kysyy, mitä agentti teki, vastaat näiden perusteella, et agentin oman kertomuksen perusteella.

## Lupapyyntö ja kolme kysymystä

Oletuksena agentti kysyy luvan, ennen kuin se muuttaa tiedostoa tai ajaa komennon. Tätä kysymystä kutsutaan **lupapyynnöksi**. Asetusta, joka ratkaisee, mitä agentti saa tehdä kysymättä, kutsutaan lupatilaksi. Muutokset voi sallia automaattisesti. Tässä osiossa et tee niin. Päätät asiasta itse osiossa 05.

Lue jokainen lupapyyntö kolmella kysymyksellä:

- Mikä? Mikä tiedosto tai komento on kyseessä?
- Missä? Onko se projektikansion sisällä?
- Miksi? Liittyykö se siihen, mitä pyysin?

Jos jokin jää epäselväksi, älä hyväksy vielä. Pyydä agenttia selittämään omin sanoin, mitä se aikoo tehdä ja miksi. Hyväksy vasta, kun ymmärrät vastauksen.

Lupapyynnössä voi olla myös vaihtoehto, joka sallii saman toiminnon jatkossa kysymättä. Älä valitse sitä. Hyväksy vain tämän kerran. Muuten seuraava samanlainen muutos tapahtuu ilman, että näet sitä etukäteen. Työkortissa sama sääntö kuuluu näin: hyväksyn vain tämän kerran, enkä valitse vaihtoehtoa, joka sallii saman jatkossa kysymättä.

Esimerkki: pyysit agenttia luomaan tiedoston `TYOKORTTI.md`. Lupapyynnössä agentti haluaa luoda juuri sen tiedoston projektikansioon. Kaikki kolme kysymystä saavat vastauksen, ja hyväksyt. Jos agentti haluaisi samalla muuttaa tiedostoa Tiedostot-kansiossa, Missä-kysymys ei täyty. Kiellät ja kysyt syytä.

Komento on vaikeampi lukea kuin tiedoston nimi. Kun otat Gitin käyttöön, agentti pyytää lupaa ajaa komennon. Mikä: komento, joka ottaa Gitin käyttöön. Missä: projektikansiossa. Miksi: pyysit sitä. Jos komennosta ei näe, mitä se tekee, kirjoita agentille: "Selitä tämä komento yhdellä lauseella. Mitä se muuttaa?"

Lupapyyntöjä tulee paljon, varsinkin asennuksissa. Silloin houkuttaa hyväksyä lukematta. Juuri silloin virhe pääsee läpi. Jos pyyntöjä tulee peräkkäin kymmenen, lue jokainen. Jos et jaksa, pidä tauko.

Kun muutos on tehty, näet sen sovelluksen **muutosnäkymästä**. Se näyttää, mitä tiedostoissa muuttui. Lisätyt ja poistetut rivit erottuvat toisistaan.

**Pysähdy hetkeksi:** Milloin hyväksyisit lupapyynnön lukematta? Vastaus on: ei koskaan.

## Tallennuspiste

**Git** on ohjelma, jolla tallennuspisteet tehdään. Tallennuspiste (commit) on Gitillä tehty nimetty välitila projektikansiosta. Siihen voi palata. Paluu kumoaa kaikki tallennuspisteen jälkeen tehdyt muutokset. Aiemmat tallennuspisteet säilyvät.

Tee tallennuspiste kahdessa kohdassa: ennen jokaista isompaa tehtävää ja jokaisen hyväksynnän jälkeen. Silloin sinulla on aina kohta, johon palata, jos agentti rikkoo jotain.

Kuvittele, että pyydät myöhemmin agenttia muuttamaan urasuunnitelman näkymää. Samalla opiskelijahaku lakkaa toimimasta. Ilman tallennuspistettä sinun pitäisi selittää agentille, millainen haku oli. Tallennuspisteen avulla palaat kohtaan, jossa haku toimi, ja yrität muutosta uudelleen.

Jokaisella tallennuspisteellä on viesti. Viesti kertoo, mitä tallennuspisteessä on valmiina. Kirjoita se niin, että tunnistat sen viikon päästä. "Työkortti ja kehotepohjat valmiina" on hyvä viesti. "Muutoksia" ei ole.

Git toimii vain omalla koneellasi. Se ei ole varmuuskopio pilveen. Gitiä ei tarvitse ymmärtää tämän enempää. Pyydät agenttia tekemään tallennuspisteen tai palaamaan siihen kehotepohjilla K6 ja K7.

## Päätösloki: sinä olet portinvartija

Agentti tekee työn. Sinä päätät, kelpaako se. **Päätösloki** on tiedosto `PAATOSLOKI.md`. Kirjaat siihen jokaisesta isommasta agentin tuotoksesta päätöksen ja yhden perusteen omin sanoin.

Päätöksiä on kolme. Hyväksyn tarkoittaa, että tuotos kelpaa. Korjautan tarkoittaa, että pyydän agenttia korjaamaan. Hylkään tarkoittaa, että palaan tallennuspisteeseen.

Hylkäyksessä järjestys on tärkeä: kun hylkään, palaan ensin ja kirjaan päätöksen sitten. Sulje ensin Muistio. Palaa sitten tallennuspisteeseen ja kirjoita merkintä vasta sen jälkeen. Paluu voi kumota myös merkinnän, jonka kirjoitit ennen paluuta. Kehotepohja K7 pyytää agenttia jättämään päätöslokin, kriteerit ja testit ennalleen. Järjestys suojaa merkintääsi silloinkin, kun agentti ei noudata pyyntöä.

Peruste on lyhyt, mutta se kertoo, mitä tarkistit. "Näyttää hyvältä" ei ole peruste. "Tiivistelmästä puuttui, että työpaikan pitää olla Wilmassa ennen oppisopimusta" on peruste.

Isompi tuotos on esimerkiksi uusi tiedosto, agentin suunnitelma tai sovelluksen uusi toimiva osa. Pieniä korjauksia ei tarvitse kirjata yksitellen.

Agentti ei kirjoita päätöslokia. Jos se kirjoittaisi, se arvioisi omaa työtään. Päätösloki näyttää jälkikäteen, mitä sinä tarkistit ja päätit. Siksi kirjoitat sen itse Muistiolla.

## Esimerkki: tiivistelmä, joka on melkein oikein

Pyydät agenttia tiivistämään kuvauspaketin viidellä lauseella. Yksi lause kuuluu: "Ohjelma etsii opiskelijan Wilmasta nimellä ja täyttää hänen lomakkeensa."

Luet lauseen omaa kokemustasi vasten. Tiedät, että nimi ei riitä. Kuvitteellisessa aineistossa on kaksi Aino Testista. Toisen opiskelijanumero on 000123, toisen 000456. Kuvauspaketin osa 9 sanoo, että oikea henkilö varmistetaan opiskelijanumerolla ennen Wilma-tallennusta.

Kirjaat päätöslokiin päätöksen korjautan. Perusteeksi kirjoitat: "Nimi on vain hakusana. Kohdistus tehdään opiskelijanumerolla, koska Aino Testisiä on kaksi."

Agentti ei keksinyt mitään. Se tiivisti liikaa. Tällaisen kohdan huomaat vain, koska tunnet työn.

## Yhteenveto

Agentti lukee ja muuttaa tiedostoja ja ajaa komentoja projektikansiossa. Luet jokaisen lupapyynnön kolmella kysymyksellä ja katsot muutokset muutosnäkymästä. Tallennuspiste on Gitillä tehty välitila, johon voi palata. Päätösloki on sinun: kirjaat siihen päätöksen ja perusteen omin sanoin.
