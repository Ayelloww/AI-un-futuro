document.getElementById("send-button").addEventListener("click", function() {
    const userMessage = document.getElementById("user-input").value;
    fetch("/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        // Ottieni la risposta dal server
        const aiResponse = data.message;

        // Aggiorna l'elemento HTML con l'ID "response" con la risposta
        document.getElementById("response").textContent = aiResponse;

        // Aggiungi il messaggio dell'utente e la risposta all'elemento "messages" per tenerne traccia
        const messages = document.getElementById("messages");
        messages.innerHTML += `<p>Utente: ${userMessage}</p>`;
        messages.innerHTML += `<p>AI: ${aiResponse}</p>`;

        // Cancella l'input dell'utente
        document.getElementById("user-input").value = "";
    })
    .catch(error => console.error("Errore:", error));
});
