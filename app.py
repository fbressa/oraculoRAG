import tempfile

import streamlit as st
from langchain.memory import ConversationBufferMemory

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from loaders import *
from langchain.prompts import ChatPromptTemplate

TIPOS_VALIDOS = ["Youtube", "Site", "pdf", "txt", "csv", "docx", "pptx"]

CONFIG_MODELOS = {"Groq": 
                        {"modelos": ["gemma2-9b-it", "llama-3.3-70b-versatile"],
                         "chat": ChatGroq},
                  "OpenAI": 
                        {"modelos": ["gpt-3.5-turbo-0125", "o4-mini-2025-04-16", "chatgpt-4o-latest", "gpt-4.1-mini-2025-04-14"],
                         "chat": ChatOpenAI}}

MEMORIA = ConversationBufferMemory()
MEMORIA.chat_memory.add_user_message("Olá IA! Você pode me ajudar com algumas perguntas?")
MEMORIA.chat_memory.add_ai_message("Olá! Estou aqui para ajudar. O que você gostaria de saber?")

def carrega_arquivos(tipo_arquivo, arquivo):
    if tipo_arquivo == 'Site':
        documento = carrega_site(arquivo)
    if tipo_arquivo == 'Youtube':
        documento = carrega_youtube(arquivo)
    if tipo_arquivo == 'pdf':
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp:
            temp.write(arquivo.read())
            nome_temp = temp.name
        documento = carrega_pdf(nome_temp)
    if tipo_arquivo == 'csv':
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as temp:
            temp.write(arquivo.read())
            nome_temp = temp.name
        documento = carrega_csv(nome_temp)
    if tipo_arquivo == 'txt':
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp:
            temp.write(arquivo.read())
            nome_temp = temp.name
        documento = carrega_txt(nome_temp)

    return documento

def carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo):

    documento = carrega_arquivos(tipo_arquivo, arquivo)

    system_message = '''Você é um assistente amigável chamado Oráculo.
    Você possui acesso às seguintes informações vindas 
    de um documento {}: 

    ####
    {}
    ####

    Utilize as informações fornecidas para basear as suas respostas.

    Sempre que houver $ na sua saída, substita por S.

    Se a informação do documento for algo como "Just a moment...Enable JavaScript and cookies to continue" 
    sugira ao usuário carregar novamente o Oráculo!'''.format(tipo_arquivo, documento)

    template = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ('placeholder', "{chat_history}"),
        ('human', "{input}"),
    ])

    chat =  CONFIG_MODELOS[provedor]["chat"](
        model=modelo,
        api_key=api_key
    )
    chain = template | chat

    st.session_state["chain"] = chain
    
def page_chat():
    st.header("Chat with AI")

    chain = st.session_state.get('chain')
    if not chain:
        st.warning("Carregue um modelo primeiro!")
        st.stop()

    memoria = st.session_state.get("memoria", MEMORIA)
    if "memoria" not in st.session_state:
        st.session_state["memoria"] = memoria

    for mensagem in memoria.chat_memory.messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    input_usuario = st.chat_input("Digite sua mensagem")
    if input_usuario:
        memoria.chat_memory.add_user_message(input_usuario)
        chat = st.chat_message('human')
        chat.markdown(input_usuario)

        chat = st.chat_message('ai')
        chat.write_stream(chain.stream(input_usuario))

        resposta = chat.write_stream(chain.stream({
            'input': input_usuario, 
            'chat_history': memoria.buffer_as_messages
            }))
        memoria.chat_memory.add_ai_message(resposta)

        st.session_state["memoria"] = memoria
        st.rerun()
        
def sidebar():
    tabs = st.tabs(["Upload de arquivos", "Seleção de modelos"])
    with tabs[0]:
        st.header("Upload de arquivos")
        tipo_arquivo = st.selectbox('Selecione o tipo de arquivo', TIPOS_VALIDOS)
        
        if tipo_arquivo == "Youtube":
            arquivo = st.text_input("Cole o link do vídeo do Youtube")
        if tipo_arquivo == "Site":
            arquivo = st.text_input("Cole o link do site")
        if tipo_arquivo == "pdf":
            arquivo = st.file_uploader("Selecione o arquivo PDF", type=["pdf"])
        if tipo_arquivo == "txt":
            arquivo = st.file_uploader("Selecione o arquivo TXT", type=["txt"])
        if tipo_arquivo == "csv":
            arquivo = st.file_uploader("Selecione o arquivo CSV", type=["csv"])
        if tipo_arquivo == "docx":
            arquivo = st.file_uploader("Selecione o arquivo DOCX", type=["docx"])
        if tipo_arquivo == "pptx":
            arquivo = st.file_uploader("Selecione o arquivo PPTX", type=["pptx"])

    with tabs[1]:
        st.header("Seleção de modelos")
        provedor = st.selectbox("Escolha um provedor", CONFIG_MODELOS.keys())
        modelo = st.selectbox("Escolha um modelo", CONFIG_MODELOS[provedor]["modelos"])
        api_key = st.text_input(f"Cole sua chave de API para o provedor {provedor}", value=st.session_state.get(f'api_key_{provedor}', ''), type="password")

        if st.button("Salvar configuração", use_container_width=True):
            st.session_state[f'api_key_{provedor}'] = api_key
            st.success(f"Chave de API para {provedor} salva com sucesso!")
        

    if st.button("Carregar modelo", use_container_width=True):
        carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo)
    if st.button('Apagar Histórico de Conversa', use_container_width=True):
        st.session_state['memoria'] = MEMORIA

def main():
    with st.sidebar:
        sidebar()
    page_chat()
    
if __name__ == "__main__":
    main()