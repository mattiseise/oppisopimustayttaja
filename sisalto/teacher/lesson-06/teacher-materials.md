# Opettajan materiaali: osio 06 – Opiskelijalista ja työjono

## Ajattelukysymys ja tavoitteet (Bloom)

> Ajattelukysymys: Voiko jono avata seuraavan opiskelijan tai kirjoittaa väärälle henkilölle, ja millä testillä sen osoitat?

- Ymmärtää: oppija selittää, miksi nimi ei riitä kohdistukseen.
- Soveltaa: oppija testaa tuonnin ja jonon testeillä T18, T02, T20 ja T21.
- Arvioida: oppija arvioi, voiko jono kirjoittaa väärälle henkilölle tai merkitä keskeneräisen valmiiksi.
- Arvioida: oppija päättää jonon tilojen nimet kuvauspaketin ristiriidan perusteella.

Painotus on testaamisessa. Kattavuus: vaihe 2 osa 2 (tuonti, kohdistus, jono). V10 ja V01 (kohdistus). T02, T18 (osin), T19 (osin), T20, T21 ja T22 (osin). T02 ja T20 kuuluvat vähimmäistavoitteeseen: vähintään kahden opiskelijan jono, jossa VALMIS tulee vasta varmennuksen jälkeen, seuraava avautuu itsestään eikä edellisen hyväksyntä periydy. Vähimmäistavoite: palat 1–4 (oppijan tehtävät 1–6). Tavoite: pala 5 (tehtävä 7: T21, T19, T22). Päivän 2 prioriteetti on osion 05 materiaalin varasuunnitelmassa.

## Aikataulu (minuutit, summa = osion kesto)

| Min | Kello | Sisältö |
|---|---|---|
| 5 | 10.45–10.50 | Kehystys |
| 6 | 10.50–10.56 | Tehtävä 1: uusi keskustelu, K11 ja kriteerit |
| 6 | 10.56–11.02 | Tehtävä 2: jonon tilojen nimet |
| 6 | 11.02–11.08 | Tehtävä 3: K2 ja suunnitelman tarkistus |
| 13 | 11.08–11.21 | Tehtävä 4: pala 1, tuonti ja esikatselu (T18) |
| 13 | 11.21–11.34 | Tehtävä 5: pala 2, kohdistus ja valinta (T02) |
| 20 | 11.34–11.54 | Tehtävä 6: palat 3 ja 4 yhdellä kierroksella, jono ja VALMIS (T20) |
| 6 | 11.54–12.00 | Tehtävä 7 (tavoite) alkaa, tai tallennuspiste "Kesken" |
| 75 | | Yhteensä |

Palat 3 ja 4 tehdään yhdellä K3:lla, koska viisi kierrosta ei mahdu 50 minuuttiin. Pala 5 jää yleensä osion 07 aikaan.

## Ennen osiota

- Osion 05 lopputilanne: tehdyt palat on hyväksytty, ja kesken jääneet on merkitty työlistaan. Jos osion 05 pala 3 on kesken, se tehdään ensin, koska T20 tarvitsee sen. Testikytkimet ovat pois päältä. Päätöslokissa on lupa-asetus tai tarkistustapa.
- Avaa oppijan `testiaineisto/opiskelijalista.csv` Muistiolla. Siinä on viisi kuvitteellista opiskelijaa, etunollat, yksi tyhjä rivi ja virherivi 12A. Nimilistassa ovat Aino Testinen ja Eero Esimerkki. Ville Testaajalta puuttuu esitietolomake.
- CSV on mukana jossakin tallennuspisteessä. Muuten T22:n Git-tarkistuksella ei ole vertailukohtaa.
- Lue KP osat 9, 10 ja 20 sekä osan 14 tilaesimerkki. Tunnet silloin ristiriidan tarkasti.
- Testit alkavat palautuksella (`palauta-lahtotila.cmd`). Se poistaa testien urasuunnitelmat, tyhjentää jonon ja käsittelyt ja jättää Aino Testiselle 000456 lähtötilan urasuunnitelman.

## Ohjaus askel askeleelta

**Kehystys.** Kysy ajattelukysymys. Pyydä oppijaa kertomaan, miten hän nyt käsittelee listan ja mistä hän tietää, kuka on valmis. Vastaus johtaa usein Excel-merkintöihin. Ne ovat hyvä vertailukohta väärinkäsitykselle 3.

**Tehtävä 1.** Ei saa koskaan -kriteeri on osion tärkein. Hyvä esimerkki: "Jono ei saa koskaan kirjoittaa opiskelijalle, jota en ole valinnut, kun nimi on kahdella." Älä anna sitä valmiina. Uusi keskustelu aloitetaan, koska agentti lukee K11:n pyynnöstä ohjetiedoston uudelleen. Säännöt pysyvät silloin tuoreina.

**Tehtävä 2.** KP osa 9: Odottaa tarkoittaa käsittelemätöntä ja Odottaa lisätietoja puutetta. KP osa 20 käyttää sanaa ODOTTAA puutteen merkityksessä. KP osa 14 mainitsee esimerkkeinä ODOTTAA, KÄSITTELYSSÄ ja VALMIS ilman määritelmää. Suositus on osan 9 nimet. Hyväksy myös oppijan omat nimet, jos jokainen sana tarkoittaa yhtä asiaa ja perustelu on oma. Materiaali käyttää osan 9 nimiä joka tapauksessa. Jos oppija valitsee omat nimet, pyydä häntä kirjoittamaan päätöslokiin vastaavuus osan 9 nimiin. Päätös on myös esimerkki osion 02 väärinkäsityksestä "kuvauspaketti on oikeassa kaikessa".

**Tehtävä 3.** Esikatselun aukon hyvä vastaus: virherivi näkyy omana rivinään ja syy kerrotaan, tyhjä rivi näkyy, ja opiskelijanumerot näkyvät etunollineen. Rivi "XLSX ei kuulu tähän" pitää agentin rajattuna. Rivi "Kun hyväksyn suunnitelman, älä aloita" pyytää agenttia odottamaan. Jos agentti silti aloittaa, oppija toimii osion 05 tehtävän 3 askeleen 7 mukaan. Palautusrivi varmistaa, että palautus tyhjentää myös jonon.

**Tehtävä 4.** Oppija avaa CSV:n Muistiolla ennen tuontia. Silloin hän tietää, mitä esikatselussa pitää näkyä. Käsittelyä ei aloiteta CSV:stä. Jono tehdään nimilistasta, koska siinä nimi on ainoa tieto. Jokainen testi alkaa palautuksella, ja oppija kirjaa Lähtötila-rivin.

**Tehtävä 5.** T02:n ydin on askel 4: yritys jatkaa ilman valintaa. Jos sovellus päästää kirjoittamaan, tulos on ei läpi. Korjautus tehdään ennen palaa 3, koska kaikki myöhemmät testit nojaavat oikeaan kohdistukseen.

**Tehtävä 6.** Palat 3 ja 4 yhdellä kierroksella. Askel 4 todistaa, että palautus poisti T05:n urasuunnitelman. Jono on kolmen nimen lista: Aino Testinen, Ville Testaaja ja Liisa Kokeilu. Eero ei ole jonossa, joten hän pysyy puhtaana osion 08 B1:tä varten. Seuraa askelta 8: oppija etsii itse tapaa merkitä Aino valmiiksi ennen Wilma-tallennusta. T20:n toinen osa on Villen tarkistus: hänen esitietolomakkeensa puuttuu, joten jos Villellä näkyy Ainon esitietoarvo, tulos on ei läpi. Mitään ei saa olla hyväksytty. Kolmas osa on simuloidun Wilman tarkistus: uusi urasuunnitelma on opiskelijalla 000123, ei nimikaimalla.

**Tehtävä 7.** T20 ja T21 ovat samaa jonoa. Pala 5 tuo pysyvyyden, joten T20:n jono ei säily palan 5 rakentamisen yli. Siksi oppija palauttaa lähtötilan ja vie Ainon uudelleen VALMIS-tilaan (askel 4), noin 3 min. Sen jälkeen Ville on aktiivinen (T21). Liisan työajassa näkyy ristiriita, koska palautus tyhjensi osion 05 valinnan. Pysyvyys ja T19 jatkavat T21:n jälkeisestä tilanteesta. Valmiiden merkintöjen pitää säilyä (KP osa 10). T22: agentin Git-vastaus on agentin kertomus. Oppijan oma tarkistus on CSV Muistiossa ja Codex-polulla Git-toiminnot.

Oppija pitää hiiren koko osion ajan.

## Polkujen erot (taulukko Claude | Codex)

| Asia | Claude | Codex |
|---|---|---|
| Uusi keskustelu | Uusi istunto Code-välilehdellä | Uusi työsäie samassa projektissa |
| Ohjetiedosto K2:ssa ja K11:ssä | `CLAUDE.md` | `AGENTS.md` |
| Suunnitelma ensin | Suunnittelutila ja K2:n viimeinen rivi. Hyväksyntä osion 05 päätöksen mukaan. | K2:n viimeinen rivi. Hyväksyntä lauseella "Hyväksyn suunnitelman. Älä vielä aloita. Annan ensimmäisen palan seuraavaksi." |
| Agentti aloittaa ennen K3:a | Kiellä lupapyyntö: "Pysähdy. Odota, että annan palan." Automaattisen sallimisen jälkeen pysäytä agentti ja katso muutosnäkymä. | Pysäytä agentti ja tarkista Git-toiminnot. K7 tarvittaessa. |
| Muutosten tarkistus palan jälkeen | Osion 05 päätöksen mukaan: lupapyynnöt ja muutosnäkymä tai pelkkä muutosnäkymä | Git-toimintojen muuttuneet tiedostot pysäytyssäännön mukaan |
| T22 lähtötiedosto | Agentin Git-vastaus ja Muistio | Agentin Git-vastaus, Git-toiminnot ja Muistio |

Sisältö, tehtävät ja testit ovat samat.

## Väärinkäsitykset (vähintään 3)

**Väärinkäsitys 1:** "Nimi riittää, jos se on harvinainen." Harvinainen nimi voi olla kahdella, ja yhdellä ihmisellä voi olla kaksi opiskeluoikeutta. KP osa 20: nimi on hakusyöte, ei kirjoituskohteen tunniste.

**Väärinkäsitys 2:** "Jono saa jatkaa automaattisesti vaikean opiskelijan ohi." Puuttuva tieto ei aiheuta automaattista ohitusta (KP osa 20). Odottaa lisätietoja vaatii oppijan päätöksen ja perustelun. Tarkistettava tallennus pysäyttää jonon, eikä sitä ohiteta siirtämällä opiskelijaa odottamaan.

**Väärinkäsitys 3:** "Excel-tiedostoon voi merkitä valmiit." Alkuperäistä listaa ei muuteta (KP osa 10). Valmis-tieto on sovelluksen jonossa ja Wilmassa. Tuloskopio on lisätavoite, ja sekin on vain tilannekuva, joka ei todista Wilman tallennuksia (KP osa 20).

**Väärinkäsitys 4:** "VALMIS sovelluksessa tarkoittaa, että Wilmassa on kaikki." Työpajassa VALMIS koskee vain urasuunnitelmaa. Kun oppisopimus tulee mukaan osiossa 07, VALMIS vaatii senkin varmennuksen.

## Jumikohdat ja purku (taulukko: oire | todennäköinen syy | purku)

| Oire | Todennäköinen syy | Purku |
|---|---|---|
| Agentti muuttaa lähtö-CSV:tä, esimerkiksi poistaa virherivin | Agentti korjaa testiaineistoa | Hylkää ja K7. Ohjetiedoston kohta 6. Virherivi on testitapaus. |
| Opiskelija merkitään valmiiksi ennen varmennusta | VALMIS on kytketty Wilma-tallennukseen, ei uudelleenlukuun | Ei läpi T20:ssä. K5 ennen palaa 5. |
| Jono ei säily | Jono on vain sovelluksen muistissa | Ei läpi pysyvyystestissä. K5 palassa 5. |
| Etunollat katoavat | CSV avattu ja tallennettu Excelillä tai tunniste luettu lukuna | Oppija kysyy Gitiltä, onko CSV muuttunut. Jos on, K7. Jos ei, K5: tunnisteet tekstinä. |
| Sovellus löytää Aino Testiselle (000123) vanhan urasuunnitelman | Palautusta ei tehty, tai simuloitu Wilma oli auki palautuksen aikana | Sulje ohjelmat ja palauta uudelleen. Kaksoiskappaleen esto toimii oikein. |
| Liisan osion 05 valinta näkyy palautuksen jälkeen | Palautus ei tyhjennä käsittelyjä | Oppija kirjaa havainnon T21:een ja korjauttaa palautuksen K5:llä. T21 ei kaadu tähän. |
| Nimilista tulkitaan yhdeksi nimeksi | Liitetyt rivit luetaan yhtenä | K5: yksi nimi riviä kohden |
| Agentti rakentaa XLSX-tuonnin | Suunnitelma laajeni | Pyydä poistamaan tai palaa tallennuspisteeseen. XLSX on lisätavoite. |
| Agentti aloittaa heti hyväksynnän jälkeen tai rakentaa kaikki palat kerralla | Suunnitelman hyväksyntä tulkittiin toteutusluvaksi | Pysäytä polun tavalla (polkujen erot). K7 tarvittaessa. K3 pala kerrallaan. |

## Varasuunnitelma

Noudata osion 05 Varasuunnitelman prioriteettilistaa. Tarkista tilanne kello 12.00.

Osion 05 pala 3 on kesken: se tehdään ensin, koska T20 tarvitsee tarkistusnäkymän hyväksynnän. Aika otetaan palasta 5.

Päivä 1 jäi kesken, ja osio 05 tehtiin lyhennettynä: osio 06 alkaa silti ajallaan. Tehdään vähimmäistavoite: palat 1–4, T02 ja T20. Jos aika on tiukka, T18:n CSV-osa (tehtävän 4 askeleet 4–5) siirtyy myöhemmäksi. Nimilistan tuonti tehdään, koska jono tarvitsee sen. Pala 5 siirtyy osion 07 aikaan. Osio 07 jää pois.

Aikataulu venyy: T02 ja T20 ensin, koska ne ovat vähimmäistavoitteessa. Sitten pala 5: T21 ja pysyvyys, viimeisinä T19 ja T22. Kesken jääneet tehdään osion 07 aikana. Osiota 06 ei pudoteta.

XLSX ei kuulu osioon. Siihen ei käytetä aikaa, jos CSV ja nimilista ovat kesken.

Agentti kiertää kehää: K10 ja K7. Jos projekti on rikki yli 15 min, pura vetäjän välitila osion 05 lopusta. Oppijan omat tiedostot säilytetään. Oppija kirjaa päätöslokiin, mitä tapahtui.

## Tarkista ennen seuraavaa osiota

- [ ] Päätöslokissa ovat jonon tilojen nimet ja oppijan oma peruste.
- [ ] T02 ja T20 on kirjattu oppijan sanoin Lähtötila-riveineen. Ei läpi -tulokset on korjautettu tai siirretty osion 07 alkuun. Uusinnat ovat omilla riveillään.
- [ ] `opiskelijalista.csv` on ennallaan.
- [ ] Jono säilyy uudelleenkäynnistyksen yli, tai pysyvyys on kirjattu ei läpi -tulokseksi, tai pala 5 on työlistalla keskeneräisenä.
- [ ] Viimeinen tallennuspiste on tehty.
- [ ] Osion 07 laajuus on päätetty prioriteettilistan mukaan ja kirjattu päätöslokiin. Osio 07 on joustokohta.

## Tarkistettavat nimet

- Claude: uuden istunnon aloitus Code-välilehdellä.
- Claude: suunnitelman hyväksynnän vaihtoehdot suunnittelutilassa.
- Claude ja Codex: agentin pysäytys kesken työn.
- Codex: uuden työsäikeen aloitus samassa projektissa.
- Codex: Git-toimintojen näkymä, jossa muuttuneet tiedostot ja tiedostokohtainen muutos näkyvät (T22).
- Windows: tiedoston avaaminen Muistiolla raahaamalla, jos CSV:n oletusohjelma on Excel.
