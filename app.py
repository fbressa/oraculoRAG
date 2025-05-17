import streamlit as st

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


def main():
    page_chat()

if __name__ == "__main__":
    main()