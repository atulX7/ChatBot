# Imports and Initial Setup:

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer
import chainlit as cl

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Create Vector Database Function:

def create_vector_db():
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()
	
# Define Custom Prompt and QA Chain:

custom_prompt_template = """
Context: {context}
Question: {question}
Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=db.as_retriever(search_kwargs={'k': 2}), return_source_documents=True, chain_type_kwargs={'prompt': prompt})
    return qa_chain
	
# Load Model and QA Bot Function:

def load_llm():
    llm = CTransformers(model="TheBloke/Llama-2-7B-Chat-GGML", model_type="llama", max_new_tokens=512, temperature=0.5)
    return llm

def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)
    return qa

# Define prepare_query Function:

def prepare_query(query, max_length=512):
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    inputs = tokenizer(query, truncation=True, max_length=max_length, return_tensors="pt")
    truncated_query = tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)
    return truncated_query

# Final Query function

def final_result(query):
    prepared_query = prepare_query(query)
    qa_result = qa_bot()
    response = qa_result({'query': prepared_query})
    return response

# Make the Query

print(final_result("Query"))
