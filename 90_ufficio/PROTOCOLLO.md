# Protocollo dell'Officina

## 1. Due unità di lavoro, non una

Motore Talento aveva un solo ritmo, il Ciclo. Qui ce ne sono due, perché il
lavoro non è più un unico flusso continuo ma **più commesse indipendenti** che
condividono la stessa Officina.

- **Sprint** — unità di lavoro del Regista sull'insieme delle commesse attive.
  Sceglie quali commesse avanzano in questo turno e con quali task.
- **Fase di Commessa** — Scoping → Prototipo → Punto di Decisione → Sviluppo →
  Rilascio → Manutenzione. Ogni commessa vive il proprio percorso in
  `70_progetti/<slug>/`, con il proprio `STATO_COMMESSA.md`.

Un Ciclo non esiste più come unità autonoma: **uno Sprint contiene una o più
Fasi di Commessa**, ciascuna gestita dal mandato competente.

## 2. Lo Sprint, comando `/sprint`

1. **Rileggi lo stato.** `CLAUDE.md`, `STATO.md`, `DOMANDE_APERTE.md`,
   `GLOSSARIO.md`, per ogni commessa attiva il suo `STATO_COMMESSA.md`. Sempre
   dai file, mai dalla memoria di sessione.
2. **Per ogni commessa attiva**, verifica se è al o oltre il prossimo Punto di
   Decisione dichiarato in `SCOPING.md`. Se sì, **non si procede
   automaticamente**: si prepara il Punto di Decisione per l'umano (§5) e si
   sospende il lavoro tecnico su quella commessa finché non arriva la risposta.
3. **Scegli i task** dalle commesse non in attesa di decisione, massimo tre per
   commessa, massimo nove totali per Sprint.
4. **Delega in parallelo** ai subagenti dei mandati competenti.
5. **Gate automatico**: `python strumenti/controllo_rigore.py`. Gerarchia dei
   quattro presidi in ordine di priorità (§1 di `CLAUDE.md`): compliance →
   budget/scope → qualità tecnica → validazione della domanda. Il gate segnala
   sempre la violazione di rango più alto per prima. Sprint non chiuso con gate
   rosso.
6. **Aggiorna stato**: `STATO.md`, `STATO_COMMESSA.md` di ogni commessa
   toccata, `DEBITO_TECNICO.md` e `DEBITO_RISCHIO.md` dove pertinente.
7. **Commit**: uno per Sprint, `sprint NNN: <cosa è cambiato per quali
   commesse>`.
8. **Continua o fermati.** Se ogni commessa attiva è in attesa di decisione
   umana, il Regista si ferma: «FERMO: tutte le commesse attive attendono un
   Punto di Decisione».

**Budget per Sprint**: 3 artefatti nuovi o 5 revisioni **per commessa**, non
cumulativo tra commesse. Il motivo è diverso da Motore Talento: qui il rischio
non è solo "produrre più di quanto si possa validare", è "far correre una
commessa più veloce di quanto il committente riesca a seguirla e a pagarla".

## 3. Punto di Decisione — l'equivalente del gate DEL-0001

Ogni commessa dichiara nello Scoping almeno tre Punti di Decisione: dopo il
Prototipo Minimo Verificabile, prima dello sviluppo pieno, prima del primo
rilascio pubblico. **Nessun mandato tecnico attraversa un Punto di Decisione
da solo.** È l'equivalente, in questo dominio, del tetto sulle etichette di
DEL-0001 in Motore Talento: un cancello che nessun agente può alzare per
sé stesso, indipendentemente da quanto il lavoro proceda bene.

## 4. Gerarchia dei veti

In ordine, dal più alto: **Custode Normativo** (compliance/etica) →
**Referente di Commessa** (scope/budget) → **DevOps & Sicurezza** (rilascio
in produzione) → **Archivista di Prodotto** (fonti/licenze) →
**Stratega di Prodotto** (assenza di Ipotesi di Valore). Un veto di rango
superiore sospende automaticamente l'esecuzione di un artefatto anche se un
mandato di rango inferiore lo aveva già approvato. Solo il Consiglio, con
conferma dell'umano, può riaprire un veto del Custode.

## 5. Messaggi e Punti di Decisione verso l'umano

Stesso formato di Motore Talento per i messaggi interni tra mandati
(`90_ufficio/messaggi/`). Per un Punto di Decisione, il Referente di Commessa
prepara in `70_progetti/<slug>/PUNTO_DECISIONE_NNN.md`:

```
### Punto di Decisione — <commessa>, <fase>
COSA ABBIAMO IMPARATO: <segnali raccolti, con fonte>
COSA COSTEREBBE PROSEGUIRE: <ore/budget stimati per la fase successiva>
OPZIONI: procedi come da scope | taglia lo scope a <cosa> | ferma la commessa
RACCOMANDAZIONE: <quale e perché>
RISCHI SE NON SI DECIDE ORA: <scadenze, costi che crescono nel frattempo>
```

Stessa regola di Motore Talento: una domanda senza opzioni e raccomandazione
non è un Punto di Decisione pronto, è lavoro incompleto.

## 6. Quando si convoca il Consiglio, comando `/consiglio`

Si convoca se: la decisione supera un mese di lavoro o una parte significativa
del budget della commessa; riguarda un pivot o l'interruzione; un veto del
Custode è contestato; la decisione riguarda una scelta strutturale che vale per
tutte le commesse future (es. lo stack di default dell'Officina), non solo per
una.

I cinque seggi restano quelli di Motore Talento, con un adattamento del quarto:

1. Bastian Contrario — cosa va storto, costi nascosti.
2. Pensatore da Principi Primi — cosa è vero davvero di questa commessa/scelta.
3. Espansionista — la versione più grande dell'opportunità.
4. **L'Utente Reale** — non generico: la persona che userà davvero la webapp,
   con il suo livello di alfabetizzazione digitale dichiarato nello Scoping.
   Fa le domande ingenue e giudica se l'interfaccia è davvero semplice da
   capire. Il suo giudizio pesa quanto un'obiezione tecnica.
5. Esecutore — cosa si fa lunedì mattina, con quali risorse.

Output: una Delibera in `00_delibere/` se la decisione vale per l'Officina, o
in `70_progetti/<slug>/delibere/` se vale solo per quella commessa.

## 7. Manutenzione, comando `/fine-sessione`

Ogni cinque Sprint: compattare `STATO.md` e gli `STATO_COMMESSA.md`; verificare
che nessun claim di mercato sia salito di etichetta senza fonte; ricontare le
LACUNA aperte; per ogni commessa, verificare che `DEBITO_RISCHIO.md` non abbia
voci scadute; aggiornare `60_conoscenza/` con pattern e lezioni emerse dalle
commesse dello sprint, in vista del riuso.

## 8. Conoscenza e messa online

`60_conoscenza/` non è un archivio, è pensato per essere riusato rapidamente:

- `60_conoscenza/pattern/` — soluzioni tecniche riutilizzabili tra commesse
  (autenticazione, pagamenti, onboarding), ciascuna con lo stack in cui è stata
  provata e il tempo di integrazione osservato;
- `60_conoscenza/checklist-rilascio/` — la checklist di sicurezza e di
  compliance in forma eseguibile, aggiornata a ogni commessa che scopre un caso
  nuovo;
- `60_conoscenza/errori/` — cosa non ha funzionato e perché, con la commessa di
  origine anonimizzata se il committente lo richiede.

Ogni commessa che si chiude lascia almeno una voce in una di queste tre
cartelle: è il modo in cui l'Officina diventa più veloce nella commessa
successiva invece di ripartire sempre da zero.

## 9. Git e Drive

Stesso principio di Motore Talento: **git è la fonte di verità, Drive è
specchio in sola lettura**, sincronizzazione a senso unico a fine sessione.
Mappatura in `strumenti/sync_drive.md`, pensata per far arrivare su Drive
anche i link di staging/produzione delle webapp consegnate, non solo i
documenti.
