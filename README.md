# Automated-System-using-n8n

An **open-source AI-powered customer support system** that utilizes a **local LLM** (via **Ollama**) combined with **LangChain FAISS** as an **in-memory vector store** to retrieve past support solutions. The system is built with **FastAPI** for the backend and uses **n8n** for workflow automation. The entire setup is **containerized using Docker Compose** for easy deployment and scalability.  

---

## **🚀 Features**  

✅ **Local LLM with Ollama** – Runs models like **Mistral locally**, eliminating API costs.  
✅ **Knowledge Base** – Uses **LangChain FAISS** to store and retrieve past support queries and solutions.  
✅ **FastAPI Backend** – Processes customer queries, searches the knowledge base, and generates AI-driven responses.  
✅ **n8n Workflow Automation** – Automates query handling, response generation, and email/messaging notifications.  
✅ **Dockerized Deployment** – Uses **Docker Compose** to seamlessly manage all services.  

---

## **📂 Project Workflow**  

1. **Customer Query Handling** – A user submits a query via **n8n Webhook**.  
2. **Processing & Retrieval** – **FastAPI backend** searches the in-memory vector database (FAISS) for similar past queries.  
3. **AI-Powered Response Generation** – **Ollama LLM** generates a response based on the query and retrieved solutions.  
4. **Response Delivery** – The generated response is sent back to the user via **email, chat, or another preferred method** using n8n.  
5. **Containerized System** – **Docker Compose** ensures that all components (Ollama, FastAPI, n8n) run efficiently and communicate seamlessly.  

---

## **🛠️ Installation & Setup**  

### **1️⃣ Prerequisites**  

Ensure you have the following installed:  

- [Docker & Docker Compose](https://docs.docker.com/get-docker/)  
- [Ollama](https://ollama.com/)  

---

### **2️⃣ Clone the Repository**  

```bash
git clone https://github.com/your-username/Automated-Support-AI.git
cd Automated-Support-AI

### **3️⃣ Set Up Ollama **  
Install Ollama and pull a model (e.g., Mistral):  

```bash
ollama pull mistral
### ** 4️⃣ Run the FastAPI Backend **
Navigate to the backend/ directory and install dependencies:
```bash
cd backend
pip install -r requirements.txt

Run the FastAPI server:
```bash
uvicorn main:app --reload
### ** 5️⃣ Set Up n8n Workflow **
- Open n8n UI at http://localhost:5678/.
- Import the workflow file: workflows/support-workflow.json.
- Configure webhook and response handling in n8n.

### ** 6️⃣ Access the Services **
- FastAPI Backend: http://localhost:8000
- n8n UI: http://localhost:5678

## **✅ Summary of Additions:**
✔ **Included all necessary commands**  
✔ **Step-by-step installation guide**  
✔ **How to start the project manually & using Docker**  
✔ **How to set up n8n & Ollama**  
