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

**Scoping** (in chiusura) | Prototipo | Sviluppo | Rilascio | Manutenzione

Nota: `scoping/IPOTESI.md` è stata compilata dallo Stratega di Prodotto
(Ipotesi di Valore falsificabile, etichetta DESIGN, Segnale dichiarato
debole/auto-riferito in questa fase — vedi il file per i dettagli). Il
blocco di CLAUDE.md §4 è sciolto: si può passare a Prototipo. Restano però
aperte lacune non bloccanti per CLAUDE.md §4 ma rilevanti per budget/scope
(vedi sotto) prima di considerare lo Scoping davvero chiuso.

## Cosa abbiamo promesso / consegnato / manca

Risposta in un minuto, aggiornata a ogni Sprint (Definition of Done del
Referente di Commessa). Rinvio a `SCOPING.md §7` per il dettaglio granulare.

| Voce dello scope firmato | Consegnata? | Nota |
|---|---|---|
| Aggiungere una risorsa al catalogo | no | non ancora avviato lo sviluppo |
| Visualizzare l'elenco delle risorse | no | non ancora avviato lo sviluppo |
| Segnare una risorsa come "letta/provata" | no | non ancora avviato lo sviluppo |
| Contenuto reale RADAR IA (non placeholder) | no | in attesa di materiale dal committente/Designer di Prodotto |

## Prossimo Punto di Decisione

Punto di Decisione #1 — dopo il Prototipo Minimo Verificabile (catalogo
risorse): procedi / taglia / ferma. Data/trigger non fissati:
`[[LACUNA: budget e scadenza non ancora dichiarati dal committente,
SCOPING.md §5]]`. Fino a chiarimento su queste lacune, non si procede a
sviluppo pieno oltre il CRUD minimo già delimitato.

## Budget e tempo

`[[LACUNA: nessun budget/ore massime né scadenza dichiarati dal
committente — SCOPING.md §0 domanda 16]]`. Nessun consumo da registrare a
questo Sprint (fase Scoping, nessun task tecnico avviato).

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
