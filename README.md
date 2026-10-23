# 🤖 Chatbot de IA

Chatbot de Inteligência Artificial desenvolvido com **Python**, **Streamlit** e **Google Gemini**.

Este projeto começou como a **primeira versão (v1.0.0)** de um chatbot desenvolvido durante meus estudos de Python, APIs e Inteligência Artificial, e está evoluindo para a **v1.1.0**.

A ideia é começar com uma aplicação simples e evoluí-la gradualmente, adicionando novas funcionalidades, melhorias na interface e novas integrações com modelos de IA.

> 🚧 Projeto em desenvolvimento.

---

## 📌 Sobre o projeto

O chatbot permite que o usuário envie mensagens através de uma interface de conversa e receba respostas geradas pelo **Google Gemini**.

A aplicação utiliza o **Streamlit** para criar a interface web e a API do Gemini para realizar a comunicação com o modelo de Inteligência Artificial.

O histórico das mensagens é mantido durante a sessão para que a conversa tenha continuidade.

---

## ✨ Funcionalidades

- 💬 Interface de conversa
- 🤖 Respostas geradas por Inteligência Artificial
- 🧠 Histórico de mensagens durante a sessão
- 🧹 Botão para limpar a conversa
- ⚠️ Mensagem amigável quando a API falha
- ⚡ Respostas em streaming (o texto aparece em tempo real, conforme é gerado)
- 🎭 Personalidade configurável por meio de uma mensagem de sistema
- 🔌 Integração com Google Gemini
- 🔐 Proteção da API Key utilizando `st.secrets`

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Streamlit | Criação da interface web |
| Google Gemini | Modelo de Inteligência Artificial |
| OpenAI Python SDK | Comunicação com a API compatível |
| Git | Controle de versão |
| GitHub | Hospedagem do código |

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

**5. Rode o chatbot**

```bash
streamlit run codigo.py
```

O chatbot abre automaticamente no navegador.

---

## 🎭 Personalizando o chatbot

O comportamento do chatbot é definido pela constante `PERSONALIDADE`, no início do `codigo.py`. Ela é enviada para a IA como mensagem de sistema antes de toda conversa e não aparece no chat.

Para mudar o tom das respostas, basta editar o texto. Por exemplo:

```python
PERSONALIDADE = "Você é um professor de programação paciente, que responde em português com exemplos de código."
```

---

## 📂 Estrutura do projeto

```text
chat-bot-ia/
│
├── .streamlit/
│   └── secrets.toml      # chave da API (não versionado)
│
├── .gitignore
├── codigo.py             # código do chatbot
├── requirements.txt      # dependências
└── README.md
```

---

## 🗺️ Próximas melhorias

- [x] Respostas em streaming (texto aparecendo aos poucos)
- [x] Personalidade configurável para o chatbot
- [ ] Publicação online no Streamlit Community Cloud
