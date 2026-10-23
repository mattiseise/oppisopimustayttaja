# Tehtävät: osio 08 – Hyväksymistestit ja häiriötilanne

Aika noin 75 min. Tarvitset: Claude-työpöytäsovelluksen Code-välilehden, projektikansion, Muistion, selaimen ja tiedostot `TESTIT.md`, `KAYNNISTYS.md` ja `TYOKORTTI.md`.

Agentin valmis ei ole testitulos. Tässä osiossa et kysy agentilta, menivätkö testit läpi. Katsot tuloksen itse sovelluksesta ja simuloidusta Wilmasta.

Jos korjautat, käytä K5:tä. Jos hylkäät, sulje Muistio, palaa ensin tallennuspisteeseen (commit) K7:llä ja kirjaa päätös vasta sitten.

Testi, joka tekee Wilma-tallennuksen, alkaa lähtötilasta. Palauta lähtötila näin: sulje simuloitu Wilma ja sovellus, kaksoisnapsauta `palauta-lahtotila.cmd` ja käynnistä molemmat `KAYNNISTYS.md`:n ohjeella.

`TESTIT.md`:ssä kirjoitat Lähtötila-riville palauta ensin tai jatka testistä Tnn. Aiempaa tulosta et pyyhi. Jos testillä on jo tulos, lisäät testin alle rivin:

```text
- Uusinta [päivä]: [läpi / ei läpi]. [havainto]
```

## Tehtävä 1: Kriteerit työpajaversiolle

1. Lue alla oleva tarkistuslista.
2. **Oma kriteeri:** Kirjoita Muistiolla `HYVAKSYMISKRITEERIT.md`:hen osio 08: milloin hyväksyt työpajaversion, milloin et ja miten tarkistat.
3. Tallenna tiedosto ja sulje Muistio.

Vähimmäistavoite:

- [ ] Simuloitu Wilma käynnistyy `KAYNNISTYS.md`:n ohjeella ilman agenttia. Siinä on kirjautuminen ilman salasanaa, opiskelijahaku, profiili ja urasuunnitelma.
- [ ] Sovellus käynnistyy samalla ohjeella ja avaa näkyvän selaimen, jossa kirjaudut itse. Se kirjoittaa vain simuloituun Wilmaan.
- [ ] Yhden opiskelijan tiedot haetaan automaattisesti kuvitteellisista lähteistä ja näytetään tarkistettavina lähteineen.
- [ ] Urasuunnitelman Wilma-tallennus varmennetaan uudelleenluvulla. Poikkeava arvo näkyy tarkistamattomana.
- [ ] Kahden opiskelijan jonossa VALMIS tulee vasta varmennuksen jälkeen. Seuraava avautuu itsestään, eikä edellisen hyväksyntä periydy.
- [ ] Ohjetiedosto, työlista, päätösloki (vähintään 10 merkintää), hyväksymiskriteerit, `TESTIT.md` (vähintään T01, T02, T05, T13 ja T20 tuloksineen) ja tallennuspiste jokaisen osion lopussa. `JATKO.md` tehdään osiossa 09.

Tavoite lisää tähän lukutilat ja ristiriidat, listatuonnin ja nimikaimat, jonon tilan Odottaa lisätietoja, oppisopimuksen riippuvuuksineen, PRO-ilmeen, yhden häiriötestin ja testi-Wilman lukukokeilun, jos ehdot täyttyvät.

Seuraavaksi: testikierros.

## Tehtävä 2: Testikierros

Testit teet ilman agenttia.

1. Tee tallennuspiste K6:lla, jos edellisen jälkeen on muutoksia.
2. Palauta lähtötila.
3. Avaa simuloitu Wilma. Totea, ettei Aino Testisellä (000123), Ville Testaajalla eikä Liisa Kokeilulla ole urasuunnitelmaa.
4. Avaa `TESTIT.md` Muistiolla. Lue jokaisesta testistä Mitä teen ja Odotan, ennen kuin teet sen.
5. **Oma testi T01, T02, T05 ja T20:** Liitä sovellukseen nimilista, jossa ovat Aino Testinen, Ville Testaaja ja Liisa Kokeilu. Valitse Ainoksi 000123.
6. Totea, että Ainon tiedot tulivat lähteistä ja näkyvät tarkistettavina.
7. Hyväksy Ainon sisältö ja tee urasuunnitelman Wilma-tallennus. Totea, että Aino on VALMIS vasta varmennuksen jälkeen.
8. Totea, että Ville avautui itsestään eikä mitään ole hyväksytty.
9. Avaa simuloitu Wilma suoraan. Totea, että Ainon (000123) arvot ovat oikein ja 000456:n urasuunnitelma on ennallaan.
10. Kirjaa T01, T02, T05 ja T20 omin sanoin.
11. **Oma testi T13:** Jatka Ville Testaajalla. Kytke testikytkin tallenna kenttä väärin päälle.
12. Täydennä Villen puuttuvat arvot tarkistusnäkymässä kuvitteellisilla arvoilla ja hyväksy sisältö. Tee Villen urasuunnitelman Wilma-tallennus. Totea, että väärä kenttä näkyy tarkistamattomana eikä Ville ole VALMIS.
13. Kytke testikytkin pois. Kirjaa T13. Lähtötila on jatka testistä T20.
14. **Oma testi T14:** Palauta lähtötila. Liitä nimilista, jossa on vain Liisa Kokeilu. Käsittele hänet pelkällä näppäimistöllä Wilma-tallennukseen asti.
15. Totea, että lukutilat, jonon tilat ja virheet näkyvät myös sanoina.
16. Vertaa sovelluksen värejä ohjetiedoston kohtaan Ulkoasu. Kirjaa T14.
17. Tee muut työpajatestit ilman Wilma-tallennusta: T03, T17, T18, T19, T22 ja O02. Kirjoittavat testit T04, T08 ja T21 teet vain, jos aikaa jää ja vetäjä ohjaa. Aloita ne palautuksella.
18. Merkitse ei testattu vain testiin, jolla ei ole tulosta mistään osiosta.
19. Tallenna tiedosto ja sulje Muistio.
20. Tee tallennuspiste K6:lla.

Seuraavaksi: häiriötilanne tai testi-Wilma.

## Tehtävä 3: Häiriötilanne (B1) tai testi-Wilma (B2)

Vetäjä kertoo, kumman teet. B2 tehdään vain, jos testi-Wilma on käytössä, kenttäluku on valmis ja vetäjä on tarkistanut ehdot.

B1: Katko Wilma-tallennuksen jälkeen (T10)

1. Kytke suunnittelutila päälle.
2. **Kehote (K2):** Kopioi K2 `KEHOTEPOHJAT.md`:stä. Kirjoita tehtäväksi omin sanoin: simuloituun Wilmaan testikytkin, joka katkaisee yhteyden heti Wilma-tallennuksen jälkeen, ja lähtötilaan se pois päältä. Osio on 08. Täytä muut aukot. Lähetä.
3. Lue suunnitelma. Tarkista, että muuttuvat vain simuloitu Wilma ja sen lähtötila.
4. Hyväksy suunnitelma. Toimi osiossa 05 tekemäsi päätöksen mukaan.
5. Kiellä lupapyyntö tai pysäytä agentti, jos se aloittaa ennen K3:a. Kirjoita: Pysähdy. Odota, että annan palan.
6. **Kehote (K3):** Kopioi K3. Täytä aukot. Lähetä.
7. Toimi osiossa 05 tekemäsi päätöksen mukaan. Lue lupapyynnöt kolmella kysymyksellä.
8. Katso muutosnäkymästä, että muuttuivat vain simuloitu Wilma ja sen lähtötila.
9. Kirjoita `TESTIT.md`:n T10:n Odotan-kohtaan, mitä sovelluksen pitää näyttää.
10. Palauta lähtötila. Totea simuloidusta Wilmasta, että uusi kytkin on pois päältä.
11. Liitä nimilista, jossa ovat Eero Esimerkki ja Liisa Kokeilu. Valitse Eerolle Testikoulutus.
12. Kytke uusi kytkin päälle.
13. **Oma testi T10:** Tee Eeron urasuunnitelman Wilma-tallennus.
14. Totea, että sovellus näyttää Tallennustulos tuntematon ja pysäyttää jonon. Totea, ettei Liisa avautunut. Eeron jonon tila on Tarkistettava tallennus tai päätöksesi mukainen nimi.
15. Kytke kytkin pois ja jatka Eeron käsittelyä sovelluksessa.
16. Avaa simuloitu Wilma suoraan. Totea, että Eerolla on täsmälleen yksi urasuunnitelma.
17. Kirjaa T10:n Lähtötila, tulos ja havainto.
18. **Päätös:** Kirjaa päätöslokiin testikytkimestä ja T10:n tuloksesta päätös ja peruste.
19. Tee tallennuspiste K6:lla.

B2: Testi-Wilman kenttäluku

1. Käy vetäjän kanssa läpi testi-Wilman turvatarkistus.
2. Lue `TYOKORTTI.md`:n tietoturvan muistilista ääneen.
3. Pidä agentin keskustelu tauolla B2:n ajan. Kiellä jokainen lupapyyntö, joka avaisi testi-Wilman sovelluksen sisäänrakennetussa selaimessa tai muuten.
4. Käynnistä sovellus itse `KAYNNISTYS.md`:n ohjeella.
5. Kirjoita testi-Wilman osoite itse sovelluksen näkyvään selaimeen.
6. Kirjaudu testitunnuksellasi. Tunnus ei mene agentille eikä mihinkään tiedostoon.
7. Avaa testiopiskelijan haku.
8. Aja kenttäluku.
9. Avaa urasuunnitelman uusi lomake (Ohjaus ja tuki → Urasuunnitelmat → Lisää uusi). Älä tallenna sitä.
10. Aja kenttäluku.
11. Kirjaudu ulos, sulje näkyvä selain ja sulje sovellus.
12. **Oma testi:** Avaa kenttäluvun tulostiedosto kansiosta `C:\dev\testi-wilma-raaka` Muistiolla. Totea, ettei siinä ole nimiä, tunnisteita, arvoja, osoitteita eikä evästeitä. Ei niitä myöskään tiedoston nimessä.
13. Pysähdy ja kerro vetäjälle, jos löydät jotain niistä.
14. Kirjoita `KENTAT.md`:hen Muistiolla omin sanoin, mitkä testi-Wilman kentät eroavat simuloidusta. Kirjoita vain kenttien nimet ja tyypit kuvauspaketin liitteen A mukaan. Älä kopioi tulostiedostoa projektikansioon.
15. Avaa projektikansio Resurssienhallinnassa. Totea, ettei sinne tullut uutta kansiota tai tiedostoa. Selainprofiilia, evästeitä, tallenteita tai sivujen sisältöä ei saa olla.
16. Pysähdy ja kerro vetäjälle, jos näet uuden kansion tai tiedoston. Älä tee tallennuspistettä.
17. **Päätös:** Kirjaa päätöslokiin kenttäluvun tuloksesta päätös ja peruste.
18. Tee tallennuspiste K6:lla vasta, kun askeleiden 12 ja 15 tulos on puhdas.

Seuraavaksi: korjautat yhden testin.

## Tehtävä 4: Korjautus ja uusi testi

1. Valitse yksi ei läpi -testi. Jos sellaista ei ole, tee yksi ei testattu -testi ja jatka sillä.
2. **Kehote (K5):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K5. Täytä aukot: testin tunnus, mitä näit ja mitä pitää tapahtua. Lähetä.
3. Toimi osiossa 05 tekemäsi päätöksen mukaan. Lue lupapyynnöt kolmella kysymyksellä.
4. Katso muutosnäkymästä, että muuttui vain korjattava kohta.
5. Palauta lähtötila, jos testi tekee Wilma-tallennuksen. Muuten käynnistä simuloitu Wilma ja sovellus `KAYNNISTYS.md`:n ohjeella.
6. **Oma testi:** Tee sama testi uudelleen samalla opiskelijalla.
7. Palauta lähtötila ja tee T05 uudelleen Aino Testisellä (000123). Totea, ettei korjaus rikkonut sitä.
8. Lisää kummankin testin alle uusintarivi. Älä pyyhi aiempaa tulosta.
9. **Päätös:** Kirjaa päätöslokiin korjauksesta päätös ja peruste.
10. Tee tallennuspiste K6:lla.

Seuraavaksi: vetäjä pyytää näyttöä kolmesta testistä. Sen jälkeen teet päätöksen työpajaversiosta.

## Tehtävä 5: Hyväksymispäätös

1. Käy tehtävän 1 tarkistuslista läpi. Rastita paperille kohdat, jotka näit testeissä itse.
2. Vertaa tulosta osion 08 kriteereihisi.
3. **Päätös:** Kirjaa päätöslokiin työpajaversiosta hyväksyn, korjautan tai hylkään, peruste omin sanoin ja yksi asia, jota testisi eivät osoita.
4. Pyydä agenttia merkitsemään työlistaan valmiiksi tehtävät, joiden testin viimeisin tulos on `TESTIT.md`:ssä läpi.
5. Katso muutosnäkymästä, että vain `TYOLISTA.md` muuttui.
6. **Kehote (K6):** Kopioi K6 `KEHOTEPOHJAT.md`:stä. Aloita viesti sanoilla Työpajaversio 1 ja kirjoita perään, mitä nyt toimii. Lähetä.
7. Totea agentin vastauksesta, että tallennuspisteen viesti alkaa sanoilla Työpajaversio 1.

Seuraavaksi: tarkistat, että osio on valmis.

## Valmis, kun

- `HYVAKSYMISKRITEERIT.md`:ssä on osion 08 kriteerit omin sanoin.
- Jokaisella työpajatestillä on `TESTIT.md`:ssä tulos (läpi, ei läpi tai ei testattu) ja oma havaintosi. Uusinnat ovat omilla riveillään, ja aiemmat tulokset ovat tallessa.
- Vähintään yksi ei läpi -testi on korjautettu ja testattu uudelleen.
- T14 on kirjattu. B1:ssä T10 on kirjattu. B2:ssa testi-Wilman havainnot ovat `KENTAT.md`:ssä, eikä projektikansioon tullut selainprofiilia, evästeitä eikä tallenteita.
- Päätöslokissa on hyväksymispäätös ja asia, jota testit eivät osoita.
- Tallennuspiste Työpajaversio 1 on tehty.

## Jos jäät jumiin

Jos aika loppuu, tee ensin vähimmäistestit T01, T02, T05, T13 ja T20. Merkitse ei testattu vain testeihin, joilla ei ole tulosta mistään osiosta.

Jos tulos poikkeaa Odotan-kohdasta, tarkista ensin, palautitko lähtötilan. Älä korjauta pois turvasääntöä, kuten kaksoiskappaleen estoa.

Jos testi-Wilman kirjautuminen ei onnistu näkyvässä selaimessa, älä etsi kiertotietä. Kirjaa havainto `KENTAT.md`:hen ja tee B1.

Jos kenttäluvun tulosteessa on arvoja tai tunnisteita, älä anna tiedostoa agentille. Kerro vetäjälle heti.

Jos korjaus ei onnistu kahdella yrityksellä, katkaise kehä K10:llä ja palaa tallennuspisteeseen K7:llä.

## Seuraava osio

Osio 09 alkaa kello 15.45. Siinä kokoat jatkosuunnitelman `JATKO.md` ja sovit seurantatapaamisen.
