# Avvio da desktop

## 1. Installare Claude Code

Serve un piano Pro, Max, Team, Enterprise o un account Console.

**macOS / Linux**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows**: installare Git for Windows (fornisce Bash) oppure usare WSL e
lanciare `claude` dal terminale WSL. Riferimento:
`https://code.claude.com/docs/en/setup`.

Verifica:
```bash
claude --version
claude doctor
```

## 2. Mettere il repo al suo posto

Questo repo è **indipendente da Motore Talento**: cartella separata, non
sottocartella.

```bash
unzip officina-web.zip
cd officina-web
git init && git add -A && git commit -m "sprint 000: struttura dell'Officina"
python3 strumenti/controllo_rigore.py     # deve dare GATE VERDE
```

## 3. Prima sessione

```bash
claude
```
poi
```
/sprint
```

Verifica che gli undici subagenti siano visibili (`/agents`) e i tre comandi
rispondano (`/sprint`, `/consiglio`, `/fine-sessione`). Le definizioni sono in
`.claude/`, relative alla cartella di lavoro: lancia `claude` **dentro**
`officina-web/`.

## 4. Prima di aprire la prima commessa reale

Rispondi a D-001 in `DOMANDE_APERTE.md` (commessa reale, simulata, o reale ma
piccola) e a D-002 (stack di default, va deciso in Consiglio perché vale per
tutte le commesse future). Lo Sprint 001 prepara il terreno (template di
scoping, checklist di sicurezza, parere quadro sui dati, primi pattern
riusabili) prima che serva davvero per un cliente.

Per aprire una nuova commessa:
```bash
cp -r 70_progetti/_TEMPLATE 70_progetti/<slug-cliente>
```
poi si compila `SCOPING.md` e `scoping/IPOTESI.md` prima di qualunque riga di
codice.

## 5. Ritmo consigliato

3-4 Sprint per sessione, poi `/fine-sessione`. Ogni commessa che raggiunge un
Punto di Decisione si ferma automaticamente: la tua manutenzione principale
tra una sessione e l'altra è rispondere a quei Punti di Decisione, non gestire
lo stato a mano.

## 6. Prima di consegnare qualcosa a un committente

```bash
python3 strumenti/controllo_rigore.py
```
Gate verde, `parere_rilascio: firmata` sull'artefatto, checklist di sicurezza
di DevOps superata se va in produzione. Nessuna eccezione per fretta di
scadenza: è il vincolo che l'intero metodo esiste per proteggere.
