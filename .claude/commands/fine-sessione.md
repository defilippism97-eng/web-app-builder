---
description: Manutenzione periodica dopo cinque Sprint
---

Esegui la manutenzione di 90_ufficio/PROTOCOLLO.md §7.

1. Compatta STATO.md e ogni STATO_COMMESSA.md attivo.
2. Rileggi GLOSSARIO.md, verifica che non siano entrati sinonimi.
3. Verifica che nessun claim commerciale sia salito di etichetta senza fonte.
4. Per ogni commessa, controlla DEBITO_RISCHIO.md: segnala ogni voce scaduta,
   non estinta, e ricorda che il Custode può sospendere la Consegna successiva
   finché non è estinta.
5. Ricontare le LACUNA aperte, confrontare con la sessione precedente.
6. Aggiorna 60_conoscenza/ con pattern, checklist ed errori emersi dalle
   commesse toccate: ogni commessa chiusa lascia almeno una voce.
7. Esegui `python strumenti/controllo_rigore.py --report` e allega l'esito.
8. Prepara la sincronizzazione verso Drive secondo strumenti/sync_drive.md,
   includendo i link di staging/produzione delle webapp consegnate.

Chiudi con un rapporto di sessione di venti righe al massimo, aperto dalle
decisioni che servono all'umano.
