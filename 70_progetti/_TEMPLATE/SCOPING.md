---
id: 10-0000
titolo: Scoping — <nome commessa>
mandato: referente-commessa + stratega-prodotto
commessa: <slug>
etichetta: N/A
parere_rilascio: non richiesto
stato: bozza
data:
---

> Questo file è la fonte di verità per rispondere in un minuto a "cosa
> abbiamo promesso, cosa abbiamo consegnato, cosa manca" (Definition of Done
> del Referente di Commessa, `90_ufficio/MANDATI.md`). Ogni estensione di
> scope successiva si confronta con quanto scritto qui, non con l'ultima
> richiesta arrivata: è così che si vede lo scostamento cumulativo, non solo
> l'ultimo incremento "ragionevole".

## 0. Domande da porre al committente prima di scrivere questo file

Non compilare le sezioni sottostanti per inferenza: ogni voce sotto dovrebbe
avere una risposta tracciabile a una di queste domande (verbale, email,
call), non un'assunzione dell'Officina. Se una domanda non ha risposta,
si marca `[[LACUNA: ...]]` nella sezione corrispondente, non si inventa.

**Committente e utenti**
1. Chi è il committente legalmente (ragione sociale, settore)? Chi, in
   concreto, userà la webapp — non "gli utenti" in astratto ma un profilo
   reale?
2. Che livello di alfabetizzazione digitale ha il pubblico target? (serve
   al quarto seggio del Consiglio, l'Utente Reale)
3. Oggi, senza questa webapp, come risolvono lo stesso problema? Cosa rende
   *ora* il momento giusto per cambiare?

**Scope e priorità**
4. Qual è la singola cosa che, se non funzionasse, renderebbe l'intera
   commessa un fallimento agli occhi del committente?
5. Cosa è esplicitamente FUORI scope in questa fase, anche se "sarebbe
   comodo averlo"? (va scritto tanto quanto il dentro-scope: è la base su
   cui il Referente eserciterà il veto sulle estensioni non deliberate)
6. Esiste già un termine di paragone (competitor, prodotto simile) a cui il
   committente si aspetta somigliamo o da cui vogliamo differenziarci?

**Ipotesi di valore e redditività**
7. Qual è l'assunzione più rischiosa su cui si regge il progetto — quella
   che, se falsa, dovrebbe far fermare tutto? (alimenta
   `scoping/IPOTESI.md`)
8. Il committente immagina un ritorno oltre la fattura una tantum — dati
   che generano valore nel tempo, un modello ricorrente — o è una consegna
   singola? (CLAUDE.md §3: la risposta va dichiarata esplicitamente anche
   se è "nessuna delle due")
9. Chi possiede i dati generati dall'uso della webapp? Il committente li
   userà per altro oltre al servizio dichiarato agli utenti finali?

**Vincoli e compliance (CLAUDE.md §6, da chiedere sempre, non solo se il
settore sembra regolato)**
10. Che tipo di dati personali tratterà la webapp (categorie: anagrafici,
    sanitari, finanziari, minori, geolocalizzazione...)? Su quale base
    giuridica il committente intende trattarli?
11. Il committente opera in un settore regolato (sanità, finanza, minori,
    pubblica amministrazione)? Ci sono normative di settore note fin da ora?
12. È richiesta l'accessibilità (WCAG) per legge o per pubblico target?
13. La webapp integrerà modelli che prendono decisioni su persone (scoring,
    raccomandazioni con effetti su persone, moderazione)? Se sì, va
    verificata la categoria di rischio AI Act prima di implementare.
14. Il committente fornisce asset (loghi, testi, immagini, font, librerie)?
    Con quale licenza? Chi verifica che siano effettivamente suoi da
    concedere?
15. Ci sono richieste esplicite del committente che assomigliano a dark
    pattern (consenso preselezionato, disiscrizione complicata, costi
    nascosti fino al checkout)? Se sì, si registra qui il rifiuto motivato:
    non si eseguono anche se richieste (CLAUDE.md §6).

**Budget, tempo, governance della relazione**
16. Qual è il budget massimo (ore o importo) e la scadenza reale, non
    aspirazionale? Cosa succede se si sfora l'uno o l'altra?
17. Chi, lato committente, ha davvero potere di approvare un'estensione di
    scope o una spesa aggiuntiva? È la stessa persona con cui parliamo di
    solito?
18. Con quale cadenza il committente si aspetta un aggiornamento, e in quale
    forma (demo, report scritto, call)?
19. Cosa succede ai dati e al codice se il rapporto si interrompe prima
    della fine prevista?

## 1. Committente

Ragione sociale, settore, chi sono gli utenti finali. Livello di
alfabetizzazione digitale del pubblico target (domanda 2).

## 2. Cosa costruiamo e perché ora

Una frase. Se non sta in una frase, lo scope non è ancora chiaro abbastanza
per iniziare. (domande 3-4)

## 3. Ipotesi di Valore

Rinvio a `scoping/IPOTESI.md`. Deve esistere prima di aprire `30_prototipo/`
per questa commessa (o l'equivalente `repo-app/`). Riporta qui solo
l'assunzione centrale in una riga (domanda 7) e il link al file.

## 4. Obiettivo di redditività oltre la fattura (CLAUDE.md §3)

- [ ] Data Flywheel — descrivere il meccanismo e chi possiede il dato
- [ ] Superficie ricorrente — descrivere il modello
- [ ] Nessuna delle due — consegna singola, valore = la fattura

(domande 8-9)

## 5. Vincoli dichiarati

- **Budget e scadenza**: importo/ore massime, data limite e perché è reale
  (domanda 16).
- **Stack imposto** dal committente, se presente.
- **Dati personali trattati**: categorie e base giuridica dichiarata
  (domanda 10). Se non ancora chiaro: `[[LACUNA: base giuridica da
  verificare col Custode Normativo]]`.
- **Settore regolato / normative note**: sì/no, quali (domanda 11).
- **Accessibilità richiesta**: sì/no, standard (domanda 12).
- **AI Act**: la webapp prende decisioni su persone? Se sì, categoria di
  rischio da verificare prima di implementare (domanda 13).
- **Asset e licenze forniti dal committente**: elenco e stato di verifica
  da parte dell'Archivista di Prodotto (domanda 14).
- **Richieste rifiutate per dark pattern**: elenco motivato, se presenti
  (domanda 15).

## 6. Punti di Decisione previsti

| # | Dopo cosa | Cosa si decide | Data o trigger |
|---|---|---|---|
| 1 | Prototipo Minimo Verificabile | procedi / taglia / ferma | |
| 2 | Prima dello sviluppo pieno | procedi / taglia / ferma | |
| 3 | Prima del rilascio pubblico | procedi / rinvia | |

Referente lato committente con potere di decisione (domanda 17); cadenza e
forma degli aggiornamenti attesi (domanda 18).

## 7. Scope firmato (riferimento per il Referente di Commessa)

Cosa è stato concordato col committente, in modo verificabile a ogni
Sprint. Va tenuto granulare: ogni voce deve poter essere spuntata come
"costruita" o "non costruita" a ogni Sprint, per calcolare lo scostamento
cumulativo — non solo l'ultima estensione.

**Dentro scope:**
-

**Esplicitamente fuori scope in questa fase** (domanda 5):
-

**Dati e continuità** (domanda 19): cosa succede a dati/codice in caso di
interruzione anticipata del rapporto.
