# Tehtävät: osio 03 – Simuloitu Wilma ja kuvitteellinen aineisto

Aika noin 75 min. Tarvitset: Claude-työpöytäsovelluksen Code-välilehden, projektikansion, Muistion ja Edgen.

## Tehtävä 1: Tapaukset ja kriteerit ennen rakentamista

1. Viimeistele `TYOLISTA.md` osion 02 ohjeella, jos se jäi kesken.
2. Avaa `HYVAKSYMISKRITEERIT.md` Muistiolla osion 00 tavalla. Kopioi alla oleva pohja tiedoston loppuun.
3. **Oma kriteeri:** Kirjoita omin sanoin vähintään viisi tapausta, jotka aineistossa on oltava. Yksi tulee omasta kokemuksestasi.
4. Kirjoita pohjan muut kohdat. Hyväksyn, kun -kohtiin tulee, mitä näet simuloidussa Wilmassa.
5. Tallenna tiedosto ja sulje Muistio.
6. Tee tallennuspiste (commit) K6:lla.

```text
## Osio 03: simuloitu Wilma ja kuvitteellinen aineisto
Tapaukset, jotka testiaineistossa on oltava:
- [tapaus]
- [tapaus]
- [tapaus]
- [tapaus]
- [tapaus omasta kokemuksestani]
Hyväksyn, kun:
- [kriteeri]
- [kriteeri]
En hyväksy, jos:
- [kriteeri]
Tarkistan näin:
- [mitä teen ja mitä näen]
Liittyvät testit:
- O01, O02
```

Seuraavaksi: simuloitu Wilma.

## Tehtävä 2: Simuloitu Wilma

1. Kytke suunnittelutila päälle.
2. **Kehote (K2):** Kopioi koko lohko kehotekenttään. Täytä aukot: tärkein kriteerisi ja muistamasi urasuunnitelman kentät. Lähetä.

```text
Tehtävä: rakenna kansioon simuloitu-wilma mahdollisimman yksinkertainen simuloitu Wilma. Sillä ei ole yhteyttä oikeaan Wilmaan.
Lue ensin CLAUDE.md, TYOLISTA.md ja HYVAKSYMISKRITEERIT.md:n osio 03.
Tärkein kriteerini: [tärkein kriteeri].
Simuloidussa Wilmassa on:
(1) teksti SIMULOITU jokaisella sivulla sekä ympäristön ja roolin tieto
(2) kirjautuminen ilman salasanaa: testikäyttäjä valitaan listalta
(3) opiskelijahaku nimellä ja opiskelijanumerolla
(4) profiili, jossa Primus-tiedot näkyvät vain luettavina: nimi, opiskelijanumero, opiskeluoikeus ja ryhmä
(5) urasuunnitelma polulla Ohjaus ja tuki → Urasuunnitelmat → Lisää uusi sekä tallennettujen urasuunnitelmien luettelo
(6) Wilma-tallennus tiedostoon, joka säilyy, kun simuloitu Wilma suljetaan
(7) lähtötila tiedostossa testiaineisto/wilma-lahtotila.json: opiskelijat ja profiilit sekä yksi aiempi urasuunnitelma Aino Testisellä 000456
Urasuunnitelman kentät: [kentät, jotka muistat oikeasta Wilmasta, ilman oikeita tietoja].
Opiskelijat: Aino Testinen 000123 (ryhmä TK26A) ja 000456 (ryhmä TK26B), Eero Esimerkki 001789 (Testikoulutus ja Esimerkkikoulutus), Liisa Kokeilu 002024 ja Ville Testaaja 000999. Muiden koulutus on Testikoulutus.
Tee juureen kaksoisnapsautettavat tiedostot kaynnista-wilma.cmd ja palauta-lahtotila.cmd. Jälkimmäinen palauttaa tiedot lähtötilaan. Ikkuna jää auki virheen sattuessa, ja suljen Wilman sulkemalla ikkunan.
Kirjoita KAYNNISTYS.md:hen osoite ja ohje: käynnistys, mitä pitää nähdä, sulkeminen, palautus ja mitä teen virheen sattuessa.
Pidä muut tiedostot kansiossa simuloitu-wilma.
Tee suunnitelma. Kerro, mitkä tiedostot muuttuvat, mitä komentoja ajat ja miten tarkistan tuloksen ilman koodin lukemista.
Älä muuta tiedostoja ennen kuin hyväksyn.
Kun hyväksyn suunnitelman, älä vielä aloita. Annan palat yksi kerrallaan.
```

3. Lue suunnitelma. Tarkista seitsemän kohtaa, kenttäsi ja kaksoisnapsautettavat tiedostot.
4. Korjauta: kirjoita agentille, mitä puuttuu. Jos ei mitään, jatka.
5. Hyväksy suunnitelma niin, että sovellus kysyy edelleen luvan ennen muutoksia. Älä valitse vaihtoehtoa, joka sallii muutokset automaattisesti.
6. Jos tulee lupapyyntö, ennen kuin lähetit K3:n, kiellä se. Kirjoita agentille: Pysähdy. Odota, että annan palan.
7. **Kehote (K3):** Kopioi koko lohko kehotekenttään. Täytä aukot: tehtävänumero työlistalta ja tilanne, jonka haluat tarkistaa. Lähetä.

```text
Toteuta hyväksytty suunnitelma: TYOLISTA.md:n tehtävä [numero].
Noudata CLAUDE.md:n sääntöjä.
Kun olet valmis, kerro, miten käynnistän sovelluksen ja mitä minun pitää nähdä, kun [tilanne, jonka haluan tarkistaa].
Älä tee tallennuspistettä.
```

8. Lue jokainen lupapyyntö kolmella kysymyksellä. Jos lupaa ei kysytä lainkaan, pysähdy ja kutsu vetäjä.
9. Katso muutosnäkymästä, että uudet tiedostot ovat suunnitelman nimeämissä paikoissa.
10. Avaa `KAYNNISTYS.md` Muistiolla.
11. Kaksoisnapsauta Resurssienhallinnassa tiedostoa `kaynnista-wilma.cmd`. Älä sulje avautuvaa ikkunaa.
12. Avaa ohjeen osoite Edgessä.
13. Kirjaudu valitsemalla testikäyttäjä.
14. **Oma testi:** Hae nimellä Aino Testinen. Totea kaksi tulosta eri opiskelijanumeroilla.
15. Avaa Aino Testisen (000456) profiili. Totea, ettei Primus-tietoja voi muuttaa ja että urasuunnitelmia on yksi.
16. Tee hänelle uusi urasuunnitelma ja Wilma-tallennus kuvitteellisilla arvoilla.
17. Sulje selain ja ikkuna. Käynnistä simuloitu Wilma uudelleen.
18. Avaa Ainon (000456) urasuunnitelmat. Totea, että uusi urasuunnitelmasi on tallessa.
19. Sulje selain ja ikkuna. Kaksoisnapsauta tiedostoa `palauta-lahtotila.cmd`.
20. Käynnistä simuloitu Wilma. Totea, että Ainolla (000456) on vain aiempi urasuunnitelma.
21. **Päätös:** Kirjaa `PAATOSLOKI.md`:hen Muistiolla hyväksyn, korjautan tai hylkään ja peruste muodossa Näin: … Siksi: … Tallenna ja sulje Muistio.
22. Tee tallennuspiste K6:lla omalla viestilläsi.

Seuraavaksi: kuvitteellinen aineisto.

## Tehtävä 3: Kuvitteellinen aineisto

1. Kopioi koko lohko kehotekenttään. Lähetä.

```text
Lisää kansioon testiaineisto opiskelijalista.csv, liitettävä nimilista omana tiedostonaan sekä esitiedot ja haastattelut. Käytä simuloidun Wilman opiskelijoita.
Tapaukset:
(1) Aino Testinen 000123: kaikki tiedot kunnossa. Työaika 37,5 h/vko, palkka 2 450 €/kk, työpaikka Testileipomo Oy, toimipaikka Keskusta, työpaikkaohjaaja Maija Mallikas, työnantajan edustaja Kaisa Mallikas.
(1b) Aino Testinen 000456: nimikaima.
(2) Eero Esimerkki: kaksi opiskeluoikeutta. Palkka 14,20 €/h, työaika 30 h/vko.
(3) Liisa Kokeilu: työaika haastattelussa 37,5 h/vko, esitiedoissa 30 h/vko. Palkka 2 450 ilman yksikköä.
(4) Ville Testaaja: esitietolomake puuttuu.
(5) Opiskelijalistassa on myös tyhjä rivi ja virherivi, opiskelijanumero 12A.
(6) Nimilistassa ovat Aino Testinen ja Eero Esimerkki.
Opiskelijanumerot ovat tekstiä, ja etunollat säilyvät. Älä muuta tiedostoa wilma-lahtotila.json äläkä muita kansioita.
```

2. Lue lupapyynnöt kolmella kysymyksellä. Uudet tiedostot saavat olla vain kansiossa `testiaineisto`.
3. Kopioi alla oleva lohko kehotekenttään. Lähetä.

```text
Lisää KEHOTEPOHJAT.md:n loppuun tämä pohja sellaisenaan. Älä muuta muita tiedostoja.

## K8 Kuvitteellinen tapaus
Lisää testiaineistoon kuvitteellinen tapaus: [tapaus omin sanoin: mikä tilanteessa menee kirjatessa helposti väärin].
Käytä vain keksittyjä nimiä ja tunnisteita testiaineiston tyyliin.
Älä käytä henkilötunnuksia, Y-tunnuksia, osoitteita, puhelinnumeroita tai sähköposteja.
Kerro, mihin tiedostoon lisäsit tapauksen.
```

4. Lue lupapyyntö kolmella kysymyksellä. Muuttua saa vain `KEHOTEPOHJAT.md`.
5. **Kehote (K8):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K8. Täytä aukko: oma tapauksesi tehtävästä 1. Lähetä.
6. Lue lupapyyntö kolmella kysymyksellä. Muuttua saa vain testiaineiston tiedosto.
7. Avaa `testiaineisto/opiskelijalista.csv` Muistiolla, ei Excelillä.
8. **Oma testi:** Tarkista etunollat, tyhjä rivi ja virherivi 12A.
9. Avaa testiaineiston muut tiedostot Muistiolla. Tarkista, että jokainen tehtävän 1 tapaus löytyy. Jos jokin puuttuu, lisää se K8:lla.
10. Etsi oikealta näyttäviä nimiä, yrityksiä tai tunnisteita. Pyydä agenttia vaihtamaan ne keksityiksi.
11. **Päätös:** Kirjaa päätöslokiin testiaineistosta päätös ja peruste omin sanoin. Tallenna ja sulje Muistio.
12. Tee tallennuspiste K6:lla.

Seuraavaksi: kenttäkartoitus.

## Tehtävä 4: Kenttäkartoitus

1. **Kehote:** Kopioi koko lohko kehotekenttään. Täytä aukko: urasuunnitelman kentät, jotka tiedät pakollisiksi. Lähetä.

```text
Tee projektikansion juureen KENTAT.md. Lähteet: kuvauspaketin osa 19, simuloitu Wilma ja maarittely/03-kenttakartoitus.csv, jos se on.
Ota mukaan urasuunnitelman ja profiilin kentät.
Tee jokaisesta kentästä oma kohta, ei taulukkoa. Rivit: Tieto, Lähde, Simuloidun Wilman kenttä, Tarkistustapa, Oma huomio, Testi-Wilman havainto.
Merkitse pakollisiksi nämä urasuunnitelman kentät: [kentät, jotka tiedät pakollisiksi].
Jos kytkentää ei ole selvitetty, kirjoita "kartoitetaan".
Jätä Oma huomio ja Testi-Wilman havainto tyhjiksi äläkä muuta niitä myöhemmin. Älä muuta muita tiedostoja.
```

2. Lue lupapyyntö kolmella kysymyksellä. Muuttua saa vain `KENTAT.md`.
3. Avaa `KENTAT.md` Muistiolla.
4. **Oma testi:** Kirjoita urasuunnitelman jokaisen kentän Oma huomio -riville, eroaako kenttä muistamastasi oikeasta Wilmasta. Kirjoita muistista, älä kuvakaappauksista.
5. Kirjoita loppuun oikean Wilman kentät, jotka puuttuvat simuloidusta. Tallenna ja sulje Muistio.
6. **Päätös:** Kirjaa päätöslokiin kenttäkartoituksesta päätös ja peruste.
7. Tee tallennuspiste K6:lla.

Seuraavaksi: hyväksymistestien runko.

## Tehtävä 5: TESTIT.md-runko

1. **Kehote:** Kopioi koko lohko kehotekenttään. Täytä aukot: tehtävän 2 testisi ja testi omasta tapauksestasi. Lähetä.

```text
Tee projektikansion juureen TESTIT.md kuvauspaketin osan 28 testeistä T01–T22.
Kirjoita tiedoston alkuun: Uusinta kirjataan testin alle rivinä - Uusinta [päivä]: [läpi / ei läpi]. [havainto]. Aiempaa tulosta ei pyyhitä.
Tee jokaiselle testille oma otsikko. Sen alle tulevat rivit Lähtötila (palauta ensin), Mitä teen, Odotan, Työpaja / lisä / jatko, Tulos, Havainto ja Päivä. Älä tee taulukkoa.
Täytä Mitä teen ja Odotan kuvauspaketista. Ota merkintä työpaja, lisä tai jatko TYOLISTA.md:stä.
Kirjoita Tulos-riville vain vaihtoehdot läpi / ei läpi / ei testattu. Jätä Havainto ja Päivä tyhjiksi. Täytän ne itse.
Lisää loppuun omat testini samassa muodossa:
O01 [tehtävän 2 testisi: mitä teit ja mitä odotit]
O02 [testi omasta tapauksestasi: mitä teet ja mitä odotat]
O03 Kaksoiskappaleen esto: toinen kirjaus samalle opiskelijalle ei tee toista urasuunnitelmaa. Lähtötila: jatka testistä T05.
```

2. Lue lupapyyntö kolmella kysymyksellä. Muuttua saa vain `TESTIT.md`.
3. Avaa `TESTIT.md` Muistiolla.
4. **Oma testi:** Vertaa T05:n, T13:n ja T15:n merkintää `TYOLISTA.md`:hen. Korjauta väärät agentilla.
5. Kirjaa O01:lle tulos, havainto ja päivä tehtävän 2 testistäsi. Jätä Tulos-riville yksi vaihtoehto. Tallenna ja sulje.
6. **Päätös:** Kirjaa päätöslokiin `TESTIT.md`:n rungosta päätös ja peruste omin sanoin.
7. Tee tallennuspiste K6:lla.

Seuraavaksi: valmis-tarkistus.

## Valmis, kun

- Simuloitu Wilma käynnistyy kaksoisnapsautuksella `KAYNNISTYS.md`:n ohjeella ilman agenttia, ja sen sivuilla lukee SIMULOITU.
- Haku nimellä Aino Testinen näyttää kaksi opiskelijaa. Uusi urasuunnitelmasi säilyi uudelleenkäynnistyksessä ja katosi palautuksessa.
- `testiaineisto` sisältää tehtävän 1 tapaukset etunollineen.
- `KENTAT.md`:ssä ovat urasuunnitelman ja profiilin kentät ja omat huomiosi.
- `TESTIT.md`:ssä ovat T01–T22 ja O01–O03 Lähtötila-riveineen. O01:llä on tulos.
- `KEHOTEPOHJAT.md`:ssä on K8.
- Päätöslokissa on neljä uutta merkintää, ja viisi uutta tallennuspistettä on tehty.

## Jos jäät jumiin

Jos ilmoitus kertoo, että portti on jo käytössä, pyydä agenttia sulkemaan käynnistämänsä simuloitu Wilma.

Jos käynnistysikkuna sulkeutuu heti, kutsu vetäjä.

Jos hylkäät tai agentti kiertää kehää, sulje Muistio. Palaa ensin tallennuspisteeseen K7:llä ja kirjaa päätös sitten. Kerro vetäjälle.

## Seuraava osio

Osio 04 alkaa kello 14.00. Siinä sovellus tekee ensimmäisen varmennetun Wilma-tallennuksen.
