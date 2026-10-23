# Tehtävät: osio 01 – Agentti ei ole chat: ensimmäinen tehtävä ja tallennuspiste

Aika noin 75 min. Tarvitset: Claude-työpöytäsovelluksen Code-välilehden, projektikansion `C:\dev\oppisopimustayttaja`, Resurssienhallinnan ja Muistion.

Lue ensin osion lukuteksti (self-study.md), jos et lukenut sitä etukäteen. Kopioit kehotteet aina koko lohkona, kuten osiossa 00. Tallennat ja avaat .md-tiedostot Muistiolla osion 00 tavalla.

## Tehtävä 1: Ensimmäinen rajattu tehtävä

1. Avaa Claude-työpöytäsovelluksen Code-välilehti.
2. Valitse kansioksi projektikansio `C:\dev\oppisopimustayttaja`.
3. **Kehote (K1):** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukko sillä, mitä haluat ohjelmasta erityisesti tietää. Lähetä.

```text
Lue kansiossa maarittely oleva kuvauspaketti. Älä muuta mitään tiedostoa.
Kerro viidellä lauseella suomeksi, mitä Oppisopimustäyttäjä tekee.
Kerro erityisesti [mitä haluat ohjelmasta tietää].
Kerro lopuksi, mitä et löytänyt kuvauspaketista.
```

4. **Oma testi:** Lue tiivistelmä lause kerrallaan ja vertaa sitä omaan tietoosi.
5. Kirjoita paperille yksi asia, jonka agentti ilmaisi väärin, epätarkasti tai jätti pois.

Seuraavaksi: annat agentille tehtävän, joka muuttaa tiedostoja.

## Tehtävä 2: Työkortti ja kehotepohjat

Työkortti on muistilista koko työpajaan. Kehotepohjat ovat kehotteita, joiden aukot täytät myöhemmin itse. Alla olevissa lohkoissa on sekä pyyntö että tiedoston teksti. Älä täytä niiden hakasulkeita.

1. Kopioi työkortin lohko kokonaan. Liitä se agentin kehotekenttään. Lähetä.
2. Kuuntele, kun vetäjä lukee lupapyynnön ääneen kolmella kysymyksellä: Mikä? Missä? Miksi?
3. Hyväksy lupapyyntö vain tämän kerran, kun kaikki kolme kysymystä saavat vastauksen.
4. Kopioi kehotepohjien lohko kokonaan. Liitä se agentin kehotekenttään. Lähetä.
5. Lue tämä lupapyyntö itse ääneen kolmella kysymyksellä, ennen kuin hyväksyt.
6. Avaa projektikansio Resurssienhallinnassa. Totea, että siellä on vain kansio `maarittely` sekä tiedostot `TYOKORTTI.md` ja `KEHOTEPOHJAT.md`.
7. Avaa `TYOKORTTI.md` Muistiolla samalla tavalla kuin osiossa 00: avaa Muistio ja vedä tiedosto sen ikkunaan.
8. Tarkista, että kaikki viisi osaa ovat mukana.
9. Sulje Muistio.

Työkortin lohko:

```text
Luo projektikansion juureen tiedosto TYOKORTTI.md. Kopioi siihen alla oleva teksti sellaisenaan. Älä muuta muita tiedostoja.

# Työkortti

## (1) Työkierros
Tallennuspiste → kriteeri → suunnitelma → agentti tekee → tarkistan muutokset → ajan ja testaan itse → päätös → tallennuspiste.
Yksi pieni tehtävä kerrallaan.

## (2) Lupapyyntö: kolme kysymystä
- Mikä? Mikä tiedosto tai komento?
- Missä? Onko se projektikansion sisällä?
- Miksi? Liittyykö se siihen, mitä pyysin?
Jos jokin jää epäselväksi, pyydän agenttia selittämään ennen kuin hyväksyn.
Hyväksyn vain tämän kerran. En valitse vaihtoehtoa, joka sallii saman jatkossa kysymättä.

## (3) Ennen kuin hyväksyn
- Luin lupapyynnöt ja katsoin muutosnäkymästä, mitä muuttui.
- Ajoin sovelluksen ja näin tuloksen itse.
- Kävin kriteerini läpi yksi kerrallaan.
- Kokeilin vähintään yhtä tapausta, jonka pitää pysähtyä.
- Muuttui vain se, mitä pyysin.
- Kirjasin oman havainnon TESTIT.md:hen.
- Kirjasin päätöksen.
- Teen tallennuspisteen vasta hyväksynnän jälkeen.

## (4) Tietoturva
- Ei oikeaa opiskelijatietoa agentille: ei kehotteeseen, tiedostoon eikä kuvaan.
- Ei salasanoja eikä tunnuksia agentille.
- Kirjaudun itse näkyvässä selaimessa.
- Luen lupapyynnön ennen hyväksymistä.
- En salli kaikkea automaattisesti.
- Oikea Wilma ei kuulu työpajaan.
- Testi-Wilmasta saatu aineisto puhdistetaan kuvauspaketin liitteen A mukaan ennen agenttia.
- Projektikansio ei ole OneDrivessa.
- Epäilen tietovuotoa: pysähdyn ja kerron vetäjälle.

## (5) Kun olen jumissa
- Annan virheilmoituksen agentille sellaisenaan.
- Jos ongelma on jäljellä kahden korjausyrityksen jälkeen, katkaisen kehän ja palaan tallennuspisteeseen.
- Kun hylkään, suljen Muistion, palaan ensin ja kirjaan päätöksen sitten.
- Pyydän vetäjän apuun.
```

Kehotepohjien lohko:

```text
Luo projektikansion juureen tiedosto KEHOTEPOHJAT.md. Kopioi siihen alla oleva teksti sellaisenaan. Älä täytä hakasulkeita. Älä muuta muita tiedostoja.

# Kehotepohjat

Täytän hakasulkeissa olevat aukot itse ennen lähettämistä.

## K1 Tutustu, älä muuta
Lue [mitä luetaan]. Älä muuta mitään tiedostoa.
Kerro [vastauksen muoto ja pituus] suomeksi.
Kerro erityisesti [mitä haluan tietää].
Kerro lopuksi, mitä et löytänyt.

## K6 Tallennuspiste
Tee tallennuspiste. Viesti: [mitä nyt toimii, omin sanoin].
Näytä sen jälkeen, mitkä tiedostot tulivat mukaan.

## K7 Palaa tallennuspisteeseen
Haluan palata tallennuspisteeseen [tallennuspisteen viesti].
Älä palauta tiedostoja PAATOSLOKI.md, HYVAKSYMISKRITEERIT.md ja TESTIT.md.
Kerro ensin, mitkä muutokset katoavat. Älä tee mitään ennen kuin vahvistan.
```

Seuraavaksi: aloitat päätöslokin.

## Tehtävä 3: Päätösloki

Päätösloki on sinun tiedostosi, ja kirjoitat sen itse.

1. Avaa Muistio.
2. Kopioi Muistioon alla oleva pohja.
3. Tallenna tiedosto projektikansion juureen osion 00 tavalla. Kirjoita nimi lainausmerkeissä: "PAATOSLOKI.md".
4. Katso Muistion otsikkoriviltä, että nimi on `PAATOSLOKI.md` eikä `PAATOSLOKI.md.txt`.
5. **Päätös:** Kirjaa merkintä 1 tehtävän 1 tiivistelmästä. Valitse hyväksyn, korjautan tai hylkään. Kirjoita peruste omin sanoin paperille kirjoittamasi havainnon pohjalta.
6. Tallenna tiedosto.
7. Sulje Muistio.

```text
# Päätösloki

Kirjoitan tämän itse. Agentti ei muokkaa tätä tiedostoa.

## Merkintä 1
- Päivä ja osio: [päivä], osio 01
- Tuotos: [mitä agentti teki]
- Päätös: [hyväksyn / korjautan / hylkään]
- Peruste: [yksi peruste omin sanoin]
- Tallennuspisteen viesti: [viesti tai "ei vielä"]
```

Kopioi merkinnän rivit uudeksi merkinnäksi aina, kun kirjaat uuden päätöksen.

Seuraavaksi: otat Gitin käyttöön ja teet ensimmäisen tallennuspisteen (commit).

## Tehtävä 4: Ensimmäinen tallennuspiste

Tallennuspiste (commit) on Gitillä tehty nimetty välitila projektikansiosta. Git toimii vain koneellasi.

1. Kysy vetäjältä, mitä nimeä ja sähköpostia käytät Gitissä.
2. **Kehote (K6):** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukot. Kirjoita viesti omin sanoin: mitä projektikansiossa nyt on. Lähetä.

```text
Ota Git käyttöön tässä projektikansiossa. Käytä vain tässä projektissa nimeä [sovittu nimi] ja sähköpostia [sovittu sähköposti].
Tee tallennuspiste. Viesti: [mitä nyt toimii, omin sanoin].
Näytä sen jälkeen, mitkä tiedostot tulivat mukaan.
```

3. Lue jokainen lupapyyntö kolmella kysymyksellä, ennen kuin hyväksyt. Hyväksy vain tämän kerran.
4. Tarkista agentin vastauksesta, että mukana ovat `TYOKORTTI.md`, `KEHOTEPOHJAT.md`, `PAATOSLOKI.md` ja kansio `maarittely`.

Seuraavaksi: kokeilet, miten tallennuspisteeseen palataan.

## Tehtävä 5: Palaa tallennuspisteeseen

Kokeilet paluuta pienellä muutoksella.

1. Katso, kun vetäjä rikkoo tiedoston omalla koneellaan ja palaa tallennuspisteeseen.
2. Kopioi koko lohko. Liitä se agentin kehotekenttään. Lähetä.

```text
Poista TYOKORTTI.md:stä viimeinen rivi. Älä muuta muuta.
```

3. Hyväksy lupapyyntö vain tämän kerran, kun se koskee vain tiedostoa `TYOKORTTI.md`.
4. Katso muutosnäkymästä, mikä rivi poistui.
5. Avaa `TYOKORTTI.md` Muistiolla ja totea, että rivi puuttuu.
6. Sulje Muistio. Se suljetaan aina ennen paluuta.
7. **Kehote (K7):** Kopioi koko lohko. Liitä se agentin kehotekenttään. Kirjoita aukkoon tehtävän 4 tallennuspisteen viesti. Lähetä.

```text
Haluan palata tallennuspisteeseen [tallennuspisteen viesti].
Älä palauta tiedostoja PAATOSLOKI.md, HYVAKSYMISKRITEERIT.md ja TESTIT.md.
Kerro ensin, mitkä muutokset katoavat. Älä tee mitään ennen kuin vahvistan.
```

8. Lue agentin vastaus. Siinä pitää mainita vain poistettu rivi.
9. Vahvista paluu kirjoittamalla agentille: "Kyllä, palaa."
10. Lue lupapyyntö kolmella kysymyksellä, ennen kuin hyväksyt.
11. Avaa `TYOKORTTI.md` Muistiolla ja totea, että rivi on palannut.
12. Sulje Muistio.

Seuraavaksi: kirjaat, mitä paluu osoitti.

## Tehtävä 6: Päätös ja toinen tallennuspiste

1. Avaa `PAATOSLOKI.md` Muistiolla.
2. **Päätös:** Kirjaa merkintä 2 agentin tekemästä paluusta. Kirjoita perusteeksi omin sanoin, mitä näit.
3. Kirjoita kohtaan Tallennuspisteen viesti se viesti, jonka annat seuraavaksi.
4. Tallenna tiedosto.
5. Sulje Muistio.
6. **Kehote (K6):** Avaa `KEHOTEPOHJAT.md` Muistiolla. Kopioi K6 ja liitä se agentin kehotekenttään. Täytä aukko samalla viestillä kuin päätöslokissa. Lähetä.
7. Lue lupapyyntö kolmella kysymyksellä, ennen kuin hyväksyt.
8. Kopioi koko lohko. Liitä se agentin kehotekenttään. Lähetä.

```text
Näytä tallennuspisteiden viestit. Älä muuta mitään.
```

9. Totea agentin vastauksesta, että tallennuspisteitä on kaksi.

Seuraavaksi: tarkistat, että osio on valmis.

## Valmis, kun

- Projektikansiossa ovat `TYOKORTTI.md`, `KEHOTEPOHJAT.md` (K1, K6 ja K7) ja `PAATOSLOKI.md`.
- Päätöslokissa on kaksi merkintää, ja perusteet ovat omin sanoin.
- Agentti näytti tehtävässä 6 kaksi tallennuspistettä.
- Kokeilit paluuta, ja poistettu rivi palasi tiedostoon `TYOKORTTI.md`.

## Jos jäät jumiin

Jos agentti kertoo, ettei Gitiä löydy, kerro vetäjälle. Jatka sillä välin tehtäviä 1–3.

Jos agentti kysyy nimeä tai sähköpostia, tarkista, että tehtävän 4 kehotteen ensimmäinen rivi on mukana. Käytä vetäjän kanssa sovittuja tietoja.

Jos et löydä tiedostoa Resurssienhallinnasta, tarkista, että katsot kansiota `C:\dev\oppisopimustayttaja`.

Jos agentti tekee enemmän kuin pyysit, älä hyväksy enempää. Pyydä agenttia selittämään, mitä se teki. Sulje Muistio ja palaa tarvittaessa tallennuspisteeseen K7:llä.

Jos et ymmärrä lupapyyntöä, älä hyväksy sitä. Pyydä agenttia selittämään se omin sanoin tai kysy vetäjältä.

## Seuraava osio

Osio 02 alkaa kello 10.30. Siinä agentti kirjoittaa ohjetiedoston ja työlistan, ja sinä tarkistat niiden säännöt. Tarvitset tiedoston `maarittely/oma-kokemus.md`.
