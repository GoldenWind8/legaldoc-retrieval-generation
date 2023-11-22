from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient


host = "23.244.73.132"
api_key = "adfs8973241nwe8%213^%%^&nj"
api_base = 'https://saturn-scoring-shipment-subscriber.trycloudflare.com/v1'

embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en-v1.5")
client = QdrantClient(host, port=6333, api_key=api_key, https=False)
retriever = Qdrant(client, "aipg",embeddings).as_retriever()
llm = ChatOpenAI( openai_api_base=api_base,
                  openai_api_key=api_base,max_tokens=1024)
qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                  chain_type="stuff",
                                  retriever=retriever,
                                  return_source_documents=True)


query = "Who is jojo"
print(retriever.get_relevant_documents(query))
llm_response = qa_chain(query)
print(llm_response['result'])