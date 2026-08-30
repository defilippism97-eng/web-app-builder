---
id: DEL-0005
titolo: Nuovo mandato permanente — Collaudatore & QA
data: 2026-08-30
stato: in vigore
vincola: [regista, referente-commessa, collaudatore]
ambito: officina
---

## Decisione

Aggiunto un dodicesimo mandato permanente, **Collaudatore & QA**
(`collaudatore`, vedi `90_ufficio/MANDATI.md` §9 e
`.claude/agents/collaudatore.md`), su richiesta diretta del committente
durante la commessa RADAR IA: verifica ogni Consegna eseguendo davvero
l'applicazione — non leggendo il codice — prima che raggiunga il
committente, e riporta un verdetto al Referente di Commessa. Inserito nella
gerarchia dei veti (`90_ufficio/PROTOCOLLO.md` §4) tra DevOps & Sicurezza e
Archivista di Prodotto.

## Ragione più forte a favore

Prima di questa Delibera, tra "lo sviluppatore dichiara che funziona" e "il
committente lo scopre da solo" non c'era nessun controllo che eseguisse
davvero l'applicazione dal punto di vista di chi la usa. I test automatici
verificano il codice, non l'esperienza; il Designer verifica il concept, non
l'implementazione; il Referente verifica lo scope sulla carta, non
nell'uso reale.

## Rischio più grosso da tenere d'occhio

Un mandato di verifica funzionale rischia di sovrapporsi al lavoro già
fatto dagli sviluppatori (test automatici) o di degenerare in una seconda
revisione di codice invece che in un collaudo d'uso reale — per questo il
mandato è scritto per vietare esplicitamente quella deriva ("Come
fallisce" in `MANDATI.md`).

## Cosa questa decisione vieta

1. Nessuna Consegna verso il committente salta il collaudo se il
   Collaudatore è disponibile per quella commessa.
2. Il Collaudatore non ha veto su scelte di design/gusto (restano del
   Designer di Prodotto) né sostituisce il Consiglio come critica ampia
   sulla direzione della commessa (vedi `MANDATI.md`, nota nel mandato).

## Debito contratto

Nessuno.

## Primo passo

Applicato subito su RADAR IA: collaudo del mockup community prima della
Consegna al committente.

## Cosa la farebbe riaprire

Se il Collaudatore degenera nella deriva descritta in "Come fallisce" del
suo mandato, o se il costo di un collaudo per ogni Consegna risulta
sproporzionato per commesse molto piccole, si porta la questione al
Consiglio per definire una soglia sotto cui il collaudo è facoltativo.
