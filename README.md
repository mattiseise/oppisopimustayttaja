# Vibekoodaus-työpaja: Oppisopimustäyttäjä

Sivusto kahden päivän työpajaan, jossa ohjelmointia osaamaton rakentaa agentin avulla Oppisopimustäyttäjän. Kaksi erillistä polkua: Claude Code ja Codex.

- `sisalto/`: lähdemateriaali Markdownina (oppijan polut ja vetäjän materiaali)
- `tools/build.py`: rakentaa sivut `sisalto/`-kansiosta
- `index.html`, `claude/`, `codex/`, `ohjaaja/`: rakennetut sivut (älä muokkaa käsin)
- `assets/`: tyyli ja kopiointipainikkeet

Vetäjän sivut (`ohjaaja/`) eivät ole linkitettyjä etusivulta.

## Rakentaminen

```
uv run tools/build.py
```

## Julkaisu

GitHub Pages gh-pages-haarasta:

```
git push origin main
git push origin main:gh-pages
```
