---
id: 50_compliance-0001
titolo: Parere quadro — base giuridica del trattamento dati e minimizzazione per webapp committenti esterni
mandato: custode
commessa: interno
etichetta: N/A
parere_rilascio: non richiesto
stato: approvato
data: 2026-08-30
---

# Parere quadro — base giuridica e minimizzazione dati

## 0. Cosa è, e cosa non è, questo documento

Questo è un parere **quadro**: uno schema di riferimento ricorrente, non legato
a una commessa specifica, che ogni commessa futura richiama e specializza in
`70_progetti/<slug>/PARERE_RILASCIO.md`. Non sostituisce l'analisi puntuale
richiesta per ogni Consegna reale — la specializza, riducendo il lavoro da
zero a "quali di queste caselle si applicano qui".

Per questo motivo il frontmatter porta `parere_rilascio: non richiesto`: non è
una Consegna verso un committente, è materiale interno (§8 di `CLAUDE.md`).
Il verdetto finale (§7) riguarda l'adeguatezza dello schema stesso, non una
commessa.

Le norme citate sono in evoluzione. Ogni riferimento porta la data di verifica
(2026-08-30). Prima di applicare questo parere a una commessa con
caratteristiche non standard (minori, dati sanitari, dati biometrici,
trasferimenti extra-UE, volumi molto grandi), va fatta una verifica puntuale
aggiuntiva: questo schema copre il caso comune di una webapp business-to-
consumer o business-to-business con dati identificativi e comportamentali
ordinari.

## 1. Basi giuridiche tipiche (GDPR art. 6) — quando usare quale

Per ogni trattamento di dati personali nella webapp deve esistere **una** base
giuridica dichiarata prima di scrivere lo schema dati, non dopo. Le quattro
più rilevanti per le webapp che l'Officina costruisce:

| Base giuridica | Quando si applica | Esempio tipico in una webapp | Attenzione |
|---|---|---|---|
| **Contratto** (art. 6.1.b) | Il dato è necessario per erogare il servizio che l'utente ha richiesto | Email e password per l'account, indirizzo di spedizione per un ordine, dati di fatturazione | Non copre dati "utili ma non necessari" (es. data di nascita per personalizzazione se il servizio funziona senza) |
| **Consenso** (art. 6.1.a) | Il trattamento non è necessario al servizio: marketing, profilazione, cookie non tecnici, condivisione con terzi non necessaria all'erogazione | Newsletter, tracking pubblicitario, raccomandazioni basate su comportamento extra-servizio | Deve essere libero, specifico, informato, inequivocabile; **mai preselezionato** (vedi §4); revocabile con la stessa facilità con cui è dato |
| **Legittimo interesse** (art. 6.1.f) | Il trattamento serve un interesse legittimo del titolare (o di terzi) che non prevale sui diritti dell'utente, e un utente ragionevole se lo aspetterebbe | Prevenzione frodi, sicurezza applicativa, analytics aggregati di prodotto senza profilazione individuale | Richiede un bilanciamento documentato (legitimate interest assessment), non è una scorciatoia per evitare il consenso quando il consenso sarebbe la base corretta |
| **Obbligo legale** (art. 6.1.c) | Una norma impone la conservazione o comunicazione del dato | Conservazione fatture per obblighi fiscali, dati richiesti da autorità | Determina anche il periodo di conservazione minimo, non solo la base |

Regola operativa: **contratto e obbligo legale** coprono il nucleo minimo
funzionale e amministrativo; tutto ciò che va oltre (marketing, profilazione,
condivisione con terzi, funzionalità opzionali) richiede **consenso** o, se
argomentabile e documentato, **legittimo interesse**. Il legittimo interesse
non è mai la base di comodo per evitare la frizione del consenso: se
l'interesse dell'Officina o del committente è più forte del confronto con
l'aspettativa ragionevole dell'utente, la base è sbagliata.

Il Custode verifica, per ogni commessa, che **ogni campo dello schema dati sia
mappato a una di queste quattro basi**, non genericamente "al GDPR".

## 2. Minimizzazione operativa — checklist

Principio (art. 5.1.c GDPR): si raccoglie solo ciò che è adeguato, pertinente
e limitato a quanto necessario. In pratica, per ogni campo dati previsto nello
schema, prima che lo Sviluppatore Backend & Dati lo implementi:

1. **Uso dichiarato**: a quale funzionalità concreta della webapp serve questo
   campo? Se la risposta è "potrebbe servire in futuro" o "è standard
   raccoglierlo", il campo non entra nello schema in questo giro.
2. **Base giuridica**: quale delle quattro di §1 copre questo campo
   specifico? Un campo senza base giuridica dichiarata non entra in
   produzione (Regola di Blocco dello Sviluppatore Backend, `MANDATI.md` §5).
3. **Periodo di conservazione**: per quanto tempo serve? Se non è dichiarato,
   il default è "il tempo minimo per l'uso dichiarato", non "per sempre".
4. **Accesso**: chi, tra i sistemi e le persone coinvolte nella commessa, ha
   accesso a questo campo? Un campo visibile a più ruoli di quanto l'uso
   dichiarato richieda è una violazione di minimizzazione anche se la base
   giuridica è corretta.
5. **Alternativa meno invasiva**: esiste un modo di ottenere lo stesso uso con
   un dato meno identificativo o più aggregato (es. fascia d'età invece di
   data di nascita, evento aggregato invece di log puntuale)? Se sì, si usa
   quella.
6. **Terzi**: il dato viene inviato a un fornitore terzo (analytics, email
   transazionali, pagamenti, hosting)? Se sì, serve un accordo di trattamento
   dati (DPA) con quel fornitore prima che il dato lasci il perimetro
   dell'Officina — verifica a carico del Custode prima del rilascio.

Questa checklist si applica **per ogni campo**, non per lo schema nel suo
insieme: uno schema può avere metà dei campi ben giustificati e metà no, e il
gate blocca solo i secondi, non l'intero schema.

## 3. Accessibilità (WCAG) — quando si applica

Si applica quando dichiarato nello Scoping (§6 di `CLAUDE.md`). In assenza di
un vincolo normativo settoriale specifico del committente (es. pubblica
amministrazione, dove l'accessibilità è spesso obbligatoria per legge
indipendentemente dallo Scoping), la dichiarazione nello Scoping è la fonte
che attiva o meno la verifica. Il Custode segnala allo Stratega di Prodotto se
il pubblico target dichiarato (es. utenza anziana, servizio pubblico,
utenza con disabilità nota) rende l'accessibilità un requisito de facto anche
se il committente non l'ha esplicitata, e lo registra come domanda aperta se
il committente non risponde.

## 4. Dark pattern — vietati sempre, anche su richiesta esplicita

Non negoziabili indipendentemente dalla base giuridica o dal contratto col
committente (§6 di `CLAUDE.md`):

- consenso preselezionato o ottenuto per default (opt-out invece di opt-in
  dove serve consenso);
- costi nascosti o rivelati solo a un passo avanzato del funnel;
- disiscrizione/cancellazione account più complessa dell'iscrizione (numero di
  passaggi, canali richiesti, frizione aggiuntiva);
- linguaggio ambiguo che fa apparire un'azione commerciale come tecnica
  ("continua" che in realtà autorizza un addebito).

Se il committente chiede esplicitamente uno di questi pattern, il Custode
**non lo implementa e non lo fa implementare**: registra il rifiuto motivato
(in `70_progetti/<slug>/PARERE_RILASCIO.md` o in un messaggio verso il
Referente di Commessa) e lascia che sia il Referente, con l'umano, a
comunicarlo al committente. Questo vale anche se il committente minaccia di
annullare la commessa: non è una leva su cui il Custode negozia.

## 5. AI Act — quando si applica, verifica pre-implementazione

Riferimento verificato al 2026-08-30. Lo stato normativo è **in evoluzione**:
un accordo provvisorio sul "Digital Omnibus AI" (Consiglio UE, Parlamento
europeo, Commissione, 7 maggio 2026) ha differito le scadenze per gli obblighi
sui sistemi ad alto rischio Annex III (uso) dal 2 agosto 2026 al 2 dicembre
2027, e quelli Annex I (prodotto regolamentato) dal 2 agosto 2027 al 2 agosto
2028. Questo è un accordo politico provvisorio: **prima di ogni commessa che
coinvolge un sistema potenzialmente ad alto rischio, va verificato lo stato
di adozione formale del testo al momento**, non assunto da questo documento.
Le disposizioni sulle pratiche vietate (art. 5) sono in vigore dal 2 febbraio
2025 e non sono oggetto del differimento.

Verifica da fare **prima dell'implementazione**, non dopo, ogni volta che la
webapp integra un modello che produce un output usato per decidere su una
persona (non solo per assisterla):

1. **La decisione è presa o influenzata da un modello?** Se il modello
   fornisce solo informazione che un umano valuta liberamente e può ignorare
   senza costo, il rischio è più basso; se il modello determina o orienta
   fortemente un esito (accesso a un servizio, prezzo personalizzato,
   punteggio, priorità in una coda, moderazione di contenuti con effetti su
   un account), il rischio sale.
2. **Rientra in una pratica vietata (art. 5)?** Es. manipolazione subliminale,
   sfruttamento di vulnerabilità, scoring sociale, categorizzazione biometrica
   per inferire dati sensibili. Se sì: non si implementa, punto, nessuna
   condizione possibile.
3. **Rientra in una categoria ad alto rischio (Annex III)?** Es. selezione del
   personale, accesso a servizi essenziali, valutazione di affidabilità
   creditizia, alcuni usi in ambito educativo o sanitario. Se sì: obblighi di
   trasparenza, documentazione tecnica, supervisione umana e, secondo il
   calendario post-Omnibus da riverificare al momento, un termine di
   adeguamento — ma l'obbligo di **non trattare la scadenza differita come
   licenza di costruire senza presidio nel frattempo**: il Custode può comunque
   richiedere le stesse garanzie come Debito di Rischio con scadenza propria,
   indipendente dal calendario normativo.
4. **Se il modello non decide su persone** (es. suggerimenti di
   categorizzazione interna, estrazione dati da PDF per uso interno
   all'Officina, sintesi di reportistica non esposta all'utente finale con
   effetti su di lui) l'AI Act non si applica nella sua parte più stringente,
   ma restano gli obblighi di trasparenza generali se il committente lo
   comunica come "assistito da IA" ai propri utenti.

Il Custode verifica questa casistica **prima** che l'Architetto scelga come
integrare il modello (§6 di `CLAUDE.md`: "prima di implementare, non dopo").

## 6. Quando serve una DPIA (Data Protection Impact Assessment)

Una DPIA (art. 35 GDPR) è richiesta prima di avviare un trattamento quando è
probabile un rischio elevato per i diritti delle persone. Indicatori che
attivano la verifica per una commessa dell'Officina (non serve che ricorrano
tutti):

- **Profilazione o scoring** con effetti legali o significativi su una
  persona (incluso l'uso di un modello come in §5.1);
- **Monitoraggio sistematico** su larga scala di un'area accessibile al
  pubblico o del comportamento degli utenti (tracking comportamentale esteso,
  non semplice analytics aggregata);
- **Dati sensibili su larga scala** (art. 9: salute, origine etnica,
  orientamento sessuale, opinioni politiche/religiose, dati biometrici o
  genetici) o **dati relativi a condanne penali**;
- **Combinazione o incrocio di dataset** provenienti da trattamenti diversi
  oltre le aspettative ragionevoli dell'utente;
- **Dati di soggetti vulnerabili** (minori, dipendenti in contesti di
  monitoraggio, pazienti);
- **Nuove tecnologie** o usi innovativi su larga scala di cui non esiste
  ancora prassi consolidata.

Se anche uno solo di questi indicatori è presente in modo non trascurabile,
il Custode apre la valutazione prima dello sviluppo pieno (non al Punto di
Decisione successivo): la DPIA, se necessaria, è un artefatto di
`70_progetti/<slug>/`, non di questo parere quadro.

## 7. Cosa non è mai delegabile a un agente

Rimando diretto a `CLAUDE.md` §10, che questo parere non ripete ma richiama
come vincolante senza eccezioni per ogni commessa che tratta dati personali:
firma del contratto e negoziazione economica col committente; comunicazione
di un problema grave o di uno sforamento al committente; accettazione di un
rischio di compliance oltre la scadenza del Debito di Rischio; qualunque
rilascio in produzione con dati reali di utenti finché il Custode non ha
firmato; decisione finale su pivot o interruzione di una commessa. Nessun
agente, incluso questo, può auto-autorizzarsi su questi punti.

## 8. Come una commessa usa questo parere

1. Nello Scoping, la commessa elenca i campi dati previsti e per ciascuno
   applica la checklist di §2.
2. Il Custode compila `70_progetti/<slug>/PARERE_RILASCIO.md` richiamando le
   sezioni pertinenti di questo documento (es. "base giuridica: vedi §1,
   contratto per i campi X, Y; consenso per Z") invece di riscrivere lo schema
   da zero.
3. Ogni scostamento dallo schema qui descritto (es. una base giuridica non tra
   le quattro elencate, un caso limite di minimizzazione) va argomentato per
   iscritto nel parere della commessa, non risolto per analogia silenziosa.
4. Questo parere quadro va rivisto quando cambia in modo sostanziale lo stato
   normativo citato in §5 (AI Act) o a ogni manutenzione quinquennale dello
   Sprint (`PROTOCOLLO.md` §7), quale dei due arriva prima.

## 9. Verdetto

Questo parere quadro definisce uno schema di riferimento coerente con la
gerarchia di `CLAUDE.md` §1 e con i vincoli sempre attivi di §6: basi
giuridiche mappate per uso, minimizzazione verificabile per campo, dark
pattern esclusi senza eccezioni, verifica AI Act pre-implementazione, criteri
DPIA espliciti. È utilizzabile da ogni commessa futura come punto di partenza,
a condizione che ogni specializzazione per una commessa reale sia scritta e
non assunta per analogia.

**FIRMATA**
