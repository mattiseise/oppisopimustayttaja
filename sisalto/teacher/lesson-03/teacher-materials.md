# Opettajan materiaali: osio 03 – Simuloitu Wilma ja kuvitteellinen aineisto

## Ajattelukysymys ja tavoitteet (Bloom)

> Ajattelukysymys: Kattaako kuvitteellinen aineisto ne tilanteet, joissa oikea kirjaus menee helpoimmin väärin?

- Ymmärtää: oppija selittää, mitä simuloitu Wilma todistaa ja mitä ei.
- Luoda: oppija määrittelee testitapaukset omasta kokemuksestaan.
- Analysoida: oppija vertaa simuloidun lomakkeen kenttiä omaan tietoonsa oikeasta Wilmasta.
- Arvioida: oppija arvioi kuvitteellisen aineiston uskottavuuden ja turvallisuuden.

Painotus on testaamisessa. Kattavuus: vaihe 0 simuloituna (kenttäkartoitus, testitunnukset, kuvitteellinen aineisto, testitapaukset). Osio on päivän 1 kriittistä polkua. Ilman simuloitua Wilmaa ja `TESTIT.md`:tä osiota 04 ei voi aloittaa.

## Aikataulu (minuutit, summa = osion kesto)

| Min | Kello | Sisältö |
|---|---|---|
| 5 | 12.30–12.35 | Osion 02 katselmoinnin kysymykset 4 ja 6. Kesken jäänyt työlista (tehtävän 1 askel 1). |
| 6 | 12.35–12.41 | Kehystys: ajattelukysymys ja se, mitä simuloitu Wilma ei todista |
| 8 | 12.41–12.49 | Tehtävä 1: tapaukset, kriteerit ja tallennuspiste |
| 26 | 12.49–13.15 | Tehtävä 2: simuloitu Wilma, käynnistystiedostot ja palautus (K2, K3, oma testi, päätös, tallennuspiste) |
| 12 | 13.15–13.27 | Tehtävä 3: testiaineisto ja K8 |
| 9 | 13.27–13.36 | Tehtävä 4: `KENTAT.md` ja oppijan huomiot |
| 9 | 13.36–13.45 | Tehtävä 5: `TESTIT.md`-runko ja O01:n tulos |
| 75 | | Yhteensä |

Aloittelijalle tehtävä 2 vie arviolta 30–35 min. Päätöskohta on kello 13.15 (varasuunnitelma).

## Ennen osiota

- Osion 02 tuotokset ovat projektikansiossa: ohjetiedosto, `TYOLISTA.md`, `HYVAKSYMISKRITEERIT.md` ja yhteensä viisi tallennuspistettä osioista 01 ja 02. Tiedät, jäikö työlista kesken. `TESTIT.md` ottaa merkinnät työlistalta.
- Harjoitusajon välitila osion 03 lopusta on saatavilla (simuloitu Wilma ja testiaineisto ilman oppijan tiedostoja).
- Varmuusaineisto (liite) on tekstinä valmiina liitettäväksi.
- Ensimmäisen koulutuksen tutkinnon osat (P05): jos ne on saatu, oppija voi korvata Testikoulutuksen oikealla julkisella koulutuksella tehtävän 2 kehotteessa. Päätös kirjataan päätöslokiin. Opiskelijat pysyvät kuvitteellisina.
- Tiedät harjoitusajosta, aukeaako käynnistystiedosto kaksoisnapsautuksella hallitulla koneella, toimiiko palautus ja odottaako agentti hyväksynnän jälkeen K3:a.
- Osion 02 `teacher-led-tasks.md`:n kysymykset 4 ja 6 vastauksineen ovat esillä.

## Ohjaus askel askeleelta

**Osion 02 kysymykset.** Oppija näyttää säännön ohjetiedostosta. Kysymys 4: saako ohjelma luoda työpaikan kysymättä? Odotettu vastaus: ei. Ohjelma etsii olemassa olevan ja näyttää sen ennen uuden luomista, ja puuttuvan lisäys valmistellaan hyväksyttäväksi (KP osat 6 ja 8). Kysymys 6: mitä ohjelma tekee, jos Wilma-kenttää ei löydy? Odotettu vastaus: pysäyttää kirjoituksen ja merkitsee kentän puuttuvaksi. Kenttää ei keksitä, eikä toista valita tilalle (KP osat 19 ja 21). Jos sääntö puuttuu, oppija pyytää omin sanoin agenttia lisäämään sen ja tarkistaa lisäyksen polun tavalla. Hän kirjaa lisäyksen päätöslokiin omana merkintänään.

**Kehystys.** Kysy ajattelukysymys ja anna oppijan vastata ääneen yhdellä tapauksella. Sano sitten tärkein lause: agentti tekee sekä simuloidun Wilman että sovelluksen, joten ne sopivat yhteen silloinkin, kun molemmat ovat väärin. Oppijan vertailu oikeaan työhön on ainoa korjaus tähän.

**Tehtävä 1.** Viisi tapausta, joista yksi omasta kokemuksesta. Liitteen A tapaukset ovat lukutekstissä, joten neljä löytyy helposti. Viides on osion arvokkain. Jos oppija jumittuu, kysy: Mikä kirjaus on mennyt viimeksi uusiksi? Mikä tieto on puuttunut, kun olisit tarvinnut sen? Älä ehdota tapausta itse. Tapaus kirjoitetaan tilanteena, ei henkilönä. Lopun tallennuspiste suojaa kriteerit.

**Tehtävä 2.** Rajaa simulaatio seitsemään kohtaan. Agentti ehdottaa helposti ulkoasua, tietokantapalvelinta tai oppisopimusnäkymää. Ne korjautetaan pois. Kenttäaukon pitää tulla oppijan muistista ilman oikeita tietoja.

Agentti tekee käynnistys- ja palautustiedostot, `KAYNNISTYS.md`:n ja lähtötilan (sopimukset 9.3 ja 10.1). Oppija käynnistää simuloidun Wilman itse kaksoisnapsautuksella. Lähtötilassa Aino Testisellä 000456 on yksi aiempi urasuunnitelma: T05:n vertailukohta ja olemassa olevan tietueen tapaus. Oppijan käsin tekemä urasuunnitelma testaa säilymisen, ja palautus poistaa sen.

K2:n viimeinen rivi pyytää agenttia odottamaan K3:a, mutta se ei ole varmaa. Oppijalla on varaohje (sopimukset 9.4). K3 lisätään kehotepohjiin vasta osiossa 04. Jos työlistalla ei ole simuloidun Wilman tehtävää, K3:een kirjoitetaan tehtävän nimi. Katso hyväksyntähetkellä polun tapa (Polkujen erot).

**Tehtävä 3.** Aineisto luodaan suoraan kehotteella, koska sisältö annetaan valmiina. Sääntö osioille 03–09 (sopimukset 9.2): suora kehote ilman K2:ta ja K3:a vain dokumenteille ja aineistolle, joiden sisältö annetaan kehotteessa. Koodi kulkee aina koko työkierroksen. Testikytkimellä on silti oma testi, päätös ja tallennuspiste. Oppijan työ on tarkistus. Aineistossa ovat myös 000456 ja Mallikkaat osioita 05–07 varten. Varmista, että CSV avataan Muistiolla. Jos aineistossa on uskottava oikea nimi, esimerkiksi agentin keksimä tavallinen etu- ja sukunimi, oppija korjauttaa sen liitteen A tyyliin.

**Tehtävä 4.** Oma huomio on osion analyysiosa. Hyväksy myös epävarmat huomiot, kunhan ne ovat muistista. Älä anna oppijan avata oikeaa Wilmaa tarkistaakseen. Oikea Wilma ei kuulu työpajaan. Jos urasuunnitelmasta puuttuu kenttä, jota oppija tarvitsee osiossa 04, päätös on korjautan. Kenttä lisätään simuloituun Wilmaan ja `KENTAT.md`:hen työkierroksella: muutosten tarkistus, kokeilu ja tallennuspiste.

**Tehtävä 5.** Listamuoto on tarkoituksellinen, koska oppija kirjoittaa tulokset Muistiolla. Vertaa merkintöjä suunnitelman luvun 1.2 tasoihin. Vähimmäistavoitteessa ovat T01 (sim.), T02 (osin), T05, T13 ja T20. Lisätavoitteessa ovat T06, T07 ja T09, ja jatkoon jäävät T11, T12, T15 ja T16. Muut ovat tavoitetta. Jos oppijan työlista poikkeaa, oppija päättää. Puutu vain, jos T05 tai T13 ei ole työpajassa. O01 on oppijan ensimmäinen itse kirjoitettu tulos. Katso, että Tulos-rivillä on yksi vaihtoehto ja havainto on oma. Jokaisella testillä on Lähtötila-rivi (palauta ensin), ja tiedoston alussa on uusinnan malli (sopimukset 4 ja 10.3). O03 (kaksoiskappaleen esto) jatkaa T05:stä, ja se tehdään osiossa 04.

Oppija pitää hiiren koko osion ajan.

## Polkujen erot (taulukko Claude | Codex)

| Asia | Claude | Codex |
|---|---|---|
| Suunnitelma ensin | Suunnittelutila ja K2 | K2:n viimeinen rivi. Kehote on pyyntö, ei tekninen este. |
| Suunnitelman hyväksyntä | Vaihtoehto, joka jättää lupapyynnöt päälle. Jos agentti aloittaa ennen K3:a, oppija kieltää lupapyynnön ja kirjoittaa "Pysähdy. Odota, että annan palan." | Täsmälleen "Hyväksyn suunnitelman. Älä vielä aloita. Annan ensimmäisen palan seuraavaksi." Jos agentti aloittaa, oppija pysäyttää sen ja katsoo Git-toiminnot. |
| Agentin kokeilema palvelin | Lupapyyntö käynnistyskomennolle | PowerShell hiekkalaatikossa. Palvelimen käynnistys voi vaatia hyväksynnän. |
| Oppijan käynnistys | `kaynnista-wilma.cmd` kaksoisnapsautuksella | Sama |
| Muutosten tarkistus | Lupapyynnöt ja muutosnäkymä | Agenttisovelluksen Git-toiminnot. Agentin luettelo on vain apu. |
| Esikatselu | Edge tai sisäänrakennettu selain | Edge |
| Ohjetiedosto kehotteissa | `CLAUDE.md` | `AGENTS.md` |
| Polun riski | Lupapyyntöjä tulee rakennuksessa useita, ja oppija alkaa hyväksyä lukematta | Agentti muokkaa kansion tiedostoja kysymättä. Git-näkymä on ainoa kontrolli. |

## Väärinkäsitykset (vähintään 3)

**Väärinkäsitys 1:** "Simuloitu Wilma vastaa oikeaa." Se vastaa sitä, mitä agentti ymmärsi kuvauspaketista ja oppijan muistista. Kentät, oikeudet ja kirjautuminen todennetaan testi-Wilmassa. Oppijan huomiot `KENTAT.md`:ssä ovat ainoa kirjattu ero.

**Väärinkäsitys 2:** "Kuvitteellinen aineisto saa olla oikeasta muokattu." Ei saa. Vaihdettu nimi ei poista tunnistettavaa tilannetta. Tapaus keksitään alusta, ja nimet ja tunnisteet noudattavat liitettä A.

**Väärinkäsitys 3:** "Läpäisty testi simuloidussa Wilmassa tarkoittaa, että ohjelma toimii Wilmassa." Se tarkoittaa, että ohjelma toimii simuloitua Wilmaa vasten. KP osa 27 vaatii erottamaan, mitä testattiin paikallisesti ja mitä testi-Wilmassa. Siksi `TESTIT.md`:n havaintoon kirjataan ympäristö.

## Jumikohdat ja purku (taulukko: oire | todennäköinen syy | purku)

| Oire | Todennäköinen syy | Purku |
|---|---|---|
| Simuloitu Wilma ei käynnisty, ilmoitus kertoo portin olevan käytössä | Agentti jätti oman kokeilunsa käyntiin | Oppija pyytää agenttia sulkemaan sen. Tarvittaessa agentti vaihtaa portin ja päivittää ohjeen. |
| Selain ei avaa paikallista osoitetta | Simuloitu Wilma ei ole käynnissä, tai osoite on kirjoitettu väärin | Tarkista käynnistysikkuna. Kopioi osoite `KAYNNISTYS.md`:stä sellaisenaan. |
| Agentti tekee liian hienon simulaation | Rajaus jäi lukematta tai agentti ennakoi myöhempiä osioita | Korjauta seitsemään kohtaan. Ylimääräinen poistetaan ennen hyväksyntää, ei myöhemmin. |
| Etunollat ovat kadonneet | CSV avattiin ja tallennettiin Excelillä | Pyydä lista uudelleen. Näytä Muistio-tapa. Gitistä näkee, muuttuiko tiedosto. |
| Oppija haluaa näyttää oikean Wilman näkymän kuvana | Halu saada simulaatio tarkaksi | Ei. Oppija kuvailee kentän omin sanoin. Kuvat kerätään jatkossa testi-Wilmasta puhdistettuina (KP liite A). |
| Codex: agentin käynnistämä simuloitu Wilma ei vastaa | Hiekkalaatikko tai hyväksyntä puuttuu | Oppija käynnistää simuloidun Wilman itse kaksoisnapsauttamalla `kaynnista-wilma.cmd`:tä. |
| Käynnistysikkuna sulkeutuu heti | Virhe käynnistyksessä | Oppija pyytää agenttia pitämään ikkunan auki virheen jälkeen. Sitten virhe agentille sellaisenaan. |
| Agentti aloittaa heti hyväksynnän jälkeen tai tekee kaiken kerralla | Hyväksyntä käynnisti toteutuksen | Polkujen erot, rivi Suunnitelman hyväksyntä. Jatka K3:lla. |
| Palautuksen jälkeen oma urasuunnitelma näkyy yhä | Simuloitu Wilma oli käynnissä palautuksen aikana | Sulje ikkunat ja palauta uudelleen. |

## Varasuunnitelma

Jos työlista jäi osiossa 02 kesken eikä se valmistu alun viidessä minuutissa, oppija viimeistelee siitä vain V01–V10-luettelon ja T05:n ja T13:n tehtävät. Ne tarvitaan tehtävässä 5. Loput tehdään osion 04 asennusten odotusaikana.

Jos testiaineiston luonti ei onnistu kahdella yrityksellä, anna agentille varmuusaineisto. Oppija tarkistaa sen samoin kuin oman aineistonsa.

Jos simuloitu Wilma ei toimi kello 13.10, pura harjoitusajon välitila projektikansioon. Säilytä oppijan omat tiedostot: `PAATOSLOKI.md`, `HYVAKSYMISKRITEERIT.md`, `maarittely/oma-kokemus.md` ja mahdollinen `TESTIT.md`. Oppija kirjaa päätöslokiin, että välitila otettiin käyttöön ja miksi.

Kello 13.15, jos tehtävä 2 on kesken: `TESTIT.md` tehdään ennen `KENTAT.md`:n omia huomioita, koska T05 ja T13 tarvitsevat rungon. Huomiot kirjoitetaan osion 04 asennusten odotusaikana.

Jos agentti kiertää kehää, pysäytä se. K10 esitellään vasta osiossa 04, joten tässä vetäjä katkaisee kehän ja oppija palaa tallennuspisteeseen K7:llä.

## Tarkista ennen seuraavaa osiota

- [ ] Simuloitu Wilma käynnistyy kaksoisnapsautuksella ilman agenttia, ja palautus on kokeiltu. Jokaisella sivulla lukee SIMULOITU.
- [ ] Haku nimellä Aino Testinen näyttää kaksi opiskelijaa. Aino Testisellä 000456 on vain lähtötilan urasuunnitelma.
- [ ] Profiilin Primus-tiedot ovat vain luettavia.
- [ ] `testiaineisto` sisältää liitteen A tapaukset, Mallikkaat ja oppijan oman tapauksen. Etunollat ovat tallessa.
- [ ] `KENTAT.md`:ssä ovat urasuunnitelman ja profiilin kentät sekä oppijan omat huomiot.
- [ ] `TESTIT.md` on listamuodossa Lähtötila-riveineen, T05 ja T13 ovat työpajassa, O03 on mukana, ja O01:llä on oppijan tulos.
- [ ] `KEHOTEPOHJAT.md`:ssä on K8.
- [ ] Kysymysten 4 ja 6 säännöt ovat ohjetiedostossa. Mahdollinen lisäys on kirjattu päätöslokiin.
- [ ] Päätöslokissa on vähintään neljä uutta merkintää omin sanoin, ja viimeinen tallennuspiste on tehty.

## Tarkistettavat nimet

- Claude: sisäänrakennetun selaimen avaaminen Code-välilehdellä.
- Claude: vaihtoehdot suunnitelman hyväksynnässä ja lupatila hyväksynnän jälkeen.
- Claude: lupapyynnön vaihtoehto, joka sallii saman jatkossa kysymättä.
- Codex: hyväksyntäpyynnön muoto, kun agentti käynnistää paikallisen palvelimen hiekkalaatikossa.
- Codex: Git-toimintojen näkymä, jossa uudet tiedostot näkyvät.
- Windows: Muistion avausikkuna .csv-tiedostolle ja raahaustapa.
- Windows: .cmd-käynnistystiedosto hallitulla koneella ja päätteen näkyminen.
- Windows: tekstin kopiointi käynnistysikkunasta.
- Claude: aloittaako agentti toteutuksen suunnitelman hyväksynnän jälkeen, vaikka K2 kieltää.
- Codex: agentin pysäytys kesken työn.

## Liite: varmuusaineisto

Ei lasketa sanamäärään. Liitä agentille kehotteella "Lisää kansioon testiaineisto tämä aineisto. Opiskelijanumerot ovat tekstiä. Älä muuta tiedostoa wilma-lahtotila.json." Simuloidun Wilman lähtötilassa ovat opiskelijat ja profiilit sekä yksi aiempi urasuunnitelma Aino Testisellä 000456.

| Opiskelija | Nro | Opiskeluoikeus | Esitiedot | Haastattelu |
|---|---|---|---|---|
| Aino Testinen | 000123 | Testikoulutus, TK26A | 37,5 h/vko, 2 450 €/kk, Testileipomo Oy Keskusta | 37,5 h/vko, työpaikkaohjaaja Maija Mallikas, työnantajan edustaja Kaisa Mallikas |
| Aino Testinen | 000456 | Testikoulutus, TK26B | nimikaima, tiedot kunnossa | nimikaima |
| Eero Esimerkki | 001789 | Testikoulutus ja Esimerkkikoulutus | 30 h/vko, 14,20 €/h | 30 h/vko |
| Liisa Kokeilu | 002024 | Testikoulutus | 30 h/vko, palkka 2 450 (ei yksikköä) | 37,5 h/vko |
| Ville Testaaja | 000999 | Testikoulutus | puuttuu | tehty |
| (tyhjä rivi) | | | | |
| (virherivi) | 12A | | | |

Liitettävä nimilista: Aino Testinen, Eero Esimerkki. Työpaikat (osio 07): Testileipomo Oy (Keskusta, Satama), Esimerkkikone Oy (yksi toimipaikka), Kokeiluverstas Oy (puuttuu simuloidusta Wilmasta). Henkilöt: Maija Mallikas (työpaikkaohjaaja, Testileipomo Oy Keskusta), Kaisa Mallikas (työnantajan edustaja, Testileipomo Oy), Pekka Mallikas (työpaikkaohjaaja, Esimerkkikone Oy) ja Pekka Mallikas (työpaikkaohjaaja, Testileipomo Oy Satama).
