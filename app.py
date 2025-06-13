import streamlit as st
from langchain.memory import ConversationBufferMemory

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

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

def carrega_modelo(provedor, modelo, api_key):
    chat =  CONFIG_MODELOS[provedor]["chat"](
        model=modelo,
        api_key=api_key
    )
    st.session_state["chat"] = chat
    
def page_chat():
    st.header("Chat with AI")
    
    chat_model = st.session_state.get('chat')
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
        chat.write_stream(chat_model.stream(input_usuario))
        
        resposta = chat_model.invoke(input_usuario).content
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
        carrega_modelo(provedor, modelo, api_key)

def main():
    page_chat()
    with st.sidebar:
        sidebar()
if __name__ == "__main__":
    main()