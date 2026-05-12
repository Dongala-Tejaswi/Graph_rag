# Graph_rag
Graph RAG using FastAPI, Neo4j, Sentence Transformers & LLM

A Graph-based Retrieval Augmented Generation (Graph RAG) system built using:

FastAPI
Neo4j Graph Database
Sentence Transformers
Vector Embeddings
LLM Integration
Docker
Python
🚀 Features
Graph-based knowledge retrieval
Neo4j relationship storage
Semantic search using embeddings
FastAPI backend APIs
Dockerized deployment
Context retrieval pipeline
LLM answer generation
Graph relationship visualization
🏗️ Architecture

User Query
↓
Embedding Generation
↓
Vector Similarity Search
↓
Neo4j Graph Retrieval
↓
Context Aggregation
↓
LLM Response Generation

📂 Project Structure
graph_rag/
│
├── backend/
│   ├── graph/
│   │   └── neo4j_graph.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── llm/
│   │   └── llm_engine.py
│   │
│   ├── embeddings/
│   │   └── embedding_model.py
│   │
│   └── main.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
⚙️ Installation
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/graph_rag.git
cd graph_rag
2. Create Virtual Environment
python -m venv venv

Activate virtual environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
🐳 Docker Setup

Build Docker image:

docker compose build

Run containers:

docker compose up

Check running containers:

docker ps
🧠 Neo4j Setup

Run Neo4j using Docker:

docker run \
--name neo4j \
-p7474:7474 -p7687:7687 \
-e NEO4J_AUTH=neo4j/password \
-d neo4j

Neo4j Browser:

http://localhost:7474

Login:

Username: neo4j
Password: password
🔐 Environment Variables

Create .env file:

NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password
▶️ Run Backend
python -m uvicorn backend.main:app --reload

Server:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs
📊 Neo4j Queries

View nodes:

MATCH (n)
RETURN n;

View relationships:

MATCH (a)-[r]->(b)
RETURN a,r,b;
🧠 Technologies Used
Python
FastAPI
Neo4j
Docker
Sentence Transformers
Hugging Face
Uvicorn
Graph RAG
Vector Search
LLMs
📌 Current Progress
Neo4j integration completed
Graph relationships created
Retrieval pipeline implemented
Docker setup completed
FastAPI backend running
Embedding model integrated
Context retrieval working
