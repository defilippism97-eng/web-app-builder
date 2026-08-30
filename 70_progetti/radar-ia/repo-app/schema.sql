CREATE TABLE IF NOT EXISTS risorse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    url TEXT,
    tipo TEXT NOT NULL DEFAULT 'pratica' CHECK (tipo IN ('pratica', 'strumento', 'esperimento')),
    note TEXT DEFAULT '',
    stato TEXT NOT NULL DEFAULT 'da_provare' CHECK (stato IN ('da_provare', 'letta_provata')),
    creato_il TEXT NOT NULL DEFAULT (datetime('now')),
    aggiornato_il TEXT NOT NULL DEFAULT (datetime('now'))
);
