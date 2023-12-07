from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

def gerar_historias(prompt):
    KEY_GPT = os.getenv("GPT_KEY")
    print(KEY_GPT)
    headers = {"Authorization": f"Bearer {KEY_GPT}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    prompt_completo = prompt + "\n\n Crie um trecho de uma história com base no contexto fornecido acima e me devolva apenas o trecho da história."

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": prompt_completo}]
    }

    body_mensagem = json.dumps(body_mensagem)

    try:
        requisicao_GPT = requests.post(link, headers=headers, data=body_mensagem)
        requisicao_GPT.raise_for_status()  # Levanta um erro se a requisição falhar
        resposta_GPT = requisicao_GPT.json()

        # Certifique-se de que a resposta contém o caminho esperado antes de acessá-lo
        if 'choices' in resposta_GPT and resposta_GPT['choices']:
            historia_atualizada = resposta_GPT['choices'][0]['message']['content']
            return historia_atualizada
        else:
            return "Resposta da GPT não contém o caminho esperado."

    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
    
def complementar_historia(historia_base, trecho):
    KEY_GPT = os.getenv("GPT_KEY")
    print(KEY_GPT)
    headers = {"Authorization": f"Bearer {KEY_GPT}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    prompt_completo = f"Vou te pedir para complementar uma história base com um trecho novo. Coloque o trecho sem altera-lo no melhor lugar e adapte a história para fazer sentido. Preciso que responda apenas o resultado.\n História base: {historia_base}\n\n trecho complementar: {trecho}"

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": prompt_completo}]
    }

    body_mensagem = json.dumps(body_mensagem)

    try:
        requisicao_GPT = requests.post(link, headers=headers, data=body_mensagem)
        requisicao_GPT.raise_for_status()  # Levanta um erro se a requisição falhar
        resposta_GPT = requisicao_GPT.json()

        # Certifique-se de que a resposta contém o caminho esperado antes de acessá-lo
        if 'choices' in resposta_GPT and resposta_GPT['choices']:
            historia_atualizada = resposta_GPT['choices'][0]['message']['content']
            return historia_atualizada
        else:
            return "Resposta da GPT não contém o caminho esperado."

    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
    