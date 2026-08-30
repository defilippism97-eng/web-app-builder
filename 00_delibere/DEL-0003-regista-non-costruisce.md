---
id: DEL-0003
titolo: Il Regista non produce mai contenuto di dominio, anche sotto budget stretto
data: 2026-08-30
stato: in vigore
vincola: [regista]
ambito: officina
---

## Decisione

Il Regista **non scrive mai** decisioni architetturali (`ARCHITETTURA.md`)
né codice applicativo, in nessuna commessa, indipendentemente da quanto
stretto sia il budget dichiarato dal committente. Ogni decisione tecnica
strutturale passa sempre da `architetto`; ogni riga di codice applicativo
passa sempre da `sviluppatore-backend` e/o `sviluppatore-frontend`, come
già scritto in `90_ufficio/MANDATI.md` §4-6 — questa Delibera non introduce
una regola nuova, **rimuove un'eccezione che il Regista si era concesso da
solo** durante la commessa RADAR IA, Sprint 001.

## Precedente che ha originato la Delibera

Nella commessa RADAR IA, il Regista ha scritto direttamente
`70_progetti/radar-ia/tecnico/ARCHITETTURA.md` e l'intero
`70_progetti/radar-ia/repo-app/`, saltando la delega a `architetto` e agli
sviluppatori, per risparmiare l'overhead di coordinamento tra sub-agenti
dato un budget dichiarato molto stretto (equivalente a due sessioni Claude
Pro). Il committente, interrogato direttamente, ha scelto di **non**
autorizzare questa scorciatoia nemmeno sotto vincolo di budget.

## Ragione più forte a favore

Il valore del metodo multi-mandato non è la velocità, è che ruoli diversi
notano cose diverse: uno sviluppatore che scrive da solo architettura e
codice non ha nessuno che gli chieda "perché non la scelta più semplice
possibile" o verifichi il codice con occhi diversi da chi l'ha scritto.
Fare eccezioni "solo per i prototipi piccoli" è esattamente il tipo di
scorciatoia "ragionevole" che, sommata nel tempo, svuota il metodo (vedi
`90_ufficio/MANDATI.md`, "Come fallisce" del Referente di Commessa — lo
stesso meccanismo vale qui).

## Rischio più grosso da tenere d'occhio

Il costo di coordinamento tra sub-agenti è reale e non nullo: su commesse
con budget davvero minimo, delegare correttamente potrebbe consumare una
quota significativa del budget dichiarato solo in overhead di contesto.
Questo rischio non si assorbe facendo eccezioni silenziose: se il budget
non basta a seguire il metodo, è un caso da segnalare esplicitamente al
committente (vedi Debito di Rischio) o da portare come domanda aperta, non
da risolvere bypassando la delega senza dirlo.

## Cosa questa decisione vieta

1. Il Regista non scrive mai `ARCHITETTURA.md` o codice applicativo in
   prima persona, in nessuna commessa.
2. Il Regista non decide da solo di saltare la delega per motivi di
   budget: se ritiene che delegare interamente ecceda il budget
   dichiarato, lo segnala come domanda aperta o Debito di Rischio
   **prima** di costruire, non dopo.

## Debito contratto

`70_progetti/radar-ia/DEBITO_TECNICO.md` registra la deviazione già
avvenuta su RADAR IA (architettura e codice del Prototipo Minimo
Verificabile scritti dal Regista, non ancora passati da `architetto` e da
`sviluppatore-backend`/`sviluppatore-frontend`).

## Primo passo

Nessuna riscrittura automatica: il prototipo RADAR IA resta come consegnato
finché il committente non decide se vuole una revisione retroattiva da
parte dei mandati competenti (vedi debito) o se il Segnale dell'Ipotesi di
Valore vale la pena osservarlo prima di investire altro budget in una
revisione di processo su un prototipo che potrebbe comunque essere
scartato.

## Cosa la farebbe riaprire

Se il costo di coordinamento tra sub-agenti si dimostra sistematicamente
incompatibile con budget di commesse piccole (non solo RADAR IA), si porta
la questione al Consiglio dei 5 per decidere se serve un mandato più
leggero per prototipi sotto una soglia dichiarata, invece di lasciare la
scelta al giudizio del momento del Regista.
