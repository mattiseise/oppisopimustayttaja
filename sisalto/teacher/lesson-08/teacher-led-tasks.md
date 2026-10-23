# Vetäjän ohjaamat tehtävät: osio 08 – Hyväksymistestit ja häiriötilanne

## TL Hyväksyjän kierros (10 min, tehtävän 4 jälkeen)

Tavoite: oppija osoittaa kolmen testin tuloksen omalla näytöllään ja nimeää, mitä kukin testi ei vielä osoita. Tämä on osion ajattelukysymyksen koe.

Roolit: vetäjä toimii Wilma-pääkäyttäjänä, joka päättää, saako sovellus jatkaa testi-Wilmaan. Oppija näyttää sovelluksesta, `TESTIT.md`:stä ja päätöslokista. Vetäjä ei näytä eikä vastaa oppijan puolesta. Agentilta ei kysytä mitään.

Kulku: pyydä näyttö yksi testi kerrallaan. Kun oppija on näyttänyt, kysy jokaisesta sama kysymys: "Mitä tämä ei todista?" Hyväksy vastaus, joka nimeää konkreettisen asian. Yleinen "ei kaikkea" ei riitä.

| Testi | Mitä oppija näyttää | Mitä se ei todista |
|---|---|---|
| T05 | Simuloidusta Wilmasta hyväksytyt arvot oikealla opiskelijalla. Toinen Aino Testinen ei muuttunut. | Oikean Wilman kentät, pakolliset kentät ja oikeudet. Ne selvitetään Wilma-pääkäyttäjän kanssa (P04). |
| T20 | Jono: VALMIS vasta varmennuksen jälkeen, ja seuraava avautui ilman edellisen hyväksyntää. | Oikean listan tapaukset ja kahden käyttäjän samanaikainen työ. |
| T10 | Tallennustulos tuntematon, jono pysähtyi tilaan Tarkistettava tallennus, ja simuloidussa Wilmassa on yksi urasuunnitelma. | Oikean Wilman käytös katkossa, istunnon vanheneminen ja toisen käyttäjän muutos (T11, T12). |
| B2 | `KENTAT.md`:n erot testi-Wilman ja simuloidun Wilman välillä. | Kirjoitus testi-Wilmaan, sen Wilma-tallennus ja varmennus. |

Jos oppija ei löydä näyttöä, testin tulos muutetaan ei testattu -merkinnäksi yhdessä. Se on oikea lopputulos, ei rangaistus.

Purku (1 min): kysy ajattelukysymys. Tavoitevastaus: "Testit osoittavat, että sovellus toimii simuloidussa Wilmassa kuvitteellisella aineistolla. Ne eivät osoita, että se toimii oikeassa Wilmassa oikealla aineistolla."

Kirjaus: oppija vie yhden kierroksella nimetyn asian hyväksymispäätöksen kohtaan "asia, jota testit eivät osoita".

## TL Testi-Wilman turvatarkistus (B2, 5 min ennen kirjautumista)

Tavoite: varmistaa yhdessä, että B2:n ehdot täyttyvät, ennen kuin oppija kirjautuu. Vetäjä lukee rivin, oppija vastaa ja näyttää.

- [ ] Testi-Wilma on vahvistetusti testikäytössä, eikä siinä ole oikeita tietoja. Kirjallinen vahvistus on tallessa.
- [ ] Oppijalla on testirooli. Testitunnus ei ole missään projektikansion tiedostossa.
- [ ] Kirjautuminen toimi savutestissä.
- [ ] Kenttäluku on testattu simuloidussa Wilmassa, ja tulosteessa oli vain kenttien nimet ja tyypit.
- [ ] Ohjetiedoston tietoturvakohta kieltää agenttia avaamasta testi-Wilmaa.
- [ ] Agentin keskustelu on tauolla. Claude-polulla agentti ei avaa sivua sisäänrakennetussa selaimessa. Codex-polulla täysiä oikeuksia ei ole valittu.
- [ ] Oppija käynnistää sovelluksen itse `KAYNNISTYS.md`:n mukaan.
- [ ] Oppija näyttää osion 07 testin C havainnon: kirjautumisesta ei jäänyt projektikansioon selainprofiilia, evästeitä, tallenteita (HAR, jäljet) eikä sivun lähdekoodia.
- [ ] Kenttäluku kirjoittaa tulosteen projektikansion ulkopuolelle (`C:\dev\testi-wilma-raaka`), eikä agentti lue sitä.
- [ ] Testi-Wilmaan ei kirjoiteta. Urasuunnitelman lomaketta ei tallenneta.
- [ ] Sovittu: jos tulosteessa on henkilötietoa, oppija pysähtyy, eikä tiedosto mene agentille.

Jos yksikin rivi ei täyty, oppija tekee B1:n. Päätös sanotaan ääneen, ja oppija kirjaa sen päätöslokiin.
