# Vibekoodaus-työpaja: Oppisopimustäyttäjä

Tämä on kahden päivän työpaja. Siinä ohjelmointia osaamaton rakentaa agentin avulla oikean työkalun, Oppisopimustäyttäjän. Sovellus kokoaa oppisopimuksen tiedot, näyttää ne tarkistettaviksi ja täyttää Wilma-lomakkeet. Paketti on samalla demo siitä, miten tekoälyllä tehdään aito työtä helpottava työkalu.

Agentti kirjoittaa koodin. Oppija omistaa säännöt, tarkistukset ja päätökset.

## Kenelle

Oppija on hallinnon työntekijä, joka tuntee oppisopimusprosessin ja Wilman kirjaukset. Ohjelmointia ei tarvitse osata. Vetäjä tekee ennakkovalmistelut ja ohjaa työpajan paikan päällä.

## Valitse polku

Polkuja on kaksi: Claude (Claude-työpöytäsovelluksen Code-välilehti) ja Codex (Codex-työpöytäsovellus Windowsille). Valitse se, johon sinulla tai organisaatiollasi on tilaus. Molemmat tuottavat saman tuotteen samoilla vaiheilla ja hyväksymiskriteereillä. Lue vain oman polkusi kansiota.

## Näin luet materiaalia

Lue materiaalia muotoiltuna, esimerkiksi vetäjän jakamana verkkosivuna tai Markdown-esikatselussa. Älä lue sitä Muistiossa. Kehotelohkot kopioidaan agentille sellaisinaan, ja Muistiosta mukaan tulee ylimääräisiä merkkejä.

## Ennakkovaatimukset

- Tilaus: Claude Pro, Max, Team tai Enterprise, tai ChatGPT-tilaus, jossa Codex on mukana.
- Node.js (LTS) ja Git for Windows. Hallitulla koneella ne asentaa IT.
- Projektikansio `C:\dev\oppisopimustayttaja`. Ei OneDrivessa, Tiedostoissa eikä Työpöydällä.
- Testi-Wilma on valinnainen. Ilman sitä koko työpaja tehdään simuloidussa Wilmassa.

Vetäjä lähettää IT-pyynnön 4 viikkoa ennen työpajaa. Pyynnön sisältö on vetäjän osiossa 00.

## Rakenne

- `student/claude/`: oppija, Claude-polku
- `student/codex/`: oppija, Codex-polku
- `teacher/`: vetäjä, molemmat polut

Jokaisessa on kansiot `lesson-00`–`lesson-09`. Oppijan osiossa on `self-study.md` (lukuteksti), `student-tasks.md` (tehtävät) ja `vocabulary.md` (sanasto). Vetäjän osiossa on `teacher-materials.md` ja joissakin myös `teacher-led-tasks.md`. `teacher/TARKISTETTAVAT-NIMET.md` kokoaa käyttöliittymän nimet, jotka vetäjä tarkistaa harjoitusajossa.

| Osio | Nimi | Aika |
|---|---|---|
| 00 | Ennen työpajaa: kone, kansio ja turvaraja | itsenäisesti 60–90 min, viimeistään 3 arkipäivää ennen |
| 01 | Agentti ei ole chat: ensimmäinen tehtävä ja tallennuspiste | päivä 1, 9.00–10.15 |
| 02 | Määrittely ennen koodia: ohjetiedosto ja työlista | päivä 1, 10.30–11.45 |
| 03 | Simuloitu Wilma ja kuvitteellinen aineisto | päivä 1, 12.30–13.45 |
| 04 | Ensimmäinen varmennettu tallennus | päivä 1, 14.00–16.00 |
| 05 | Lähteet, puutteet ja ristiriidat | päivä 2, 9.00–10.30 |
| 06 | Opiskelijalista ja työjono | päivä 2, 10.45–12.00 |
| 07 | Oppisopimus ja sen edellytykset (joustokohta) | päivä 2, 12.45–14.15 |
| 08 | Hyväksymistestit ja häiriötilanne | päivä 2, 14.30–15.45 |
| 09 | Jatko: seuraavat askeleet ja pilotti | päivä 2, 15.45–16.15 ja itsenäisesti 60 min |

## Aloitus

Aloita osiosta 00: [Claude-polku](student/claude/lesson-00/self-study.md) tai [Codex-polku](student/codex/lesson-00/self-study.md). Tee se itsenäisesti ennen työpajaa. Lue ensin `self-study.md` ja tee sitten `student-tasks.md`.

## Turvaraja

Oikeaa opiskelijatietoa ei koskaan anneta agentille: ei kehotteeseen, tiedostoon eikä kuvaan. Salasanoja ja tunnuksia ei anneta agentille. Oppija kirjautuu itse näkyvässä selaimessa. Oikea Wilma ei kuulu työpajaan.

## Mitä työpajan lopussa on

Kahdessa päivässä ei valmistu koko sovellus. Rehellinen lopputulos on työpajaversio. Se toimii simuloitua Wilmaa vasten kuvitteellisella aineistolla.

Vähimmäistavoite on tämä. Simuloitu Wilma ja sovellus käynnistyvät ohjeella ilman agenttia. Sovellus avaa selaimen, jossa kirjaudut itse. Se hakee yhden opiskelijan tiedot kuvitteellisista lähteistä ja näyttää ne tarkistettavina. Se tekee urasuunnitelman Wilma-tallennuksen ja lukee lomakkeen uudelleen. Näin näet, tallentuiko tieto oikein. Kahden opiskelijan jonossa seuraava avautuu vasta, kun edellinen on varmennettu. Lisäksi sinulla on omat tiedostosi: säännöt, työlista, päätösloki, hyväksymiskriteerit, testitulokset ja jatkosuunnitelma.

Tavoite on vähimmäistavoitetta laajempi. Silloin sovellus näyttää myös puuttuvat ja ristiriitaiset tiedot. Se tuo opiskelijalistan, erottaa samannimiset opiskelijat ja osaa jättää opiskelijan odottamaan lisätietoja. Se kirjaa oppisopimuksen tiedot oikeassa järjestyksessä. Ulkoasu noudattaa PRO-ilmettä, ja yksi häiriötilanne on testattu. Jos testi-Wilma on käytössä, kokeilet myös sen kenttien lukemista.

Yhteys oikeaan Wilmaan, oikeat tiedot, asennettava ohjelma ja pilotti ovat jatkoa.

## Projektikansioon syntyvät tiedostot

Tiedosto esitellään osiossa, jossa sitä käytetään ensimmäisen kerran. Sen jälkeen se elää projektikansiossa ja jää oppijalle jatkoon. Nuoli tarkoittaa, että tiedostoa täydennetään myöhemmissä osioissa.

| Tiedosto tai kansio | Osio |
|---|---|
| `maarittely/` (kuvauspaketti, mahdollinen `03-kenttakartoitus.csv`) | 00 |
| `maarittely/oma-kokemus.md` | 00 |
| `TYOKORTTI.md` | 01 |
| `KEHOTEPOHJAT.md` | 01 → 04 |
| `PAATOSLOKI.md` | 01 |
| `HYVAKSYMISKRITEERIT.md` | 02 |
| `CLAUDE.md` (Claude) tai `AGENTS.md` (Codex) | 02 |
| `TYOLISTA.md` | 02 |
| `simuloitu-wilma/` | 03 → 08 |
| `testiaineisto/` | 03 |
| `testiaineisto/wilma-lahtotila.json` | 03 → 07 |
| `kaynnista-wilma.cmd` | 03 |
| `palauta-lahtotila.cmd` | 03 → 04 |
| `KAYNNISTYS.md` | 03 → 04 |
| `KENTAT.md` | 03 → 08 |
| `TESTIT.md` | 03 |
| `kaynnista-sovellus.cmd` | 04 |
| `JATKO.md` | 09 |
