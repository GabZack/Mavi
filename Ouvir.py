import speech_recognition as sr
def ouvir_microfone():
        recognizer = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)

                    print("Teste:")

                    fala = recognizer.listen(source)
                
                
                try:
                    frase = recognizer.recognize_google(fala, language="pt-BR")
                    frase = frase.lower()
                    print(frase)
                    return frase
                except sr.UnknownValueError:
                    print("Não entendi o que você falou")
            except sr.RequestError:
                print("Deu problema no Google, volte novamente mais tarde")
                return ""


if __name__ == "__main__":
    ouvir_microfone()