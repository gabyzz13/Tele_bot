import requests
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv(".env")

def updates():
    updates = requests.get(
        f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates?offset=-1"
    ).json()

    last_update = updates["result"][0]
    if last_update:
        last_date = last_update["message"]["date"]

    return (
        last_update["message"]["chat"]["id"],
        last_update["message"]["text"],
        last_date
    )


def calcular_com_mathjs(expressao):
    """Envia a expressão para a API do MathJS."""
    try:
        encoded = urllib.parse.quote(expressao)
        url = f"https://api.mathjs.org/v4/?expr={encoded}"

        res = requests.get(url)
        return res.text  # MathJS retorna o resultado como texto puro
    except Exception as e:
        return f"Erro ao calcular: {e}"


last_date = 0

while True:
    try:
        upd = updates()

        if upd[2] > last_date:
            chat_id = upd[0]
            expressao = upd[1]
            last_date = upd[2]

            # Envia para a API do MathJS
            resultado = calcular_com_mathjs(expressao)

            # Envia o resultado para o Telegram
            requests.post(
                url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
                data={"chat_id": chat_id, "text": f"Resultado: {resultado}"}
            )

    except Exception:
        pass

        url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage",
        data={"chat_id": 8398528515, "text": "Olá tudo bem?"}
    ).json()

    
