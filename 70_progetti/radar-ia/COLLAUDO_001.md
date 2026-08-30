---
id: COLLAUDO-0001
titolo: Collaudo — Mockup community RADAR IA (DEL-LOCALE-001) e continuità del catalogo esistente
mandato: collaudatore
commessa: radar-ia
etichetta: N/A
parere_rilascio: non richiesto
stato: consegnato
data: 2026-08-30
---

## Verdetto

**PASSA.**

Ho avviato il servizio dal vivo (non letto solo il codice) e navigato sia il
catalogo esistente sia il mockup community con un vero browser (Playwright/
Chromium). Nessun problema bloccante trovato. Un'osservazione minore
(non bloccante) riportata in fondo.

## Setup di collaudo

- Avviato `RADAR_IA_PORT=8430 python3 server.py` da
  `70_progetti/radar-ia/repo-app/`, in background, log su file.
- Browser reale: Chromium via Playwright (Node), navigazione effettiva delle
  pagine, click reali sui pulsanti, screenshot a ogni passo, intercettazione
  di tutte le richieste di rete generate dalla pagina, più cross-check sui
  log del processo server Python.
- Al termine: server fermato (kill del processo), `data/radar.db` cancellato,
  cartella `data/` lasciata vuota. `git status` sul repo-app conferma nessun
  file di dati residuo tracciato (la cartella `data/*.db` è comunque in
  `.gitignore`).

## 1. Catalogo esistente (scope firmato, SCOPING.md §7) — deve restare invariato

Passi eseguiti e osservazioni:

1. `GET /` → 200, pagina caricata correttamente (verificato sia via `curl`
   sia via screenshot Playwright): form "Aggiungi una risorsa", elenco
   "Catalogo" con filtri Tutte/Da provare/Letta-provata.
2. `GET /api/risorse` prima di aggiungere → `[]` (catalogo vuoto, atteso, DB
   di test pulito).
3. `POST /api/risorse` con una risorsa di prova (titolo, url, tipo,
   descrizione) → `201`, corpo di risposta con id, stato iniziale
   `"da_provare"`, timestamp di creazione/aggiornamento popolati.
4. `GET /api/risorse` dopo il POST → la risorsa compare nell'elenco, dato
   persistito correttamente.
5. Navigazione via browser: la risorsa appena creata è visibile nel pannello
   "Catalogo" della pagina `/`, con pulsante "✓ Letta/provata — segna come da
   provare" (screenshot acquisito).
6. Tentativo di `PATCH /api/risorse/1` con `{"stato":"provata"}` (valore
   plausibile ma sbagliato) → l'API rifiuta correttamente con `400` e
   messaggio esplicito `"stato non ammesso: deve essere uno tra
   ['da_provare', 'letta_provata']"` — comportamento di validazione robusto,
   non un bug.
7. `PATCH /api/risorse/1` con lo stato corretto `{"stato":"letta_provata"}` →
   `200`, `GET /api/risorse` successivo conferma il cambio di stato
   persistito e il campo `aggiornato_il` aggiornato.

**Esito**: il CRUD di base del catalogo (aggiungere, visualizzare, segnare
come "letta/provata") funziona esattamente come da scope firmato. Nessuna
regressione osservata rispetto al comportamento atteso.

## 2. Mockup community (DEL-LOCALE-001) — navigazione dal vivo con browser reale

Pagine visitate: `/community/index.html` (Feed), `/community/post.html?id=1`
(dettaglio post normale), `/community/post.html?id=5` (variante "richiesta di
aiuto"), `/community/progetti.html` (vetrina progetti).

### 2.1 Banner "Anteprima — non ancora attivo"

- Presente e **visivamente leggibile** su tutte e quattro le pagine fin dal
  primo caricamento (verificato via screenshot, non solo via markup): fascia
  gialla (`--giallo` #F2C94C) in alto, testo nero in grassetto: "ANTEPRIMA —
  non ancora attivo. I contenuti sono di esempio, nessuna persona reale sta
  scrivendo qui."
- Verificato che resta visibile durante lo scroll: ho scrollato la pagina
  Feed di 600px e il banner (CSS `position: sticky; top: 0`) rimane ancorato
  in cima, leggibile, non scompare (screenshot acquisito).
- Nessun pulsante di chiusura presente: il banner non è mai nascosto/
  disattivabile.

### 2.2 Pulsanti di interazione sociale — nessuna azione reale

Ho cliccato dal vivo, con Playwright, mentre intercettavo tutte le richieste
di rete della pagina e in parallelo osservavo il log del processo server:

- "Mi piace" sul feed → mostra toast "In arrivo — questa funzione non è
  ancora attiva." (screenshot acquisito). Nessun contatore che cambia.
- "Commenta" sul feed → stesso toast.
- Nel dettaglio post (id=1): ho scritto un testo in "Scrivi un commento…" e
  cliccato "Invia commento" → toast "in arrivo", **nessun commento aggiunto**
  (verificato che il testo "Nessun commento tra gli esempi." resta presente
  dopo l'invio, cioè non c'è stato nessun finto successo).
- "Unisciti" nella vetrina progetti → toast "in arrivo", nessuna schermata
  di conferma iscrizione, nessun cambio di stato del progetto.
- Nel dettaglio "richiesta di aiuto" (id=5): ho scritto un testo in
  "Rispondi…" e cliccato "Invia risposta" → toast "in arrivo", nessuna
  risposta aggiunta all'elenco (resta "Nessuna risposta tra gli esempi.").
- **Verifica di rete**: durante l'intera sessione di navigazione e click
  (Feed, dettaglio post, dettaglio richiesta d'aiuto, vetrina progetti, più
  tutti i click sopra) l'elenco delle richieste HTTP intercettate da
  Playwright contiene **zero** chiamate verso `/api/`. Confermato in modo
  indipendente controllando in parallelo il log del processo server Python:
  le uniche righe generate durante la navigazione del mockup sono `GET` di
  file statici (`.html`, `.css`, `.js`); nessuna riga con metodo diverso da
  `GET` né con path `/api/*` compare per l'intera durata del test del
  mockup. Coerente con l'ispezione del codice (`community.js`, `dati.js`):
  nessuna `fetch`/`XMLHttpRequest`, nessun uso di `localStorage`, dati
  hardcoded in `dati.js`.

### 2.3 Autori dei post d'esempio

Ogni autore ("Marta R.", "Luca D.", "Sara T.", "Fede B.", "Giorgio N.",
più i due commentatori "Anna P." e "Marco V." nel dettaglio) porta accanto
al nome un badge "esempio" ben visibile, sia nel Feed sia nelle viste di
dettaglio (screenshot acquisiti). Nessuna ambiguità visiva: il badge è
leggibile a uno sguardo veloce, non un dettaglio nascosto.

### 2.4 Nessuna schermata di login

Ho verificato via ricerca testuale in tutti i file `.html`/`.js` della
cartella `community/`: nessuna occorrenza di "login", "password", "profilo"
o "account" se non nella frase di disclaimer ("nessun account"). Coerente
con `MOCKUP_COMMUNITY.md` §1.5, che indicava il Profilo come vista
facoltativa a bassa priorità, la prima da tagliare col budget stretto: lo
sviluppatore-frontend l'ha correttamente tagliata, non c'è nessuna schermata
di login né scenografica né funzionante da valutare.

### 2.5 Link catalogo ↔ mockup

- Sul catalogo (`/`), in fondo alla pagina: link testuale "Anteprima
  community (mockup, non ancora attiva) →" verificato presente, cliccabile
  con Playwright, porta correttamente a `/community/index.html`.
  Distinto dal contenuto reale (non integrato come tab di pari livello),
  coerente con la raccomandazione di design.
- Sul mockup, link di ritorno "← Torna al catalogo (prodotto reale)"
  verificato cliccabile, riporta correttamente a `/` (catalogo reale).

## 3. Valutazione d'esperienza (occhio di chi non ha scritto il codice)

- È chiaro fin dal primo secondo cosa si sta guardando: il banner giallo è
  la prima cosa visibile, il titolo di pagina del browser stesso dice
  "RADAR IA — Anteprima community (mockup)", e ogni pagina ripete in fondo
  "Mockup non funzionante — nessun dato reale, nessun account, nessuna
  interazione salvata." Tre livelli di rinforzo (banner, titolo pagina,
  footer) — nessuno dei quali richiede di cercare o scrollare per trovarlo.
- Nessun elemento osservato potrebbe far credere per errore di star
  interagendo con persone reali: i toast sono espliciti ("questa funzione
  non è ancora attiva"), non c'è alcun feedback che simuli successo, i nomi
  degli autori sono marcati, non esiste una superficie che assomigli a un
  login/account reale.
- Riuso coerente dell'identità visiva del catalogo (palette, font, pattern
  di card) — non introduce un secondo linguaggio visivo, come richiesto dal
  concept.

## 4. Osservazione non bloccante

- `MOCKUP_COMMUNITY.md` §1.2 descriveva il campo "modello/temperatura" nel
  dettaglio post come dato d'esempio con valori indicativi; nell'implementazione
  compaiono come `—` (placeholder vuoto). Non è un problema di funzionamento
  né di Delibera, è una scelta di contenuto minore — la segnalo solo per
  completezza, non è materia di veto del Collaudatore (non è né una
  funzionalità rotta né una violazione della Delibera).
- Non ho potuto verificare la licenza del font Inter (fuori mandato del
  Collaudatore, resta compito dell'Archivista di Prodotto, già segnalato
  come `[[LACUNA]]` aperta sia in `MOCKUP_COMMUNITY.md` sia in `SCOPING.md`
  — non bloccante per questo collaudo locale, ma da chiudere prima di una
  Consegna che esca stabilmente verso il committente).

## Sintesi per il Referente di Commessa

- Scope firmato del catalogo: **confermato funzionante**, nessuna
  regressione.
- Vincoli di `DEL-LOCALE-001-mockup-community.md` (banner sempre visibile,
  nessuna azione sociale reale, nessuna chiamata di rete verso `/api/`
  generata dal mockup, autori marcati come esempio, nessuna schermata di
  login funzionante o scenografica) verificati **tutti rispettati
  nell'esperienza reale**, non solo nel codice sorgente.
- Nessun problema bloccante. Nessun veto.
