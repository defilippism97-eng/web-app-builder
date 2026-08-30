---
id: DEL-0001
titolo: Metodo — agenzia per committenti esterni con metodo da startup interna
data: 2026-08-30
stato: in vigore
vincola: [tutti]
ambito: officina
---

## Decisione

L'Officina lavora per committenti esterni reali, ma ogni commessa attraversa
uno Scoping esplicito con Ipotesi di Valore falsificabile, un Prototipo Minimo
Verificabile prima dell'investimento pieno, e Punti di Decisione che nessun
mandato tecnico attraversa da solo. La gerarchia dei presidi, in ordine di
priorità: compliance/privacy/etica → budget e scope → qualità e sicurezza del
codice → validazione della domanda prima della costruzione.

## Ragione più forte a favore

Un'agenzia tradizionale ottimizza per consegnare ciò che il contratto
descrive. Una startup ottimizza per imparare cosa funziona. Il metodo unisce
le due cose: si consegna quanto pattuito, ma non si costruisce scope non
verificato solo perché il contratto lo permetterebbe. Questo protegge sia il
margine dell'Officina sia il committente da funzionalità che nessuno userà.

## Rischio più grosso da tenere d'occhio

Il rischio speculare a DEL-0001 di Motore Talento: lì il rischio era la
validazione mai fatta, qui è **la validazione che rallenta una scadenza reale
del cliente**. Un Punto di Decisione mal calibrato può bloccare una commessa
nel momento sbagliato. Va monitorato nella prima commessa reale (D-001) prima
di considerare il metodo maturo.

## Cosa questa decisione vieta

1. Nessuna funzionalità nuova entra in sviluppo senza Ipotesi di Valore
   dichiarata (CLAUDE.md §4).
2. Nessuna Consegna con parere del Custode «non firmata» esce, per nessun
   motivo, nemmeno su richiesta esplicita del committente o pressione di
   scadenza.
3. Nessuno scope si estende senza una Delibera locale che lo autorizzi.
4. Nessun rilascio pubblico senza checklist di sicurezza superata.

## Debito contratto

Nessuno a livello di Officina: il debito si contrae per commessa nei registri
locali `DEBITO_TECNICO.md` e `DEBITO_RISCHIO.md`.

## Primo passo

Task 1–4 dello Sprint 001, propedeutici alla prima commessa.

## Cosa la farebbe riaprire

Se dopo tre commesse i Punti di Decisione si rivelano sistematicamente un
freno rispetto al valore che aggiungono (rilevabile da D-001), il metodo va
alleggerito per le commesse piccole e mantenuto integrale per quelle grandi.
