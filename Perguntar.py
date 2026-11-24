import Ouvir
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
cliente = Groq()
def perguntar(frase):
    resposta = cliente.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "system", "content": os.getenv("regras")},
                  {"role": "user", "content": frase}
                    ],
        tools=[ 
                {
                    "type": "browser_search"
                }
            ]
        )


    return resposta.choices[0].message.content

if __name__ == "__main__":
    print(perguntar(Ouvir.ouvir_microfone()))