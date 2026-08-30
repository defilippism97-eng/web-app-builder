#!/usr/bin/env python3
"""Test automatici sul percorso critico dei 3 endpoint API (estinzione
DT-0004, mandato Sviluppatore Backend — MANDATI.md §5).

Solo unittest della libreria standard, nessuna dipendenza esterna (coerente
con tecnico/ARCHITETTURA.md). Avvia il server reale su una porta di test
dedicata, con un database SQLite temporaneo separato da quello di
sviluppo/produzione (data/radar.db), e lo interroga via HTTP.

Uso:
    python3 -m unittest test_server -v
"""

import json
import os
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import server as radar

PORTA_TEST = 8421
BASE_URL = f"http://127.0.0.1:{PORTA_TEST}"


class TestAPIRadarIA(unittest.TestCase):
    """Percorso critico: creare una risorsa, leggerla, aggiornarne lo
    stato — il flusso che l'utente userà davvero (aggiungi al catalogo,
    vedi l'elenco, segna come letta/provata)."""

    @classmethod
    def setUpClass(cls):
        # DB temporaneo isolato, non quello di sviluppo/produzione.
        cls._tmpdir = tempfile.TemporaryDirectory()
        radar.DB_PATH = os.path.join(cls._tmpdir.name, "test_radar.db")
        radar.inizializza_db()

        cls.server = ThreadingHTTPServer(("127.0.0.1", PORTA_TEST), radar.GestoreRadarIA)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls._tmpdir.cleanup()

    def _richiesta(self, metodo, percorso, corpo=None):
        dati = json.dumps(corpo).encode("utf-8") if corpo is not None else None
        richiesta = urllib.request.Request(
            f"{BASE_URL}{percorso}",
            data=dati,
            method=metodo,
            headers={"Content-Type": "application/json"} if dati else {},
        )
        try:
            with urllib.request.urlopen(richiesta) as risposta:
                return risposta.status, json.loads(risposta.read().decode("utf-8"))
        except urllib.error.HTTPError as errore:
            return errore.code, json.loads(errore.read().decode("utf-8"))

    def test_01_lista_iniziale_e_creazione(self):
        status, corpo = self._richiesta("GET", "/api/risorse")
        self.assertEqual(status, 200)
        self.assertIsInstance(corpo, list)

        status, creata = self._richiesta(
            "POST",
            "/api/risorse",
            {"titolo": "Un articolo utile", "url": "https://example.com/a",
             "tipo": "pratica", "note": "letto sabato"},
        )
        self.assertEqual(status, 201)
        for campo in ("id", "titolo", "url", "tipo", "note", "stato",
                      "creato_il", "aggiornato_il"):
            self.assertIn(campo, creata)
        self.assertEqual(creata["stato"], "da_provare")
        self.assertEqual(creata["titolo"], "Un articolo utile")

        status, lista = self._richiesta("GET", "/api/risorse")
        self.assertEqual(status, 200)
        self.assertTrue(any(r["id"] == creata["id"] for r in lista))

    def test_02_creazione_senza_titolo_400(self):
        status, corpo = self._richiesta("POST", "/api/risorse", {"titolo": "  "})
        self.assertEqual(status, 400)
        self.assertIn("errore", corpo)

    def test_03_creazione_url_non_http_400(self):
        status, corpo = self._richiesta(
            "POST", "/api/risorse", {"titolo": "Prova", "url": "javascript:alert(1)"}
        )
        self.assertEqual(status, 400)
        self.assertIn("errore", corpo)

        status, corpo = self._richiesta(
            "POST", "/api/risorse", {"titolo": "Prova", "url": "non-una-url"}
        )
        self.assertEqual(status, 400)

    def test_04_creazione_url_assente_ok(self):
        status, corpo = self._richiesta("POST", "/api/risorse", {"titolo": "Senza url"})
        self.assertEqual(status, 201)
        self.assertEqual(corpo["url"], "")

    def test_05_patch_stato(self):
        status, creata = self._richiesta(
            "POST", "/api/risorse", {"titolo": "Da aggiornare", "tipo": "strumento"}
        )
        self.assertEqual(status, 201)

        status, aggiornata = self._richiesta(
            "PATCH", f"/api/risorse/{creata['id']}", {"stato": "letta_provata"}
        )
        self.assertEqual(status, 200)
        self.assertEqual(aggiornata["stato"], "letta_provata")
        self.assertEqual(aggiornata["id"], creata["id"])

        status, lista = self._richiesta("GET", "/api/risorse")
        aggiornata_in_lista = next(r for r in lista if r["id"] == creata["id"])
        self.assertEqual(aggiornata_in_lista["stato"], "letta_provata")

    def test_06_patch_risorsa_inesistente_404(self):
        status, corpo = self._richiesta("PATCH", "/api/risorse/999999", {"stato": "letta_provata"})
        self.assertEqual(status, 404)

    def test_07_patch_stato_non_ammesso_400(self):
        status, creata = self._richiesta("POST", "/api/risorse", {"titolo": "Altra"})
        status, corpo = self._richiesta(
            "PATCH", f"/api/risorse/{creata['id']}", {"stato": "invalido"}
        )
        self.assertEqual(status, 400)


if __name__ == "__main__":
    unittest.main()
