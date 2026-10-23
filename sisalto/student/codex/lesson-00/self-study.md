# Osio 00: Ennen työpajaa: kone, kansio ja turvaraja

> Ajattelukysymys: Mitä tietoa agentti saa nähdä, ja mitä se ei saa nähdä koskaan?

Työpajassa rakennat Oppisopimustäyttäjän ensimmäisen version agentin avulla. Oppisopimustäyttäjä on sovellus, joka kokoaa oppisopimuksen tiedot, näyttää ne tarkistettaviksi ja täyttää Wilma-lomakkeet. Sen määrittely on valmiina kuvauspaketissa.

Et opettele ohjelmointia. Agentti kirjoittaa koodin. Sinä omistat säännöt, tarkistukset ja päätökset. Sinä tiedät, miten oppisopimus kirjataan oikein. Agentti ei tiedä.

Tämä osio tehdään ennen työpajaa. Siinä laitat valmiiksi koneen, kansion ja oman aineistosi. Samalla opit turvarajan, joka pätee koko työpajan ajan.

## Mikä agentti on

**Agentti** on tekoälyohjelma, joka lukee ja muokkaa tiedostoja ja ajaa komentoja sille annetussa projektikansiossa. Chat-palvelu vastaa tekstillä. Agentti tekee muutoksia koneellasi. Tässä työpajassa agentti toimii Codex-työpöytäsovelluksessa Windowsilla. Osiossa 01 katsot tarkemmin, mitä agentti tekee ja miten valvot sitä.

## Mitä työpajan lopussa on

Kahdessa päivässä ei valmistu koko sovellus. Rehellinen lopputulos on työpajaversio. Se toimii simuloitua Wilmaa vasten kuvitteellisella aineistolla.

Vähimmäistavoite on tämä. Simuloitu Wilma ja sovellus käynnistyvät ohjeella ilman agenttia. Sovellus avaa selaimen, jossa kirjaudut itse. Se hakee yhden opiskelijan tiedot kuvitteellisista lähteistä ja näyttää ne tarkistettavina. Se tekee urasuunnitelman Wilma-tallennuksen ja lukee lomakkeen uudelleen. Näin näet, tallentuiko tieto oikein. Kahden opiskelijan jonossa seuraava avautuu vasta, kun edellinen on varmennettu. Lisäksi sinulla on omat tiedostosi: säännöt, työlista, päätösloki, hyväksymiskriteerit, testitulokset ja jatkosuunnitelma.

Tavoite on vähimmäistavoitetta laajempi. Silloin sovellus näyttää myös puuttuvat ja ristiriitaiset tiedot. Se tuo opiskelijalistan, erottaa samannimiset opiskelijat ja osaa jättää opiskelijan odottamaan lisätietoja. Se kirjaa oppisopimuksen tiedot oikeassa järjestyksessä. Ulkoasu noudattaa PRO-ilmettä, ja yksi häiriötilanne on testattu. Jos testi-Wilma on käytössä, kokeilet myös sen kenttien lukemista.

Työpajan lopussa ei ole yhteyttä oikeaan Wilmaan. Ei ole oikeita tietoja, valmista asennettavaa ohjelmaa eikä pilottia. Ne ovat jatkoa, ja niihin tarvitaan IT:tä ja pääkäyttäjiä.

## Simuloitu Wilma ja testi-Wilma

**Simuloitu Wilma** on projektikansiossa toimiva kuvitteellinen testisivusto. Se jäljittelee niitä Wilman näkymiä, joita sovellus tarvitsee. Agentti rakentaa sen osiossa 03. Sillä ei ole yhteyttä oikeaan Wilmaan.

Simuloitu Wilma tulee ensin, koska se on turvallinen. Siinä ei ole oikeita tietoja. Sen voi rikkoa tahallaan, ja saman testin voi toistaa yhä uudelleen.

Testi-Wilma on oppilaitoksen Wilma-testiympäristö, jossa on vain testiopiskelijoita. Sitä käytetään vain, jos vetäjä on saanut sen ennakkoon. Silloinkaan siihen ei kirjoiteta työpajassa. Oikea Wilma ei kuulu työpajaan lainkaan.

**Pysähdy hetkeksi:** Mitä tietoa sinulla on koneellasi juuri nyt, jota agentti ei saa nähdä?

## Turvaraja

Turvaraja on yksinkertainen. Oikeaa opiskelijatietoa ei koskaan anneta agentille. Oikeaa tietoa on kaikki, mikä koskee oikeaa opiskelijaa, työpaikkaa tai henkilöä: nimi, tunniste, palkka, haastattelu ja kuvakaappaus. Sitä ei kirjoiteta kehotteeseen eikä projektikansion tiedostoon, eikä sitä näytetä kuvana.

Salasanoja ja tunnuksia ei anneta agentille. Kun sovellus myöhemmin avaa selaimen, kirjaudut siihen itse. Agentti ei näe salasanaasi.

Codexissa agentti toimii hiekkalaatikossa. Oletusoikeuksilla hiekkalaatikko estää kirjoittamisen projektikansion ulkopuolelle ja verkkoyhteydet ilman hyväksyntää. Et valitse täysiä oikeuksia, koska silloin agenttia ei ole rajattu projektikansioon. Kun sovellus kysyy lupaa, luet lupapyynnön, ennen kuin hyväksyt, ja hyväksyt vain sen kerran. Projektikansio on koneesi omassa kansiossa, ei OneDrivessa. Codex voi ehdottaa uudelle projektille Tiedostot-kansiota, joka voi olla OneDrivessa.

Jos testi-Wilmasta saadaan aineistoa, se puhdistetaan kuvauspaketin liitteen A mukaan, ennen kuin agentti näkee sen. Jos epäilet, että jotain vuoti, pysähdy ja kerro vetäjälle.

Tietoturvan muistilista:

- Ei oikeaa opiskelijatietoa agentille: ei kehotteeseen, tiedostoon eikä kuvaan.
- Ei salasanoja eikä tunnuksia agentille.
- Kirjaudut itse näkyvässä selaimessa.
- Lue lupapyyntö ennen hyväksymistä.
- Älä valitse täysiä oikeuksia.
- Oikea Wilma ei kuulu työpajaan.
- Testi-Wilmasta saatu aineisto puhdistetaan liitteen A mukaan ennen agenttia.
- Projektikansio ei ole OneDrivessa.
- Epäilet tietovuotoa: pysähdy ja kerro vetäjälle.

## Sinun osaamisesi on raaka-aine

Agentti osaa kirjoittaa koodia. Se ei tiedä, mikä oppisopimuksen kirjauksessa menee käytännössä väärin. Sinä tiedät. Tiedät, missä järjestyksessä lomakkeet täytetään, mitkä kentät sekoittuvat ja mitä ei saa koskaan arvata.

Tämän osion tehtävissä kirjoitat tiedoston `oma-kokemus.md`. Siihen tulevat lomakkeet, jotka kirjaat, kolme yleisintä virhettä ja kaksi asiaa, joita ohjelma ei saa koskaan tehdä. Osiossa 02 vertaat agentin kirjoittamia sääntöjä tähän tiedostoon. Ilman sitä et voi tarkistaa, ovatko säännöt oikein.

Luet tässä osiossa myös kuvauspaketin ensimmäisen pääosan. Kuvauspaketissa on kaksi pääosaa, ja ne jakautuvat numeroituihin kohtiin 1–31. Materiaalissa "kuvauspaketin osa 8" tarkoittaa kohtaa 8. Ensimmäinen pääosa, osat 1–12, on kirjoitettu hallinnon työntekijälle. Vertaa sitä lukiessasi omaan työhösi. Toinen pääosa on teknistä, ja sen lukee agentti.

**Pysähdy hetkeksi:** Mikä kirjauksen kohta vie sinulta eniten aikaa tai menee useimmin uusiksi?

## Esimerkki: mitä agentti saa nähdä

Työpajassa käsittelet esimerkiksi Aino Testista. Hänen opiskelijanumeronsa on 000123, ja hän opiskelee Testikoulutuksessa. Hänen työpaikkansa on Testileipomo Oy, ja työpaikkaohjaaja on Maija Mallikas. Kaikki nämä on keksitty. Agentti saa nähdä ne, koska ne eivät koske ketään oikeaa ihmistä.

Kuvittele, että kopioisit kehotteeseen oikean haastattelun ja vaihtaisit siitä vain nimen. Palkka, työtehtävät ja työpaikka paljastaisivat henkilön silti. Se on oikeaa opiskelijatietoa. Agentti ei saa nähdä sitä edes muokattuna.

Sama koskee omaa kokemustasi. Voit kirjoittaa, että palkan yksikkö unohtuu usein. Et kirjoita, kenen palkasta oli kyse.

## Yhteenveto

Työpajassa agentti kirjoittaa koodin, ja sinä omistat säännöt ja päätökset. Lopputulos on työpajaversio, joka toimii simuloitua Wilmaa vasten kuvitteellisella aineistolla. Agentti saa nähdä kuvauspaketin, kuvitteellisen aineiston ja oman kokemuksesi ilman tunnistetietoja. Se ei saa koskaan nähdä oikeaa opiskelijatietoa, salasanoja eikä tunnuksia.
