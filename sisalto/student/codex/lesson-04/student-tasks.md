# Tehtävät: osio 04 – Ensimmäinen varmennettu tallennus

Aika noin 120 min. Tarvitset: Codex-työpöytäsovelluksen, projektikansion, Muistion ja Edgen.

Agentin valmis ei ole testitulos. Tarkistat jokaisen palan itse, ennen kuin hyväksyt sen.

## Tehtävä 1: Uudet kehotepohjat ja tilannekatsaus

1. Aloita Codexissa uusi työsäie samassa projektissa. Vetäjä näyttää, miten.
2. Kopioi alla oleva lohko kehotekenttään. Lähetä.
3. Tarkista Git-toiminnoista, että muuttui vain `KEHOTEPOHJAT.md`.
4. **Kehote (K11):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K11. Täytä aukko: mitä haluat tietää, ennen kuin jatkat. Lähetä.
5. Vertaa vastausta päätöslokiisi. Totea, että agentti tuntee osion 03 tuotokset.
6. Tee tallennuspiste (commit) K6:lla omalla viestilläsi.

```text
Lisää KEHOTEPOHJAT.md:n loppuun alla olevat kuusi pohjaa sellaisinaan. Älä muuta muita tiedostoja.

## K3 Toteuta yksi pala
Toteuta hyväksytty suunnitelma: TYOLISTA.md:n tehtävä [numero].
Noudata AGENTS.md:n sääntöjä.
Kun olet valmis, kerro, miten käynnistän sovelluksen ja mitä minun pitää nähdä, kun [tilanne, jonka haluan tarkistaa].
Älä tee tallennuspistettä.

## K4 Virheilmoitus
Tein näin: [mitä tein].
Sain tämän virheilmoituksen:
[virheilmoitus sellaisenaan]
Odotin: [mitä odotin näkeväni].
Selvitä syy. Kerro ennen korjausta, mitä aiot muuttaa. Älä muuta tiedostoja ennen kuin hyväksyn.

## K5 Korjauta
Testi tai kriteeri: [testin tunnus tai kriteeri].
Havaitsin: [mitä näin].
Korjaa niin, että [mitä pitää tapahtua].
Älä muuta muuta toimintaa. Kerro lopuksi, miten tarkistan korjauksen.

## K9 Sovittimen työjärjestys
Rakennetaan lomake [lomakkeen nimi] simuloituun Wilmaan.
Käytä vain KENTAT.md:n kenttiä. Jos kenttä puuttuu, merkitse se puuttuvaksi. Älä keksi kenttiä.
Etene tässä järjestyksessä ja pysähdy jokaisen kohdan jälkeen:
(1) kenttien haku: jokaiselle kentälle täsmälleen yksi osuma
(2) täyttö
(3) Wilma-tallennus
(4) uudelleenluku ja vertailu hyväksyttyyn sisältöön
(5) kaksoiskappaleen esto
Kiinnitä erityistä huomiota kenttään [kenttä, joka menee käsin kirjatessa helpoimmin väärin].
Kerro jokaisen kohdan jälkeen, miten tarkistan sen itse sovelluksesta.

## K10 Katkaise kehä
Lopeta korjaaminen. Älä muuta tiedostoja.
Halusin saada aikaan: [mitä halusin saada aikaan].
Kerro kolmella lauseella, mitä yritit ja miksi se ei toiminut.
Kerro, mihin tallennuspisteeseen kannattaa palata ja mitä silloin katoaa.

## K11 Tilannekatsaus
Lue AGENTS.md, TYOLISTA.md, PAATOSLOKI.md ja TESTIT.md. Älä muuta mitään.
Kerro, mitkä tehtävät ovat valmiita, mikä on seuraava avoin tehtävä ja mitkä testit ovat tekemättä.
Kerro erityisesti [mitä haluan tietää ennen kuin jatkan].
```

Seuraavaksi: kriteerit ennen rakentamista.

## Tehtävä 2: Kriteerit ja hyväksyttävät arvot

1. Kopioi alla oleva pohja Muistiolla tiedoston `HYVAKSYMISKRITEERIT.md` loppuun.
2. **Oma kriteeri:** Kirjoita vähintään kolme Hyväksyn, kun -kohtaa ensimmäiselle varmennetulle Wilma-tallennukselle.
3. Kirjoita vähintään yksi En hyväksy, jos -kohta.
4. Kirjoita Aino Testisen urasuunnitelmalle arvot. Käytä `KENTAT.md`:n kenttiä ja keksi arvot itse.
5. Kirjoita Tarkistan näin -kohta. Tallenna ja sulje Muistio.
6. Tee tallennuspiste K6:lla.

```text
## Osio 04: ensimmäinen varmennettu tallennus
Hyväksyn, kun:
- [kriteeri]
- [kriteeri]
- [kriteeri]
En hyväksy, jos:
- [kriteeri]
Aino Testisen (000123) urasuunnitelman arvot, jotka hyväksyn:
- [kenttä]: [kuvitteellinen arvo]
- [kenttä]: [kuvitteellinen arvo]
Tarkistan näin:
- [mitä teen ja mitä näen]
Liittyvät testit:
- T05, T13
```

Seuraavaksi: turvaraja ja suunnitelma.

## Tehtävä 3: Turvaraja ja suunnitelma teknisestä kokeilusta

1. Lue Muistiolla tietoturvan muistilista `TYOKORTTI.md`:n osasta 4. Sovellus ei myöskään tallenna istuntoa, evästeitä eikä tallenteita.
2. Tarkista, että alla olevan kehotteen lopussa kielletään muutokset ennen hyväksyntääsi.
3. **Kehote (K2 + K9):** Kopioi koko lohko kehotekenttään. Täytä kolme aukkoa. Lähetä.

```text
Tehtävä: tekninen kokeilu. Sovellus tekee Aino Testisen (000123) urasuunnitelmasta Wilma-tallennuksen simuloituun Wilmaan ja varmentaa sen uudelleenluvulla.
Lue ensin AGENTS.md, TYOLISTA.md ja HYVAKSYMISKRITEERIT.md:n osio 04.
Tärkein kriteerini: [tärkein kriteeri].
Noudata KEHOTEPOHJAT.md:n pohjaa K9 lomakkeelle urasuunnitelma. Kiinnitä erityistä huomiota kenttään [kenttä, joka menee käsin kirjatessa helpoimmin väärin].
Jaa työ viiteen palaan:
(a) sovellus käynnistyy kehitystilassa kaksoisnapsautettavalla tiedostolla kaynnista-sovellus.cmd kuten simuloitu Wilma. Lisää sovelluksen ohje KAYNNISTYS.md:hen samassa muodossa.
(b) sovellus avaa näkyvän selaimen simuloituun Wilmaan, minä kirjaudun, ja sovellus tarkistaa, että ympäristö on SIMULOITU
(c) kohdistus opiskelijanumerolla
(d) K9:n kohdat (1)–(3): arvot näkyvät muokattavina, minä hyväksyn ne, sitten täyttö ja Wilma-tallennus
(e) K9:n kohdat (4)–(5): jokainen kenttä näkyy varmennettuna tai tarkistamattomana. Laajenna palauta-lahtotila.cmd tyhjentämään myös sovelluksen paikallinen työjono ja käsittelyt.
Aino Testisen hyväksyttävät arvot: [arvot kriteeritiedostostasi].
Sovellus ei pyydä salasanaa. Se ei tallenna selaimen istuntoa, evästeitä eikä tallenteita. Se kirjoittaa vain simuloidun Wilman osoitteeseen.
Kerro jokaiselle palalle TYOLISTA.md:n tehtävän numero.
Tee suunnitelma. Kerro, mitkä tiedostot muuttuvat, mitä komentoja ajat ja miten tarkistan tuloksen ilman koodin lukemista.
Älä muuta tiedostoja ennen kuin hyväksyn.
Kun hyväksyn suunnitelman, älä vielä aloita. Annan palat yksi kerrallaan.
```

4. **Oma testi:** Etsi suunnitelmasta vastaus neljään kysymykseen. Onko mukana uudelleenluku? Pyydetäänkö salasanaa? Tallennetaanko istunto? Kirjoittaako sovellus muualle kuin simuloituun Wilmaan? Oikeat vastaukset ovat kyllä, ei, ei ja ei.
5. Korjauta: kirjoita agentille, mikä on väärin. Jos ei mitään, jatka.
6. Kirjoita palojen tehtävänumerot paperille.
7. Hyväksy suunnitelma kirjoittamalla täsmälleen: Hyväksyn suunnitelman. Älä vielä aloita. Annan ensimmäisen palan seuraavaksi.
8. Jos agentti alkaa silti muuttaa tiedostoja, pysäytä se. Jos Git-toiminnoissa näkyy muutoksia, palaa tallennuspisteeseen K7:llä.

Seuraavaksi: palat yksi kerrallaan.

## Tehtävä 4: Rakenna pala kerrallaan

Teet saman kierroksen jokaiselle palalle (a)–(e).

1. **Kehote (K3):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K3. Täytä aukot: palan tehtävänumero ja tilanne, jonka haluat tarkistaa. Lähetä.
2. Lue jokainen lupapyyntö kolmella kysymyksellä. Asennus saa käyttää verkkoa ja kirjoittaa kahteen paikkaan projektikansion ulkopuolelle: asennusten välimuistiin ja Playwrightin selainkansioon. Niihin vastaat kyllä. Kiellä muut kansion ulkopuoliset kirjoitukset ja kutsu vetäjä.
3. Kirjoita odottaessasi päätöslokiin merkinnän alku tai `KENTAT.md`:n kesken jääneet huomiot. Jos agentti ei etene 15 minuuttiin, kutsu vetäjä.
4. Avaa Git-toiminnoista muuttuneet tiedostot. Kysy agentilta jokaisesta, jota et tunnista.
5. Aja sovellus itse `KAYNNISTYS.md`:n ohjeella.
6. **Oma testi:** Tee palan tarkistus alla olevasta listasta.
7. **Päätös:** Jos hylkäät, toimi ensin alla olevan Hylkään-rivin mukaan. Kirjaa päätöslokiin palasta hyväksyn, korjautan tai hylkään ja peruste muodossa Näin: … Siksi: … Tallenna ja sulje Muistio.
8. Tee tallennuspiste K6:lla. Kirjoita viestiin, mikä pala toimii.

Korjautan: K5 ja takaisin askeleeseen 4. Hylkään: sulje Muistio, palaa ensin tallennuspisteeseen K7:llä ja kirjaa päätös sitten. Virheilmoitus: tehtävä 5.

Palojen tarkistukset:

- (a) Kaksoisnapsautat tiedostoa `kaynnista-sovellus.cmd`, ja sovelluksen ikkuna aukeaa.
- (b) Näkyvä selain avautuu simuloituun Wilmaan, ja sivulla lukee SIMULOITU. Valitset testikäyttäjän itse. Salasanaa ei kysytä.
- (c) Kirjoita sovellukseen 000123. Sovellus näyttää Aino Testisen ryhmästä TK26A. Kokeile numeroa 000777. Sovellus kertoo, ettei opiskelijaa löydy, eikä avaa ketään.
- (d) Sovellus näyttää kriteeritiedostosi arvot. Hyväksyt ne. Näet selaimessa, kun lomake täyttyy ja Wilma-tallennus tehdään.
- (e) Sovellus näyttää jokaisen kentän varmennettuna tai tarkistamattomana. Kaikki ovat varmennettuja.

Seuraavaksi: kun palat (a)–(e) toimivat, tehtävä 6. Tehtävä 5 on virhetilanteisiin.

## Tehtävä 5: Kun pala ei toimi

1. Maalaa virheilmoitus hiirellä ja kopioi se Ctrl+C:llä. Älä paina Ctrl+C ennen maalaamista: se voi sulkea ohjelman. Jos kopiointi ei onnistu, kirjoita ensimmäiset rivit K4:ään.
2. **Kehote (K4):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K4. Täytä aukot. Lähetä.
3. Lue agentin selitys. Kirjoita agentille, että se saa tehdä muutoksen, kun ymmärrät, mitä muuttuu.
4. Tarkista Git-toiminnoista, että muuttui vain se, mitä agentti kertoi.
5. Aja sovellus uudelleen `KAYNNISTYS.md`:n ohjeella. Jos pala toimii, jatka tehtävän 4 askeleesta 6. Jos ei ja yritys oli ensimmäinen, tee askeleet 1–5 uudelleen.
6. Jos sama ongelma on jäljellä toisen yrityksen jälkeen, lopeta korjaaminen.
7. **Kehote (K10):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K10. Täytä aukko. Lähetä.
8. Sulje Muistio. Palaa agentin ehdottamaan tallennuspisteeseen K7:llä ja kerro vetäjälle. Kirjaa päätöslokiin hylkään ja peruste vasta paluun jälkeen. Aloita pala tehtävän 4 askeleesta 1.

Seuraavaksi: tehtävä 4 askeleen 5 tai 8 mukaan.

## Tehtävä 6: Käynnistysohje ilman agenttia

1. **Kehote:** Kopioi koko lohko kehotekenttään. Täytä aukko. Lähetä.

```text
Lue KAYNNISTYS.md. Selvennä tätä kohtaa: [kohta, joka oli sinulle epäselvä paloissa a–e].
Varmista, että ohjeessa on simuloidun Wilman osoite, sulkeminen ja palautus lähtötilaan.
Älä muuta muita tiedostoja.
```

2. Tarkista Git-toiminnoista, että muuttui vain `KAYNNISTYS.md`.
3. Sulje sovellus, näkyvä selain ja simuloitu Wilma.
4. Kaksoisnapsauta tiedostoa `palauta-lahtotila.cmd`.
5. **Oma testi:** Käynnistä simuloitu Wilma ja sovellus `KAYNNISTYS.md`:n ohjeella. Älä kysy agentilta mitään.
6. Tee tallennuspiste K6:lla.

Seuraavaksi: testit T05 ja O03.

## Tehtävä 7: Testit T05 ja O03

1. **Oma testi T05:** Tee sovelluksella kirjaus Aino Testiselle (000123). Hyväksy kriteeritiedostosi arvot.
2. Avaa simuloitu Wilma Edgessä `KAYNNISTYS.md`:n osoitteesta ja kirjaudu.
3. Avaa Aino Testisen (000123) urasuunnitelma. Vertaa arvoja kriteeritiedostosi arvoihin kenttä kerrallaan.
4. Avaa Aino Testisen (000456) urasuunnitelmat. Totea, että siellä on vain aiempi urasuunnitelma.
5. Kirjaa Muistiolla `TESTIT.md`:hen T05:lle tulos, havainto ja päivä. Mainitse havainnossa myös 000456 ja palan (c) 000777.
6. **Oma testi O03:** Tee kirjaus Ainolle 000123 uudelleen. Totea Edgessä, että urasuunnitelmia on yhä yksi.
7. Kirjaa O03:lle tulos, havainto ja päivä. Tallenna ja sulje Muistio.

Jos T05 tai O03 ei mene läpi, korjauta K5:llä ja tee uusinta.

Seuraavaksi: testikytkin.

## Tehtävä 8: Testikytkin ja testi T13

1. Seuraa, kun vetäjä näyttää testikytkimen omalla koneellaan.
2. **Kehote:** Kopioi koko lohko kehotekenttään. Täytä aukko: kenttä ja virhe, jonka haluat testata. Lähetä.

```text
Lisää simuloituun Wilmaan testikytkin "tallenna kenttä väärin". Kun kytkin on päällä, simuloitu Wilma tallentaa yhden kentän väärin näin: [mikä kenttä tallentuu väärin ja miten].
Tee kytkimestä valinta simuloidun Wilman sivulle. Kytkin on oletuksena pois päältä, ja palautus lähtötilaan kytkee sen pois.
Muuta vain kansiota simuloitu-wilma ja tarvittaessa lähtötilaa. Älä muuta sovellusta.
```

3. Tarkista Git-toiminnoista, että muuttuivat vain `simuloitu-wilma` ja lähtötila.
4. Sulje sovellus ja simuloitu Wilma. Kaksoisnapsauta tiedostoa `palauta-lahtotila.cmd`.
5. Käynnistä simuloitu Wilma ja sovellus `KAYNNISTYS.md`:n ohjeella.
6. Kytke testikytkin päälle simuloidun Wilman sivulta.
7. **Oma testi T13:** Kirjoita `TESTIT.md`:n T13:n Odotan-rivin perään oma ennusteesi sanalla Ennuste:.
8. Tee sovelluksella urasuunnitelman kirjaus Ville Testaajalle (000999) kuvitteellisilla arvoilla.
9. Vertaa sovelluksen näyttöä ennusteeseesi. Avaa sitten Villen urasuunnitelma Edgessä ja katso, mikä arvo tallentui.
10. Kirjaa T13:lle tulos, havainto ja päivä. Tallenna ja sulje Muistio.
11. Kytke testikytkin pois päältä.
12. **Päätös:** Kirjaa päätöslokiin testikytkimestä ja T13:sta päätös ja peruste. Tee tallennuspiste K6:lla.

Jos väärä kenttä näkyy varmennettuna, T13 ei mene läpi. Korjauta K5:llä.

Seuraavaksi: päivän päätös.

## Tehtävä 9: Päivän päätös

1. Pyydä agenttia merkitsemään valmiiksi ne `TYOLISTA.md`:n tehtävät, joiden testin kirjasit läpi, myös osion 03 tehtävät (O01). Kerro numerot itse.
2. Tarkista Git-toiminnoista, että muuttui vain `TYOLISTA.md`.
3. **Päätös:** Kirjaa päätöslokiin teknisestä kokeilusta hyväksyn, korjautan tai hylkään. Kirjoita perusteeseen T05:n ja T13:n tulokset omin sanoin.
4. Kirjoita päätöslokin loppuun "Huomenna aloitan tästä:" ja yksi lause. Tallenna ja sulje Muistio.
5. Tee tallennuspiste K6:lla. Aloita viesti sanoilla Päivä 1.

Seuraavaksi: tarkistat, että osio on valmis.

## Valmis, kun

- Simuloitu Wilma ja sovellus käynnistyvät kaksoisnapsautuksella `KAYNNISTYS.md`:n ohjeella, ja olet kokeillut sen itse.
- Kirjaudut sovelluksen avaamassa selaimessa itse ilman salasanaa.
- `TESTIT.md`:ssä on tulos T05:lle, O03:lle ja T13:lle.
- `KEHOTEPOHJAT.md`:ssä ovat K3, K4, K5, K9, K10 ja K11.
- Päätöslokissa ovat palojen päätökset, päivän päätös ja huomisen aloituskohta.
- Tallennuspiste Päivä 1 on tehty.

## Jos jäät jumiin

Jos asennus pysähtyy latausvirheeseen, anna virheilmoitus agentille K4:llä ja kutsu vetäjä. Älä muuta koneen asetuksia itse.

Jos selaimen lataus estyy, pyydä agenttia käyttämään koneen Edgeä. Jos komennot estyvät PowerShellissä, pyydä toista tapaa.

Jos agentti pysähtyy kesken palan (d) tai (e), tee sen kertoma tarkistus ja kirjoita: Jatka seuraavaan kohtaan.

Jos sovelluksen ikkuna ei aukea, kun agentti kokeilee sitä, käynnistä sovellus itse `KAYNNISTYS.md`:n ohjeella. Älä valitse täysiä oikeuksia.

Ennen uusintaa sulje sovellus ja simuloitu Wilma ja kaksoisnapsauta `palauta-lahtotila.cmd`. Kirjaa uusinta testin alle `TESTIT.md`:n alun mallilla.

## Seuraava osio

Osio 05 alkaa huomenna kello 9.00 uudella työsäikeellä ja K11:llä. Jos vetäjän katselmointi ja T13 jäivät tänään tekemättä, teet tehtävän 8 huomenna heti K11:n jälkeen.
