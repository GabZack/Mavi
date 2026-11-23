import pyttsx3

init = pyttsx3.init()
def falar(texto):
    init.setProperty("voice", r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")
    init.say(texto)
    init.runAndWait()


if __name__ == "__main__":
    falar(texto="Ola pessoal, Sou a mavi, Seu assitente virtual feito por Cristiano Ronaldo!")