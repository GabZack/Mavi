import Ouvir
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
cliente = Groq()

def limpar(limpeza):
    limpeza = limpeza.replace("*","")
    return limpeza


def perguntar(frase):
    if frase != "":
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

        return limpar(resposta.choices[0].message.content)
    else:
        return "Houve um problema de conexão, por favor, espere e tente novamente mais tarde!"



if __name__ == "__main__":
    print(perguntar(Ouvir.ouvir_microfone()))