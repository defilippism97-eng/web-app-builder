# Officina — agenzia webapp con metodo da startup interna

Repository indipendente da Motore Talento. Undici mandati che sviluppano
webapp per committenti esterni reali, con Scoping esplicito, Ipotesi di Valore
falsificabile e Punti di Decisione che nessun mandato tecnico attraversa da
solo.

## Avvio

Istruzioni complete in `AVVIO.md`. In breve: installare Claude Code, aprire un
terminale dentro questa cartella, lanciare `claude`, poi `/sprint`.

Comandi: `/sprint`, `/consiglio <decisione>`, `/fine-sessione`.

## Il vincolo che governa tutto

C'è sempre un committente esterno con soldi, scadenze e potere di cambiare
idea (CLAUDE.md §1). La gerarchia dei presidi, in ordine:

1. Compliance, privacy, etica del prodotto — mai in deroga, nemmeno per l'MVP
2. Budget e tempo rispetto al valore atteso
3. Qualità e sicurezza del codice
4. Costruire feature prima di validarne il senso

Il gate applica questo ordine quando più violazioni coesistono: segnala e
blocca sempre prima il rango più alto.

## Da leggere in quest'ordine

1. `CLAUDE.md` — regole permanenti, ha precedenza su tutto
2. `STATO.md` — dove siamo adesso, unica fonte di verità
3. `00_delibere/DEL-0001` — il metodo
4. `90_ufficio/PROTOCOLLO.md` — Sprint, Fase di Commessa, Punti di Decisione
5. `90_ufficio/MANDATI.md` — gli undici ruoli e le loro Regole di Blocco
6. `70_progetti/_TEMPLATE/` — cosa si compila per aprire una commessa

## Cosa non fa da solo

Firma del contratto, comunicazione di problemi o sforamenti al committente,
accettazione di rischi di compliance oltre scadenza, rilascio in produzione
con dati reali senza parere del Custode, decisione su pivot o interruzione di
una commessa. Tutto questo arriva in `DOMANDE_APERTE.md` o in un Punto di
Decisione, mai eseguito in autonomia.
