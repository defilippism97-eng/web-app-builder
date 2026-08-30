---
id: 70-radar-ia-tecnico-0001
titolo: Architettura — RADAR IA (Prototipo Catalogo Risorse)
mandato: architetto
commessa: radar-ia
etichetta: DESIGN
parere_rilascio: non richiesto
stato: approvato con correzioni
data: 2026-08-30
---

## Nota di revisione (estinzione DT-0001)

Questo documento era stato scritto dal Regista in prima persona, fuori
mandato (`DEBITO_TECNICO.md` DT-0001, `00_delibere/DEL-0003-regista-non-costruisce.md`).
Questa sezione e le successive segnate "Revisione architetto" sono la
revisione che sarebbe dovuta avvenire prima della build, fatta a
posteriori sul codice già scritto in `repo-app/`. Le decisioni originarie
sono **confermate nella sostanza** (stack, assenza di autenticazione,
assenza di framework) ma **corrette nello schema dati**, che non è pronto
al Data Flywheel nel modo in cui il testo originale sosteneva. Il codice
in `repo-app/` non è stato toccato: la revisione dello sviluppatore segue
questo documento, non lo anticipa.

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

**Revisione architetto — confermata, con una ragione aggiuntiva più
solida di quella scritta originariamente.** Il testo originale motivava la
scelta solo con "meno iterazioni-agente per il budget stretto". Motivo
vero ma debole da solo: uno stdlib hand-rolled (routing manuale, parsing
JSON manuale, gestione manuale del path traversal sui file statici) è, riga
per riga, più codice scritto da zero — e quindi più superficie di bug — di
quanto lo sarebbero tre route Flask. Se il criterio fosse solo "minimizzare
righe scritte dall'agente", un micro-framework avrebbe vinto.

La ragione che regge davvero la scelta è un'altra, ed è nello Scoping
stesso (§5): *"stack che il committente stesso non dovrà poi gestire
manualmente"*. Il committente esegue questo prototipo in locale, da solo.
`pip install flask` è un passo in più che può fallire per motivi non legati
al prodotto (versione di Python, ambiente virtuale, permessi) e che il
committente — non tecnico per quanto dichiarato nello Scoping — dovrebbe
diagnosticare da solo. `python3 server.py` senza installazioni è un
vincolo operativo reale, non un'estetica di semplicità. Confermo la
decisione su questa base, non su quella (più debole) del budget da sola.

Rivalutare **obbligatoriamente** non appena si introduce l'autenticazione
(prossima fase, fuori scope oggi): a quel punto la superficie cresce e la
scelta va riaperta, non ereditata per inerzia. Vedi anche "Nota di impatto
— visione community" più sotto: se lo scope si allarga alla community, la
domanda non è più "framework sì/no" ma "questo intero approccio mono-processo
regge", ed è una domanda diversa e più grande.

## Schema dati — abilitare il Data Flywheel senza costruirlo ora

**Revisione architetto — correzione, non conferma.** Il testo originale
prevedeva una tabella unica `risorse` (`id`, `titolo`, `url`, `tipo`,
`note`, `stato`, `creato_il`, `aggiornato_il`) sostenendo che bastasse
aggiungere una colonna `utente_id` in futuro "senza migrazione
distruttiva". Questa affermazione non regge a un esame più attento e va
corretta ora, quando costa poco, non quando ci saranno dati reali
accumulati.

Il problema: la tabella attuale conflate due concetti che nel Data
Flywheel dichiarato in SCOPING.md §4 sono distinti — **la risorsa in sé**
(un'entità condivisibile: uno stesso strumento o articolo può essere
segnalato da più persone) e **la relazione di un singolo utente con quella
risorsa** (il suo stato "letta/provata", le sue note personali). Aggiungere
oggi una colonna `utente_id` alla tabella così com'è non abiliterebbe
l'aggregazione: partizionerebbe soltanto i dati per utente. Se domani due
persone diverse aggiungono lo stesso URL, si ottengono due righe scollegate
— non un segnale aggregato ("N persone hanno trovato utile questa
risorsa"), che è esattamente il tipo di dato che rende un Data Flywheel un
asset e non solo un database. Per correggere questo dopo che il
committente ha già usato il prototipo per settimane servirebbe uno script
di migrazione che deduplica URL simili, decide quale titolo/nota "vince"
tra copie divergenti e ricostruisce le relazioni — un lavoro con rischio
reale di alterare o perdere dati del committente, cioè esattamente la
"migrazione distruttiva" che il documento originale sosteneva di aver
evitato.

**Correzione, a costo marginale oggi** (nessun dato reale ancora
accumulato, `schema.sql` ha undici righe):

```sql
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
```

Per il perimetro di oggi (single-user) questo si comporta in modo
osservabile identico alla tabella unica — una risorsa, un'interazione
implicita — e non aggiunge complessità percepibile nel CRUD (lo
sviluppatore fa due INSERT invece di uno, dietro un unico endpoint). La
differenza è che l'identità della risorsa e la relazione dell'utente con
essa sono già separate quando servirà aggregarle. `url_canonico` resta
`NULL`/non applicato oggi: si dichiara qui che la normalizzazione URL è un
problema noto e rimandato (Debito Tecnico da registrare, non un requisito
per il prototipo single-user), non un dettaglio dimenticato.

Questa è la correzione minima richiesta prima che lo sviluppatore tocchi
di nuovo `repo-app/`; non è un via libera a costruire pipeline di
aggregazione o dashboard, che restano fuori scope.

## Data Flywheel — stato in questo prototipo

Il meccanismo non è costruito ora (nessuna pipeline, nessuna aggregazione):
con la correzione sopra, lo schema dati distingue l'identità della risorsa
dalla relazione utente-risorsa, condizione necessaria (non sufficiente) al
flywheel. Il flywheel vero e proprio richiede utenti multipli, un criterio
di normalizzazione URL, e resta fuori scope finché non c'è l'autenticazione
(Delibera locale richiesta, SCOPING.md §7).

## Revisione del codice — segnalazioni per lo sviluppatore

Non rientra nel mandato dell'Architetto correggere il codice (`repo-app/`
non è stato toccato), ma la revisione ha trovato problemi che uno
sviluppatore avrebbe dovuto sollevare prima della consegna. Vanno
verificati e risolti da `sviluppatore-backend`/`sviluppatore-frontend`
prima del Punto di Decisione #2, non solo annotati:

1. **Validazione dell'URL solo lato client (`app.js`, `urlSicuro`).**
   `server.py` (`_crea_risorsa`) accetta qualunque stringa come `url` (solo
   limite di lunghezza), senza validarne lo schema. Oggi il rischio è
   contenuto: il frontend attuale usa `textContent` per titolo/note (non
   `innerHTML`, quindi niente XSS diretto) e filtra `http/https` prima di
   creare un link cliccabile. Ma la validazione è una responsabilità del
   server, non solo del client che l'API oggi si trova a servire: un client
   diverso (un'app mobile futura, una chiamata API diretta, un frontend
   community riscritto) non erediterebbe automaticamente il controllo fatto
   in `app.js`. Da correggere: validare lo schema (`http`/`https`) anche
   server-side, indipendentemente da chi chiama l'API — checklist OWASP di
   base, CLAUDE.md §6.
2. **`connetti_db()` riesegue `executescript(schema.sql)` a ogni singola
   richiesta**, aprendo una nuova connessione per ogni GET/POST/PATCH.
   Idempotente (non rompe nulla) ma è uno spreco che a volumi anche modesti
   (decine di richieste concorrenti) genera più lock SQLite del necessario.
   Non blocca il prototipo single-user, ma è un debito tecnico a bassa
   priorità da registrare in `DEBITO_TECNICO.md`, non da ignorare.
3. **Nessun test automatico.** Il mandato dello Sviluppatore Backend
   (`MANDATI.md` §5) richiede test sul percorso critico come condizione di
   Definition of Done; non ce ne sono. Per un CRUD a 3 endpoint il costo di
   scriverli è basso; l'assenza pesa di più quando (e se) la superficie
   cresce, quindi va colmata ora che è a buon mercato, non rimandata.

Nessuno di questi tre punti è, da solo, motivo per bloccare l'uso locale
del prototipo dal committente (nessun dato personale trattato, nessuna
esposizione pubblica dichiarata). Sono condizioni da chiudere prima che il
codice venga esteso, non prima che il committente lo usi da solo oggi.

## Nota di impatto — visione community (informativa, non un'autorizzazione)

Il committente ha descritto, fuori dal perimetro autorizzato in
SCOPING.md §7, una visione molto più ampia: profili utente, condivisione di
esperienze e opinioni, adesione al progetto di altri, richieste d'aiuto.
Questa sezione risponde solo alla domanda tecnica "lo stack di oggi regge
quella direzione", per uso di Referente e Stratega nel valutare la
richiesta di estensione — **non è un via libera a costruire nulla di
quanto segue**, che resta sotto veto del Referente di Commessa finché non
c'è una Delibera locale (SCOPING.md §7, MANDATI.md §2).

**Cosa regge senza riscrittura, se la correzione di schema sopra viene
applicata ora:**
- SQLite in un solo file regge volumi di lettura/scrittura sorprendentemente
  alti per una community di piccole dimensioni (centinaia di utenti attivi,
  non migliaia concorrenti) se configurato in modalità WAL; non è, da solo,
  il collo di bottiglia.
- La separazione risorsa/interazione proposta sopra è esattamente la forma
  che serve anche per profili, contributi di terzi e "adesione a un
  progetto altrui": si generalizza a `entità condivisa` + `relazione
  utente-entità`, non va ripensata da zero se fatta ora.

**Cosa NON regge e richiederebbe una riscrittura sostanziale, non
un'estensione incrementale:**
- **Autenticazione e gestione sessioni**: oggi non esiste nulla (scelta
  corretta per il perimetro attuale). Costruirla a mano su `http.server`
  stdlib (hashing password, sessioni, eventuale OAuth, protezione CSRF) è
  un lavoro paragonabile, come rischio e ore, a quello che richiederebbe
  con un framework — su questo punto specifico non si perde nulla a
  rimandarlo, come già deciso.
- **Contenuti generati da terzi** (opinioni, richieste d'aiuto, commenti,
  adesioni a progetti) cambia la natura del prodotto da "catalogo curato da
  una persona" a "piattaforma con moderazione". Serve: schema relazionale
  ben oltre le due tabelle proposte sopra (utenti, post, commenti, progetti,
  membership, segnalazioni di abuso), paginazione, rate limiting,
  protezione CSRF, difese XSS più rigorose di "usare `textContent`" (oggi
  sufficiente perché il solo contenuto è quello di un singolo utente
  fidato — il committente stesso). Il routing manuale scritto a mano in
  `server.py` regge 3 endpoint; non regge in modo sostenibile una dozzina
  di risorse REST con permessi differenziati — a quel punto il costo
  "installare un framework" smette di essere il rischio dominante e lo
  diventa "mantenere a mano ciò che un framework darebbe gratis".
- **Processo singolo (`ThreadingHTTPServer`) senza supervisione**: accettabile
  per un prototipo locale, non per un servizio pubblico con aspettative di
  uptime — manca gestione di restart, deploy, logging strutturato,
  osservabilità. Materia di `devops-sicurezza`, non solo dell'Architetto,
  ma la scelta attuale non è stata pensata per quel contesto e non deve
  essere presunta adeguata solo perché "ha sempre funzionato finora".

**Costo di migrazione, in sintesi per chi deve decidere:**
- Se la correzione allo schema dati (sezione sopra) viene applicata **ora**,
  il costo di aggiungere in futuro autenticazione e nuove entità è
  incrementale (si aggiungono tabelle e colonne, non si ristrutturano
  quelle esistenti).
- Se si scopre solo dopo — cioè si autorizza la visione community e la si
  costruisce sopra lo schema attuale non corretto — il costo include: una
  migrazione dati con rischio di perdita/alterazione (vedi sopra), la
  riscrittura del layer HTTP da stdlib a un framework con routing/middleware
  reali, l'introduzione ex novo di autenticazione, moderazione e difese di
  sicurezza che oggi semplicemente non servono. Questo non è un
  aggiustamento incrementale: è, nella sostanza, un secondo progetto che
  riusa lo schema concettuale ma non il codice. Va trattato come tale nella
  stima che lo Stratega/Referente presenteranno al committente, non come
  "estendiamo quello che c'è".

## Alternative scartate

- **Node.js + Express + SQLite**: equivalente in complessità, ma richiede
  `npm install` (dipendenze esterne, tempo/rischio non necessario dato lo
  stdlib Python già sufficiente).
- **Database gestito esterno (Supabase/Postgres hosted)**: introduce un
  account/servizio terzo da configurare — costo di setup non giustificato
  per un prototipo single-user con budget di due sessioni.
