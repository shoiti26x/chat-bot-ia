import streamlit as st
from openai import OpenAI


# configurar a aba do navegador (titulo e icone)
st.set_page_config(page_title="Chatbot de IA", page_icon="🤖")


modelo_ia = OpenAI(
    api_key=st.secrets["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)


# modos de uso do chatbot
MODO_ASSISTENTE = "Assistente geral"
MODO_ENTREVISTA = "Simulador de entrevista"

# opcoes do simulador de entrevista
AREAS = [
    "Python",
    "Java",
    "SQL e Banco de Dados",
    "Git e GitHub",
    "Lógica de Programação",
    "Comportamental (RH)",
]
NIVEIS = ["Iniciante", "Estágio", "Júnior"]


def montar_instrucoes(modo, area, nivel):
    # mensagem de sistema: define como a IA se comporta em cada modo
    if modo == MODO_ASSISTENTE:
        return (
            "Você é um assistente simpático e direto, que responde sempre em português do Brasil. "
            "Explique as coisas de forma simples, com exemplos quando ajudar, "
            "e diga quando não souber algo em vez de inventar."
        )

    return (
        "Você é um entrevistador técnico experiente, conduzindo uma entrevista "
        f"para uma vaga de estágio em tecnologia. Área: {area}. Nível do candidato: {nivel}.\n\n"
        "Regras:\n"
        "- Faça uma pergunta por vez e espere a resposta do candidato.\n"
        "- Depois de cada resposta, dê uma **Nota** de 0 a 10, diga o que ficou bom, "
        "o que faltou e mostre uma resposta modelo curta. Em seguida, faça a próxima pergunta.\n"
        "- Aumente a dificuldade aos poucos, conforme o candidato for bem.\n"
        "- Se o candidato pedir uma dica, dê uma pista sem entregar a resposta.\n"
        "- Responda sempre em português do Brasil, em tom profissional e encorajador."
    )


def pedacos_de_texto(resposta_ia):
    # devolve so o texto de cada pedaco da resposta, conforme ele chega
    for pedaco in resposta_ia:
        if pedaco.choices and pedaco.choices[0].delta.content:
            yield pedaco.choices[0].delta.content


# criar historico de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state.lista_mensagens = []

# barra lateral com as configuracoes
with st.sidebar:
    st.header("Configurações")
    modo = st.radio("Modo", [MODO_ASSISTENTE, MODO_ENTREVISTA])

    # area e nivel so aparecem no simulador de entrevista
    area = None
    nivel = None
    if modo == MODO_ENTREVISTA:
        area = st.selectbox("Área", AREAS)
        nivel = st.radio("Nível", NIVEIS, index=1)

    if st.button("Nova conversa"):
        st.session_state["lista_mensagens"] = []

# se o usuario trocar o modo, a area ou o nivel, comeca uma conversa nova
configuracao_atual = (modo, area, nivel)
if st.session_state.get("configuracao") != configuracao_atual:
    st.session_state["configuracao"] = configuracao_atual
    st.session_state["lista_mensagens"] = []


# textos e icones que mudam conforme o modo
if modo == MODO_ASSISTENTE:
    subtitulo = "Converse com uma IA sobre qualquer assunto."
    boas_vindas = "Olá! Sou o seu assistente de IA. Pode me perguntar qualquer coisa."
    campo_texto = "Escreva sua mensagem aqui"
    avatar_ia = "🤖"
else:
    subtitulo = "Treine para entrevistas de estágio com uma IA que pergunta, corrige e dá nota."
    boas_vindas = (
        f"Olá! Vou ser seu entrevistador de **{area}**, nível **{nivel}**. "
        "Quando estiver pronto, escreva **começar**."
    )
    campo_texto = "Escreva sua resposta aqui"
    avatar_ia = "🧑‍💼"

AVATARES = {
    "user": "🙋",
    "assistant": avatar_ia,
}


st.title("🤖 Chatbot de IA")
st.caption(subtitulo)

mensagem_usuario = st.chat_input(campo_texto)


# mensagem de boas-vindas enquanto a conversa estiver vazia
if not st.session_state["lista_mensagens"] and not mensagem_usuario:
    st.chat_message("assistant", avatar=AVATARES["assistant"]).write(boas_vindas)


# mostrar historico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]

    st.chat_message(quem_enviou, avatar=AVATARES[quem_enviou]).write(texto_mensagem)


if mensagem_usuario:

    # exibir a mensagem do usuario na tela e guardar no historico
    st.chat_message("user", avatar=AVATARES["user"]).write(mensagem_usuario)

    mensagem1 = {
        "role": "user",
        "content": mensagem_usuario
    }

    st.session_state["lista_mensagens"].append(mensagem1)


    # pegar a resposta da IA em streaming e mostrar no chat conforme ela chega
    instrucoes = {"role": "system", "content": montar_instrucoes(modo, area, nivel)}

    try:
        resposta_ia = modelo_ia.chat.completions.create(
            messages=[instrucoes] + st.session_state["lista_mensagens"],
            model="gemini-flash-lite-latest",
            stream=True
        )

        with st.chat_message("assistant", avatar=AVATARES["assistant"]):
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
