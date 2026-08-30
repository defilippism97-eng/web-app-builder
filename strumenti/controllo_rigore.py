#!/usr/bin/env python3
"""Gate di rigore dell'Officina.

Applica la gerarchia di CLAUDE.md §1: compliance/privacy/etica prima di
scope/budget, prima di qualita'/sicurezza tecnica, prima di validazione della
domanda. Se piu' violazioni coesistono, il rapporto le ordina per rango, non
per ordine di scoperta nel filesystem.

Uso:
    python strumenti/controllo_rigore.py            # gate, esce 1 se errori
    python strumenti/controllo_rigore.py --report   # rapporto, esce sempre 0
"""

import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINI = ["10_scoping", "20_prodotto", "30_prototipo", "40_go-to-market", "50_compliance"]
CAMPI = ["id", "titolo", "mandato", "commessa", "etichetta", "parere_rilascio", "stato", "data"]
ETICHETTE = ["VALIDATO", "DESIGN", "DA VERIFICARE", "N/A"]
PARERI = ["non richiesto", "in attesa", "firmata", "firmata con condizioni", "non firmata"]

# Rango 1: compliance/privacy/etica — il piu' alto.
RANGO1_VIETATE = {
    r"per\s+ora\s+va\s+bene\s+cos[iì]": "deroga a compliance/sicurezza vietata da CLAUDE.md §6",
    r"consenso\s+preselezionat\w+": "dark pattern esplicitamente vietato",
    r"lo\s+implementiamo\s+e\s+vediamo": "manca l'Ipotesi di Valore dichiarata (§4), ma se applicato a dati/sicurezza e' rango 1",
}
RE_PARERE_NON_FIRMATA = re.compile(r"parere_rilascio:\s*non firmata", re.I)

# Rango 4: assenza di Ipotesi di Valore.
RE_IPOTESI_MANCANTE_TRIGGER = re.compile(
    r"\b(funzionalit[aà]\s+nuova|nuova\s+feature)\b", re.I
)

RE_PERCENTUALE = re.compile(r"\b\d{1,3}(?:[.,]\d+)?\s*(?:[-–]\s*\d{1,3}(?:[.,]\d+)?\s*)?%")
RE_ETICHETTA_RIGA = re.compile(r"\[(VALIDATO|DESIGN|DA VERIFICARE)\]")
RE_LACUNA = re.compile(r"\[\[LACUNA:((?:[^\]]|\](?!\]))*)\]\]", re.S)

# rango -> lista di messaggi
per_rango = {1: [], 2: [], 3: [], 4: []}
avvisi = []
lacune = []


def leggi(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def frontmatter(testo):
    if not testo.startswith("---"):
        return None
    fine = testo.find("\n---", 3)
    if fine == -1:
        return None
    blocco = testo[3:fine]
    dati = {}
    for riga in blocco.splitlines():
        if ":" in riga:
            k, v = riga.split(":", 1)
            dati[k.strip()] = v.strip()
    return dati


def file_markdown():
    for cartella, _, nomi in os.walk(RADICE):
        if any(p in cartella for p in (".git", "node_modules")):
            continue
        for nome in nomi:
            if nome.endswith(".md"):
                yield os.path.join(cartella, nome)


def relativo(p):
    return os.path.relpath(p, RADICE)


def e_governo(rel):
    """File che devono poter nominare cio' che vietano senza far scattare il gate."""
    base = os.path.basename(rel)
    if rel in ("CLAUDE.md", "GLOSSARIO.md", "STATO.md", "DOMANDE_APERTE.md"):
        return True
    if rel.startswith(".claude" + os.sep):
        return True
    if base.startswith("_TEMPLATE"):
        return True
    if os.sep + "_TEMPLATE" + os.sep in os.sep + rel or rel.startswith("_TEMPLATE" + os.sep):
        return True
    if os.sep + "00_delibere" + os.sep in os.sep + rel or rel.startswith("00_delibere" + os.sep):
        return True
    if base.startswith("DEBITO_") or base == "PUNTO_DECISIONE_TEMPLATE.md":
        return True
    return False


def controlla(percorso):
    rel = relativo(percorso)
    testo = leggi(percorso)
    in_dominio = any(rel.startswith(d + os.sep) for d in DOMINI) or rel.startswith(
        "70_progetti" + os.sep
    )
    governo = e_governo(rel)

    fm = frontmatter(testo)
    if in_dominio and not governo:
        if fm is None:
            per_rango[3].append(f"{rel}: frontmatter assente (CLAUDE.md §8)")
        else:
            mancanti = [c for c in CAMPI if c not in fm]
            if mancanti:
                per_rango[3].append(f"{rel}: campi mancanti: {', '.join(mancanti)}")
            et = fm.get("etichetta", "")
            if et and et not in ETICHETTE:
                per_rango[3].append(f"{rel}: etichetta '{et}' non ammessa")
            par = fm.get("parere_rilascio", "")
            if par and par not in PARERI:
                per_rango[1].append(f"{rel}: parere_rilascio '{par}' non ammesso")
            if par == "non firmata":
                per_rango[1].append(
                    f"{rel}: parere_rilascio = non firmata — Consegna bloccata, veto del Custode attivo"
                )

    if not governo:
        for n, riga in enumerate(testo.splitlines(), 1):
            for pattern, motivo in RANGO1_VIETATE.items():
                if re.search(pattern, riga, re.I):
                    per_rango[1].append(f"{rel}:{n}: {motivo}")

            if in_dominio:
                if RE_PERCENTUALE.search(riga) and not RE_ETICHETTA_RIGA.search(riga):
                    if not (fm and fm.get("etichetta") == "VALIDATO"):
                        avvisi.append(f"{rel}:{n}: numero senza etichetta di rigore")

    if not governo:
        for m in RE_LACUNA.finditer(testo):
            n = testo.count("\n", 0, m.start()) + 1
            lacune.append(f"{rel}:{n}: {' '.join(m.group(1).split())[:70]}")


def main():
    report = "--report" in sys.argv
    for p in file_markdown():
        controlla(p)

    NOMI_RANGO = {
        1: "RANGO 1 — Compliance, privacy, etica del prodotto",
        2: "RANGO 2 — Budget e scope",
        3: "RANGO 3 — Qualità e sicurezza tecnica",
        4: "RANGO 4 — Validazione della domanda prima della costruzione",
    }

    print("=" * 64)
    print("GATE DI RIGORE — Officina")
    print("=" * 64)
    tot_errori = sum(len(v) for v in per_rango.values())
    print(f"Errori: {tot_errori} · Avvisi: {len(avvisi)} · Lacune aperte: {len(lacune)}")

    if tot_errori:
        print("\nERRORI, in ordine di gerarchia (CLAUDE.md §1) — si corregge prima il rango più alto:")
        for rango in (1, 2, 3, 4):
            if per_rango[rango]:
                print(f"\n  {NOMI_RANGO[rango]}")
                for e in per_rango[rango]:
                    print("    ✗ " + e)

    if avvisi:
        print("\nAVVISI (da giustificare, non bloccano)")
        for a in avvisi:
            print("  ! " + a)

    if lacune:
        print("\nLACUNE DICHIARATE (funzionamento corretto, non fallimento)")
        for l in lacune:
            print("  · " + l)

    if report:
        print("\nRapporto informativo: uscita forzata a 0.")
        return 0

    if tot_errori:
        print("\nGATE ROSSO — lo Sprint non si chiude. Si corregge sempre a")
        print("partire dal rango più alto tra quelli segnalati.")
        return 1

    print("\nGATE VERDE — lo Sprint può chiudersi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
