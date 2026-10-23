# Tehtävät: osio 05 – Lähteet, puutteet ja ristiriidat

Aika noin 90 min. Tarvitset: Claude-työpöytäsovelluksen Code-välilehden, Muistion ja projektikansion.

Vähimmäistavoite on tehtävät 1–5: lähteet, T01 ja tarkistusnäkymä. Osion 06 jono tarvitsee tarkistusnäkymän, jossa hyväksyt sisällön. Tehtävät 6–8 ovat tavoitetta. Jos ne jäävät kesken, ne tehdään osion 07 aikana.

## Tehtävä 1: Aloita päivä ja kirjoita kriteerit

1. Aloita Code-välilehdellä uusi istunto projektikansiossa `C:\dev\oppisopimustayttaja`.
2. **Kehote (K11):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K11. Täytä aukko: mitä haluat tietää, ennen kuin jatkat. Katso apua päätöslokin viimeisestä merkinnästä. Lähetä.
3. Vertaa agentin vastausta tiedostoon `TESTIT.md`. Testi on tehty vain, jos siinä on sinun tuloksesi.
4. Lue päätöslokin rivi Huomenna aloitan tästä. Jos T13 jäi eilen tekemättä, tee nyt osion 04 tehtävä Testikytkin ja testi T13. Aikaa on enintään 20 min. Jos osion 04 pala (d) tai (e) jäi kesken, kerro vetäjälle, ennen kuin jatkat.
5. Avaa `HYVAKSYMISKRITEERIT.md` Muistiolla.
6. **Oma kriteeri:** Lisää osio 05 samalla rungolla kuin aiemmat osiot. Kirjoita Hyväksyn, kun -kohtaan, mitä tarkistusnäkymässä pitää näkyä jokaisesta kentästä.
7. Kirjoita En hyväksy, jos -kohtaan, mikä estää hyväksynnän. Mieti erityisesti puuttuvaa ja piilossa olevaa tietoa.
8. Tallenna tiedosto ja sulje Muistio.

Seuraavaksi: päätät, miten valvot agentin muutoksia tänään.

## Tehtävä 2: Päätä lupa-asetus

Lue ensin lukutekstin kohta Oma lupa-asetus.

1. Valitse, pidätkö lupapyynnöt tiedostomuutoksille vai sallitko muutokset automaattisesti. Komennoille lupapyyntö pidetään joka tapauksessa.
2. Päätä, milloin ja mistä tarkistat muutokset ja mikä muutos saa sinut hylkäämään.
3. Avaa `PAATOSLOKI.md` Muistiolla.
4. **Päätös:** Kirjaa uusi merkintä alla olevilla riveillä. Kirjoita peruste omin sanoin.
5. Tallenna tiedosto ja sulje Muistio.
6. Pyydä vetäjää näyttämään asetus, jos päätit sallia muutokset automaattisesti. Vaihda asetus itse.
7. Tee tallennuspiste (commit) K6:lla. Kirjoita viesti omin sanoin.

```text
## Merkintä [numero]
- Päivä ja osio: [päivä], osio 05
- Tuotos: lupa-asetus ja muutosten tarkistus
- Päätös: [lupapyynnöt pysyvät / tiedostomuutokset sallitaan automaattisesti]
- Tarkistan muutokset: [milloin ja mistä]
- Hylkään, jos: [oma pysäytyssääntö]
- Peruste: [miksi juuri näin, omin sanoin]
- Tallennuspisteen viesti: [viesti]
```

Seuraavaksi: pyydät agentilta suunnitelman.

## Tehtävä 3: Suunnitelma lähteistä ja tarkistusnäkymästä

1. Avaa `KENTAT.md` Muistiolla. Katso, mitkä kentät tulevat esitiedoista, haastattelusta ja profiilista.
2. Kytke suunnittelutila päälle.
3. **Kehote (K2):** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukot. Lähetä.

```text
Tehtävä: [tehtävä omin sanoin].
Lue ensin CLAUDE.md, TYOLISTA.md ja HYVAKSYMISKRITEERIT.md:n osio 05.
Tärkein kriteerini: [tärkein kriteeri].
Sovellus hakee yhden opiskelijan tiedot itse kolmesta lähteestä: esitiedot ja haastattelu kansiosta testiaineisto sekä profiili simuloidusta Wilmasta WilmaRead-luvulla, joka ei muuta mitään.
Jokaisesta kentästä näytetään arvo, lähde ja lukutila: OK, EMPTY, NOT_VISIBLE, READ_FAILED tai CONFLICT (kuvauspaketin osa 15). Lukutila näkyy myös sanoina.
Nämä kentät ja lukutilat estävät hyväksynnän: [kenttä ja lukutila, jotka estävät hyväksynnän työssäsi].
Ristiriidassa näytetään molemmat arvot lähteineen. Sovellus ei valitse. Käyttäjän valinta kirjataan.
Käyttäjä voi korjata arvon tarkistusnäkymässä.
Hyväksyntä sidotaan sisältöön. Kun hyväksytty arvo muuttuu, hyväksyntä vanhenee. Urasuunnitelman Wilma-tallennus käyttää vain voimassa olevaa hyväksyntää.
Lähtötilan palautus (palauta-lahtotila.cmd) tyhjentää myös valinnat ja hyväksynnät.
Jaa työ viiteen palaan: (1) esitiedot ja haastattelu, (2) profiili, (3) tarkistusnäkymä, (4) ristiriidan ratkaisu ja kirjaus, (5) hyväksynnän vanheneminen. Kerro jokaisen palan kohdalla TYOLISTA.md:n tehtävän numero.
Kun hyväksyn suunnitelman, älä aloita. Annan palat yksi kerrallaan, palat 1 ja 2 yhdessä.
Tee suunnitelma. Kerro, mitkä tiedostot muuttuvat, mitä komentoja ajat ja miten tarkistan tuloksen ilman koodin lukemista.
Älä muuta tiedostoja ennen kuin hyväksyn.
```

4. Lue suunnitelma. Tarkista, että siinä on viisi palaa, niiden tehtävänumerot ja estävät lukutilasi.
5. Korjauta suunnitelmaa kirjoittamalla agentille, mitä puuttuu. Jos mitään ei puutu, siirry seuraavaan askeleeseen.
6. Hyväksy suunnitelma tehtävän 2 päätöksesi mukaan. Jos pidät lupapyynnöt, älä valitse vaihtoehtoa, joka sallii muutokset automaattisesti.
7. Jos agentti alkaa toteuttaa ennen K3:a, kiellä lupapyyntö ja kirjoita: Pysähdy. Odota, että annan palan. Jos sallit muutokset automaattisesti, pysäytä agentti, katso muutosnäkymä ja palaa tarvittaessa tallennuspisteeseen K7:llä.
8. Kirjoita palojen tehtävänumerot paperille.

Seuraavaksi: rakennat palat 1 ja 2.

## Tehtävä 4: Palat 1 ja 2 – lähteet ja T01

Teet palat 1 ja 2 yhdellä kierroksella. Työkierros on sama kaikissa paloissa:
- Palauta lähtötila ennen testiä: sulje simuloitu Wilma ja sovellus ja kaksoisnapsauta `palauta-lahtotila.cmd`. Testin Lähtötila-rivi on silloin palauta ensin.
- Korjautan: K5, sitten muutosten tarkistus ja testi uudelleen. Kirjaa uusinta testin alle omalle rivilleen: `- Uusinta [päivä]: [läpi / ei läpi]. [havainto]`. Älä pyyhi aiempaa tulosta.
- Hylkään: sulje Muistio, palaa tallennuspisteeseen K7:llä ja kirjaa päätös vasta sitten.
- Hyväksyn: pyydä agenttia merkitsemään työlistan tehtävä valmiiksi ennen tallennuspistettä.

1. **Kehote (K3):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K3. Täytä aukot: palojen 1 ja 2 tehtävänumerot ja tilanne, jonka haluat tarkistaa. Lähetä.
2. Kirjoita odotusajalla T01:n kohdat Lähtötila, Mitä teen ja Odotan.
3. Tarkista muutokset päätöksesi mukaan. Lue lupapyynnöt kolmella kysymyksellä ja katso lopuksi muutosnäkymä.
4. Palauta lähtötila. Käynnistä simuloitu Wilma ja sovellus `KAYNNISTYS.md`:n ohjeella.
5. Kirjaudu itse simuloituun Wilmaan sovelluksen avaamassa näkyvässä selaimessa.
6. **Oma testi T01 (sim.):** Hae Aino Testinen opiskelijanumerolla 000123. Totea, että esitietojen ja haastattelun kentillä näkyvät arvo ja lähde.
7. Totea, että profiilin kenttien lähteenä on profiili ja ryhmä on TK26A, ei TK26B.
8. Totea, ettet vienyt etkä kopioinut yhtään tiedostoa itse.
9. Kirjaa tulos ja havainto T01:n kohdalle.
10. **Päätös:** Kirjaa päätöslokiin päätös ja peruste omin sanoin. Tee tallennuspiste K6:lla.

Seuraavaksi: kokoat kentät yhteen näkymään.

## Tehtävä 5: Pala 3 – tarkistusnäkymä

1. **Kehote (K3):** Kopioi K3 ja täytä aukot palan 3 mukaan. Lähetä.
2. Tarkista muutokset kuten tehtävässä 4.
3. Palauta lähtötila. Käynnistä simuloitu Wilma ja sovellus.
4. **Oma testi:** Avaa Aino Testisen tarkistusnäkymä. Käy osion 05 kriteerisi läpi yksi kerrallaan. Totea, että voit hyväksyä sisällön.
5. **Päätös:** Kirjaa päätöslokiin päätös ja peruste muodossa "Näin: … Siksi: …". Tee tallennuspiste K6:lla.

Seuraavaksi: vähimmäistavoite on tehty. Jatka tavoitteeseen.

## Tehtävä 6: Pala 4 – ristiriita ja T03 (tavoite)

1. **Kehote (K3):** Kopioi K3 ja täytä aukot palan 4 mukaan. Lähetä.
2. Kirjoita odotusajalla T03:n kohdat Lähtötila, Mitä teen ja Odotan.
3. Tarkista muutokset kuten tehtävässä 4.
4. Palauta lähtötila. Käynnistä simuloitu Wilma ja sovellus.
5. **Oma testi T03 (työaika):** Avaa Liisa Kokeilun (002024) tiedot. Totea, että työajan lukutila on CONFLICT ja molemmat arvot näkyvät lähteineen: 37,5 h/vko ja 30 h/vko.
6. Totea, ettei kumpaakaan arvoa ole valittu valmiiksi.
7. Valitse toinen arvo.
8. Avaa Liisan tiedot uudelleen. Totea, että valintasi on tallessa.
9. Kirjaa tulos ja havainto T03:n kohdalle. Merkitse, että palkka testataan osiossa 07.
10. **Päätös:** Kirjaa päätöslokiin päätös ja peruste. Tee tallennuspiste K6:lla.

Seuraavaksi: rikot simuloidun Wilman tahallaan.

## Tehtävä 7: Testikytkimet ja T17 (tavoite)

1. **Kehote:** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukko `KENTAT.md`:n profiilikentällä. Lähetä.

```text
Lisää simuloituun Wilmaan kaksi testikytkintä samalla tavalla kuin eilinen testikytkin.
(1) Piilota kenttä: profiilista piilotetaan kenttä [profiilin kenttä, jonka puuttuminen olisi työssäsi vaarallisinta].
(2) Sammuta: simuloitu Wilma ei vastaa sovelluksen lukuun.
Lisää molemmat lähtötilaan pois päältä, jotta palauta-lahtotila.cmd kytkee ne pois.
Älä muuta sovellusta. Kerro, miten kytken kytkimet päälle ja pois.
```

2. Tarkista muutokset kuten tehtävässä 4. Vain simuloidun Wilman ja lähtötilan tiedostoja saa muuttua.
3. Palauta lähtötila. Käynnistä simuloitu Wilma ja sovellus.
4. **Oma testi T17:** Kytke kentän piilotus päälle. Avaa Aino Testisen tiedot. Totea, että kentän lukutila on NOT_VISIBLE eikä kenttä näy tyhjänä.
5. Yritä hyväksyä sisältö, jos kenttä on hyväksynnän estävien listallasi. Hyväksynnän pitää estyä.
6. Kytke piilotus pois ja sammutus päälle.
7. Avaa Aino Testisen tiedot uudelleen. Totea, että profiilin kenttien lukutila on READ_FAILED ja virhe näkyy. Mikään profiilin kenttä ei saa näkyä tyhjänä.
8. Kirjaa T17:n kohdalle Lähtötila, tulos ja havainto.
9. Kokeile palautusta: palauta lähtötila ja käynnistä simuloitu Wilma. Totea, että molemmat kytkimet ovat pois päältä.
10. **Päätös:** Kirjaa päätöslokiin päätös ja peruste. Tee tallennuspiste K6:lla.

Seuraavaksi: testaat, vanheneeko hyväksyntä.

## Tehtävä 8: Pala 5 – hyväksynnän vanheneminen (tavoite)

1. **Kehote (K3):** Kopioi K3 ja täytä aukot palan 5 mukaan. Lähetä.
2. Tarkista muutokset kuten tehtävässä 4.
3. Palauta lähtötila. Käynnistä simuloitu Wilma ja sovellus.
4. Hyväksy Aino Testisen sisältö tarkistusnäkymässä.
5. **Oma testi:** Muuta yhtä hyväksymääsi arvoa. Totea, että hyväksyntä näkyy vanhentuneena.
6. Yritä aloittaa urasuunnitelman Wilma-tallennus. Sen pitää estyä. Älä tee Wilma-tallennusta.
7. **Päätös:** Kirjaa päätöslokiin päätös ja peruste muodossa "Näin: … Siksi: …". Tee tallennuspiste K6:lla.

Seuraavaksi: tarkistat, että osio on valmis.

## Valmis, kun

Vähimmäistavoite:
- `HYVAKSYMISKRITEERIT.md`:ssä on osio 05.
- Päätöslokissa on lupa-asetus pysäytyssääntöineen ja päätös jokaisesta tehdystä palasta.
- Sovellus näyttää Aino Testisen kentät arvoineen, lähteineen ja lukutiloineen, ja voit hyväksyä sisällön.
- `TESTIT.md`:ssä on T01:n tulos, havainto ja Lähtötila-rivi.
- Viimeinen tallennuspiste on tehty.

Tavoite:
- Liisa Kokeilun työaika näyttää molemmat arvot, ja valintasi säilyy (T03).
- Piilotettu kenttä on NOT_VISIBLE ja sammutetun simuloidun Wilman profiili READ_FAILED (T17). Palautus kytkee kytkimet pois.
- Muutettu arvo vanhentaa hyväksynnän.

## Jos jäät jumiin

Jos lukutila näkyy vain koodina tai värinä, korjauta K5:llä ja pyydä se myös sanoina.

Jos piilotettu tai sammutettu kenttä näkyy tyhjänä, kirjaa ei läpi. Korjauta K5:llä ja testaa uudelleen.

Jos `palauta-lahtotila.cmd` puuttuu tai ei toimi, kerro vetäjälle.

Jos komennoille ei enää tule lupapyyntöä, pysähdy ja kutsu vetäjä.

Jos sama ongelma on jäljellä kahden korjausyrityksen jälkeen, katkaise kehä K10:llä ja palaa tallennuspisteeseen K7:llä. Kerro vetäjälle.

Jos kello on 10.30 ja pala on kesken, tee tallennuspiste K6:lla viestillä Kesken: [pala] tai palaa edelliseen tallennuspisteeseen K7:llä. Pyydä agenttia merkitsemään pala työlistaan keskeneräiseksi. Vetäjä päättää osion 06 alussa, jatketaanko. Osion 06 jono tarvitsee palan 3.

## Seuraava osio

Osio 06 alkaa kello 10.45. Siinä sovellus tuo opiskelijalistan ja käsittelee sen työjonona. Mieti tauolla, miten erotat kaksi samannimistä opiskelijaa.
