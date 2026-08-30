---
id: pattern-0002
titolo: Pagamenti e abbonamenti (checkout, billing ricorrente)
mandato: archivista-prodotto
commessa: interno
etichetta: DA VERIFICARE
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

## Problema che risolve

Qualunque commessa con "Superficie ricorrente" dichiarata nello Scoping (§3
CLAUDE.md: abbonamento, add-on, marketplace interno) o anche solo un acquisto
singolo ha bisogno di un flusso di pagamento che non tratti mai dati di carta
grezzi lato nostro (rischio PCI-DSS altrimenti enorme).

## Stato d'uso nell'Officina

`[[LACUNA: nessuna commessa reale ha ancora integrato un sistema di
pagamento — Officina in Sprint 000/001, zero commesse attive. Ricognizione di
un'opzione comune, non un pattern collaudato. Va validata alla prima
commessa e riclassificata VALIDATO.]]`

## Opzione considerata — Stripe (Checkout + Billing, SDK stripe-node)

- **Cosa fa**: pagina di pagamento ospitata da Stripe (Checkout) o
  componenti embedded (Elements), gestione abbonamenti ricorrenti (Billing),
  webhook per sincronizzare lo stato lato nostro backend.
- **Licenza dell'SDK client (`stripe-node`)**: file LICENSE nel repo
  ufficiale https://github.com/stripe/stripe-node/blob/master/LICENSE — SDK
  open source, copyright Stripe Inc. 2013. `[[LACUNA: il testo esatto del
  tipo di licenza (es. MIT) non è stato riletto carattere per carattere dal
  file in questa ricognizione — prima di un uso reale va aperto il file
  LICENSE e trascritto il tipo esatto, non presunto per notorietà del
  progetto.]]`
- **Termini del servizio (non licenza software)**: l'uso del servizio Stripe
  stesso è regolato dallo Stripe Services Agreement
  https://stripe.com/legal/ssa — è un contratto commerciale (commissioni per
  transazione, obblighi KYC), non una licenza software: va letto dal
  Referente di Commessa insieme al committente prima di firmare, non solo
  verificato dall'Archivista.
- **Alternative non ricognite in questo giro**: `[[LACUNA: PayPal, Paddle,
  LemonSqueezy non verificate in questa ricognizione — utile se una
  commessa futura ha esigenze di merchant-of-record (tasse gestite dal
  provider) che Stripe di base non copre.]]`

## Tempo di integrazione

`[[LACUNA: nessun tempo osservato dall'Officina. Non riporto la stima
generica "un pomeriggio" spesso citata online perché non è una fonte
verificabile riconducibile a un caso nostro — etichetta [DA VERIFICARE],
va misurato alla prima commessa che lo implementa e registrato qui con la
data e la commessa di origine.]]`

## Rischi noti da presidiare (non di licenza)

- Non transitare mai numeri di carta grezzi sui nostri server: usare sempre
  Checkout/Elements/tokenizzazione lato Stripe — presidio
  `sviluppatore-backend` + `devops-sicurezza`.
- Verifica firma webhook obbligatoria per evitare eventi falsificati.
- Se il modello è abbonamento, il flusso di disiscrizione non deve essere più
  difficile dell'iscrizione (§6 CLAUDE.md, dark pattern vietati) — presidio
  `custode`.
