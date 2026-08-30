#!/usr/bin/env python3
"""RADAR IA — prototipo catalogo risorse (Prototipo Minimo Verificabile).

Solo libreria standard, nessuna dipendenza esterna (vedi
70_progetti/radar-ia/tecnico/ARCHITETTURA.md per il perché).

Single-user, nessuna autenticazione (decisione esplicita del committente,
SCOPING.md §5): pensato per girare in locale sulla macchina del
committente, non per essere esposto pubblicamente. Non superare la
checklist di rilascio (60_conoscenza/checklist-rilascio/v0.md) prima di
qualunque esposizione pubblica.

Uso:
    python3 server.py            # ascolta su 127.0.0.1:8420
"""

import json
import os
import re
import sqlite3
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

RADICE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(RADICE, "data", "radar.db")
SCHEMA_PATH = os.path.join(RADICE, "schema.sql")
STATIC_DIR = os.path.join(RADICE, "static")

TIPI_AMMESSI = {"pratica", "strumento", "esperimento"}
STATI_AMMESSI = {"da_provare", "letta_provata"}

RE_ID = re.compile(r"^/api/risorse/(\d+)$")


def connetti_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        conn.executescript(f.read())
    return conn


def adesso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def riga_a_dict(riga):
    return {chiave: riga[chiave] for chiave in riga.keys()}


class GestoreRadarIA(BaseHTTPRequestHandler):
    server_version = "RadarIA/0.1"

    def log_message(self, formato, *args):
        # Log minimale su stdout, nessun dato sensibile (nessun dato
        # personale trattato in questo prototipo, SCOPING.md §5).
        print(f"[{self.log_date_time_string()}] {formato % args}")

    def _json(self, status, payload):
        corpo = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def _errore(self, status, messaggio):
        self._json(status, {"errore": messaggio})

    def _leggi_corpo_json(self):
        lunghezza = int(self.headers.get("Content-Length", 0))
        if lunghezza == 0:
            return {}
        grezzo = self.rfile.read(lunghezza)
        try:
            dati = json.loads(grezzo.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None
        return dati if isinstance(dati, dict) else None

    # --- routing -----------------------------------------------------

    def do_GET(self):
        percorso = urlparse(self.path).path
        if percorso == "/api/risorse":
            return self._lista_risorse()
        if percorso in ("/", ""):
            return self._servi_statico("/index.html")
        return self._servi_statico(percorso)

    def do_POST(self):
        percorso = urlparse(self.path).path
        if percorso == "/api/risorse":
            return self._crea_risorsa()
        self._errore(404, "non trovato")

    def do_PATCH(self):
        percorso = urlparse(self.path).path
        m = RE_ID.match(percorso)
        if m:
            return self._aggiorna_risorsa(int(m.group(1)))
        self._errore(404, "non trovato")

    # --- endpoint API --------------------------------------------------

    def _lista_risorse(self):
        conn = connetti_db()
        try:
            righe = conn.execute(
                "SELECT * FROM risorse ORDER BY creato_il DESC"
            ).fetchall()
            self._json(200, [riga_a_dict(r) for r in righe])
        finally:
            conn.close()

    def _crea_risorsa(self):
        dati = self._leggi_corpo_json()
        if dati is None:
            return self._errore(400, "corpo JSON non valido")

        titolo = (dati.get("titolo") or "").strip()
        if not titolo:
            return self._errore(400, "titolo obbligatorio")
        if len(titolo) > 200:
            return self._errore(400, "titolo troppo lungo (max 200 caratteri)")

        url = (dati.get("url") or "").strip()
        if len(url) > 2000:
            return self._errore(400, "url troppo lungo")

        tipo = (dati.get("tipo") or "pratica").strip()
        if tipo not in TIPI_AMMESSI:
            return self._errore(400, f"tipo non ammesso: deve essere uno tra {sorted(TIPI_AMMESSI)}")

        note = (dati.get("note") or "").strip()
        if len(note) > 2000:
            return self._errore(400, "note troppo lunghe (max 2000 caratteri)")

        conn = connetti_db()
        try:
            ora = adesso()
            cur = conn.execute(
                "INSERT INTO risorse (titolo, url, tipo, note, stato, creato_il, aggiornato_il) "
                "VALUES (?, ?, ?, ?, 'da_provare', ?, ?)",
                (titolo, url, tipo, note, ora, ora),
            )
            conn.commit()
            riga = conn.execute(
                "SELECT * FROM risorse WHERE id = ?", (cur.lastrowid,)
            ).fetchone()
            self._json(201, riga_a_dict(riga))
        finally:
            conn.close()

    def _aggiorna_risorsa(self, id_risorsa):
        dati = self._leggi_corpo_json()
        if dati is None:
            return self._errore(400, "corpo JSON non valido")

        stato = dati.get("stato")
        if stato is None or stato not in STATI_AMMESSI:
            return self._errore(400, f"stato non ammesso: deve essere uno tra {sorted(STATI_AMMESSI)}")

        conn = connetti_db()
        try:
            esiste = conn.execute(
                "SELECT id FROM risorse WHERE id = ?", (id_risorsa,)
            ).fetchone()
            if esiste is None:
                return self._errore(404, "risorsa non trovata")

            conn.execute(
                "UPDATE risorse SET stato = ?, aggiornato_il = ? WHERE id = ?",
                (stato, adesso(), id_risorsa),
            )
            conn.commit()
            riga = conn.execute(
                "SELECT * FROM risorse WHERE id = ?", (id_risorsa,)
            ).fetchone()
            self._json(200, riga_a_dict(riga))
        finally:
            conn.close()

    # --- file statici ----------------------------------------------------

    def _servi_statico(self, percorso):
        # Normalizza e blocca traversal fuori da STATIC_DIR.
        percorso_pulito = os.path.normpath(percorso).lstrip("/\\")
        percorso_assoluto = os.path.normpath(os.path.join(STATIC_DIR, percorso_pulito))
        if not percorso_assoluto.startswith(os.path.normpath(STATIC_DIR)):
            return self._errore(403, "vietato")
        if not os.path.isfile(percorso_assoluto):
            return self._errore(404, "non trovato")

        estensione = os.path.splitext(percorso_assoluto)[1]
        tipo_contenuto = {
            ".html": "text/html; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".js": "application/javascript; charset=utf-8",
        }.get(estensione, "application/octet-stream")

        with open(percorso_assoluto, "rb") as f:
            corpo = f.read()
        self.send_response(200)
        self.send_header("Content-Type", tipo_contenuto)
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)


def main():
    host = os.environ.get("RADAR_IA_HOST", "127.0.0.1")
    porta = int(os.environ.get("RADAR_IA_PORT", "8420"))
    connetti_db().close()  # crea schema/db se non esiste
    server = ThreadingHTTPServer((host, porta), GestoreRadarIA)
    print(f"RADAR IA in ascolto su http://{host}:{porta} (solo locale, nessuna autenticazione)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
