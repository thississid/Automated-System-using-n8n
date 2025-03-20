from fastapi import FastAPI, Request
import ollama
import pinecone

app = FastAPI()

# Initialize Pinecone for Knowledge Base
pinecone.init(api_key="your_pinecone_api_key", environment="your_env")
index = pinecone.Index("support-db")

@app.post("/support")
async def process_query(request: Request):
    data = await request.json()
    user_query = data["query"]

    # Step 1: Check past support tickets using Pinecone
    search_results = index.query(user_query, top_k=3, include_metadata=True)

    if search_results["matches"]:
        relevant_answers = [match["metadata"]["solution"] for match in search_results["matches"]]
    else:
        relevant_answers = ["No past solutions found."]

    # Step 2: Generate a response using Ollama
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant for customer support."},
            {"role": "user", "content": f"Query: {user_query}\nPast Solutions: {relevant_answers}"}
        ]
    )

    return {"response": response["message"]}
