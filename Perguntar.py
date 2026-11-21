import os
import Ouvir
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
cliente = Groq()
def perguntar(frase):
    resposta = cliente.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": frase}]
        )
    return resposta.choices[0].message.content

print(perguntar(Ouvir.ouvir_microfone()))