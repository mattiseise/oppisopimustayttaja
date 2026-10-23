# Osio 02: Määrittely ennen koodia: ohjetiedosto ja työlista

> Ajattelukysymys: Kuvaako ohjetiedosto oikein sen, miten oppisopimus kirjataan, ja mistä sen tiedät?

Agentti kirjoittaa koodia nopeasti. Se kirjoittaa sitä myös silloin, kun se ei tiedä, mitä pitäisi tehdä. Silloin se arvaa. Tässä osiossa estät arvaamisen, ennen kuin ensimmäistäkään koodiriviä on kirjoitettu.

Agentti tekee kuvauspaketista kaksi tiedostoa. Ohjetiedosto kertoo säännöt, joita agentti noudattaa koko ajan. Työlista pilkkoo työn pieniksi tehtäviksi. Sinä tarkistat, että säännöt vastaavat sitä, miten oppisopimus oikeasti kirjataan.

Ennen sitä kirjoitat ensimmäiset hyväksymiskriteerisi. Ne kertovat, milloin hyväksyt agentin työn.

Teet osiossa saman kierroksen kahdesti, ensin ohjetiedostolle ja sitten työlistalle. Kumpikin päättyy omaan tarkistukseen, päätökseen ja tallennuspisteeseen (commit). Näin jokainen hyväksytty tuotos on tallessa ennen seuraavaa.

## Miksi agentille ei sanota "tee oppisopimusohjelma"

Lyhyt pyyntö tuottaa jotain, joka näyttää valmiilta. Agentti täyttää aukot omilla oletuksillaan. Oletukset ovat usein järkeviä. Oppisopimuksessa ne ovat silti vaarallisia.

Katso kahta esimerkkiä. Liisa Kokeilun palkaksi on kirjattu "2 450" ilman yksikköä. Agentti voi päätellä, että kyse on kuukausipalkasta, koska summa näyttää siltä. Kuvauspaketin osa 8 kieltää tämän. Palkan yksikkö tarkistetaan, sitä ei arvata.

Toinen esimerkki tulee Testileipomo Oy:stä. Aino Testisen työpaikkaohjaaja on Maija Mallikas, ja työnantajan edustaja on Kaisa Mallikas. Agentti voi olettaa, että sama henkilö hoitaa molemmat roolit. Kuvauspaketin osa 7 sanoo, että he voivat olla eri henkilöitä. Ohjelma ei saa olettaa heitä samaksi.

Kumpikaan virhe ei näy koodista. Ne näkyvät vasta, kun Wilmassa on väärä tieto. Siksi säännöt kirjoitetaan ennen koodia.

## Kuvauspaketti on lähde

Luit kuvauspaketin ensimmäisen pääosan, osat 1–12, osiossa 00. Tärkeimmät niistä ovat osat 6–10. Osa 6 kertoo, mitä Wilmaan täytetään. Osa 7 kertoo järjestyksen. Osa 8 kertoo, mitä työntekijä tarkistaa. Osat 9 ja 10 kertovat listan käsittelystä ja siitä, milloin opiskelija on valmis. Nämä osat ovat sinun alaasi.

Toinen pääosa on kirjoitettu järjestelmäasiantuntijoille. Kaksi sen osaa koskee myös sinua. Osa 15 sisältää vaatimukset V01–V10 ja osa 28 hyväksymistestit. Niitä ei tarvitse lukea nyt. Agentti käyttää niitä työlistassa, ja sinä katsot niistä tarvittavat rivit myöhemmin. Muut osat ovat teknisiä, eikä sinun tarvitse ymmärtää niitä. Agentti lukee ne.

Kuvauspaketti ei ole virheetön. Siinä voi olla kohtia, joissa sinun kokemuksesi on tarkempi. Kun huomaat sellaisen, kerrot sen agentille ja kirjaat sen päätöslokiin. Agentti ei voi huomata sitä itse, koska sillä ei ole muuta lähdettä kuin kuvauspaketti.

## Ohjetiedosto ja työlista

**Ohjetiedosto** on projektikansion juuressa oleva `CLAUDE.md`. Agentti lukee sen istunnon alussa. Siinä ovat projektin pysyvät säännöt.

Ohjetiedostossa on yhdeksän kohtaa. Ne kertovat projektista, käyttäjästä, työtavasta ja tietoturvasta. Lisäksi niissä ovat tuotteen säännöt, tiedostot, joita agentti ei saa muokata, tekniikka, ulkoasu ja oma sääntösi.

Kaikki kohdat eivät ole yhtä tärkeitä sinulle. Tekniikan agentti valitsee kuvauspaketin ehdotuksen pohjalta. Käyttäjä-kohta kertoo agentille, ettet ohjelmoi. Silloin agentti kertoo jokaisen tuloksen kohdalla, miten tarkistat sen ajamalla sovellusta. Kohta tiedostoista, joita agentti ei muokkaa, suojaa päätöslokisi ja hyväksymiskriteerisi. Suoja toimii vain, jos tiedostojen nimet ovat oikein, esimerkiksi `PAATOSLOKI.md` eikä `PAATOSLOKI.md.txt`. Tärkein kohta sinulle on tuotteen säännöt. Agentti kokoaa ne kuvauspaketista, ja sinä tarkistat ne.

Ohjetiedosto ei valmistu kerralla. Kun huomaat työpajan aikana uuden säännön, lisäät sen. Agentti ei myöskään noudata ohjetiedostoa aina. Siksi tarvitaan testit.

**Työlista** on tiedosto `TYOLISTA.md`. Siinä kuvauspaketin vaiheet 0–7 on pilkottu pieniksi, järjestetyiksi ja tarkistettaviksi tehtäviksi. Vaiheet kuvataan kuvauspaketin osissa 25 ja 26. Lyhyesti ne ovat nämä:

- Vaihe 0: selvitetään, mistä tiedot saadaan ja mihin Wilman kenttiin ne menevät.
- Vaihe 1: kokeillaan koko ketju yhdellä opiskelijalla: tiedot lähteistä, Wilma-tallennus ja uudelleenluku.
- Vaihe 2: ohjelma näyttää puuttuvat ja ristiriitaiset tiedot ja käsittelee opiskelijalistan jonona.
- Vaihe 3: oikea yritys, toimipaikka ja työpaikkaohjaaja löytyvät ilman väärää yhdistämistä.
- Vaihe 4: urasuunnitelma ja HOPS.
- Vaihe 5: näyttösuunnitelmat ja oppisopimus.
- Vaihe 6: häiriötilanteet, tietojen suojaus ja asennuspaketti.
- Vaihe 7: rajattu pilotti, jossa henkilöstö kokeilee ohjelmaa oikeassa työssä.

Työpajassa tehdään osion 00 vähimmäistavoite. Se on vaihe 0 simuloituna, vaihe 1 ja osia vaiheista 2 ja 4. Tavoitteessa mukaan tulee osia vaiheista 3, 5 ja 6. Vaihe 7 on jatkoa.

Yksi työlistan rivi voi näyttää tältä. Tehtävä on urasuunnitelman Wilma-tallennus ja uudelleenluku simuloidussa Wilmassa. Vaihe on 1, vaatimukset V01 ja V04, testi T05. Merkintä on työpaja, ja tehtävän tila on avoin. Rivistä näet, mitä tehdään, mihin vaatimukseen se liittyy ja millä testillä tarkistat sen. Leveää taulukkoa on vaikea lukea Muistiossa. Siksi agentti kirjoittaa tiedoston loppuun myös luettelon V01–V10, yksi rivi kustakin. Tarkistat luettelon, et koko taulukkoa.

Järjestys tulee riippuvuuksista. Työpaikan ja työpaikkaohjaajan pitää olla Wilmassa ennen oppisopimusta. Tutkinnon osan pitää olla opinnoissa ennen näyttösuunnitelmaa. Jos työlista on väärässä järjestyksessä, agentti rakentaa asiat väärässä järjestyksessä.

Jokaisessa tehtävässä on merkintä työpaja, lisä tai jatko. Kahdessa päivässä ei ehdi kaikkea. Työlista näyttää rehellisesti, mitä tehdään nyt ja mitä myöhemmin. Jokaisella vaatimuksella V01–V10 on toteutustapa työpajassa tai merkintä "jatko + syy". Pyydät agenttia merkitsemään tehtävän valmiiksi vasta, kun olet testannut sen itse ja kirjannut tuloksen. Agentti ei merkitse tehtäviä valmiiksi omin päin.

**Pysähdy hetkeksi:** Mikä kuvauspaketin sääntö on työssäsi tärkein, ja mitä tapahtuu, jos ohjelma rikkoo sen?

## Hyväksymiskriteeri

**Hyväksymiskriteeri** on ehto, jonka kirjoitat omin sanoin ennen rakentamista. Sen täyttymisen pitää näkyä. Kriteeri ei ole toive.

Huono kriteeri on "toimii hyvin". Kukaan ei voi tarkistaa sitä. Hyvä kriteeri on: "Urasuunnitelma löytyy uudelleen avattuna oikealta opiskelijalta, ja tavoite-kentässä on sama teksti, jonka hyväksyin." Sen voi tarkistaa avaamalla lomakkeen.

Kirjoitat kriteerit tiedostoon `HYVAKSYMISKRITEERIT.md` osioittain. Agentti lukee tiedoston, mutta ei muokkaa sitä. Jokaisessa osiossa on kolme kohtaa. Hyväksyn, kun -kohta kertoo, mitä pitää näkyä. En hyväksy, jos -kohta kertoo, mikä estää hyväksynnän, vaikka muu toimisi. Tarkistan näin -kohta kertoo, mitä teet ja mitä näet.

Kolmas kohta on tärkein. Jos et osaa kirjoittaa, miten tarkistat, kriteeri on vielä toive.

Kriteeri kirjoitetaan, ennen kuin agentti rakentaa. Jos kirjoitat sen vasta tuloksen nähtyäsi, kirjoitat helposti sen, mitä agentti teki. Silloin kriteeri ei enää tarkista mitään.

Kriteeri ja vaatimus ovat eri asioita. Vaatimus V04 kertoo, että urasuunnitelma täytetään. Kriteeri kertoo, mistä sinä näet, että se on tehty oikein.

Jos et keksi kriteeriä, kysy kaksi kysymystä. Mitä näet, kun se toimii? Mitä ei saa tapahtua?

## Suunnitelma ensin

**Suunnitelma ensin** on työtapa, jossa agentti kertoo ensin, mitä aikoo tehdä. Se ei muuta tiedostoja ennen hyväksyntääsi. Tällä polulla apuna on suunnittelutila (plan mode). Suunnittelutilassa agentti tekee suunnitelman muuttamatta tiedostoja. Vetäjä näyttää, mistä sen saa päälle.

Hyvä suunnitelma on lyhyt. Siinä on luettelo tiedostoista, jotka syntyvät tai muuttuvat, ja ohje siitä, miten tarkistat tuloksen. Jos suunnitelmassa on tiedostoja, joita et pyytänyt, kysy miksi. Suunnitelmasta näet, mitkä tiedostot muuttuvat ja mitä komentoja agentti aikoo ajaa. Jos suunnitelma on väärä, korjaat sen, ennen kuin mitään on tehty. Se on helpompaa kuin korjata valmista.

Kehotepohja K2 pyytää samaa sanoin. Käytät sitä jokaisen isomman tehtävän alussa, myös suunnittelutilan kanssa.

Kun suunnitelma on valmis, sovellus pyytää hyväksyntää. Hyväksynnässä voi olla useita vaihtoehtoja. Osa niistä sallii samalla muutokset automaattisesti istunnon loppuun asti. Älä valitse sellaista. Hyväksy niin, että sovellus kysyy edelleen luvan ennen muutoksia. Tarkista se heti: kun agentti luo tiedoston, sovelluksen pitää kysyä lupaa. Jos lupaa ei kysytä, pysähdy ja kutsu vetäjä. Muuten lupapyyntö, tämän polun tärkein tarkistus, katoaa huomaamatta.

**Pysähdy hetkeksi:** Jos agentti olisi kirjoittanut ohjetiedoston ilman suunnitelmaa, mistä huomaisit, että siitä puuttuu sääntö?

## Esimerkki: sääntö ja kriteeri samasta kokemuksesta

Oma kokemuksesi sanoo, että palkan yksikkö unohtuu usein. Siitä tulee ohjetiedostoon sääntö: "Palkalla on aina yksikkö. Jos yksikkö puuttuu, kirjaus estyy."

Hyväksymiskriteeri tulee samasta kokemuksesta. Hyväksyn ohjetiedoston, kun palkan yksikköä koskeva sääntö on mukana. En hyväksy, jos ohjetiedosto sallii yksikön päättelemisen summasta. Tarkistan näin: avaan `CLAUDE.md`:n Muistiolla ja etsin sanan "yksikkö".

Myöhemmin sama sääntö testataan sovelluksessa. Liisa Kokeilun palkka "2 450" ilman yksikköä ei saa mennä läpi. Aino Testisen palkka 2 450 €/kk menee, koska yksikkö on mukana.

## Yhteenveto

Määrittely tehdään ennen koodia, koska agentti arvaa, jos se ei tiedä. Ohjetiedosto kertoo agentille pysyvät säännöt, ja työlista pilkkoo työn tehtäviksi. Sinä tarkistat molemmat oman kokemuksesi ja kuvauspaketin perusteella. Hyväksymiskriteeri on havaittava ehto, jonka kirjoitat ennen rakentamista.
