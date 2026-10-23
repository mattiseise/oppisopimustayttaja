# Osio 03: Simuloitu Wilma ja kuvitteellinen aineisto

> Ajattelukysymys: Kattaako kuvitteellinen aineisto ne tilanteet, joissa oikea kirjaus menee helpoimmin väärin?

Tähän asti agentti on kirjoittanut tekstiä: työkortin, ohjetiedoston ja työlistan. Nyt se rakentaa ensimmäisen ohjelman. Ohjelma ei ole vielä Oppisopimustäyttäjä. Se on simuloitu Wilma, jota vasten Oppisopimustäyttäjää testataan.

Samalla agentti tekee kuvitteellisen aineiston. Sinä päätät, mitä tapauksia siinä on. Tiedät, missä kirjaus menee oikeassa työssä väärin. Agentti ei tiedä.

Osion lopussa projektikansiossa on simuloitu Wilma, testiaineisto, kenttäkartoitus ja hyväksymistestien runko. Käytät niitä työpajan loppuun asti.

## Miksi simuloitu Wilma

**Simuloitu Wilma** on projektikansiossa ajettava kuvitteellinen testisivusto. Se jäljittelee niitä Wilman näkymiä, joita sovellus tarvitsee. Sillä ei ole yhteyttä oikeaan Wilmaan. Se avautuu paikallisesta osoitteesta vain sinun koneellasi. Avaat sen Edgessä.

Tässä osiossa simuloituun Wilmaan tulee vain se, mitä osio 04 tarvitsee. Jokaisella sivulla lukee SIMULOITU. Kirjautuminen tehdään valitsemalla testikäyttäjä ilman salasanaa. Opiskelijan voi hakea nimellä ja opiskelijanumerolla. Profiilissa näkyvät Primus-tiedot, joita ei voi muuttaa. Urasuunnitelma avataan samalla polulla kuin kuvauspaketin osassa 6: Ohjaus ja tuki → Urasuunnitelmat → Lisää uusi. Wilma-tallennus säilyy tiedostossa, vaikka simuloitu Wilma suljetaan.

Simuloitu Wilma käynnistetään ilman agenttia. Testaat sovellusta myös silloin, kun agentti ei ole auki. Siksi kokeilet käynnistyksen itse jo tässä osiossa. Kaksoisnapsautat projektikansion käynnistystiedostoa, ja simuloitu Wilma käynnistyy. Avautuva ikkuna on auki niin kauan kuin simuloitu Wilma on käynnissä. Suljet sen sulkemalla ikkunan. Ohje on tiedostossa `KAYNNISTYS.md`.

Simuloidulla Wilmalla on kolme etua. Se on turvallinen, koska siinä ei ole oikeita tietoja. Se on toistettava. Voit tehdä saman kirjauksen kymmenen kertaa ja aloittaa alusta. Sen voi myös rikkoa tahallaan. Oikeaa Wilmaa ei rikota testin takia.

Simuloitu Wilma ei todista kaikkea. Se ei kerro, millaiset kentät oikeassa Wilmassa on. Se ei kerro, mitä oikeuksia roolillasi on. Se ei kerro, miten kirjautuminen toimii oppilaitoksen koneella. Nämä selvitetään testi-Wilmassa ja jatkossa.

Agentti rakentaa sekä simuloidun Wilman että sovelluksen. Ne sopivat yhteen, koska sama tekijä teki molemmat. Jos agentti ymmärsi urasuunnitelman väärin, molemmat ovat väärin samalla tavalla. Testi menee silti läpi. Siksi sinun vertailusi oikeaan työhön on tärkeä. Sinä tiedät, millainen oikea lomake on.

**Pysähdy hetkeksi:** Mitä simuloidussa Wilmassa läpäisty testi ei vielä kerro oikeasta Wilmasta?

## Kuvitteellinen aineisto

Testiaineisto ei ole otos oikeista opiskelijoista. Se on kokoelma tilanteita, joissa kirjaus menee helposti väärin. Jokainen tapaus on valittu syystä.

Aineiston henkilöt ovat keksittyjä. Aino Testisiä on kaksi, opiskelijanumeroilla 000123 ja 000456. He ovat nimikaimoja. Sillä testataan, ettei nimi yksin riitä. Eero Esimerkillä on kaksi opiskeluoikeutta, joten oikea koulutus pitää valita. Liisa Kokeilun työaika on haastattelussa 37,5 tuntia ja esitiedoissa 30 tuntia viikossa. Hänen palkkansa on 2 450 ilman yksikköä. Ville Testaajan esitietolomake puuttuu. Testileipomo Oy:llä on kaksi toimipaikkaa, Keskusta ja Satama.

Opiskelijanumerot alkavat nollalla. Se on tahallista. Excel voi muuttaa numeron 001789 muotoon 1789. Silloin oikeaa opiskelijaa ei löydy, tai löytyy väärä. Siksi CSV-tiedosto tarkistetaan Muistiolla, ei Excelillä.

Opiskelijalistassa on lisäksi tyhjä rivi ja virherivi, jonka opiskelijanumero on 12A. Sovelluksen pitää näyttää ne, ei ohittaa niitä hiljaa.

Nämä tapaukset tulevat kuvauspaketista. Sinun työssäsi voi olla muita. Kirjoitat vähintään yhden tapauksen omasta kokemuksestasi. Hyvä tapaus on tilanne, joka on oikeassa työssä mennyt väärin tai melkein mennyt.

Kuvitteellista aineistoa ei tehdä muokkaamalla oikeaa. Jos vaihdat oikean opiskelijan nimen, hänen tilanteensa voi silti tunnistaa. Keksi tilanne alusta. Käytä vain keksittyjä nimiä ja tunnisteita. Henkilötunnuksia, Y-tunnuksia, osoitteita, puhelinnumeroita ja sähköposteja ei käytetä lainkaan. Kehotepohja K8 muistuttaa tästä joka kerta.

**Pysähdy hetkeksi:** Mikä tilanne on oikeassa työssä johtanut väärään kirjaukseen, ja miten se näkyisi testiaineistossa?

## Kenttäkartoitus

Sovelluksen pitää tietää, mistä kukin tieto tulee ja mihin kenttään se menee. Tätä kutsutaan **kenttäkartoitukseksi**. Se kirjataan tiedostoon `KENTAT.md`.

Jokaisesta kentästä kirjataan tieto, sen lähde ja simuloidun Wilman kenttä. Esimerkiksi tieto on urasuunnitelman tavoite, lähde on haastattelu ja kenttä on urasuunnitelman tavoitekenttä. Lisäksi kirjataan, miten tallentuminen tarkistetaan.

Jos kytkentää ei ole selvitetty, kenttään kirjoitetaan "kartoitetaan". Kuvauspaketin osa 19 sanoo, että merkintä on tietoinen este. Sovellus ei saa arvata kenttää, jonka kohdalla lukee "kartoitetaan".

Sinun osuutesi on Oma huomio -rivi. Kirjoitat siihen, eroaako simuloidun Wilman kenttä siitä, mitä muistat oikeasta Wilmasta. Kirjoitat muistista. Oikeasta Wilmasta ei oteta kuvakaappauksia agentille.

Huomiosi ei muuta simuloitua Wilmaa heti. Se on kuitenkin ainoa paikka, jossa ero näkyy. Jos oikeassa Wilmassa on pakollinen kenttä, jota simuloidussa ei ole, sovellus ei täytä sitä. Simuloidussa Wilmassa kaikki näyttää toimivan. Testi-Wilmassa sama kirjaus pysähtyisi. Huomiosi kertoo jatkossa, mistä aloitetaan.

**Pysähdy hetkeksi:** Mikä urasuunnitelman kenttä on sinusta pakollinen, ja mistä tiedät sen?

## Hyväksymistestit tarkistuslistana

Kuvauspaketin osassa 28 on 22 hyväksymistestiä, T01–T22. **Hyväksymistesti** on testi, jonka teet tarkistuslistana ajamalla sovellusta. Et lue koodia. Teet kirjauksen ja katsot, mitä tapahtuu.

Kaikkia testejä ei tehdä työpajassa. Osa vaatii testi-Wilman, osa oikean säilytysratkaisun. Tiedostossa `TESTIT.md` jokaisella testillä on merkintä työpaja, lisä tai jatko. Merkintä tulee työlistalta.

Esimerkiksi T05 sanoo, että hyväksytyt arvot löytyvät uudelleen avatulta oikean opiskelijan lomakkeelta. Teet sen näin. Avaat simuloidun Wilman, haet opiskelijan opiskelijanumerolla ja avaat urasuunnitelman. Vertaat arvoja hyväksymiisi kenttä kerrallaan.

Agentti tekee tiedostosta rungon. Tuloksen kirjoitat aina itse Muistiolla. Tulos on läpi, ei läpi tai ei testattu, ja sen perässä on oma havaintosi. Omat testisi numeroidaan O01, O02 ja niin edelleen. Jos teet testin uudelleen, aiempaa tulosta ei pyyhitä. Uusinta kirjataan testin alle omalle rivilleen.

Testin tulos ei saa riippua siitä, mitä aiemmat testit jättivät simuloituun Wilmaan. Siksi simuloidulla Wilmalla on **lähtötila**: opiskelijat, profiilit ja yksi aiempi urasuunnitelma Aino Testisellä 000456. Palautat sen kaksoisnapsauttamalla tiedostoa `palauta-lahtotila.cmd`. Palautus ei koske omia tiedostojasi, kuten päätöslokia ja `TESTIT.md`:tä. Jokaisen testin Lähtötila-rivillä lukee, aloitetaanko palautuksesta vai jatketaanko edellisestä testistä.

Osa testeistä tarvitsee virheen, jota ei tavallisesti tapahdu. Siihen käytetään **testikytkintä**. Se on simuloidun Wilman asetus, joka aiheuttaa tahallisen virheen. Kytkin voi esimerkiksi tallentaa yhden kentän väärin. Ensimmäinen kytkin lisätään osiossa 04.

## Esimerkki: kaksi Aino Testistä

Haet simuloidusta Wilmasta nimellä Aino Testinen. Tuloksia on kaksi. Toinen on ryhmästä TK26A ja toinen ryhmästä TK26B.

Tilanne on aineistossa tarkoituksella. Jos sovellus valitsisi ensimmäisen hakutuloksen, urasuunnitelma voisi mennä väärälle Ainolle. Simuloidussa Wilmassa virheestä ei seuraa vahinkoa. Oikeassa työssä seuraisi.

Ainolla 000456 on lähtötilassa yksi aiempi urasuunnitelma. Osiossa 04 sovellus kirjaa urasuunnitelman Ainolle 000123. Sen jälkeen tarkistat, että Ainon 000456 urasuunnitelma on ennallaan. Testi kertoo jotain vain siksi, että aineistossa on kaksi samannimistä.

## Yhteenveto

Simuloitu Wilma on turvallinen ja toistettava testisivusto. Se ei todista oikean Wilman kenttiä, oikeuksia eikä kirjautumista. Kuvitteellinen aineisto koostuu tilanteista, joissa kirjaus menee helposti väärin, ja sinä lisäät siihen oman tapauksesi. Kenttäkartoitus kertoo, mistä tieto tulee ja mihin se menee. Hyväksymistestit tehdään tarkistuslistana, ja tuloksen kirjoitat aina itse.
