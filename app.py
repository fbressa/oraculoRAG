import streamlit as st

TIPOS_VALIDOS = ["Youtube", "Site", "pdf", "txt", "csv", "docx", "pptx"]

CONFIG_MODELOS = {"Groq": {"modelos": ["gemma2-9b-it", "llama-3.3-70b-versatile"]},
                  "OpenAI": {"modelos": ["gpt-3.5-turbo-0125", "o4-mini-2025-04-16", "chatgpt-4o-latest", "gpt-4.1-mini-2025-04-14"]}}

def page_chat():
    st.header("Chat with AI")
    
    mensagens = st.session_state.get("mensagens", [])
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []
    
    for mensagem in mensagens:
        chat = st.chat_message(mensagem[0])
        chat.markdown(mensagem[1])

    input_usuario = st.chat_input("Digite sua mensagem")
    if input_usuario:
        mensagens.append(("user", input_usuario))
        st.session_state['mensagens'] = mensagens
        chat = st.chat_message("user")
        chat.markdown(input_usuario)
        
        # Simulate AI response
        resposta_ai = "Esta é uma resposta simulada da IA."
        st.session_state.mensagens.append(("ai", resposta_ai))
        chat = st.chat_message("ai")
        chat.markdown(resposta_ai)

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

        if st.button("Salvar configuração"):
            st.session_state[f'api_key_{provedor}'] = api_key
            st.success(f"Chave de API para {provedor} salva com sucesso!")
        st.info("As chaves de API são armazenadas em sessão e não são salvas permanentemente.")

def main():
    page_chat()
    with st.sidebar:
        sidebar()
if __name__ == "__main__":
    main()