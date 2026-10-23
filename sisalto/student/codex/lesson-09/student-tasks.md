# Tehtävät: osio 09 – Jatko: seuraavat askeleet ja pilotti

Aika työpajassa noin 30 min. Sen jälkeen itsenäisesti kerran viikossa 60–90 min. Tarvitset: Codex-työpöytäsovelluksen, projektikansion ja Muistion.

Tehtävät 1–4 teet työpajassa. Tehtävä 5 on työpajan jälkeistä työtä. Agentti ei muista työpajaa, mutta tiedostosi muistavat. Tarkistat muutokset agenttisovelluksen Git-toiminnoista. Agentin oma luettelo on vain apu.

## Tehtävä 1: Tekemättömät testit jatkoon

1. Avaa `TESTIT.md` Muistiolla.
2. Etsi testit, joiden viimeisin tulos on ei testattu tai ei läpi. Jos testillä on uusintarivejä, viimeisin tulos on alimmalla rivillä.
3. Kirjoita niiden kohtaan Työpaja / lisä / jatko: jatko.
4. Tallenna tiedosto ja sulje Muistio.

Seuraavaksi: agentti kokoaa jatkosuunnitelman rungon.

## Tehtävä 2: Jatkosuunnitelman runko

1. Tee tallennuspiste (commit) K6:lla.
2. **Kehote:** Kopioi koko lohko. Liitä se agentin kehotekenttään. Täytä aukko. Lähetä.

```text
Luo projektikansion juureen tiedosto JATKO.md. Älä muuta muita tiedostoja.
Lue ensin AGENTS.md, TYOLISTA.md, TESTIT.md, PAATOSLOKI.md ja KENTAT.md sekä kuvauspaketin osa 29.
Tee tiedostoon viisi otsikkoa:
(1) Avoimet tehtävät: työlistan tehtävät, jotka eivät ole valmiita, numeroineen.
(2) Tekemättömät testit: testit, joiden merkintä on jatko.
(3) Avoimet päätökset: P01–P11, kustakin yksi rivi ja vastuu kuvauspaketin osan 29 mukaan.
(4) Kokeiluhavainnot: päätöslokin ja KENTAT.md:n havainnot teknisestä kokeilusta ja testi-Wilmasta.
(5) Seuraavat askeleet: jätä tyhjäksi. Kirjoitan sen itse.
Lisää avoimiin päätöksiin omat tietoni: [P-tunnukset, joihin voit tuoda omaa tietoa, ja mitä tiedät niistä].
Älä kirjoita ihmisten nimiä. Käytä vain rooleja.
Kerro lopuksi, miten tarkistan tiedoston ilman sinua.
```

3. Lue kuvauspaketin osa 29 sillä aikaa, kun agentti kirjoittaa.
4. Lue jokainen lupapyyntö kolmella kysymyksellä, ennen kuin hyväksyt.
5. Avaa Git-toiminnoista muuttuneet tiedostot. Totea, että vain `JATKO.md` syntyi.
6. Avaa `JATKO.md` Muistiolla.
7. Tarkista, että avoimissa päätöksissä on rivit P01–P11 ja jokaisella vastuu osan 29 mukaan.
8. Valitse kaksi testiä `TESTIT.md`:stä, joiden merkintä on jatko. Totea, että ne ovat myös `JATKO.md`:ssä.
9. Sulje Muistio.

Seuraavaksi: kirjoitat itse seuraavat askeleet.

## Tehtävä 3: Kolme seuraavaa askelta

1. Lue `JATKO.md`:n avoimet tehtävät ja tekemättömät testit.
2. Kopioi alla oleva pohja Muistiolla `JATKO.md`:n kohtaan Seuraavat askeleet kolme kertaa ja numeroi askeleet.
3. **Oma kriteeri:** Täytä kolme askelta omin sanoin.
4. Tarkista, että vähintään yhden askeleen voit tehdä ja tarkistaa itse simuloidussa Wilmassa.
5. Tarkista, että jokaisessa askeleessa, joka tarvitsee muita, rooli on nimetty.
6. Tallenna tiedosto ja sulje Muistio.

```text
### Askel 1
- Mitä teen: [yksi työlistan tehtävä tai testi]
- Hyväksyn, kun: [mitä näen, kun se on tehty]
- Tarkistan näin: [mitä teen ja mitä näen]
- Tarvitsen: [en ketään / IT / Wilma-pääkäyttäjä / Primus-pääkäyttäjä / koulutuksen vastuuhenkilö]
```

Seuraavaksi: sovit seurantatapaamisen.

## Tehtävä 4: Seurantatapaaminen ja viimeinen päätös

1. Sovi vetäjän kanssa ensimmäinen seurantatapaaminen noin kahden viikon päähän.
2. Sovi, miten otat yhteyttä vetäjään tapaamisten välillä, esimerkiksi sähköpostilla tai Teamsissa.
3. Kirjoita `JATKO.md`:n loppuun tapaamisen päivä, yhteydenottotapa ja yksi kysymys, jonka haluat esittää tapaamisessa.
4. **Päätös:** Kirjaa päätöslokiin jatkosuunnitelmasta hyväksyn, korjautan tai hylkään ja peruste omin sanoin.
5. **Kehote (K6):** Kopioi K6 `KEHOTEPOHJAT.md`:stä. Kirjoita viesti omin sanoin. Lähetä.
6. Lue jokainen lupapyyntö kolmella kysymyksellä, ennen kuin hyväksyt.
7. Totea agentin vastauksesta, että `JATKO.md` ja `PAATOSLOKI.md` tulivat mukaan.

Seuraavaksi: työpaja päättyy. Jatkat itsenäisesti tehtävästä 5.

## Tehtävä 5: Itsenäinen työkerta työpajan jälkeen

Tee tämä kerran viikossa 60–90 min. Ensimmäisillä kerroilla teet tekemättömiä simuloidun Wilman testejä.

1. Avaa Codex-työpöytäsovellus ja projektikansio.
2. Aloita uusi työsäie. Pidä auki vain yksi työsäie.
3. **Kehote (K11):** Kopioi K11 `KEHOTEPOHJAT.md`:stä. Kysy aukossa, mikä `JATKO.md`:n seuraavista askeleista on ensimmäinen. Lähetä.
4. Vertaa agentin vastausta `JATKO.md`:hen ja päätöslokin viimeiseen merkintään.
5. Valitse yksi askel. Pienin askel on yksi testi.
6. Tee tallennuspiste K6:lla, jos edellisen jälkeen on muutoksia.
7. Tee ensin työkierros kuten työpajassa, jos askel vaatii rakentamista: **Oma kriteeri**, K2, hyväksyntä, K3 ja muutosten tarkistus Git-toiminnoista. Hyväksy suunnitelma lauseella: Hyväksyn suunnitelman. Älä vielä aloita. Annan ensimmäisen palan seuraavaksi.
8. Palauta lähtötila kaksoisnapsauttamalla `palauta-lahtotila.cmd`, jos testi tekee Wilma-tallennuksen.
9. Käynnistä simuloitu Wilma ja sovellus `KAYNNISTYS.md`:n ohjeella.
10. **Oma testi:** Tee testi ja kirjaa tulos ja havainto `TESTIT.md`:hen. Jos testillä on jo tulos, lisää sen alle rivi: - Uusinta [päivä]: [läpi / ei läpi]. [havainto]
11. Korjauta ei läpi -tulos K5:llä, tarkista muuttuneet tiedostot Git-toiminnoista ja tee testi uudelleen.
12. **Päätös:** Kirjaa päätöslokiin päätös ja peruste.
13. Tee tallennuspiste K6:lla.
14. Merkitse askel tehdyksi `JATKO.md`:hen.
15. Lopeta työkerta tallennuspisteeseen, vaikka askel jäisi kesken. Kirjoita päätöslokiin, mihin jäit.

Seuraavaksi: sama työkerta ensi viikolla seuraavalla askeleella.

## Valmis, kun

- `TESTIT.md`:ssä jokainen tekemätön testi on merkitty jatkoon.
- `JATKO.md`:ssä on viisi otsikkoa, P01–P11 vastuineen ja kolme omaa askeltasi kriteereineen.
- Seurantatapaamisen päivä ja yhteydenottotapa ovat `JATKO.md`:n lopussa.
- Päätöslokissa on viimeinen merkintä, ja tallennuspiste on tehty.

## Jos jäät jumiin

Agentti ei muista eilistä. Se ei ole vika. Aloita aina uudella työsäikeellä ja K11:llä. Jos agentin tilannekatsaus ei vastaa päätöslokia, luota päätöslokiin ja kerro agentille, mikä on oikein.

Pysähdy ja ota yhteys vetäjään sovitulla tavalla, jos kysymys koskee tietoturvaa tai oikeaa Wilmaa. Pysähdy myös, jos ongelma jatkuu kahden korjausyrityksen jälkeen tai et ymmärrä lupapyyntöä. Palaa silloin tallennuspisteeseen K7:llä ja kirjaa tilanne päätöslokiin.

## Seuraava osio

Seuraavaa osiota ei ole. Seuraava yhteinen kerta on seurantatapaaminen. Tuo siihen `JATKO.md`, `TESTIT.md` ja päätösloki.
