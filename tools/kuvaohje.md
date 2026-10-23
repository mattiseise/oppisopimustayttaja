# Animoitujen kuvien ohje (pikaohje)

Kuvat ovat inline-SVG:itä, jotka `tools/build.py` upottaa sivulle `pikaohje.html` merkinnän `[[kuva:nimi|kuvateksti]]` kohdalle. Mallikuva: `sisalto/kuvat/tyokierros.svg`.

## Tiedosto

- Polku `sisalto/kuvat/<nimi>.svg`. Yksi juuri: `<svg class="anim anim-<nimi>" viewBox="0 0 560 H" role="img" aria-labelledby="<nimi>-title" xmlns="http://www.w3.org/2000/svg">`.
- Ensimmäisenä `<title id="<nimi>-title">`, joka kertoo yhdellä tai kahdella lauseella, mitä animaatio näyttää.
- Leveys aina 560 (viewBox). Korkeus 220–320.
- Kaikki CSS SVG:n omassa `<style>`-lohkossa. Jokainen valitsin alkaa `.anim-<nimi>`, jokainen keyframes-nimi ja marker-id alkaa `<nimi>-`. Kuvat ovat samalla sivulla, joten nimet eivät saa törmätä.
- Ei ulkoisia kuvia, fontteja eikä skriptejä.

## Typografia

- Fontti `font-family: var(--sans, sans-serif)`; tunnisteet ja tiedostonimet `var(--mono, monospace)`.
- Pienin fonttikoko 15 (viewBox-yksiköissä), pääotsikot 17–18, paino 500–600. Puhelimella kuva skaalautuu noin 0,6-kertaiseksi, joten pienempi teksti ei ole luettavaa.
- Vähän sanoja. Yksi tai kaksi sanaa laatikossa. Suomi, oikeinkirjoitus tarkistettu.

## Värit

| Käyttö | Väri |
|---|---|
| Teksti | #1A0530 |
| Toissijainen teksti | #5B5470 |
| Haalea (viivat, selitteet) | #7D7694 |
| Korostus | #6A50BD |
| Korostuksen vaalea tausta | #EEE8FF |
| Reunat | #E4DFEE |
| Kortti | #FFFFFF |
| Paneelin tausta | #F5F3F8 |
| Onnistui | #0F9D6C, tausta #E3F5EE |
| Virhe / pysähtyy | #B42318, tausta #FDECEA |
| Odottaa | #B54708, tausta #FEF3E2 |

Tilat näytetään aina myös sanana (VALMIS, ODOTTAA, RISTIRIITA), ei pelkkänä värinä.

## Animaatio

- Yksi tarina 3–5 tahdissa. Silmukka 8–12 s, `infinite`.
- Elementit ilmestyvät (opacity, pieni translate), korostus siirtyy, merkit (✓, ✕) ilmestyvät. Ei pyöriviä tai vilkkuvia efektejä.
- **Perustila on valmis kuva.** Ilman animaatiota kaikki tarinan lopputilan elementit näkyvät. Animaation keyframes vie elementin piilosta näkyviin. Tilapäiset välivaiheet (esim. virhe, joka korjataan) piilotetaan perustilassa ja näytetään vain animaatiossa: anna niille perustilaksi `opacity: 0`.
- Pakollinen lopussa:
  `@media (prefers-reduced-motion: reduce) { .anim-<nimi> * { animation: none !important; } }`
- Viivoille ja nuolille `<marker>` kuten mallikuvassa.

## Sisältö

- Kyse on oikeasta tuotteesta oikeaan Wilmaan. Kehitys ja testaus tehdään testi-Wilmassa: Wilma on aina selaimen ikkuna, jonka yläpalkissa lukee TESTI-WILMA. Ei Wilman logoa eikä oikean Wilman ulkoasun jäljittelyä. Sanaa SIMULOITU ei käytetä.
- Lukija on hallinnon työntekijä, joka ei ole tekninen. Tekoäly on yleinen laatikko "Tekoäly" (ei "Agentti"). Ei Clauden eikä Codexin käyttöliittymän kopiointia.
- Ei testikoodeja (T01, T13 …) eikä teknisiä sanoja (skripti, JSON-rakenne, rajapinta, commit). Kerro asia tavallisella kielellä, esimerkiksi "Oikea opiskelija löytyy" tai "Kaksi samannimistä".
- Kun kuvassa tekee joku, tekijä näkyy: "Tekoäly rakentaa", "Sinä hyväksyt". Ei pelkkiä irrallisia verbejä.
- Sovellus on ikkuna nimeltä "Oppisopimustäyttäjä".
- Vain kuvitteelliset tiedot: Aino Testinen 000123, Aino Testinen 000456, Eero Esimerkki 001789, Liisa Kokeilu 002024, Ville Testaaja 000999; Testileipomo Oy (Keskusta, Satama), Esimerkkikone Oy, Kokeiluverstas Oy; työpaikkaohjaaja Maija Mallikas, työnantajan edustaja Kaisa Mallikas; Testiosa A, Testiosa B; palkka 2 450 €/kk, työaika 37,5 h/vko tai 30 h/vko.
- Kuvan pitää vastata `sisalto/pikaohje.md`:n vaiheen tekstiä ja kuvatekstiä.

## Tarkistus

1. Rakenna: repon juuressa `D:\programming\uv\uv.exe run tools/build.py`.
2. Avaa `http://localhost:8535/pikaohje.html` sovelluksen selaimeen (palvelin on käynnissä) ja kuvakaappaa kuva kahdessa eri hetkessä.
3. Tarkista: teksti ei mene päällekkäin eikä yli reunan, kaikki teksti on luettavaa, animaatio kertoo vaiheen asian.
4. Tarkista myös puhelinleveys (375 px). Palauta näkymä työpöytäkokoon lopuksi.
