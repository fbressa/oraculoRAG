import streamlit as st

TIPOS_VALIDOS = ["Youtube", "Site", "pdf", "txt", "csv", "docx", "pptx"]

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
        

def main():
    page_chat()
    with st.sidebar:
        sidebar()
if __name__ == "__main__":
    main()