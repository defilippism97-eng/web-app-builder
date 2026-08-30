---
id: 70-radar-ia-repo-0001
titolo: README — repo-app RADAR IA
mandato: sviluppatore-backend + sviluppatore-frontend
commessa: radar-ia
etichetta: N/A
parere_rilascio: non richiesto
stato: approvato
data: 2026-08-30
---

# RADAR IA — prototipo catalogo risorse

Prototipo Minimo Verificabile (vedi `../SCOPING.md` e `../scoping/IPOTESI.md`).
Single-user, senza autenticazione, pensato per girare in locale.

## Avvio

Richiede solo Python 3 (nessuna dipendenza da installare):

```bash
cd 70_progetti/radar-ia/repo-app
python3 server.py
```

Apri http://127.0.0.1:8420 nel browser. Il database SQLite viene creato al
primo avvio in `data/radar.db` (non versionato, vedi `.gitignore`).

## Test

Test automatici sul percorso critico dei 3 endpoint (solo `unittest` della
libreria standard, nessuna dipendenza esterna):

```bash
cd 70_progetti/radar-ia/repo-app
python3 -m unittest test_server -v
```

## Cosa fa (perimetro dichiarato in SCOPING.md §7)

- Aggiungere una risorsa (titolo, url opzionale, tipo, note).
- Vedere l'elenco delle risorse, filtrabile per stato.
- Segnare/togliere lo stato "letta/provata".

Niente altro: niente login, niente ricerca avanzata, niente condivisione
pubblica — sono esplicitamente fuori scope per questa fase.

## Anteprima community (mockup, non ancora attiva)

Con il server avviato, apri http://127.0.0.1:8420/community/index.html (o
segui il link "Anteprima community" in fondo alla pagina del catalogo).
È un mockup statico (DEL-LOCALE-001, `../delibere/DEL-LOCALE-001-mockup-community.md`):
dati d'esempio hardcoded in `static/community/dati.js`, nessuna chiamata di
rete, nessun endpoint nuovo lato server, nessuna interazione sociale reale
(ogni pulsante mostra "In arrivo — questa funzione non è ancora attiva").
Non fa parte del prodotto reale sopra descritto.

## Prima di esporlo fuori dal tuo computer

Questo prototipo **non ha superato** la checklist di sicurezza pre-rilascio
(`../../../60_conoscenza/checklist-rilascio/v0.md`) e non ha autenticazione:
non esporlo su internet così com'è. Va bene solo per l'uso locale che hai
dichiarato in questa fase.
