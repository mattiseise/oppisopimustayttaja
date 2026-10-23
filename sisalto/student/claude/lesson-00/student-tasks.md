# Tehtävät: osio 00 – Ennen työpajaa: kone, kansio ja turvaraja

Aika noin 60–90 min. Tarvitset: Claude-työpöytäsovelluksen, vetäjän toimittaman kuvauspaketin, Resurssienhallinnan ja Muistion.

Teet tämän osion itsenäisesti viimeistään kolme arkipäivää ennen työpajaa. Lue ensin osion lukuteksti (self-study.md).

Lue materiaalia vetäjän jakamassa muodossa, esimerkiksi verkkosivuna. Muistiossa kehotteiden mukaan kopioituu ylimääräisiä merkkejä.

## Tehtävä 1: Tarkista tilaus ja agenttisovellus

1. Avaa Claude-työpöytäsovellus.
2. Kirjaudu sovellukseen itse, jos se pyytää.
3. Siirry Code-välilehdelle.

Tilauksesi on oltava Pro, Max, Team tai Enterprise. Tilaus toimii, kun agentti vastaa käynnistystestissä (tehtävä 4).

Seuraavaksi: luot kansion, jossa agentti työskentelee.

## Tehtävä 2: Luo projektikansio

Projektikansio on agentin työalue. Kaikki työpajan tiedostot tulevat sinne. Kansio ei saa olla OneDrivessa, koska OneDrive kopioi tiedostot pilveen.

1. Avaa Resurssienhallinta.
2. Luo kansio `C:\dev`, jos sitä ei vielä ole.
3. Luo sen sisään kansio `oppisopimustayttaja`.
4. Käytä varapaikkaa `%USERPROFILE%\dev\oppisopimustayttaja`, jos `C:\`-juureen ei saa luoda kansiota.
5. Tarkista, ettei kansio ole Tiedostot-, Työpöytä- tai OneDrive-kansion sisällä.
6. Valitse Code-välilehdellä tämä kansio kansioksi, jossa agentti työskentelee. Sovellus käyttää siitä nimeä työhakemisto.
7. Tarkista, että sovellus näyttää valitun kansion nimen `oppisopimustayttaja`.

Seuraavaksi: kopioit kuvauspaketin projektikansioon ja luet sen ensimmäisen pääosan.

## Tehtävä 3: Kopioi ja lue kuvauspaketti

Kuvauspaketti on Oppisopimustäyttäjän määrittely. Agentti lukee sitä, mutta ei muuta sitä.

1. Luo projektikansioon alikansio `maarittely`.
2. Kopioi vetäjän toimittama kuvauspaketti kansioon `maarittely`. Käytä teksti- tai Markdown-muotoa, älä Word-tiedostoa.
3. Kopioi samaan kansioon myös tiedosto `03-kenttakartoitus.csv`, jos vetäjä toimitti sen.
4. Lue kuvauspaketin ensimmäinen pääosa, osat 1–12. Voit lukea sen missä muodossa tahansa. Varaa siihen noin 15 minuuttia.
5. Lue osat 6–10 tarkimmin. Tarvitset niitä osiossa 02.

Seuraavaksi: kokeilet, että agentti toimii projektikansiossa.

## Tehtävä 4: Tee käynnistystesti

Testi kertoo, että agentti toimii projektikansiossa ja koneella on tarvittavat ohjelmat. Tässä kehotteessa ei ole aukkoja. Muissa kehotteissa täytät aukot itse.

Kopioit kehotteen aina koko lohkona, ja rivinvaihdot tulevat mukaan. Älä paina Enteriä kesken kehotteen. Se voi lähettää viestin liian aikaisin.

1. Tarkista Code-välilehdellä, että projektikansio on valittuna.
2. Kopioi koko lohko. Liitä se agentin kehotekenttään. Lähetä.

```text
Tarkista, onko tällä koneella Node.js ja Git. Kerro kummankin versio ja komennot, jotka ajoit.
Älä asenna mitään äläkä muuta mitään tiedostoa.
```

3. Lue lupapyyntö, ennen kuin hyväksyt.
4. Hyväksy vain komento, joka kysyy versiota. Jos komento asentaa tai muuttaa jotain, kiellä se.
5. Hyväksy vain tämän kerran. Jos lupapyynnössä on vaihtoehto, joka sallii saman jatkossa kysymättä, älä valitse sitä.
6. Avaa projektikansio Resurssienhallinnassa. Totea, että siellä on edelleen vain kansio `maarittely`.
7. Kirjoita Node.js- ja Git-versiot paperille. Siirrät ne tiedostoon tehtävässä 5.
8. Ilmoita vetäjälle, jos agentti kertoo, että Node.js tai Git puuttuu.

Seuraavaksi: luet turvarajan ja aloitat oman tiedostosi.

## Tehtävä 5: Lue turvaraja ja aloita oma tiedosto

Oma tiedostosi tulee kansioon `maarittely`. Agentti saa lukea sen. Siksi siinä ei saa olla oikeaa opiskelijatietoa.

Opit samalla tallentamaan ja avaamaan .md-tiedoston Muistiolla. Tapa on sama koko työpajan ajan.

1. Lue tietoturvan muistilista osion lukutekstistä.
2. Avaa Muistio.
3. Kopioi Muistioon tämä pohja:

```text
# Oma kokemus

Miksi oikeaa opiskelijatietoa ei anneta agentille:
[yksi lause omin sanoin]

Mitä agentti saa nähdä tässä työpajassa (2–3 asiaa):
- [asia]
- [asia]

Mitä agentti ei saa nähdä koskaan (2–3 asiaa):
- [asia]
- [asia]

Mitä työpajan lopussa on valmiina:
[1–2 lausetta omin sanoin]

Lomakkeet, jotka kirjaan oppisopimuksessa:
[lomakkeet]

Kolme yleisintä virhettä tai hankaluutta:
- [virhe tai hankaluus 1]
- [virhe tai hankaluus 2]
- [virhe tai hankaluus 3]

Kaksi asiaa, joita ohjelma ei saa koskaan tehdä:
- [asia 1]
- [asia 2]

Koneen versiot: Node.js [versio], Git [versio]

Testi-Wilman tilanne:
[vetäjän vastaus tai "ei tiedossa"]
```

4. Valitse Muistion valikosta Tiedosto → Tallenna nimellä.
5. Valitse tallennuspaikaksi kansio `maarittely`.
6. Kirjoita tiedostonimi lainausmerkkeihin: "oma-kokemus.md". Silloin Windows ei lisää nimen loppuun .txt-päätettä.
7. Tallenna.
8. Katso Muistion otsikkoriviltä tai välilehdeltä, että nimi on `oma-kokemus.md` eikä `oma-kokemus.md.txt`.
9. Sulje Muistio.
10. Avaa tiedosto uudelleen näin: avaa Muistio ja vedä `oma-kokemus.md` Resurssienhallinnasta Muistion ikkunaan.
11. Kirjoita pohjan neljä ensimmäistä kohtaa omin sanoin lukutekstin perusteella.
12. Kirjoita kohtaan Koneen versiot käynnistystestin versiot.
13. Tallenna tiedosto.

Avaa .md-tiedosto aina raahaamalla. Kaksoisnapsautus tai Muistion avausikkuna ei välttämättä avaa sitä oikein.

Seuraavaksi: kirjoitat oman kokemuksesi oppisopimuksen kirjaamisesta.

## Tehtävä 6: Kirjoita oma kokemuksesi

Käytät tätä tiedostoa osiossa 02, kun tarkistat agentin säännöt. Kirjoita yleisellä tasolla. Älä kirjoita nimiä, opiskelijanumeroita, yritysten nimiä tai palkkoja. Älä liitä kuvakaappauksia.

Lomakkeista riittävät nimet ja virheestä lyhyt kuvaus. Kirjoita niin kuin selittäisit asiaa uudelle työkaverille.

1. Kirjoita, mitkä lomakkeet kirjaat Wilmaan oppisopimuksessa.
2. Kirjoita kolme yleisintä virhettä tai hankaluutta. Mieti, mikä menee uusiksi, mikä unohtuu ja mikä sekoittuu.
3. Kirjoita kaksi asiaa, joita ohjelma ei saa koskaan tehdä.
4. Lue teksti läpi ja varmista, ettei siinä ole nimiä tai tunnisteita.
5. Tallenna tiedosto.
6. Sulje Muistio.

Seuraavaksi: selvität, onko testi-Wilma käytössä.

## Tehtävä 7: Selvitä testi-Wilman tilanne

1. Kysy vetäjältä sähköpostilla tai Teamsissa, onko testi-Wilma saatu käyttöön.
2. Avaa `oma-kokemus.md` Muistiolla raahaamalla.
3. Kirjoita vastaus kohtaan Testi-Wilman tilanne. Jos et saa vastausta samana päivänä, kirjoita "ei tiedossa". Vetäjä kertoo tilanteen savutestissä.
4. Tallenna tiedosto.
5. Sulje Muistio.

Seuraavaksi: tarkistat, että kaikki on valmiina.

## Valmis, kun

- Claude-työpöytäsovellus avautuu Code-välilehdelle, ja agentti vastasi käynnistystestiin.
- Kansio `C:\dev\oppisopimustayttaja` tai varapaikka on olemassa. Se ei ole OneDrivessa, Tiedostoissa eikä Työpöydällä.
- Kansiossa `maarittely` on kuvauspaketti tekstimuodossa, ja olet lukenut sen osat 1–12.
- Muistion otsikkorivillä näkyy nimi `oma-kokemus.md`, ja tiedosto avautuu raahaamalla.
- `oma-kokemus.md`:ssä on täytetty kohdat Mitä agentti saa nähdä, Mitä agentti ei saa nähdä koskaan ja Mitä työpajan lopussa on valmiina.
- Myös turvarajan lause, lomakkeet, kolme virhettä, kaksi kieltoa, versiot ja testi-Wilman tilanne on kirjattu.
- Tiedostossa ei ole nimiä, tunnisteita eikä kuvakaappauksia.

## Jos jäät jumiin

Jos sovellus, Node.js tai Git puuttuu tai ei asennu, älä muuta koneen asetuksia. Hallitulla koneella asennukset tekee IT. Kerro vetäjälle, mikä puuttuu.

Jos kansio päätyi OneDriveen, Tiedostoihin tai Työpöydälle, luo uusi kansio `C:\dev`:n alle. Valitse se sitten Code-välilehdellä.

Jos sovellus ilmoittaa tilauksesta tai ei päästä Code-välilehdelle, kirjoita ilmoituksen teksti ylös. Kerro se vetäjälle.

Jos agentti pyytää käynnistystestissä lupaa asentaa jotain tai muuttaa tiedostoa, kiellä lupapyyntö. Kerro vetäjälle, mitä agentti yritti tehdä.

Jos Muistion otsikossa näkyy `oma-kokemus.md.txt` tai `oma-kokemus.txt`, tallenna tiedosto uudelleen tehtävän 5 tavalla. Kirjoita nimi lainausmerkeissä. Vääränniminen tiedosto voi jäädä kansioon. Kerro siitä vetäjälle savutestissä.

## Seuraava osio

Kun olet tehnyt tämän osion, vetäjä tekee kanssasi koneellasi lyhyen savutestin. Aluksi käytte yhdessä läpi Valmis, kun -listan.

Osio 01 alkaa työpajan ensimmäisenä päivänä kello 9.00. Lue osioiden 01 ja 02 lukutekstit ennen ensimmäistä päivää, koska työpajassa niihin on vähän aikaa.
