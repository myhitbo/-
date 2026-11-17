#!/usr/bin/env python3
"""Récupère depuis Sefaria la paracha de la semaine (7 alyot, texte hébreu + Onkelos)
et écrit web/data/text.js. En cas d'échec, laisse le fichier de secours en place."""
import datetime, html, json, os, re, sys, urllib.request, urllib.parse

API = "https://www.sefaria.org/api"
OUT = os.path.join(os.path.dirname(__file__), "..", "web", "data", "text.js")
DIASPORA = os.environ.get("SM_DIASPORA", "1")
WEEKS = int(os.environ.get("SM_WEEKS", "4"))  # semaine en cours + 3 suivantes
MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

EN = ["Bereshit","Noach","Lech-Lecha","Vayera","Chayei Sara","Toldot","Vayetzei","Vayishlach","Vayeshev","Miketz","Vayigash","Vayechi",
      "Shemot","Vaera","Bo","Beshalach","Yitro","Mishpatim","Terumah","Tetzaveh","Ki Tisa","Vayakhel","Pekudei",
      "Vayikra","Tzav","Shmini","Tazria","Metzora","Achrei Mot","Kedoshim","Emor","Behar","Bechukotai",
      "Bamidbar","Nasso","Beha'alotcha","Sh'lach","Korach","Chukat","Balak","Pinchas","Matot","Masei",
      "Devarim","Vaetchanan","Eikev","Re'eh","Shoftim","Ki Teitzei","Ki Tavo","Nitzavim","Vayeilech","Ha'Azinu","V'Zot HaBerachah"]
FR = ["Béréchit","Noa'h","Lekh Lekha","Vayéra","'Hayé Sarah","Toledot","Vayétsé","Vayichla'h","Vayéchev","Mikets","Vayigach","Vayé'hi",
      "Chemot","Vaéra","Bo","Bechala'h","Yitro","Michpatim","Terouma","Tetsavé","Ki Tissa","Vayakhel","Pekoudé",
      "Vayikra","Tsav","Chemini","Tazria","Metsora","A'harei Mot","Kedochim","Emor","Behar","Be'houkotaï",
      "Bamidbar","Nasso","Behaalotekha","Chela'h","Kora'h","'Houkat","Balak","Pin'has","Matot","Massé'i",
      "Devarim","Vaet'hanan","Ekev","Reé","Choftim","Ki Tetsé","Ki Tavo","Nitsavim","Vayélekh","Haazinou","Vezot Haberakha"]
BOOKS = {"Genesis":"Béréchit","Exodus":"Chemot","Leviticus":"Vayikra","Numbers":"Bamidbar","Deuteronomy":"Devarim"}
ALYA = [("Rishon","רִאשׁוֹן"),("Sheni","שֵׁנִי"),("Shlishi","שְׁלִישִׁי"),("Revi'i","רְבִיעִי"),("Hamishi","חֲמִישִׁי"),("Shishi","שִׁשִּׁי"),("Shvi'i","שְׁבִיעִי")]
DAYS = ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Shabbat"]

def get(path, **params):
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"User-Agent": "shnayim-mikra-app/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def clean(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    s = html.unescape(s)
    s = re.sub(r"\s*\{[פס]\}\s*", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def verses(ref):
    """ref 'Genesis 29:18-30:13' -> [(ch, v, text)]"""
    d = get("/texts/" + urllib.parse.quote(ref.replace(" ", "_")), context=0, commentary=0, pad=0)
    he = d.get("he") or []
    sec = d.get("sections") or [1, 1]
    ch, v0 = int(sec[0]), int(sec[1]) if len(sec) > 1 else 1
    out = []
    if he and isinstance(he[0], list):
        for ci, chap in enumerate(he):
            start = v0 if ci == 0 else 1
            for vi, t in enumerate(chap):
                out.append((ch + ci, start + vi, clean(t)))
    else:
        for vi, t in enumerate(he):
            out.append((ch, v0 + vi, clean(t)))
    return out

def span(ref):
    m = re.match(r"^[A-Za-z ]+?\s+(\d+):(\d+)-(?:(\d+):)?(\d+)$", ref)
    if not m: return ref
    c1, v1, c2, v2 = m.groups()
    return f"{c1}:{v1} – {v2}" if not c2 or c2 == c1 else f"{c1}:{v1} – {c2}:{v2}"

def week(day):
    """Paracha lue le Shabbat qui suit `day` (date), avec ses 7 alyot."""
    cal = get("/calendars", diaspora=DIASPORA, year=day.year, month=day.month, day=day.day)
    item = next(i for i in cal["calendar_items"] if i["title"]["en"] == "Parashat Hashavua")
    en = item["displayValue"]["en"]; he = item["displayValue"]["he"]; ref = item["ref"]
    parts = [p.strip() for p in en.split("-")] if en not in EN else [en]
    idx = EN.index(parts[0]) if parts[0] in EN else -1
    fr = " – ".join(FR[EN.index(p)] if p in EN else p for p in parts)
    book = ref.split(" ")[0]
    aliyot_refs = (item.get("extraDetails") or {}).get("aliyot", [])[:7]
    if len(aliyot_refs) < 7: raise RuntimeError("aliyot manquantes pour " + en)
    alyot = []
    for i, aref in enumerate(aliyot_refs):
        mik = verses(aref)
        onk_map = {(c, v): t for c, v, t in verses("Onkelos " + aref)}
        vs = [{"ref": f"{c}:{v}", "he": t, "onk": onk_map.get((c, v), "")} for c, v, t in mik]
        alyot.append({"name": ALYA[i][0], "heb": ALYA[i][1], "day": DAYS[i], "verses": span(aref), "min": max(3, round(len(vs) * 0.4)), "ref": aref, "v": vs})
        print(f"  {ALYA[i][0]}: {aref} — {len(vs)} versets, Onkelos {len(onk_map)}", file=sys.stderr)
    shabbat = day + datetime.timedelta(days=(5 - day.weekday()) % 7)
    return {"parasha": fr, "parashaEn": en, "parashaHe": he, "parashaRef": BOOKS.get(book, book) + " " + span(ref),
            "parashaIndex": idx, "shabbat": f"{shabbat.day} {MOIS[shabbat.month - 1]}", "alyot": alyot}

def main():
    today = datetime.date.today()
    weeks = []
    for k in range(WEEKS):
        try:
            w = week(today + datetime.timedelta(days=7 * k))
            print(f"Semaine {k}: {w['parasha']} ({w['parashaEn']}) — Shabbat {w['shabbat']}", file=sys.stderr)
            weeks.append(w)
        except Exception as e:
            if k == 0: raise
            print(f"Semaine {k} ignorée : {e}", file=sys.stderr)
    data = dict(weeks[0]); data.update({"source": "Sefaria (sefaria.org)", "diaspora": DIASPORA == "1", "weeks": weeks})
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("window.SM_TEXT = " + json.dumps(data, ensure_ascii=False) + ";\n")
    print(f"OK : {len(weeks)} parachiyot ({', '.join(w['parasha'] for w in weeks)})", file=sys.stderr)

if __name__ == "__main__":
    try: main()
    except Exception as e:
        print("Sefaria indisponible, texte de secours conservé :", e, file=sys.stderr)
