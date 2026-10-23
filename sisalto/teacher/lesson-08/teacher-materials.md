# Opettajan materiaali: osio 08 – Hyväksymistestit ja häiriötilanne

## Ajattelukysymys ja tavoitteet (Bloom)

> Ajattelukysymys: Mitä hyväksymistestisi osoittavat, ja mitä ne eivät vielä osoita?

- Soveltaa: oppija tekee hyväksymistestit tarkistuslistana ja kirjaa havainnon omin sanoin.
- Analysoida: oppija erottaa simuloidussa Wilmassa osoitetun asian siitä, mitä testi-Wilmassa pitää vielä osoittaa.
- Arvioida: oppija tekee perustellun hyväksymispäätöksen työpajaversiosta.
- Soveltaa (testi-Wilma): oppija noudattaa tietoturvan muistilistaa testi-Wilmassa.

Painotus on arvioinnissa. Tämä on osio, jossa agentin valmis ei ole testitulos -periaate testataan oikeasti. Oppija ei kysy agentilta, menivätkö testit läpi. Kattavuus: vaihe 6 osin (yksi häiriötilanne) ja B2:ssa vaiheet 0–1 testi-Wilmassa. Vaatimukset V08, V01 ja V09. Testit T10 ja T14 sekä kaikki aiemmat työpajatestit uudelleen.

Lupaa sama kuin osiossa 00. Vähimmäistavoite: simuloitu Wilma ja Oppisopimustäyttäjä käynnistyvät `KAYNNISTYS.md`:n ohjeella ilman agenttia. Sovellus avaa näkyvän selaimen, ja oppija kirjautuu itse. Yhden opiskelijan tiedot haetaan kuvitteellisista lähteistä tarkistettaviksi. Urasuunnitelman Wilma-tallennus varmennetaan uudelleenluvulla. Kahden opiskelijan jonossa VALMIS tulee vasta varmennuksen jälkeen. Lisäksi oppijalla on ohjetiedosto, työlista, päätösloki, hyväksymiskriteerit, `TESTIT.md` ja `JATKO.md`. Tavoite lisää lukutilat ja ristiriidat, listatuonnin ja nimikaimat, jonon tilan Odottaa lisätietoja, oppisopimuksen riippuvuuksineen, PRO-ilmeen, yhden häiriötestin ja testi-Wilman lukukokeilun, jos ehdot täyttyvät. Hyväksytty työpajaversio ei ole käyttövalmis ohjelma.

## Aikataulu (minuutit, summa = osion kesto)

| Min | Kello | Sisältö |
|---|---|---|
| 5 | 14.30–14.35 | Kehystys: valmis ei ole testitulos, B1 vai B2 |
| 5 | 14.35–14.40 | Tehtävä 1: kriteerit työpajaversiolle |
| 22 | 14.40–15.02 | Tehtävä 2: testikierros ja T14 |
| 18 | 15.02–15.20 | Tehtävä 3: B1 (T10) tai B2 (testi-Wilma) |
| 10 | 15.20–15.30 | Tehtävä 4: korjautus ja uusi testi |
| 10 | 15.30–15.40 | TL Hyväksyjän kierros |
| 5 | 15.40–15.45 | Tehtävä 5: hyväksymispäätös ja tallennuspiste Työpajaversio 1 |
| 75 | | Yhteensä |

Testikierros on tiukka. Vähimmäistestit T01, T02, T05, T13 ja T20 tehdään ensin. Loput saavat jäädä ei testattu -merkinnälle, jos niillä ei ole tulosta aiemmista osioista. Jokainen lähtötilan palautus vie noin 2 min.

## Ennen osiota

**Päivän 2 prioriteetti.** Noudata osion 05 Varasuunnitelman prioriteettilistaa. Osion 08 vähimmäistestit, työpajaversio ja osio 09 eivät putoa. Jos oppijalla on kesken osion 05 tai 06 vähimmäistavoitteen pala, sovi ennen testikierrosta, tehdäänkö se nyt vai kirjataanko testit ei testattu.

**Lähtötila.** Kirjoittavat testit alkavat palautuksella (`palauta-lahtotila.cmd`). Tarkista, että palautus toimii oppijan koneella: urasuunnitelmia on vain Aino Testisellä (000456), ja testikytkimet ovat pois päältä.

**B1 vai B2.** B2 tehdään vain, jos kaikki ehdot täyttyvät:

- Testi-Wilma on vahvistetusti testikäytössä, eikä siinä ole oikeita tietoja.
- Oppijalla on testirooli.
- Kirjautuminen toimi savutestissä.
- Oppija kirjautuu itse.
- Agentti ei avaa testi-Wilmaa omilla työkaluillaan.
- Kenttäluku tallentaa vain rakenteen, ja oppija tarkistaa tulosteen ennen agenttia.
- HAR-tallenteita tai koko sivun lähdekoodia ei tallenneta (KP liite A).

Kenttäluku rakennettiin osion 07 tehtävässä 7 ja testattiin simuloidussa Wilmassa. Jos se ei ole valmis tai tuloste sisälsi arvoja, B2 tehdään ilman agenttia (ks. Varasuunnitelma). Jos yksikin ehto ei täyty, oppija tekee B1:n.

**Testitunnus.** Oppija on saanut testi-Wilman osoitteen ja testitunnuksen Wilma-pääkäyttäjältä. Tunnus ei ole missään projektikansion tiedostossa, kehotteessa eikä päätöslokissa.

**TL Hyväksyjän kierros.** Valitse etukäteen kolme testiä, joista pyydät näytön. Suositus: T05, T20 ja oppijan B-osan testi (T10 tai B2:n havainnot).

**Oma ennuste.** T10 menee todennäköisesti ensimmäisellä kerralla ei läpi, jos sovelluksessa ei vielä ole operaation tilaa Tallennustulos tuntematon (KP osa 22). Se on hyvä. Oppija saa korjattavan tehtävään 4.

## Ohjaus askel askeleelta

**Kehystys.** Sano ääneen: agentin valmis ei ole testitulos, eikä agentin automaattinen testi ole hyväksymistesti. Kysy oppijalta: "Mitä T05 ei todista?" Palaatte kysymykseen TL:ssä.

**Tehtävä 1.** Kriteerit kirjoitetaan ennen testejä. Muuten oppija kirjoittaa kriteeriksi sen, mitä testit sattuivat näyttämään. Hyvä Hyväksyn, kun -kohta: "Vähimmäistavoitteen kuusi kohtaa näkyvät omissa testeissäni, ja T05, T13 ja T20 ovat läpi." Hyvä En hyväksy, jos -kohta: "Yksikin Wilma-tallennus näkyy varmennettuna ilman uudelleenlukua."

**Tehtävä 2.** Testit tehdään ilman agenttia. Oppija käynnistää sovelluksen `KAYNNISTYS.md`:n ohjeella ja avaa simuloidun Wilman suoraan, kun testi koskee Wilma-tallennusta. Järjestys on lukittu, jotta testit eivät riipu toisistaan. Palautuksen jälkeen T01, T02, T05 ja T20 tehdään samalla jonolla kuin osiossa 06 (Aino, Ville, Liisa). T13 jatkaa Villellä. Hänen esitietolomakkeensa puuttuu, joten oppija täydentää puuttuvat arvot tarkistusnäkymässä kuvitteellisilla arvoilla ja hyväksyy sisällön. T14 alkaa uudella palautuksella Liisalla. O02 tehdään muiden testien kanssa ilman Wilma-tallennusta. Eeroa ei käytetä ennen B1:tä. Kierros päättyy tallennuspisteeseen. Aiempia tuloksia ei pyyhitä. Uusinta kirjataan testin alle omalle rivilleen, ja Lähtötila-riville tulee palauta ensin tai jatka testistä Tnn. Kierrä ja pyydä näyttöä: "Näytä, mistä näit tämän." Havainnon pitää kertoa, mitä oppija näki, ei mitä agentti sanoi. T14:ssä värit verrataan silmämääräisesti ohjetiedoston värikoodeihin. Lukutilat ja jonon tilat sanoina sekä näppäimistökäyttö ovat tärkeämpiä kuin sävyt.

**Tehtävä 3, B1.** Testikytkin rakennetaan työkierroksella, ja se lisätään lähtötilaan pois päältä. Oppija kokeilee palautusta ennen testiä. Oppija kirjoittaa ennusteen T10:n Odotan-kohtaan ennen ajoa. Palautuksen jälkeen Eero Esimerkillä ei ole urasuunnitelmaa. Jonossa on myös Liisa, jotta pysähdys näkyy. Liisalle ei kirjoiteta. Kaksi opiskeluoikeutta vaatii valinnan, mikä kuuluu testiin. Osio 06 lupasi, että Tarkistettava tallennus testataan tässä: Eeron jonon tila on katkon jälkeen Tarkistettava tallennus tai oppijan päättämä nimi. Ratkaiseva havainto on simuloidusta Wilmasta: täsmälleen yksi urasuunnitelma.

**Tehtävä 3, B2.** Aloita TL Testi-Wilman turvatarkistuksella. Oppija lukee muistilistan ääneen. Agentin keskustelu on tauolla koko B2:n ajan. Oppija käynnistää sovelluksen itse, kirjoittaa testi-Wilman osoitteen näkyvään selaimeen ja kirjautuu. Kenttäluku ajetaan kahteen näkymään: opiskelijan haku (W01) ja urasuunnitelman uusi lomake (W02). Lomaketta ei tallenneta. Tuloste menee projektikansion ulkopuolelle kansioon `C:\dev\testi-wilma-raaka`. Oppija lukee sen Muistiolla, puhdistaa liitteen A mukaan ja kirjoittaa erot `KENTAT.md`:hen omin sanoin. Agentti ei saa tulostetta. Ennen tallennuspistettä oppija tarkistaa muutokset: projektikansioon ei saa tulla selainprofiilia, evästeitä, tallenteita eikä sivujen sisältöä. Jos tulee, tallennuspistettä ei tehdä.

**Tehtävä 4.** Yksi korjaus, ei useampia. Oppija valitsee ei läpi -testin, täyttää K5:n havainnollaan, palauttaa lähtötilan ja tekee saman testin uudelleen samalla opiskelijalla. Ilman palautusta T10:n uusinta törmäisi ensimmäisen ajon urasuunnitelmaan. T05:n uusinta palautuksen jälkeen osoittaa, ettei korjaus rikkonut ydintä. Ennen K5:tä tarkista, ettei ei läpi -tulos johdu puuttuvasta palautuksesta. Muuten agentti korjaa pois kaksoiskappaleen eston.

**TL Hyväksyjän kierros.** Ks. `teacher-led-tasks.md`.

**Tehtävä 5.** Päätöksessä on peruste ja yksi asia, jota testit eivät osoita. Hyväksyn tarkoittaa työpajaversiota, ei käyttöönottoa. Agentti saa merkitä työlistan tehtävät valmiiksi `TESTIT.md`:n tulosten perusteella, mutta se ei muuta testien tuloksia. Tallennuspisteen viesti alkaa sanoilla Työpajaversio 1.

Oppija pitää hiiren koko osion ajan.

## Polkujen erot (taulukko Claude | Codex)

| Asia | Claude | Codex |
|---|---|---|
| Suunnitelma ensin (B1) | Suunnittelutila ja K2:n kaksi viimeistä riviä | K2:n kaksi viimeistä riviä |
| Suunnitelman hyväksyntä | Osion 05 lupapäätöksen mukaan. Varaohje: lupapyynnön kielto tai pysäytys ja "Pysähdy. Odota, että annan palan." | Täsmälleen: "Hyväksyn suunnitelman. Älä vielä aloita. Annan ensimmäisen palan seuraavaksi." Varaohje: pysäytys ja Git-toiminnot. |
| Muutosten tarkistus | Muutosnäkymä | Muuttuneet tiedostot Git-toiminnoista. Agentin luettelo on vain apu. |
| B2: agentin rajaus | Agentti ei avaa testi-Wilmaa sisäänrakennetussa selaimessa. Oppija kieltää lupapyynnön. | Hiekkalaatikko estää verkkoyhteydet ilman hyväksyntää. Oppija kieltää verkkoyhteyspyynnön testi-Wilmaan. Täysiä oikeuksia ei valita. |
| B2: näkyvä selain | Avataan oppijan käynnistämästä sovelluksesta | Sama. Ei agentin komennolla. |
| B2: tarkistus ennen tallennuspistettä | Projektikansio Resurssienhallinnassa | Muuttuneet tiedostot Git-toiminnoista |
| Muistilistan rivi | Et salli kaikkea automaattisesti. | Et valitse täysiä oikeuksia. |
| Polun riski | Agentti tarjoutuu avaamaan sivun sisäänrakennetussa selaimessa "tarkistaakseen" | Oppija hyväksyy verkkoyhteyspyynnön tottumuksesta |

## Väärinkäsitykset (vähintään 3)

**Väärinkäsitys 1:** "Kaikki testit läpi tarkoittaa, että sovellus on valmis käyttöön." Testit osoittavat toiminnan simuloidussa Wilmassa kuvitteellisella aineistolla. Ennen käyttöä tarvitaan testi-Wilma, salaus ja säilytys, asennuspaketti ja pilotti (KP osat 25–26).

**Väärinkäsitys 2:** "Testi-Wilmaan saa antaa agentin kirjautua, koska siellä ei ole oikeita tietoja." Tunnukset ovat oppijan henkilökohtaiset, ja kirjautunut istunto antaa pääsyn oppijana (KP osa 23). Oppija kirjautuu aina itse.

**Väärinkäsitys 3:** "Ei läpi -tulos on epäonnistuminen." Ei läpi on tieto siitä, mitä korjata tai viedä jatkoon. Työpajan arvioinnissa rehellinen ei läpi on parempi kuin perustelematon läpi.

**Väärinkäsitys 4:** "Agentin automaattiset testit menivät läpi, joten hyväksymistestin voi ohittaa." Automaattinen testi on agentin työkalu. Se ei näe, onko arvo oikealla opiskelijalla simuloidussa Wilmassa.

## Jumikohdat ja purku (taulukko: oire | todennäköinen syy | purku)

| Oire | Todennäköinen syy | Purku |
|---|---|---|
| Oppija merkitsee läpi ilman havaintoa | Kiire tai luottamus agenttiin | Pyydä näyttö: "Näytä simuloidusta Wilmasta." Havainto kirjoitetaan uudelleen. |
| Aika loppuu kesken testikierroksen | Testejä on paljon | Vähimmäistestit T01, T02, T05, T13 ja T20 ensin. Loput ei testattu. |
| Testi-Wilman kirjautuminen ei onnistu näkyvässä selaimessa | Kertakirjautuminen, lisätunnistautuminen tai selainkäytäntö | Havainto `KENTAT.md`:hen ja osiossa 09 `JATKO.md`:hen IT:lle. Ei kiertoteitä. Siirry B1:een. |
| Kenttäluvun tulosteessa on arvoja tai piilokenttiä | Kenttäluku lukee kenttien sisällön | Pysäytä. Tiedostoa ei anneta agentille. Vetäjä hoitaa poiston oppijan kanssa. Kenttäluku korjataan simuloidussa Wilmassa jatkossa. |
| Agentti pyytää lupaa avata testi-Wilman | Agentti haluaa tarkistaa itse | Kielto. Muistuta ohjetiedoston tietoturvakohdasta. |
| T10: jono jatkaa seuraavaan | Sovelluksessa ei ole operaation tilaa Tallennustulos tuntematon | Ei läpi. Korjautus tehtävässä 4 K5:llä. |
| Uusinta luo toisen urasuunnitelman | Sovellus ei lue Wilman nykytilaa ennen uusintaa | Ei läpi. K5:n odotettu tulos: nykytila luetaan ensin (KP osa 22). |
| Oppija haluaa korjauttaa kaiken | Useita ei läpi -tuloksia | Yksi korjaus nyt. Muut jatkoon. |
| Uusinta ei tallennu, ja oppija kirjaa ei läpi | Lähtötilaa ei palautettu, ja kaksoiskappaleen esto toimi oikein | Palautus ja testi uudelleen. Turvasääntöä ei korjauteta. |
| B2:n jälkeen projektikansiossa on uusi kansio tai tiedosto | Sovellus tallensi selainprofiilin tai evästeitä | Ei tallennuspistettä. Vetäjä poistaa sen oppijan kanssa, ennen kuin agentti jatkaa. Korjautus simuloidussa Wilmassa jatkossa. |

## Varasuunnitelma

Jos testi-Wilmaa ei ole tai ehdot eivät täyty, oppija tekee B1:n. Päärunko ei muutu.

Jos kenttäluku ei ole valmis, B2 tehdään vetäjän ohjaamana havainnointina ilman agenttia. Oppija avaa testi-Wilman ja kirjaa kenttien nimet käsin `KENTAT.md`:hen. Arvoja ei kirjata.

Jos aika loppuu, korjautus voi jäädä viiteen minuuttiin, ja TL lyhenee yhteen testiin (T05). Hyväksymispäätöstä ja tallennuspistettä Työpajaversio 1 ei jätetä pois.

Jos projekti rikkoutuu yli 15 minuutiksi, pura osion 07 välitila projektikansioon. Oppijan omat tiedostot säilytetään, ja päätöslokiin tulee merkintä.

Jos oppija hylkää viimeisimmän muutoksen, hän palaa edelliseen tallennuspisteeseen K7:llä. Tallennuspiste Työpajaversio 1 tehdään sen jälkeen.

## Tarkista ennen seuraavaa osiota

- [ ] Jokaisella työpajatestillä on tulos ja havainto oppijan sanoin.
- [ ] Vähintään yksi ei läpi -testi on korjautettu ja testattu uudelleen.
- [ ] T14 on kirjattu, ja T10 tai B2:n havainnot ovat tallessa.
- [ ] Päätöslokissa on hyväksymispäätös ja asia, jota testit eivät osoita.
- [ ] Tallennuspiste Työpajaversio 1 on tehty.
- [ ] Uusinnat ovat omilla riveillään, ja aiemmat tulokset ovat tallessa.
- [ ] B2:n jälkeen: näkyvä selain on suljettu, tuloste on projektikansion ulkopuolella ja tarkistettu, eikä tunnuksia ole missään tiedostossa. Projektikansioon ei tullut selainprofiilia, evästeitä eikä tallenteita.

## Tarkistettavat nimet

- Claude: sisäänrakennetun selaimen käyttö ja miten sen lupapyyntö näkyy.
- Claude: vaihtoehdot suunnitelman hyväksynnässä.
- Codex: hyväksyntäpyynnön muoto, kun agentti pyytää verkkoyhteyttä.
- Codex: Git-toimintojen näkymä, jossa muuttuneet ja uudet tiedostot näkyvät.
- Claude: näkyvätkö muutosnäkymässä tiedostot, jotka sovellus, ei agentti, loi. Jos eivät, B2:n tarkistus tehdään Resurssienhallinnassa.
- Molemmat: agentin pysäyttäminen kesken työn.
- Molemmat: miten agentin keskustelu pysäytetään tai jätetään tauolle B2:n ajaksi.
