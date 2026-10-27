# Zing als iPhone-App (IPA)

Die App wird nicht auf diesem PC gebaut (dafür bräuchte es einen Mac), sondern kostenlos
auf einem Cloud-Mac von GitHub. Heraus kommt eine **unsignierte** `Zing-unsigned.ipa`,
die du mit Sideloadly und deiner Apple-ID aufs iPhone bringst.

## 1. Projekt zu GitHub hochladen (einmalig)

1. Konto auf <https://github.com> anlegen (kostenlos).
2. Neues Repository erstellen, z. B. `zing`, am besten **Private**.
3. Den Ordner `Documents\zing` hochladen. Am einfachsten mit **GitHub Desktop**
   (<https://desktop.github.com>): *File → Add local repository* → Ordner wählen →
   „create a repository“ → *Publish repository*.
   Wichtig: Der Ordner `.github` muss mit hochgeladen werden (darin steckt der Bauauftrag).

## 2. IPA bauen lassen

1. Im Repository auf GitHub den Reiter **Actions** öffnen.
2. Der Lauf **„iOS IPA bauen“** startet nach dem Hochladen von selbst
   (sonst links den Workflow wählen → *Run workflow*).
3. Nach etwa 5–10 Minuten ist er grün. Unten unter **Artifacts** `Zing-unsigned-ipa`
   herunterladen und entpacken → `Zing-unsigned.ipa`.

Nach Änderungen am Spiel: `python build.py` ausführen und die Änderungen hochladen –
GitHub baut dann automatisch eine neue IPA.

## 3. Aufs iPhone installieren (Sideloadly)

1. **iTunes** und **iCloud** von der Apple-Webseite installieren (nicht aus dem
   Microsoft Store) – Sideloadly braucht deren Treiber.
2. **Sideloadly** von <https://sideloadly.io> installieren.
3. iPhone per USB-Kabel anschließen und am iPhone „Vertrauen“ tippen.
4. `Zing-unsigned.ipa` in Sideloadly ziehen, deine Apple-ID eintragen, **Start**.
   (Tipp: Dafür kannst du eine Zweit-Apple-ID verwenden.)
5. Am iPhone:
   - *Einstellungen → Allgemein → VPN & Geräteverwaltung* → deine Apple-ID → **Vertrauen**
   - ab iOS 16: *Einstellungen → Datenschutz & Sicherheit → Entwicklermodus* einschalten
     (iPhone startet neu).
6. Zing auf dem Home-Bildschirm starten.

## Gut zu wissen

- Mit einer **kostenlosen Apple-ID** läuft die App **7 Tage**, danach in Sideloadly
  einfach erneut installieren (Spielstände bleiben erhalten). Mit einem Apple-Entwickler-
  konto (99 €/Jahr) läuft sie ein Jahr.
- Die App funktioniert komplett **offline** – das ganze Spiel samt Wörterbuch steckt drin.
- Alternative zu Sideloadly: **AltStore** (<https://altstore.io>), kann alle 7 Tage
  automatisch per WLAN neu signieren.
