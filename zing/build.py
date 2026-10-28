"""Baut scrabble_zing.html: bettet die Wortlisten in zing_src.html ein."""
import re
from pathlib import Path

here = Path(__file__).parent
words = set()

def add(raw):
    w = re.sub(r"[^A-ZÄÖÜ]", "", raw.upper().replace("ß", "SS"))
    if 2 <= len(w) <= 15:
        words.add(w)

for line in (here / "scrabble_2-8_buchstaben.txt").read_text(encoding="utf-8").splitlines():
    add(line)

# offizielle Liste: nur kommagetrennte Wortzeilen, keine Kommentare/Überschriften
for line in (here / "offizielle_scrabble_zing_wortliste.txt").read_text(encoding="utf-8").splitlines():
    s = line.strip()
    if not s or s[0] in "#=" or ":" in s:
        continue
    for tok in s.split(","):
        tok = tok.strip()
        if re.fullmatch(r"[A-ZÄÖÜß]+", tok):
            add(tok)

src = (here / "zing_src.html").read_text(encoding="utf-8")

# Beutel aus der Seitenleiste als eigenständiges SVG (für Fenster-, iPhone- und EXE-Symbol)
import base64, io
bag_start = src.index('<svg class="abs" id="bag"')
bag_svg = src[bag_start:src.index("</svg>", bag_start) + len("</svg>")]
bag_svg = bag_svg.replace('<svg class="abs" id="bag" viewBox="0 0 330 430" aria-hidden="true">',
                          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 95 330 335">', 1)


def render_bag_png(png):
    """Rendert den Beutel mit Edge (headless) als PNG mit transparentem Hintergrund."""
    import subprocess, tempfile
    edge = next((p for p in (Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
                             Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe")) if p.exists()), None)
    if not edge:
        return False
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "icon.html"
        page.write_text('<!doctype html><html><body style="margin:0;background:transparent">' +
                        bag_svg.replace('viewBox=', 'width="512" height="512" viewBox=', 1) +
                        "</body></html>", encoding="utf-8")
        subprocess.run([str(edge), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--user-data-dir={tmp}\\prof", "--default-background-color=00000000",
                        "--window-size=512,512", f"--screenshot={png}", page.as_uri()],
                       capture_output=True, timeout=60)
        # Edge schreibt den Screenshot aus einem Kindprozess – kurz darauf warten
        import time
        for _ in range(40):
            if Path(png).exists() and Path(png).stat().st_size > 0:
                time.sleep(0.5)
                break
            time.sleep(0.5)
    return Path(png).exists()


def tile_icon_image():
    """Ersatz-Symbol ohne Edge: cremefarbener Spielstein mit Z."""
    from PIL import Image, ImageDraw, ImageFont
    s = 256
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((14, 20, s - 10, s - 4), 30, fill=(150, 125, 70, 255))
    d.rounded_rectangle((8, 8, s - 16, s - 16), 30, fill=(246, 236, 200, 255), outline=(185, 160, 100, 255), width=6)
    try:
        big = ImageFont.truetype("georgiab.ttf", 170)
        small = ImageFont.truetype("georgiab.ttf", 52)
    except OSError:
        big = small = ImageFont.load_default()
    d.text((118, 118), "Z", font=big, fill=(20, 15, 10, 255), anchor="mm")
    d.text((200, 196), "3", font=small, fill=(20, 15, 10, 255), anchor="mm")
    return img


def icon_image():
    """Symbol als quadratisches RGBA-Bild (256 px): der Beutel, sonst der Ersatz-Spielstein."""
    from PIL import Image
    png = here / "zing_icon.png"
    png.unlink(missing_ok=True)
    if render_bag_png(png):
        img = Image.open(png).convert("RGBA")
        png.unlink()
        img = img.crop(img.getbbox() or (0, 0, 512, 512))
        side = max(img.size)
        sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        sq.paste(img, ((side - img.width) // 2, (side - img.height) // 2))
        return sq.resize((256, 256), Image.LANCZOS)
    return tile_icon_image()


def save_ico(img, path):
    """Schreibt das Symbol über eine Zwischendatei (die alte .ico kann von Windows gesperrt sein)."""
    import os
    tmp = Path(path).with_suffix(".new.ico")
    img.save(tmp, sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    os.replace(tmp, path)


def touch_icon_png(img, size=180):
    """iPhone-/App-Symbol: iOS füllt Transparenz schwarz, daher orangefarbener Hintergrund."""
    from PIL import Image
    bg = Image.new("RGBA", (size, size), (241, 101, 52, 255))
    inner = round(size * 5 / 6)
    bag = img.resize((inner, inner), Image.LANCZOS)
    bg.alpha_composite(bag, ((size - inner) // 2, (size - inner) // 2))
    buf = io.BytesIO()
    bg.convert("RGB").save(buf, "PNG")
    return buf.getvalue()


icon = None
try:
    icon = icon_image()
except ImportError:
    print("Pillow fehlt – ohne iPhone- und EXE-Symbol gebaut")

head = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,' + \
       base64.b64encode(bag_svg.encode("utf-8")).decode("ascii") + '">'
if icon is not None:
    head += '\n<link rel="apple-touch-icon" href="data:image/png;base64,' + \
            base64.b64encode(touch_icon_png(icon)).decode("ascii") + '">'

out = src.replace("__WORDS__", " ".join(sorted(words)), 1).replace("</title>", "</title>\n" + head, 1)
(here / "scrabble_zing.html").write_text(out, encoding="utf-8")
print(f"{len(words)} Wörter eingebettet, {len(out.encode('utf-8')) // 1024} KB")

# iOS-App (Capacitor): Spiel und App-Symbol ins App-Projekt legen; gebaut wird per GitHub Actions
ios = here.parent / "ios-app"
if ios.exists():
    (ios / "www").mkdir(exist_ok=True)
    (ios / "www" / "index.html").write_text(out, encoding="utf-8")
    if icon is not None:
        (ios / "resources").mkdir(exist_ok=True)
        (ios / "resources" / "icon-1024.png").write_bytes(touch_icon_png(icon, 1024))
    print("iOS-App-Projekt aktualisiert (../ios-app/www, ../ios-app/resources)")


# Portable EXE (nur Windows, nutzt den mitgelieferten C#-Compiler von .NET Framework 4)
csc = Path(r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe")
if csc.exists() and icon is not None:
    import subprocess
    save_ico(icon, here / "zing.ico")
    r = subprocess.run([str(csc), "/nologo", "/target:winexe", "/optimize+", "/out:Zing.exe",
                        "/resource:scrabble_zing.html,zing.html", "/win32icon:zing.ico",
                        "/r:System.Windows.Forms.dll", "launcher.cs"],
                       cwd=here, capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr)
        raise SystemExit("EXE-Bau fehlgeschlagen")
    print(f"Zing.exe gebaut, {(here / 'Zing.exe').stat().st_size // 1024} KB")
