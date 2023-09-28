import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA
import os

from rag.loadEmbeddings import loadEmbeddings

os.environ["OPENAI_API_KEY"] = "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"

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory,
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            with st.chat_message("User"):
                st.write(message.content)
        else:
            with st.chat_message("AI"):
                st.write(message.content)


def main():
    st.set_page_config(page_title="First Step Act Assistant", page_icon=":books:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("First Step Act Assistant :judge:")
    user_question = st.text_input("Ask a question:")

    with st.sidebar:
        st.subheader("Click here to initialize")
        if st.button("Load Data"):
            with st.spinner("Loading Data..."):
                # Load the existing vectorstore
                vectorstore = loadEmbeddings("db3")
                # Create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

    if user_question and st.session_state.conversation:
        handle_userinput(user_question)


if __name__ == "__main__":
    main()
