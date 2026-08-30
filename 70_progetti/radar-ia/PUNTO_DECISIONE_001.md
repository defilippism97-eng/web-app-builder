---
id: 70-radar-ia-0002
titolo: Punto di Decisione 001 — richiesta committente di estendere a community multi-utente
mandato: referente-commessa
commessa: radar-ia
etichetta: N/A
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

> Bozza per l'umano (Regista / persona che tiene la relazione col
> committente). Non è un messaggio pronto da inviare al committente:
> è materiale di lavoro per prendere e comunicare una decisione.
> Nessuna riga di questo file autorizza da sola l'avvio di sviluppo.

### Punto di Decisione — radar-ia, richiesta di estensione a community multi-utente

**COSA ABBIAMO IMPARATO, con fonte:**
- Il committente ha chiesto (comunicazione riportata al Referente, Sprint
  corrente) di espandere la visione: community dove condividere esperienze
  sull'IA e sul lavoro, sul vibe coding, su esperimenti; condividere
  opinioni; unirsi al progetto di qualcun altro; chiedere aiuto per il
  proprio progetto.
- Questa richiesta corrisponde, voce per voce, a quanto elencato in
  `SCOPING.md` §7 come **esplicitamente fuori scope in questa fase**:
  "l'intera rete/community aperta a regime... utenti multipli esterni,
  contributi di terzi, moderazione" e "autenticazione multi-utente, ruoli,
  permessi differenziati". Non è un'estensione ai margini del prototipo
  attuale, è la visione a regime che lo Scoping aveva già isolato e
  rimandato.
- `scoping/IPOTESI.md`, Punto di Decisione #2, condiziona esplicitamente lo
  sviluppo pieno (di cui la community è il nucleo) a un Segnale da almeno
  3-5 utenti terzi reali, con uso spontaneo misurato per 2-3 settimane, non
  ancora raccolto. Ad oggi il committente resta l'unico utente del
  prototipo, consegnato in questo stesso Sprint: il Segnale del Punto di
  Decisione #1 (2 settimane di uso spontaneo da parte del committente) non
  ha ancora avuto il tempo di manifestarsi, tantomeno quello più forte
  richiesto per il #2.
- Nessuna Delibera locale esiste oggi in `70_progetti/radar-ia/delibere/`
  (cartella vuota) che autorizzi questa estensione: per mandato del
  Referente di Commessa (`90_ufficio/MANDATI.md`) e per la gerarchia dei
  veti (`PROTOCOLLO.md` §4), questa richiesta non può diventare codice senza
  passare prima da qui.
- Lettura sullo scostamento cumulativo (non solo l'ultima richiesta): a
  questo Sprint lo scope costruito coincide ancora con lo scope firmato
  (CRUD catalogo, single-user). Questa è la **prima** richiesta di
  estensione ricevuta. Segnalarla ora, prima che diventi lavoro tecnico,
  è esattamente il presidio contro lo scostamento cumulativo silenzioso:
  se la si accogliesse implicitamente "perché il cliente è contento e
  chiede solo un po' di più", il prototipo del Sprint 001 smetterebbe di
  essere il perimetro di riferimento senza che nessuno l'abbia deciso
  esplicitamente.

**COSA COSTEREBBE PROSEGUIRE (stima di ordine di grandezza):**
- Budget dichiarato per l'intera commessa finora: equivalente di **due
  sessioni Claude Pro, Sonnet 5, ragionamento medio** (SCOPING.md §5) — un
  vincolo di compute stretto, pensato e già in parte consumato per il
  Prototipo Minimo Verificabile a singolo utente.
- La community richiesta implica, come minimo: autenticazione e gestione
  utenti multipli, un modello dati e permessi per contenuti di terzi
  (opinioni, richieste di aiuto, progetti condivisi), moderazione (anche
  minima) dei contenuti generati da altri utenti, e ricadute dirette su
  compliance/privacy (dati personali multi-utente, base giuridica del
  trattamento, moderazione = responsabilità editoriale) che oggi in
  `SCOPING.md` §5 sono ancora `[[LACUNA]]` non chiarite nemmeno per il
  singolo utente. Si tratta di uno sviluppo di ordine di grandezza
  superiore al budget rimasto stimato per questa commessa, non un
  incremento marginale.
- Il Custode Normativo dovrebbe essere coinvolto prima di qualunque riga di
  codice (base giuridica multi-utente, moderazione, eventuale AI Act se in
  futuro si aggiungono suggerimenti/matching tra progetti) — costo
  aggiuntivo non ancora stimato, ma sicuramente non nullo.

**OPZIONI:**
1. **Procedi come da scope attuale** — non si tocca nulla lato prodotto ora.
   Si raccoglie prima il Segnale del Prototipo Minimo Verificabile così
   com'è (2-3 settimane di uso spontaneo del committente, come da
   `scoping/IPOTESI.md`), poi — solo con quel Segnale, e idealmente con i
   3-5 utenti terzi richiesti per il Punto di Decisione #2 — si rivaluta
   l'estensione verso la community con dati reali invece che con
   entusiasmo per l'idea.
2. **Taglia lo scope** — il committente autorizza ORA, con una Delibera
   locale in `70_progetti/radar-ia/delibere/`, un ampliamento *limitato e
   specifico* del prototipo attuale che resta single-user: ad esempio un
   campo libero "opinione/nota" collegato a ogni risorsa del catalogo,
   visibile solo al committente stesso, per iniziare a far emergere
   l'interesse per la dimensione "condivisione di opinioni" senza
   costruire autenticazione, utenti terzi o moderazione. Nessuna delle
   voci "fuori scope" di `SCOPING.md` §7 verrebbe toccata: resterebbe un
   CRUD esteso, non una community.
3. **Ferma il prototipo attuale e riparti da uno Scoping nuovo** per la
   visione community, trattata come commessa o fase distinta con
   `SCOPING.md`, budget e Ipotesi di Valore proprie (probabilmente non
   coperta dal budget di due sessioni Claude Pro già dichiarato, che è
   stato dimensionato per un CRUD a singolo utente, non per un sistema
   multi-utente con moderazione).

**RACCOMANDAZIONE:**
Opzione 1, con Opzione 2 come alternativa accettabile se il committente ha
bisogno di un segnale concreto in tempi brevi sulla dimensione
"condivisione" prima di aspettare 2-3 settimane. Motivo: la richiesta del
committente corrisponde punto per punto a ciò che lo Scoping aveva già
isolato come fuori scope e condizionato a un Segnale non ancora raccolto —
non è una scoperta nuova, è la visione originaria del committente
("rete aperta di documentazione, apprendimento e riproducibilità") che
torna a farsi sentire prima che il prototipo abbia avuto il tempo di essere
usato. Non c'è ancora nessun dato — nemmeno il debole Segnale auto-riferito
del solo committente — che indichi che vale la pena investire nella
community. Costruirla ora userebbe la maggior parte del budget residuo
senza aver verificato l'ipotesi più economica (il catalogo semplice) e
saltando esplicitamente il Punto di Decisione #2 già scritto e concordato.
L'Opzione 2 è preferibile all'Opzione 3 se il committente vuole comunque
un segnale di interesse ora, perché resta dentro il budget dichiarato e
non richiede un nuovo Scoping.
L'Opzione 3 va scelta solo se il committente conferma esplicitamente di
voler saltare la validazione con il prototipo attuale: in tal caso va
trattata con trasparenza come un nuovo impegno economico, non come
"continuazione" della commessa presente.

**RISCHI SE NON SI DECIDE ORA:**
- Se si lascia che la richiesta scivoli in mandati tecnici (Architetto,
  Sviluppatore) senza passare da qui, si crea esattamente lo scostamento
  cumulativo silenzioso che il mandato del Referente è tenuto a
  intercettare: una serie di estensioni "ragionevoli" — prima un campo,
  poi un secondo utente per provare, poi un sistema di commenti — che
  sommate ricostruiscono l'intera community senza che nessuna singola
  decisione l'abbia mai autorizzata esplicitamente.
- Il committente, avendo *espresso* l'aspettativa di una community, potrebbe
  ragionevolmente credere che sia già in corso di realizzazione se
  l'Officina non gli comunica chiaramente che si tratta di una fase/
  decisione separata: il rischio non è tecnico, è di relazione — un
  disallineamento di aspettative che emerge tardi è più costoso di uno
  affrontato ora con un Punto di Decisione esplicito.
- Il budget dichiarato (due sessioni Claude Pro) è già stretto per il solo
  prototipo consegnato: iniziare a costruire pezzi di community senza una
  decisione esplicita rischia di consumare il budget residuo su una
  direzione non validata, lasciando meno margine anche per completare bene
  il perimetro già firmato (contenuti reali, eventuale rifinitura del
  catalogo).
- Compliance: qualunque frammento di multi-utente o contenuto di terzi
  introdotto "per provare" prima di una decisione esplicita del Custode
  Normativo aggirerebbe la gerarchia dei veti di `PROTOCOLLO.md` §4 (il
  Custode ha rango superiore al Referente ma va comunque interpellato prima,
  non dopo, per compliance/privacy multi-utente).
