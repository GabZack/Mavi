import Ouvir
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
cliente = Groq()
def perguntar(frase):
    resposta = cliente.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": frase}],
        tools=[ 
                {
                    "type": "browser_search"
                }
            ]
        )


    return resposta.choices[0].message.content

if __name__ == "__main__":
    print(perguntar(Ouvir.ouvir_microfone()))