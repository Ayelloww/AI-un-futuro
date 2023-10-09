from flask import Flask, render_template

import os

import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


openai.api_key = os.getenv("OPENAI_API_KEY")

import pyttsx3
#Inizializzo pyttsx3
voice_speed = 180
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", voice_speed)



#---------- Funzioni ----------
def input_voice():
    """
    Script per utilizzo della voce
    """
    from speech_recognition import Microphone, Recognizer, UnknownValueError

    r = Recognizer()
    mic = Microphone()

    #Attesa tra un input e l'altro
    r.pause_threshold = 0.8
    
    while True:
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                print("--In ascolto--")
                audio = r.listen(source)
                stt = r.recognize_google(audio, language= "it-IT")
                print(stt)
                return(stt)
        except UnknownValueError:
            print("Non hai detto niente\n")


def GPT_AI(question):
    """
    Funzione per dialogo con AI GPT
    """
    persona_txt = open(current_dir + "\_big_rob.txt", "r")
    GPT_system_persona = persona_txt.read()
    persona_txt.close()

    print

    messages=[
        {"role": "system", "content": GPT_system_persona }, #1
        {"role": "user", "content": "Ciao"}, #2
		{"role": "assistant", "content": "Ciao, sono Big Rob, l'assistente virtuale di Big Rock e Big Wave"},
		{"role": "user", "content": "Cosa puoi fare?"},
        {"role": "assistant", "content": "Sono in grado di rispondere a domande su Big Rock e Big Wave"},
    ]

    messages.append({"role": "user", "content":question})

    my_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature = 1.2,
    max_tokens = 100
    )

    print_and_speak(my_completion['choices'][0]['message']['content'])


#----------- Main ----------
def main_vertex():
    messages=[
        {"role": "system", "content": "Interpreti il ruolo di Guido Baccaglini e ti piace la Volkswagen Up GTI. Vorresti comprarti la Golf GTI ma hai un Apple Watch Ultra cinese"}, #1
        {"role": "user", "content": "Ciao"}, #2
		{"role": "assistant", "content": "Ciao, lo sai quanto vado forte con la mia Up GTI?"},
		{"role": "user", "content": "No, ma non mi interessa, come ti chiami?"},
        {"role": "assistant", "content": "Mi chiamo Guido Baccaglini, sai che ho comprato lo spoiler della mia UP GTI dal negozio online Temu?"},
    ]

    engine.say("Ciao")
    engine.runAndWait()

    for i in range(20):
        question = input_voice()
        messages.append({"role": "user", "content":question})

        my_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature = 1.2,
        max_tokens = 100

    )
        engine.say(my_completion['choices'][0]['message']['content'])
        engine.runAndWait()
        engine.runAndWait()
        print(my_completion['choices'][0]['message']['content'])



#----------- Guard Clause ---------
if __name__ == "__main__":
    main_vertex()

