---
id: DEL-0004
titolo: Ripresa automatica del lavoro al reset del limite di sessione dell'abbonamento
data: 2026-08-30
stato: in vigore
vincola: [regista]
ambito: officina
---

## Decisione

Quando un committente dichiara che il budget di una commessa è "tutte le
risorse disponibili nell'abbonamento Claude, nessun credito aggiuntivo", il
Regista imposta **di default** un meccanismo di ripresa automatica: se il
lavoro si interrompe perché la sessione ha raggiunto il limite d'uso
dell'abbonamento, il Regista non si limita a fermarsi e aspettare che
l'umano se ne accorga — programma un promemoria/controllo periodico
(`send_later`/Routine) che, al momento in cui la sessione torna
utilizzabile, verifica cosa resta da fare e riprende la delega ai mandati
competenti, senza bisogno che l'umano debba far ripartire manualmente il
lavoro ogni volta.

## Limite onesto di questa regola (va dichiarato al committente, non taciuto)

Il Regista **non ha visibilità diretta** sul consumo residuo del piano
dell'utente né sull'orario esatto in cui un limite si resetta: può solo
programmare un tentativo periodico e verificare, quando il controllo parte,
se la sessione risponde di nuovo. Non è quindi una ripresa "immediata al
secondo dello sblocco", è una ripresa "al prossimo controllo programmato
dopo lo sblocco". La cadenza dei controlli va dichiarata esplicitamente nel
`STATO_COMMESSA.md` della commessa, non lasciata implicita.

## Ragione più forte a favore

Un committente che paga con l'abbonamento invece che con crediti dedicati
sta scegliendo esplicitamente di accettare tempi di consegna variabili
(dipendenti dal reset del limite) in cambio di zero costo aggiuntivo. Il
Regista che si ferma silenziosamente e aspetta un messaggio umano per
ripartire spreca esattamente il tempo che quella scelta avrebbe dovuto
recuperare.

## Rischio più grosso da tenere d'occhio

Un controllo programmato troppo frequente non serve (se il limite non si è
ancora resettato, il tentativo fallisce e basta) ma un controllo troppo
raro allunga inutilmente i tempi di consegna. Nessun dato certo
sull'esatta finestra di reset è disponibile al Regista: la cadenza scelta
è una stima, va rivista se sistematicamente troppo larga o troppo stretta.

## Cosa questa decisione vieta

1. Il Regista non si ferma mai silenziosamente su una commessa con budget
   "solo abbonamento" senza programmare un tentativo di ripresa.
2. Il Regista non promette mai un orario esatto di ripresa: comunica solo
   una cadenza di controllo e l'incertezza che comporta.

## Debito contratto

Nessuno.

## Primo passo

Applicata subito su RADAR IA (`70_progetti/radar-ia/`): vedi
`STATO_COMMESSA.md` per la cadenza scelta e la Routine programmata.

## Cosa la farebbe riaprire

Se in futuro diventa disponibile un modo per il Regista di conoscere con
certezza il momento esatto di reset del limite, questa Delibera va
aggiornata per usare quel dato invece di un controllo a cadenza fissa.
