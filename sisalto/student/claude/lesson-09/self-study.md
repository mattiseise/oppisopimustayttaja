# Osio 09: Jatko: seuraavat askeleet ja pilotti

> Ajattelukysymys: Mikä on seuraava pienin askel, jonka voit tehdä ja tarkistaa itse, ja mikä kuuluu IT:lle tai pääkäyttäjälle?

Työpaja päättyy, mutta työ ei. Sinulla on työpajaversio ja omat tiedostosi. Niillä työ jatkuu kohti testi-Wilmaa ja pilottia.

Tämä osio kestää työpajassa puoli tuntia. Siinä kokoat jatkosuunnitelman. Lukuteksti on myös työpajan jälkeistä työtä varten. Palaa siihen, kun aloitat ensimmäisen itsenäisen työkerran.

## Mitä sinulla nyt on

Vähimmäistavoite oli tämä. Simuloitu Wilma ja sovellus käynnistyvät ohjeella ilman agenttia. Sovellus avaa selaimen, jossa kirjaudut itse. Se hakee yhden opiskelijan tiedot kuvitteellisista lähteistä ja näyttää ne tarkistettavina. Se tekee urasuunnitelman Wilma-tallennuksen ja lukee lomakkeen uudelleen. Kahden opiskelijan jonossa seuraava avautuu vasta, kun edellinen on varmennettu. Lisäksi sinulla on omat tiedostosi: säännöt, työlista, päätösloki, hyväksymiskriteerit, testitulokset ja jatkosuunnitelma.

Tavoite oli laajempi. Silloin sovellus näyttää myös puuttuvat ja ristiriitaiset tiedot. Se tuo opiskelijalistan, erottaa samannimiset opiskelijat ja osaa jättää opiskelijan odottamaan lisätietoja. Se kirjaa oppisopimuksen tiedot oikeassa järjestyksessä. Ulkoasu noudattaa PRO-ilmettä, ja yksi häiriötilanne on testattu. Jos testi-Wilma oli käytössä, kokeilit myös sen kenttien lukemista.

Hyväksymispäätöksesi kertoo, mitä näistä toteutui. Se, mikä jäi kesken, ei ole kadonnut. Se on `TESTIT.md`:ssä merkinnällä jatko ja pian `JATKO.md`:ssä.

Sinulla ei ole yhteyttä oikeaan Wilmaan, oikeita tietoja, asennettavaa ohjelmaa eikä pilottia. Ne ovat jatkoa, ja niihin tarvitaan muita.

## Agentti ei muista eilistä

Kun aloitat uuden istunnon, agentti aloittaa tyhjästä. Se ei muista työpajaa, päätöksiäsi eikä sitä, mihin jäit. Tiedostot muistavat. `CLAUDE.md` kertoo säännöt. `TYOLISTA.md` kertoo tehtävät. `PAATOSLOKI.md` kertoo päätökset ja perusteet. `TESTIT.md` kertoo tulokset, ja `JATKO.md` seuraavat askeleet.

Siksi jokainen työkerta alkaa tilannekatsauksella K11. Se pyytää agenttia lukemaan tiedostot, ennen kuin se tekee mitään. Jos jokin tieto ei ole tiedostossa, sitä ei ole agentille olemassa. Kirjaa siis päätökset aina.

Ohjetiedosto elää edelleen. Kun huomaat jatkossa uuden säännön, lisäät sen ohjetiedostoon ja kirjaat lisäyksen päätöslokiin. Muuten agentti ei tiedä sitä seuraavalla kerralla.

## Sama työkierros yksin

Työpajan jälkeen työ etenee samalla kierroksella kuin työpajassa. Aloitat uuden istunnon ja annat K11:n. Valitset yhden tehtävän. Pyydät suunnitelman ja hyväksyt sen. Agentti toteuttaa, sinä tarkistat muutokset, ajat sovelluksen ja testaat. Lopuksi kirjaat päätöksen ja teet tallennuspisteen (commit).

Varaa kalenteriin kerran viikossa 60–90 minuuttia. Lyhyempi kerta jää helposti kesken, eikä pidempi ole tarpeen. Yksi tehtävä kerrallaan. Pienin askel on yksi testi. Jos testi tekee Wilma-tallennuksen, palautat ensin simuloidun Wilman lähtötilaan. Jos testi menee läpi, kirjaat sen. Jos ei, korjautat sen K5:llä tai viet sen jatkosuunnitelmaan. Aiempaa tulosta et pyyhi, vaan uusinta kirjataan sen alle.

Kolme pysäytyssääntöä pätee edelleen. Jos ongelma jatkuu kahden korjausyrityksen jälkeen, katkaiset kehän ja palaat tallennuspisteeseen. Jos et ymmärrä lupapyyntöä, et hyväksy sitä. Työkerta päättyy aina tallennuspisteeseen ja päätöslokin merkintään, vaikka tehtävä jäisi kesken.

**Pysähdy hetkeksi:** Mikä on seuraava pienin askel, jonka voit tarkistaa itse?

## Mitä et tee yksin

Kuvauspaketin osassa 29 on yksitoista avointa päätöstä, P01–P11. Jokaisella on vastuutaho. Esitietopalvelu (P01) ja pilotti (P10) kuuluvat toiminnan omistajalle ja IT:lle. Tallennustapa (P08) kuuluu toiminnan omistajalle. Primus-haku (P02) kuuluu Primus-pääkäyttäjälle ja IT:lle. Lomakekartta (P04) kuuluu Wilma-pääkäyttäjälle. Koulutukset (P05) ja vakiokentät (P06) kuuluvat koulutuksen vastuuhenkilölle. Säilytys (P09) kuuluu IT:lle ja tiedon omistajalle.

Osa päätöksistä on lähellä sinua. Haastattelun kirjaus (P03) on kirjaavan henkilöstön asia. Sinä tiedät, missä haastattelu on ja miten se kirjataan. Myös nykyisen tiedon käsittely (P07) ja sarja-ajon säännöt (P11) tarvitsevat sinun kokemustasi.

Roolisi on substanssi ja hyväksyntä. Kerrot, mikä on oikein, ja tarkistat sen testeillä. Et ratkaise yhteyksiä, käyttöoikeuksia tai asennusta. Oikeaa aineistoa ei käsitellä, ennen kuin salaus ja säilytys on ratkaistu (P09). Asennuspaketti ja jakelu ovat IT:n työtä. Pilotti on kuvauspaketin vaihe 7, ja siinä mukana ovat kaikki vastuutahot.

Kun puhut IT:n tai pääkäyttäjän kanssa, vie mukanasi `JATKO.md` ja `TESTIT.md`. Kerro, että työpajaversio on prototyyppi kuvitteellisella aineistolla. Älä lupaa sitä käyttöön. Sen arvo on siinä, että säännöt, testit ja avoimet kysymykset ovat jo kirjoitettuina.

## Testi-Wilman polku

Kun testi-Wilma on käytössä, etenet pienin askelin. Ensin luetaan. Lukeminen ei muuta mitään. Jos kenttä puuttuu tai on eriniminen, huomaat sen, ennen kuin mikään kirjoittaa. Kenttäluku käy läpi opiskelijan haun, urasuunnitelman ja Primus-tietojen näkymät. Sitten tehdään yksi testikirjaus urasuunnitelmaan, ja se varmennetaan uudelleenluvulla. Vasta sen jälkeen siirretään yksi sovitin kerrallaan testi-Wilmaan. Jokainen sovitin tehdään samalla työjärjestyksellä kuin K9:ssä.

Jokaisen askeleen jälkeen teet testit ja päätöksen. Testi-Wilman käyttö sovitaan Wilma-pääkäyttäjän kanssa, ja samat ehdot kuin osiossa 08 pätevät. Kirjaudut itse, eikä agentti avaa testi-Wilmaa.

## Milloin pyydät apua

Pyydä apua heti, jos kysymys koskee tietoturvaa. Pyydä apua, jos agentti kiertää kehää etkä pääse eteenpäin paluulla. Pyydä apua, jos et ymmärrä lupapyyntöä. Kaikki, mikä koskee oikeaa Wilmaa, kysytään, ennen kuin tehdään.

Seurantatapaamiset ovat noin kahden ja kuuden viikon päästä. Tuot niihin `JATKO.md`:n, `TESTIT.md`:n ja päätöslokin. Teette yhden työkierroksen yhdessä ja sovitte seuraavat askeleet.

**Pysähdy hetkeksi:** Mikä avoimista päätöksistä estää eniten seuraavaa askeltasi, ja kenen kanssa puhut siitä ensin?

## Esimerkki: kolme seuraavaa askelta

Osio 07 siirtyi jatkoon, ja työpajassa tehtiin B2. Jatkosuunnitelman kolme askelta voisivat olla nämä.

Askel 1: teen T04:n simuloidussa Wilmassa. Hyväksyn, kun Testileipomo Oy näyttää kaksi toimipaikkaa ja Kokeiluverstas Oy:n lisäys odottaa hyväksyntääni. Tarkistan hakemalla sovelluksella ja avaamalla simuloidun Wilman. En tarvitse ketään.

Askel 2: teen T10:n, koska en tehnyt B1:tä. Hyväksyn, kun katko pysäyttää jonon ja Eero Esimerkillä on simuloidussa Wilmassa yksi urasuunnitelma. En tarvitse ketään.

Askel 3: pyydän Wilma-pääkäyttäjältä oppisopimuslomakkeen kentät (P04). Hyväksyn, kun `KENTAT.md`:ssä ei ole oppisopimuksen kohdalla merkintää kartoitetaan. Tarkistan avaamalla `KENTAT.md`:n. Tarvitsen Wilma-pääkäyttäjän, koska oikean lomakkeen kentät eivät ole minun päätettävissäni.

## Yhteenveto

Työpajaversio on lähtökohta, ei valmis ohjelma. Agentti ei muista eilistä, mutta tiedostosi muistavat, ja K11 lukee ne. Teet yhden pienen askeleen kerrallaan ja tarkistat sen itse. Yhteydet, oikeudet, säilytys, asennus ja pilotti kuuluvat vastuutahoille, ja sinun roolisi niissä on substanssi ja hyväksyntä.
