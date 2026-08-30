---
id: pattern-0001
titolo: Autenticazione utente (email/password + OAuth)
mandato: archivista-prodotto
commessa: interno
etichetta: DA VERIFICARE
parere_rilascio: non richiesto
stato: bozza
data: 2026-08-30
---

## Problema che risolve

Ogni webapp con account utente ha bisogno di: registrazione, login, gestione
sessione, reset password, e spesso login social (Google, GitHub...). È un
pezzo ad alto rischio di compliance (§6 CLAUDE.md: gestione segreti, OWASP
Top 10) che conviene non reinventare commessa per commessa.

## Stato d'uso nell'Officina

`[[LACUNA: nessuna commessa reale ha ancora attraversato lo sviluppo pieno —
STATO.md, Sprint 000/001, riporta "Commesse attive: Nessuna". Questa voce è
quindi una ricognizione di alternative comuni con licenza compatibile, non un
pattern collaudato dall'Officina. Va validata alla prima commessa che
implementa autenticazione e poi riclassificata VALIDATO.]]`

## Alternative comuni (stack-agnostiche, per D-002 nessuno stack di default è ancora scelto)

### Opzione A — Auth.js (ex NextAuth.js), ecosistema Next.js/JS full-stack
- **Cosa fa**: gestione sessione, provider OAuth precostruiti, adapter per
  diversi database.
- **Licenza**: ISC. Fonte verificata: file LICENSE nel repo ufficiale
  https://github.com/nextauthjs/next-auth/blob/main/LICENSE — licenza
  permissiva, compatibile con uso commerciale, nessuna royalty.
- **Vincolo di stack**: pensato per Next.js/framework React SSR; disponibile
  anche per Express e SvelteKit tramite pacchetti dedicati.

### Opzione B — Passport.js, ecosistema Express/Node generico
- **Cosa fa**: middleware di autenticazione con strategie plug-in (locale,
  OAuth, JWT).
- **Licenza**: MIT. Fonte verificata: file LICENSE nel repo ufficiale
  https://github.com/jaredhanson/passport/blob/master/LICENSE
- **Vincolo di stack**: qualunque backend Node/Express; richiede più
  cablaggio manuale (sessioni, storage utenti) rispetto a soluzioni
  "batteries included".

### Opzione C — Supabase Auth, backend-as-a-service
- **Cosa fa**: autenticazione gestita (email/password, OAuth, magic link) più
  database Postgres e storage nello stesso servizio.
- **Licenza del codice open source**: Apache License 2.0. Fonte verificata:
  file LICENSE nel repo principale
  https://github.com/supabase/supabase/blob/master/LICENSE (componenti
  come Storage API sono anch'essi Apache 2.0).
- **Nota**: l'offerta hosted di Supabase è un servizio a pagamento con
  termini contrattuali propri, distinti dalla licenza del codice open
  source; `[[LACUNA: termini del piano hosted (limiti free tier, prezzo)
  non verificati in questa ricognizione — di competenza dello Stratega
  Commerciale se rilevanti per il pricing della commessa]]`.

## Tempo di integrazione

`[[LACUNA: nessun tempo di integrazione osservato dall'Officina — zero
commesse chiuse a oggi. Le guide "quickstart" ufficiali di Auth.js e Passport
dichiarano setup minimo in meno di un'ora per il caso base (solo email/password
o un solo provider OAuth), ma questo è un claim della documentazione del
vendor, non un'osservazione nostra: etichetta [DA VERIFICARE], da sostituire
con un tempo osservato reale alla prima commessa.]]`

## Rischi noti da presidiare (non di licenza)

- Gestione segreti (client secret OAuth, chiavi di sessione) mai in chiaro
  nel repo — di competenza `sviluppatore-backend` e `devops-sicurezza`.
- Base giuridica GDPR per i dati raccolti in registrazione — di competenza
  `custode`, va fissata prima dello schema dati (§6 CLAUDE.md).
