# Osio 04: Ensimmäinen varmennettu tallennus

> Ajattelukysymys: Mistä tiedät, että tieto todella tallentui, kun agentti sanoo valmis?

Tässä osiossa sovellus tekee ensimmäisen Wilma-tallennuksen. Wilma on simuloitu, ja opiskelija on kuvitteellinen. Ketju on silti sama kuin myöhemmin oikeassa työssä. Sovellus löytää opiskelijan, täyttää lomakkeen, tekee Wilma-tallennuksen ja tarkistaa tuloksen.

Osio on päivän 1 tärkein. Sen jälkeen vähimmäistavoitteesta on valmiina kolme kohtaa. Simuloitu Wilma käynnistyy ohjeella ilman agenttia. Sovellus käynnistyy samalla ohjeella ja avaa selaimen, jossa kirjaudut itse. Urasuunnitelman Wilma-tallennus varmennetaan uudelleenluvulla, ja poikkeava arvo näkyy tarkistamattomana. Automaattinen haku lähteistä tulee osiossa 05 ja kahden opiskelijan jono osiossa 06.

Osion tärkein asia ei kuitenkaan ole tekniikka. Se on ero agentin valmis-ilmoituksen ja oman testisi välillä.

Aloitat osion uudella istunnolla. Agentti ei muista edellistä keskustelua, mutta se lukee ohjetiedoston istunnon alussa. Kehotepohja K11 pyytää sitä lukemaan lisäksi työlistan, päätöslokin ja testit. Vastauksesta näet, tunteeko agentti projektin tilanteen. Vertaat sitä omaan päätöslokiisi. Jos agentti muistaa jotain väärin, korjaat sen, ennen kuin se rakentaa mitään.

## Pienin kokonainen ketju

Kuvauspaketin vaihe 1 on tekninen kokeilu. Siinä rakennetaan pienin ketju, joka kulkee alusta loppuun. Ketjua laajennetaan vasta, kun se toimii. Kuvauspaketin osa 30 kutsuu tätä ensimmäiseksi kehityskokonaisuudeksi.

Tässä versiossa sovellus tekee seitsemän asiaa. Se avaa näkyvän selaimen simuloituun Wilmaan. Sinä kirjaudut. Sovellus tarkistaa, että ympäristö on simuloitu Wilma. Se etsii opiskelijan opiskelijanumerolla. Se näyttää urasuunnitelman arvot, ja sinä hyväksyt ne. Se täyttää lomakkeen ja tekee Wilma-tallennuksen. Lopuksi se lukee lomakkeen uudelleen ja vertaa arvoja hyväksymiisi.

Agentti rakentaa ketjun viidessä palassa. Pala (a) käynnistää sovelluksen. Pala (b) avaa selaimen. Pala (c) kohdistaa opiskelijan. Pala (d) täyttää lomakkeen ja tekee Wilma-tallennuksen. Pala (e) lukee uudelleen ja vertaa. Jokaisen palan jälkeen ajat sovelluksen itse, katsot tuloksen ja teet tallennuspisteen (commit). Jos pala (d) rikkoo jotain, palaat palan (c) tallennuspisteeseen. Et menetä koko iltapäivää.

Opiskelija kohdistetaan opiskelijanumerolla, ei nimellä. Aino Testisiä on kaksi, ja nimihaku löytäisi molemmat. Siksi kokeilet palassa (c) myös numeroa, jota simuloidussa Wilmassa ei ole. Sovelluksen pitää kertoa, ettei opiskelijaa löydy. Se ei saa avata ketään muuta. Työkortin tarkistuslista sanoo saman: kokeile aina vähintään yhtä tapausta, jonka pitää pysähtyä.

Sovellus on työpöytäsovellus, joka avautuu omaan ikkunaansa. Se ajetaan **kehitystilassa** suoraan projektikansiosta. Asennuspakettia ei tehdä työpajassa. Sovellus käynnistyy samalla tavalla kuin simuloitu Wilma: kaksoisnapsautat käynnistystiedostoa. Ohje lisätään tiedostoon `KAYNNISTYS.md`. Sen pitää toimia ilman agenttia, koska huomenna ja työpajan jälkeen käynnistät sovelluksen itse.

Ensimmäiset asennukset voivat kestää hallitussa verkossa 5–15 minuuttia. Asennuksissa tulee monta lupapyyntöä peräkkäin. Lue jokainen, vaikka ne alkavat näyttää samalta. Käytä odotusaika päätöslokin kirjoittamiseen.

## Miksi uudelleenluku

Kun painat Wilmassa tallennusta, näet usein onnistumisviestin. Viesti kertoo, että painallus meni perille. Se ei kerro, mitä lomakkeelle jäi. Kenttä voi katketa, arvo voi mennä väärään kenttään, tai tallennus voi jäädä kesken.

Kuvauspaketin osa 21 sanoo saman. Onnistumisviesti tai napin painallus ei yksin riitä. Sovellus avaa tallennetun lomakkeen uudelleen ja lukee arvot. Tätä kutsutaan **uudelleenluvuksi**. Jos luetut arvot vastaavat hyväksyttyjä, Wilma-tallennus on varmennettu. Jos jokin arvo poikkeaa tai sitä ei voi lukea, kenttä näytetään tarkistamattomana. Silloin kirjausta ei näytetä valmiina.

Simuloitu Wilma tallentaa yleensä oikein, koska agentti teki sen. Siksi siihen lisätään testikytkin. Kun kytkin on päällä, simuloitu Wilma tallentaa yhden kentän väärin. Testi T13 tarkistaa, että sovellus huomaa sen. Teet T13:n Ville Testaajalle. Ennen sitä palautat simuloidun Wilman lähtötilaan, jotta aiemmat kirjaukset eivät vaikuta tulokseen.

**Pysähdy hetkeksi:** Jos sovellus näyttää valmista, mutta simuloidussa Wilmassa on väärä arvo, kumpaan uskot ja miksi?

## Agentin valmis ei ole testitulos

Agentti kertoo usein, että työ on valmis. Se voi myös kertoa ajaneensa testit. Agentin valmis ei ole testitulos.

Agentti kirjoittaa ja ajaa **automaattisia testejä**. Ne ovat agentin työkalu. Ne tarkistavat, että koodi toimii niin, kuin agentti sen ymmärsi. Jos agentti ymmärsi urasuunnitelman väärin, testi menee silti läpi.

Hyväksymistesti on sinun. Teet sen ajamalla sovellusta ja katsomalla tuloksen itse. Testitulos on sinun havaintosi: läpi, ei läpi tai ei testattu. Kirjoitat sen `TESTIT.md`:hen Muistiolla. Agentti ei merkitse testiä läpäistyksi. Se ei myöskään merkitse työlistan tehtävää valmiiksi ennen testiäsi.

Valmiilta voi näyttää kolme asiaa: agentin viesti, sovelluksen onnistumisviesti ja läpi mennyt automaattinen testi. Mikään niistä ei ole testitulos. Testitulos syntyy, kun katsot itse, mitä lomakkeelle jäi.

T13:ssa kirjoitat ennusteen Odotan-riville, ennen kuin ajat. Syy on sama kuin kriteereissä. Jos kirjoitat odotuksen vasta tuloksen nähtyäsi, kirjoitat helposti sen, mitä näit.

Tämä koskee jokaista palaa. Kun agentti sanoo palan olevan valmis, ajat sovelluksen `KAYNNISTYS.md`:n ohjeella. Katsot, näkyykö se, mitä kriteerisi lupaa. Vasta sitten kirjaat päätöksen.

## Kun jokin ei toimi

Ohjelma tai komento antaa virheilmoituksen, kun jokin epäonnistuu. Virheilmoitus näyttää usein sekavalta. Sinun ei tarvitse ymmärtää sitä. Annat sen agentille sellaisenaan kehotepohjalla K4. Kerrot lisäksi, mitä teit ja mitä odotit. Agentti selvittää syyn ja kertoo ennen korjausta, mitä aikoo muuttaa.

Joskus korjaus ei auta. Agentti yrittää uudelleen, ja sama virhe palaa. Tätä kutsutaan **kehäksi**. Sääntö on yksinkertainen. Jos ongelma on jäljellä kahden korjausyrityksen jälkeen, katkaiset kehän kehotepohjalla K10. Agentti lopettaa ja kertoo, mitä yritti. Sitten palaat tallennuspisteeseen K7:llä ja kerrot vetäjälle.

Kehän katkaisu ei ole epäonnistuminen. Se säästää aikaa. Pieni pala ja tuore tallennuspiste tekevät paluusta halvan.

**Pysähdy hetkeksi:** Miksi on parempi palata tallennuspisteeseen kahden yrityksen jälkeen kuin yrittää, kunnes virhe katoaa?

## Sovittimen työjärjestys

Sovellus hoitaa jokaisen lomakkeen omalla osallaan. Tätä osaa kutsutaan **sovittimeksi**. Ensimmäinen sovitin hoitaa urasuunnitelman.

Kuvauspaketin liitteen A lopussa on työjärjestys, jolla sovitin rakennetaan. Kehotepohja K9 noudattaa sitä. Ensin jokaiselle kentälle haetaan lomakkeelta täsmälleen yksi osuma. Sitten kenttä täytetään. Sen jälkeen tehdään Wilma-tallennus. Sitten lomake luetaan uudelleen, ja arvoja verrataan hyväksyttyyn sisältöön. Lopuksi estetään kaksoiskappale, jotta sama lomake ei synny kahdesti. Testaat eston omalla testilläsi O03.

Työjärjestyksessä on kaksi sääntöä, jotka koskevat sinua. Agentti käyttää vain `KENTAT.md`:n kenttiä. Puuttuva kenttä merkitään puuttuvaksi, eikä sitä keksitä. Jos haku osuu kahteen kenttään, sovellus pysähtyy eikä valitse ensimmäistä.

## Turvaraja ennen ensimmäistä Wilma-kosketusta

Tänään sovellus koskee Wilmaan ensimmäisen kerran. Wilma on simuloitu, mutta toimit kuin se olisi oikea. Silloin tapa on valmis, kun vastassa on testi-Wilma.

Kirjaudut itse näkyvässä selaimessa. Agentti ei saa salasanaa eikä tunnuksia. Simuloidussa Wilmassa salasanaa ei ole, mutta sovellus ei saa pyytää sitä silloinkaan. Sovellus ei tallenna selaimen istuntoa, evästeitä eikä tallenteita. Käynnistät sovelluksen itse `KAYNNISTYS.md`:n ohjeella, ja sovellus avaa selaimen. Agentti ei avaa selainta puolestasi kirjautumista varten.

Tietoturvan muistilista on työkortin osassa 4. Kertaat sen ennen suunnitelmaa:

- Ei oikeaa opiskelijatietoa agentille: ei kehotteeseen, tiedostoon eikä kuvaan.
- Ei salasanoja eikä tunnuksia agentille.
- Kirjaudut itse näkyvässä selaimessa.
- Lue lupapyyntö ennen hyväksymistä.
- Älä salli kaikkea automaattisesti.
- Oikea Wilma ei kuulu työpajaan.
- Testi-Wilmasta saatu aineisto puhdistetaan kuvauspaketin liitteen A mukaan ennen agenttia.
- Projektikansio ei ole OneDrivessa.
- Epäilys tietovuodosta: pysähdy ja kerro vetäjälle.

**Pysähdy hetkeksi:** Mitä tapahtuisi, jos sovellus tallentaisi kirjautuneen istunnon projektikansioon, jonka agentti näkee?

## Esimerkki: tavoite katkesi

Teet Aino Testisen (000123) urasuunnitelman. Hyväksyt tavoitteeksi kuvitteellisen tekstin, joka on 120 merkkiä pitkä. Sovellus täyttää lomakkeen ja tekee Wilma-tallennuksen. Simuloitu Wilma näyttää onnistumisviestin. Agentti kertoo, että pala on valmis ja sen automaattiset testit menivät läpi.

Sovellus lukee lomakkeen uudelleen. Tavoitekentässä on vain 50 ensimmäistä merkkiä. Sovellus näyttää kentän tarkistamattomana, eikä kirjausta näytetä varmennettuna.

Ilman uudelleenlukua et olisi huomannut mitään. Onnistumisviesti ja agentin valmis olisivat kertoneet päinvastaista. Kirjaat päätöslokiin korjautan. Perusteeksi kirjoitat: "Tavoite katkesi 50 merkkiin. Uudelleenluku näytti sen tarkistamattomana." Sitten selvität agentin kanssa, onko raja simuloidussa Wilmassa tahallinen vai virhe. Kirjaat rajan myös `KENTAT.md`:n Oma huomio -riville, jos muistat oikeasta Wilmasta jotain vastaavaa.

## Yhteenveto

Tekninen kokeilu rakentaa pienimmän kokonaisen ketjun viidessä palassa, ja jokainen pala testataan ennen seuraavaa. Wilma-tallennus varmennetaan uudelleenluvulla, koska onnistumisviesti ei todista, mitä lomakkeelle jäi. Agentin valmis ei ole testitulos. Testitulos on oma havaintosi `TESTIT.md`:ssä. Virheilmoitus annetaan agentille sellaisenaan, ja kahden yrityksen jälkeen kehä katkaistaan. Kirjaudut aina itse, eikä sovellus tallenna istuntoa.
