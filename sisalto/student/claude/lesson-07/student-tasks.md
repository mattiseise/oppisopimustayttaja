# Tehtävät: osio 07 – Oppisopimus ja sen edellytykset (joustokohta)

Aika noin 90 min. Tarvitset: Claude-työpöytäsovelluksen Code-välilehden, projektikansion, Muistion ja selaimen.

Osio on joustokohta, ja sen palat ovat tavoitetta. Lyhennetyssä toteutuksessa teet vain työpaikan.

Jos korjautat, käytä K5:tä. Jos hylkäät, sulje Muistio, palaa ensin tallennuspisteeseen (commit) K7:llä ja kirjaa päätös vasta sitten.

`TESTIT.md`:ssä kirjoitat Lähtötila-riville palauta ensin tai jatka testistä Tnn. Aiempaa tulosta et pyyhi. Lisäät testin alle rivin:

```text
- Uusinta [päivä]: [läpi / ei läpi]. [havainto]
```

## Tehtävä 1: Laajuus, tilannekatsaus ja kriteerit

1. Kysy vetäjältä, teetkö koko osion, lyhennetyn toteutuksen vai siirtyykö osio jatkoon.
2. **Kehote (K11):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K11. Täytä aukko: mitkä osioiden 04–06 palat ja testit ovat kesken. Lähetä.
3. Vertaa agentin vastausta päätöslokin viimeiseen merkintään.
4. Tee siirrossa tehtävä 8 ja sitten kesken jääneet palat vetäjän järjestyksessä. Ensin vähimmäistavoite: osion 04 T13, osion 05 tehtävät 1–5 ja osion 06 tehtävät 1–6. Siirrossa et tee tämän osion muita tehtäviä.
5. Tee lyhennetyssä ensin osioiden 05 ja 06 kesken jääneet palat samassa järjestyksessä.
6. **Oma kriteeri:** Kirjoita Muistiolla `HYVAKSYMISKRITEERIT.md`:hen osio 07: vähintään kaksi Hyväksyn, kun -kohtaa, yksi En hyväksy, jos -kohta ja Tarkistan näin. Liittyvät testit: T03, T04 ja T08, lyhennetyssä vain T04.
7. Tallenna tiedosto ja sulje Muistio.

Seuraavaksi: pyydät agentilta suunnitelman.

## Tehtävä 2: Suunnitelma paloissa

1. Kirjoita paperille oppisopimuksen kentät, jotka tunnet työstäsi. Lyhennetyssä ohita tämä.
2. Kytke suunnittelutila päälle.
3. **Kehote (K2 + K9):** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukot. Lähetä. Lyhennetyssä katso lohkon alta.

```text
Tehtävä: lisää simuloituun Wilmaan oppisopimus-, työpaikka- ja työpaikkaohjaajanäkymät. Lisää niiden kentät KENTAT.md:hen. Tee sovellukseen sovittimet näille lomakkeille.
Simuloidussa Wilmassa pitää olla: Testileipomo Oy (toimipaikat Keskusta ja Satama), Esimerkkikone Oy, työpaikkaohjaajat Maija Mallikas (Testileipomo Oy Keskusta), Pekka Mallikas (Esimerkkikone Oy) ja Pekka Mallikas (Testileipomo Oy Satama) sekä työnantajan edustaja Kaisa Mallikas (Testileipomo Oy). Kokeiluverstas Oy puuttuu tarkoituksella.
Lisää ne ensimmäisessä palassa myös lähtötilaan (testiaineisto/wilma-lahtotila.json), ilman Kokeiluverstas Oy:tä ja oppisopimuksia.
Oppisopimus on jonossa uusi valittava tehtävä. VALMIS vaatii kaikkien valittujen tehtävien varmennuksen.
Oppisopimuksen kentät, jotka tunnen työstäni: [kentät paperiltasi, ilman oikeita tietoja].
Lue ensin CLAUDE.md, TYOLISTA.md ja HYVAKSYMISKRITEERIT.md:n osio 07.
Tärkein kriteerini: [tärkein kriteeri].
Rakennetaan lomakkeet [lomakkeet siinä järjestyksessä, jossa ne pitää viedä Wilmaan] simuloituun Wilmaan.
Käytä vain KENTAT.md:n kenttiä. Jos kenttä puuttuu, merkitse se puuttuvaksi. Älä keksi kenttiä.
Etene jokaisen lomakkeen kohdalla tässä järjestyksessä ja pysähdy jokaisen kohdan jälkeen:
(1) kenttien haku: jokaiselle kentälle täsmälleen yksi osuma
(2) täyttö
(3) Wilma-tallennus
(4) uudelleenluku ja vertailu hyväksyttyyn sisältöön
(5) kaksoiskappaleen esto
Kiinnitä erityistä huomiota kenttään [kenttä, joka menee käsin kirjatessa helpoimmin väärin].
Kerro jokaisen kohdan jälkeen, miten tarkistan sen itse sovelluksesta.
Tee suunnitelma paloissa: ensin näkymät, sitten yksi pala kutakin lomaketta kohden. Kerro jokaisen palan TYOLISTA.md:n tehtävän numero.
Kerro, mitkä tiedostot muuttuvat, mitä komentoja ajat ja miten tarkistan tuloksen ilman koodin lukemista.
Älä muuta tiedostoja ennen kuin hyväksyn.
Kun hyväksyn suunnitelman, älä vielä aloita. Annan palat yksi kerrallaan.
```

Lyhennetty toteutus: kopioi K2 ja K9 `KEHOTEPOHJAT.md`:stä samaan viestiin. Kirjoita K2:n tehtäväksi alla oleva lohko ja K9:n lomakkeeksi Työpaikka. Täytä muut aukot. Lähetä.

```text
Lisää simuloituun Wilmaan työpaikkanäkymä ja sovellukseen työpaikan sovitin. Lisää kentät KENTAT.md:hen. Simuloidussa Wilmassa pitää olla Testileipomo Oy (toimipaikat Keskusta ja Satama) ja Esimerkkikone Oy, ei Kokeiluverstas Oy:tä. Lisää ne ensimmäisessä palassa myös lähtötilaan (testiaineisto/wilma-lahtotila.json). Tee kaksi palaa: näkymä ja sovitin.
```

4. Lue suunnitelma. Tarkista lomakkeiden järjestys ja se, ettei puuttuvaa työpaikkaa luoda kysymättä.
5. Korjauta puutteet kirjoittamalla ne agentille.
6. Hyväksy suunnitelma. Toimi osiossa 05 tekemäsi päätöksen mukaan.
7. Kiellä lupapyyntö tai pysäytä agentti, jos se aloittaa ennen K3:a. Kirjoita: Pysähdy. Odota, että annan palan.

Seuraavaksi: ensimmäinen pala.

## Palan alku ja loppu (tehtävät 3–7)

Tehtävä kertoo pysähdysten tapauksen.

1. **Kehote (K3):** Kopioi K3 `KEHOTEPOHJAT.md`:stä. Täytä aukot tälle palalle. Lähetä.
2. Toimi osiossa 05 tekemäsi päätöksen mukaan. Lue lupapyynnöt kolmella kysymyksellä.
3. Käynnistä simuloitu Wilma ja sovellus `KAYNNISTYS.md`:n ohjeella, jos agentti pysähtyy tarkistukseen.
4. Tee jokaisessa pysähdyksessä agentin kertoma tarkistus vain tehtävän tapauksella. Anna sitten lupa jatkaa.
5. Katso palan lopuksi muutosnäkymästä, että muuttui vain se, mitä suunnitelma lupasi.
6. Sulje simuloitu Wilma ja sovellus. Palauta lähtötila kaksoisnapsauttamalla `palauta-lahtotila.cmd`. Käynnistä molemmat uudelleen.

Palan loppu päätöksen jälkeen: jos hyväksyit, pyydä agenttia merkitsemään työlistan tehtävä valmiiksi. Tee tallennuspiste K6:lla.

## Tehtävä 3: Pala 1, uudet näkymät ja lähtötila

Lyhennetyssä ohita askeleet 4 ja 5.

1. Tee tallennuspiste K6:lla.
2. Tee palan alku. Muuttua saavat simuloitu Wilma, sen lähtötila ja `KENTAT.md`.
3. **Oma testi:** Totea simuloidusta Wilmasta Testileipomo Oy:n kaksi toimipaikkaa ja se, ettei Kokeiluverstas Oy:tä löydy.
4. Avaa Aino Testisen (000123) oppisopimusnäkymä. Vertaa sen kenttiä paperisi kenttiin.
5. Kirjoita `KENTAT.md`:hen Muistiolla, mikä oppisopimuksen kentissä eroaa muistamastasi oikeasta Wilmasta.
6. **Päätös:** Kirjaa päätöslokiin näkymistä päätös. Kirjoita perusteeseen Näin: … Siksi: …
7. Tee palan loppu.

Seuraavaksi: työpaikan sovitin.

## Tehtävä 4: Pala 2, työpaikka ja toimipaikka

1. Tee palan alku. Pysähdysten tapaus on Kokeiluverstas Oy. Lue lisäyksen tiedot ennen kohtaa (3) Wilma-tallennus.
2. Totea simuloidusta Wilmasta, ettei Kokeiluverstas Oy:tä ole. Jos on, palauta lähtötila.
3. **Oma testi T04:** Hae sovelluksella työpaikkaa Testileipomo Oy ilman toimipaikkaa. Totea, että sovellus näyttää Keskustan ja Sataman eikä valitse itse.
4. Hae Esimerkkikone Oy. Totea, että sovellus löytää olemassa olevan tietueen.
5. Hae Kokeiluverstas Oy. Totea, että sovellus valmistelee lisäyksen ja odottaa hyväksyntääsi. Lue tiedot ennen hyväksyntää.
6. Hae Kokeiluverstas Oy uudelleen. Totea simuloidusta Wilmasta, että yritys on siellä vain kerran.
7. Kirjaa tulos ja havainto `TESTIT.md`:n testiin T04.
8. **Päätös:** Kirjaa päätöslokiin työpaikan sovittimesta päätös ja peruste.
9. Tee palan loppu.

Seuraavaksi: työpaikkaohjaaja. Lyhennetyssä tehtävä 8.

## Tehtävä 5: Pala 3, työpaikkaohjaaja

1. Tee palan alku. Pysähdysten tapaus on Esimerkkikone Oy:n Pekka Mallikas.
2. **Oma testi T04:** Hae työpaikkaohjaajaa nimellä Pekka Mallikas. Totea, että sovellus näyttää kaksi vaihtoehtoa työpaikkoineen eikä valitse itse.
3. Valitse Pekka Mallikas, jonka työpaikka on Esimerkkikone Oy. Totea, ettei valinta liity Testileipomo Oy:n Satamaan.
4. Kirjaa tulos ja havainto testin T04 alle uudelle riville.
5. **Päätös:** Kirjaa päätöslokiin työpaikkaohjaajan sovittimesta päätös ja peruste.
6. Tee palan loppu.

Seuraavaksi: oppisopimus.

## Tehtävä 6: Pala 4, oppisopimus

1. Tee palan alku. Pysähdysten tapaukset: (1)–(2) Liisa Kokeilu, (3)–(5) Aino Testinen (000123).
2. **Oma testi T03:** Liitä nimilista, jossa on vain Liisa Kokeilu. Valitse tehtäväksi oppisopimus.
3. Valitse Esimerkkikone Oy, jos sovellus kysyy työpaikkaa.
4. Totea, että sovellus estää kirjauksen ja kertoo syyksi palkan puuttuvan yksikön. Jos työajan ristiriita on ratkaisematta, sekin näkyy syynä.
5. Totea simuloidusta Wilmasta, ettei Liisalle syntynyt oppisopimusta.
6. Kirjaa tulos ja havainto testiin T03.
7. **Oma testi T08:** Palauta lähtötila. Liitä nimilista, jossa on vain Aino Testinen. Valitse 000123 ja tehtäviksi urasuunnitelma ja oppisopimus.
8. Tee urasuunnitelman Wilma-tallennus. Totea, ettei Ainon jonon tila ole vielä VALMIS.
9. Tarkista ennen oppisopimuksen hyväksyntää: Testileipomo Oy Keskusta, 37,5 h/vko, 2 450 €/kk sekä Maija ja Kaisa Mallikas eri kentissä.
10. Hyväksy sisältö. Totea, että kirjaus on varmennettu ja Ainon jonon tila on nyt VALMIS.
11. Avaa simuloitu Wilma suoraan. Totea samat arvot Ainon (000123) oppisopimuksessa. Toisella Aino Testisellä (000456) ei ole oppisopimusta.
12. Kirjaa tulos ja havainto testiin T08.
13. **Päätös:** Kirjaa päätöslokiin oppisopimuksen sovittimesta päätös ja peruste.
14. Tee palan loppu.

Seuraavaksi: lisätehtävä tai kenttäluku.

## Tehtävä 7: Lisätehtävä tai testi-Wilman kenttäluku

Jos testi-Wilma on käytössä, teet kenttäluvun C osiota 08 varten. Muuten valitset A:n tai B:n.

1. **Oma kriteeri:** Kirjoita `HYVAKSYMISKRITEERIT.md`:n osioon 07 tehtävällesi yksi Hyväksyn, kun -kohta ja yksi En hyväksy, jos -kohta.
2. Kytke suunnittelutila päälle.
3. **Kehote (K2):** Kopioi K2 `KEHOTEPOHJAT.md`:stä. Kirjoita tehtäväksi A tai B omin sanoin tai liitä C:n lohko. Täytä muut aukot. Lähetä.
4. Lue suunnitelma ja hyväksy se kuten tehtävässä 2.
5. Tee palan alku.
6. **Oma testi:** Tee tehtäväsi testi. Kirjaa tulos ja havainto `TESTIT.md`:hen.
7. **Päätös:** Kirjaa päätöslokiin päätös ja peruste.
8. Tee palan loppu.

A. HOPS (T06). Simuloituun Wilmaan ja lähtötilaan tulee HOPS-näkymä, sovellukseen sen sovitin. Testi: Aino Testisen Testiosa A saa aikataulun 2027–2028 ja Testiosa B itse valitsemasi. Totea ne simuloidusta Wilmasta. Uusinta ei monista osia.

B. Lausepohja (T09). Kirjoitat itse tavoitetekstin lausepohjan hakasulkeineen. Kielimallia ei käytetä. Testi: täyttämätön aukko estää hyväksynnän.

C. Kenttäluku testi-Wilmaa varten, vain vetäjän luvalla. K2:n tehtävä:

```text
Lisää sovellukseen kenttäluku. Käynnistän sen itse sovelluksesta, kun näkymä on auki näkyvässä selaimessa. Kenttäluku lukee vain auki olevan sivun. Se ei siirry muille sivuille, ei kirjoita kenttiin eikä paina painikkeita. Se kirjoittaa tiedostoon vain näkyvien kenttien nimet ja tyypit. Ei arvoja, piilokenttiä, sivun osoitetta, evästeitä, istuntoa eikä sivun lähdekoodia. Tiedosto tulee projektikansion ulkopuolelle kansioon C:\dev\testi-wilma-raaka. Sovellus ei tallenna projektikansioon selainprofiilia, evästeitä eikä tallenteita. Älä lue tulostiedostoa.
```

Testi C: aja kenttäluku simuloidun Wilman urasuunnitelmaan näkyvässä selaimessa. Sulje sovellus. Avaa tuloste Muistiolla. Yksikin arvo on ei läpi. Avaa ennen tallennuspistettä projektikansio Resurssienhallinnassa. Totea, ettei kenttäluku tuonut uutta kansiota tai tiedostoa.

Seuraavaksi: tarkistat, että osio on valmis.

## Tehtävä 8: Jos osio lyhennetään tai siirtyy jatkoon

1. **Päätös:** Kirjaa päätöslokiin osion 07 lyhennys tai siirto ja syy omin sanoin.
2. Avaa `TESTIT.md` Muistiolla. Kirjoita jatko Työpaja / lisä / jatko -riville testeihin T03, T04 ja T08, joita et tehnyt kokonaan. Älä pyyhi aiempia tuloksia.
3. Tallenna tiedosto ja sulje Muistio.
4. Pyydä agenttia merkitsemään `TYOLISTA.md`:hen osion 07 tekemättömät tehtävät jatkoon.
5. Katso muutosnäkymästä, että vain `TYOLISTA.md` muuttui.
6. Tee tallennuspiste K6:lla.

Seuraavaksi: siirrossa kesken jääneet palat kello 14.15 asti, sitten osio 08. Lyhennetyssä osio 08.

## Valmis, kun

- Osion 07 kriteerit ja huomiosi oppisopimuksen kentistä ovat tallessa.
- Palautus tuo simuloituun Wilmaan työpaikat ja henkilöt ilman Kokeiluverstas Oy:tä.
- Testileipomo Oy ja Pekka Mallikas näkyvät vaihtoehtoina. Liisan oppisopimus estyy. Aino on VALMIS vasta oikein varmennetun oppisopimuksen jälkeen.
- T03:lla, T04:llä ja T08:lla on tulos tai merkintä jatko, ja aiemmat tulokset ovat tallessa.
- Jokaisesta palasta on päätös ja tallennuspiste. Lyhennetyssä riittää työpaikka, siirrossa tehtävä 8 ja kesken jääneet palat.

## Jos jäät jumiin

Jos agentti luo työpaikan tai työpaikkaohjaajan kysymättä, hylkää pala. Jos palkka tallentuu ilman yksikköä, korjauta K5:llä.

Jos pala on kesken kello 14.15, tee tallennuspiste viestillä Kesken: [pala] tai palaa edelliseen K7:llä. Pyydä agenttia merkitsemään pala työlistaan keskeneräiseksi. Tee tehtävä 8.

Jos ongelma jatkuu kahden korjausyrityksen jälkeen, katkaise kehä K10:llä, palaa tallennuspisteeseen K7:llä ja kerro vetäjälle.

## Seuraava osio

Osio 08 alkaa kello 14.30. Siinä teet hyväksymistestit ja päätät, hyväksytkö työpajaversion.
