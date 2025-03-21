from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_ollama import Ollama
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

app = FastAPI()

# Initialize the Ollama LLM
llm = Ollama(model="mistral")

# Initialize the knowledge base (FAISS vector store)
documents = [
    {"page_content": "Example support document content."},
    # Add more documents as needed
]
embedding_model = OpenAIEmbeddings()
vector_store = FAISS.from_documents(documents, embedding_model)

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="Context: {context}\n\nQuestion: {question}\n\nAnswer:"
)

# Load the QA chain
qa_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)

class Query(BaseModel):
    question: str

@app.post("/support")
async def get_support_response(query: Query):
    # Retrieve similar documents
    similar_docs = vector_store.similarity_search(query.question, k=3)
    context = "\n".join([doc.page_content for doc in similar_docs])

    # Generate the response using the QA chain
    answer = qa_chain.run(input_documents=similar_docs, question=query.question)

    if answer:
        return {"answer": answer.strip()}
    else:
        raise HTTPException(status_code=500, detail="LLM service error")
