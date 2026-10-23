# Vetäjän ohjaamat tehtävät: osio 01 – Agentti ei ole chat: ensimmäinen tehtävä ja tallennuspiste

Näissä tehtävissä vetäjä näyttää ja haastaa. Oppija ei tee niissä rakennustyötä. Oppija pitää hiiren omalla koneellaan.

## TL1 Lupapyyntö ääneen (noin 5 min, tehtävä 2)

Tavoite: oppija kuulee kerran, miltä tarkistus kuulostaa, ja tekee sen sitten itse.

Claude-polku. Kun oppijan ruudulle tulee työkortin lupapyyntö, lue se ääneen. Mikä: luodaan tiedosto `TYOKORTTI.md`. Missä: polku alkaa `C:\dev\oppisopimustayttaja`. Miksi: oppija pyysi juuri tätä. Sano ääneen myös, mitä tekisit, jos yksi vastaus puuttuisi. Kieltäisit ja kysyisit agentilta syytä. Näytä, että hyväksyt vain tämän kerran. Seuraavan lupapyynnön (`KEHOTEPOHJAT.md`) oppija lukee itse ääneen. Älä auta, ennen kuin hän on vastannut kaikkiin kolmeen.

Codex-polku. Git ei ole vielä käytössä. Avaa oppijan kanssa projektikansio Resurssienhallinnassa ja käy tulos ääneen läpi. Mikä: uusi tiedosto `TYOKORTTI.md`. Missä: projektikansion juuressa, eikä muita uusia tiedostoja ole. Miksi: oppija pyysi juuri tätä. Sano ääneen, miksi tarkistus tehdään näin. Agentti muutti kansiota kysymättä, ja sen oma vastaus on kertomus, ei tarkistus. Tulos katsotaan aina sovelluksen ulkopuolelta: nyt Resurssienhallinnasta, tehtävästä 4 alkaen Git-toiminnoista. Seuraavan tuloksen oppija käy itse läpi.

Jos oppija vastaa kysymyksiin agentin sanoin, pyydä häntä sanomaan sama omin sanoin. Tavoite on, että tarkistuksesta tulee tapa ennen tehtävää 4. Siinä lupapyyntöjä tai ajettuja komentoja tulee useita peräkkäin.

Purkukysymys: Mistä näit, mitä agentti teki? Hyvä vastaus nimeää lupapyynnön (Claude) tai Resurssienhallinnan (Codex). Agentin oma vastaus ei riitä.

## TL2 Rikotaan ja palataan (noin 5 min, ennen tehtävää 5)

Tavoite: oppija näkee paluun kerran, ennen kuin tekee sen itse.

Valmistelu: omalla koneellasi on projektikansio, jossa on tallennuspiste ja tiedosto `TYOKORTTI.md`. Käytä oppijan polun agenttisovellusta.

1. Pyydä agenttia poistamaan työkortista koko osa 4 (tietoturva).
2. Näytä muutos. Claude-polulla käytä muutosnäkymää. Codex-polulla avaa agenttisovelluksen Git-toiminnoista muuttuneet tiedostot.
3. Avaa tiedosto Muistiolla ja näytä, että osa puuttuu. Sulje Muistio ja sano ääneen miksi.
4. Anna K7. Lue ääneen agentin vastaus siitä, mitkä muutokset katoavat.
5. Vahvista paluu ja avaa tiedosto. Näytä, että osa palasi.

Sano ääneen kaksi asiaa. Paluu kumoaa vain tallennuspisteen jälkeiset muutokset. K7 pyytää agenttia jättämään päätöslokin, kriteerit ja testit ennalleen, mutta hylkäyksessä palataan silti ensin ja kirjataan sitten. Siksi tallennuspiste tehdään jokaisen hyväksynnän jälkeen.

Tietoturvaosa on valittu tarkoituksella. Kun se katoaa, menetys on helppo nähdä ja ymmärtää.

Purkukysymys: Mitä olisi tapahtunut, jos tallennuspistettä ei olisi ollut? Odotettu vastaus: osa olisi pitänyt kirjoittaa uudelleen, eikä kukaan tietäisi varmasti, mitä siinä oli.
