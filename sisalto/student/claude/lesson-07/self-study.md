# Osio 07: Oppisopimus ja sen edellytykset (joustokohta)

> Ajattelukysymys: Missä järjestyksessä tiedot pitää viedä, ja mitä ohjelma ei saa koskaan arvata?

Urasuunnitelma on yksi lomake. Oppisopimus on erilainen. Sen voi kirjata vasta, kun muut tiedot ovat Wilmassa. Työpaikan pitää olla siellä. Työpaikkaohjaajan pitää olla siellä ja liitettynä oikeaan toimipaikkaan.

Tässä osiossa agentti lisää simuloituun Wilmaan työpaikka-, työpaikkaohjaaja- ja oppisopimusnäkymät. Sovellukseen tulee kolme uutta sovitinta. Sinä päätät järjestyksen ja testaat tapaukset, joissa kirjaus menee helpoimmin väärin.

Osio on joustokohta. Jos aamupäivän työ on kesken, vetäjä lyhentää osion pelkkään työpaikkaan tai siirtää sen jatkoon. Silloin teet ensin kesken jääneet palat. Kumpikaan ei ole epäonnistuminen. Varmennettu urasuunnitelma ja toimiva jono ovat tärkeämpiä kuin keskeneräinen oppisopimus.

Jos osio lyhenee tai siirtyy, mikään ei katoa. Kirjaat päätöksen ja syyn päätöslokiin. Merkitset tekemättömät testit `TESTIT.md`:hen jatkoon. Osiossa 09 ne siirtyvät jatkosuunnitelmaan, ja teet ne työpajan jälkeen samalla työtavalla.

## Järjestys tulee riippuvuuksista

Kuvauspaketin osa 7 kertoo järjestyksen. Työpaikka ja työpaikkaohjaaja lisätään ennen oppisopimusta ja näyttösuunnitelmaa. Tutkinnon osan pitää löytyä opinnoista, ennen kuin sille tehdään näyttösuunnitelma.

Syy on yksinkertainen. Kuvauspaketin mukaan oppisopimus viittaa Wilmassa jo olevaan työpaikkaan ja työpaikkaohjaajaan. Jos työpaikkaa ei ole, viitattavaa ei ole. Puuttuva viittaus estää Wilma-tallennuksen (osa 21).

Järjestys on sinun tietoasi. Agentti lukee sen kuvauspaketista, mutta et voi luottaa siihen, että se noudattaa sitä. Siksi kirjoitat lomakkeiden järjestyksen itse kehotteeseen ja tarkistat sen suunnitelmasta.

## Yritys ja toimipaikka

Yrityksellä voi olla monta toimipaikkaa. Testileipomo Oy:llä on kaksi: Keskusta ja Satama. Opiskelija on töissä yhdessä niistä. Pelkkä yrityksen nimi ei siis kerro, mihin oppisopimus kohdistuu. Kuvauspaketin osa 7 sanoo, että saman yrityksen toimipaikat erotetaan.

Sama koskee henkilöitä. **Työpaikkaohjaaja** ohjaa opiskelijaa työpaikalla. Työnantajan edustaja on oppisopimuksen työnantajapuolen henkilö. He voivat olla eri henkilöitä, vaikka toimisivat samassa yrityksessä. Ohjelma ei saa olettaa heitä samaksi henkilöksi.

Testiaineistossa on lisäksi kaksi työpaikkaohjaajaa nimeltä Pekka Mallikas. Toinen on Esimerkkikone Oy:ssä, toinen Testileipomo Oy:n Satamassa. Nimi ei riitä työpaikkaohjaajankaan kohdistukseen. Työpaikkaohjaaja tunnistetaan työpaikan ja toimipaikan kautta.

**Pysähdy hetkeksi:** Mistä tunnistat oikean toimipaikan, jos yrityksellä on kaksi?

## Palkka, yksikkö ja työaika

Kuvauspaketin osa 8 sanoo, että puuttuvaa palkkaa, työaikaa tai työpaikkaohjaajaa ei arvata. Palkan kohdalla tarkistetaan aina, onko kyse kuukausi- vai tuntipalkasta.

Liisa Kokeilun palkaksi on kirjattu "2 450" ilman yksikköä. Summa näyttää kuukausipalkalta, mutta ohjelma ei saa päätellä sitä. Puuttuva yksikkö estää oppisopimuksen kirjauksen, kunnes joku selvittää sen. Liisan työajassa on lisäksi ristiriita. Haastattelussa se on 37,5 h/vko, esitiedoissa 30 h/vko. Ratkaisit sen osiossa 05, mutta ratkaisematon ristiriita estää kirjauksen samalla tavalla.

Eero Esimerkin palkka on 14,20 €/h. Yksikön pitää kulkea summan mukana Wilmaan asti. Jos sovellus tallentaa pelkän luvun, tieto on väärin, vaikka luku on oikein.

## Ensin haku, sitten uusi tietue

Ennen kuin sovellus lisää mitään, se etsii. Kuvauspaketin osat 6 ja 8 sanovat, että olemassa oleva tietue näytetään ennen uuden luomista. Haun tulos on yksi kolmesta.

Haku voi löytää yhden tietueen. Esimerkkikone Oy:llä on yksi toimipaikka, joten tulos on selvä. Haku voi löytää monta. Testileipomo Oy ilman toimipaikkaa on moniselitteinen. Sovellus pysähtyy ja näyttää vaihtoehdot, ja sinä valitset. Haku voi myös jäädä tyhjäksi. Kokeiluverstas Oy:tä ei ole simuloidussa Wilmassa. Sovellus valmistelee lisäyksen, ja sinä hyväksyt sen, ennen kuin mitään kirjoitetaan.

Kuvauspaketin osa 21 lisää säännön: ensimmäistä osumaa ei valita arvaamalla. Sääntö koskee yrityksiä, toimipaikkoja ja henkilöitä.

Valmisteltu lisäys ei ole vielä Wilmassa. Luet sen tiedot, ennen kuin hyväksyt. Onko yrityksen nimi kirjoitettu oikein? Mistä lähteestä se tuli? Onko toimipaikka oikea? Kuvauspaketin vaiheessa 3 on lisäksi ehto: kun saman opiskelijan käsittely uusitaan, sovellus tunnistaa jo luodun tietueen. Siksi haet testissä Kokeiluverstas Oy:n uudelleen ja toteat, että se on Wilmassa vain kerran.

## Mitä ohjelma ei saa arvata

Ajattelukysymyksen toinen puoli kokoaa osion. Ohjelma ei arvaa opiskelijaa nimestä. Se ei arvaa toimipaikkaa yrityksen nimestä eikä työpaikkaohjaajaa henkilön nimestä. Se ei päättele palkan yksikköä summasta. Se ei valitse työaikaa kahdesta eri lähteestä. Se ei keksi kenttää, jota ei löydy.

Jokaisessa tapauksessa oikea toiminta on sama. Sovellus pysähtyy, näyttää vaihtoehdot tai puutteen ja odottaa sinua. Pysähtyminen ei ole vika. Se on se kohta, jossa sinun osaamisesi tulee sovellukseen.

**Pysähdy hetkeksi:** Mikä näistä arvauksista olisi omassa työssäsi vaarallisin, ja miksi?

**Pysähdy hetkeksi:** Mitä Wilmassa tapahtuu, jos sovellus luo työpaikan uudelleen joka kerta, kun käsittelet saman opiskelijan?

## Sama työjärjestys uusille lomakkeille

Osiossa 04 rakensit urasuunnitelman sovittimen kehotepohjalla K9. Samaa työjärjestystä käytetään nyt kolmelle lomakkeelle. Ensin kentän haku ja yksi osuma, sitten täyttö, Wilma-tallennus, uudelleenluku ja kaksoiskappaleen esto. Agentti pysähtyy jokaisen kohdan jälkeen. Sinä tarkistat tuloksen ja annat vasta sitten luvan jatkaa. Palojen välissä katsot muutosnäkymästä, mitä muuttui.

Kaksoiskappaleen esto on tässä osiossa tärkeä. Jos käsittelet työpaikan kahdesti, Wilmassa pitää olla edelleen yksi Kokeiluverstas Oy.

Pysähdysten tarkistukset teet testien tapauksilla. Niissä Kokeiluverstas Oy päätyy simuloituun Wilmaan jo rakennusvaiheessa. Siksi palautat ennen omaa testiä simuloidun Wilman lähtötilaan. Lähtötilassa ovat testiaineiston työpaikat ja henkilöt, mutta ei Kokeiluverstas Oy:tä eikä oppisopimuksia. Silloin testi alkaa joka kerta samasta tilanteesta, eikä tulos riipu siitä, mitä edellinen kokeilu jätti.

Oppisopimus tulee jonoon uudeksi tehtäväksi. Osiossa 06 opiskelija oli VALMIS, kun urasuunnitelma oli varmennettu. Nyt VALMIS vaatii kaikkien valittujen tehtävien varmennuksen. Jos valitset urasuunnitelman ja oppisopimuksen, opiskelija on VALMIS vasta, kun molemmat on varmennettu.

Puuttuvaa kenttää ei keksitä. Jos simuloidusta oppisopimusnäkymästä puuttuu kenttä, jonka muistat oikeasta Wilmasta, kirjaat sen `KENTAT.md`:hen. Simuloitu Wilma ei todista, millainen oikea lomake on. Oikean lomakkeen kentät selvitetään jatkossa Wilma-pääkäyttäjän kanssa.

## Lisä: HOPS ja lausepohja

Jos aikaa jää, teet lisätehtävän. HOPSissa opiskelijalle lisätään tutkinnon osat. Jokainen osa saa oman aikataulunsa, esimerkiksi 2027–2028. Kuvauspaketin osa 19 kieltää kovakoodaamasta samaa aikataulua kaikille osille.

Lausepohja on valmis tavoiteteksti, jossa on hakasulkeissa aukkoja. Kuvauspaketin osa 18 antaa esimerkin: "Opiskelija kehittää osaamistaan tehtävässä [vahvistettu työtehtävä] harjoittelemalla [tutkinnon osan tavoite]." Jos hakasulkeita jää tekstiin, ehdotusta ei voi hyväksyä. Tekstiehdotus ei myöskään osoita opiskelijan osaamista. Kielimallia ei käytetä, koska se on kuvauspaketissa jatkopäätös.

## Esimerkki: Aino Testisen oppisopimus

Aino Testinen (000123) on töissä Testileipomo Oy:n Keskustan toimipaikassa. Haastattelussa työajaksi on kirjattu 37,5 h/vko ja palkaksi 2 450 €/kk. Työpaikkaohjaaja on Maija Mallikas. Työnantajan edustaja on Kaisa Mallikas.

Sovellus hakee ensin työpaikan. Testileipomo Oy:llä on kaksi toimipaikkaa, joten sovellus kysyy. Valitset Keskustan, koska haastattelu sanoo niin. Sitten sovellus hakee työpaikkaohjaajan. Maija Mallikas löytyy Keskustan toimipaikasta. Kaisa Mallikas tulee omaan kenttäänsä työnantajan edustajaksi. Vasta nyt sovellus täyttää oppisopimuksen, tekee Wilma-tallennuksen ja lukee lomakkeen uudelleen.

Avaat simuloidun Wilman itse. Aino Testisen oppisopimuksessa on Keskusta, 37,5 h/vko ja 2 450 €/kk. Maija ja Kaisa ovat eri kentissä. Toisen Aino Testisen (000456) tietoihin ei ole tullut mitään. Vasta nyt sovellus näyttää Ainon jonon tilana VALMIS. Kirjaat testin T08 tuloksen.

Liisa Kokeilun kohdalla sama ketju pysähtyy palkkaan. Se on oikea tulos, ja kirjaat sen testiin T03.

## Yhteenveto

Oppisopimus kirjataan viimeisenä, koska se viittaa työpaikkaan ja työpaikkaohjaajaan. Sovellus etsii, ennen kuin lisää, ja moniselitteinen haku pysähtyy sinun valintaasi. Yritys ja toimipaikka erotetaan, samoin työpaikkaohjaaja ja työnantajan edustaja. Palkkaa, sen yksikköä, työaikaa tai työpaikkaohjaajaa ei arvata.
