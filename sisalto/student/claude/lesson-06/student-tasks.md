# Tehtävät: osio 06 – Opiskelijalista ja työjono

Aika noin 75 min. Tarvitset: Claude-työpöytäsovelluksen Code-välilehden, Muistion ja projektikansion.

Vähimmäistavoite on tehtävät 1–6: tuonti, kohdistus (T02), jono ja VALMIS (T20). Tehtävä 6 tarvitsee osion 05 palan 3. Jos se on kesken, kerro vetäjälle. Tehtävä 7 on tavoitetta. Kesken jäänyt tehdään osion 07 aikana.

## Tehtävä 1: Uusi istunto ja kriteerit jonolle

1. Aloita Code-välilehdellä uusi istunto projektikansiossa `C:\dev\oppisopimustayttaja`.
2. **Kehote (K11):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K11. Täytä aukko: mitä haluat tietää ennen jonon rakentamista. Lähetä.
3. Vertaa vastausta tiedostoon `TESTIT.md`.
4. Avaa `HYVAKSYMISKRITEERIT.md` Muistiolla.
5. **Oma kriteeri:** Lisää osio 06. Kirjoita Hyväksyn, kun -kohtaan, mitä jonossa pitää näkyä.
6. Kirjoita En hyväksy, jos -kohtaan vähintään yksi asia, jota jono ei saa koskaan tehdä.
7. Tallenna tiedosto ja sulje Muistio.

Seuraavaksi: päätät jonon tilojen nimet.

## Tehtävä 2: Päätä jonon tilojen nimet

1. Avaa kuvauspaketti kansiosta `maarittely` Muistiolla.
2. Etsi Muistion haulla (Ctrl+F) sanat Listan tila. Lue osan 9 taulukko jonon tiloista.
3. Etsi haulla sanat Puuttuva tieto ei aiheuta. Lue osan 20 kappale.
4. Päätä nimet. Suositus on osan 9 nimet. Yksi sana saa tarkoittaa vain yhtä asiaa.
5. **Päätös:** Kirjaa päätöslokiin jonon tilojen nimet ja peruste omin sanoin. Hyväksyn tarkoittaa osan 9 nimiä. Korjautan tarkoittaa omia nimiäsi.
6. Tee tallennuspiste (commit) K6:lla.

Seuraavaksi: pyydät agentilta suunnitelman.

## Tehtävä 3: Suunnitelma tuonnista ja jonosta

1. Kytke suunnittelutila päälle.
2. **Kehote (K2):** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukot. Lähetä.

```text
Tehtävä: [tehtävä omin sanoin].
Lue ensin CLAUDE.md, TYOLISTA.md ja HYVAKSYMISKRITEERIT.md:n osio 06.
Tärkein kriteerini: [tärkein kriteeri].
Tuonti: CSV-tiedosto kansiosta testiaineisto ja liitettävä nimilista. XLSX ei kuulu tähän. Lähtötiedostoa ei muuteta. Tunnisteet käsitellään tekstinä, jotta etunollat säilyvät.
Tuonnin esikatselussa käyttäjä kohdistaa sarakkeet ennen käsittelyä. Esikatselussa pitää näkyä: [mitä sinun pitää nähdä, jotta huomaat virherivin].
Nimi on vain hakusyöte. Nimikaimoista ja useista opiskeluoikeuksista näytetään erottavat tiedot, ja käyttäjä valitsee. Kirjoitus sallitaan vasta yksiselitteisen valinnan jälkeen.
Jonossa on yksi aktiivinen opiskelija. Jonon tilat näytetään sanoina: [nimet päätökseni mukaan].
VALMIS vasta, kun valittu tehtävä, nyt urasuunnitelma, on varmennettu. Sen jälkeen seuraava avautuu automaattisesti. Edellisen arvot ja hyväksyntä eivät periydy.
Opiskelijan voi siirtää odottamaan lisätietoja vain perustelun kanssa.
Jono säilyy, kun sovellus suljetaan. Saman listan uudelleentuonti ei käynnistä valmista uudelleen.
Lähtötilan palautus (palauta-lahtotila.cmd) tyhjentää myös jonon.
Jaa työ viiteen palaan: (1) tuonti ja esikatselu, (2) kohdistus ja valinta, (3) jono ja jonon tilat, (4) VALMIS ja seuraava, (5) odottaminen ja pysyvyys. Kerro jokaisen palan kohdalla TYOLISTA.md:n tehtävän numero.
Kun hyväksyn suunnitelman, älä aloita. Annan palat yksi kerrallaan, palat 3 ja 4 yhdessä.
Tee suunnitelma. Kerro, mitkä tiedostot muuttuvat, mitä komentoja ajat ja miten tarkistan tuloksen ilman koodin lukemista.
Älä muuta tiedostoja ennen kuin hyväksyn.
```

3. Lue suunnitelma. Tarkista, että siinä on viisi palaa, niiden tehtävänumerot ja jonon tilojen nimet.
4. Korjauta puuttuvat kohdat kirjoittamalla agentille.
5. Hyväksy suunnitelma. Toimi osiossa 05 tekemäsi päätöksen mukaan. Jos agentti alkaa toteuttaa ennen K3:a, toimi kuten osion 05 tehtävän 3 askeleessa 7.
6. Kirjoita palojen tehtävänumerot paperille.

Seuraavaksi: rakennat tuonnin.

## Tehtävä 4: Pala 1 – tuonti ja esikatselu (T18)

Työkierros on sama kuin osiossa 05. K3:n jälkeen tarkistat muutokset osiossa 05 tekemäsi päätöksen mukaan, palautat lähtötilan ja käynnistät simuloidun Wilman ja sovelluksen `KAYNNISTYS.md`:n ohjeella. Korjautan: K5 ja uusinta omalle rivilleen. Hylkään: sulje Muistio, palaa ensin tallennuspisteeseen K7:llä ja kirjaa päätös sitten. Hyväksyn: pyydä agenttia merkitsemään työlistan tehtävä valmiiksi.

1. Avaa `testiaineisto/opiskelijalista.csv` Muistiolla, ei Excelillä. Katso opiskelijanumerot sekä tyhjät ja virheelliset rivit.
2. **Kehote (K3):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K3. Täytä aukot: palan 1 tehtävänumero ja tilanne, jonka haluat tarkistaa. Lähetä.
3. Tarkista muutokset, palauta lähtötila ja käynnistä kuten yllä.
4. **Oma testi T18 (osin):** Tuo `opiskelijalista.csv`. Totea esikatselusta, että numero 000123 näkyy etunollineen, tyhjä rivi ja virherivi 12A erottuvat ja sarakkeet ovat oikein.
5. Älä aloita käsittelyä CSV-listasta.
6. Avaa kansion `testiaineisto` nimilista Muistiolla ja kopioi nimet.
7. Liitä nimet sovellukseen nimilistana. Totea esikatselusta, että nimiä on kaksi.
8. Kirjaa T18:n kohdalle Lähtötila (palauta ensin), tulos ja havainto.
9. **Päätös:** Kirjaa päätöslokiin päätös ja peruste. Tee tallennuspiste K6:lla.

Seuraavaksi: nimikaimat ja opiskeluoikeudet.

## Tehtävä 5: Pala 2 – kohdistus ja valinta (T02)

1. **Kehote (K3):** Kopioi K3 ja täytä aukot palan 2 mukaan. Lähetä.
2. Tarkista muutokset, palauta lähtötila ja käynnistä kuten tehtävässä 4.
3. **Oma testi T02:** Liitä nimilista ja aloita käsittely. Totea, että Aino Testiselle näytetään kaksi vaihtoehtoa erottavine tietoineen.
4. Yritä jatkaa valitsematta. Kirjoituksen pitää estyä.
5. Valitse Aino Testinen 000123.
6. Totea, että Eero Esimerkille näytetään kaksi opiskeluoikeutta.
7. Valitse Eerolle Testikoulutus.
8. Kirjaa T02:n kohdalle Lähtötila (palauta ensin), tulos ja havainto.
9. **Päätös:** Kirjaa päätöslokiin päätös ja peruste. Tee tallennuspiste K6:lla.

Seuraavaksi: jono ja VALMIS.

## Tehtävä 6: Palat 3 ja 4 – jono, VALMIS ja seuraava (T20)

Teet palat 3 ja 4 yhdellä kierroksella. Tehtävä tarvitsee osion 05 palan 3.

1. **Kehote (K3):** Kopioi K3 ja täytä aukot palojen 3 ja 4 mukaan. Lähetä.
2. Kirjoita odotusajalla Muistioon omille riveilleen: Aino Testinen, Ville Testaaja, Liisa Kokeilu. Jätä Muistio auki. Täytä T20:n Lähtötila (palauta ensin), Mitä teen ja Odotan.
3. Tarkista muutokset, palauta lähtötila ja käynnistä kuten tehtävässä 4.
4. Avaa simuloitu Wilma. Totea, ettei Aino Testisellä (000123) ole urasuunnitelmaa.
5. Kopioi nimet ja liitä ne sovellukseen nimilistana. Aloita käsittely ja valitse Aino Testinen 000123.
6. **Oma testi:** Avaa jono. Totea, että aktiivisia opiskelijoita on yksi ja jokaisella rivillä on jonon tila sanana päätöksesi mukaan.
7. **Oma testi T20:** Tarkista ja hyväksy Aino Testisen sisältö.
8. Etsi tapaa merkitä Aino valmiiksi ennen Wilma-tallennusta. Sitä ei saa olla.
9. Tee urasuunnitelman Wilma-tallennus. Totea, että se on varmennettu ja Ainon jonon tila on VALMIS.
10. Totea, että Ville Testaaja avautui itsestään eikä mitään ole hyväksytty. Esitiedoista ei näy arvoja, koska hänen lomakkeensa puuttuu.
11. Avaa simuloitu Wilma. Totea, että uusi urasuunnitelma on opiskelijalla 000123. Aino Testisellä (000456) on vain lähtötilan urasuunnitelma.
12. Kirjaa tulos ja havainto T20:n kohdalle.
13. **Päätös:** Kirjaa päätöslokiin päätös ja peruste. Tee tallennuspiste K6:lla.

Seuraavaksi: odottaminen ja pysyvyys.

## Tehtävä 7: Pala 5 – odottaminen ja pysyvyys (T21, tavoite)

1. **Kehote (K3):** Kopioi K3 ja täytä aukot palan 5 mukaan. Lähetä.
2. Täytä odotusajalla T21:n Lähtötila (palauta ensin), Mitä teen ja Odotan.
3. Tarkista muutokset, palauta lähtötila ja käynnistä kuten tehtävässä 4.
4. Liitä tehtävän 6 kolme nimeä. Valitse Aino 000123, hyväksy sisältö ja tee Wilma-tallennus. Ville avautuu.
5. **Oma testi T21:** Yritä siirtää Ville Testaaja odottamaan lisätietoja ilman perustelua. Siirron pitää estyä.
6. Siirrä Ville perustelulla: esitietolomake puuttuu.
7. Totea, että Liisa Kokeilu avautui omilla tiedoillaan eikä mitään ole hyväksytty. Työajassa näkyy ristiriita, koska palautus tyhjensi osion 05 valintasi.
8. Kirjaa tulos ja havainto T21:n kohdalle.
9. **Oma testi:** Sulje sovellus ja käynnistä se uudelleen ilman palautusta. Totea, että jono on tallessa ja Villen perustelu näkyy.
10. **Oma testi T19 (osin):** Tuo `opiskelijalista.csv` uudelleen. Totea, että Aino Testinen (000123) näkyy valmiina eikä hänen käsittelynsä ala alusta. Aino Testinen (000456) ei ole valmis.
11. Kopioi alla oleva lohko. Liitä se agentin kehotekenttään. Lähetä.

```text
Näytä Gitillä, onko testiaineisto/opiskelijalista.csv muuttunut sen jälkeen, kun se tuli tallennuspisteeseen. Älä muuta mitään.
```

12. Avaa CSV Muistiolla ja vertaa sitä tehtävän 4 havaintoosi.
13. Kirjaa T19:n ja T22:n tulokset ja havainnot. Lähtötila on jatka testistä T21.
14. **Päätös:** Kirjaa päätöslokiin päätös ja peruste. Tee tallennuspiste K6:lla.

Seuraavaksi: tarkistat, että osio on valmis.

## Valmis, kun

Vähimmäistavoite:
- Kriteereissä on osio 06 ja vähintään yksi ei saa koskaan -ehto.
- Päätöslokissa ovat jonon tilojen nimet ja päätös jokaisesta tehdystä palasta.
- Esikatselu näyttää etunollat, tyhjän rivin ja virherivin (T18).
- Nimikaima ja kaksi opiskeluoikeutta pysäyttävät, kunnes valitset (T02).
- Aino tuli valmiiksi vasta varmennuksen jälkeen, ja Ville avautui ilman Ainon tietoja (T20).
- Viimeinen tallennuspiste on tehty.

Tavoite:
- Ville odottaa lisätietoja perusteluineen, ja Liisa avautui omilla tiedoillaan (T21).
- Jono säilyy, uudelleentuonti ei avaa valmista Ainoa (T19), eikä `opiskelijalista.csv` ole muuttunut (T22).

## Jos jäät jumiin

Jos etunollat puuttuvat esikatselusta, avaa CSV Muistiolla. Jos agentti on muuttanut tiedostoa, hylkää ja palaa tallennuspisteeseen K7:llä. Muuten korjauta K5:llä.

Jos Aino tulee valmiiksi ennen Wilma-tallennusta, T20 on ei läpi. Korjauta K5:llä ennen palaa 5.

Jos Aino Testisellä (000123) on urasuunnitelma palautuksen jälkeen, sulje ohjelmat ja palauta uudelleen. Jos se ei auta, kerro vetäjälle.

Jos ongelma jatkuu kahden korjausyrityksen jälkeen, katkaise kehä K10:llä, palaa tallennuspisteeseen K7:llä ja kerro vetäjälle.

Jos kello on 12.00 ja pala on kesken, tee tallennuspiste K6:lla viestillä Kesken: [pala] tai palaa edelliseen tallennuspisteeseen K7:llä. Pyydä agenttia merkitsemään pala työlistaan keskeneräiseksi. Vetäjä päättää osion 07 alussa, jatketaanko.

## Seuraava osio

Osio 07 alkaa kello 12.45, ja siinä rakennetaan oppisopimus. Mieti lounaalla, miten tunnistat oikean toimipaikan.
