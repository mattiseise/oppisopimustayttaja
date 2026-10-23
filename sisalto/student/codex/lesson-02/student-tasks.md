# Tehtävät: osio 02 – Määrittely ennen koodia: ohjetiedosto ja työlista

Aika noin 75 min. Tarvitset: Codex-työpöytäsovelluksen, projektikansion, Muistion ja tiedoston `maarittely/oma-kokemus.md`.

Kopioit kehotteet koko lohkona ja käsittelet .md-tiedostot Muistiolla osion 00 tavalla.

## Tehtävä 1: Kirjoita kriteerit, ennen kuin agentti kirjoittaa

1. Avaa Muistio.
2. Kopioi Muistioon alla oleva pohja.

```text
# Hyväksymiskriteerit

Kirjoitan nämä itse ennen kuin agentti rakentaa. Agentti lukee, ei muokkaa.

## Osio 02: ohjetiedosto ja työlista
Hyväksyn, kun:
- [kriteeri]
- [kriteeri]
- [kriteeri]
En hyväksy, jos:
- [kriteeri]
Tarkistan näin:
- [mitä teen ja mitä näen]
Liittyvät testit:
- ei vielä
```

3. Tallenna tiedosto projektikansion juureen osion 00 tavalla. Kirjoita nimi lainausmerkeissä: "HYVAKSYMISKRITEERIT.md".
4. Katso Muistion otsikkoriviltä, että nimi päättyy `.md` eikä `.txt`.
5. Lue tiedostosta `maarittely/oma-kokemus.md` kaksi asiaa, joita ohjelma ei saa tehdä.
6. **Oma kriteeri:** Täytä pohja oman kokemuksesi perusteella. Hyväksyn, kun -kohtaan tulee kolme sääntöä, jotka ohjetiedostossa on oltava.
7. Tallenna tiedosto.
8. Sulje Muistio.
9. **Kehote (K6):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K6. Täytä aukko. Lähetä.

Seuraavaksi: pyydät agentilta suunnitelman ohjetiedostosta.

## Tehtävä 2: Ohjetiedosto suunnitelma ensin

1. Tarkista, että alla olevan kehotteen viimeinen rivi kieltää muutokset ennen hyväksyntääsi.
2. **Kehote (K2):** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukot. Lähetä.

```text
Tehtävä: kirjoita projektikansion juureen ohjetiedosto AGENTS.md kuvauspaketin pohjalta. Käytä alla olevan rungon yhdeksää kohtaa.
Lue ensin kansio maarittely ja HYVAKSYMISKRITEERIT.md:n osio 02. Ohjetiedostoa ja työlistaa ei vielä ole.
Painota erityisesti tätä kuvauspaketin osaa: [yksi osa, jota agentin pitää painottaa erityisesti, ja syy työstäsi].
Tärkein kriteerini: [tärkein kolmesta säännöstäsi].
Kirjoita kohtaan (9) tämä sääntö sanasta sanaan: [oma sääntösi].

Ohjetiedoston runko:
(1) Projekti: Oppisopimustäyttäjä. Määrittely on kansiossa maarittely. Työpajaversio tehdään simuloitua Wilmaa vasten kuvitteellisella aineistolla.
(2) Käyttäjä: hallinnon työntekijä, joka ei ohjelmoi. Vastaa suomeksi ja selkokielellä. Kerro aina, miten tulos tarkistetaan ajamalla sovellusta. Tee tekniset valinnat itse ja kerro ne yhdellä lauseella. Kysy vain, jos valinta muuttaa sitä, mitä käyttäjä näkee tai tekee.
(3) Työtapa: yksi pieni tehtävä kerrallaan, suunnitelma ensin. Älä tee tallennuspistettä pyytämättä. Älä merkitse testejä läpäistyiksi äläkä työlistan tehtäviä valmiiksi ilman käyttäjän testiä. Valmis-ilmoitukseen kuuluu tarkistusohje.
(4) Tietoturva: ei oikeita opiskelijatietoja. Älä pyydä salasanoja tai tunnuksia äläkä tallenna kirjautumis- tai istuntotietoja. Käyttäjä kirjautuu itse näkyvässä selaimessa. Älä avaa Wilmaa tai testi-Wilmaa itse. Sovellus kirjoittaa vain simuloituun Wilmaan ja myöhemmin erikseen sovittuun testi-Wilmaan. Verkkoyhteydet vain asennuksiin.
(5) Tuotteen säännöt: kokoa kuvauspaketista, erityisesti osista 6–10, 15 ja 20–22. Yksi lyhyt sääntö riviä kohden.
(6) Tiedostot, joita et muokkaa: PAATOSLOKI.md, HYVAKSYMISKRITEERIT.md, TESTIT.md:n Tulos-, Havainto- ja Päivä-rivit ja kansio maarittely (vain luku). Kansiota testiaineisto muokkaat vain pyydettäessä.
(7) Tekniikka: kuvauspaketin osan 13 ehdotus ja kehitystila. Valinta vahvistetaan teknisessä kokeilussa. Jos asennus estyy, kerro ennen kiertotietä. Playwright voi käyttää koneen Edgeä. Sovellus ja simuloitu Wilma käynnistyvät ilman agenttia ohjeella KAYNNISTYS.md. Mahdollisimman vähän riippuvuuksia.
(8) Ulkoasu: PRO-värit kuvauspaketin osasta 14. Lukutilat ja jonon tilat näytetään aina myös sanoina. Toimii näppäimistöllä.
(9) Oppijan oma sääntö: sanasta sanaan kehotteesta.

Tee suunnitelma. Kerro, mitkä tiedostot muuttuvat, mitä komentoja ajat ja miten tarkistan tuloksen ilman koodin lukemista.
Älä muuta tiedostoja ennen kuin hyväksyn.
```

3. Lue agentin suunnitelma. Jos siitä puuttuu jokin yhdeksästä kohdasta tai oma sääntösi, korjauta se.
4. Hyväksy suunnitelma kirjoittamalla agentille, että se saa toteuttaa sen.
5. Avaa agenttisovelluksen Git-toiminnoista muuttuneet tiedostot. Totea, että uusi tiedosto on vain `AGENTS.md`. Agentin luettelo on vain apu.

Seuraavaksi: tarkistat ja arvioit, mitä ohjetiedostoon tuli.

## Tehtävä 3: Tarkista ohjetiedosto

1. Avaa `AGENTS.md` Muistiolla.
2. **Oma testi:** Etsi ohjetiedostosta `HYVAKSYMISKRITEERIT.md`:n kolme sääntöäsi.
3. Rastita paperille tarkistuslistan tuotesäännöt, jotka löydät.
4. Lue ohjetiedoston tuotteen säännöt. Merkitse paperille yksi sääntö, joka on kokemuksesi mukaan epätarkka tai väärä. Jos sellaista ei ole, kirjoita, mihin vertasit.
5. Tarkista En hyväksy, jos -ehtosi. Kirjoita paperille, täyttyykö se.
6. Sulje Muistio.
7. Jos mitään ei puutu tai ole väärin, siirry vetäjän kysymyksiin.
8. **Kehote:** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukko. Lähetä.

```text
Lisää tai korjaa ohjetiedostoon AGENTS.md nämä säännöt: [puuttuvat tai korjattavat säännöt omin sanoin].
Älä muuta muuta.
```

9. Avaa agenttisovelluksen Git-toiminnoista muuttuneet tiedostot. Totea, että muuttui vain `AGENTS.md`.
10. Avaa `AGENTS.md` Muistiolla ja totea, että pyytämäsi säännöt ovat siellä.

Tuotesääntöjen tarkistuslista:

- Nimi ei yksin riitä kohdistukseen.
- Palkkaa, työaikaa tai työpaikkaohjaajaa ei arvata.
- Palkalla on aina yksikkö.
- Työpaikkaohjaajaa ja työnantajan edustajaa ei oleteta samaksi.
- Saman yrityksen toimipaikat erotetaan.
- Työpaikka ja työpaikkaohjaaja ennen oppisopimusta, tutkinnon osa ennen näyttösuunnitelmaa.
- Wilma-tallennus varmennetaan uudelleenluvulla.
- VALMIS vasta, kun kaikki valitut pakolliset kirjaukset on varmennettu.

Seuraavaksi: vetäjä kysyy neljä kysymystä, ja sitten kirjaat päätöksen.

## Tehtävä 4: Päätös ohjetiedostosta ja tallennuspiste (commit)

1. Avaa `PAATOSLOKI.md` Muistiolla.
2. **Päätös:** Kirjaa merkintä ohjetiedostosta. Kirjoita perusteeksi omin sanoin, mitä löysit tai mihin vertasit tehtävässä 3. Mainitse vetäjän kysymyksissä lisätyt säännöt.
3. Tallenna tiedosto.
4. Sulje Muistio.
5. Kopioi alla oleva lohko kokonaan. Liitä se agentin kehotekenttään. Lähetä. Pohjan viimeinen rivi on uusi, koska myöhemmin työ tehdään paloina.

```text
Lisää KEHOTEPOHJAT.md:hen K1:n perään alla oleva pohja sellaisenaan. Älä täytä hakasulkeita.

## K2 Suunnitelma ensin
Tehtävä: [tehtävä omin sanoin].
Lue ensin AGENTS.md, TYOLISTA.md ja HYVAKSYMISKRITEERIT.md:n osio [XX].
Tärkein kriteerini: [tärkein kriteeri].
Tee suunnitelma. Kerro, mitkä tiedostot muuttuvat, mitä komentoja ajat ja miten tarkistan tuloksen ilman koodin lukemista.
Älä muuta tiedostoja ennen kuin hyväksyn.
Kun hyväksyn suunnitelman, älä vielä aloita. Annan palat yksi kerrallaan.
```

6. Avaa agenttisovelluksen Git-toiminnoista muuttuneet tiedostot. Totea, että muuttuneet ovat vain `AGENTS.md`, `PAATOSLOKI.md` ja `KEHOTEPOHJAT.md`.
7. **Kehote (K6):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K6. Täytä aukko. Lähetä.

Seuraavaksi: pyydät agentilta työlistan.

## Tehtävä 5: Työlista

Katso ensin lukutekstistä vaiheet 0–7.

1. Tarkista, että alla olevan kehotteen viimeinen rivi kieltää muutokset ennen hyväksyntääsi.
2. **Kehote:** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukko. Lähetä.

```text
Tee projektikansion juureen TYOLISTA.md. Pilko kuvauspaketin vaiheet 0–7 (osat 25 ja 26) pieniksi tehtäviksi riippuvuusjärjestyksessä.
Tee taulukko, jossa on sarakkeet: nro, tehtävä, vaihe, V, T, työpaja / lisä / jatko ja tehtävän tila (avoin / kesken / valmis).
Työpajassa tehdään kuvauspaketin osan 30 ensimmäinen kehityskokonaisuus simuloitua Wilmaa vasten.
Uskon, että tämä vaihe jää jatkoon: [yksi vaihe, jonka uskot jäävän jatkoon, ja syy työstäsi].
Kirjoita tiedoston loppuun luettelo V01–V10, yksi rivi kustakin: toteutustapa työpajassa ja tehtävien numerot tai "jatko + syy".
Merkitse tehtävät avoimiksi. Merkitse tehtävä valmiiksi vasta, kun pyydän sitä testini jälkeen.
Tee suunnitelma. Älä muuta tiedostoja ennen kuin hyväksyn.
```

3. Lue suunnitelma. Tarkista, että siinä ovat taulukko, kaikki vaiheet 0–7 ja luettelo V01–V10.
4. Hyväksy suunnitelma kirjoittamalla agentille, että se saa toteuttaa sen.
5. Avaa agenttisovelluksen Git-toiminnoista muuttuneet tiedostot. Totea, että uusi tiedosto on vain `TYOLISTA.md`.
6. Avaa `TYOLISTA.md` Muistiolla.
7. **Oma testi:** Tarkista järjestys tehtävien numeroista. Työpaikan ja työpaikkaohjaajan tehtävät tulevat ennen oppisopimusta. Tutkinnon osa tulee ennen näyttösuunnitelmaa.
8. Tarkista tiedoston lopun luettelosta, että jokaisella vaatimuksella V01–V10 on rivi.
9. Sulje Muistio.
10. Jos jotain puuttuu tai järjestys on väärä, korjauta se agentilla. Tarkista muutos Git-toiminnoista.

Seuraavaksi: kirjaat päätöksen työlistasta.

## Tehtävä 6: Päätös työlistasta ja tallennuspiste

1. Avaa `PAATOSLOKI.md` Muistiolla.
2. **Päätös:** Kirjaa merkintä työlistasta. Kirjoita perusteeksi omin sanoin, mitä huomasit järjestyksestä ja luettelosta V01–V10.
3. Tallenna tiedosto.
4. Sulje Muistio.
5. **Kehote (K6):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K6. Täytä aukko. Lähetä.
6. Avaa agenttisovelluksen Git-toiminnoista muuttuneet tiedostot. Totea, että luettelo on tyhjä.

Seuraavaksi: tarkistat, että osio on valmis.

## Valmis, kun

- `HYVAKSYMISKRITEERIT.md`:ssä on osion 02 kriteerit omin sanoin.
- `AGENTS.md`:ssä on yhdeksän kohtaa, oma sääntösi, kolme sääntöäsi ja kahdeksan tuotesääntöä.
- `TYOLISTA.md`:ssä vaiheet 0–7 on pilkottu tehtäviksi, ja lopussa on luettelo V01–V10.
- `KEHOTEPOHJAT.md`:ssä ovat K1, K2, K6 ja K7.
- Päätöslokissa on kaksi uutta merkintää.
- Osiossa on tehty kolme tallennuspistettä.
- Agenttisovelluksen Git-toiminnoissa ei ole muuttuneita tiedostoja.

## Jos jäät jumiin

Jos Git-toiminnoissa näkyy muutoksia, ennen kuin hyväksyit suunnitelman, palaa tallennuspisteeseen K7:llä. Tarkista, että kehotteen viimeinen rivi on mukana.

Jos ohjetiedosto on yli kaksi sivua tai kopio kuvauspaketista, korjauta: yksi lyhyt sääntö riviä kohden.

Jos hylkäät ohjetiedoston tai työlistan tai agentti kiertää kehää, pysähdy. Sulje Muistio. Palaa edelliseen tallennuspisteeseen K7:llä. K7 jättää päätöslokin ja kriteerit ennalleen. Kirjaa hylkäys vasta paluun jälkeen.

## Seuraava osio

Osio 03 alkaa kello 12.30. Agentti rakentaa siinä simuloidun Wilman ja kuvitteellisen aineiston.
