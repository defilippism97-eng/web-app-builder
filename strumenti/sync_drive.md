# Sincronizzazione verso Drive

**Git è la fonte di verità. Drive è uno specchio in sola lettura**, pensato
per due pubblici diversi da quello di Motore Talento: l'umano che supervisiona
l'Officina, e — indirettamente, tramite export preparati dal Referente di
Commessa — il committente che vuole vedere lo stato del proprio progetto senza
toccare il repo.

## Cosa si specchia, e dove

| Repo | Drive | Chi lo legge |
|---|---|---|
| `STATO.md` | radice | supervisione interna |
| `00_delibere/` (ambito: officina) | `Decisioni-Officina/` | interno |
| `60_conoscenza/` | `Base-di-Conoscenza/` | interno, riuso tra commesse |
| `70_progetti/<slug>/SCOPING.md`, `STATO_COMMESSA.md` | `Clienti/<slug>/` | interno + export per il committente |
| `70_progetti/<slug>/PUNTO_DECISIONE_*.md` | `Clienti/<slug>/Decisioni/` | interno, propedeutico alla comunicazione col cliente |
| `70_progetti/<slug>/prodotto/BRAND.md` e asset approvati | `Clienti/<slug>/Brand/` | interno + committente su condivisione esplicita |
| Link di staging/produzione (non le credenziali) | `Clienti/<slug>/Ambienti.md` | interno |

## Cosa non si specchia mai

Bozze (`stato: bozza`), `90_ufficio/messaggi/`, codice in
`70_progetti/<slug>/repo-app/` (sta su git, eventualmente su un repo separato
per commessa se il committente richiede accesso diretto al codice),
`.claude/`, qualunque segreto o credenziale — quelli restano in un gestore di
segreti, mai su Drive nemmeno come specchio.

## Procedura

1. `python strumenti/controllo_rigore.py` — gate verde obbligatorio.
2. Filtrare per `stato: approvato` o `consegnato`.
3. Per ogni commessa, verificare che nessun artefatto con `parere_rilascio:
   non firmata` sia tra quelli da sincronizzare.
4. Caricare sostituendo, mai fondendo.
5. Se la sincronizzazione prepara materiale da condividere col committente,
   il Referente di Commessa lo segnala esplicitamente: la condivisione
   effettiva resta una decisione umana (CLAUDE.md §10).

## Messa online

Per ogni Consegna che va in produzione, `70_progetti/<slug>/Ambienti.md`
(specchiato) riporta: URL di staging, URL di produzione, provider di hosting,
stato del dominio, data dell'ultima checklist di sicurezza superata. Non
riporta mai credenziali: solo link ai pannelli di gestione, l'accesso agli
stessi passa dai canali già in uso, non da Drive.

## Da completare

`[[LACUNA: la convenzione di naming delle cartelle Clienti/<slug>/ su Drive
non è ancora stata verificata con la struttura Drive esistente. Va confermata
prima della prima Consegna reale — si veda D-003]]`
