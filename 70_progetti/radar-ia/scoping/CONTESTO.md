---
id: 10-0002
titolo: Contesto di mercato — RADAR IA (Prototipo Catalogo Risorse)
mandato: stratega-prodotto
commessa: radar-ia
etichetta: DA VERIFICARE
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

> Nota di metodo: nessun claim quantitativo sotto è [VALIDATO] — non
> disponiamo di fonti primarie verificate (analytics di terzi, survey
> proprie). Ogni numero visto in ricerca web è di prodotti/aziende terze,
> non nostro, e viene marcato come tale o scartato. Dove non c'è fonte
> affidabile, si marca `[[LACUNA: ...]]` invece di stimare.

## Concorrenza diretta

Prodotti che fanno la stessa cosa dichiarata dal PMV: un catalogo curato di
risorse (pratiche, strumenti, esperimenti) sull'IA, con azione di
salvataggio/segnatura da parte dell'utente.

- **Directory generaliste di tool IA** (es. "There's An AI For That",
  TopAI.tools, e le ~150+ directory elencate in aggregatori come
  appscribed.com) — cataloghi molto ampi, orientati alla scoperta di
  prodotti commerciali, non alla riproducibilità o alla curatela critica.
  [DA VERIFICARE] copertura reale e taglio editoriale, non abbiamo verificato
  i singoli prodotti in profondità.
- **Hub tecnici verticali**: Hugging Face (Model Hub, Spaces), Papers with
  Code — cataloghi *di modelli/codice*, non di "pratiche ed esperimenti
  documentati" in senso più ampio; pubblico più tecnico e già servito bene
  su questo fronte specifico. Sono concorrenza diretta solo se RADAR IA
  finisse per sovrapporsi al loro perimetro (modelli/repo), non se resta su
  pratiche/strumenti/esperimenti documentati in linguaggio più divulgativo.
- **Liste "awesome-*" su GitHub** (es. awesome-ai-news e simili) — cataloghi
  curati manualmente, gratuiti, senza UI dedicata né funzione di stato
  personale ("letta/provata"); è probabilmente il concorrente diretto più
  vicino nello spirito (community, riproducibilità, gratuità) ma più povero
  come prodotto (niente stato utente, niente ricerca/filtri).

`[[LACUNA: non abbiamo verificato quante di queste piattaforme abbiano
funzionalità di "segna come letta/provata" o tracciamento personale — è il
differenziale di prodotto dichiarato del PMV, va controllato prima di
vantarlo come unico.]]`

## Concorrenza sostitutiva (la più trascurata, spesso la più forte)

Come il pubblico dichiarato (ricercatori, studenti, professionisti, curiosi)
risolve oggi lo stesso problema — "tenere traccia di risorse IA valide e
riproducibili" — senza un prodotto come RADAR IA:

- **Newsletter esistenti** (TLDR AI, "An AI For That" e simili) — consumo
  passivo, nessuna funzione di catalogo personale né di riproducibilità
  verificata; il segnale "letto" è nella mente dell'utente o al più in un
  filtro email, non in uno strumento dedicato.
- **Bookmark del browser / Notion / Obsidian personali** — la vera
  concorrente sostitutiva più forte: ogni utente tecnico già organizza le
  proprie risorse in uno strumento generico che padroneggia, senza dover
  imparare un nuovo prodotto né fidarsi della curatela di terzi.
- **Twitter/X, LinkedIn, Reddit (r/MachineLearning e simili), Discord/Slack
  di community IA** — scoperta sociale continua, spesso già "buona
  abbastanza" per chi è già dentro quelle community: il problema che RADAR
  IA vuole risolvere (trovare + tracciare risorse valide) è oggi parzialmente
  risolto informalmente lì, a costo di rumore e di nessuna riproducibilità
  verificata.
- **"Non fare nulla"** — per una parte del pubblico dichiarato (curiosi,
  professionisti non specialisti) il problema non è abbastanza sentito da
  giustificare uno strumento dedicato: si informano in modo saltuario e
  accettano di perdere risorse valide nel tempo. Questo è il caso peggiore
  per l'Ipotesi di Valore e va monitorato esplicitamente (si veda IPOTESI.md).

## Perché "ora" (rispetto al momento di mercato)

`[[LACUNA: il committente non ha fornito un motivo esplicito di timing
("perché ora e non un anno fa/dopo"); da chiedere in Sprint successivo —
SCOPING.md §0 domanda 3 resta parzialmente aperta]]`. L'osservazione
qualitativa (non validata) è che l'offerta di strumenti/pratiche IA è
cresciuta più rapidamente della capacità dei canali esistenti (newsletter,
liste awesome, directory generaliste) di garantirne la riproducibilità
verificata — ma è un'ipotesi di contesto, non un dato.

## Implicazione per il PMV

La concorrenza sostitutiva (bookmark personali, community informali,
newsletter passive) è più pericolosa della concorrenza diretta per
l'Ipotesi di Valore di questo prototipo: non basta essere "meglio curato"
di una directory generalista, bisogna essere abbastanza migliore di
"tenerlo a mente / salvarlo altrove" da giustificare il cambio di abitudine
— per un solo utente reale in questa fase, il committente stesso. Vedi
`IPOTESI.md` per come questo si traduce in Segnale falsificabile.
