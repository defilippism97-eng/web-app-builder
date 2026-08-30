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

A questo Sprint (001) non c'è ancora scostamento: lo scope firmato di
riferimento è quello appena fissato in `SCOPING.md §7` (solo catalogo
risorse). Questa sezione va confrontata ad ogni Sprint successivo con
`SCOPING.md §7`, sommando tutte le piccole estensioni "ragionevoli" via via
proposte — non solo l'ultima — per far emergere lo scostamento cumulativo.

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

Rinvio a `DEBITO_TECNICO.md` e `DEBITO_RISCHIO.md` (entrambi da verificare/
popolare quando inizia lo sviluppo). Nessun debito registrato a questo
Sprint poiché non è ancora stato scritto codice.

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
