// RADAR IA — Anteprima community: utilità condivise tra le viste del
// mockup. Nessuna chiamata di rete, nessuna azione reale: ogni interazione
// sociale passa da qui e mostra sempre lo stesso messaggio "in arrivo"
// (DEL-LOCALE-001, MOCKUP_COMMUNITY.md §3.2). Vanilla JS, nessuna libreria.

const elementoToast = document.getElementById("toast-in-arrivo");
let timerToast = null;

/**
 * Mostra il toast "in arrivo" — mai una finta conferma di successo.
 * role="status" + aria-live="polite" nel markup: annuncia il messaggio a
 * chi usa uno screen reader senza spostare il focus dalla pagina.
 */
function mostraFunzioneInArrivo(evento) {
  if (evento) evento.preventDefault();
  if (!elementoToast) return;
  elementoToast.textContent = "In arrivo — questa funzione non è ancora attiva.";
  elementoToast.hidden = false;
  clearTimeout(timerToast);
  timerToast = setTimeout(() => {
    elementoToast.hidden = true;
  }, 3200);
}

/** Badge "esempio" accanto al nome di un autore d'esempio (mai persone reali). */
function creaBadgeEsempio() {
  const badge = document.createElement("span");
  badge.className = "badge-esempio";
  badge.textContent = "esempio";
  return badge;
}

function creaNomeAutore(nome) {
  const span = document.createElement("span");
  span.className = "autore-post";
  span.append(nome, creaBadgeEsempio());
  return span;
}

// Collega automaticamente ogni pulsante marcato come "azione sociale finta"
// al toast, così ogni pagina non deve ripetere l'ascoltatore a mano.
document.addEventListener("click", (evento) => {
  const bottone = evento.target.closest("[data-azione-finta]");
  if (bottone) mostraFunzioneInArrivo(evento);
});

document.addEventListener("submit", (evento) => {
  if (evento.target.matches("[data-form-finto]")) mostraFunzioneInArrivo(evento);
});
