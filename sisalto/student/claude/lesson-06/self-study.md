# Osio 06: Opiskelijalista ja työjono

> Ajattelukysymys: Voiko jono avata seuraavan opiskelijan tai kirjoittaa väärälle henkilölle, ja millä testillä sen osoitat?

Tähän asti sovellus on käsitellyt yhden opiskelijan kerrallaan, ja sinä olet valinnut hänet. Oikeassa työssä käsittelet usein koko listan. Kuvauspaketin osat 9 ja 20 kuvaavat, miten lista muuttuu työjonoksi.

Jono säästää aikaa, mutta se tuo kaksi uutta riskiä. Jono voi kirjoittaa väärälle henkilölle, jos nimi tulkitaan väärin. Jono voi myös merkitä opiskelijan valmiiksi liian aikaisin ja siirtyä eteenpäin. Tässä osiossa testaat molemmat.

Teet myös päätöksen, jota kuvauspaketti ei tee puolestasi. Päätät, mitä nimiä jonon tiloilla on.

## Lista muuttuu työjonoksi

Kuvauspaketin osa 1 kuvaa tavoitteen. Kun yhden opiskelijan kirjaukset on tehty ja tarkistettu, ohjelma merkitsee hänet valmiiksi ja avaa seuraavan. Sinun ei tarvitse etsiä seuraavaa nimeä listalta itse. Jonosta näet myös, montako opiskelijaa on valmiina ja montako odottaa.

Lista tuodaan CSV-tiedostosta tai liittämällä nimilista. Excel-tiedoston tuonti on lisätavoite. Ennen käsittelyä sovellus näyttää **tuonnin esikatselun**. Siinä näet, miten sovellus tulkitsi jokaisen rivin. Tyhjät rivit ja virherivit näkyvät erikseen. Kohdistat itse sarakkeet: mikä sarake on nimi, mikä opiskelijanumero ja mikä koulutus. Kaksi samanlaista nimiriviä tarkistetaan erikseen, koska ne voivat tarkoittaa eri ihmisiä (kuvauspaketin osa 20).

Opiskelijanumerot käsitellään tekstinä. Silloin etunollat säilyvät. Aino Testisen numero on 000123. Jos se luettaisiin lukuna, siitä tulisi 123, eikä se enää vastaisi ketään. Excel tekee tämän helposti, kun CSV avataan ja tallennetaan. Siksi tarkistat CSV:n Muistiolla.

Alkuperäistä listaa ei muuteta (kuvauspaketin osa 10). Sovellus pitää kirjaa omassa jonossaan. Jos merkitsisit valmiit Excel-tiedostoon, merkintä ei todistaisi mitään Wilmasta. Se kertoisi vain, että joku kirjoitti sanan valmis.

Jonossa on aina yksi **aktiivinen opiskelija**. Sovellus lukee hänen lähteensä ja Wilman nykytilan. Sinä tarkistat ja hyväksyt juuri hänen sisältönsä. Kuvauspaketin osa 14 sanoo saman tekniseltä puolelta: yhdellä jonolla on yksi aktiivinen opiskelija.

## Nimi on hakusyöte, ei kirjoituskohde

Kuvauspaketin osa 20 erottaa kaksi asiaa. Nimellä haetaan. Kirjoitus tehdään vasta, kun opiskelija ja opiskeluoikeus on tunnistettu yksiselitteisesti.

Kuvitteellisessa aineistossa on kaksi Aino Testistä. Toinen on ryhmässä TK26A ja hänen numeronsa on 000123. Toinen on ryhmässä TK26B ja hänen numeronsa on 000456. Eero Esimerkillä on kaksi opiskeluoikeutta: Testikoulutus ja Esimerkkikoulutus. Nimilistassa lukee vain Aino Testinen ja Eero Esimerkki. Kumpikaan nimi ei kerro, kenelle kirjoitetaan.

Sovellus näyttää silloin vaihtoehdot ja niiden erottavat tiedot, kuten opiskelijanumeron, ryhmän ja koulutuksen. Sinä valitset. Ensimmäistä hakutulosta ei arvata oikeaksi. Ei silloinkaan, kun nimi on harvinainen. Harvinainen nimi voi silti olla kahdella ihmisellä, ja yhdellä ihmisellä voi olla kaksi opiskeluoikeutta.

Opiskeluoikeus on yhtä tärkeä kuin henkilö. Jos Eeron urasuunnitelma menee väärän koulutuksen alle, henkilö on oikea, mutta kirjaus väärä. Kun listassa on opiskelijanumero, kohdistus on helpompi. Sovellus varmistaa silti henkilön ja koulutuksen ennen Wilma-tallennusta (kuvauspaketin osa 9).

**Pysähdy hetkeksi:** Jos ohjelma valitsisi ensimmäisen Aino Testisen, kuka huomaisi virheen ja milloin?

## Jonon tilat ja kuvauspaketin ristiriita

Jokaisella opiskelijalla on jonon tila. Se näytetään sanana, ei pelkkänä värinä. Kuvauspaketin osa 9 nimeää kuusi jonon tilaa: Odottaa, Valittava opiskelija, Käsittelyssä, Odottaa lisätietoja, Tarkistettava tallennus ja Valmis.

Osan 9 nimet kertovat, mitä sinulta odotetaan. Odottaa tarkoittaa, että opiskelija on jonossa käsittelemättä. Valittava opiskelija tarkoittaa, että sinun pitää valita oikea henkilö tai koulutus. Käsittelyssä on aktiivinen opiskelija. Odottaa lisätietoja tarkoittaa, että jokin tieto puuttuu ja olet siirtänyt opiskelijan sivuun. Tarkistettava tallennus tarkoittaa, että ohjelma selvittää, tallentuiko tieto. Valmis tarkoittaa, että kaikki on tehty ja tarkistettu Wilmasta.

Kuvauspaketissa on tässä kohdassa ristiriita. Osassa 9 Odottaa tarkoittaa, ettei opiskelijaa ole vielä käsitelty. Puuttuvasta tiedosta käytetään nimeä Odottaa lisätietoja. Osa 20 käyttää sanaa ODOTTAA juuri puutteen merkityksessä. Jos sovellus seuraa molempia, sama sana tarkoittaa kahta eri asiaa. Silloin et näe jonosta, onko opiskelija käsittelemätön vai jumissa.

Sinä päätät, mitä nimiä sovelluksesi käyttää. Suositus on osan 9 nimet, koska niissä jokaisella jonon tilalla on oma sanansa. Voit valita myös toisin, kunhan yksi sana tarkoittaa vain yhtä asiaa. Kirjaat päätöksen ja perusteen päätöslokiin. Tämä materiaali käyttää osan 9 nimiä. VALMIS kirjoitetaan isoin kirjaimin kuten kuvauspaketin osassa 20.

**Pysähdy hetkeksi:** Millä sanalla kutsut nyt opiskelijaa, jonka paperit puuttuvat? Ymmärtäisikö kollegasi sanan samoin?

## VALMIS ja seuraava

Opiskelija on VALMIS vasta, kun kaikki hänelle valitut tehtävät on hyväksytty, tallennettu Wilmaan ja uudelleenluettu (kuvauspaketin osat 10 ja 20). Työpajassa valittu tehtävä on urasuunnitelma. Kun oppisopimus tulee mukaan, VALMIS vaatii senkin.

Kun opiskelija on VALMIS, sovellus avaa seuraavan käsittelemättömän opiskelijan itsestään. Seuraavan sisältö pysähtyy taas tarkistettavaksi. Edellisen arvot ja hyväksyntä eivät siirry. Jos Aino Testisen hyväksyntä jäisi voimaan, Eero Esimerkin tiedot voisivat mennä Wilmaan kenenkään tarkistamatta.

**Pysähdy hetkeksi:** Mitä tapahtuu, jos ohjelma avaa seuraavan opiskelijan ja edellisen hyväksyntä jää voimaan?

Puuttuva tieto ei ohita opiskelijaa automaattisesti. Sinä voit siirtää opiskelijan odottamaan lisätietoja, mutta vain perustelun kanssa. Ville Testaajalta puuttuu esitietolomake. Perustelu kertoo myöhemmin sinulle tai kollegalle, miksi hän odottaa ja mitä puuttuu.

Tarkistettava tallennus on eri asia. Silloin sovellus ei tiedä, tallentuiko tieto Wilmaan. Jono pysähtyy, eikä sitä kierretä siirtämällä opiskelijaa odottamaan. Tätä testataan osiossa 08.

## Jono muistaa

Jono säilyy, kun sovellus suljetaan ja avataan. Muuten keskeneräinen työ katoaisi joka kerta. Kuvauspaketin osa 10 sanoo, että jonon voi pysäyttää ja sitä voi jatkaa myöhemmin. Saman listan tuominen uudelleen ei käynnistä valmista opiskelijaa alusta. Sovellus tunnistaa opiskelijan pysyvästä tunnisteesta, ei nimestä.

Lähtötiedoston muuttumattomuuden tarkistat Gitillä ja Muistiolla. Git näyttää, onko tiedosto muuttunut sen jälkeen, kun se tuli tallennuspisteeseen (commit). Muistiossa näet itse, että etunollat ja rivit ovat ennallaan.

Testit tehdään tunnetusta tilanteesta. Ennen testiä palautat lähtötilan tiedostolla `palauta-lahtotila.cmd`. Se poistaa testien urasuunnitelmat ja tyhjentää sovelluksen jonon. Muuten sovellus löytää vanhan kirjauksen, ja testi mittaa jotain muuta kuin aiot. Testi jatkaa edellisestä vain silloin, kun se tarkistaa juuri jatkumista, kuten jonon säilymistä.

## Esimerkki: kahden opiskelijan jono

Liität nimilistan: Aino Testinen ja Eero Esimerkki. Esikatselussa on kaksi riviä. Aloitat käsittelyn. Ainon jonon tila on Valittava opiskelija. Sovellus näyttää kaksi vaihtoehtoa: 000123 ryhmästä TK26A ja 000456 ryhmästä TK26B. Valitset 000123. Eerolle valitset Testikoulutuksen.

Aino on Käsittelyssä. Hyväksyt sisällön ja teet Wilma-tallennuksen. Ennen uudelleenlukua Ainoa ei voi merkitä valmiiksi. Kun Wilma-tallennus on varmennettu, Ainon kohdalla lukee VALMIS. Eero avautuu. Hänen työaikansa on 30 h/vko, ei Ainon 37,5 h/vko. Mitään ei ole hyväksytty. Aloitat tarkistuksen alusta.

Kaikki esimerkin tiedot ovat kuvitteellisia.

## Yhteenveto

Lista muuttuu työjonoksi, jossa yksi opiskelija on kerrallaan aktiivinen. Nimi on vain hakusyöte, ja sinä valitset nimikaimoista ja opiskeluoikeuksista. VALMIS tulee vasta varmennuksen jälkeen, ja seuraava alkaa ilman edellisen tietoja. Jonon tilojen nimet päätät itse kuvauspaketin ristiriidan perusteella.
