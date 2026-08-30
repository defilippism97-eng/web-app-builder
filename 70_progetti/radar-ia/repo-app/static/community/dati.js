// RADAR IA — Anteprima community: dati d'esempio STATICI.
//
// Vincolo non negoziabile (DEL-LOCALE-001, MOCKUP_COMMUNITY.md): questi dati
// sono inventati dall'Officina per il mockup, non persone reali, non
// raccolti da nessun backend. Nessuna chiamata di rete: tutto hardcoded qui.
// Non aggiungere qui dati reali di terzi, nemmeno "solo per la demo".

const POST_COMMUNITY = [
  {
    id: 1,
    autore: "Marta R.",
    tag: "vibe coding",
    testo:
      "Ho provato a far scrivere a Claude l'intera struttura di un piccolo tool CLI partendo solo da una descrizione a voce trascritta. Ha funzionato per lo scaffolding, molto meno per la logica di edge case: lì ho dovuto riscrivere quasi tutto a mano. Vale la pena per il primo 20%, non oltre.",
    tipo: "post",
  },
  {
    id: 2,
    autore: "Luca D.",
    tag: "esperimento",
    testo:
      "Esperimento di riproducibilità: stesso prompt, stesso modello, tre run in giorni diversi su un task di estrazione dati da PDF. Output strutturalmente identico due volte su tre; la terza volta ha invertito due colonne di una tabella. Sto documentando il seed/temperatura usati per capire se è determinismo reale o casualità percepita.",
    tipo: "post",
    dettagli: [
      { etichetta: "Modello", valore: "—" },
      { etichetta: "Temperatura", valore: "—" },
    ],
    commenti: [
      {
        autore: "Anna P.",
        testo: "Anche a me è capitato un caso simile su un task di classificazione, sto raccogliendo dati.",
      },
      {
        autore: "Marco V.",
        testo: "Quale versione del modello stai usando per il confronto tra i tre run?",
      },
    ],
  },
  {
    id: 3,
    autore: "Sara T.",
    tag: "opinione",
    testo:
      "Continuo a pensare che il problema con 'l'IA scrive il codice al posto tuo' non sia la qualità del codice ma la perdita del modello mentale di chi lo revisiona. Se non hai scritto tu la logica, fai fatica a fare code review seria un mese dopo.",
    tipo: "post",
  },
  {
    id: 4,
    autore: "Fede B.",
    tag: "pratica",
    testo:
      "Piccola pratica che uso da un mese: prima di ogni sessione di vibe coding scrivo tre righe di 'cosa NON deve fare' oltre a 'cosa deve fare'. Riduce parecchio le derive silenziose dell'agente su funzionalità non richieste.",
    tipo: "post",
  },
  {
    id: 5,
    autore: "Giorgio N.",
    tag: "vibe coding",
    testo:
      "Chiedo aiuto: sto costruendo un prototipo con un agente IA che continua a reintrodurre una dipendenza che avevo scartato esplicitamente due prompt prima. Qualcuno ha un pattern per far 'ricordare' vincoli negativi lungo una sessione lunga?",
    tipo: "aiuto",
    stato: "aperta",
  },
];

const PROGETTI_COMMUNITY = [
  {
    id: 1,
    titolo: "Confronto riproducibilità tra modelli",
    descrizione:
      "Piccolo gruppo che documenta run ripetuti dello stesso task su modelli diversi, per capire quanto variano gli output a parità di prompt.",
    stato: "cerca collaboratori",
  },
  {
    id: 2,
    titolo: "Diario di vibe coding — un mese",
    descrizione:
      "Raccolta collettiva di sessioni reali di sviluppo assistito da IA, con cosa ha funzionato e cosa no.",
    stato: "in corso",
  },
  {
    id: 3,
    titolo: "Prompt library per l'estrazione dati da PDF",
    descrizione:
      "Repository condiviso di pattern di prompt testati per l'estrazione strutturata.",
    stato: "appena avviato",
  },
];
