---
id: pattern-0005
titolo: Notifiche email transazionali (conferma, reset password, ricevute)
mandato: archivista-prodotto
commessa: interno
etichetta: DA VERIFICARE
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

## Problema che risolve

Quasi ogni webapp con account utente deve inviare email transazionali
(conferma registrazione, reset password, ricevuta di pagamento). Sono email
ad alta deliverability richiesta (finiscono nello spam più facilmente delle
email marketing se il mittente non è configurato correttamente) e spesso
contengono dati personali o link sensibili (token di reset).

## Stato d'uso nell'Officina

`[[LACUNA: nessuna commessa reale ha ancora integrato invio email
transazionali — Officina in Sprint 000/001, zero commesse attive.
Ricognizione di alternative comuni, non un pattern collaudato. Va validata
alla prima commessa.]]`

## Alternative comuni (stack-agnostiche)

### Opzione A — Resend (servizio) + SDK ufficiale `resend-node`
- **Cosa fa**: API per invio email transazionali con template, gestione
  deliverability/dominio verificato lato servizio.
- **Licenza dell'SDK**: MIT. Fonte verificata: file LICENSE nel repo
  ufficiale https://github.com/resend/resend-node/blob/canary/LICENSE
- **Nota**: l'SDK è open source (MIT), ma il servizio di invio è a pagamento
  oltre una soglia gratuita — termini contrattuali distinti dalla licenza
  del codice. `[[LACUNA: prezzo e limiti del piano gratuito non verificati
  in questa ricognizione — di competenza Stratega Commerciale se il costo
  ricorrente è rilevante per il pricing della commessa]]`.

### Opzione B — Nodemailer, invio via qualunque server SMTP (self-hosted o provider)
- **Cosa fa**: libreria di invio email generica, non legata a un servizio
  specifico; si appoggia a un server SMTP a scelta (proprio o di terzi).
- **Licenza**: MIT-0 (MIT senza obbligo di attribuzione). Fonte verificata:
  pagina ufficiale https://nodemailer.com/license e repo ufficiale
  https://github.com/nodemailer/nodemailer. Nota storica verificata dalla
  stessa fonte: per un breve periodo (v3) il progetto era sotto licenza
  EUPL 1.1, poi tornato a MIT — utile da sapere se una commessa fissa una
  versione precedente per errore.
- **Vincolo di stack**: Node.js, indipendente dal provider SMTP scelto (che
  ha però le proprie condizioni di servizio, non verificate qui).

## Tempo di integrazione

`[[LACUNA: nessun tempo osservato dall'Officina. Va misurato alla prima
commessa che implementa invio email transazionali e registrato qui con data
e commessa di origine.]]`

## Rischi noti da presidiare (non di licenza)

- Token di reset password: scadenza breve, uso singolo, mai in chiaro nei
  log — `sviluppatore-backend` + `devops-sicurezza`.
- Base giuridica per l'indirizzo email raccolto (contratto/esecuzione del
  servizio, tipicamente non serve consenso separato per email puramente
  transazionali, ma va dichiarato esplicitamente) — `custode`.
