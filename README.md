# 🎯 Simulador de Entrevista Técnica

Aplicação em **Python** que usa Inteligência Artificial (**Google Gemini**) para simular entrevistas técnicas de estágio. O candidato escolhe a área e o nível, responde às perguntas no chat e recebe nota, comentários e uma resposta modelo a cada pergunta.

> 🚧 Projeto em desenvolvimento contínuo.

---

## 📌 Sobre o projeto

Criei este projeto para treinar para as minhas próprias entrevistas de estágio.

Ele começou como um chatbot genérico (v1.0.0) e foi evoluindo aos poucos: histórico de conversa, tratamento de erros, respostas em streaming e personalidade configurável. Com essa base pronta, transformei o chatbot em um entrevistador, usando uma mensagem de sistema que define as regras da entrevista.

---

## ✨ Funcionalidades

- 🎯 Entrevista em 6 áreas: Python, Java, SQL e Banco de Dados, Git e GitHub, Lógica de Programação e Comportamental (RH)
- 📈 Três níveis de dificuldade: Iniciante, Estágio e Júnior
- 📝 Nota de 0 a 10, comentários e resposta modelo a cada resposta
- 💡 Dicas sem entregar a resposta, quando o candidato pede
- ⚡ Respostas em streaming (o texto aparece em tempo real, conforme é gerado)
- 🔄 Nova entrevista com um clique, ou automaticamente ao trocar a área ou o nível
- ⚠️ Mensagem amigável quando a API falha
- 🔐 Chave da API protegida com `st.secrets`

---

## 🧠 Como funciona

1. O candidato escolhe a área e o nível na barra lateral.
2. A função `montar_instrucoes` gera uma **mensagem de sistema** com as regras da entrevista para aquela área e nível. Ela é enviada para a IA antes da conversa e não aparece no chat.
3. A cada resposta do candidato, o app envia para a API a mensagem de sistema e **todo o histórico da conversa**, guardado em `st.session_state`. É assim que a IA "lembra" das perguntas anteriores, já que ela não guarda memória entre as chamadas.
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

A aplicação abre automaticamente no navegador. Escolha a área e o nível e escreva **começar**.

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
- [ ] Relatório final da entrevista, com a nota média e os pontos a melhorar
- [ ] Salvar o histórico de entrevistas para acompanhar a evolução
