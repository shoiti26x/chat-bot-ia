# 🤖 Chatbot de IA

Chatbot de Inteligência Artificial em **Python**, com interface em **Streamlit** e respostas geradas pelo **Google Gemini**. Ele tem dois modos de uso:

- **🤖 Assistente geral**: conversa sobre qualquer assunto.
- **🎯 Simulador de entrevista**: simula uma entrevista de emprego para a vaga que você digitar, corrige as respostas e dá nota.

> 🚧 Projeto em desenvolvimento contínuo.

---

## 📌 Sobre o projeto

O projeto começou como um chatbot simples (v1.0.0), desenvolvido durante meus estudos de Python, APIs e Inteligência Artificial, e foi evoluindo aos poucos: histórico de conversa, tratamento de erros, respostas em streaming e personalidade configurável.

Com essa base pronta, adicionei o **modo simulador de entrevista**, que criei para treinar para as minhas próprias entrevistas de estágio. Os dois modos usam o mesmo código de conversa. O que muda entre eles é a **mensagem de sistema**, que define como a IA se comporta.

---

## ✨ Funcionalidades

- 🔀 Dois modos de uso, escolhidos na barra lateral
- 🎯 Simulador para qualquer vaga, digitada pelo usuário, com 3 tipos de entrevista: Mista, Técnica e Comportamental (RH)
- 📝 No simulador: nota de 0 a 10, comentários e resposta modelo a cada resposta, e dicas sem entregar a resposta
- 🧠 Histórico da conversa durante a sessão
- ⚡ Respostas em streaming (o texto aparece em tempo real, conforme é gerado)
- 🔄 Nova conversa com um clique, ou automaticamente ao trocar o modo, a vaga ou o tipo de entrevista
- ⚠️ Mensagem amigável quando a API falha
- 🔐 Chave da API protegida com `st.secrets`

---

## 🧠 Como funciona

1. O usuário escolhe o modo na barra lateral e, no simulador, também digita a vaga e escolhe o tipo de entrevista.
2. A função `montar_instrucoes` gera a **mensagem de sistema** de acordo com essas escolhas. Ela é enviada para a IA antes da conversa e não aparece no chat.
3. A cada mensagem, o app envia para a API a mensagem de sistema e **todo o histórico da conversa**, guardado em `st.session_state`. É assim que a IA "lembra" do que foi dito antes, já que ela não guarda memória entre as chamadas.
4. A resposta da IA chega em pedaços (streaming) e é mostrada na tela conforme é gerada.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Streamlit | Interface web |
| Google Gemini | Modelo de Inteligência Artificial |
| OpenAI Python SDK | Comunicação com a API do Gemini (formato compatível com a OpenAI) |
| Git e GitHub | Controle de versão e hospedagem do código |

---

## 🚀 Como rodar o projeto

**1. Clone o repositório**

```bash
git clone https://github.com/shoiti26x/chat-bot-ia.git
cd chat-bot-ia
```

**2. Crie e ative um ambiente virtual**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows, o comando de ativação é `.venv\Scripts\activate`.

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure a chave da API**

Gere uma chave gratuita no [Google AI Studio](https://aistudio.google.com/apikey) e crie o arquivo `.streamlit/secrets.toml` com o conteúdo:

```toml
GEMINI_API_KEY = "sua-chave-aqui"
```

Esse arquivo está no `.gitignore` e nunca é enviado ao GitHub.

**5. Rode a aplicação**

```bash
streamlit run codigo.py
```

A aplicação abre automaticamente no navegador. No modo simulador, digite a vaga, escolha o tipo de entrevista e escreva **começar**.

---

## 📂 Estrutura do projeto

```text
chat-bot-ia/
│
├── .streamlit/
│   ├── config.toml       # tema de cores da interface
│   └── secrets.toml      # chave da API (não versionado)
│
├── .gitignore
├── codigo.py             # código da aplicação
├── requirements.txt      # dependências
└── README.md
```

---

## 🗺️ Próximas melhorias

- [ ] Publicação online no Streamlit Community Cloud
- [ ] Relatório final da entrevista no simulador, com a nota média e os pontos a melhorar
- [ ] Salvar o histórico de entrevistas para acompanhar a evolução
