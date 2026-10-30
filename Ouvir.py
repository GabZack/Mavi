import speech_recognition as sr
def ouvir_microfone():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)

            print("Teste:")

            fala = recognizer.listen(source)

        try:
            frase = recognizer.recognize_google(fala, language="pt-BR")
            frase = frase.lower()
            print(frase)
        except sr.UnknownValueError:
            print("Não entendi o que você falou")
            frase = ""
    except sr.RequestError:
        print("Deu problema no Google, volte novamente mais tarde")
        frase = ""


    return frase

ouvir_microfone()