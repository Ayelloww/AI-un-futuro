from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/send", methods=["POST"])
def send_message():
    user_message = request.json.get("message")
    
    # Simuliamo una risposta AI statica
    ai_response = "Ciao, sono l'AI. Ho ricevuto il tuo messaggio: " + user_message
    
    return jsonify({"message": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
