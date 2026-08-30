// RADAR IA — frontend del prototipo catalogo risorse. Vanilla JS, nessuna
// libreria (vedi ARCHITETTURA.md). Nessun dato sensibile: single-user,
// senza autenticazione.

const API = "/api/risorse";

const form = document.getElementById("form-risorsa");
const campoTitolo = document.getElementById("campo-titolo");
const campoUrl = document.getElementById("campo-url");
const campoTipo = document.getElementById("campo-tipo");
const campoNote = document.getElementById("campo-note");
const messaggioForm = document.getElementById("messaggio-form");
const lista = document.getElementById("lista-risorse");
const listaVuota = document.getElementById("lista-vuota");
const bottoniFiltro = document.querySelectorAll(".filtro");

let risorse = [];
let filtroCorrente = "tutte";

const ETICHETTE_TIPO = {
  pratica: "Pratica",
  strumento: "Strumento",
  esperimento: "Esperimento",
};

function urlSicuro(url) {
  if (!url) return null;
  try {
    const parsata = new URL(url);
    return ["http:", "https:"].includes(parsata.protocol) ? parsata.href : null;
  } catch {
    return null;
  }
}

async function caricaRisorse() {
  const risposta = await fetch(API);
  risorse = await risposta.json();
  disegnaLista();
}

function disegnaLista() {
  lista.innerHTML = "";
  const visibili = risorse.filter(
    (r) => filtroCorrente === "tutte" || r.stato === filtroCorrente
  );

  listaVuota.hidden = visibili.length > 0;

  for (const risorsa of visibili) {
    const li = document.createElement("li");
    li.className = `risorsa ${risorsa.stato}`;

    const rigaAlto = document.createElement("div");
    rigaAlto.className = "risorsa-riga-alto";

    const titolo = document.createElement("span");
    titolo.className = "risorsa-titolo";
    const href = urlSicuro(risorsa.url);
    if (href) {
      const link = document.createElement("a");
      link.href = href;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = risorsa.titolo;
      titolo.appendChild(link);
    } else {
      titolo.textContent = risorsa.titolo;
    }

    const tipo = document.createElement("span");
    tipo.className = "risorsa-tipo";
    tipo.textContent = ETICHETTE_TIPO[risorsa.tipo] || risorsa.tipo;

    rigaAlto.append(titolo, tipo);
    li.appendChild(rigaAlto);

    if (risorsa.note) {
      const note = document.createElement("p");
      note.className = "risorsa-note";
      note.textContent = risorsa.note;
      li.appendChild(note);
    }

    const azioni = document.createElement("div");
    azioni.className = "risorsa-azioni";
    const bottone = document.createElement("button");
    bottone.type = "button";
    const daProvare = risorsa.stato === "da_provare";
    bottone.textContent = daProvare ? "Segna come letta/provata" : "✓ Letta/provata — segna come da provare";
    bottone.addEventListener("click", () => cambiaStato(risorsa.id, daProvare ? "letta_provata" : "da_provare"));
    azioni.appendChild(bottone);
    li.appendChild(azioni);

    lista.appendChild(li);
  }
}

async function cambiaStato(id, nuovoStato) {
  const risposta = await fetch(`${API}/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ stato: nuovoStato }),
  });
  if (!risposta.ok) return;
  const aggiornata = await risposta.json();
  risorse = risorse.map((r) => (r.id === aggiornata.id ? aggiornata : r));
  disegnaLista();
}

form.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  messaggioForm.textContent = "";
  messaggioForm.className = "messaggio";

  const corpo = {
    titolo: campoTitolo.value.trim(),
    url: campoUrl.value.trim(),
    tipo: campoTipo.value,
    note: campoNote.value.trim(),
  };

  const risposta = await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(corpo),
  });

  const dati = await risposta.json();

  if (!risposta.ok) {
    messaggioForm.textContent = dati.errore || "Errore imprevisto";
    messaggioForm.classList.add("errore");
    return;
  }

  risorse.unshift(dati);
  disegnaLista();
  form.reset();
  messaggioForm.textContent = "Risorsa aggiunta al catalogo.";
  messaggioForm.classList.add("ok");
});

bottoniFiltro.forEach((bottone) => {
  bottone.addEventListener("click", () => {
    filtroCorrente = bottone.dataset.filtro;
    bottoniFiltro.forEach((b) => b.classList.toggle("attivo", b === bottone));
    disegnaLista();
  });
});

caricaRisorse();
