# STATO — fonte di verità sullo stato dell'Officina

Ultimo aggiornamento: 2026-08-30 · Sprint: 001

## Delibere in vigore

- **DEL-0001** — Metodo: agenzia per committenti esterni con metodo da
  startup interna. Gerarchia dei veti: compliance → scope/budget → rilascio →
  fonti/licenze → validazione della domanda.
- **DEL-0002** — Architettura di lavoro: repo git indipendente da Motore
  Talento, Drive come specchio in sola lettura pensato per la messa online.
- **DEL-0003** — Il Regista non produce mai contenuto di dominio
  (architettura, codice), nemmeno sotto budget stretto: sempre delega ad
  `architetto` e a `sviluppatore-backend`/`sviluppatore-frontend`. Nata da
  una scorciatoia presa dal Regista su RADAR IA e non autorizzata dal
  committente — debito registrato in
  `70_progetti/radar-ia/DEBITO_TECNICO.md`.
- **DEL-0004** — Quando il budget di una commessa è "risorse
  dell'abbonamento, nessun credito aggiuntivo", il Regista programma di
  default una ripresa automatica del lavoro (Routine periodica) al posto
  di fermarsi silenziosamente su limite di sessione. Applicata la prima
  volta su RADAR IA (Routine `trig_01MsNvLecksQF6tXEU4A8sug`, ogni 3 ore).

## Commesse attive

- **RADAR IA** (`70_progetti/radar-ia/`) — commessa reale piccola (risolve
  D-001), committente = utente reale. Fase: Scoping in chiusura → Prototipo.
  Prototipo Minimo Verificabile: catalogo di risorse (CRUD
  aggiungi/visualizza/segna "letta-provata"), non l'intera rete/community a
  regime. Ipotesi di Valore compilata (DESIGN), Segnale dichiarato
  debole/auto-riferito. Bloccata su budget/scadenza/redditività non ancora
  dichiarati dal committente — vedi domande aperte in
  `70_progetti/radar-ia/STATO_COMMESSA.md`.

## Coda — Sprint 002 (in attesa della prima commessa)

Nessun task tecnico residuo propedeutico: i quattro task interni della coda
Sprint 001 sono tutti completati (vedi Fatto). Il prossimo Sprint si apre
solo quando arriva una commessa reale (D-001 in `DOMANDE_APERTE.md`), oppure
per chiudere D-002 (stack di default) in Consiglio se la questione blocca
concretamente l'avvio di una commessa.

## Fatto

- 2026-08-30 — Sprint 000: struttura del repo, protocollo a due unità
  (Sprint/Fase di Commessa), undici mandati, gerarchia dei veti, gate di
  rigore adattato.
- 2026-08-30 — Sprint 001 (lavoro interno, propedeutico alla prima
  commessa; nessuna commessa attiva, nessun Punto di Decisione da attendere):
  - `referente-commessa` — `70_progetti/_TEMPLATE/SCOPING.md` riscritto con
    19 domande esplicite di intervista al committente (raggruppate per
    tema: committente/utenti, scope dentro/fuori, ipotesi di valore e
    redditività, vincoli/compliance, budget/governance); aggiunta sezione
    "fuori scope" mancante, base concreta per il veto su scope creep.
    `STATO_COMMESSA.md` del template esteso con tabella
    promesso/consegnato/manca e sezione budget/tempo.
  - `devops-sicurezza` — `60_conoscenza/checklist-rilascio/v0.md`: checklist
    binaria OWASP Top 10 (tutte e dieci le categorie), gestione segreti,
    backup con distinzione configurato/testato, piano di rollback, verifica
    finale che lega ogni "no" residuo a `DEBITO_RISCHIO.md` con scadenza.
  - `custode` — `50_compliance/PARERE_QUADRO_DATI.md`: parere quadro
    riusabile su basi giuridiche GDPR, minimizzazione operativa,
    accessibilità, dark pattern, AI Act, criteri DPIA. Verdetto: FIRMATA.
    Ha segnalato due lacune, riportate in `DOMANDE_APERTE.md` (D-004, D-005).
  - `archivista-prodotto` — `60_conoscenza/pattern/` popolato con 5 pattern
    (autenticazione, pagamenti, onboarding-utente, upload-file,
    notifiche-transazionali), tutti etichettati **DA VERIFICARE** (nessuna
    commessa reale li ha ancora usati) con licenze verificate per ogni
    libreria citata e fonte tracciabile.
  - Gate `strumenti/controllo_rigore.py`: individuati 2 falsi positivi di
    rango 1 (il regex "dark pattern vietato" scattava anche nei documenti
    che lo vietano esplicitamente, `50_compliance/` e `60_conoscenza/`).
    Corretto estendendo l'esenzione `e_governo()` a questi due domini, sullo
    stesso principio già applicato a `CLAUDE.md`/`_TEMPLATE`/`00_delibere`.
    Gate verde dopo la correzione (0 errori, 1 lacuna aperta residua in
    `strumenti/sync_drive.md`, nota da D-003).

## Note per il prossimo Sprint

L'Officina ha ora template di Scoping, checklist di rilascio, parere quadro
dati e una base di pattern iniziale: pronta a ricevere la prima commessa
(D-001 ancora aperta, bloccante). Nessun altro lavoro interno è in coda:
il prossimo Sprint si apre sulla prima commessa reale, non su altro lavoro
propedeutico.
