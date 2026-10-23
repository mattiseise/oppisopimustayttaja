# Osio 05: Lähteet, puutteet ja ristiriidat

> Ajattelukysymys: Kun lähteet ovat eri mieltä tai tieto puuttuu, mitä ohjelma saa päättää ja mitä vain sinä?

Päivä 2 alkaa. Agentti ei muista eilistä keskustelua. Tiedostot muistavat: ohjetiedosto, työlista, päätösloki ja testit. Siksi aloitat uuden istunnon kehotepohjalla K11. Agentti lukee tiedostot ja kertoo, missä olette.

Eilen sovellus teki yhden varmennetun Wilma-tallennuksen. Arvot olivat valmiina. Tänään sovellus hakee arvot itse kolmesta lähteestä. Lähteet eivät aina ole samaa mieltä, ja joskus tieto puuttuu. Ohjelma ei saa paikata näitä kohtia arvaamalla.

Tässä osiossa agentti rakentaa tarkistusnäkymän, ja sinä testaat sen tahallisilla virheillä. Teet myös oman päätöksen siitä, miten valvot agentin muutoksia.

## Kolme lähdettä

Kuvauspaketin osa 4 nimeää oppisopimuksen tietolähteet. Tässä osiossa käytetään kolmea. Esitietolomakkeella opiskelija kertoo tietojaan etukäteen. Haastattelusta käytetään talteen kirjatut tiedot, kuten tavoitteet, työtehtävät ja työaika. Primuksen tiedot, kuten koulutus ja opiskeluoikeus, luetaan Wilman näkymistä, joissa ne näkyvät käyttäjälle. Tätä lukutapaa kutsutaan nimellä **WilmaRead** (kuvauspaketin osat 5 ja 16). Luku ei muuta Wilmassa mitään.

Ohjelma hakee tiedot automaattisesti. Sinä et vie tiedostoja mistään etkä kopioi arvoja. Tämä on testin T01 ydin. Kuvauspaketin osa 16 sanoo, ettei käsin tehty tiedostovienti korvaa automaattista hakua. Käsin viety tiedosto voi olla vanha, väärän opiskelijan tai puutteellinen, eikä kukaan huomaa sitä.

Jokainen lähde kytketään opiskelijaan opiskelijanumerolla, ei nimellä. Kuvitteellisessa aineistossa on kaksi Aino Testistä. Jos sovellus hakisi esitiedot nimellä, se voisi yhdistää toisen Ainon esitiedot ensimmäisen Ainon profiiliin. Tarkistusnäkymässä kaikki näyttäisi oikealta, koska nimi täsmää.

Työpajassa lähteet ovat kuvitteellisia. Esitiedot ja haastattelut ovat tiedostoja kansiossa `testiaineisto`. Profiili luetaan simuloidusta Wilmasta. Oikeissa lähteissä on vielä avoimia päätöksiä. Kuvauspaketin osa 29 nimeää ne: esitietopalvelu (P01), Primus-tietojen haku (P02) ja haastattelun kirjauspaikka (P03). Ne ratkaisevat IT ja pääkäyttäjät. Sinun osuutesi on kertoa, mitä tietoa työ tarvitsee.

## Kenttähavainto ja viisi lukutilaa

Sovellus ei säilytä pelkkää arvoa. Jokaisesta kentästä syntyy **kenttähavainto**, jossa on arvo, lähde ja lukutila. Lukutila kertoo, miten arvo saatiin. Kuvauspaketin osa 15 määrittelee viisi lukutilaa.

OK tarkoittaa, että kenttä luettiin ja arvo löytyi. EMPTY tarkoittaa, että kenttä näkyi, mutta oli tyhjä. NOT_VISIBLE tarkoittaa, ettei kenttä ollut näkymässä tai käyttäjän saatavilla. READ_FAILED tarkoittaa, että lukeminen epäonnistui, esimerkiksi yhteysvirheen takia. CONFLICT tarkoittaa, että lähteiden arvot ovat ristiriidassa.

EMPTY on rehellinen tieto. Kenttä on olemassa, ja se on tyhjä. Silloin pyydetään täydennys, jos tieto tarvitaan.

Tärkein ero on EMPTY:n ja NOT_VISIBLE:n välillä. Kuvittele, että palkkakenttä ei näy sinun roolillesi. Ohjelma ei silloin tiedä palkkaa. Se ei tarkoita, että palkkaa ei ole. Jos ohjelma näyttäisi kentän tyhjänä, joku täyttäisi sen arvaamalla tai jättäisi sen pois. Molemmat olisivat väärin. Kuvauspaketin osa 5 sanoo saman: puuttuvaa käyttöoikeutta ei tulkita tyhjäksi tiedoksi.

READ_FAILED toimii samalla periaatteella. Jos Wilma ei vastaa, ohjelma ei saa näyttää onnistunutta tyhjää hakua. Virhe näytetään virheenä. Testaat molemmat tilanteet testikytkimillä. Toinen kytkin piilottaa kentän, toinen sammuttaa simuloidun Wilman.

Lukutila näytetään myös sanoina, ei pelkkänä koodina tai värinä. Ohjetiedostossa on tästä sääntö.

**Pysähdy hetkeksi:** Minkä tiedon arvaaminen aiheuttaisi suurimman vahingon?

## Ristiriita: sinä ratkaiset

Liisa Kokeilun haastattelussa työaika on 37,5 h viikossa. Esitietolomakkeella se on 30 h. Kuvauspaketin osa 8 sanoo, että ohjelma näyttää molemmat arvot. Työntekijä selvittää oikean tiedon ennen Wilma-tallennusta.

Ohjelma ei siis valitse uudempaa lähdettä. Se ei valitse myöskään lähdettä, joka tuntuu luotettavammalta. Haastattelu voi olla uudempi, mutta opiskelija on voinut muistaa väärin. Esitiedot voivat olla vanhat, mutta työsopimus on voinut muuttua. Oikean vastauksen tietää vain se, joka selvittää asian.

Kun valitset, valinta kirjataan. Myöhemmin näkyy, mistä arvo tuli ja että sen valitsi ihminen. Oikeassa työssä selvittäisit työajan opiskelijalta tai työpaikalta. Testissä valitset itse.

**Pysähdy hetkeksi:** Muistatko tilanteen, jossa kaksi lähdettä kertoi saman asian eri tavalla? Miten selvitit oikean tiedon?

Puute on eri asia kuin ristiriita. Puutteessa tietoa ei saada mistään lähteestä. Kuvauspaketin osa 15 sanoo, että pakollisen tiedon puute estää siitä riippuvan kirjauksen. Liisan palkasta puuttuu yksikkö. Sitä testataan osiossa 07, kun oppisopimus rakennetaan.

## Hyväksyntä sidotaan sisältöön

Tarkistusnäkymässä hyväksyt sisällön. Hyväksyntä koskee juuri niitä arvoja, jotka näit. Jos arvo muuttuu hyväksynnän jälkeen, hyväksyntä vanhenee. Silloin hyväksyt uudelleen.

Ilman tätä sääntöä hyväksyntä 30 tunnista kelpaisi myös 37,5 tunnille. Kukaan ei olisi tarkistanut uutta arvoa. Kuvauspaketin osa 20 sitoo hyväksynnän kohteeseen ja sisältöversioon.

Sisältö voi muuttua kahdella tavalla. Korjaat itse arvoa tarkistusnäkymässä, tai sovellus lukee lähteen uudelleen ja saa eri arvon. Kummassakin tapauksessa vanha hyväksyntä ei enää koske sitä, mitä Wilmaan menisi. Urasuunnitelman Wilma-tallennus käyttää vain voimassa olevaa hyväksyntää.

Sovelluksen hyväksyntä ja päätöslokin päätös ovat eri asioita. Sovelluksessa hyväksyt opiskelijan tiedot ennen Wilma-tallennusta. Päätöslokiin kirjaat, kelpaako agentin tekemä työ.

## Oma lupa-asetus

Tähän asti agentti on kysynyt luvan ennen jokaista tiedostomuutosta. Tämä on lupatilan oletus. Tänään agentti rakentaa viisi palaa, ja lupapyyntöjä tulee paljon. Kun niitä tulee paljon, niitä alkaa hyväksyä lukematta. Silloin kontrolli on vain näennäinen.

Voit sallia tiedostomuutokset automaattisesti. Silloin agentti ei kysy lupaa tiedostomuutoksille. Komennoille lupapyyntö pidetään päällä. Kontrolli siirtyy kahteen kohtaan. Teet tallennuspisteen (commit) ennen palaa ja katsot muutosnäkymän palan jälkeen. Jos muutosnäkymässä on jotain, mitä et pyytänyt, palaat tallennuspisteeseen.

Kumpikin ratkaisu käy, kun tarkistus tehdään. Väärä ratkaisu on sallia muutokset ja jättää muutosnäkymä katsomatta. Työkortin sääntö pysyy: et salli kaikkea automaattisesti.

Muutosnäkymästä katsot ensin tiedostojen nimet. Sovelluksen ja simuloidun Wilman tiedostot saavat muuttua, kun pyysit palaa. Kansioiden `maarittely` ja `testiaineisto` ei pidä muuttua. Omia tiedostojasi agentti ei muokkaa: päätöslokia, hyväksymiskriteereitä ja testien tuloksia. Jos niissä näkyy muutos, jota et itse tehnyt, kysy syytä, ennen kuin jatkat.

Kirjaat päätöksen päätöslokiin. Kirjoitat myös oman pysäytyssäännön. Se kertoo, mikä muutos saa sinut hylkäämään. Esimerkiksi: jos kansiossa `testiaineisto` muuttui jotain, mitä en pyytänyt, hylkään.

**Pysähdy hetkeksi:** Kumpi pitää sinut tarkkana: monta pientä lupapyyntöä vai yksi huolellinen tarkistus palan lopussa?

## Esimerkki: Liisa Kokeilun tarkistusnäkymä

Avaat Liisa Kokeilun (002024) tiedot. Koulutus on Testikoulutus. Lähde on profiili, ja lukutila on OK. Työajan kohdalla lukee CONFLICT ja sanoin ristiriita. Alla ovat molemmat arvot: 37,5 h/vko haastattelusta ja 30 h/vko esitiedoista. Kumpaakaan ei ole valittu.

Palkan kohdalla on 2 450. Lähde on haastattelu, mutta yksikkö puuttuu. Panet sen merkille osiota 07 varten.

Valitset työajaksi 37,5 h. Sovellus näyttää valintasi ja sen, että valinnan teki käyttäjä. Hyväksyt sisällön. Sitten työpaikka kertoo, että sovittu työaika on 30 h. Korjaat arvon. Hyväksyntä näkyy heti vanhentuneena, eikä Wilma-tallennus käynnisty. Tarkistat sisällön ja hyväksyt sen uudelleen.

Kaikki esimerkin tiedot ovat kuvitteellisia.

## Yhteenveto

Sovellus hakee tiedot kolmesta lähteestä ja näyttää jokaisesta kentästä arvon, lähteen ja lukutilan. Piilossa oleva tai lukematon kenttä ei ole tyhjä. Ristiriidassa ohjelma näyttää molemmat arvot, ja sinä valitset. Hyväksyntä koskee vain sitä sisältöä, jonka näit. Lupa-asetuksen päätät itse, mutta muutokset tarkistetaan aina.
