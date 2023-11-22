from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader

#splitting the text into
loader = CSVLoader(file_path="data.csv",source_column="source", encoding='utf-8-sig')

data = loader.load()
print(data[5].page_content)


def generateEmbeddings():
    model_name = "C:/Users/sashi/PycharmProjects/legalrag/rag/bge-base-en-v1.5"
    encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    model_norm = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},
        encode_kwargs=encode_kwargs
    )
    persist_directory = 'db3'
    ## Here is the nmew embeddings being used
    embedding = model_norm
    vectordb = Chroma.from_documents(documents=data,
                                     embedding=embedding,
                                     persist_directory=persist_directory)
    return vectordb


vectordb = generateEmbeddings()
retriever = vectordb.as_retriever()
print(retriever.get_relevant_documents("Phone time rules")[0].page_content)