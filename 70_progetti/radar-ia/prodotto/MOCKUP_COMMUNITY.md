---
id: prodotto-0001
titolo: Concept visivo — Mockup/anteprima Community RADAR IA
mandato: designer-prodotto
commessa: radar-ia
etichetta: DESIGN
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

## Perimetro e cosa NON è questo documento

Questo documento definisce il **concept delle schermate**, non l'implementazione
(compito di `sviluppatore-frontend`). È vincolato a
`delibere/DEL-LOCALE-001-mockup-community.md`: solo frontend, dati statici o
salvati in locale, nessun backend condiviso, nessuna autenticazione reale.
Non introduce nessuna funzionalità elencata in `SCOPING.md §7` come fuori
scope (backend community, moderazione, contributi di terzi reali). Ogni dato
"di altri utenti" mostrato è inventato dall'Officina, mai reale, per non
violare né la Delibera né la nota sul debito contratto (persone identificabili
reali vietate anche in un mockup).

## 0. Principio guida di design: scena, non funzione

Ogni schermata sotto deve essere **immediatamente riconoscibile come anteprima**
a chiunque la apra, non solo a chi ha letto questo documento. Due dispositivi
di design ricorrenti, presenti su ogni vista senza eccezioni (dettaglio in §3):

1. Un banner fisso "Anteprima — non ancora attivo" nella parte alta della vista.
2. Ogni azione che simulerebbe interazione sociale reale (commentare, mettere
   "mi piace", rispondere, unirsi, inviare un messaggio) è visivamente
   presente ma **non esegue l'azione**: al click mostra un messaggio "in
   arrivo", non una finta conferma di successo. Non si deve mai vedere un
   contatore che sale o un "grazie per aver commentato" — sarebbe una
   simulazione di community reale, esattamente il rischio di percezione che
   la Delibera segnala come il più grosso.

## 1. Schermate proposte

Quattro viste, minime e mirate — sufficienti a far intuire la direzione senza
costruire il prodotto:

### 1.1 Feed — bacheca di esperienze e opinioni

**Cosa mostra**: un elenco cronologico di post brevi, ciascuno con autore
d'esempio, testo, tag (es. "vibe coding", "esperimento", "opinione"),
placeholder di reazioni disattivate. Serve a comunicare "qui la community
condivide cosa sta facendo/pensando sull'IA", il nucleo della visione del
committente.

**Dati d'esempio statici** (5, scritti a mano, tono coerente con RADAR IA —
pratico, riflessivo, non da social generico). Nota di rigore: i numeri che
compaiono nei testi sotto (es. "20%") sono **contenuto di finzione** per un
post d'esempio in un mockup — non sono claim di mercato dell'Officina né
dati misurati, quindi non prendono un'etichetta [VALIDATO]/[DESIGN]/[DA
VERIFICARE] di CLAUDE.md §7, che si applica ai claim quantitativi reali:

1. *Autore: "Marta R." — tag: vibe coding* — "Ho provato a far scrivere a
   Claude l'intera struttura di un piccolo tool CLI partendo solo da una
   descrizione a voce trascritta. Ha funzionato per lo scaffolding, molto
   meno per la logica di edge case: lì ho dovuto riscrivere quasi tutto a
   mano. Vale la pena per il primo 20%, non oltre."
2. *Autore: "Luca D."  — tag: esperimento* — "Esperimento di riproducibilità:
   stesso prompt, stesso modello, tre run in giorni diversi su un task di
   estrazione dati da PDF. Output strutturalmente identico due volte su tre;
   la terza volta ha invertito due colonne di una tabella. Sto documentando
   il seed/temperatura usati per capire se è determinismo reale o casualità
   percepita."
3. *Autore: "Sara T." — tag: opinione* — "Continuo a pensare che il problema
   con 'l'IA scrive il codice al posto tuo' non sia la qualità del codice
   ma la perdita del modello mentale di chi lo revisiona. Se non hai scritto
   tu la logica, fai fatica a fare code review seria un mese dopo."
4. *Autore: "Fede B." — tag: pratica* — "Piccola pratica che uso da un mese:
   prima di ogni sessione di vibe coding scrivo tre righe di 'cosa NON deve
   fare' oltre a 'cosa deve fare'. Riduce parecchio le derive silenziose
   dell'agente su funzionalità non richieste."
5. *Autore: "Giorgio N." — tag: vibe coding* — "Chiedo aiuto: sto costruendo
   un prototipo con un agente IA che continua a reintrodurre una dipendenza
   che avevo scartato esplicitamente due prompt prima. Qualcuno ha un
   pattern per far 'ricordare' vincoli negativi lungo una sessione lunga?"

### 1.2 Dettaglio di un post/esperienza

**Cosa mostra**: apertura di un singolo post del feed (es. quello di Luca D.
sull'esperimento di riproducibilità) con testo completo, eventuali dettagli
aggiuntivi (es. "modello: —, temperatura: —" come campi d'esempio), area
commenti **visibile ma disattivata** con 1-2 commenti d'esempio già presenti
(statici) e un campo "Scrivi un commento…" che al click/invio mostra "in
arrivo" invece di aggiungere nulla.

**Dati d'esempio aggiuntivi**: due commenti statici coerenti, es. — *"Anche a
me è capitato un caso simile su un task di classificazione, sto raccogliendo
dati" (Anna P.)* e *"Quale versione del modello stai usando per il confronto
tra i tre run?" (Marco V.)*.

### 1.3 Vetrina progetti — "unisciti a un progetto"

**Cosa mostra**: una griglia/elenco di 3-4 schede-progetto, ciascuna con
titolo, breve descrizione, stato (es. "in corso", "cerca collaboratori"), e
un pulsante "Unisciti" che al click mostra "in arrivo — non ancora attivo",
mai una finta iscrizione riuscita.

**Dati d'esempio statici** (3, coerenti col dominio):

1. *"Confronto riproducibilità tra modelli"* — piccolo gruppo che documenta
   run ripetuti dello stesso task su modelli diversi, per capire quanto
   variano gli output a parità di prompt. Stato: cerca collaboratori.
2. *"Diario di vibe coding — un mese"* — raccolta collettiva di sessioni
   reali di sviluppo assistito da IA, con cosa ha funzionato e cosa no.
   Stato: in corso.
3. *"Prompt library per l'estrazione dati da PDF"* — repository condiviso di
   pattern di prompt testati per l'estrazione strutturata. Stato: appena
   avviato.

### 1.4 Richiesta di aiuto (esempio)

**Cosa mostra**: una singola scheda "richiesta di aiuto" in evidenza (può
essere la stessa voce di Giorgio N. del feed, presentata come formato
dedicato) con un pulsante "Rispondi" disattivato ("in arrivo") e un badge di
stato ("aperta"/"in arrivo risposte", entrambi solo scenografici).

**Nota di scope**: questa vista è deliberatamente la più leggera delle
quattro — è quasi un caso particolare del post di dettaglio (§1.2) con un
layout che enfatizza "qualcuno chiede aiuto", non una quarta struttura dati
diversa. Coerente con "poche schermate mirate", non moltiplica pattern UI.

### 1.5 Profilo (facoltativa, scenografica)

**Valutazione**: la includo come *opzionale, a bassa priorità*, non tra le
schermate minime. Motivo: un profilo utente scenografico aggiunge rischio di
percezione (è la schermata più facile da scambiare per "account reale", vedi
Delibera) senza aggiungere molto alla comprensione della direzione del
prodotto rispetto alle 4 viste sopra. Se lo sviluppatore-frontend ha margine
di budget, può essere una quinta vista minimale (nome scenografico, bio
d'esempio, elenco dei post/progetti "propri" tra quelli statici), ma **deve**
portare un badge ancora più esplicito delle altre ("Profilo di esempio — non
il tuo account") per non lasciare dubbi. Se il budget è stretto (vedi
`SCOPING.md §5`, due sessioni token), è la prima da tagliare.

## 2. Collegamento visivo al catalogo risorse esistente

**Stessa identità visiva**: palette (#111111/#10B981/#5B4BFF/#F2C94C/#F7F5EE),
font Inter, header con `.logo-nome`/`.claim` e footer `.piede` identici a
`repo-app/static/index.html`. Le nuove viste riusano le classi già esistenti
dove il pattern coincide (`.pannello-lista`, `.risorsa`→ pattern di scheda
riadattato a "post"/"progetto", `.filtro` per i tag) invece di introdurre un
secondo linguaggio visivo: lo sviluppatore-frontend non deve reinventare
componenti che già esistono nello stesso file CSS.

**Navigazione**: propongo di **tenere le due aree separate con un link
esplicito**, non una voce di menu paritaria integrata nel catalogo. Ragione:
il catalogo è il prodotto reale (dati veri, CRUD funzionante); il mockup è
scena statica. Fondere le due navigazioni in un'unica barra di tab
rischierebbe di far percepire la community come una funzione della stessa
app con lo stesso livello di realtà del catalogo — esattamente il rischio
di percezione che la Delibera segnala come il maggiore. Propongo quindi:

- Nel catalogo (`index.html`), un singolo link testuale ben visibile ma non
  integrato come tab di pari livello, es. in fondo alla pagina o come voce
  distinta nell'header: **"Anteprima community (mockup, non ancora attiva) →"**.
- Nel mockup stesso, un link di ritorno equivalente verso il catalogo reale,
  e il banner di anteprima (§3) presente su ogni vista del mockup fin dal
  primo caricamento, non solo alla prima interazione.
- Cartella/percorso separato per il mockup (es. `static/community/`), così
  che la separazione sia anche strutturale, non solo di navigazione — decisione
  che lascio confermare da `sviluppatore-frontend` in coerenza con
  `tecnico/ARCHITETTURA.md` (nessun backend nuovo, file statici serviti dallo
  stesso processo Python).

## 3. Etichettatura esplicita — vincolo non negoziabile (Delibera locale)

Requisito su **ogni singola schermata** del mockup, senza eccezioni:

1. **Banner fisso in alto**, sempre visibile (non scompare allo scroll, non è
   chiudibile in modo permanente — se chiudibile per sessione, deve
   ricomparire al refresh): testo "Anteprima — non ancora attivo. I contenuti
   sono di esempio, nessuna persona reale sta scrivendo qui." Colore di
   sfondo distinto dalla palette funzionale del catalogo (propongo `--giallo`
   #F2C94C come sfondo, `--nero` come testo — colore di attenzione, non di
   allarme/errore che userebbe rosso, coerente con la palette esistente che
   non ha un rosso dedicato).
2. **Ogni pulsante di interazione sociale** (Mi piace, Commenta, Unisciti,
   Rispondi, Scrivi un commento, eventuale "Segui progetto") resta visibile e
   cliccabile — non va disabilitato in modo da sembrare rotto — ma al click
   mostra un messaggio inline o un piccolo toast: **"In arrivo — questa
   funzione non è ancora attiva."** Mai un feedback che simuli successo
   (niente contatori che salgono, niente "Fatto!", niente nuova voce che
   appare come se fosse stata inviata).
3. **Autori dei contenuti d'esempio** marcati visivamente come tali: badge
   piccolo "esempio" accanto al nome, o nome stesso reso in corsivo/colore
   secondario — per non lasciare ambiguità nemmeno a uno sguardo veloce che
   "Marta R." sia una persona reale iscritta.
4. **Nessuna schermata di login/registrazione con campi funzionanti**: se
   presente (facoltativa, vedi profilo §1.5), è puramente illustrativa,
   etichettata "esempio" allo stesso modo, non deve accettare/validare
   credenziali vere né mostrare un "accesso riuscito".

Questo blocco è la traduzione operativa del "rischio più grosso" indicato
nella Delibera (percezione di prodotto reale) e va trattato dallo
sviluppatore-frontend come requisito di Definition of Done, non come nota
estetica facoltativa.

## 4. Verifica licenza — font Inter

`[[LACUNA]]`: non ho fonte verificata con certezza in questa sessione — il
mio ricordo è che Inter (Google Fonts) sia distribuito sotto SIL Open Font
License 1.1, che è generalmente permissiva anche per uso commerciale con
modifiche, ma **non è una fonte tracciabile che posso citare con certezza
ora**, ed è esattamente il tipo di claim che CLAUDE.md §6 e il mandato
dell'Archivista di Prodotto vietano di presumere. Il font è già in uso nel
catalogo esistente (`repo-app/static/style.css`, commento in cima al file
segnala la stessa lacuna: "verifica licenza: Archivista di Prodotto"), quindi
questo mockup **non introduce un nuovo asset da verificare**, eredita una
verifica già dovuta e non ancora fatta.

**Azione richiesta**: `archivista-prodotto` deve verificare e documentare la
licenza di Inter in `BRAND.md` prima che il catalogo *o* il mockup community
siano considerati Consegne pronte per uscire verso il committente in modo
definitivo — per un mockup locale non pubblicato il rischio è basso ma non
nullo (il committente stesso lo vedrà, ed è già un "terzo" ai fini di
CLAUDE.md §1). Nessun altro asset (icone, immagini) è previsto in questo
mockup: le uniche schede/card sono testo e colori CSS, nessuna libreria di
icone esterna — scelta deliberata per non introdurre una seconda licenza da
verificare quando una verifica sola (Inter) è già pendente.

## 5. Sintesi per lo Sviluppatore Frontend

- 4 schermate minime (feed, dettaglio post, vetrina progetti, richiesta
  d'aiuto-come-caso-del-dettaglio), 1 facoltativa a bassa priorità (profilo).
- Riuso dei componenti CSS esistenti (`.pannello-lista`, `.risorsa`→scheda,
  `.filtro`→tag), stessa palette e font del catalogo.
- Percorso separato (proposta `static/community/`), link esplicito di andata
  e ritorno tra catalogo e mockup, non un'unica barra di tab.
- Banner "Anteprima — non ancora attivo" fisso su ogni vista; ogni azione
  sociale mostra "in arrivo", mai un finto successo; autori marcati come
  "esempio".
- Nessun asset nuovo oltre Inter (già in uso, verifica licenza pendente
  presso l'Archivista, non bloccante per uso locale ma da chiudere prima di
  qualunque Consegna che esca stabilmente verso il committente).
