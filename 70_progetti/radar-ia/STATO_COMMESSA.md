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

**Budget per il mockup community — deciso dal committente (2026-08-30):**
tutto il budget di token necessario a completare questa fase, ma **solo
entro le risorse dell'abbonamento Claude già attivo, nessun credito
aggiuntivo**. Non è un tetto in ore/sessioni fisse come il budget
originario del catalogo (due sessioni Claude Pro): è un vincolo di fonte,
non di quantità — il lavoro continua finché serve, ma si ferma ogni volta
che la sessione esaurisce il limite d'uso del piano, e riparte da sola al
prossimo controllo programmato (vedi sotto, DEL-0004).

**Meccanismo di ripresa automatica** (DEL-0004, applicata qui per la prima
volta): è stata programmata una Routine che controlla periodicamente se la
sessione è di nuovo utilizzabile e, in tal caso, riprende la delega ai
mandati competenti senza bisogno di un messaggio dell'umano. Limite onesto:
il Regista non conosce l'orario esatto di reset del limite del committente,
quindi la ripresa avviene al prossimo controllo programmato dopo lo
sblocco, non nell'istante esatto dello sblocco. Cadenza scelta: ogni 3 ore
— una stima, non un dato certo sul piano del committente.

**Stima di tempo/sessioni per il mockup, con le riserve dovute**: il
Regista non ha visibilità sul consumo residuo reale del committente né
sui token esatti che designer e sviluppatore consumeranno (dipende da
quante schermate, quante iterazioni di revisione). Etichetta
**[DA VERIFICARE]**, non [VALIDATO]: a titolo di solo ordine di grandezza,
il mockup (poche schermate statiche, solo frontend, nessuna integrazione
backend) è un lavoro più piccolo di quanto già consegnato per il catalogo
(scoping + architettura + build + revisione + correzioni, distribuito su
più deleghe in questa stessa sessione) — probabile che rientri in una
sessione se il perimetro resta quello della Delibera, con margine di 2-3
sessioni se emergono revisioni. Non è una promessa vincolante.

## Scostamento di scope cumulativo

**Aggiornamento Sprint corrente**: il committente ha risposto a
`PUNTO_DECISIONE_001.md` con una richiesta puntuale (non tra le opzioni
testuali offerte, ma variante mirata dell'Opzione 2): un mockup/anteprima
visiva della community, solo frontend, senza backend reale. Il Referente
ha tradotto la richiesta in un perimetro scrivibile e l'ha coperta con
`delibere/DEL-LOCALE-001-mockup-community.md` (2026-08-30). Questo
scostamento **cambia stato**: da "richiesta in attesa, veto aperto" a
**"deliberato e autorizzato nel perimetro esatto della Delibera"** — non è
più uno scostamento non deliberato come lo era fino a questo Sprint.

**Scostamento #1 — ORA DELIBERATO E AUTORIZZATO (perimetro preciso):**
- **Cosa è autorizzato**: mockup/anteprima visiva e interattiva della
  community (schermate navigabili, condivisione di esperienze/opinioni,
  "unisciti a un progetto altrui", "chiedi aiuto"), con dati d'esempio
  statici o salvati solo localmente sul dispositivo del committente.
  Nessun account reale, nessuna autenticazione reale.
- **Cosa resta vietato, invariato**: backend community reale,
  autenticazione reale, dati di utenti terzi reali, persistenza
  multi-utente condivisa, moderazione. Tutti questi restano vincolati al
  Punto di Decisione #2 di `scoping/IPOTESI.md` (Segnale da 3-5 utenti
  terzi reali), non sciolti da questa Delibera locale — vedi
  `DEL-LOCALE-001-mockup-community.md` per il dettaglio.
- **Copertura**: `delibere/DEL-LOCALE-001-mockup-community.md`, in vigore
  dal 2026-08-30. Il veto del Referente su questa specifica richiesta è
  quindi **sciolto**, ma resta attivo, invariato, su tutto ciò che la
  Delibera esplicitamente non autorizza (vedi sopra).
- **Budget**: non ancora coperto da una cifra confermata dal committente —
  vedi `[[LACUNA]]` in §Budget e tempo sopra. Lo sviluppo del mockup non
  dovrebbe partire fino a conferma, per lo stesso principio che ha
  bloccato la community piena: uno scope autorizzato senza budget
  dichiarato è comunque un rischio economico, anche se più piccolo.
- **Nota per lo scostamento cumulativo dei prossimi Sprint**: questa
  Delibera copre *solo* il mockup così definito. Qualunque nuova richiesta
  — anche piccola, anche "solo per la demo" — che introduca un elemento
  tra quelli vietati (backend, auth, dati di terzi, persistenza condivisa,
  moderazione) è un **nuovo** scostamento, non compreso qui, e torna sotto
  veto del Referente finché non ha una propria Delibera o una decisione
  esplicita dell'umano. Il pattern da sorvegliare resta lo stesso di
  sempre: piccole estensioni "solo per far vedere meglio il mockup" che,
  sommate, ricostruiscono il backend che questa Delibera esclude
  esplicitamente.

**Storico — scostamento proposto #1 originario (superato, ora deliberato):**
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
- **Stato originario**: era "in attesa di decisione". **Superato da questo
  Sprint**: il committente ha risposto, ed è stata scritta la Delibera
  `DEL-LOCALE-001-mockup-community.md` che copre il perimetro mockup —
  vedi voce "Scostamento #1 — ORA DELIBERATO E AUTORIZZATO" sopra per lo
  stato aggiornato.

Questa sezione va confrontata ad ogni Sprint successivo con `SCOPING.md
§7`, sommando tutte le piccole estensioni "ragionevoli" via via proposte —
non solo l'ultima — per far emergere lo scostamento cumulativo.

**Perimetro di riferimento per il veto del Referente di Commessa
(aggiornato a questo Sprint con `DEL-LOCALE-001-mockup-community.md` in
vigore):**
- Il mockup/anteprima visiva della community (solo frontend, dati
  locali/statici) è **autorizzato** nel perimetro esatto della Delibera:
  non è più sotto veto.
- Tutto il resto che va oltre il CRUD minimo del catalogo risorse e oltre
  il mockup autorizzato (vedi `SCOPING.md §7`, "Esplicitamente fuori scope
  in questa fase") resta un **veto aperto** finché non viene coperto da
  una propria Delibera locale.
- In particolare restano sotto veto: backend community reale,
  autenticazione reale, dati di utenti terzi reali, persistenza
  multi-utente condivisa, moderazione, riproducibilità sperimentale,
  ricerca/filtri avanzati, ruoli/permessi, raccomandazioni o scoring,
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
