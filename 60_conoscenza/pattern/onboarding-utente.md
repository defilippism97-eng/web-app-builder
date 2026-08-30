---
id: pattern-0003
titolo: Onboarding utente (form multi-step con validazione)
mandato: archivista-prodotto
commessa: interno
etichetta: DA VERIFICARE
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

## Problema che risolve

Il primo contatto tra un utente nuovo e il prodotto (§0 CLAUDE.md: "semplice
da capire" — un utente nuovo completa il compito primario senza istruzioni).
Serve validazione dati lato client e server coerente, senza duplicare la
logica di validazione in due posti che poi divergono.

## Stato d'uso nell'Officina

`[[LACUNA: nessuna commessa reale ha ancora costruito un onboarding —
Officina in Sprint 000/001, zero commesse attive. Ricognizione di alternative
comuni, non un pattern collaudato. Va validata alla prima commessa.]]`

## Alternative comuni (stack-agnostiche)

### Opzione A — react-hook-form + zod, ecosistema React
- **Cosa fa**: `react-hook-form` gestisce stato e performance dei form,
  `zod` definisce lo schema di validazione riusabile sia lato client sia
  lato server (stesso schema, meno divergenza).
- **Licenza react-hook-form**: MIT. Fonte verificata: file LICENSE nel repo
  ufficiale
  https://github.com/react-hook-form/react-hook-form/blob/master/LICENSE
- **Licenza zod**: MIT. Fonte verificata: file LICENSE nel repo ufficiale
  https://github.com/colinhacks/zod/blob/main/LICENSE
- **Vincolo di stack**: React (o framework che lo incorporano, es. Next.js).

### Opzione B — validazione nativa dello stack backend scelto
`[[LACUNA: non ricognita in questo giro. Se una commessa non usa React sul
frontend (D-002, stack di default non ancora scelto dall'Officina), serve
una ricerca separata per l'ecosistema effettivo — non presumere che
react-hook-form/zod siano applicabili fuori da React.]]`

## Tempo di integrazione

`[[LACUNA: nessun tempo osservato dall'Officina. Nessuna stima riportata:
va misurato alla prima commessa e registrato qui con data e commessa di
origine.]]`

## Nota di metodo (non di licenza)

L'onboarding è tipicamente il punto dove più facilmente si introduce dark
pattern (campi obbligatori non necessari, consenso preselezionato). Ogni
campo raccolto va mappato a un uso dichiarato — minimizzazione GDPR, §6
CLAUDE.md — presidio `custode`, non di questo mandato.
