---
id: 10-0001
titolo: Ipotesi di Valore — RADAR IA (Prototipo Catalogo Risorse)
mandato: stratega-prodotto
commessa: radar-ia
etichetta: DESIGN
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

## Perimetro di questa Ipotesi

Riguarda **solo** il Prototipo Minimo Verificabile già deciso dal
committente: catalogo di risorse RADAR IA con aggiungi / visualizza / segna
come "letta o provata". Non riguarda la rete/community a regime (rete
aperta di documentazione, apprendimento e riproducibilità) — quella visione
resta fuori scope finché questo prototipo non ha un Segnale, anche debole,
che la giustifichi.

## Ipotesi centrale

Se costruiamo un catalogo curato di risorse IA (pratiche, strumenti,
esperimenti) con la sola funzione di aggiungere, sfogliare e marcare una
risorsa come "letta/provata", **il committente stesso**, nel ruolo di primo
utente reale, lo consulterà e alimenterà con regolarità sufficiente da
preferirlo al proprio metodo attuale (bookmark, note sparse, memoria) entro
le prime 2-3 settimane di uso — senza che nessuno glielo debba ricordare.

## Segnale che la confermerebbe

- Il committente aggiunge risorse nuove al catalogo **senza sollecitazione**
  dell'Officina, con una cadenza regolare (proposta: almeno 1 risorsa/
  settimana per 3 settimane consecutive).
- Il committente marca risorse come "letta/provata" nel tempo, non solo in
  un'unica sessione di test subito dopo la consegna del prototipo (segnale
  di uso reale vs. collaudo una tantum).
- Il committente, interrogato direttamente, dichiara di aver **smesso o
  ridotto** l'uso del proprio metodo precedente (bookmark/Notion/altro) a
  favore del catalogo, per questo scopo specifico.

## Segnale che la smentirebbe

- Il catalogo resta popolato solo dalle risorse inserite durante il collaudo
  iniziale con l'Officina; zero aggiunte spontanee nelle settimane
  successive.
- Il committente continua a usare il proprio metodo precedente in parallelo
  o al posto del catalogo, anche dopo la consegna.
- Il committente usa il prodotto solo quando esplicitamente richiesto da
  noi (per una demo, un feedback), non di iniziativa propria.

## Cosa la smentirebbe (falsificazione)

**Questa Ipotesi è falsificata se, a 3 settimane dalla consegna del
prototipo, il committente non ha aggiunto o marcato nessuna risorsa di
propria iniziativa al di fuori delle sessioni concordate con l'Officina.**
In quel caso l'assunzione "un catalogo dedicato batte gli strumenti generici
che l'utente già usa" è falsa per questo utente, e non c'è base per
investire nello sviluppo pieno finché non si capisce perché (frizione
d'uso? valore percepito insufficiente? il problema non è abbastanza
sentito nemmeno dal committente?).

## Limite esplicito del Segnale in questa fase

Il committente è **al momento l'unico utente reale**: è al tempo stesso
sponsor economico e utente finale del prototipo. Questo rende il Segnale
sopra **debole e auto-riferito** per due motivi:

1. Il committente ha un incentivo (consapevole o no) a validare la propria
   idea, non solo a usarla per bisogno reale — bias che un utente terzo
   pagante o un ricercatore esterno non avrebbe nello stesso modo.
2. Un singolo utente, per quanto rappresentativo, non dice nulla sulla
   distribuzione del pubblico dichiarato (ricercatori, studenti,
   professionisti, curiosi) — un solo caso non regge una decisione di
   investimento oltre il prototipo.

**Condizioni per un Segnale più forte, richieste prima di procedere oltre
lo sviluppo pieno (Punto di Decisione #2):**

- Almeno 3-5 utenti terzi reali (non l'Officina, non il committente) che
  usano il prototipo senza supervisione diretta per un periodo comparabile
  (2-3 settimane), reclutati da almeno due dei profili dichiarati (es. uno
  studente e un professionista, non solo persone della rete del
  committente).
- Segnale misurato sugli stessi indicatori sopra (aggiunte spontanee,
  marcature nel tempo, non solo apertura una tantum), non un'intervista
  soft "ti piace?".
- `[[LACUNA: come recluteremo questi 3-5 utenti terzi e in quale finestra
  temporale non è ancora deciso — da chiarire col committente prima del
  Punto di Decisione #2, non a ridosso di esso]]`.

Fino a quel momento, ogni conferma del Segnale in questa fase va letta e
comunicata come "indicazione preliminare dal solo committente", non come
validazione di mercato.

## Concorrenza sostitutiva

Rinvio a `scoping/CONTESTO.md` per il dettaglio. In sintesi: bookmark del
browser, Notion/Obsidian personali, newsletter passive, community social
(Twitter/X, Reddit, Discord) e, per una parte del pubblico dichiarato,
semplicemente "non tracciare nulla". Questa concorrenza sostitutiva è più
pericolosa della concorrenza diretta (altre directory/hub IA) perché non
richiede all'utente di cambiare abitudine: è il vero avversario che il
Segnale sopra deve battere.

## Punti di Decisione previsti (SCOPING.md §6)

| # | Dopo cosa | Cosa si decide | Criterio / trigger legato al Segnale |
|---|---|---|---|
| 1 | Prototipo Minimo Verificabile (catalogo aggiungi/visualizza/segna) | procedi allo sviluppo pieno / taglia lo scope / ferma | Segnale confermato dal solo committente per almeno 2 settimane consecutive di uso spontaneo (vedi "Segnale che la confermerebbe"). Se falsificato (vedi sopra), non si procede senza prima capire la causa — si torna a un ciclo di scoping ridotto, non si taglia direttamente allo sviluppo pieno. |
| 2 | Prima dello sviluppo pieno | procedi / taglia lo scope / ferma | Richiede il Segnale più forte descritto sopra: almeno 3-5 utenti terzi reali con uso spontaneo misurato, non solo il committente. Senza questo, lo sviluppo pieno non è autorizzato — resta al più un'estensione limitata del prototipo con nuovi utenti di test. |
| 3 | Prima del rilascio pubblico | procedi / rinvia | Segnale del Punto #2 confermato su una finestra più ampia (proposta: 4-6 settimane) *e* nessun Debito di Rischio aperto oltre scadenza (privacy, licenze delle risorse catalogate — verificare con l'Archivista di Prodotto e il Custode Normativo prima, non durante il rilascio). |

## Etichetta e verifica

Etichetta: **DESIGN** — questa Ipotesi è un'assunzione dichiarata
dall'Officina sulla base del contesto fornito dal committente, non un dato
verificato. Passa a VALIDATO solo dopo che il Segnale è stato osservato e
registrato con evidenza tracciabile (log d'uso reale, non dichiarazioni a
voce non verificabili).
