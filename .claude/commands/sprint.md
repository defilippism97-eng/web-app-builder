---
description: Esegue uno Sprint dell'Officina su tutte le commesse attive
---

Esegui uno Sprint come Regista, seguendo 90_ufficio/PROTOCOLLO.md §2.

1. Leggi CLAUDE.md, STATO.md, DOMANDE_APERTE.md, GLOSSARIO.md, e lo
   STATO_COMMESSA.md di ogni commessa attiva in 70_progetti/. Riparti dai
   file, non da ciò che ricordi.
2. Per ogni commessa, verifica se ha raggiunto il prossimo Punto di Decisione
   dichiarato in SCOPING.md. Se sì, sospendi il lavoro tecnico su quella
   commessa: il Referente di Commessa prepara il Punto di Decisione, non si
   procede oltre senza risposta umana.
3. Sulle commesse non sospese, scegli al massimo tre task ciascuna (nove
   totali), rispettando le dipendenze.
4. Delega in parallelo ai subagenti competenti, passando task, file da
   leggere, artefatto atteso, Definition of Done del mandato.
5. Esegui `python strumenti/controllo_rigore.py`. Applica la gerarchia dei
   veti: compliance (Custode) → scope/budget (Referente) → rilascio
   (DevOps) → fonti/licenze (Archivista) → assenza di Ipotesi di Valore
   (Stratega di Prodotto). Non chiudere con gate rosso.
6. Aggiorna STATO.md e gli STATO_COMMESSA.md toccati, più i registri di
   debito pertinenti.
7. Commit `sprint NNN: <sintesi per commessa>`.
8. Riporta in chat, in massimo quindici righe: cosa è avanzato per quale
   commessa, quali commesse sono ferme e perché, quali Punti di Decisione
   attendono l'umano.

Se è stato passato un argomento a questo comando, usalo come priorità dello
Sprint: $ARGUMENTS
