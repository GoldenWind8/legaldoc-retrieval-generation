from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings

def loadEmbeddings(dir):
    model_name = "C:/Users/sashi/PycharmProjects/legalrag/rag/bge-base-en-v1.5"
    encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    model_norm = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},
        encode_kwargs=encode_kwargs
    )
    # load from disk
    return Chroma(persist_directory=dir, embedding_function=model_norm)

