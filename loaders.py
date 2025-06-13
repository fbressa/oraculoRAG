from langchain_community.document_loaders import (WebBaseLoader,
                                                 YoutubeLoader,
                                                 CSVLoader,
                                                 PyPDFLoader,
                                                 TextLoader)

def carreag_site(url):

    loader = WebBaseLoader(url)
    lista_documentos = loader.load()
    documento = '\n''\n'.join([doc.page_content for doc in lista_documentos])
    return documento

def carreag_youtube(video_id):

    loader = YoutubeLoader(video_id, add_video_info= False, language="pt-br")
    lista_documentos = loader.load()
    documento = '\n''\n'.join([doc.page_content for doc in lista_documentos])
    return documento

def carreag_csv(caminho):

    loader = CSVLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n''\n'.join([doc.page_content for doc in lista_documentos])
    return documento

def carreag_pdf(caminho):

    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n''\n'.join([doc.page_content for doc in lista_documentos])
    return documento

def carreag_pdf(caminho):

    loader = TextLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n''\n'.join([doc.page_content for doc in lista_documentos])
    return documento

