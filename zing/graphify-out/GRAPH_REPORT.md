# Graph Report - zing  (2026-10-27)

## Corpus Check
- Corpus is ~5,626 words - fits in a single context window. You may not need a graph.

## Summary
- 68 nodes · 84 edges · 8 communities (6 shown, 2 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.82)
- Token cost: 106,214 input · 0 output

## Community Hubs (Navigation)
- Build-Skript und Programmsymbol
- Spielregeln und Wertung
- EXE-Starter (C#)
- Spielablauf und Mehrspieler
- Wörterbuch und Wortprüfung
- Beutel und Buchstaben
- Eingabe und Steuerung
- Bühne und Skalierung

## God Nodes (most connected - your core abstractions)
1. `nextRound` - 9 edges
2. `submit (LEGEN)` - 7 edges
3. `Claude prompt: Scrabble Zing recreation` - 6 edges
4. `evaluate (move validation and scoring)` - 6 edges
5. `make_icon()` - 5 edges
6. `save_ico()` - 4 edges
7. `make_tile_icon()` - 4 edges
8. `Built-in dictionary, upload and tolerance mode spec` - 4 edges
9. `SFX sound effects (tone/noise)` - 4 edges
10. `endGame` - 4 edges

## Surprising Connections (you probably didn't know these)
- `zing_src.html (Zing Wortspiel single-file game)` --implements--> `Claude prompt: Scrabble Zing recreation`  [INFERRED]
  zing_src.html → claude_prompt_f_r_scrabble_zing.txt
- `submit (LEGEN)` --implements--> `ZING bonus, tempo multiplier and time bonus`  [INFERRED]
  zing_src.html → claude_prompt_f_r_scrabble_zing.txt
- `render / tileHTML / buildDom` --implements--> `Retro King.com/Fettspielen visual style and HUD spec`  [INFERRED]
  zing_src.html → claude_prompt_f_r_scrabble_zing.txt
- `evaluate (move validation and scoring)` --implements--> `Scrabble Zing game mechanics spec (start word, drag/drop, validation)`  [INFERRED]
  zing_src.html → claude_prompt_f_r_scrabble_zing.txt
- `drawOne (vowel/consonant balanced draw)` --implements--> `German letter values and distribution with jokers`  [INFERRED]
  zing_src.html → claude_prompt_f_r_scrabble_zing.txt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Move validation and scoring flow** — zing_src_submit, zing_src_evaluate, zing_src_checkword, zing_src_animatescore, zing_src_burst [EXTRACTED 0.90]
- **Game and turn lifecycle** — zing_src_newgame, zing_src_nextround, zing_src_endgame, zing_src_playertimeout, zing_src_passturn, zing_src_showstart [EXTRACTED 0.90]
- **Dictionary checking system** — zing_src_dict, zing_src_checkword, zing_src_isplausible, zing_src_normword, zing_src_upload_handler [EXTRACTED 0.90]

## Communities (8 total, 2 thin omitted)

### Community 0 - "Build-Skript und Programmsymbol"
Cohesion: 0.18
Nodes (5): add(), make_icon(), make_tile_icon(), render_bag_png(), save_ico()

### Community 1 - "Spielregeln und Wertung"
Cohesion: 0.17
Nodes (15): Claude prompt: Scrabble Zing recreation, Scrabble Zing game mechanics spec (start word, drag/drop, validation), Retro King.com/Fettspielen visual style and HUD spec, Web Audio API retro sound effects spec, ZING bonus, tempo multiplier and time bonus, zing_src.html (Zing Wortspiel single-file game), animateScore, buildBonus (+7 more)

### Community 3 - "Spielablauf und Mehrspieler"
Cohesion: 0.24
Nodes (9): applySettings / initSettings / buildPlayerRows, CONFIG, endGame, loop (game loop, timer, clock), nextRound, passTurn, playerTimeout, renderPlayers (+1 more)

### Community 4 - "Wörterbuch und Wortprüfung"
Cohesion: 0.47
Nodes (6): Built-in dictionary, upload and tolerance mode spec, checkWord, DICT / BASE_WORDS dictionary, isPlausible (tolerance heuristic), normWord, Custom word list upload handler

### Community 5 - "Beutel und Buchstaben"
Cohesion: 0.33
Nodes (6): German letter values and distribution with jokers, drawOne (vowel/consonant balanced draw), makeBag, newGame, newRack, VALUES and DISTRIBUTION tables

### Community 6 - "Eingabe und Steuerung"
Cohesion: 0.50
Nodes (4): Pointer drag and drop / click input handlers, Keyboard input handler, toRack / detach / placeOnBoard, togglePause / updPaused

## Knowledge Gaps
- **10 isolated node(s):** `zing_src.html (Zing Wortspiel single-file game)`, `CONFIG`, `normWord`, `Background music loop (MELODY/BASS)`, `buildBonus` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 26 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `nextRound` connect `Spielablauf und Mehrspieler` to `Spielregeln und Wertung`, `Beutel und Buchstaben`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `evaluate (move validation and scoring)` (e.g. with `buildBonus` and `Scrabble Zing game mechanics spec (start word, drag/drop, validation)`) actually correct?**
  _`evaluate (move validation and scoring)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `zing_src.html (Zing Wortspiel single-file game)`, `CONFIG`, `normWord` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Why does `submit (LEGEN)` connect `Spielregeln und Wertung` to `Spielablauf und Mehrspieler`, `Eingabe und Steuerung`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Why does `evaluate (move validation and scoring)` connect `Spielregeln und Wertung` to `Wörterbuch und Wortprüfung`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._