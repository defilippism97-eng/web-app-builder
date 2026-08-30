-- Schema corretto in tecnico/ARCHITETTURA.md (revisione architetto,
-- estinzione DT-0002): "risorsa" (identità condivisibile) separata da
-- "interazione" (relazione utente-risorsa: stato, note). Nel perimetro
-- single-user di oggi ogni risorsa ha esattamente un'interazione implicita
-- (utente_id NULL); l'aggregazione multi-utente resta fuori scope.

CREATE TABLE IF NOT EXISTS risorse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    url TEXT,
    url_canonico TEXT,          -- normalizzato, per dedup futura (oggi non applicata)
    tipo TEXT NOT NULL DEFAULT 'pratica' CHECK (tipo IN ('pratica','strumento','esperimento')),
    creato_il TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS interazioni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    risorsa_id INTEGER NOT NULL REFERENCES risorse(id),
    utente_id INTEGER,          -- NULL oggi (single-user); popolato con l'autenticazione
    note TEXT DEFAULT '',
    stato TEXT NOT NULL DEFAULT 'da_provare' CHECK (stato IN ('da_provare','letta_provata')),
    aggiornato_il TEXT NOT NULL DEFAULT (datetime('now'))
);
