from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from loadEmbeddings import loadEmbeddings
import textwrap

#Prompt
prompt = """You are a helpful assistant that will help them write letters of complaint based on their situation and the existing regulations.

The following text is an extract from an implementation of The First Step Act, a U.S. federal guidelines for prisons, particularly for inmates and staff. It emphasizes increased penalties for certain drugs. It also discusses the ineligibility of deportable prisoners to claim time credits and mandates periodic risk reassessments for inmates. Additionally, the guidelines provide for dyslexia screening and support in prisons, ensure training for prison staff, and set up mechanisms to monitor and ensure the consistent application of these rules.

[context]

Please use the information to  write a complaint for the inmate. Ask him for more info if necessary:
Inmate: I am not receiving any phone time"""

query = "I am not receiving any phone time. Please write a complaint email"

#LLM
llm = ChatOpenAI(openai_api_key="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", model_name="gpt-3.5-turbo")
retriever = loadEmbeddings("db3").as_retriever()
print(retriever.get_relevant_documents(query))
qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                  chain_type="stuff",
                                  retriever=retriever,
                                  return_source_documents=True)


llm_response = qa_chain(query)
print(llm_response['result'])