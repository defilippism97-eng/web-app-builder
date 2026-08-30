---
id: 70-radar-ia-0001
titolo: Stato commessa — RADAR IA
mandato: referente-commessa
commessa: radar-ia
etichetta: N/A
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

# Stato della commessa — RADAR IA

Ultimo aggiornamento: 2026-08-30 · Sprint: 001

## Fase corrente

Scoping | **Prototipo** (consegnato, in attesa di uso e Segnale) | Sviluppo | Rilascio | Manutenzione

Il committente ha risposto alle domande bloccanti (budget, redditività,
autenticazione rimandata, criterio di successo confermato — vedi SCOPING.md
§0 aggiornato il 2026-08-30). Il Prototipo Minimo Verificabile è stato
costruito e testato: catalogo risorse CRUD in `repo-app/` (Python stdlib,
SQLite, nessuna dipendenza esterna — vedi `tecnico/ARCHITETTURA.md`).
Ora la palla passa al committente: usarlo per 2-3 settimane è la condizione
del Segnale dichiarato in `scoping/IPOTESI.md`.

## Cosa abbiamo promesso / consegnato / manca

Risposta in un minuto, aggiornata a ogni Sprint (Definition of Done del
Referente di Commessa). Rinvio a `SCOPING.md §7` per il dettaglio granulare.

| Voce dello scope firmato | Consegnata? | Nota |
|---|---|---|
| Aggiungere una risorsa al catalogo | **sì** | `repo-app/`, testato end-to-end |
| Visualizzare l'elenco delle risorse | **sì** | con filtro per stato |
| Segnare una risorsa come "letta/provata" | **sì** | toggle nei due sensi |
| Contenuto reale RADAR IA (non placeholder) | in attesa | l'app è pronta a riceverlo; il committente inserisce le prime risorse vere durante l'uso |

## Prossimo Punto di Decisione

Punto di Decisione #1 — dopo il Prototipo Minimo Verificabile (catalogo
risorse, consegnato): procedi allo sviluppo pieno / taglia / ferma.
Trigger: Segnale dichiarato in `scoping/IPOTESI.md` — 2 settimane
consecutive di uso spontaneo del committente. Nessuna data calendariale
fissata: il trigger è comportamentale, non temporale.

## Budget e tempo

Budget massimo dichiarato dal committente (2026-08-30): equivalente in
token di **due sessioni Claude Pro, Sonnet 5, livello di ragionamento
medio** (SCOPING.md §5). Nessuna scadenza calendariale.
Consumo a questo Sprint: apertura commessa, Scoping, Ipotesi di Valore,
decisione architetturale e build del Prototipo Minimo Verificabile
(`repo-app/`), tutto in una sessione — nessuna cifra token esatta
tracciata da questo processo (il committente monitora il proprio consumo
lato piattaforma Claude); il Referente segnala qui che l'ordine di
grandezza resta "poche ore-agente", coerente col budget dichiarato.

## Scostamento di scope cumulativo

**Aggiornamento Sprint corrente**: costruito = ancora invariato rispetto a
`SCOPING.md §7` (nessuna riga di codice nuova aggiunta a `repo-app/` a
questo Sprint). Ma è arrivata la **prima richiesta di estensione**, ed è
la voce che pesa di più tra tutte quelle elencate in §7 come fuori scope:
non un campo in più, ma l'intera rete/community multi-utente.

**Scostamento proposto #1 (non ancora deciso, non costruito):**
- **Data**: 2026-08-30, Sprint 001.
- **Richiesta**: il committente ha chiesto di espandere la visione a una
  community — condivisione di esperienze su IA/lavoro/vibe coding/
  esperimenti, condivisione di opinioni, possibilità di unirsi al progetto
  di qualcun altro, richieste di aiuto sul proprio progetto.
- **Confronto con lo scope firmato**: corrisponde punto per punto a
  `SCOPING.md §7`, blocco "Esplicitamente fuori scope in questa fase" —
  in particolare "l'intera rete/community aperta a regime... utenti
  multipli esterni, contributi di terzi, moderazione" e "autenticazione
  multi-utente, ruoli, permessi differenziati". Non è un incremento
  marginale sommabile alle piccole estensioni tipiche dello scope creep:
  è di fatto un salto diretto allo Sviluppo Pieno della visione a regime,
  che `scoping/IPOTESI.md` (Punto di Decisione #2) condiziona a un Segnale
  da 3-5 utenti terzi reali non ancora raccolto. Oggi il committente resta
  l'unico utente del prototipo, consegnato in questo stesso Sprint.
- **Copertura**: nessuna Delibera locale presente in
  `70_progetti/radar-ia/delibere/` (cartella vuota). **Veto del Referente
  di Commessa attivo** su questa richiesta finché non viene deliberata.
- **Trattamento**: preparato un Punto di Decisione formale per l'umano —
  `70_progetti/radar-ia/PUNTO_DECISIONE_001.md` — con opzioni (procedi come
  da scope / taglia lo scope con un'estensione limitata single-user /
  ferma e riparti con uno Scoping nuovo per la commessa community) e
  raccomandazione. Nessuna comunicazione è stata inviata al committente:
  è una bozza per l'umano.
- **Stato**: in attesa di decisione. Finché non c'è una decisione esplicita
  (via Delibera locale o conferma dell'umano su una delle opzioni), lo
  scostamento resta a **0 righe di codice costruite fuori scope**, ma il
  rischio è alto proprio perché la richiesta è già stata espressa dal
  committente: da monitorare ad ogni Sprint successivo perché non
  rientri "di fatto" per piccoli passi (un campo, poi un secondo utente di
  prova, poi un sistema di commenti) senza mai passare da una decisione
  esplicita — è esattamente il pattern che il mandato del Referente deve
  intercettare.

Questa sezione va confrontata ad ogni Sprint successivo con `SCOPING.md
§7`, sommando tutte le piccole estensioni "ragionevoli" via via proposte —
non solo l'ultima — per far emergere lo scostamento cumulativo.

**Perimetro di riferimento per il veto del Referente di Commessa (nessuna
Delibera presente ad oggi in `70_progetti/radar-ia/delibere/`, cartella
vuota):**
- Tutto ciò che va oltre il CRUD minimo del catalogo risorse (vedi
  SCOPING.md §7, "Esplicitamente fuori scope in questa fase") resta un
  **veto aperto** finché non viene coperto da una Delibera locale.
- In particolare: rete/community a regime, riproducibilità sperimentale,
  ricerca/filtri avanzati, multi-utente/ruoli, raccomandazioni o scoring,
  integrazioni IA lato prodotto, pubblicazione pubblica.

## Pareri di rilascio in essere

Nessuno. Nessuna Consegna verso il committente è ancora stata preparata o
inviata a questo Sprint.

## Debiti aperti

`DEBITO_TECNICO.md`: DT-0001 (scorciatoia di processo — Regista che
costruisce senza delegare) **estinto** dopo revisione di `architetto` e
`sviluppatore-backend`; DT-0002/0003/0004 (schema dati, validazione URL
server-side, connessione/test) **estinti** con codice corretto e 7/7 test
`unittest` verdi. `DEBITO_RISCHIO.md` ancora da popolare (nessun rischio di
compliance aperto oggi: nessun dato personale trattato, single-user).

## Domande aperte verso il committente (da SCOPING.md §0)

Elenco delle lacune che bloccano o rischiano la commessa, da girare
all'umano/committente prima o durante il prossimo Sprint — vedi dettaglio
completo in `SCOPING.md`:

1. Ragione sociale/settore del committente e profilo reale degli utenti
   finali; livello di alfabetizzazione digitale del pubblico target.
2. Perché *ora* è il momento giusto (rispetto a come gestiscono oggi le
   stesse informazioni).
3. Conferma esplicita che il CRUD base (aggiungi/visualizza/segna
   letta-provata) è il criterio di successo/fallimento del Prototipo Minimo
   Verificabile agli occhi del committente.
4. Competitor o prodotto simile di riferimento, se esiste.
5. Ipotesi di Valore falsificabile (da raccogliere per compilare
   `scoping/IPOTESI.md` — bloccante per aprire lo sviluppo, CLAUDE.md §4).
6. Obiettivo di redditività oltre la fattura (CLAUDE.md §3): Data Flywheel,
   superficie ricorrente, o nessuna delle due — va dichiarato esplicitamente
   anche per questo Prototipo Minimo Verificabile.
7. Proprietà e riuso dei dati generati dall'uso (es. stato "letta/provata").
8. Categorie di dati personali trattati e base giuridica (rilevante se si
   prevede un utente registrato).
9. Settore regolato / normative note.
10. Accessibilità (WCAG) richiesta o no, dato il pubblico "curiosi".
11. Licenza degli asset forniti (font "Inter" e altro materiale del
    Designer di Prodotto) da verificare con l'Archivista di Prodotto.
12. Budget massimo (ore/importo) e scadenza reale, e cosa succede in caso
    di sforamento.
13. Chi, lato committente, ha potere di approvare estensioni di scope —
    domanda resa più delicata dal fatto che il committente è anche
    l'unico utente reale in questa fase (D-001, DOMANDE_APERTE.md):
    rischio di scope creep auto-richiesto dallo stesso utente/committente.
14. Cadenza e forma degli aggiornamenti attesi (demo/report/call).
15. Cosa succede a dati e codice in caso di interruzione anticipata del
    rapporto.
</content>
