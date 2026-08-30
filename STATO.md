# STATO — fonte di verità sullo stato dell'Officina

Ultimo aggiornamento: 2026-08-30 · Sprint: 000 (inizializzazione)

## Delibere in vigore

- **DEL-0001** — Metodo: agenzia per committenti esterni con metodo da
  startup interna. Gerarchia dei veti: compliance → scope/budget → rilascio →
  fonti/licenze → validazione della domanda.
- **DEL-0002** — Architettura di lavoro: repo git indipendente da Motore
  Talento, Drive come specchio in sola lettura pensato per la messa online.

## Commesse attive

Nessuna. (Sprint 000: l'Officina non ha ancora ricevuto una commessa.)

## Coda — Sprint 001 (lavoro interno, propedeutico alla prima commessa)

| # | Task | Mandato | Dipende da | Esito atteso |
|---|---|---|---|---|
| 1 | Template di Scoping completo, con le domande minime da porre a un committente nuovo | referente-commessa | — | `70_progetti/_TEMPLATE/SCOPING.md` |
| 2 | Checklist di sicurezza pre-rilascio v0, basata su OWASP Top 10 | devops-sicurezza | — | `60_conoscenza/checklist-rilascio/v0.md` |
| 3 | Parere quadro su base giuridica e minimizzazione per webapp generiche (schema ricorrente indipendente dalla commessa) | custode | — | `50_compliance/PARERE_QUADRO_DATI.md` |
| 4 | Ricognizione di 3-5 pattern tecnici riusabili (autenticazione, pagamenti, onboarding) con licenze verificate | archivista-prodotto | — | `60_conoscenza/pattern/` popolato |

## Fatto

- 2026-08-30 — Struttura del repo, protocollo a due unità (Sprint/Fase di
  Commessa), undici mandati, gerarchia dei veti, gate di rigore adattato.

## Note per il prossimo Sprint

I task 1–4 sono indipendenti e propedeutici: preparano l'Officina a ricevere
la prima commessa reale senza dover improvvisare template e checklist a metà
lavoro. Nessuna commessa si apre finché non esiste almeno il task 1.
