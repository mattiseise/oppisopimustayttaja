# Sanasto – osio 05

## Lähde

Paikka, josta sovellus saa tiedon: esitietolomake, haastattelu tai Primuksen tiedot Wilman kautta. Jokaisen kentän lähde näkyy tarkistusnäkymässä. Työpajassa lähteet ovat kuvitteellisia.

## Esitietolomake

Lomake, jolla opiskelija antaa tietojaan etukäteen. Työpajassa se on kuvitteellinen tiedosto kansiossa `testiaineisto`.

## WilmaRead

Tapa lukea Primuksen tiedot niistä Wilman näkymistä, joissa ne näkyvät käyttäjälle. Luku ei muuta Wilmassa mitään. Työpajassa luetaan simuloidun Wilman profiilia.

## Kenttähavainto

Yhden kentän tieto sovelluksessa. Siinä on arvo, lähde ja lukutila. Pelkkä arvo ei riitä.

## Lukutila

Kertoo, miten kentän arvo saatiin: OK (luettu), EMPTY (näkyi tyhjänä), NOT_VISIBLE (ei näkyvissä), READ_FAILED (luku epäonnistui) tai CONFLICT (ristiriita). Koodit ovat kuvauspaketin osasta 15. Sovellus näyttää lukutilan myös sanoina.

## Ristiriita

Lähteissä on samasta tiedosta eri arvot. Sovellus näyttää molemmat, sinä valitset, ja valinta kirjataan. Esimerkki: Liisa Kokeilun työaika on haastattelussa 37,5 h/vko ja esitiedoissa 30 h/vko.

## Hyväksynnän vanheneminen

Kun hyväksytty sisältö muuttuu, hyväksyntä ei ole enää voimassa. Sisältö hyväksytään uudelleen ennen Wilma-tallennusta.
