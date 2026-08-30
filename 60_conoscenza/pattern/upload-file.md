---
id: pattern-0004
titolo: Upload e gestione file/immagini (storage a oggetti)
mandato: archivista-prodotto
commessa: interno
etichetta: DA VERIFICARE
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

## Problema che risolve

Qualunque webapp che accetta upload (avatar, documenti, allegati) ha bisogno
di non far transitare file di grandi dimensioni attraverso il proprio server
applicativo se evitabile, e di non esporre credenziali di storage al client.
Pattern comune: upload diretto a storage a oggetti con URL prefirmato
generato dal backend.

## Stato d'uso nell'Officina

`[[LACUNA: nessuna commessa reale ha ancora implementato upload file —
Officina in Sprint 000/001, zero commesse attive. Ricognizione di
alternative comuni, non un pattern collaudato. Va validata alla prima
commessa.]]`

## Alternative comuni (stack-agnostiche)

### Opzione A — `@aws-sdk/client-s3` (AWS SDK v3) verso S3 o storage
S3-compatibile (es. altri provider che espongono API compatibile — la
compatibilità dei singoli provider non è verificata in questa ricognizione)
- **Cosa fa**: genera URL prefirmati (presigned URL) lato backend, il client
  carica direttamente sullo storage senza passare i byte dal nostro server.
- **Licenza**: Apache License 2.0. Fonte verificata: repo ufficiale
  https://github.com/aws/aws-sdk-js-v3 (licenza dichiarata nel repository;
  tutte le pull request sono sottoposte esplicitamente sotto Apache 2.0).
- **Vincolo di stack**: qualunque backend Node/TypeScript; richiede un
  account/servizio storage S3-compatibile, che è un servizio a pagamento con
  termini propri distinti dalla licenza dell'SDK — `[[LACUNA: termini di
  prezzo e SLA del provider di storage effettivo non verificati in questa
  ricognizione, dipendono dalla scelta della commessa]]`.

### Opzione B — `multer` per upload multipart verso il proprio server (Node/Express)
- **Cosa fa**: middleware Express per parsing di `multipart/form-data` quando
  si sceglie di far transitare il file dal server applicativo (caso più
  semplice ma meno scalabile per file grandi).
- **Licenza**: MIT. Fonte verificata: file LICENSE nel repo ufficiale
  https://github.com/expressjs/multer/blob/main/LICENSE
- **Vincolo di stack**: Node/Express.

## Tempo di integrazione

`[[LACUNA: nessun tempo osservato dall'Officina. Va misurato alla prima
commessa che implementa upload file e registrato qui con data e commessa
di origine.]]`

## Rischi noti da presidiare (non di licenza)

- Validare tipo/dimensione file sia lato client sia lato server (un client
  compromesso può bypassare i controlli JS) — `sviluppatore-backend`.
- URL prefirmati con scadenza breve, mai credenziali permanenti esposte al
  client — `devops-sicurezza`.
- Se i file contengono dati personali (es. documenti d'identità), base
  giuridica e conservazione dichiarate prima dello schema — `custode`.
