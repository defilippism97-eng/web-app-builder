---
id: 70-radar-ia-tecnico-0001
titolo: Architettura — RADAR IA (Prototipo Catalogo Risorse)
mandato: architetto
commessa: radar-ia
etichetta: DESIGN
parere_rilascio: non richiesto
stato: approvato
data: 2026-08-30
---

## Vincolo che governa questa decisione

Budget dichiarato dal committente (SCOPING.md §5): equivalente in token di
**due sessioni Claude Pro, Sonnet 5, livello di ragionamento medio**. Non è
un vincolo di ore-persona tradizionale, è un vincolo di iterazioni-agente:
la scelta tecnica deve minimizzare il rischio di dover rifare/debuggare a
lungo, non ottimizzare per eleganza a lungo termine.

## Decisione

- **Backend**: Python, solo libreria standard (`http.server` + `sqlite3`,
  nessuna dipendenza esterna da installare). Un solo processo, un solo file
  `server.py`.
- **Dati**: SQLite, un file (`data/radar.db`), schema in `schema.sql`.
- **Frontend**: HTML/CSS/JS statici, nessun bundler, nessun framework.
  Serviti dallo stesso processo Python.
- **Autenticazione**: nessuna in questo prototipo (SCOPING.md §5, decisione
  esplicita del committente di rimandarla).

## Perché non la scelta più semplice possibile (solo frontend + localStorage)

Era l'opzione più rapida in assoluto, ma **rende impossibile l'obiettivo di
redditività dichiarato** (Data Flywheel, SCOPING.md §4): dati chiusi nel
browser di un solo dispositivo non sono un asset, non sono osservabili
dall'Officina né riusabili quando arriverà l'autenticazione multi-utente.
Per il mandato dell'Architetto (MANDATI.md §4) un'architettura che preclude
il flywheel dichiarato non è approvabile, anche sotto vincolo di budget
stretto — quindi si sceglie comunque un vero backend con dati persistenti
lato server, ma nella sua forma più minimale possibile per restare dentro
budget.

## Perché non un framework web (Flask/FastAPI/Node+Express)

Ogni dipendenza esterna è un'installazione, una superficie di errore e un
consumo di iterazioni-agente in più per un budget di due sessioni. Lo
stdlib Python basta per 3 endpoint JSON su un CRUD a singolo utente.
Rivalutare **obbligatoriamente** non appena si introduce l'autenticazione
(prossima fase, fuori scope oggi): a quel punto la superficie cresce e la
scelta va riaperta, non ereditata per inerzia.

## Schema dati — abilitare il Data Flywheel senza costruirlo ora

Tabella unica `risorse` con campi minimi per il CRUD di oggi, ma che non
precludono l'aggregazione futura tra utenti (quando arriverà
l'autenticazione): `id`, `titolo`, `url`, `tipo` (pratica/strumento/
esperimento), `note`, `stato` (`da_provare` / `letta_provata`),
`creato_il`, `aggiornato_il`. Nessun campo "utente" oggi (single-user), ma
la tabella è progettata per accettare una colonna `utente_id` in futuro
senza migrazione distruttiva.

## Data Flywheel — stato in questo prototipo

Il meccanismo non è costruito ora (nessuna pipeline, nessuna aggregazione):
solo lo schema dati non lo preclude. Il flywheel vero e proprio richiede
utenti multipli e resta fuori scope finché non c'è l'autenticazione
(Delibera locale richiesta, SCOPING.md §7).

## Alternative scartate

- **Node.js + Express + SQLite**: equivalente in complessità, ma richiede
  `npm install` (dipendenze esterne, tempo/rischio non necessario dato lo
  stdlib Python già sufficiente).
- **Database gestito esterno (Supabase/Postgres hosted)**: introduce un
  account/servizio terzo da configurare — costo di setup non giustificato
  per un prototipo single-user con budget di due sessioni.
