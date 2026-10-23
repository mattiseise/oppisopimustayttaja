# Sanasto – osio 01

## Chat-palvelu

Keskustelupalvelu, joka vastaa tekstillä mutta ei muuta tiedostoja koneellasi.

## Kehote

Viesti, jolla annat agentille tehtävän. Puhekielessä myös prompti.

## Kehotepohja

Valmis kehote, jossa on hakasulkeissa aukot. Täytät aukot itse ennen lähettämistä.

## Lupapyyntö

Agenttisovelluksen kysymys, ennen kuin agentti muuttaa tiedostoa tai ajaa komennon. Tällä polulla sovellus kysyy, kun agentti haluaa ylittää hiekkalaatikon rajan.

## Oikeusasetus ja hiekkalaatikko

Oikeusasetus ratkaisee, milloin agentti kysyy. Hiekkalaatikko (sandbox) on tekninen raja, joka estää kirjoittamisen projektikansion ulkopuolelle ja verkkoyhteydet ilman hyväksyntää.

## Muuttuneet tiedostot

Tiedostot, joita agentti muutti. Tarkistat ne agenttisovelluksen Git-toiminnoista tai ennen Gitiä Resurssienhallinnasta. Agentin oma luettelo on vain apu.

## Komento

Tekstimuotoinen käsky, jonka agentti ajaa koneella, esimerkiksi asennus tai käynnistys.

## Tallennuspiste (commit)

Gitillä tehty nimetty välitila projektikansiosta. Siihen voi palata. Tallennuspisteen viesti kertoo omin sanoin, mitä siinä on valmiina.

## Palata tallennuspisteeseen

Palauttaa projektikansion aiempaan tallennuspisteeseen. Sen jälkeiset muutokset katoavat.

## Päätösloki

`PAATOSLOKI.md`. Kirjaat siihen jokaisesta isommasta agentin tuotoksesta päätöksen ja yhden perusteen omin sanoin. Agentti ei kirjoita eikä muokkaa sitä.

## Hyväksyn / korjautan / hylkään

Päätöslokin kolme päätöstä. Korjautan: pyydän agenttia korjaamaan. Hylkään: palaan tallennuspisteeseen.
