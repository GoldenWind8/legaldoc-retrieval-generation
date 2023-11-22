from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Qdrant

url = "23.244.73.132"
api_key = "adfs8973241nwe8%213^%%^&nj"

#splitting the text into
loader = CSVLoader(file_path="aipg/aipg.csv", encoding='utf-8-sig')
data = loader.load()


def generateEmbeddings():
    model_norm = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en-v1.5")


    vectordb = Qdrant.from_documents(documents=data, url=url, port=6333, api_key=api_key, https=False, embedding=model_norm,prefer_grpc=False, collection_name="aipg")
    return vectordb

vectordb = generateEmbeddings()
retriever = vectordb.as_retriever()
print(retriever.get_relevant_documents("Who is Jojo")[0].page_content)