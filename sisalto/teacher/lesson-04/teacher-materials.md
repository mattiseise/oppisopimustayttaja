# Opettajan materiaali: osio 04 – Ensimmäinen varmennettu tallennus

## Ajattelukysymys ja tavoitteet (Bloom)

> Ajattelukysymys: Mistä tiedät, että tieto todella tallentui, kun agentti sanoo valmis?

- Ymmärtää: oppija selittää, miksi Wilma-tallennus varmennetaan uudelleenluvulla.
- Soveltaa: oppija ohjaa agentin rakentamaan pienen kokonaisen ketjun pala kerrallaan.
- Soveltaa: oppija antaa virheilmoituksen agentille sellaisenaan ja katkaisee kehän.
- Arvioida: oppija erottaa agentin valmis-ilmoituksen omasta testituloksestaan.

Painotus on testaamisessa. Kattavuus: vaihe 1 (tekninen kokeilu) ja vaihe 4 osin (urasuunnitelma). Vaatimukset V01, V04 (osin) ja V09 (kohdistus profiilista). Testit T05, T13 ja T02 osin: kohdistus opiskelijanumerolla ja T05:n tarkistus, ettei nimikaima 000456 muutu.

Osion jälkeen suunnitelman luvun 1.2 vähimmäistavoitteesta täyttyvät kohdat 1, 2 ja 4. Simuloitu Wilma ja sovellus käynnistyvät `KAYNNISTYS.md`:n ohjeella ilman agenttia. Sovellus avaa näkyvän selaimen, jossa oppija kirjautuu itse, ja kirjoittaa vain simuloituun Wilmaan. Urasuunnitelman Wilma-tallennus varmennetaan uudelleenluvulla, ja poikkeava arvo näkyy tarkistamattomana. Automaattinen haku (kohta 3) tulee osiossa 05 ja jono (kohta 5) osiossa 06. Tavoitetaso on realistinen vain, jos päivä 1 päättyy varmennettuun Wilma-tallennukseen.

## Aikataulu (minuutit, summa = osion kesto)

| Min | Kello | Sisältö |
|---|---|---|
| 10 | 14.00–14.10 | Kehystys: ajattelukysymys ja lause "agentin valmis ei ole testitulos". Tehtävä 1: uusi keskustelu, kehotepohjat ja K11. |
| 8 | 14.10–14.18 | Tehtävä 2: kriteerit, Aino Testisen arvot ja tallennuspiste |
| 12 | 14.18–14.30 | Tehtävä 3: muistilista, K2 + K9 ja suunnitelman tarkistus |
| 50 | 14.30–15.20 | Tehtävät 4 ja 5: palat (a)–(e) ja virhetilanteet |
| 15 | 15.20–15.35 | Tehtävät 6–7: palautus, kylmä käynnistys, T05 ja O03 |
| 15 | 15.35–15.50 | TL Valmis vai varmennettu ja tehtävä 8: testikytkin ja T13 |
| 10 | 15.50–16.00 | Tehtävä 9: päivän päätös ja tallennuspiste Päivä 1 |
| 120 | | Yhteensä |

Taulukko on ihannepolku. Palojen arvio ennen harjoitusajoa: (a) 15 min, koska siinä on asennukset, (b) 10, (c) 8, (d) 10 ja (e) 7. Aloittelijalle yksi pala vie 12–20 min, ja koko osio arviolta 150–180 min. Korjaa luvut harjoitusajon mittausten mukaan. Leikkaa ajoissa:

- Kello 15.00: jos pala (c) ei ole hyväksytty, TL ja T13 siirtyvät päivän 2 alkuun (noin 20 min, ks. varasuunnitelma).
- Kello 15.30: jos pala (e) ei ole valmis, tehtävän 6 kylmä käynnistys tehdään palan (e) tarkistuksessa, ja T05 tehdään ennen päivän päätöstä.

## Ennen osiota

- Osion 03 tarkistuslista täyttyy. Erityisesti `TESTIT.md` on olemassa, palautus toimii, ja Aino Testisellä 000456 on lähtötilan urasuunnitelma.
- Savutestin tulos on tiedossa. Jos Electron tai Playwrightin selain ei latautunut, päätä varapolku ennen osiota (luku 1.5).
- Harjoitusajon välitila osion 04 lopusta on omalla koneellasi: sovellus, simuloitu Wilma testikytkimineen ja `KAYNNISTYS.md`. Tarvitset sitä TL:ssä ja varapolkuna.
- Tunnet oman versiosi: uuden keskustelun aloitus samassa projektikansiossa, suunnitelman hyväksynnän vaihtoehdot (Claude) ja verkko- ja kirjoitushyväksyntöjen muoto (Codex).
- Tiedät harjoitusajosta, odottaako agentti hyväksynnän jälkeen K3:a, aukeaako `kaynnista-sovellus.cmd` ja tyhjentääkö palautus sovelluksen työjonon.
- K9 on KP liitteen A "GPT-6.1 Sol -avusteisen devauksen työjärjestys" sovellettuna molempiin polkuihin. Oppijan materiaalissa mallin nimeä ei mainita. Työjärjestys on sama mallista riippumatta.
- Tilauksen käyttöraja: osio 04 kuluttaa eniten. Tiedä, mitä teet, jos raja tulee vastaan.

## Ohjaus askel askeleelta

**Kehystys ja tehtävä 1.** Sano ääneen: "Agentin valmis ei ole testitulos." Kysy ajattelukysymys ja jätä vastaus auki. Näytä uuden keskustelun aloitus, mutta anna oppijan tehdä se. Kehotepohjat lisätään ennen K11:tä, jotta K11 otetaan jo tiedostosta. Jos K11:n vastauksesta puuttuu simuloitu Wilma tai `TESTIT.md`, agentti ei lukenut tiedostoja. Oppija pyytää uudelleen.

**Tehtävä 2.** Hyvä En hyväksy, jos -kohta on esimerkiksi: "En hyväksy, jos sovellus näyttää valmiin ennen uudelleenlukua." Aino Testisen arvot kirjoitetaan kriteeritiedostoon ennen rakentamista. Silloin T05 vertaa oppijan omaan tiedostoon eikä sovelluksen näyttöön. Arvot ovat keksittyjä. Jos oppija aikoo muokata oikean opiskelijan tavoitetta, pysäytä. Lopun tallennuspiste suojaa kriteerit ja mahdollistaa paluun, jos agentti aloittaa ennen K3:a.

**Tehtävä 3.** Pyydä oppijaa sanomaan muistilistasta ääneen kohta, joka koskee tätä osiota. Odotettu vastaus on kirjautuminen. K2 + K9:ssä on kolme aukkoa. Kenttäaukko on substanssia: kenttä, joka menee käsin helpoimmin väärin. Suunnitelman Oma testi on neljä kysymystä. Jos suunnitelma tallentaa kirjautumistilan tiedostoon, se on istunto. Oppija korjauttaa sen ennen hyväksyntää. Pala (a) tekee `kaynnista-sovellus.cmd`:n, ja pala (e) laajentaa palautuksen sovelluksen työjonoon ja käsittelyihin (sopimukset 9.3 ja 10.1). Agentti ei välttämättä odota K3:a. Hyväksynnän tapa ja varaohje ovat Polkujen erot -taulukossa.

**Tehtävä 4.** Pala (a) on raskain, koska siinä asennetaan Electron. Claude-polulla lupapyyntöjä tulee kymmeniä. Seuraa, ettei oppija valitse vaihtoehtoa, joka sallii saman jatkossa kysymättä. Codex-polulla oppija hyväksyy verkon ja kaksi kansion ulkopuolista kohdetta (Polkujen erot). Muut hän kieltää ja kutsuu sinut. Palassa (b) oppija kirjautuu itse. Agentti saa kokeilla simuloitua Wilmaa automaattisilla testeillään, mutta näkyvän selaimen kirjautuminen on oppijan. Katso palan (b) tallennuspisteen jälkeen, ettei projektikansioon syntynyt selaimen profiili- tai istuntokansiota. Palassa (c) numero 000777 on pysähtyvä tapaus. Palassa (d) arvot näkyvät muokattavina. Tätä tarvitaan T13:ssa Ville Testaajalle. Päätösten perusteet saavat olla lyhyitä, kunhan ne ovat muotoa "Näin: … Siksi: …" ja nimeävät havainnon (sopimukset 9.1). "Toimii" ei kelpaa.

**Tehtävä 5.** Yleisimmät virheet ovat asennusvirheitä. Vaadi, että oppija kopioi virheilmoituksen eikä kuvaile sitä. Käynnistysikkunassa teksti maalataan ennen Ctrl+C:tä, koska pelkkä Ctrl+C voi pysäyttää ohjelman. Laske yritykset ääneen oppijan kanssa. Kahden jälkeen K10 ja K7. Jos syy on ympäristössä, kuten välityspalvelin tai IT:n esto, kehää ei jatketa. Siirrytään varapolkuun.

**Tehtävä 6.** `KAYNNISTYS.md` testataan kylmästä käynnistyksestä. Oppija ei kysy agentilta. Ennen käynnistystä oppija palauttaa lähtötilan, joten T05 ei riipu palojen (d) ja (e) kokeiluista. Jos ohjeessa on askel, jota oppija ei voi tehdä, kuten PowerShellin suoritusasetuksen muutos, oppija korjauttaa sen. Agentti valitsee toisen käynnistystavan.

**Tehtävä 7.** Oppija tekee kirjauksen sovelluksella ja tarkistaa sen sovelluksen ohi, suoraan simuloidusta Wilmasta Edgessä. Vertailukohta on kriteeritiedosto. Nimikaiman 000456 tarkistus ja palan (c) 000777 ovat T02:n osa, ja ne kirjataan T05:n havaintoon (sopimukset 9.1). O03 jatkaa T05:stä: toinen kirjaus Ainolle ei saa tehdä toista urasuunnitelmaa. Se testaa K9:n kohdan (5).

**TL ja tehtävä 8.** TL tehdään ennen oppijan omaa testikytkintä (`teacher-led-tasks.md`). Ville Testaaja on valittu, koska hänen esitietolomakkeensa puuttuu. Osiossa 06 hän siirtyy jonon tilaan Odottaa lisätietoja, eikä sovellus kirjoita hänelle jonossa. T13:n jälki ei siis häiritse osion 06 testejä. Uusinnat tehdään lähtötilasta. Testikytkin on sivun valinta, jolla on oma päätös ja tallennuspiste (sopimukset 9.2). T13 alkaa palautuksella, joka poistaa aiemmat kirjaukset ja kytkee kytkimen pois. Ennuste kirjoitetaan Odotan-rivin perään sanalla Ennuste: ennen ajoa. Läpi tarkoittaa, että väärä kenttä näkyy tarkistamattomana eikä kirjausta näytetä varmennettuna. Jos se näkyy varmennettuna, tulos on ei läpi ja oppija korjauttaa K5:llä. Tämä on arvokas löydös. Älä kiirehdi sen ohi.

**Tehtävä 9.** Päivän päätöksen perusteen pitää viitata T05:n ja T13:n tuloksiin oppijan sanoin. "Huomenna aloitan tästä" on päivän 2 ensimmäinen syöte. Tarkista, että agentti merkitsi työlistalta valmiiksi vain testatut tehtävät, myös osion 03 tehtävät, joiden O01 on läpi.

Oppija pitää hiiren koko osion ajan. Vetäjä tarttuu näppäimistöön vain asennus- ja järjestelmäongelmissa.

## Polkujen erot (taulukko Claude | Codex)

| Asia | Claude | Codex |
|---|---|---|
| Uusi keskustelu | Uusi istunto Code-välilehdellä. `CLAUDE.md` luetaan istunnon alussa, K11 täydentää. | Uusi työsäie samassa projektissa. K11 pyytää lukemaan `AGENTS.md`:n. |
| Suunnitelman hyväksyntä | Vaihtoehto, joka jättää lupapyynnöt päälle. Jos lupapyyntö tulee ennen K3:a, oppija kieltää sen ja kirjoittaa "Pysähdy. Odota, että annan palan." | Täsmälleen "Hyväksyn suunnitelman. Älä vielä aloita. Annan ensimmäisen palan seuraavaksi." Jos agentti aloittaa, oppija pysäyttää sen, katsoo Git-toiminnot ja palaa tarvittaessa tallennuspisteeseen. |
| Asennusten luvat | Lupapyyntö jokaiselle komennolle, usein kymmeniä peräkkäin | Hyväksyntä verkolle ja kahdelle kohteelle kansion ulkopuolella: asennusten välimuisti ja Playwrightin selainkansio. Muut kielletään. |
| Ikkunoiden avaaminen | Agentti voi käynnistää sovelluksen lupapyynnöllä. Oppija käynnistää `kaynnista-sovellus.cmd`:llä. | Ikkuna ei välttämättä aukea hiekkalaatikosta. Oppija käynnistää `kaynnista-sovellus.cmd`:llä. |
| Muutosten tarkistus palojen välillä | Lupapyynnöt ja muutosnäkymä | Agenttisovelluksen Git-toiminnot jokaisen palan jälkeen |
| Virheilmoituksen lähde | Käynnistysikkuna tai terminaalipaneeli | Käynnistysikkuna tai agentin ajaman komennon tuloste |
| Polun riski | Lupapyyntöväsymys ja vaihtoehto, joka sallii saman jatkossa | Houkutus valita täydet oikeudet asennusten nopeuttamiseksi |

## Väärinkäsitykset (vähintään 3)

**Väärinkäsitys 1:** "Valmis = toimii." Agentin valmis tarkoittaa, että agentti lopetti. Toimiminen todetaan ajamalla sovellus ja katsomalla tulos. Ohjetiedoston kohta 3 vaatii, että valmis-ilmoituksessa on tarkistusohje.

**Väärinkäsitys 2:** "Onnistumisviesti = tallentunut." KP osa 21 sanoo, ettei onnistumisviesti, napin painallus tai HTTP-vastaus yksin riitä. Vain uudelleenluku kertoo, mitä lomakkeelle jäi. TL näyttää tämän.

**Väärinkäsitys 3:** "Virheilmoitus pitää ymmärtää itse." Oppija antaa sen agentille sellaisenaan K4:llä. Oppijan tehtävä on kertoa, mitä hän teki ja mitä odotti. Agentti selvittää syyn.

**Väärinkäsitys 4:** "Automaattiset testit läpi = hyväksymistesti läpi." Automaattinen testi tarkistaa agentin oman ymmärryksen. Hyväksymistesti tarkistaa oppijan kriteerin. Ne voivat olla eri mieltä, ja silloin oppijan havainto ratkaisee.

**Väärinkäsitys 5:** "Simuloidussa Wilmassa kirjautumisen voi jättää agentille, koska salasanaa ei ole." Tapa opitaan nyt. Testi-Wilmassa samaa tapaa ei voi enää muuttaa ilman riskiä.

## Jumikohdat ja purku (taulukko: oire | todennäköinen syy | purku)

| Oire | Todennäköinen syy | Purku |
|---|---|---|
| Electronin lataus estyy | Välityspalvelin tai IT:n esto | Luvun 1.5 varapolku: käyttöliittymä selaimessa ja Playwright erillisenä prosessina. Oppija kirjaa teknologiavalinnan muutoksen päätöslokiin. V01:n työpöytäkuori siirtyy jatkoon. |
| Playwrightin selainlataus estyy | Välityspalvelin | Playwright käyttää koneen Edgeä. |
| npm-komennot estyvät PowerShellissä | Suoritusasetus | Agentti valitsee toisen käynnistystavan. Oppija ei muuta järjestelmäasetuksia. Jos ei ratkea, IT. |
| Codex: asennus pysähtyy | Verkko tai kirjoitus projektikansion ulkopuolelle vaatii hyväksynnän | Oppija lukee pyynnön kolmella kysymyksellä. Hyväksyy verkon, asennusten välimuistin ja Playwrightin selainkansion. Täysiä oikeuksia ei valita. |
| Codex: ikkuna ei aukea agentin kokeilussa | Hiekkalaatikko | Oppija käynnistää sovelluksen itse `kaynnista-sovellus.cmd`:llä. |
| Käynnistysikkuna sulkeutuu heti | Virhe käynnistyksessä | Oppija pyytää agenttia pitämään ikkunan auki virheen jälkeen. Sitten K4. |
| Virheilmoituksen kopiointi sulkee ohjelman | Ctrl+C painettiin ennen maalaamista | Käynnistä uudelleen ja maalaa ensin. Tai kirjoita ensimmäiset rivit K4:ään. |
| Agentti aloittaa heti hyväksynnän jälkeen tai tekee monta palaa kerralla | Hyväksyntä käynnisti toteutuksen | Polkujen erot, rivi Suunnitelman hyväksyntä. Jatka K3:lla. |
| Uusinnassa sovellus ei tee kirjausta, tai Ainolla on monta urasuunnitelmaa | Lähtötilaa ei palautettu, ja kaksoiskappaleen esto pysäyttää | Palautus lähtötilaan ja testi alusta. |
| Claude: lupapyyntöjä ei enää tule | Oppija valitsi vaihtoehdon, joka sallii saman jatkossa, tai automaattisen hyväksynnän | Palauta oletuslupatila. Katso muutosnäkymästä, mitä jo muuttui. |
| Agentti kiertää kehää | Sama korjaus toistuu | K10 ja K7. Katso, onko syy ympäristössä. |
| Agentti kysyy teknisiä valintoja | Ohjetiedoston kohta 2 ei vaikuta | Muistuta kohdasta 2. Auta valinnassa vain, jos se muuttaa sitä, mitä oppija näkee. |
| Tallennuspisteessä on tuhansia tiedostoja | Asennetut kirjastot tulivat mukaan | Oppija pyytää agenttia rajaamaan asennetut kirjastot tallennuspisteiden ulkopuolelle. |
| Sovellus pyytää salasanaa tai tallentaa kirjautumistilan | Agentti toteutti tavallisen kirjautumismallin | Pysäytä. Korjautus K5:llä. Syntynyt tiedosto poistetaan ennen tallennuspistettä. |
| Agentti merkitsee testin läpäistyksi | Ohjetiedoston kohta 3 ohitettiin | Korjautus. Tuloksen kirjoittaa oppija. |

## Varasuunnitelma

Jos aika loppuu, pala (e) ja T05 tehdään ennen T13:a (päätöskohdat aikataulun alla). Jos TL ja T13 siirtyvät, päivä 2 alkaa uudella keskustelulla ja K11:llä. Sen jälkeen käytetään enintään 20 min: ensin T13 (TL sen alussa, jos aika riittää), sitten osion 04 katselmointi tämän tiedoston tarkistuslistalla (sopimukset 10.2). Oppija tietää siirrosta osion 04 Seuraava osio -kohdasta. Jos pala jää kesken, oppija tekee tallennuspisteen viestillä "Kesken: [pala]" ja kirjoittaa palan Huomenna aloitan tästä -riville.

Jos agentti aloittaa harjoitusajossa aina heti hyväksynnän jälkeen, kerro siitä materiaalin ylläpitäjälle ennen työpajaa.

Jos projekti on rikki yli 15 minuuttia, pura harjoitusajon välitila osion 04 lopusta projektikansioon. Säilytä oppijan omat tiedostot: `PAATOSLOKI.md`, `HYVAKSYMISKRITEERIT.md`, `TESTIT.md`, `KENTAT.md` ja `maarittely/oma-kokemus.md`. Oppija kirjaa päätöslokiin, miksi välitila otettiin käyttöön. T05 ja T13 tehdään silti välitilan sovelluksella, koska osion tavoite on testaus.

Jos päivä 1 päättyy ilman varmennettua Wilma-tallennusta, päivän 2 järjestys on luvun 1.5 mukainen. Osio 04 viedään loppuun enintään 60 minuutissa. Osiosta 05 tehdään vain haku ja tarkistusnäkymä, ja osiosta 06 CSV ja jono. Osio 07 jää pois, ja osiossa 08 tehdään vain vähimmäistestit. Oppijan "Huomenna aloitan tästä" -rivin pitää silloin olla tarkka.

Jos käyttöraja tulee vastaan, siirry varakoneelle tai käytä toista tunnusta organisaation lisenssiehtojen mukaan.

## Tarkista ennen seuraavaa osiota

- [ ] `KAYNNISTYS.md` toimii kylmästä käynnistyksestä ilman agenttia. Molemmat käynnistyvät kaksoisnapsautuksella, ja palautus toimii.
- [ ] Sovellus ei pyydä salasanaa. Projektikansiossa ei ole istunto-, eväste- tai tallennetiedostoja.
- [ ] `TESTIT.md`:ssä ovat T05:n, O03:n ja T13:n tulokset oppijan sanoin. T05:n havainnossa ovat 000456 ja 000777. Testikytkin on pois päältä.
- [ ] Simuloidussa Wilmassa Ville Testaajalla on yksi urasuunnitelma (T13) ja Aino Testisellä 000456 vain lähtötilan urasuunnitelma.
- [ ] Palojen perusteet ovat muotoa "Näin: … Siksi: …".
- [ ] `KEHOTEPOHJAT.md`:ssä ovat K3, K4, K5, K9, K10 ja K11.
- [ ] Päätöslokissa ovat palojen päätökset, päivän päätös ja huomisen aloituskohta.
- [ ] Työlistalla on valmiina vain tehtävät, joiden testitulos on kirjattu.
- [ ] Tallennuspiste Päivä 1 on tehty.

## Tarkistettavat nimet

- Molemmat: uuden keskustelun aloitus samassa projektikansiossa.
- Claude: vaihtoehdot suunnitelman hyväksynnässä ja lupatila hyväksynnän jälkeen.
- Claude: lupatilan vaihto ja palautus oletukseen.
- Claude: lupapyynnön vaihtoehto, joka sallii saman jatkossa kysymättä.
- Claude: terminaalipaneelin avaaminen virheilmoituksen kopiointia varten.
- Codex: hyväksyntäpyyntöjen muoto verkolle ja projektikansion ulkopuoliselle kirjoitukselle.
- Codex: Git-toimintojen näkymä muuttuneille tiedostoille.
- Codex: oikeusasetuksen näkymä, josta näkee, ettei täysiä oikeuksia ole valittu.
- Codex: miltä asennusten välimuisti ja Playwrightin selainkansio näyttävät hyväksyntäpyynnössä.
- Claude: aloittaako agentti toteutuksen suunnitelman hyväksynnän jälkeen, vaikka K2 kieltää.
- Codex: agentin pysäytys kesken työn.
- Windows: `kaynnista-sovellus.cmd` kaksoisnapsautuksella hallitulla koneella.
- Windows: tekstin kopiointi käynnistysikkunasta.
