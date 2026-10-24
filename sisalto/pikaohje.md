# Pikaohje: Oppisopimustäyttäjä tekoälyn avulla

Tällä ohjeella tehdään Oppisopimustäyttäjä oikeaan käyttöön. Sovellus kokoaa oppisopimusopiskelijan tiedot ja kirjaa ne Wilmaan. Tekoäly kirjoittaa ohjelman. Sinä tunnet kirjaukset, joten sinä päätät, mikä on oikein.

Ohjelmointia ei tarvitse osata. Kaikkea ei tarvitse ymmärtää kerralla. Tee vaihe kerrallaan ja tarkista jokainen itse.

Et tee tätä yksin. Sovi Matin kanssa etukäteen kolme yhteistä aikaa: ensimmäinen istunto (vaiheet 0B–2), vaiheen 3 ensimmäinen käynnistys ja pilotin aloitus. Pysähdy ja kysy Matilta aina, kun tekoäly pyytää kirjoittamaan komennon, muuttamaan Windowsin asetuksia, antamaan salasanan tai käyttämään oikeaa Wilmaa.

Kun testi-Wilma ja IT:n luvat ovat kunnossa, ensimmäinen kirjaus testi-Wilmaan onnistuu päivässä tai kahdessa, ja koko sovellus on pilotissa muutamassa viikossa.

## Sanat, joita tässä käytetään

- **Tekoäly:** Claude tai Codex. Se lukee ja kirjoittaa tiedostoja tietokoneellasi ja tekee ohjelman.
- **Sovellus:** Oppisopimustäyttäjä, jota rakennetaan. Claude- ja Codex-sovellus mainitaan aina nimeltä.
- **Kehote:** pyyntö tekoälylle. Tällä sivulla on valmiit kehotteet.
- **Hakasulkeet [ ]:** kohta, johon kirjoitat oman tietosi ennen lähettämistä. Esimerkiksi [testi-Wilman osoite] vaihdetaan osoitteeseen, jonka sait pääkäyttäjältä. Poista myös hakasulkeet.
- **Tallennuspiste:** välitallennus koko työstä. Jos jokin menee rikki, palataan edelliseen tallennuspisteeseen.
- **Testi-Wilma:** Wilman harjoitusympäristö, jossa on vain keksittyjä opiskelijoita. Kaikki kokeillaan siellä ennen oikeaa Wilmaa.

Kehotteen käyttö: paina Kopioi, liitä teksti tekoälyn viestikenttään (Ctrl+V), täydennä hakasulkeet ja lähetä. Kehotteissa on teknisiä sanoja. Ne on kirjoitettu tekoälylle, eikä sinun tarvitse ymmärtää niitä. Kopioi kehotteet aina tältä sivulta, älä kirjoita niitä käsin.

## Kolme sääntöä

1. Älä anna tekoälylle oikeiden opiskelijoiden tietoja. Älä liitä niitä viestiin äläkä liitä tekoälylle kuvakaappauksia oikeasta Wilmasta. Älä tallenna oikeiden opiskelijoiden listoja, haastatteluja tai esitietoja työkansioon.
2. Älä anna tekoälylle salasanoja tai tunnuksia. Kirjaudut Wilmaan itse vain siihen selaimeen, jonka apuohjelma tai Oppisopimustäyttäjä avaa. Jos tekoäly pyytää sinua kirjautumaan Wilmaan Clauden tai Codexin omassa ikkunassa, älä tee sitä. Claude- tai Codex-sovellukseen kirjaudut omalla tililläsi, ja se on sallittua.
3. Wilmaan ei tallenneta mitään ilman hyväksyntääsi. Jokainen tallennus tarkistetaan avaamalla lomake uudelleen.

## Työtapa

[[kuva:tyokierros|Sama kierros toistuu joka vaiheessa. Valkoiset tekee sinä, violetit tekoäly. Tumma laatikko näyttää, missä kohdassa kierrosta ollaan.]]

Jokainen vaihe menee samalla tavalla. Annat kehotteen, ja tekoäly kertoo ensin, mitä aikoo tehdä. Luet sen ja hyväksyt tai pyydät muutosta. Tekoäly rakentaa, ja sinä kokeilet itse. Jos jokin ei toimi, pyydät korjauksen. Kun toimii, teet tallennuspisteen.

Tekoäly sanoo usein "valmis", vaikka kaikki ei vielä toimi. Valmis on se, minkä näet itse ruudulla.

**Lupakyselyt.** Tekoäly kysyy luvan ennen kuin se muuttaa tiedostoja tai asentaa jotain. Kyselyitä tulee paljon, ja ne ovat teknisiä. Hyväksy, kun pyyntö koskee kansiota `C:\dev\oppisopimustayttaja` tai asennusta, josta tekoäly kertoi suunnitelmassaan. Kiellä ja kysy Matilta, jos pyyntö koskee muita kansioita, Windowsin asetuksia, järjestelmänvalvojan oikeuksia, salasanoja tai oikeaa Wilmaa. Vaihtoehto, joka sallii saman pyynnön jatkossa tässä kansiossa, on sallittu. Älä valitse vaihtoehtoa, joka sallii kaikki muutokset kysymättä.

| | Claude | Codex |
|---|---|---|
| Sovellus | Claude-työpöytäsovellus, Code | Codex-työpöytäsovellus. Ei ChatGPT:tä selaimessa. |
| Kansio | Valitse `C:\dev\oppisopimustayttaja` | Valitse kansio itse. Älä hyväksy ehdotettua kansiota. |
| Ennen muutosta | Tekoäly kysyy luvan. Toimi lupakyselyjen ohjeen mukaan. | Tekoäly muokkaa kansiota kysymättä. Kokeile tulos itse. Älä vaihda oikeuksia täysiin oikeuksiin. |
| Tallennuspiste | Kehotteella | Kehotteella, ei sovelluksen Git-painikkeilla |

## Vaiheet

### 0. Pyydä tiedot ja luvat (aloita viikkoja ennen)

[[kuva:valmistelu|Ennen aloitusta pyydetään tiedot ja luvat. Ilman niitä työtä ei voi aloittaa.]]

Pyydä vastaukset kirjallisena. Tarvitset niitä myöhemmin kehotteissa.

- **Wilma-pääkäyttäjä:** testi-Wilma ja testitunnus hallinnon roolilla. Varmista, että testi-Wilmassa on vain keksittyjä opiskelijoita, eikä se ole kopio oikeista tiedoista. Pyydä sinne keksityt oppisopimusopiskelijat: yksi tavallinen, yksi jolla on yksi tutkinnon osa HOPSissa (lomakkeiden kartoitukseen), yksi jonka HOPS on tyhjä (vaiheen 7 kokeiluun) ja kaksi samannimistä. Pyydä myös oikeus lisätä testi-Wilmaan työpaikka ja työpaikkaohjaaja.
- **Wilma-pääkäyttäjä:** varmista, että testitunnuksella voi avata ja tallentaa nämä lomakkeet: urasuunnitelma, HOPS, näyttösuunnitelma, oppisopimus, työpaikka ja työpaikkaohjaaja. Kirjoita muistiin, mistä valikosta kukin avataan.
- **Koulutuksen vastuuhenkilö:** valitse yksi koulutus, jolla aloitetaan. Pyydä sen näyttösuunnitelman vakiotiedot sähköpostilla tekstinä, ei kuvana.
- **IT:** missä esitietolomakkeen vastaukset ovat, ja voiko ne hakea ohjelmalla. Pyydä myös tapa tehdä keksitylle opiskelijalle esitietovastaus ja haastattelu. Yhdessä työaika on eri (37,5 h ja 30 h), toisessa palkasta puuttuu yksikkö. Jos IT kysyy teknisiä lisätietoja, ohjaa kysymys Matille.
- **Primus-pääkäyttäjä:** miten Primuksen tiedot luetaan. Sovellus tarvitsee opiskelijan ja opiskelijanumeron, opiskeluoikeuden ja koulutuksen, HOPS-valinnat sekä työpaikan ja ohjaajan.
- **IT:** asennukset ja luvat. Alla on sähköposti IT:lle, ei kehote tekoälylle. Poista siitä Claude tai Codex sen mukaan, kumpi teillä on. Matti tarkistaa viestin ennen lähettämistä.

```text
Tarvitsen työkoneelleni oppisopimuskirjausten apuohjelman tekemiseen nämä: Claude- tai Codex-työpöytäsovellus, Node.js (LTS) ja Git for Windows. Ohjelmat lataavat ohjelmapaketteja internetistä (npm), ja selainautomaatio käyttää koneen Edge-selainta. Codex käyttää PowerShelliä, joten npm:n pitää toimia siinä. Tarvitsen myös luvan ajaa kansiossa C:\dev\oppisopimustayttaja olevia käynnistystiedostoja (.cmd) ja myöhemmin asentaa valmiin sovelluksen. Lisätietoja antaa Matti Seise.
```

Tilauksen hankkii esihenkilösi tai IT. Älä ota tilausta omalla maksukortilla. Käytä sitä tekoälyä, jonka organisaatio on hankkinut.

Jos testi-Wilmaa ei saada tai se on kopio oikeista tiedoista, älä jatka vaiheeseen 3. Sovi Matin kanssa, miten edetään.

### 0B. Valmistele kone (20 min, Matin kanssa)

Aloita tästä, kun IT on asentanut ohjelmat.

**Työkansio.** Avaa Resurssienhallinta. Valitse vasemmalta Tämä tietokone ja sitten Paikallinen levy (C:). Tee uusi kansio nimeltä `dev`. Avaa se ja tee sen sisään kansio `oppisopimustayttaja` ilman ä-kirjaimia. Tee sen sisään vielä kansio `maarittely`. Jos Windows pyytää järjestelmänvalvojan oikeuksia, pysähdy ja pyydä IT:tä tekemään kansio.

**Kuvauspaketti tekstinä.** Avaa kuvauspaketti Wordissa. Valitse Tiedosto, Tallenna nimellä ja kansio `maarittely`. Valitse tiedostomuodoksi Pelkkä teksti. Word varoittaa, että muotoilut katoavat. Se on tässä oikein, joten jatka. Kun Word kysyy merkistöä, valitse Muu koodaus ja Unicode (UTF-8).

**Aloitus.** Avaa Claude-sovellus ja valitse Code, tai avaa Codex-sovellus. Valitse kansioksi `C:\dev\oppisopimustayttaja`. Pidä tämä ohje auki selaimessa vieressä. Jos Claude tai Codex kysyy jotain, mitä et ymmärrä, kysy Matilta.

### 1. Kuvaus ja työlista (30 min)

[[kuva:maarittely|Tekoäly lukee kuvauspaketin ja tekee siitä ohjeen itselleen ja työlistan.]]

Ensin tekoäly lukee, mitä ollaan tekemässä. Siitä syntyy kaksi tiedostoa: ohje, jonka tekoäly lukee aina työn alussa, ja työlista, jossa työ on pilkottu pieniksi paloiksi.

```text
Lue kansion maarittely kuvauspaketti kokonaan. Kuvauspaketissa mainittuja liitteitä ei ole. Lomakkeiden kentät selvitetään myöhemmin testi-Wilmasta. Älä vielä kirjoita koodia.
Tee projektille ohjetiedosto, jonka luet aina työn alussa. Kirjaa siihen:
- mitä Oppisopimustäyttäjä tekee, lyhyesti
- säännöt: et käsittele oikeita henkilötietoja, et pyydä salasanoja, käyttäjä kirjautuu itse, puuttuvaa tietoa ei arvata, Wilmaan ei tallenneta mitään ilman käyttäjän hyväksyntää, jokainen tallennus tarkistetaan lukemalla lomake uudelleen, paikalliset henkilötiedot salataan ja lokeihin ei kirjoiteta henkilötietoja
- tekniikka: Windows, Electron, TypeScript ja Playwright näkyvällä selaimella. Playwright käyttää koneen Edge-selainta (channel msedge), ettei erillistä selainta ladata. Wilman osoite ja lomakkeiden kenttäkartat ovat asetustiedostoissa, eivät koodissa.
- ulkoasu: PRO-ilme, tumma #1A0530, painike #9D7DFF, korostus #775EC4, tausta #F5F3F8. Tilat näytetään sanoina, ei pelkkinä väreinä.
- käyttäjä ei ole tekninen. Selitä asiat tavallisella kielellä ja kerro aina, miten hän kokeilee tuloksen.
- käyttäjä ei käytä komentoriviä eikä terminaalia. Kaikki, mitä hänen pitää käynnistää, tehdään kaksoisnapsautettavaksi .cmd-tiedostoksi. Kerro aina tiedoston nimi ja kansio.
- kun pala on valmis ja käyttäjä on kokeillut sen, merkitse se TYOLISTA.md:hen valmiiksi ennen tallennuspistettä.
Tee lisäksi TYOLISTA.md. Pilko työ pieniin paloihin tässä järjestyksessä: lomakkeiden kenttäkartta, ensimmäinen tallennus testi-Wilmaan, tietolähteet, työpaikka ja ohjaaja, oppisopimus, HOPS ja näyttösuunnitelmat, opiskelijajono, häiriötilanteet, asennuspaketti. Jos kuvauspaketissa on asioita, joita tässä järjestyksessä ei ole, kirjaa ne työlistan loppuun kohtaan Myöhemmin.
Näytä lopuksi tiivistelmä ja kerro, mikä kuvauspaketissa jäi epäselväksi.
```

Lue tiivistelmä. Jos jokin sääntö ei vastaa sitä, miten kirjaukset oikeasti tehdään, kerro se tekoälylle omin sanoin.

Tekoäly listaa myös epäselviä kohtia. Vastaa niihin, jotka koskevat kirjaamista. Jos kohta on tekninen tai kuuluu IT:lle, kirjoita: "Kirjaa tämä TYOLISTA.md:hen avoimeksi kysymykseksi. Palataan siihen myöhemmin." Näytä lista ja Myöhemmin-kohta Matille. Matti päättää, mitkä niistä tehdään ennen pilottia.

### 2. Ensimmäinen tallennuspiste (5 min)

[[kuva:tallennuspiste|Kun jokin menee pieleen, palaat edelliseen tallennuspisteeseen.]]

Täydennä ennen lähettämistä: oma nimesi ja työsähköpostisi.

```text
Ota Git käyttöön tässä kansiossa ja tee tallennuspiste viestillä "1: Kuvaus ja työlista". Jos tarvitset nimen ja sähköpostin, käytä vain tässä kansiossa nimeä [oma nimesi] ja osoitetta [työsähköpostisi]. Älä muuta koneen muita asetuksia.
```

Tee tallennuspiste aina, kun jokin toimii. Käytä tätä kehotetta ja kirjoita viestiin vaiheen numero ja se, mikä nyt toimii:

```text
Tee tallennuspiste viestillä "[vaiheen numero]: [mikä nyt toimii]". Näytä lopuksi kaikki tallennuspisteet listana.
```

### 3. Lomakkeiden kentät (2–4 h, ensimmäisellä kerralla Matin kanssa)

[[kuva:kartoitus|Apuohjelma lukee lomakkeen kenttien nimet. Lomaketta ei tarvitse täyttää, eikä kenttiin kirjoitettuja tietoja tallenneta.]]

Tekoäly ei tiedä, mitä kenttiä teidän Wilman lomakkeissa on. Siksi se tekee pienen apuohjelman, joka lukee kenttien nimet testi-Wilmasta. Kenttiin kirjoitettuja tietoja apuohjelma ei tallenna.

Täydennä ennen lähettämistä: testi-Wilman osoite.

```text
Tee skripti, joka kartoittaa Wilman lomakkeiden kentät.
- Tee käynnistystä varten tiedosto kartoita-lomake.cmd, jonka käynnistän kaksoisnapsauttamalla.
- Skripti avaa näkyvän Edge-selaimen osoitteeseen [testi-Wilman osoite]. Näytä selaimen sivun yläreunassa iso teksti KARTOITUS – TESTI-WILMA. Minä kirjaudun itse ja avaan lomakkeen.
- Mustassa ikkunassa lukee suomeksi, mitä teen seuraavaksi. Kun olen avannut lomakkeen, napsautan mustaa ikkunaa ja painan Enter. Silloin skripti lukee avoinna olevan lomakkeen kentät: näkyvä nimi, tyyppi, pakollisuus, vaihtoehdot ja tunniste.
- Skripti ei tallenna kenttien arvoja, henkilöiden nimiä, opiskelijanumeroita, evästeitä eikä istuntoa. Jos valintalistassa on ihmisten nimiä, älä tallenna vaihtoehtoja, vaan merkitse kenttä henkilövalinnaksi.
- Kunkin lomakkeen kentät tallennetaan omaan tiedostoonsa kansioon kenttakartta.
Lomakkeet: urasuunnitelma, HOPS, näyttösuunnitelma, oppisopimus, työpaikka ja työpaikkaohjaaja.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Odota, että tekoäly kertoo apuohjelman olevan valmis. Sulje oikea Wilma ja oma Edge-selaimesi. Kaksoisnapsauta sitten `kartoita-lomake.cmd` kansiossa `C:\dev\oppisopimustayttaja`. Jos Windows varoittaa tiedostosta tai estää sen, älä ohita varoitusta itse, vaan kysy Matilta.

Aukeaa musta ikkuna ja selain, jonka yläreunassa lukee KARTOITUS – TESTI-WILMA. Kirjaudu vain tähän ikkunaan. Avaa lomake keksitylle testiopiskelijalle uutena, esimerkiksi Ohjaus ja tuki → Urasuunnitelmat → Lisää uusi. Lomaketta ei tarvitse täyttää. Napsauta sitten mustaa ikkunaa ja paina Enter. Älä paina Enteriä Wilman lomakkeessa. Sulje lomake tallentamatta. Tee sama jokaiselle lomakkeelle. Näyttösuunnitelman avaat sille testiopiskelijalle, jolla on tutkinnon osa HOPSissa.

Kun kaikki lomakkeet on käyty, pyydä:

```text
Näytä jokaisen lomakkeen kentät taulukkona: kentän nimi, onko pakollinen ja mitä vaihtoehtoja siinä on. Älä näytä teknisiä tunnisteita.
```

Tarkista, että lista on oikein ja ettei siinä ole nimiä tai opiskelijanumeroita. Jos on, kirjoita: "Kenttäkartassa on henkilötietoja. Poista ne ja korjaa apuohjelma niin, ettei se tallenna niitä." Tee kartoitus sitten uudelleen. Kerro tekoälylle, mitkä kentät ovat käytännössä pakollisia. Kirjoita lopuksi tekoälylle: Tee tallennuspiste viestillä "3: lomakkeiden kentät".

### 4. Ensimmäinen kirjaus testi-Wilmaan (½–1 päivä)

[[kuva:tallennus|Sovellus täyttää lomakkeen testi-Wilmassa, tallentaa sen ja tarkistaa, että tieto meni perille.]]

Tämä on tärkein vaihe. Sovellus täyttää urasuunnitelman ja tallentaa sen. Sitten se avaa lomakkeen uudelleen ja tarkistaa, että tiedot ovat oikein. Pelkkä "Tallennettu"-ilmoitus ei riitä.

```text
Rakenna Oppisopimustäyttäjän ensimmäinen versio:
- Electron-sovellus, jonka käynnistän kaksoisnapsauttamalla tiedostoa kaynnista-sovellus.cmd. Kirjoita mustaan ikkunaan suomeksi, ettei sitä saa sulkea, kun sovellus on käytössä.
- se avaa näkyvän Edge-selaimen testi-Wilmaan, ja minä kirjaudun itse
- se näyttää koko ajan isolla, että ollaan testi-Wilmassa, eikä tallenna mitään, jos osoite ei ole asetustiedoston testi-Wilman osoite
- se hakee opiskelijan opiskelijanumerolla, ei pelkällä nimellä
- tässä versiossa kirjoitan urasuunnitelman tiedot itse sovellukseen. Tietojen haku lisätään myöhemmin.
- se näyttää urasuunnitelmaan tulevat tiedot ja odottaa hyväksyntääni
- hyväksynnän jälkeen se täyttää urasuunnitelman vain kenttäkartan kentillä. Jos kenttää ei löydy, se pysähtyy eikä arvaa.
- se tallentaa, avaa lomakkeen uudelleen ja vertaa tallentuneita tietoja
- jos jokin tieto ei täsmää, se näyttää sen tarkistamattomana
- sovelluksessa on painike Tarkista uudelleen. Se lukee jo tallennetun urasuunnitelman Wilmasta ja vertaa sitä hyväksyttyihin tietoihin.
- se ei tee toista urasuunnitelmaa, jos sama on jo olemassa
Älä tallenna selaimen istuntoa tai evästeitä tiedostoon.
Tee työ paloina ja kerro jokaisen palan jälkeen tavallisella kielellä, miten kokeilen sen.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Kun tekoäly kertoo, että sovellus on valmis, kaksoisnapsauta `kaynnista-sovellus.cmd`. Kuten vaiheessa 3, musta ikkuna jää auki. Älä sulje sitä, kun sovellus on käytössä. Pidä oikea Wilma suljettuna kokeilujen ajan, ja katso osoiteriviltä, että olet testi-Wilmassa, ennen kuin muutat mitään käsin.

Kokeile testi-Wilmassa keksityllä opiskelijalla:

- Urasuunnitelma näkyy testi-Wilmassa samoilla tiedoilla, jotka hyväksyit.
- Kun teet saman uudelleen, toista urasuunnitelmaa ei synny.
- Muuta yhtä kenttää käsin testi-Wilmassa ja paina sovelluksessa Tarkista uudelleen. Sovelluksen pitää näyttää ero.

Kirjoita lopuksi tekoälylle: Tee tallennuspiste viestillä "4: urasuunnitelma tallentuu ja tarkistuu".

### 5. Tiedot esitiedoista, haastattelusta ja Primuksesta (1 päivä)

[[kuva:lahteet|Tiedot kolmesta paikasta tulevat yhteen näkymään. Jos ne ovat ristiriidassa, valitset itse.]]

Sovellus hakee opiskelijan tiedot itse, ettei niitä tarvitse kirjoittaa uudelleen. Jos tiedot eroavat toisistaan, sovellus ei valitse puolestasi.

Kokeile vain keksityn opiskelijan tiedoilla. Älä anna tekoälylle kansiota tai tiedostoa, jossa on oikeita haastatteluja tai esitietoja.

Jos IT:n mukaan esitietoja ei voi hakea ohjelmalla, älä keksi tapaa itse. Sovi Matin kanssa varatapa: tiedot luetaan Wilman näkymästä, tai syötät ne sovellukseen itse. Jos tekoäly pyytää avainta, salasanaa tai tunnusta mihin tahansa palveluun, älä anna sitä. Ota yhteys Mattiin.

Täydennä ennen lähettämistä: IT:n ja Primus-pääkäyttäjän kirjalliset vastaukset sekä paikka, johon keksityn opiskelijan haastattelu on tallennettu.

```text
Lisää sovellukseen tietojen haku:
- esitiedot palvelusta [palvelun nimi ja IT:n vastaus siitä, miten tiedot haetaan]
- haastattelu paikasta [mihin keksityn opiskelijan haastattelu on tallennettu testiä varten]
- Primus-tiedot [Primus-pääkäyttäjän vastaus: PrimusQuery tai Wilman näkymät]
Näytä jokaisesta kentästä tieto ja mistä se tuli.
Erota nämä tilanteet: tieto löytyi, kenttä oli tyhjä, kenttää ei näkynyt, haku epäonnistui ja lähteet ovat ristiriidassa.
Ristiriidassa näytä molemmat tiedot ja anna minun valita. Puuttuvaa palkkaa, työaikaa tai ohjaajaa ei arvata.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Kokeile sillä keksityllä opiskelijalla, jonka työaika on eri esitiedoissa ja haastattelussa. Sovelluksen pitää kysyä sinulta. Katkaise sitten verkkoyhteys: laita Wi-Fi pois päältä, ja jos kone on kiinni verkkokaapelissa tai telakassa, irrota se. Paina hakua. Ruudulla pitää näkyä virhe, ei tyhjä kenttä. Kytke yhteys takaisin. Kirjoita tekoälylle: Tee tallennuspiste viestillä "5: tietolähteet".

### 6. Työpaikka, ohjaaja ja oppisopimus (1 päivä)

[[kuva:oppisopimus|Työpaikka ja ohjaaja ensin, oppisopimus vasta niiden jälkeen.]]

Järjestyksellä on väliä. Oppisopimus tarvitsee työpaikan ja ohjaajan, joten ne kirjataan ensin.

```text
Lisää oppisopimuksen kirjaus. Ensin työpaikka ja työpaikkaohjaaja, sitten oppisopimus.
Etsi olemassa oleva työpaikka ja toimipaikka. Jos vaihtoehtoja on useita, kysy minulta. Jos työpaikkaa ei ole, valmistele lisäys ja odota hyväksyntääni.
Työpaikkaohjaaja ja työnantajan edustaja voivat olla eri henkilöitä tai sama henkilö. Älä oleta kumpaakaan. Näytä molemmat erikseen hyväksyttäviksi.
Palkka tallennetaan yksikön kanssa (€/kk tai €/h). Puuttuva yksikkö tai ristiriitainen työaika estää kirjauksen.
Tarkista tallennus lukemalla lomake uudelleen, kuten urasuunnitelmassa.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Kokeile sillä keksityllä opiskelijalla, jonka esitiedoista puuttuu palkan yksikkö. Kirjauksen pitää pysähtyä. Kokeile myös, ettei samaa työpaikkaa tai ohjaajaa synny toista kertaa, kun käsittelet saman opiskelijan uudelleen. Kirjoita tekoälylle: Tee tallennuspiste viestillä "6: oppisopimus".

### 7. HOPS ja näyttösuunnitelmat (1 päivä)

[[kuva:hops|Tutkinnon osa HOPSiin ensin, sitten sille näyttösuunnitelma.]]

Täydennä ennen lähettämistä: vastuuhenkilön vakiotiedot sähköpostista.

```text
Lisää HOPS: valitsen tutkinnon osat itse sovelluksessa opiskelijan koulutuksen osista, ja kullekin valitaan aikataulu Wilman vaihtoehdoista.
Lisää jokaiselle valitulle tutkinnon osalle näyttösuunnitelma: työpaikka, ohjaaja ja nämä vakiotiedot: [koulutuksen vastuuhenkilön vakiotiedot].
Arvosanoja tai arviointeja ei tehdä.
Tutkinnon osan pitää olla HOPSissa ennen sen näyttösuunnitelmaa.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Kokeile sillä testiopiskelijalla, jonka HOPS on tyhjä. Valitse kaksi tutkinnon osaa. Tarkista testi-Wilmasta, että molemmat osat ovat HOPSissa oikealla aikataululla ja kummallakin on oma näyttösuunnitelma. Arvosanoja ei saa tulla. Kun teet saman uudelleen, osia ei saa tulla kahdesti. Kirjoita tekoälylle: Tee tallennuspiste viestillä "7: HOPS ja näyttösuunnitelmat".

### 8. Opiskelijalista ja jono (1 päivä)

[[kuva:jono|Yksi opiskelija kerrallaan. Seuraava aukeaa vasta, kun edellinen on tarkistettu.]]

Kun yksi opiskelija toimii, sovellukselle annetaan lista. Se käsittelee opiskelijat yksi kerrallaan, ja sinä tarkistat jokaisen ennen tallennusta.

```text
Lisää opiskelijalistan tuonti CSV:stä, Excelistä ja liitetystä nimilistasta. Näytä esikatselu ennen tuontia. Säilytä opiskelijanumeroiden etunollat.
Listasta tulee jono, jossa käsitellään yksi opiskelija kerrallaan.
Jos samannimisiä opiskelijoita tai koulutuksia on useita, kysy minulta.
Opiskelija on VALMIS vasta, kun hänen kaikki kirjauksensa on tallennettu ja tarkistettu. Sen jälkeen seuraava opiskelija aukeaa itsestään.
Opiskelijan voi siirtää odottamaan lisätietoja, kun kirjaan syyn.
Jono säilyy, kun sovellus suljetaan. Alkuperäistä tiedostoa ei muuteta.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Älä anna tekoälylle oikeaa opiskelijalistaa. Tee testilista itse Exceliin testi-Wilman keksityistä opiskelijoista: nimi, opiskelijanumero ja koulutus. Ota mukaan kolme opiskelijaa, joista kahdella on sama nimi. Sovelluksen pitää kysyä, kumpi on oikea. Kirjoita tekoälylle: Tee tallennuspiste viestillä "8: opiskelijajono".

### 9. Lopputestit ja häiriötilanteet (½–1 päivä)

[[kuva:testit|Tekoäly tekee testilistan tavallisella kielellä. Sinä teet testit ja kerrot tulokset.]]

Ennen pilottia kaikki kokeillaan vielä kerran. Tekoäly tekee listan siitä, mitä pitää kokeilla. Sinä teet kokeilut itse.

```text
Lisää häiriötilanteiden käsittely: yhteys katkeaa tallennuksen aikana, Wilman istunto vanhenee, sovellus suljetaan kesken. Jos ei ole varmaa, tallentuiko tieto, jono pysähtyy ja sovellus tarkistaa Wilman tilanteen ennen uutta yritystä. Kerro jokaisesta häiriötestistä, miten saan häiriön aikaan ilman teknisiä työkaluja. Jos ajoitus on vaikea, lisää sovellukseen testitila, jossa ennen tallennusta on tauko. Testitila toimii vain testi-Wilmassa, eikä se ole käytössä asennuspaketissa.
Tee TESTIT.md kuvauspaketin hyväksymistesteistä. Ota mukaan vain testit, jotka koskevat sitä, mitä on rakennettu. Listaa erikseen testit, joita ei voi vielä tehdä, ja kerro lyhyesti miksi. Kirjoita jokainen testi tavallisella kielellä, ilman testikoodeja ja teknisiä sanoja: mitä teen ja mitä pitää tapahtua.
Näytä testit minulle numeroituna listana. Kun kerron tuloksen, merkitse se TESTIT.md:hen.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Tee testit testi-Wilmassa. Kerro tulokset tekoälylle yksi kerrallaan, esimerkiksi "Testi 3 ei toiminut. Tein näin, ja tapahtui näin." Tekoäly merkitsee ne listaan. Kirjoita lopuksi tekoälylle: Tee tallennuspiste viestillä "9: testit tehty".

### 10. Asennus ja pilotti

[[kuva:pilotti|Asennuspaketti, pilotti muutamalla opiskelijalla ja korjaukset ennen laajempaa käyttöä.]]

```text
Tee sovellukseen asetus, jolla valitaan testi-Wilma tai oikea Wilma. Jätä oikean Wilman osoite asetuksiin tyhjäksi. Se lisätään pilotin alussa. Näytä valittu ympäristö koko ajan isolla (TESTI-WILMA tai OIKEA WILMA). Oikeassa Wilmassa sovellus kysyy vahvistuksen ennen jokaista tallennusta.
Tee sovelluksesta Windows-asennuspaketti ja käyttöohje KAYTTOOHJE.md tavallisella kielellä. Varmista, ettei testitila ole asennuspaketissa käytössä.
Kirjaa ASENNUS-IT.md:hen, mitä IT:n pitää tarkistaa: mitä asennetaan, mihin sovellus tallentaa tietoa, miten tieto on suojattu ja miten sovellus poistetaan.
Kerro lopuksi, missä asennuspaketti on.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Jaa asennuspaketti IT:lle OneDrive- tai Teams-linkkinä yhdessä ASENNUS-IT.md:n kanssa. Kysy esihenkilöltä, tarvitaanko pilottiin tietosuojavastaavan hyväksyntä. Pyydä Wilma-pääkäyttäjää vahvistamaan, että oikean Wilman lomakkeet ovat samat kuin testi-Wilmassa.

Pilotti aloitetaan Matin kanssa. Vaihdatte ympäristön oikeaan Wilmaan ja kokeilette sovellusta 3–5 oikealla opiskelijalla. Tarkista jokainen kirjaus Wilmasta. Käytä pilotissa IT:n asentamaa sovellusta, älä `kaynnista-sovellus.cmd`:tä. Sulje Claude- tai Codex-sovellus, kun käsittelet oikeita opiskelijoita.

Pilotissa sovellus käsittelee oikeita tietoja omalla koneellasi, mutta tekoäly ei näe niitä. Kun kerrot tekoälylle virheestä, älä kopioi opiskelijan tietoja. Kuvaa virhe ja toista se testi-Wilmassa keksityllä opiskelijalla.

## Jos jäät jumiin

Kopioi virheilmoitus tekoälylle sellaisenaan. Poista siitä ensin opiskelijan tiedot, jos niitä on. Jos virhettä ei voi kopioida, kirjoita se itse tai ota kuvakaappaus vain testi-Wilmasta.

```text
Tein näin: [mitä tein]. Sain tämän virheen: [virheilmoitus]. Odotin: [mitä odotin]. Selvitä syy ja kerro ennen korjausta, mitä muutat.
```

Jos kaksi korjausyritystä ei auta, palaa edelliseen tallennuspisteeseen:

```text
Lopeta korjaaminen. Kerro kolmella lauseella, mitä yritit. Näytä tallennuspisteet listana. Haluan palata viimeisimpään, jossa kaikki toimi. Kerro ensin, mitä katoaa, ja odota vahvistustani.
```

Kun aloitat uuden päivän, aloita uusi keskustelu samassa työkansiossa ja lähetä tämä:

```text
Lue ohjetiedosto ja TYOLISTA.md. Kerro tavallisella kielellä, mikä on valmista ja mitä tehdään seuraavaksi. Älä muuta mitään.
```

Jos tekoäly tekee jotain, mitä et pyytänyt, pysäytä se Clauden tai Codexin pysäytyspainikkeella ja kerro, mitä halusit.

Jos Claude tai Codex ilmoittaa, että käyttöraja on täynnä, työ ei katoa. Jatka samasta keskustelusta ilmoitettuna aikana.

Jos tekoälyn vastaus on liian tekninen, pyydä: "Selitä tämä niin, että ymmärrän ilman teknistä taustaa."
