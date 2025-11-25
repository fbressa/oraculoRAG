# 🔮 Oráculo RAG

Um assistente de IA conversacional alimentado por RAG (Retrieval-Augmented Generation) que permite conversar com seus documentos usando LLMs de ponta como GPT-4 e Llama 3.

## 📋 Sobre o Projeto

Oráculo RAG é uma aplicação web interativa construída com Streamlit que permite fazer perguntas sobre o conteúdo de diversos tipos de documentos. O sistema utiliza a técnica RAG para fornecer respostas precisas e contextualizadas baseadas nos seus dados.

### ✨ Funcionalidades

- 💬 **Chat Interativo**: Interface conversacional amigável com histórico de mensagens
- 📄 **Múltiplos Formatos**: Suporte para diversos tipos de arquivos:
  - 📹 Vídeos do YouTube (com transcrição automática)
  - 🌐 Sites e páginas web
  - 📑 PDFs
  - 📝 Arquivos TXT
  - 📊 Arquivos CSV
  - 📄 Documentos DOCX
  - 📊 Apresentações PPTX
- 🤖 **Múltiplos Provedores de IA**:
  - **OpenAI**: GPT-3.5, GPT-4, O4-mini, ChatGPT-4o
  - **Groq**: Gemma2-9b, Llama 3.3-70b
- 💾 **Memória de Conversação**: Mantém o contexto durante toda a conversa
- 🔒 **Gerenciamento Seguro de API Keys**: Armazenamento seguro das chaves de API

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/fbressa/oraculoRAG.git
cd oraculoRAG
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**

No Windows:
```powershell
.\venv\Scripts\activate
```

No Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

## 🎯 Como Usar

1. **Inicie a aplicação**
```bash
streamlit run app.py
```

2. **Configure o modelo de IA**
   - Na barra lateral, vá para a aba "Seleção de modelos"
   - Escolha um provedor (OpenAI ou Groq)
   - Selecione o modelo desejado
   - Insira sua chave de API
   - Clique em "Salvar configuração"

3. **Carregue seu documento**
   - Na aba "Upload de arquivos"
   - Selecione o tipo de arquivo
   - Faça o upload ou cole o link (dependendo do tipo)

4. **Carregue o modelo**
   - Clique no botão "Carregar modelo"
   - Aguarde o processamento do documento

5. **Comece a conversar!**
   - Digite suas perguntas no campo de chat
   - O Oráculo responderá baseado no conteúdo do documento

## 🔑 Obtendo API Keys

### OpenAI
1. Acesse [platform.openai.com](https://platform.openai.com)
2. Faça login ou crie uma conta
3. Vá para "API Keys" no menu
4. Clique em "Create new secret key"

### Groq
1. Acesse [console.groq.com](https://console.groq.com)
2. Faça login ou crie uma conta
3. Navegue até a seção de API Keys
4. Gere uma nova chave

## 📚 Estrutura do Projeto

```
oraculoRAG/
│
├── app.py              # Aplicação principal Streamlit
├── loaders.py          # Funções para carregar diferentes tipos de documentos
├── requirements.txt    # Dependências do projeto
├── README.md          # Este arquivo
└── help.txt           # Arquivo de ajuda
```

## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para criação da interface web
- **[LangChain](https://python.langchain.com/)**: Framework para desenvolvimento com LLMs
- **[OpenAI](https://openai.com/)**: Modelos GPT
- **[Groq](https://groq.com/)**: Modelos Llama e Gemma
- **BeautifulSoup4**: Web scraping
- **PyPDF**: Processamento de PDFs
- **youtube-transcript-api**: Extração de transcrições do YouTube

## ⚙️ Configurações

O projeto suporta os seguintes modelos:

### OpenAI
- `gpt-3.5-turbo-0125`
- `o4-mini-2025-04-16`
- `chatgpt-4o-latest`
- `gpt-4.1-mini-2025-04-14`

### Groq
- `gemma2-9b-it`
- `llama-3.3-70b-versatile`

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**Felipe Bressa**
- GitHub: [@fbressa](https://github.com/fbressa)

## 🐛 Problemas Conhecidos

- Alguns sites podem bloquear o scraping - o sistema tentará 5 vezes antes de falhar
- Vídeos do YouTube sem legendas em português podem não funcionar
- Documentos muito grandes podem levar mais tempo para processar

## 💡 Dicas

- Use modelos maiores (como GPT-4 ou Llama 3.3-70b) para respostas mais precisas
- Documente suas fontes claramente nas perguntas
- Limpe o histórico de conversas quando mudar de documento
- Para sites com JavaScript, tente carregar novamente se receber erro

## 📞 Suporte

Se encontrar problemas ou tiver sugestões, por favor abra uma [issue](https://github.com/fbressa/oraculoRAG/issues) no GitHub.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!