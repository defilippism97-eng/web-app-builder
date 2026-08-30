---
id: DEL-0002
titolo: Architettura di lavoro — repo indipendente, Drive per la messa online
data: 2026-08-30
stato: in vigore
vincola: [regista, referente-commessa, devops-sicurezza]
ambito: officina
---

## Decisione

Repository **indipendente e separato** da Motore Talento, stessa logica
infrastrutturale (repo git come fonte di verità, Drive come specchio in sola
lettura, gate Python, Consiglio dei 5). La base di conoscenza su Drive è
strutturata pensando alla messa online delle webapp: non solo documenti, ma
link di staging/produzione, credenziali di accesso ai pannelli (mai le
credenziali stesse, i link ai gestori), stato dei domini.

## Ragione più forte a favore

Un repo condiviso tra un progetto di ricerca psicometrica e un'agenzia di
sviluppo mescolerebbe due cadenze incompatibili: Cicli di validazione lenta
contro Sprint con scadenze di cliente. Tenerli separati evita che le regole
dell'uno contaminino l'altro nel momento sbagliato.

## Rischio più grosso da tenere d'occhio

Duplicazione di manutenzione: due repo, due gate, due protocolli da tenere
aggiornati se emergono miglioramenti comuni. Non c'è oggi un meccanismo di
sincronizzazione tra le due basi di conoscenza infrastrutturale.

## Cosa questa decisione vieta

1. Nessuna sincronizzazione automatica tra questo repo e quello di Motore
   Talento.
2. Nessuna sincronizzazione bidirezionale con Drive.
3. Nessun Ciclo/Sprint chiuso con gate rosso.

## Debito contratto

Nessuno.

## Primo passo

Definire la mappatura Drive (D-003) prima della prima Consegna verso un
committente.

## Cosa la farebbe riaprire

Se emerge un pattern tecnico o di processo utile a entrambe le officine, si
valuta l'estrazione in una base condivisa separata, non l'unione dei due repo.
