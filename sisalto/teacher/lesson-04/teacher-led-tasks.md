# Vetäjän ohjaamat tehtävät: osio 04 – Ensimmäinen varmennettu tallennus

Tässä tehtävässä vetäjä näyttää ja haastaa. Oppija ei tee rakennustyötä. Oppija pitää hiiren omalla koneellaan.

## TL Valmis vai varmennettu (noin 10 min, tehtävän 8 alussa, voi siirtyä päivän 2 alkuun)

Tavoite: oppija erottaa kolme asiaa toisistaan. Ne ovat agentin valmis-ilmoitus, sovelluksen onnistumisviesti ja oma testitulos.

Valmistelu: omalla koneellasi on harjoitusajon välitila osion 04 lopusta. Palauta sen lähtötila ennen TL:ää. Simuloidussa Wilmassa on testikytkin, ja se on pois päältä. Käytä oppijan polun agenttisovellusta.

Jos välitilaa ei ole, tee TL oppijan koneella, kun hänen testikytkimensä on lisätty (tehtävän 8 askel 3). Silloin oppija kytkee kytkimen päälle simuloidun Wilman sivulta sinun ohjeestasi. Tee kirjaus Ville Testaajalle. Oppijan T13 alkaa palautuksella, joten kirjauksesi ei jää häiritsemään.

1. Kytke testikytkin päälle. Älä kerro, mikä kenttä tallentuu väärin.
2. Kirjoita agentille: "Toimiiko urasuunnitelman Wilma-tallennus? Älä muuta mitään." Lue vastaus ääneen.
3. Pyydä oppijaa ennustamaan ääneen kolme asiaa. Mitä onnistumisviesti näyttää? Mitä uudelleenluku näyttää? Mitä simuloidun Wilman lomakkeella on?
4. Tee kirjaus sovelluksella. Näytä ensin onnistumisviesti ja sitten uudelleenluvun tulos.
5. Avaa simuloitu Wilma Edgessä ja näytä tallentunut arvo.
6. Kytke testikytkin pois päältä.

Agentti vastaa askeleessa 2 todennäköisesti, että Wilma-tallennus toimii. Se ei tiedä kytkimestä, tai sen automaattiset testit ajetaan ilman kytkintä. Juuri tämä on opetus.

Claude-polulla agentti voi pyytää lupaa ajaa testinsä. Lue lupapyyntö ääneen kolmella kysymyksellä ennen hyväksyntää. Codex-polulla agentti voi ajaa testit kysymättä. Näytä lopuksi Git-toiminnoista, ettei mikään tiedosto muuttunut.

## Purku

Kysy kaksi kysymystä. Mikä näyttö olisi riittänyt agentille? Mikä riittää sinulle? Odotettu vastaus: agentille riitti oma automaattinen testi ja onnistumisviesti. Oppijalle riittää uudelleenluku, ja epäselvässä tilanteessa simuloidun Wilman lomake.

Kysy lisäksi, mihin oppija kirjoittaa ennusteensa omassa T13:ssa. Oikea vastaus on Odotan-rivin perään sanalla Ennuste: ennen ajoa.

Jos oppijan ennuste oli väärä, älä korjaa sitä heti. Kysy, mihin ennuste perustui. Väärä ennuste on hyvä syy kirjoittaa ennuste aina ennen ajoa.

Jos välitilasi sovellus näyttää kentän varmennettuna kytkimestä huolimatta, käytä tilannetta. Näytä simuloidun Wilman väärä arvo ja kysy, mikä T13:n tulos olisi. Vastaus on ei läpi. Kirjaa löydös harjoitusajon muistiinpanoihin ja korjaa välitila ennen seuraavaa työpajaa.
