---
id: DEL-LOCALE-001
titolo: Mockup/anteprima visiva della community RADAR IA — solo frontend, dati locali
mandato: referente-commessa
commessa: radar-ia
etichetta: N/A
parere_rilascio: non richiesto
stato: in vigore
data: 2026-08-30
vincola: [referente-commessa, architetto, designer-prodotto, sviluppatore-frontend, sviluppatore-backend, custode]
ambito: commessa radar-ia
riferimento: PUNTO_DECISIONE_001.md (risposta del committente, 2026-08-30);
  scoping/IPOTESI.md Punto di Decisione #2
---

## Decisione

Il committente ha risposto a `PUNTO_DECISIONE_001.md` con una variante
mirata dell'Opzione 2 (non tra le tre opzioni testuali offerte, ma una
richiesta specifica e più circoscritta di essa): costruire **solo un
mockup/anteprima visiva e interattiva** di come funzionerà la community —
condivisione di esperienze/opinioni su IA e lavoro, possibilità di unirsi a
progetti altrui, richieste di aiuto — **senza** costruire ora la community
funzionante.

Questa Delibera autorizza **esclusivamente**:

- Schermate navigabili che mostrano come si presenterà la community
  (elenco/dettaglio di "esperienze"/"opinioni"/"progetti"/"richieste di
  aiuto"), con interazioni cliccabili (es. aprire una scheda, compilare un
  form, vedere un elenco filtrato) che danno l'impressione del prodotto
  finale.
- Dati **d'esempio statici** (scritti a mano dall'Officina o generati come
  placeholder realistico) oppure dati inseriti dal committente stesso e
  salvati **solo localmente sul dispositivo del committente** (es.
  `localStorage`/file locale del browser), mai su un backend condiviso.
  Nessuna sincronizzazione tra dispositivi diversi, nessun server che
  raccolga o esponga questi dati a terzi.
- Nessun account reale: se il mockup mostra una schermata di login o un
  profilo utente, è scena, non funzione — non autentica nessuno, non
  distingue utenti reali diversi.

## Cosa questa Delibera NON autorizza (resta vietato, vincolato a
`scoping/IPOTESI.md` Punto di Decisione #2 e a `SCOPING.md §7`)

1. **Nessun backend community**: nessuna API, nessun database condiviso,
   nessuna persistenza multi-utente. Se una schermata "sembra" salvare un
   dato condiviso, in realtà lo salva solo in locale o lo mostra da un
   dataset statico — mai davvero condiviso tra due dispositivi o persone.
2. **Nessuna autenticazione reale**: nessun sistema di registrazione,
   login, gestione password, sessione utente verificata. Qualunque
   schermata di login nel mockup è puramente visiva.
3. **Nessun dato di utenti terzi reali**: nessuna raccolta, visualizzazione
   o trattamento di dati personali di persone diverse dal committente. I
   contenuti "di altri utenti" mostrati nel mockup sono inventati/di
   esempio, mai reali.
4. **Nessuna persistenza multi-utente o condivisa**: escluso qualunque
   meccanismo che permetta a due dispositivi/persone diverse di vedere lo
   stesso dato aggiornato in tempo reale o quasi.
5. **Nessuna moderazione**: non esiste contenuto di terzi da moderare,
   perché non esistono terzi reali in questo perimetro.
6. Tutto quanto elencato in `SCOPING.md §7` come fuori scope resta fuori
   scope: questa Delibera non lo scioglie, apre solo un'eccezione
   puntuale e delimitata (il mockup) dentro quel perimetro più ampio
   ancora vietato.

Il Punto di Decisione #2 di `scoping/IPOTESI.md` (sviluppo pieno della
community, condizionato a un Segnale da 3-5 utenti terzi reali) **resta
interamente in piedi e non è anticipato da questa Delibera**: un mockup
visivo che "fa intuire" non è, e non sostituisce, il Segnale richiesto per
quel Punto di Decisione.

## Ragione più forte a favore

Il committente ha chiesto qualcosa di più preciso e più economico
dell'Opzione 2 originaria (che ipotizzava un campo "opinione/nota" nel
catalogo esistente): una vetrina visiva della community, senza le
implicazioni di compliance, sicurezza e costo di un backend multi-utente
reale. Questo resta dentro lo spirito dell'Opzione 2/raccomandazione del
Punto di Decisione 001 — dare un segnale concreto senza costruire ciò che
lo Scoping ha isolato come sviluppo pieno — pur essendo una richiesta
diversa nella forma da quella già scritta, e va quindi trattata con una
Delibera dedicata, non fatta rientrare implicitamente in quella vecchia.

## Rischio più grosso da tenere d'occhio

Il rischio principale non è tecnico ma di percezione: un mockup ben fatto
"sembra" un prodotto funzionante. Se il committente (o chiunque veda il
mockup) lo scambia per la community reale già in costruzione, si genera lo
stesso disallineamento di aspettative che il Punto di Decisione 001 voleva
prevenire. Mitigazione: ogni schermata di mockup deve essere accompagnata,
nella Consegna, da un avviso esplicito e visibile che si tratta di
anteprima/non prodotto funzionante, e la comunicazione verso il committente
(bozza, mai inviata direttamente) deve ribadirlo per iscritto.

Rischio secondario, di processo: la tentazione — già segnalata come pattern
di scope creep in `STATO_COMMESSA.md` — di far scivolare "solo un piccolo
salvataggio condiviso per la demo" dentro il mockup con la scusa che è "solo
per farlo vedere meglio". Questa Delibera lo blocca esplicitamente al punto
1 sopra: nessun backend, in nessuna forma, nemmeno dimostrativa.

## Debito contratto

Nessuno (nessun debito tecnico o di rischio generato da questa Delibera in
sé: si tratta di un frontend statico senza dati personali reali). Va
riverificato dal Custode Normativo se i dati d'esempio, pur inventati,
assomigliano a persone identificabili reali (es. copiare opinioni vere di
persone reali senza consenso sarebbe una violazione anche in un mockup).

## Primo passo

Delega a `designer-prodotto` (concept visivo delle schermate) e
`sviluppatore-frontend` (implementazione), a valle di questa Delibera.
Prima di ogni Consegna: verifica del Custode Normativo che nessun dato
d'esempio riproduca persone reali identificabili, e conferma esplicita del
committente sul budget aggiuntivo (vedi `STATO_COMMESSA.md` §Budget e
tempo — lacuna aperta).

## Cosa la farebbe riaprire

Se durante lo sviluppo emerge la necessità tecnica o di design di un
qualunque elemento tra quelli vietati sopra (anche minimo, es. "un solo
salvataggio condiviso per la demo dal vivo"), lo sviluppo si ferma e torna
al Referente di Commessa prima di procedere: non si estende questa
Delibera per interpretazione, se ne scrive una nuova esplicita o si torna
al Punto di Decisione 001.
