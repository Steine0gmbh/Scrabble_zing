# Zing – Scrabble Zing (1:1 Nachbau)

```
zing/                      Das Spiel
  zing_src.html            Quelltext des Spiels (hier ändern!)
  build.py                 Baut daraus scrabble_zing.html, Zing.exe und die iOS-App-Dateien
  scrabble_zing.html       Fertiges Spiel, eine einzige Datei (im Browser öffnen)
  Zing.exe, launcher.cs    Windows-Programm und sein Startcode
  zing.ico                 Programmsymbol
  *_wortliste.txt, scrabble_2-8_buchstaben.txt   Wörterbuch (wird eingebettet)
  material/                Referenz: Video-Links, Prompt, große Wortliste
ios-app/                   iPhone-App (Capacitor), von build.py befüllt
.github/workflows/ios-ipa.yml   Baut die unsignierte IPA auf GitHub
```

Nach Änderungen an `zing/zing_src.html`: `cd zing && python build.py` und alles hochladen.
Anleitung für die iPhone-App: `ios-app/ANLEITUNG.md`.
