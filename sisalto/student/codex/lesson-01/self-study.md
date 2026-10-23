# Osio 01: Agentti ei ole chat: ensimmäinen tehtävä ja tallennuspiste

> Ajattelukysymys: Mitä agentti teki koneellasi juuri nyt, ja mistä sen näet?

Olet ehkä käyttänyt chat-palvelua. Kirjoitat kysymyksen, ja saat vastauksen tekstinä. Agentti toimii eri tavalla. Se lukee ja muuttaa tiedostoja koneellasi ja ajaa komentoja. Siksi sitä myös valvotaan eri tavalla.

Tässä osiossa annat agentille ensimmäisen rajatun tehtävän. Opit tarkistamaan, mitä muuttui, ja lukemaan lupapyynnön. Teet ensimmäisen tallennuspisteen (commit) ja kokeilet palata siihen. Lopuksi kirjaat ensimmäiset päätökset päätöslokiin.

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

Agentin työn näet kolmesta paikasta. Kun agentti haluaa ylittää rajan, näet lupapyynnön. Muutoksen jälkeen näet muuttuneet tiedostot agenttisovelluksen Git-toiminnoista ja tiedostot Resurssienhallinnassa. Tallennuspisteistä näet, mitä on tehty aiemmin. Kun joku kysyy, mitä agentti teki, vastaat näiden perusteella, et agentin oman kertomuksen perusteella.

## Hiekkalaatikko ja kolme kysymystä

Codexissa agentti toimii **hiekkalaatikossa**. Hiekkalaatikko on tekninen raja. Oletusoikeuksilla se estää kirjoittamisen projektikansion ulkopuolelle ja verkkoyhteydet ilman hyväksyntää. Oikeusasetus ratkaisee, milloin agentti kysyy ennen rajan ylitystä. Täysiä oikeuksia ei käytetä, koska silloin agenttia ei ole rajattu projektikansioon.

Kun agentti haluaa ylittää rajan, sovellus kysyy lupaa. Tätä kysymystä kutsutaan **lupapyynnöksi**. Esimerkiksi asennus verkosta tarvitsee luvan. Projektikansion sisällä agentti voi oletusoikeuksilla yleensä muokata tiedostoja kysymättä. Vetäjä näyttää, miten sinun sovellusversiosi toimii. Kun hyväksyt lupapyynnön, hyväksy vain tämän kerran. Älä valitse vaihtoehtoa, joka sallii saman jatkossa kysymättä.

Siksi tällä polulla pääkontrolleja on kaksi. Teet tallennuspisteen ennen isompaa tehtävää. Tehtävän jälkeen tarkistat itse, mitkä tiedostot muuttuivat. Kun Git on käytössä, avaat agenttisovelluksen Git-toiminnoista näkymän, jossa muuttuneet tiedostot näkyvät. Ennen Gitiä katsot projektikansion Resurssienhallinnassa. Lisäksi avaat muuttuneen tiedoston ja katsot, mitä siinä on.

Agentti osaa myös luetella, mitä se muutti. Luettelo on hyvä apu, mutta se on agentin oma kertomus. Jos agentti muutti jotain huomaamattaan tai jätti sen kertomatta, luettelosta se ei näy. Git-toiminnot, Resurssienhallinta ja avattu tiedosto näyttävät, mitä kansiossa oikeasti on. Jos agentin luettelo ja Git-toiminnot eroavat, Git-toiminnot ratkaisevat. Pysähdy silloin ja kysy agentilta syytä.

Tällä polulla riski on se, että tarkistus jää tekemättä. Agentti ei kysy jokaisesta muutoksesta, joten mikään ei pysäytä sinua. Tee muuttuneiden tiedostojen tarkistuksesta tapa. Tarkista ne jokaisen tehtävän jälkeen, myös silloin, kun kaikki näyttää toimivan.

Käytä lupapyyntöön ja muuttuneisiin tiedostoihin samoja kolmea kysymystä:

- Mikä? Mikä tiedosto tai komento on kyseessä?
- Missä? Onko se projektikansion sisällä?
- Miksi? Liittyykö se siihen, mitä pyysin?

Jos jokin jää epäselväksi, älä hyväksy vielä. Pyydä agenttia selittämään omin sanoin, mitä se teki tai aikoo tehdä ja miksi. Hyväksy vasta, kun ymmärrät vastauksen.

Esimerkki: pyysit agenttia luomaan tiedoston `TYOKORTTI.md`. Avaat projektikansion Resurssienhallinnassa. Siellä on kansio `maarittely` ja juuri tämä uusi tiedosto. Kaikki kolme kysymystä saavat vastauksen. Jos kansiossa olisi myös tiedosto, jota et pyytänyt, Miksi-kysymys ei täyty. Kysyt syytä ja palaat tarvittaessa tallennuspisteeseen. Jos sovellus pyytää lupaa verkkoyhteyteen, vaikka pyysit vain tiedostoa, kiellät.

Komento on vaikeampi lukea kuin tiedoston nimi. Pyydä agenttia kertomaan vastauksessaan, mitä komentoja se ajoi. Komennon vaikutuksen tarkistat silti itse, esimerkiksi Git-toiminnoista. Kun otat Gitin käyttöön, vastauksessa on komento, joka ottaa Gitin käyttöön projektikansiossa. Mikä, missä ja miksi saavat vastauksen. Jos komennosta ei näe, mitä se tekee, kirjoita agentille: "Selitä tämä komento yhdellä lauseella. Mitä se muutti?"

**Pysähdy hetkeksi:** Milloin hyväksyisit lupapyynnön lukematta? Vastaus on: ei koskaan.

## Tallennuspiste

**Git** on ohjelma, jolla tallennuspisteet tehdään. Tallennuspiste (commit) on Gitillä tehty nimetty välitila projektikansiosta. Siihen voi palata. Paluu kumoaa kaikki tallennuspisteen jälkeen tehdyt muutokset. Aiemmat tallennuspisteet säilyvät.

Tee tallennuspiste kahdessa kohdassa: ennen jokaista isompaa tehtävää ja jokaisen hyväksynnän jälkeen. Tällä polulla tallennuspiste ennen tehtävää on erityisen tärkeä. Agentti voi muuttaa kansion tiedostoja kysymättä, joten paluu on turvaverkkosi.

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

Agentti lukee ja muuttaa tiedostoja ja ajaa komentoja projektikansiossa. Hiekkalaatikko rajaa sen projektikansioon. Teet tallennuspisteen ennen tehtävää ja tarkistat muuttuneet tiedostot sen jälkeen agenttisovelluksen Git-toiminnoista kolmella kysymyksellä. Agentin oma luettelo on vain apu. Päätösloki on sinun: kirjaat siihen päätöksen ja perusteen omin sanoin.
