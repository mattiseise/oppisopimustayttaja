# Pikaohje: Oppisopimustäyttäjä tekoälyn avulla

Tällä ohjeella tehdään Oppisopimustäyttäjä oikeaan käyttöön. Sovellus kokoaa oppisopimusopiskelijan tiedot ja kirjaa ne Wilmaan. Tekoäly kirjoittaa ohjelman. Sinä tunnet kirjaukset, joten sinä päätät, mikä on oikein.

Ohjelmointia ei tarvitse osata. Kaikkea ei tarvitse ymmärtää kerralla. Tee vaihe kerrallaan ja tarkista jokainen itse.

Aikataulu riippuu lähinnä siitä, kuinka nopeasti testi-Wilma ja IT:n luvat saadaan. Kun ne ovat kunnossa, ensimmäinen kirjaus testi-Wilmaan onnistuu päivässä tai kahdessa. Koko sovellus pilottiin vie muutaman viikon.

## Sanat, joita tässä käytetään

- **Tekoäly:** Claude tai Codex. Se lukee ja kirjoittaa tiedostoja tietokoneellasi ja tekee ohjelman.
- **Kehote:** pyyntö tekoälylle. Tällä sivulla on valmiit kehotteet. Kopioi ne Kopioi-painikkeella.
- **Tallennuspiste:** välitallennus koko työstä. Jos jokin menee rikki, palataan edelliseen tallennuspisteeseen.
- **Testi-Wilma:** Wilman harjoitusympäristö, jossa on vain keksittyjä opiskelijoita. Kaikki kokeillaan siellä ennen oikeaa Wilmaa.

Kehotteissa on teknisiä sanoja. Ne on kirjoitettu tekoälylle, eikä sinun tarvitse ymmärtää niitä.

## Kolme sääntöä

1. Tekoäly ei näe oikeiden opiskelijoiden tietoja. Ohjelma tehdään ja kokeillaan testi-Wilmassa.
2. Tekoälylle ei anneta salasanoja eikä tunnuksia. Kirjaudut Wilmaan itse.
3. Wilmaan ei tallenneta mitään ilman hyväksyntääsi. Jokainen tallennus tarkistetaan avaamalla lomake uudelleen.

## Työtapa

[[kuva:tyokierros|Sama kierros toistuu joka vaiheessa. Valkoiset tekee sinä, violetit tekoäly.]]

Jokainen vaihe menee samalla tavalla. Annat kehotteen, ja tekoäly kertoo ensin, mitä aikoo tehdä. Luet sen ja hyväksyt tai pyydät muutosta. Tekoäly rakentaa, ja sinä kokeilet itse. Jos jokin ei toimi, pyydät korjauksen. Kun toimii, teet tallennuspisteen.

Tekoäly sanoo usein "valmis", vaikka kaikki ei vielä toimi. Valmis on se, minkä näet itse ruudulla.

| | Claude | Codex |
|---|---|---|
| Aloitus | Avaa Claude-sovellus, valitse Code ja työkansio | Avaa Codex-sovellus ja valitse työkansio |
| Ennen muutosta | Tekoäly kysyy luvan. Lue, mitä se aikoo tehdä. | Tarkista muutokset sovelluksesta, kun tekoäly on valmis. |

## Vaiheet

### 0. Kerää tiedot ennen aloitusta

[[kuva:valmistelu|Ennen aloitusta kerätään viisi asiaa. Ilman niitä ei päästä oikeaan Wilmaan.]]

- Testi-Wilma ja testitunnus hallinnon roolilla. Pyydä Wilma-pääkäyttäjältä.
- Lomakkeet, jotka sovellus täyttää: urasuunnitelma, HOPS, näyttösuunnitelma, oppisopimus, työpaikka ja työpaikkaohjaaja. Näyttösuunnitelman vakiotiedot saat koulutuksen vastuuhenkilöltä.
- Tieto siitä, missä esitietolomakkeen vastaukset ovat ja mihin haastattelu kirjataan. Kysy IT:ltä, voiko vastaukset hakea suoraan ohjelmalla.
- Tapa lukea Primuksen tiedot. Primus-pääkäyttäjä tietää, onko käytössä PrimusQuery vai luetaanko tiedot Wilmasta.
- IT:n lupa ja asennukset: Claude- tai Codex-sovellus, Node.js ja Git. Ne ovat ohjelmia, joita tekoäly tarvitsee. Lisäksi lupa asentaa valmis sovellus omalle koneelle.

Tarvitset myös tilauksen: Claude (Pro, Max, Team tai Enterprise) tai ChatGPT, jossa on Codex. Tee työkansio `C:\dev\oppisopimustayttaja`, ei OneDriveen. Tee sen sisään kansio `maarittely` ja tallenna sinne järjestelmäkuvaus (kuvauspaketti) tekstitiedostona.

### 1. Kuvaus ja työlista (30 min)

[[kuva:maarittely|Tekoäly lukee kuvauspaketin ja tekee siitä ohjeen itselleen ja työlistan.]]

Ensin tekoäly lukee, mitä ollaan tekemässä. Siitä syntyy kaksi tiedostoa: ohje, jonka tekoäly lukee aina työn alussa, ja työlista, jossa työ on pilkottu pieniksi paloiksi.

```text
Lue kansion maarittely kuvauspaketti kokonaan. Älä vielä kirjoita koodia.
Tee projektille ohjetiedosto, jonka luet aina työn alussa. Kirjaa siihen:
- mitä Oppisopimustäyttäjä tekee, lyhyesti
- säännöt: et käsittele oikeita henkilötietoja, et pyydä salasanoja, käyttäjä kirjautuu itse, puuttuvaa tietoa ei arvata, Wilmaan ei tallenneta mitään ilman käyttäjän hyväksyntää, jokainen tallennus tarkistetaan lukemalla lomake uudelleen, paikalliset henkilötiedot salataan ja lokeihin ei kirjoiteta henkilötietoja
- tekniikka: Windows, Electron, TypeScript ja Playwright näkyvällä selaimella. Wilman osoite ja lomakkeiden kenttäkartat ovat asetustiedostoissa, eivät koodissa.
- ulkoasu: PRO-ilme, tumma #1A0530, painike #9D7DFF, korostus #775EC4, tausta #F5F3F8. Tilat näytetään sanoina, ei pelkkinä väreinä.
- käyttäjä ei ole tekninen. Selitä asiat tavallisella kielellä ja kerro aina, miten hän kokeilee tuloksen.
Tee lisäksi TYOLISTA.md. Pilko työ pieniin paloihin tässä järjestyksessä: lomakkeiden kenttäkartta, ensimmäinen tallennus testi-Wilmaan, tietolähteet, työpaikka ja ohjaaja, oppisopimus, HOPS ja näyttösuunnitelmat, opiskelijajono, häiriötilanteet, asennuspaketti.
Näytä lopuksi tiivistelmä ja kerro, mikä kuvauspaketissa jäi epäselväksi.
```

Lue tiivistelmä. Jos jokin sääntö ei vastaa sitä, miten kirjaukset oikeasti tehdään, kerro se tekoälylle omin sanoin.

### 2. Ensimmäinen tallennuspiste (2 min)

[[kuva:tallennuspiste|Kun jokin menee pieleen, palaat edelliseen tallennuspisteeseen.]]

```text
Ota Git käyttöön tässä kansiossa ja tee tallennuspiste viestillä "Kuvaus ja työlista".
```

Tee tallennuspiste aina, kun jokin toimii.

### 3. Lomakkeiden kentät (1–2 h)

[[kuva:kartoitus|Apuohjelma lukee lomakkeen kenttien nimet. Kenttiin kirjoitettuja tietoja se ei tallenna.]]

Tekoäly ei tiedä, mitä kenttiä teidän Wilman lomakkeissa on. Siksi se tekee pienen apuohjelman, joka lukee kenttien nimet testi-Wilmasta. Kenttiin kirjoitettuja tietoja apuohjelma ei tallenna.

```text
Tee skripti, joka kartoittaa Wilman lomakkeiden kentät.
- Skripti avaa näkyvän selaimen osoitteeseen [testi-Wilman osoite]. Minä kirjaudun itse ja avaan lomakkeen.
- Kun painan Enter, skripti lukee avoinna olevan lomakkeen kentät: näkyvä nimi, tyyppi, pakollisuus, vaihtoehdot ja tunniste.
- Skripti ei tallenna kenttien arvoja, henkilöiden nimiä, opiskelijanumeroita, evästeitä eikä istuntoa.
- Tulos menee tiedostoon kenttakartta/[lomakkeen nimi].json.
Lomakkeet: urasuunnitelma, HOPS, näyttösuunnitelma, oppisopimus, työpaikka ja työpaikkaohjaaja.
Kerro minulle tavallisella kielellä, miten käytän skriptiä.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Tee näin jokaiselle lomakkeelle: käynnistä apuohjelma tekoälyn ohjeen mukaan, kirjaudu testi-Wilmaan, avaa lomake ja paina Enter. Pyydä lopuksi tekoälyä näyttämään, mitä kenttiä se löysi. Tarkista, että lista on oikein ja ettei siinä ole nimiä tai opiskelijanumeroita. Kerro tekoälylle, mitkä kentät ovat käytännössä pakollisia.

### 4. Ensimmäinen kirjaus testi-Wilmaan (½–1 päivä)

[[kuva:tallennus|Sovellus täyttää lomakkeen testi-Wilmassa, tallentaa sen ja tarkistaa, että tieto meni perille.]]

Tämä on tärkein vaihe. Sovellus täyttää urasuunnitelman ja tallentaa sen. Sitten se avaa lomakkeen uudelleen ja tarkistaa, että tiedot ovat oikein. Pelkkä "Tallennettu"-ilmoitus ei riitä.

```text
Rakenna Oppisopimustäyttäjän ensimmäinen versio:
- Electron-sovellus, jonka käynnistän kaksoisnapsauttamalla tiedostoa kaynnista-sovellus.cmd
- se avaa näkyvän selaimen testi-Wilmaan, ja minä kirjaudun itse
- se hakee opiskelijan opiskelijanumerolla, ei pelkällä nimellä
- se näyttää urasuunnitelmaan tulevat tiedot ja odottaa hyväksyntääni
- hyväksynnän jälkeen se täyttää urasuunnitelman vain kenttäkartan kentillä. Jos kenttää ei löydy, se pysähtyy eikä arvaa.
- se tallentaa, avaa lomakkeen uudelleen ja vertaa tallentuneita tietoja
- jos jokin tieto ei täsmää, se näyttää sen tarkistamattomana
- se ei tee toista urasuunnitelmaa, jos sama on jo olemassa
Älä tallenna selaimen istuntoa tai evästeitä tiedostoon.
Tee työ paloina ja kerro jokaisen palan jälkeen tavallisella kielellä, miten kokeilen sen.
```

Kokeile testi-Wilmassa keksityllä opiskelijalla:

- Urasuunnitelma näkyy Wilmassa oikeilla tiedoilla.
- Kun teet saman uudelleen, toista urasuunnitelmaa ei synny.
- Kun muutat yhtä kenttää käsin Wilmassa ja sovellus tarkistaa lomakkeen, se huomaa eron.

Tee tallennuspiste.

### 5. Tiedot esitiedoista, haastattelusta ja Primuksesta (1 päivä)

[[kuva:lahteet|Tiedot kolmesta paikasta tulevat yhteen näkymään. Jos ne ovat ristiriidassa, valitset itse.]]

Sovellus hakee opiskelijan tiedot itse, ettei niitä tarvitse kirjoittaa uudelleen. Jos tiedot eroavat toisistaan, sovellus ei valitse puolestasi.

```text
Lisää sovellukseen tietojen haku:
- esitiedot palvelusta [palvelun nimi ja sovittu tapa hakea tiedot]
- haastattelu paikasta [mihin haastattelu kirjataan]
- Primus-tiedot [PrimusQuerystä tai Wilman näkymistä, sen mukaan mitä sovittiin]
Näytä jokaisesta kentästä tieto ja mistä se tuli.
Erota nämä tilanteet: tieto löytyi, kenttä oli tyhjä, kenttää ei näkynyt, haku epäonnistui ja lähteet ovat ristiriidassa.
Ristiriidassa näytä molemmat tiedot ja anna minun valita. Puuttuvaa palkkaa, työaikaa tai ohjaajaa ei arvata.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Kokeile keksityllä opiskelijalla, jonka työaika on haastattelussa eri kuin esitiedoissa. Sovelluksen pitää kysyä sinulta. Katkaise sitten verkkoyhteys kesken haun. Ruudulla pitää näkyä virhe, ei tyhjä kenttä. Tee tallennuspiste.

### 6. Työpaikka, ohjaaja ja oppisopimus (1 päivä)

[[kuva:oppisopimus|Työpaikka ja ohjaaja ensin, oppisopimus vasta niiden jälkeen.]]

Järjestyksellä on väliä. Oppisopimus tarvitsee työpaikan ja ohjaajan, joten ne kirjataan ensin.

```text
Lisää oppisopimuksen kirjaus. Ensin työpaikka ja työpaikkaohjaaja, sitten oppisopimus.
Etsi olemassa oleva työpaikka ja toimipaikka. Jos vaihtoehtoja on useita, kysy minulta. Jos työpaikkaa ei ole, valmistele lisäys ja odota hyväksyntääni.
Työpaikkaohjaaja ja työnantajan edustaja ovat eri henkilöitä.
Palkka tallennetaan yksikön kanssa (€/kk tai €/h). Puuttuva yksikkö tai ristiriitainen työaika estää kirjauksen.
Tarkista tallennus lukemalla lomake uudelleen, kuten urasuunnitelmassa.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Kokeile keksityllä opiskelijalla, jonka palkasta puuttuu yksikkö. Kirjauksen pitää pysähtyä. Tee tallennuspiste.

### 7. HOPS ja näyttösuunnitelmat (1 päivä)

[[kuva:hops|Tutkinnon osa HOPSiin ensin, sitten sille näyttösuunnitelma.]]

```text
Lisää HOPS: valitut tutkinnon osat ja kullekin aikataulu, joka valitaan Wilman vaihtoehdoista.
Lisää jokaiselle valitulle tutkinnon osalle näyttösuunnitelma: työpaikka, ohjaaja ja nämä vakiotiedot: [koulutuksen vastuuhenkilön hyväksymät vakiotiedot].
Arvosanoja tai arviointeja ei tehdä.
Tutkinnon osan pitää olla HOPSissa ennen sen näyttösuunnitelmaa.
Tee ensin suunnitelma ja odota hyväksyntääni.
```

Kokeile opiskelijalla, jolla on kaksi tutkinnon osaa. Tee tallennuspiste.

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

Kokeile kolmen keksityn opiskelijan listalla, jossa kahdella on sama nimi. Sovelluksen pitää kysyä, kumpi on oikea. Tee tallennuspiste.

### 9. Lopputestit ja häiriötilanteet (½–1 päivä)

[[kuva:testit|Tekoäly tekee testilistan tavallisella kielellä. Sinä teet testit ja merkitset tulokset.]]

Ennen pilottia kaikki kokeillaan vielä kerran. Tekoäly tekee listan siitä, mitä pitää kokeilla. Sinä teet kokeilut itse.

```text
Lisää häiriötilanteiden käsittely: yhteys katkeaa tallennuksen aikana, Wilman istunto vanhenee, sovellus suljetaan kesken. Jos ei ole varmaa, tallentuiko tieto, jono pysähtyy ja sovellus tarkistaa Wilman tilanteen ennen uutta yritystä.
Tee TESTIT.md kuvauspaketin hyväksymistesteistä. Kirjoita jokainen testi tavallisella kielellä, ilman testikoodeja ja teknisiä sanoja: mitä teen ja mitä pitää tapahtua. Jätä tulokselle tyhjä ruutu. Minä teen testit.
```

Tee testit testi-Wilmassa ja merkitse tulokset. Jos jokin ei toimi, kerro tekoälylle omin sanoin, mitä teit ja mitä tapahtui.

### 10. Asennus ja pilotti

[[kuva:pilotti|Asennuspaketti, pilotti muutamalla opiskelijalla ja korjaukset ennen laajempaa käyttöä.]]

```text
Tee sovelluksesta Windows-asennuspaketti ja käyttöohje KAYTTOOHJE.md tavallisella kielellä.
Kirjaa ASENNUS-IT.md:hen, mitä IT:n pitää tarkistaa: mitä asennetaan, mihin sovellus tallentaa tietoa, miten tieto on suojattu ja miten sovellus poistetaan.
```

Anna asennuspaketti IT:lle. Kun IT on hyväksynyt sen, kokeile sovellusta 3–5 oikealla opiskelijalla ja tarkista jokainen kirjaus Wilmasta.

Pilotissa sovellus käsittelee oikeita tietoja omalla koneellasi, mutta tekoäly ei näe niitä. Kun kerrot tekoälylle virheestä, älä kopioi opiskelijan tietoja. Kuvaa virhe ja toista se testi-Wilmassa keksityllä opiskelijalla.

## Jos jäät jumiin

Kopioi virheilmoitus tekoälylle sellaisenaan. Poista siitä ensin opiskelijan tiedot, jos niitä on.

```text
Tein näin: [mitä tein]. Sain tämän virheen: [virheilmoitus]. Odotin: [mitä odotin]. Selvitä syy ja kerro ennen korjausta, mitä muutat.
```

Jos kaksi korjausyritystä ei auta, palaa edelliseen tallennuspisteeseen:

```text
Lopeta korjaaminen. Kerro kolmella lauseella, mitä yritit. Haluan palata tallennuspisteeseen [tallennuspisteen viesti]. Kerro ensin, mitä katoaa, ja odota vahvistustani.
```

Kun aloitat uuden päivän:

```text
Lue ohjetiedosto ja TYOLISTA.md. Kerro tavallisella kielellä, mikä on valmista ja mitä tehdään seuraavaksi. Älä muuta mitään.
```

Jos tekoälyn vastaus on liian tekninen, pyydä: "Selitä tämä niin, että ymmärrän ilman teknistä taustaa."
