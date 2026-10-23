# Osio 08: Hyväksymistestit ja häiriötilanne

> Ajattelukysymys: Mitä hyväksymistestisi osoittavat, ja mitä ne eivät vielä osoita?

Tämä osio on työpajan tarkistuspiste. Et rakenna uutta, paitsi yhden testikytkimen. Teet hyväksymistestit tarkistuslistana, testaat yhden häiriötilanteen ja korjautat yhden virheen. Lopuksi päätät, hyväksytkö työpajaversion.

Agentin valmis ei ole testitulos. Sanoit tämän itsellesi osiossa 04, ja se pätee nyt vielä tiukemmin. Agentti on rakentanut sovelluksen. Sinä päätät, kelpaako se.

## Sinä hyväksyt, et agentti

Hyväksymistestissä ajat sovellusta ja katsot tuloksen itse. Kirjaat yhden kolmesta: läpi, ei läpi tai ei testattu. Agentti voi kertoa, että sen automaattiset testit menivät läpi. Se on agentin työkalu, ei sinun testitulosesi.

Teet myös aiemmat testit uudelleen. Osion 06 jono on voinut rikkoa osion 04 urasuunnitelman, eikä kukaan huomannut. Sitä ei tiedä, ennen kuin kokeilee.

Ennen testiä, joka tekee Wilma-tallennuksen, palautat simuloidun Wilman lähtötilaan. Silloin tulos ei riipu siitä, mitä aiemmat testit jättivät jälkeensä. Ilman palautusta oikein toimiva kaksoiskappaleen esto voisi näyttää virheeltä. Aiempi tulos jää `TESTIT.md`:hen, ja uusinta kirjataan sen alle omalle rivilleen.

Ei läpi on tietoa, ei epäonnistuminen. Se kertoo, mitä korjata tai mitä jättää jatkoon. Ei testattu on rehellinen merkintä. Se on parempi kuin läpi ilman havaintoa.

Havainto on se, mitä näit itse. Hyvä havainto T05:een on esimerkiksi tämä: "Avasin simuloidun Wilman. Aino Testisen (000123) urasuunnitelmassa oli hyväksymäni tavoiteteksti. Toisen Aino Testisen (000456) tiedot eivät muuttuneet." Huono havainto on "toimii" tai "agentti sanoi valmis". Niistä ei näe, mitä tarkistit.

## Mitä testit eivät osoita

Testi osoittaa vain sen, mitä se testasi. Simuloitu Wilma ei ole oikea Wilma. Agentti rakensi sekä simulaation että sovelluksen, joten ne sopivat yhteen. Oikean Wilman kentät, oikeudet ja kirjautuminen voivat olla toisenlaiset.

Kuvitteellinen aineisto ei ole oikea aineisto. Oikeassa listassa voi olla tapauksia, joita kukaan ei keksinyt. Yksi ajo ei myöskään kata kaikkia tilanteita. Kuvauspaketin osa 27 sanoo saman: käyttöliittymän testi ei yksin todista, että tieto tallentui palveluun.

**Pysähdy hetkeksi:** Minkä testin tulos yllätti sinut eniten?

## Häiriötilanne: katko Wilma-tallennuksen jälkeen

Kuvittele, että sovellus lähettää urasuunnitelman Wilmaan ja yhteys katkeaa. Wilma-tallennus saattoi onnistua. Sovellus ei tiedä. Kuvauspaketin osa 22 antaa tälle operaation tilan Tallennustulos tuntematon.

Silloin sovellus ei yritä uudelleen sokkona. Se pysäyttää jonon, ja opiskelijan jonon tila on Tarkistettava tallennus. Sovellus lukee ensin Wilman nykytilan. Jos Wilma-tallennus onnistui, se varmennetaan. Jos ei, sen voi tehdä hallitusti uudelleen. Jos sovellus yrittäisi heti uudelleen, opiskelijalle voisi syntyä kaksi urasuunnitelmaa. Kumpikaan ei näyttäisi virheeltä.

Testi T10 tarkistaa tämän. Simuloituun Wilmaan tulee testikytkin, joka katkaisee yhteyden heti Wilma-tallennuksen jälkeen. Ennustat ensin, mitä sovelluksen pitää näyttää. Sitten ajat ja vertaat.

## Ilme ja näppäimistö

Testi T14 tarkistaa PRO-ilmeen ja saavutettavuuden. Lukutilat ja jonon tilat näkyvät sanoina, ei pelkkänä värinä. Virhe näkyy tekstinä. Sovellusta voi käyttää pelkällä näppäimistöllä. Värit vertaat ohjetiedoston kohtaan Ulkoasu.

## Testi-Wilma

Jos testi-Wilma on käytössä, luet sen kenttiä kenttäluvulla. Moni asia muuttuu. Kirjautuminen on oikea, ja se voi vaatia lisätunnistautumisen. Kentät ovat oikeat, eivätkä ne välttämättä vastaa simuloitua Wilmaa. Testi-Wilmasta saatu aineisto puhdistetaan, ennen kuin agentti näkee sen. Kaksi asiaa pysyy ennallaan. Agentti ei saa tunnuksia, ja sinä kirjaudut itse. Siksi tietoturvan muistilista luetaan ääneen, ennen kuin aloitat:

- Ei oikeaa opiskelijatietoa agentille: ei kehotteeseen, tiedostoon eikä kuvaan.
- Ei salasanoja eikä tunnuksia agentille.
- Kirjaudut itse näkyvässä selaimessa.
- Luet lupapyynnön ennen hyväksymistä.
- Et valitse täysiä oikeuksia.
- Oikea Wilma ei kuulu työpajaan.
- Testi-Wilmasta saatu aineisto puhdistetaan kuvauspaketin liitteen A mukaan ennen agenttia.
- Projektikansio ei ole OneDrivessa.
- Epäilet tietovuotoa: pysähdyt ja kerrot vetäjälle.

Lisäksi sovellus ei tallenna selaimen istuntoa, evästeitä eikä tallenteita. Käynnistät sovelluksen itse `KAYNNISTYS.md`:n mukaan. Agentti ei avaa testi-Wilmaa. Hiekkalaatikko estää agentin verkkoyhteydet ilman hyväksyntää, etkä hyväksy pyyntöä, joka koskee testi-Wilmaa. Testi-Wilmaan ei kirjoiteta mitään. Kenttäluku kirjoittaa tulosteen projektikansion ulkopuolelle. Luet sen itse ja kirjoitat havainnot `KENTAT.md`:hen omin sanoin. Agentti ei näe tulostetta. Ennen tallennuspistettä (commit) tarkistat, ettei projektikansioon tullut selainprofiilia, evästeitä eikä tallenteita.

## Työpajaversio ja hyväksymispäätös

Työpajaversio on sovelluksen tila työpajan lopussa. Vähimmäistavoite on tämä. Simuloitu Wilma ja sovellus käynnistyvät ohjeella ilman agenttia. Sovellus avaa selaimen, jossa kirjaudut itse. Se hakee yhden opiskelijan tiedot kuvitteellisista lähteistä ja näyttää ne tarkistettavina. Se tekee urasuunnitelman Wilma-tallennuksen ja lukee lomakkeen uudelleen. Kahden opiskelijan jonossa seuraava avautuu vasta, kun edellinen on varmennettu. Lisäksi sinulla on omat tiedostosi: säännöt, työlista, päätösloki, hyväksymiskriteerit, testitulokset ja jatkosuunnitelma.

Tavoite on laajempi. Silloin sovellus näyttää myös puuttuvat ja ristiriitaiset tiedot. Se tuo opiskelijalistan, erottaa samannimiset opiskelijat ja osaa jättää opiskelijan odottamaan lisätietoja. Se kirjaa oppisopimuksen tiedot oikeassa järjestyksessä. Ulkoasu noudattaa PRO-ilmettä, ja yksi häiriötilanne on testattu. Jos testi-Wilma on käytössä, kokeilet myös sen kenttien lukemista.

Hyväksyn tarkoittaa: tämä on työpajaversio, jonka päälle jatko rakennetaan. Se ei tarkoita, että sovellus on valmis käyttöön. Korjautan tarkoittaa, että jokin vähimmäistavoitteen kohta ei toimi ja pyydät agenttia korjaamaan sen. Jos korjausta ei ehditä tehdä työpajassa, kirjaat sen jatkoon. Hylkäät, jos viimeisin muutos rikkoi jotain, mikä toimi aiemmin. Palaat silloin edelliseen tallennuspisteeseen ja teet työpajaversion siitä.

**Pysähdy hetkeksi:** Jos Wilma-pääkäyttäjä kysyisi, voiko sovellusta käyttää oikeilla tiedoilla, mitä vastaisit?

## Esimerkki: T10 Eero Esimerkillä

Ennen testiä kirjoitat T10:n Odotan-kohtaan: "Sovellus näyttää Tallennustulos tuntematon. Jono pysähtyy. Uusi yritys ei tee toista urasuunnitelmaa."

Palautat lähtötilan, kytket testikytkimen päälle ja teet Eero Esimerkin (001789) urasuunnitelman. Sovellus näyttää virheilmoituksen, mutta jono jatkaa seuraavaan opiskelijaan. Tämä on ei läpi. Kirjaat havainnon omin sanoin.

Tehtävässä 4 korjautat tämän K5:llä. Ennen uusintaa palautat lähtötilan, joten Eerolla ei taas ole urasuunnitelmaa. Uusinnassa jono pysähtyy, ja Eeron jonon tila on Tarkistettava tallennus. Kun kytket kytkimen pois ja jatkat, sovellus lukee ensin simuloidun Wilman. Siellä on yksi urasuunnitelma, ja sovellus varmentaa sen. Kirjaat uusinnan omalle rivilleen: läpi. Ensimmäinen ei läpi jää näkyviin.

## Yhteenveto

Hyväksymistestit teet sinä, ja tulos on sinun havaintosi. Ei läpi on tietoa, ja ei testattu on rehellinen merkintä. Testit osoittavat, että sovellus toimii simuloidussa Wilmassa kuvitteellisella aineistolla. Ne eivät osoita, että se toimii oikeassa Wilmassa oikealla aineistolla.
