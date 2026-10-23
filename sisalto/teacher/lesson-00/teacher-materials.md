# Opettajan materiaali: osio 00 – Ennen työpajaa: kone, kansio ja turvaraja

## Ajattelukysymys ja tavoitteet (Bloom)

> Ajattelukysymys: Mitä tietoa agentti saa nähdä, ja mitä se ei saa nähdä koskaan?

- Ymmärtää: oppija kertoo omin sanoin, mitä työpajassa rakennetaan ja mitä sen lopussa on valmiina.
- Muistaa: oppija nimeää tiedot, joita ei koskaan anneta agentille.
- Soveltaa: oppija luo projektikansion oikeaan paikkaan ja tekee käynnistystestin.
- Analysoida: oppija kuvaa omasta työstään kolme kirjauksen virhealtista kohtaa.

Osio on tunnistamisen tasolla. Oppija tekee sen itsenäisesti viimeistään kolme arkipäivää ennen työpajaa. Hän ei vielä rakenna mitään. Tavoitteet näkyvät `oma-kokemus.md`:ssä: Ymmärtää kohdassa Mitä työpajan lopussa on valmiina, Muistaa kohdissa Mitä agentti saa nähdä ja Mitä agentti ei saa nähdä koskaan, Analysoida kolmessa virheessä. Vetäjän raskain työ liittyy tähän osioon: ennakkopyynnöt, harjoitusajo ja savutesti.

Lupaa oppijalle sama kuin hänen lukutekstinsä. Vähimmäistavoite: simuloitu Wilma ja Oppisopimustäyttäjä käynnistyvät `KAYNNISTYS.md`:n ohjeella ilman agenttia. Sovellus avaa näkyvän selaimen, ja oppija kirjautuu itse. Yhden opiskelijan tiedot haetaan kuvitteellisista lähteistä tarkistettaviksi. Urasuunnitelman Wilma-tallennus varmennetaan uudelleenluvulla. Kahden opiskelijan jonossa VALMIS tulee vasta varmennuksen jälkeen. Lisäksi oppijalla on ohjetiedosto, työlista, päätösloki, hyväksymiskriteerit, `TESTIT.md` ja `JATKO.md`. Tavoite lisää lukutilat ja ristiriidat, listatuonnin ja nimikaimat, jonon tilan Odottaa lisätietoja, oppisopimuksen riippuvuuksineen, PRO-ilmeen, yhden häiriötestin ja testi-Wilman lukukokeilun, jos ehdot täyttyvät. Älä lupaa koko tuotetta V01–V10. Oikea Wilma, oikeat tiedot, asennuspaketti ja pilotti ovat jatkoa.

## Aikataulu (minuutit, summa = osion kesto)

| Min | Oppijan työ |
|---|---|
| 12 | Lukuteksti (self-study.md) |
| 8 | Tehtävä 1: tilaus ja agenttisovellus |
| 10 | Tehtävä 2: projektikansio |
| 17 | Tehtävä 3: kuvauspaketti kansioon ja ensimmäisen pääosan (KP osat 1–12) luku |
| 12 | Tehtävä 4: käynnistystesti |
| 13 | Tehtävä 5: muistilista, .md-tiedoston tallennus ja avaus, oman tiedoston alku |
| 13 | Tehtävä 6: oma kokemus |
| 5 | Tehtävä 7: testi-Wilman tilanne |
| 90 | Yhteensä |

Osion kesto on 60–90 min. Taulukko on mitoitettu ylärajalle. Oppija selviää noin 75 minuutissa, jos sovellus ja tilaus toimivat valmiiksi. KP:n ensimmäinen pääosa (noin 1 200 sanaa) luetaan tässä, jotta osion 02 aika riittää rakentamiseen. Savutesti (15–30 min) tehdään erikseen osion 00 jälkeen.

## Ennen osiota

Ennakon aikajana tarkistuslistana:

- [ ] 4 viikkoa ennen: tilaus tai lisenssi oppijan polulle.
- [ ] 4 viikkoa ennen: IT-pyyntö lähetetty (sisältö alla).
- [ ] 4 viikkoa ennen: testi-Wilma-pyyntö Wilma-pääkäyttäjälle (osa P10:tä, sisältö alla).
- [ ] 4 viikkoa ennen: koulutuksen vastuuhenkilöltä ensimmäinen koulutus ja sen tutkinnon osat (P05). Tieto on julkista, ja sen saa antaa agentille.
- [ ] 2 viikkoa ennen: harjoitusajo oppijan polulla hallitulla koneella.
- [ ] Ennen jakoa: olet kokeillut omassa Windows-versiossasi Muistion lainausmerkkitavan ja raahaustavan (alla).
- [ ] 1 viikko ennen: oppija saa osion 00 ja kuvauspaketin. Hän tekee osion viimeistään 3 arkipäivää ennen.
- [ ] Osion 00 jälkeen, viimeistään 2 arkipäivää ennen: savutesti oppijan koneella oppijan tunnuksella.
- [ ] Edellinen päivä: tilaus voimassa, käyttörajat tiedossa, kuvauspaketti ja mahdollinen `03-kenttakartoitus.csv` toimitettu, varakone valmiina.

**IT-pyynnön sisältö.** Node.js (LTS), Git for Windows ja oppijan polun agenttisovellus. Oikeus luoda kansio `C:\dev`. Välityspalvelimessa sallitaan npm-rekisteri sekä Electronin ja Playwrightin lataukset. Kysy samalla, estääkö PowerShellin suoritusasetus npm-komennot ja saako projektikansiossa ajaa kaksoisnapsautettavia .cmd-tiedostoja. Oppija ei muuta suoritusasetusta itse. Jos npm-komennot estyvät, agentti voi käyttää muuta käynnistystapaa tai IT ratkaisee asian. Electronin paketointi asennettavaksi ja koodin allekirjoitus eivät kuulu työpajaan. Sovellus ajetaan kehitystilassa.

**Testi-Wilma-pyyntö (osa P10:tä).** Pyydä Wilma-pääkäyttäjältä ympäristön osoite, testirooli ja vain kuvitteellisia testiopiskelijoita. Pyydä kirjallinen vahvistus siitä, ettei ympäristössä ole oikeita opiskelijatietoja. Testi-Wilmaa käytetään työpajassa vain kenttien lukukokeiluun osiossa 08. Siihen ei kirjoiteta. Käytön ehdot, joiden kaikkien pitää täyttyä:

- Ympäristö on vahvistetusti testikäytössä, eikä siinä ole oikeita tietoja.
- Käytössä on testirooli.
- Kirjautuminen toimi savutestissä.
- Oppija kirjautuu itse.
- Agentti ei avaa testi-Wilmaa itse.
- Kenttäluku tallentaa vain rakenteen, ja oppija tarkistaa tulosteen ennen agenttia.
- HAR-tallenteita tai koko sivun lähdekoodia ei tallenneta (KP liite A).

Jos testi-Wilmaa ei saada, päärunko ei muutu. Koko työpaja tehdään simuloidussa Wilmassa, ja testi-Wilma siirtyy jatkoon.

## Ohjaus askel askeleelta

**Harjoitusajo (2 viikkoa ennen).** Aja osiot 01–08 itse oppijan polulla hallitulla koneella materiaalin kehotepohjilla. Tallenna välitila osioiden 03–07 lopusta. Välitila on projektikansio ilman oppijan omia tiedostoja (päätösloki, hyväksymiskriteerit, testit, oma kokemus). Kirjaa todelliset kestot ja korjaa aikataulua. Mittaa osio 02 erikseen tehtävittäin. Se on päivän 1 tiukin osio, ja aloittelija on sinua hitaampi. Jos osio ei mahdu, siirrä substanssikatselmoinnista lisää kysymyksiä osion 03 alkuun. Välitiloja tarvitaan, jos oppijan projekti rikkoutuu yli 15 minuutiksi.

**Osion jakaminen.** Jaa materiaali muotoiltuna, esimerkiksi verkkosivuna tai oppimisalustalla, ei .md-tiedostoina. Jos oppija lukee materiaalia Muistiossa, kehotelohkojen reunamerkit kopioituvat agentille. Toimita kuvauspaketti tekstinä tai Markdownina, ei pelkkänä Word-tiedostona. Oppija saa lukea ensimmäisen pääosan myös Word-versiosta. Liitä mukaan `03-kenttakartoitus.csv`, jos se on olemassa. Kerro oppijalle, kumman polun kansiota hän lukee. Hän lukee vain sitä.

**Muistio ja .md ennen jakoa.** Oppija tallentaa .md-tiedoston kirjoittamalla nimen lainausmerkkeihin, esimerkiksi "oma-kokemus.md". Hän avaa .md-tiedoston raahaamalla sen Muistion ikkunaan. Myöhemmät osiot viittaavat tähän tapaan. Kokeile molempia omassa Windows-versiossasi, ennen kuin materiaali lähtee oppijalle. Tarkista samalla, näkyykö pääte Muistion otsikkorivillä tai välilehdellä. Jos jokin toimii toisin, kerro oppijalle oikea tapa jakoviestissä.

**Oppijan tehtävät.** Oppija tekee tehtävät 1–7 itse. Pyydä häntä ilmoittamaan heti, jos tehtävä 4 ei onnistu. Vastaa tehtävän 7 kysymykseen testi-Wilmasta samana päivänä, jos voit.

**Savutesti.** Tee testi osion 00 jälkeen oppijan koneella, oppijan tunnuksella ja oppijan polun agenttisovelluksella. Testi vie 15–30 min. Oppija pitää hiiren. Tartu näppäimistöön vain asennus- ja järjestelmäongelmissa.

Aloita oppijan Valmis, kun -listalla. Tarkista nämä:

- Projektikansio on `C:\dev\oppisopimustayttaja` tai varapaikka, eikä polussa näy OneDrivea.
- `maarittely/oma-kokemus.md` on oikeanniminen. Muistion otsikkorivillä näkyy `.md`, ei `.txt`.
- Tiedosto avautuu Muistioon raahaamalla, ja kaikki kohdat on täytetty ilman tunnistetietoja.
- Node.js- ja Git-versiot on kirjattu.
- Väärännimiset kopiot, kuten `oma-kokemus.md.txt`, on poistettu yhdessä.

Luo sitten tyhjä kansio `C:\dev\savutesti`, valitse se agenttisovelluksessa ja anna tämä kehote:

```text
Tämä on savutesti. Työskentele vain kansiossa C:\dev\savutesti.
Luo pienin mahdollinen Electron-sovellus, joka avaa ikkunan, jossa lukee "Savutesti".
Luo erillinen Playwright-skripti, joka avaa näkyvän selaimen tyhjälle sivulle.
Jos selaimen lataus estyy, käytä koneen Edgeä.
Jos jokin lataus tai asennus estyy, kerro virheilmoitus sellaisenaan ennen kuin kokeilet kiertotietä.
Älä tallenna selaimen istuntoa, evästeitä, tallenteita tai sivujen sisältöä.
Tee kummallekin käynnistystiedosto, jonka avaan kaksoisnapsautuksella. Ikkuna jää auki virheen sattuessa.
```

Oppija käynnistää kummankin itse kaksoisnapsauttamalla käynnistystiedostoa Resurssienhallinnassa. Sama tapa on käytössä osioista 03 ja 04 alkaen (`kaynnista-wilma.cmd`, `kaynnista-sovellus.cmd`). Kirjaa viisi asiaa: aukesivatko käynnistystiedostot kaksoisnapsautuksella, aukesiko ikkuna, aukesiko selain, mitä lupapyyntöjä tai hyväksyntöjä tuli ja kauanko asennus kesti. Kokeile samalla tekstin kopiointia käynnistysikkunasta: maalaa hiirellä, sitten Ctrl+C. Lataukset jäävät koneen välimuistiin, mikä nopeuttaa osiota 04.

Jos testi-Wilma on käytössä, oppija käynnistää selainskriptin itse sen käynnistystiedostolla. Oppija kirjoittaa testi-Wilman osoitteen itse selaimeen ja kirjautuu. Agentti ei saa osoitetta eikä tunnuksia. Kun kirjautuminen on kokeiltu, oppija sulkee selaimen. Jos kirjautuminen ei onnistu (esimerkiksi SSO tai lisätunnistautuminen), kirjaa havainto IT:lle. Kiertoteitä ei etsitä. Poista kansio `C:\dev\savutesti` lopuksi, jotta kirjautuneen istunnon jälkiä ei jää kansioon, jonka agentti näkee. Sama sääntö pätee osiossa 04.

Claude-polulla savutesti tuottaa useita lupapyyntöjä. Käytä tilaisuutta: oppija lukee jokaisen ennen hyväksyntää. Polun riski on lupapyyntöväsymys asennuksissa, ja se alkaa tässä. Codex-polulla asennukset kirjoittavat projektikansion ulkopuolelle (npm-välimuisti, Playwrightin selain). Se vaatii hyväksynnän tai Edgen. Tarkista myös, aukeaako ikkuna hiekkalaatikosta. Jos ei aukea, oppija käynnistää sovelluksen itse käynnistystiedostolla. Kirjaa tämä, koska sama toistuu osiossa 04.

**Gitin nimi ja sähköposti.** Sovi oppijan kanssa, mitä nimeä ja sähköpostia hän käyttää Gitissä osiossa 01. Asetus tehdään projektikohtaisesti. Kaikki pysyy koneella. Tallennuspisteitä ei viedä verkkopalveluun.

**Käyttörajat.** Tarkista tilauksen käyttörajat ennakkoon. Älä lupaa niistä oppijalle mitään.

## Polkujen erot (taulukko Claude | Codex)

| Asia | Claude | Codex |
|---|---|---|
| Tilaus | Pro, Max, Team tai Enterprise | ChatGPT-tilaus, jossa Codex on mukana (esim. Plus, Pro, Business, Edu, Enterprise) |
| Sovellus | Claude-työpöytäsovellus, Code-välilehti | Codex-työpöytäsovellus Windowsille. Pilvitilaa ei käytetä. |
| Sovelluksen asennus | IT-pyynnössä | IT-pyynnössä |
| Kansion valinta | Kansio, jossa agentti työskentelee. Sovellus käyttää nimeä työhakemisto. | Uusi paikallinen projekti (Local), kansio valitaan tai luodaan |
| OneDrive-riski | Oppija voi itse valita väärän kansion | Uusi paikallinen projekti voi oletuksena mennä Tiedostot-kansioon, joka voi olla OneDrivessa |
| Käynnistystesti | Oppija lukee lupapyynnön ennen komentoa ja hyväksyy vain tämän kerran. Resurssienhallinta: kansioon ei tullut mitään. | Oppija kieltää verkkoyhteyden ja lukee ajetut komennot. Resurssienhallinta: kansioon ei tullut mitään. |
| Muistilistan polkukohta | Älä salli kaikkea automaattisesti | Älä valitse täysiä oikeuksia |
| Savutestin riski | Lupapyyntöväsymys asennuksissa | Asennukset projektikansion ulkopuolelle, ikkunan avaaminen hiekkalaatikosta |

## Väärinkäsitykset (vähintään 3)

**Väärinkäsitys 1:** "Työpajan lopussa ohjelma on käyttövalmis." Työpajan lopussa on työpajaversio. Se toimii simuloitua Wilmaa vasten kuvitteellisella aineistolla. Ennen käyttöä tarvitaan oikea vaihe 0, testi-Wilma, salaus ja säilytys, asennuspaketti ja pilotti (KP osat 25–26). Sano tämä ääneen jo ennakkoon, ettei oppija pety päivän 2 lopussa.

**Väärinkäsitys 2:** "Testi-Wilmaan saa antaa agentille tunnukset, koska siellä ei ole oikeita tietoja." Tunnukset antavat pääsyn käyttäjänä. Agentti voi käyttää niitä tavalla, jota kukaan ei tarkistanut. Turvaraja on sama kaikissa ympäristöissä: oppija kirjautuu itse, eikä agentti saa tunnuksia.

**Väärinkäsitys 3:** "Projektikansio voi olla Tiedostoissa." Tiedostot-kansio on hallituilla koneilla usein OneDriven synkronoima. Tiedostot kopioituvat pilveen, ja synkronointi voi lukita tiedostoja asennusten aikana. Codex-polulla tämä on sovelluksen tunnettu oletus.

## Jumikohdat ja purku (taulukko: oire | todennäköinen syy | purku)

| Oire | Todennäköinen syy | Purku |
|---|---|---|
| Kansion polussa näkyy OneDrive | Kansio luotiin Tiedostoihin tai Työpöydälle, tai Codexin oletus hyväksyttiin | Luo kansio `C:\dev`:n alle ja valitse se agenttisovelluksessa. Kopioi `maarittely` uuteen kansioon. |
| Sovellus ilmoittaa tilauksesta | Lisenssi ei ole aktivoitunut, tai oppija kirjautui eri tunnuksella | Tarkista tunnus ja lisenssi. Varalla toinen tunnus organisaation lisenssiehtojen mukaan. |
| Agentti ei löydä Node.js:ää tai Gitiä | IT-asennus puuttuu, tai sovellus avattiin ennen asennusta | Käynnistä agenttisovellus uudelleen. Jos ei auta, IT asentaa tai otetaan varakone. |
| Savutestin lataus katkeaa | Välityspalvelin estää npm-rekisterin tai Electronin ja Playwrightin lataukset | Kirjaa virheilmoitus IT:lle. Playwright käyttää koneen Edgeä. |
| Tiedoston nimi on `oma-kokemus.md.txt` | Nimi kirjoitettiin ilman lainausmerkkejä, ja Muistio lisäsi päätteen | Avaa tiedosto raahaamalla ja tallenna uudelleen nimellä lainausmerkeissä. Poista vääränniminen tiedosto yhdessä. |
| `.md`-tiedosto ei näy Muistion avausikkunassa, tai kaksoisnapsautus avaa muun ohjelman | Avausikkuna näyttää oletuksena vain .txt-tiedostot | Avaa Muistio ja raahaa tiedosto sen ikkunaan (osion 00 tapa). |
| `oma-kokemus.md`:ssä on nimiä tai yritysten nimiä | Oppija kirjoitti tapauksen sellaisenaan | Poistakaa ne yhdessä ja kirjoittakaa yleisellä tasolla. Kertaa muistilista. |

## Varasuunnitelma

Jos agenttisovellus tai tilaus ei toimi, vaihda toiseen polkuun, jos se toimii. Polut tuottavat saman tuotteen. Oppija aloittaa toisen polun osiosta 00.

Jos Node.js tai Git ei asennu hallitulle koneelle, käytä varakonetta, jolla sama polku on asennettu. Viimeinen vaihtoehto on, että oppija ohjaa agenttia vetäjän koneella. Ohjaus, tarkistus ja päätökset säilyvät.

Jos Electron ei asennu tai käynnisty, mutta Node.js toimii, sovelluksen käyttöliittymä ajetaan selaimessa ja Playwright erillisenä prosessina. Tämä muuttaa vaiheen 1 teknologiavalintaa (KP osa 13). Oppija kirjaa sen päätöslokiin osiossa 04. Työpöytäkuori jää jatkoon.

Jos Playwrightin selainlataus on estetty, Playwright käyttää koneen Edgeä. Jos käyttöraja tulee vastaan, käytä toista tunnusta lisenssiehtojen mukaan tai varakonetta.

## Tarkista ennen seuraavaa osiota

- [ ] Projektikansio on `C:\dev\oppisopimustayttaja` tai varapaikka, eikä se ole OneDrivessa.
- [ ] `maarittely/` sisältää kuvauspaketin tekstinä ja tiedoston `oma-kokemus.md`.
- [ ] `oma-kokemus.md` on oikeanniminen ja avautuu Muistioon raahaamalla.
- [ ] `oma-kokemus.md`:ssä ovat lause, mitä agentti saa nähdä ja mitä ei koskaan, mitä työpajan lopussa on, lomakkeet, kolme virhettä, kaksi kieltoa, versiot ja testi-Wilman tilanne. Tunnistetietoja ei ole.
- [ ] Oppijan vastaus kohtaan Mitä työpajan lopussa on valmiina ei lupaa koko tuotetta. Jos lupaa, korjaa käsitys savutestissä.
- [ ] Oppija on lukenut KP osat 1–12 ja tietää, että osioiden 01 ja 02 lukutekstit luetaan ennen päivää 1.
- [ ] Savutesti on tehty osion 00 jälkeen: käynnistystiedostot aukesivat kaksoisnapsautuksella, ikkuna ja selain aukesivat, havainnot on kirjattu ja kansio `C:\dev\savutesti` poistettu.
- [ ] Gitin nimi ja sähköposti on sovittu.
- [ ] Testi-Wilman tilanne ja käytön ehdot ovat tiedossa.
- [ ] Harjoitusajon välitilat ovat tallessa.

## Tarkistettavat nimet

- Claude: kansion valinta Code-välilehdellä (työhakemiston valinta).
- Claude: lupapyynnön hyväksymis- ja kieltämispainikkeiden nimet sekä mahdollinen valinta, joka sallii saman jatkossa kysymättä.
- Codex: uuden paikallisen projektin (Local) luonti ja kansion valinta.
- Codex: miten sovellus näyttää agentin ajamat komennot.
- Codex: oletusoikeuksien ja täysien oikeuksien nimet oikeusasetuksessa.
- Codex: verkkoyhteyden hyväksyntäpyynnön muoto.
- Molemmat: rivinvaihto kehotekentässä ja liitetyn lohkon rivinvaihdot.
- Windows: Muistion valikkopolku Tiedosto → Tallenna nimellä, lainausmerkeissä kirjoitettu nimi ja tallennuspaikan valinta.
- Windows: näkyykö tiedostopääte Muistion otsikkorivillä tai välilehdellä.
- Windows: tiedoston raahaus Resurssienhallinnasta Muistion ikkunaan.
- Windows: kaksoisnapsautettava käynnistystiedosto (.cmd) hallitulla koneella: aukeaako ikkuna, näkyykö pääte Resurssienhallinnassa.
- Windows: tekstin kopiointi käynnistysikkunasta oppijan Windows-versiossa.
