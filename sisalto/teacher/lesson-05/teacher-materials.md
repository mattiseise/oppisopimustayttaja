# Opettajan materiaali: osio 05 – Lähteet, puutteet ja ristiriidat

## Ajattelukysymys ja tavoitteet (Bloom)

> Ajattelukysymys: Kun lähteet ovat eri mieltä tai tieto puuttuu, mitä ohjelma saa päättää ja mitä vain sinä?

- Ymmärtää: oppija selittää viiden lukutilan erot.
- Analysoida: oppija tunnistaa lähteiden ristiriidan ja puutteen.
- Soveltaa: oppija testaa lukutilat testikytkimillä.
- Arvioida: oppija perustelee oman lupa-asetuksensa ja muutosten tarkistustapansa.

Painotus on arvioinnissa. Osio aloittaa päivän 2. Siinä oppija muuttaa ensimmäistä kertaa omaa valvontatapaansa, ja Claude-polun lupapyyntöväsymys käsitellään tässä. Kattavuus: vaihe 2 osa 1 (lähdehavainnot, validointi, ristiriitanäkymä, sisällön versiointi). V02 ja V09. T01 (sim.), T03 (vain työaika) ja T17. Vähimmäistavoite: palat 1–3 ja T01 (oppijan tehtävät 1–5). Tavoite: pala 4 (T03), testikytkimet (T17) ja pala 5 (tehtävät 6–8).

## Aikataulu (minuutit, summa = osion kesto)

| Min | Kello | Sisältö |
|---|---|---|
| 10 | 9.00–9.10 | Kehystys, uusi keskustelu ja K11 (tehtävä 1, askeleet 1–4) |
| 5 | 9.10–9.15 | Tehtävä 1: kriteerit tarkistusnäkymälle |
| 7 | 9.15–9.22 | Tehtävä 2: lupa-asetus tai tarkistustapa |
| 8 | 9.22–9.30 | Tehtävä 3: K2 ja suunnitelman tarkistus |
| 18 | 9.30–9.48 | Tehtävä 4: palat 1 ja 2 yhdellä kierroksella, T01 |
| 12 | 9.48–10.00 | Tehtävä 5: pala 3, tarkistusnäkymä |
| 15 | 10.00–10.15 | Tehtävä 6 (tavoite): pala 4, ristiriita ja T03 |
| 15 | 10.15–10.30 | Tehtävä 7 tai 8 (tavoite) |
| 90 | | Yhteensä |

Aloittelijan työkierros vie 12–20 min. Vähimmäistavoite mahtuu, vaikka T13 tehtäisiin aamulla. Tavoitteen palat jäävät usein osion 07 aikaan.

## Ennen osiota

- Osion 04 valmis-ehdot: tallennuspiste "Päivä 1", T05 ja T13 kirjattu, päätöslokissa aloituskohta. Jos päivä 1 jäi kesken, toimi varasuunnitelman mukaan.
- `palauta-lahtotila.cmd` on projektikansiossa ja tyhjentää sovelluksen jonon ja käsittelyt. Jokainen tämän osion testi alkaa palautuksella. Kokeile tiedostoa välitilassasi.
- Avaa oppijan `testiaineisto` Muistiolla. Aino Testisellä (000123) ja Liisa Kokeilulla (002024) on esitiedot ja haastattelu. Liisan työaika on haastattelussa 37,5 h/vko ja esitiedoissa 30 h/vko. Jos ristiriita puuttuu, T03 ei testaa mitään. Oppija lisää tapauksen K8:lla ennen tehtävää 6.
- `KENTAT.md` luettelee profiilin kentät. Oppija tarvitsee niitä tehtävissä 3 ja 7.
- Vetäjän välitila osion 04 lopusta on saatavilla.
- Pyydä oppijaa lukemaan lukuteksti edellisenä iltana.

## Ohjaus askel askeleelta

**Kehystys ja K11.** Kysy ajattelukysymys ja pyydä esimerkki omasta työstä: milloin kaksi lähdettä on kertonut eri asian? Oppija aloittaa uuden keskustelun ja ajaa K11:n. Vertaa vastausta yhdessä `TESTIT.md`:hen. Jos agentti sanoo testin tehdyksi, vaikka tulos puuttuu, pysähdy siihen. Testitulos on oppijan merkintä, ei agentin muistikuva. Askel 4: jos T13 jäi eilen, se tehdään nyt (varasuunnitelma).

**Tehtävä 1.** Hyvä kriteeri on havaittava. Esimerkiksi: "Piilotettu kenttä näkyy sanoin ei näkyvissä, ei tyhjänä." Älä anna sitä valmiina. Jos oppija jumittuu, kysy: mitä tarkistusnäkymässä ei saa koskaan näkyä?

**Tehtävä 2: lupa-asetuksen ohjaus.** Hyväksy kumpi tahansa ratkaisu, jos perustelu on oppijan oma ja tallennuspiste tehdään ennen jokaista palaa. Claude-polulla komentojen lupapyynnöt pidetään päällä. Jos oppija sallii tiedostomuutokset automaattisesti, varmista ensimmäisen palan aikana, että komennoille tulee yhä lupapyyntö (jumikohdat). Codex-polulla varmista, että oikeusasetus on oletusoikeudet. Täysiä oikeuksia ei valita.

Pysäytyssäännön pitää olla havaittava: kansio, tiedosto tai muutos, jonka oppija näkee. "Jos jokin näyttää oudolta" ei ole sääntö. Kysy lopuksi: mitä teet, jos sääntösi laukeaa kesken palan? Oikea vastaus: suljen Muistion, palaan tallennuspisteeseen K7:llä ja kirjaan hylkäyksen sen jälkeen.

**Tehtävä 3.** Aukon hyvä vastaus nimeää kentän ja lukutilan oppijan työstä, esimerkiksi opiskeluoikeus NOT_VISIBLE. Tarkista suunnitelmasta viisi palaa ja tehtävänumerot. Rivi "Kun hyväksyn suunnitelman, älä aloita" pyytää agenttia odottamaan. Askel 7 on varaohje, jos agentti silti aloittaa. Hyväksyntä tehdään polun tavalla (polkujen erot). K2:n palautusrivi varmistaa, että osion 06 testit alkavat ilman osion 05 valintoja ja hyväksyntöjä.

**Tehtävät 4–6 ja 8.** Sama työkierros. Palat 1 ja 2 tehdään yhdellä K3:lla, koska aika ei riitä kahteen kierrokseen. Pidä rytmi: K3, muutosten tarkistus, palautus, ajo, Oma testi, Päätös ja tallennuspiste. Älä anna oppijan niputtaa päätöksiä loppuun. Odotusaika käytetään Lähtötila- ja Odotan-rivien kirjoittamiseen. Ennuste ennen havaintoa on osion tärkein tapa. Uusinta kirjataan testin alle omalle rivilleen, ja aiempi tulos jää.

T01: kohdistus tehdään opiskelijanumerolla, ja ryhmä on TK26A. Jos sovellus näyttää ryhmän TK26B, se luki nimikaiman tiedot. Tulos on ei läpi, ja korjaus tehdään K5:llä.

T03: kumpaakaan arvoa ei saa olla valittuna valmiiksi. Jos sovellus valitsee uudemman lähteen, tulos on ei läpi.

**Tehtävä 7.** Oppija valitsee piilotettavan kentän `KENTAT.md`:stä. Jos kenttä näkyy tyhjänä, testi on tehnyt tehtävänsä. Oppija kirjaa ei läpi, korjauttaa K5:llä ja testaa uudelleen. Tämä on hyvä ei läpi -tulos, ei epäonnistuminen. Oppija toteaa lopuksi, että palautus kytkee kytkimet pois.

**Tehtävä 8.** Oppija ei tee Wilma-tallennusta. Muutettu arvo ja vanhentunut hyväksyntä häviävät palautuksessa ennen osion 06 T20:tä.

Oppija pitää hiiren koko osion ajan.

## Polkujen erot (taulukko Claude | Codex)

| Asia | Claude | Codex |
|---|---|---|
| Uusi keskustelu | Uusi istunto Code-välilehdellä | Uusi työsäie samassa projektissa, yksi kerrallaan |
| Ohjetiedosto K2:ssa ja K11:ssä | `CLAUDE.md` | `AGENTS.md` |
| Osion päätös | Pidetäänkö lupapyynnöt tiedostomuutoksille vai sallitaanko muutokset automaattisesti. Komentojen lupapyynnöt pysyvät. | Milloin muutokset tarkistetaan Git-toiminnoista. Oletusoikeudet pysyvät, täysiä oikeuksia ei valita. |
| Suunnitelma ensin | Suunnittelutila ja K2:n viimeinen rivi. Hyväksyntä tehtävän 2 päätöksen mukaan. | K2:n viimeinen rivi. Hyväksyntä lauseella "Hyväksyn suunnitelman. Älä vielä aloita. Annan ensimmäisen palan seuraavaksi." |
| Agentti aloittaa ennen K3:a | Kiellä lupapyyntö: "Pysähdy. Odota, että annan palan." Automaattisen sallimisen jälkeen pysäytä agentti ja katso muutosnäkymä. | Pysäytä agentti ja tarkista Git-toiminnot. K7 tarvittaessa. |
| Muutosten tarkistus palan jälkeen | Lupapyynnöt ja lopuksi muutosnäkymä. Automaattisen sallimisen jälkeen pelkkä muutosnäkymä. | Git-toimintojen muuttuneet tiedostot. Agentin luettelo vain apuna. |
| Tehtävän 2 tarkistus | Asetuksen vaihto vetäjän ohjaamana, jos oppija sallii muutokset | Git-toiminnoista todetaan, että vain oppijan omat tiedostot muuttuivat |
| Polun riski | Lupapyyntöväsymys: hyväksyntä lukematta. Automaattisen sallimisen jälkeen muutosnäkymä jää katsomatta. | Tarkistus jää tekemättä, kun kaikki toimii. Oppija tyytyy agentin luetteloon. |

## Väärinkäsitykset (vähintään 3)

**Väärinkäsitys 1:** "Tyhjä kenttä tarkoittaa, että tietoa ei ole." Tyhjä on yksi viidestä lukutilasta. Piilossa oleva kenttä (NOT_VISIBLE) ja epäonnistunut luku (READ_FAILED) eivät ole tyhjiä. KP osa 5: puuttuvaa käyttöoikeutta ei tulkita tyhjäksi tiedoksi.

**Väärinkäsitys 2:** "Ohjelma voi valita uudemman lähteen." Ei voi. KP osa 8: ohjelma näyttää molemmat, ja työntekijä selvittää oikean tiedon. Uudempi lähde voi olla väärä.

**Väärinkäsitys 3:** "Hyväksyntä on pysyvä." Hyväksyntä sidotaan sisältöversioon (KP osa 20). Kun sisältö muuttuu, hyväksyntä vanhenee. Vaihe 2 on valmis vasta, kun tämä toimii (KP osa 25).

**Väärinkäsitys 4:** "Automaattinen salliminen tekee agentista turvallisemman, koska sitä ei tarvitse vahtia." Asetus ei muuta agenttia. Se poistaa yhden pysähdyksen. Turvallisuus tulee tallennuspisteestä ennen palaa ja muutosten tarkistuksesta sen jälkeen. Codex-polulla sama ajatus kuuluu muodossa "hiekkalaatikko riittää". Hiekkalaatikko ei estä muutoksia projektikansion sisällä.

## Jumikohdat ja purku (taulukko: oire | todennäköinen syy | purku)

| Oire | Todennäköinen syy | Purku |
|---|---|---|
| Lukutilat näkyvät vain koodeina tai väreinä | Pyyntö ei korostanut sanoja | K5: lukutila sanoina ja PRO-värein (V08). Ohjetiedoston kohta 8. |
| Ristiriidan valintaa ei kirjata | Pala 4 toteutti vain valinnan | K5 T03:lla: valinta näkyy ja säilyy, kun tiedot avataan uudelleen |
| Oppija hyväksyy kaiken nopeasti | Lupapyyntöväsymys tai kiire | Pyydä yksi en hyväksy -tapaus: mitä sovellus ei saa näyttää? Testataan se. |
| Agentti aloittaa heti hyväksynnän jälkeen tai tekee monta palaa kerralla | Suunnitelman hyväksyntä tulkittiin toteutusluvaksi | Pysäytä polun tavalla (polkujen erot). K7 tarvittaessa. Jatka K3:lla. |
| `palauta-lahtotila.cmd` puuttuu, ei tyhjennä jonoa tai ei kytke uusia kytkimiä pois | Osion 03 tai 04 palautus jäi kesken, tai kytkimiä ei lisätty lähtötilaan | K5: palautus lähtötilan mukaan. Testit vasta sen jälkeen. |
| Piilotettu tai sammutettu kenttä näkyy tyhjänä | Sovellus tulkitsee puuttuvan tyhjäksi | Ei läpi T17:ssä. K5 ja uusinta. |
| Komennoille ei tule lupapyyntöä automaattisen sallimisen jälkeen (Claude) | Valittiin laajempi asetus kuin tarkoitettiin | Palauta asetus. Katso muutosnäkymästä, mitä muuttui. Oppija kirjaa asian päätöslokiin. |
| Agentti muuttaa testiaineistoa korjatakseen ristiriidan | Agentti tulkitsi ristiriidan virheeksi | Hylkää ja palaa tallennuspisteeseen. Ristiriita on testitapaus. Ohjetiedoston kohta 6. |
| Profiilia ei saada luettua | Näkyvä selain ei auennut tai oppija ei kirjautunut | Käynnistys `KAYNNISTYS.md`:n mukaan, oppija kirjautuu itse. Agentti ei kirjaudu. |

## Varasuunnitelma

**Prioriteettilista.** Osiot 06–08 viittaavat tähän listaan.
- Päivä 2 alkaa uudella keskustelulla ja K11:llä. Sen jälkeen enintään 20 min päivältä 1 kesken jääneelle: ensin T13, sitten osion 04 vetäjän katselmointi. Jos päivä 1 päättyi ilman varmennettua Wilma-tallennusta, osio 04 tehdään ensin loppuun, enintään 60 min.
- Prioriteetti (vetäjä tarkistaa klo 12.00 ja 14.15): (1) vähimmäistavoitteen palat: osion 05 haku ja tarkistusnäkymä (T01), osion 06 tuonti, jono ja VALMIS (T02 osin, T20); (2) osio 08 vähimmäistestit, työpajaversio ja osio 09 – näitä ei pudoteta; (3) tavoitteen palat osioista 05–06 (T03, T17, T18, T19, T21); (4) osio 07.
- Osio 07 pudotetaan ensin. Sen jälkeen osioiden 05–06 tavoitteen palat.
- Jos osio loppuu kesken palan: oppija tekee tallennuspisteen viestillä "Kesken: [pala]" tai palaa edelliseen tallennuspisteeseen, ja pyytää agenttia merkitsemään palan työlistaan keskeneräiseksi. Seuraavan osion alussa vetäjä päättää prioriteetin mukaan, jatketaanko.
- Riippuvuus: osion 06 T20 tarvitsee osion 05 palan 3, jossa sisältö hyväksytään tarkistusnäkymässä. Jos pala 3 on kesken kello 10.30, se tehdään osion 06 alussa.

**T13 siirtyi aamuun.** K11:n jälkeen oppija tekee osion 04 T13:n, TL mukaan lukien, enintään 20 min (tehtävä 1, askel 4). Aika otetaan tavoitteen paloista. Palat 1–3 ja T01 tehdään silti tässä osiossa.

**Päivä 1 ilman varmennusta.** Osion 04 jälkeen osiosta 05 tehdään vain vähimmäistavoite. Lupa-asetuksen päätökseen 5 min. Osio 06 alkaa ajallaan kello 10.45. Osio 07 jää pois.

**Aikataulu venyy.** Järjestys: palat 1–3 ja T01, pala 4 ja T03, testikytkimet ja T17, pala 5. Kesken jääneet tavoitteen palat tehdään osion 07 aikana. Osiota 06 ei lyhennetä tämän vuoksi.

Agentti kiertää kehää: K10 ja K7. Jos projekti on rikki yli 15 min, pura vetäjän välitila osion 04 lopusta. Oppijan omat tiedostot säilytetään: `PAATOSLOKI.md`, `HYVAKSYMISKRITEERIT.md`, `TESTIT.md`, `KENTAT.md` ja `maarittely/oma-kokemus.md`. Oppija kirjaa päätöslokiin, mitä tapahtui.

## Tarkista ennen seuraavaa osiota

- [ ] Päätöslokissa on lupa-asetus tai tarkistustapa, oppijan oma peruste ja havaittava pysäytyssääntö.
- [ ] Claude: komentojen lupapyynnöt ovat päällä. Codex: oikeusasetus on oletusoikeudet.
- [ ] T01 on kirjattu oppijan sanoin, ja T03 ja T17, jos ne tehtiin. Tulos on läpi, ei läpi tai ei testattu, ja Lähtötila-rivi on täytetty.
- [ ] Jokaisesta tehdystä palasta on päätös ja tallennuspiste. Kesken jäänyt pala on työlistalla keskeneräisenä.
- [ ] Testikytkimet ovat pois päältä, ja palautus kytkee ne pois.
- [ ] Pala 3 on hyväksytty. Jos ei, se tehdään osion 06 alussa.

## Tarkistettavat nimet

- Claude: uuden istunnon aloitus Code-välilehdellä.
- Claude: automaattisen sallimisen asetuksen nimi ja paikka sekä mitkä komennot sovellus kysyy asetuksen jälkeen.
- Claude: näyttääkö muutosnäkymä kaikki muutokset edellisen tallennuspisteen jälkeen vai vain viimeisen vastauksen.
- Claude: suunnitelman hyväksynnän vaihtoehdot suunnittelutilassa, ja aloittaako agentti hyväksynnän jälkeen, vaikka K2 kieltää.
- Claude ja Codex: agentin pysäytys kesken työn.
- Codex: uuden työsäikeen aloitus samassa projektissa.
- Codex: oikeusasetuksen näkymä ja oletusoikeuksien nimi.
- Codex: Git-toimintojen näkymä, jossa muuttuneet tiedostot näkyvät.
