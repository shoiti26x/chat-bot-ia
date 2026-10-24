# titulo
# campo de mensagem (input)
# quando o usuario enviar uma mensagem
    # mostrar a mensagem
    # mandar a mensagem para a IA
    # mostrar a resposta da IA

import streamlit as st
from openai import OpenAI


# configurar a aba do navegador (titulo e icone)
st.set_page_config(page_title="Chatbot de IA", page_icon="🤖")


modelo_ia = OpenAI(
    api_key=st.secrets["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)


# personalidade do chatbot: instrucao que a IA recebe antes de toda conversa
PERSONALIDADE = (
    "Você é um assistente simpático e direto, que responde sempre em português do Brasil. "
    "Explique as coisas de forma simples, com exemplos quando ajudar, "
    "e diga quando não souber algo em vez de inventar."
)


def pedacos_de_texto(resposta_ia):
    # devolve so o texto de cada pedaco da resposta, conforme ele chega
    for pedaco in resposta_ia:
        if pedaco.choices and pedaco.choices[0].delta.content:
            yield pedaco.choices[0].delta.content


st.title("Chatbot de IA")

# criar historico de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state.lista_mensagens = []

# barra lateral com botao de limpar conversa
with st.sidebar:
    if st.button("Limpar conversa"):
        st.session_state["lista_mensagens"] = []


mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")


# mensagem de boas-vindas enquanto a conversa estiver vazia
if not st.session_state["lista_mensagens"] and not mensagem_usuario:
    st.chat_message("assistant").write("Olá! Sou o seu assistente de IA. Pode me perguntar qualquer coisa.")


# mostrar historico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]

    st.chat_message(quem_enviou).write(texto_mensagem)


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


    # pegar a resposta da IA em streaming e mostrar no chat conforme ela chega
    try:
        resposta_ia = modelo_ia.chat.completions.create(
            messages=[{"role": "system", "content": PERSONALIDADE}] + st.session_state["lista_mensagens"],
            model="gemini-flash-lite-latest",
            stream=True
        )

        with st.chat_message("assistant"):
            resposta_modelo = st.write_stream(pedacos_de_texto(resposta_ia))
    except Exception as erro:
        # tira a mensagem do usuario do historico para ele poder tentar de novo
        st.session_state["lista_mensagens"].pop()
        st.error("Não consegui falar com a IA agora. Tente de novo em alguns segundos.")
        st.caption(f"Detalhe do erro: {erro}")
        st.stop()


    mensagem2 = {
        "role": "assistant",
        "content": resposta_modelo
    }

    st.session_state["lista_mensagens"].append(mensagem2)


# manter o historico de mensagens
# tornar as respostas inteligentes