---
id: 10-0000
titolo: Scoping — RADAR IA (Prototipo Minimo Verificabile — Catalogo Risorse)
mandato: referente-commessa + stratega-prodotto
commessa: radar-ia
etichetta: N/A
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

> Questo file è la fonte di verità per rispondere in un minuto a "cosa
> abbiamo promesso, cosa abbiamo consegnato, cosa manca" (Definition of Done
> del Referente di Commessa, `90_ufficio/MANDATI.md`). Ogni estensione di
> scope successiva si confronta con quanto scritto qui, non con l'ultima
> richiesta arrivata: è così che si vede lo scostamento cumulativo, non solo
> l'ultimo incremento "ragionevole".

## 0. Domande da porre al committente prima di scrivere questo file

Stato di risposta alle 19 domande a oggi (Sprint 001). Le domande senza
risposta tracciabile restano `[[LACUNA: ...]]` nelle sezioni corrispondenti
e vengono girate al committente — non si inventa.

**Committente e utenti**
1. **[[LACUNA: ragione sociale/settore legale del committente non fornita.
   Utenti finali dichiarati dal committente in termini di pubblico
   (ricercatori, studenti, professionisti, curiosi) ma nessun profilo reale
   circostanziato — es. età media, provenienza, quanti sono oggi]]**
2. **[[LACUNA: livello di alfabetizzazione digitale del pubblico target non
   dichiarato. Assunzione implicita del committente "pubblico competente
   nell'IA" non verificata]]**
3. **[[LACUNA: non è stato chiesto come il pubblico gestisce oggi la
   raccolta di risorse/pratiche IA (fogli sparsi, bookmark, Notion...) né
   perché ora sia il momento giusto]]**

**Scope e priorità**
4. Risposta ricavabile dal mandato del committente: se il CRUD di base
   (aggiungere/visualizzare/segnare "letta/provata" una risorsa) non
   funziona, il Prototipo Minimo Verificabile fallisce — è l'intero
   perimetro dichiarato. Non risulta però una conferma esplicita del
   committente su *questa* singola cosa come criterio di successo/fallimento
   agli occhi suoi — **[[LACUNA: da far confermare esplicitamente]]**.
5. Rispposta parzialmente data dal committente: il perimetro del primo
   Prototipo Minimo Verificabile è stato scelto ed è **limitato al catalogo
   di risorse**, non alla rete/community a regime (vedi §7). Il committente
   non ha ancora specificato in dettaglio *quali* funzionalità della visione
   a regime (rete aperta, community, riproducibilità sperimentale
   verificata, sistema di contributi esterni) siano solo rimandate vs.
   scartate — trattate qui come fuori scope fino a Delibera.
6. **[[LACUNA: nessun competitor o prodotto simile dichiarato dal
   committente come termine di paragone o differenziazione]]**

**Ipotesi di valore e redditività**
7. Non ancora dichiarata dal committente in forma falsificabile.
   `scoping/IPOTESI.md` esiste come template ma è vuoto: **va compilato
   dallo Stratega di Prodotto prima che si apra `30_prototipo/`** (CLAUDE.md
   §4) — blocco esplicito, non solo lacuna informativa.
8. **[[LACUNA: nessuna indicazione dal committente su Data Flywheel /
   superficie ricorrente / nessuna delle due, come richiesto da CLAUDE.md
   §3. La visione a regime ("rete aperta di documentazione... condivisa")
   suggerisce un possibile Data Flywheel implicito (dataset di pratiche/
   esperimenti riproducibili), ma è un'inferenza dell'Officina, non una
   dichiarazione del committente: non va trattata come decisione presa]]**
9. **[[LACUNA: proprietà dei dati generati dall'uso (es. chi ha segnato
   cosa come "letto/provato") non dichiarata, né se il committente intende
   riusarli oltre al servizio]]**

**Vincoli e compliance**
10. **[[LACUNA: categorie di dati personali trattati e base giuridica non
    dichiarate. Nota: se il catalogo prevede utenti registrati (per
    associare "letta/provata" a una persona) si tratta quasi certamente di
    dati personali minimi — email/username — da mappare comunque prima di
    scrivere lo schema dati, non a valle]]**
11. **[[LACUNA: settore regolato non dichiarato esplicitamente. A prima
    vista un catalogo editoriale/educativo su IA non sembra rientrare in
    categorie ad alto rischio, ma non va assunto senza conferma]]**
12. **[[LACUNA: accessibilità (WCAG) non richiesta né esclusa
    esplicitamente, nonostante il pubblico dichiarato includa "curiosi" —
    pubblico ampio che renderebbe l'accessibilità rilevante di default]]**
13. No per il perimetro di questo Prototipo Minimo Verificabile: un CRUD di
    catalogo con stato "letta/provata" non prende decisioni automatizzate su
    persone. Da rivalutare se in futuro si introducono raccomandazioni o
    scoring (fuori scope oggi, vedi §7).
14. Identità visiva (logo, palette, font "Inter") in arrivo dal Designer di
    Prodotto su `70_progetti/radar-ia/prodotto/` — **[[LACUNA: licenza del
    font "Inter" e di eventuali altri asset da verificare dall'Archivista di
    Prodotto prima che entrino in una Consegna, CLAUDE.md §6]]**.
15. Nessuna richiesta del genere risulta finora dal committente. Nessun
    rifiuto da registrare a questo Sprint.

**Budget, tempo, governance della relazione**
16. **[[LACUNA: budget massimo (ore/importo) e scadenza reale non forniti.
    Blocco per il Punto di Decisione #1 in §6: senza questo dato il
    Referente non può valutare uno scostamento cumulativo in termini
    economici, solo funzionali]]**
17. **[[LACUNA: non è chiaro chi, lato committente, ha potere di approvare
    un'estensione di scope. Rilevante in particolare perché — per
    dichiarazione del committente stesso, D-001 in DOMANDE_APERTE.md — il
    committente è anche l'unico utente reale in questa fase: va chiarito se
    la stessa persona che userà il prodotto è anche quella che *decide* le
    estensioni di scope, perché in tal caso il rischio di scope creep
    "silenzioso" auto-richiesto è più alto, non più basso]]**
18. **[[LACUNA: cadenza e forma degli aggiornamenti attesi non dichiarate]]**
19. **[[LACUNA: cosa succede a dati e codice in caso di interruzione
    anticipata non dichiarato]]**

## 1. Committente

RADAR IA — committente descritto come rete aperta di documentazione,
apprendimento e riproducibilità sull'Intelligenza Artificiale, in fase di
avvio ("commessa reale piccola" per calibrare il metodo, D-001 in
DOMANDE_APERTE.md, rischio dichiarato basso). Pubblico dichiarato:
ricercatori, studenti, professionisti, curiosi. `[[LACUNA: ragione sociale,
forma giuridica del committente, profilo reale e alfabetizzazione digitale
del pubblico target — domande 1-2]]`.

## 2. Cosa costruiamo e perché ora

Un catalogo di risorse RADAR IA (pratiche, strumenti, esperimenti
sull'IA) con CRUD semplice — aggiungere, visualizzare, segnare come
"letta/provata" — come Prototipo Minimo Verificabile della visione a
regime di RADAR IA; il "perché ora" specifico non è stato dichiarato dal
committente (`[[LACUNA: domanda 3]]`).

## 3. Ipotesi di Valore

Compilata dallo Stratega di Prodotto in `scoping/IPOTESI.md` (etichetta
DESIGN): il committente, come primo utente reale, alimenterà e consulterà
di propria iniziativa il catalogo per almeno 2-3 settimane senza
sollecitazione. Segnale esplicitamente dichiarato **debole/auto-riferito**
finché il committente resta l'unico utente — servono 3-5 utenti terzi prima
del Punto di Decisione #2 (sviluppo pieno). Il blocco di CLAUDE.md §4 è
quindi sciolto: si può aprire il prototipo su questo perimetro.

## 4. Obiettivo di redditività oltre la fattura (CLAUDE.md §3)

- [ ] Data Flywheel — non confermato dal committente
- [ ] Superficie ricorrente — non confermato dal committente
- [ ] Nessuna delle due — non confermato dal committente

`[[LACUNA: domande 8-9 non risposte. Nessuna delle tre caselle va spuntata
per inferenza. La visione a regime dichiarata dal committente ("rete
aperta... condivisa... riproducibile") è compatibile con un Data Flywheel a
lungo termine, ma per QUESTO Prototipo Minimo Verificabile — un CRUD con
dati reali ma perimetro ridotto — la domanda va comunque posta ora, perché
CLAUDE.md §3 ricorda che è più caro aggiungere l'architettura dati dopo che
progettarla prima]]`.

## 5. Vincoli dichiarati

- **Budget e scadenza**: `[[LACUNA: domanda 16, non fornita]]`.
- **Stack imposto**: nessuno dichiarato dal committente finora.
- **Dati personali trattati**: `[[LACUNA: base giuridica da verificare col
  Custode Normativo — domanda 10; probabile identificazione minima utente
  se lo stato "letta/provata" è personale]]`.
- **Settore regolato / normative note**: `[[LACUNA: domanda 11]]`.
- **Accessibilità richiesta**: `[[LACUNA: domanda 12, rilevante dato il
  pubblico dichiarato include "curiosi"]]`.
- **AI Act**: non applicabile al perimetro CRUD di questo Prototipo Minimo
  Verificabile (nessuna decisione automatizzata su persone). Da riverificare
  se in futuro si introducono raccomandazioni/scoring — presidiato in §7
  come fuori scope.
- **Asset e licenze forniti dal committente**: identità visiva (logo,
  palette #111111/#10B981/#5B4BFF/#F2C94C/#F7F5EE, font "Inter") in arrivo
  su `70_progetti/radar-ia/prodotto/`. `[[LACUNA: verifica licenza a cura
  dell'Archivista di Prodotto non ancora effettuata]]`.
- **Richieste rifiutate per dark pattern**: nessuna a questo Sprint.

## 6. Punti di Decisione previsti

| # | Dopo cosa | Cosa si decide | Data o trigger |
|---|---|---|---|
| 1 | Prototipo Minimo Verificabile (catalogo risorse) | procedi / taglia / ferma | `[[LACUNA: data non fissata, dipende da budget/scadenza non forniti]]` |
| 2 | Prima dello sviluppo pieno (estensione verso la visione a regime RADAR IA) | procedi / taglia / ferma | da definire dopo Punto 1 |
| 3 | Prima del rilascio pubblico | procedi / rinvia | da definire; rilevante soprattutto se si passa da "solo committente come utente" a pubblico esterno reale |

Referente lato committente con potere di decisione: `[[LACUNA: domanda 17,
particolarmente sensibile qui perché committente = utente reale in questa
fase]]`. Cadenza e forma degli aggiornamenti attesi: `[[LACUNA: domanda
18]]`.

## 7. Scope firmato (riferimento per il Referente di Commessa)

Cosa è stato concordato col committente, in modo verificabile a ogni
Sprint. Va tenuto granulare: ogni voce deve poter essere spuntata come
"costruita" o "non costruita" a ogni Sprint, per calcolare lo scostamento
cumulativo — non solo l'ultima estensione.

**Dentro scope (Prototipo Minimo Verificabile — catalogo risorse RADAR IA):**
- Aggiungere una risorsa (pratica, strumento o esperimento sull'IA) al
  catalogo.
- Visualizzare l'elenco delle risorse presenti nel catalogo.
- Segnare una risorsa come "letta/provata".
- Contenuto reale legato a RADAR IA (non dati placeholder/lorem ipsum).
- Complessità tecnica paragonabile a una to-do list (CRUD semplice, single
  utente reale in questa fase — il committente stesso).

**Esplicitamente fuori scope in questa fase** (qualunque estensione qui
sotto richiede una Delibera locale in `70_progetti/radar-ia/delibere/`
prima di diventare codice — veto del Referente di Commessa altrimenti):
- L'intera rete/community aperta a regime di RADAR IA (utenti multipli
  esterni, contributi di terzi, moderazione).
- Funzionalità di "riproducibilità" degli esperimenti (esecuzione,
  verifica, versioning di pratiche/esperimenti) oltre al semplice
  tracciamento di stato "letta/provata".
- Ricerca/filtri avanzati, tag, categorizzazione oltre il minimo
  necessario a un CRUD semplice.
- Autenticazione multi-utente, ruoli, permessi differenziati (il perimetro
  attuale ha il committente come unico utente reale).
- Raccomandazioni, scoring o qualunque logica che prenda decisioni "su
  persone" (rilevanza AI Act, vedi §5).
- Qualunque integrazione con modelli IA lato prodotto (non confuso con
  l'uso di Claude Sonnet 5 / Opus da parte dell'Officina per costruire il
  prodotto, che è strumento interno, non feature del prodotto).
- Pubblicazione pubblica del catalogo verso utenti esterni al committente.

**Dati e continuità**: `[[LACUNA: domanda 19, non dichiarato dal
committente cosa succede a dati e codice in caso di interruzione anticipata
del rapporto]]`.
</content>
