# titulo
# campo de mensagem (input)
# quando o usuario enviar uma mensagem
    # mostrar a mensagem
    # mandar a mensagem para a IA
    # mostrar a resposta da IA

import streamlit as st
from openai import OpenAI


modelo_ia = OpenAI(
    api_key=st.secrets["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

st.title("# Chatbot de IA")

# criar historico de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state.lista_mensagens = []


mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")


# mostrar historico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensgem = mensagem["content"]

    st.chat_message(quem_enviou).write(texto_mensgem)


if mensagem_usuario:

    # exibir a mensagem na tela
    # user -> usuario
    # assistant -> chatbot/robo/IA

    st.chat_message("user").write(mensagem_usuario)

    mensagem1 = {
        "role": "user",
        "content": mensagem_usuario
    }

    st.session_state["lista_mensagens"].append(mensagem1)


    # pegar a resposta da IA
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )


    # pegar somente o texto da resposta
    resposta_modelo = resposta_ia.choices[0].message.content

    print(resposta_modelo)


    # enviar a resposta da IA no chat
    st.chat_message("assistant").write(resposta_modelo)

    mensagem2 = {
        "role": "assistant",
        "content": resposta_modelo
    }

    st.session_state["lista_mensagens"].append(mensagem2)


# manter o historico de mensagens
# tornar as respostas inteligentes