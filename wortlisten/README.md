# Wortlisten

Sammlung freier Wortlisten (Deutsch und Englisch) für Scrabble Zing und andere Wortspiele.
Alle Listen: eine Zeile pro Wort, UTF-8. Die selbst erzeugten Listen sind in Großbuchstaben, ß als SS.

Die Spiel-Listen, die `zing/build.py` einliest, liegen weiter in `zing/` und bleiben unverändert.

## eigene/ – selbst erzeugt

Erzeugt aus den LibreOffice-Wörterbüchern (Affixregeln ausgeklappt, nur Buchstaben, keine Bindestriche/Ziffern).

| Datei | Wörter | Inhalt |
|---|---|---|
| `deutsch_alle_laengen.txt` | 708.654 | Deutsch, alle Wortformen, inkl. Abkürzungen und Eigennamen aus dem Wörterbuch |
| `deutsch_2-8_mit_abk.txt` | 79.385 | Deutsch, 2 bis 8 Buchstaben |
| `englisch_us_alle_laengen.txt` | 87.950 | Englisch (US), alle Wortformen |
| `englisch_uk_alle_laengen.txt` | 175.987 | Englisch (UK), alle Wortformen |
| `abkuerzungen_us_uk.txt` | 497 | Typische US-/UK-Abkürzungen, von Hand zusammengestellt |
| `de_en_abk_2-8.txt` | 156.388 | Deutsch + Englisch + Abkürzungen, 2 bis 8 Buchstaben |
| `de_en_abk_2-12.txt` | 497.172 | Deutsch + Englisch + Abkürzungen, 2 bis 12 Buchstaben |

## extern/ – unverändert von GitHub übernommen

| Datei | Wörter | Quelle | Lizenz |
|---|---|---|---|
| `deutsch_enz_german-wordlist.txt` | 685.829 | [enz/german-wordlist](https://github.com/enz/german-wordlist) (Regeln nah an Scrabble, ohne Namen/Abkürzungen) | CC0 |
| `englisch_dwyl_words_alpha.txt` | 370.105 | [dwyl/english-words](https://github.com/dwyl/english-words) | Unlicense |
| `englisch_enable1.txt` | 172.823 | ENABLE, über [dolph/dictionary](https://github.com/dolph/dictionary) | gemeinfrei |
| `englisch_popular.txt` | 25.322 | häufige Wörter, ebenfalls [dolph/dictionary](https://github.com/dolph/dictionary) | siehe README dort |

Lizenztexte und READMEs der Quellen: `extern/lizenzen/`.

## Lizenzhinweis

Die Listen in `eigene/` sind abgeleitet von den [LibreOffice-Wörterbüchern](https://github.com/LibreOffice/dictionaries):
Deutsch (igerman98/frami) unter GPL 2 oder 3, Englisch US unter BSD/gemeinfrei (SCOWL), Englisch UK unter LGPL.
Beim Weitergeben bitte die jeweilige Lizenz beachten (siehe `extern/lizenzen/`).

## Grenzen

Keine der Listen ist eine offizielle Scrabble-Liste. Die Turnierlisten (Duden, Scrabble Deutschland e. V.,
Collins, NWL/TWL) sind urheberrechtlich geschützt und deshalb nicht enthalten. Marken und Abkürzungen sind nur
enthalten, soweit sie in den Quellen stehen oder in `abkuerzungen_us_uk.txt` genannt sind.
