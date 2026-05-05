# RAG API - Retrieval-Augmented Generation with PDFs

![RAG Pipeline](https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=RAG+Pipeline)

A FastAPI-based **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents, automatically process and store them in a vector database (Pinecone), and query them using a powerful LLM (Qwen2.5-7B-Instruct) for contextually grounded responses.

## 🚀 Features

- **PDF Upload & Processing**: Securely upload PDFs, extract text, chunk, clean, and embed into Pinecone vector store.
- **RAG Pipeline**: Retrieve relevant document chunks (top-3 similarity) and generate answers using HuggingFace-hosted LLM.
- **RESTful API**: Simple endpoints for upload (`/api/upload`) and chat (`/rag/chat`).
- **Production-Ready**: FastAPI with automatic docs (Swagger UI), uvicorn server, .env config.
- **Modern Stack**: LangChain, Sentence Transformers embeddings, Pinecone, no local GPU required.

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Framework** | FastAPI |
| **Vector DB** | Pinecone |
| **Embeddings** | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| **LLM** | `Qwen/Qwen2.5-7B-Instruct` (HuggingFaceEndpoint) |
| **PDF Loader** | PyPDFLoader + RecursiveCharacterTextSplitter (500 chunk/100 overlap) |
| **Deployment** | Uvicorn |

## 📦 Quick Start

### 1. Prerequisites
- Python 3.12+
- [Pinecone Account](https://www.pinecone.io/) & API Key
- [HuggingFace Account](https://huggingface.co/) & API Token

### 2. Clone & Install
```bash
git clone <repo>
cd rag
# Using uv (recommended) or pip
uv sync  # or pip install -r requirements.txt
```

### 3. Environment Setup
Create `.env`:
```
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX_NAME=your_index_name  # Dimension: 384 for MiniLM
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

**Note**: Create Pinecone index with 384 dimensions (matches embedding model).

### 4. Run Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
# or
uvicorn main:app --reload
```

Open http://localhost:8000/docs for **Swagger UI** & interactive API testing.

### 5. API Usage

#### Upload PDF
```
POST /api/upload
Content-Type: multipart/form-data
```
- Body: PDF file
- Response: `{\"message\": \"File uploaded Successfully\", \"data\": {\"file_id\": \"...\", \"filename\": \"...\", \"path\": \"...\"}}`

PDF is auto-chunked, embedded, stored, and local file deleted.

#### RAG Chat
```
POST /rag/chat
Content-Type: application/json
```
Body:
```json
{\"message\": \"What is the main topic of the document?\"}
```
Response:
```json
{
  \"question\": \"What is the main topic?\",
  \"answer\": \"Generated answer based on retrieved context...\"
}
```

## 🏗 Architecture

```
┌─────────────────┐    POST /api/upload    ┌──────────────────┐
│   Upload PDF    ├───────────────────────►│   save_file()    │
└─────────────────┘                        │  ├─ PyPDFLoader   │
                                           │  ├─ Chunk (500/100)│
                                           │  └─ store_pinecone │
                                           └──────────────────┘
                                                      │
POST /rag/chat ────► ┌──────────────┐                ▼
                      │ get_retriever│ ◄─────────────┐
                      │  (top-3 sim) │               │
                      └──────┬───────┘               │
                             │                        │
                      ┌──────▼───────┐               │
                      │  mychat()    │               │
                      │ ├─ Retrieve   │               │
                      │ ├─ Prompt LLM │               │
                      │ └─ Qwen2.5    │               │
                      └───────────────┘               │
                             │                        │
                      ┌──────▼───────┐               │
                      │   Response   │◄───────────────┘
                      └───────────────┘
```

## 📁 Project Structure
```
rag/
├── main.py                 # FastAPI app entry
├── pyproject.toml          # Dependencies (uv)
├── requirements.txt        # Legacy pip deps
├── src/
│   ├── config/             # Embeddings, LLM, DB config
│   ├── loaders/            # PDF loader + chunking
│   ├── routes/             # /api/upload, /rag/chat
│   ├── schema/             # Pydantic models
│   ├── service/            # PDF/RAG business logic
│   └── vectordb/           # Pinecone store/retrieve
├── uploads/                # Temp PDF storage (auto-delete)
└── README.md
```

## ⚙ Configuration

| Env Var | Description | Required |
|---------|-------------|----------|
| `PINECONE_API_KEY` | Pinecone project key | ✅ |
| `PINECONE_INDEX_NAME` | Index name (dim=384) | ✅ |
| `HUGGINGFACEHUB_API_TOKEN` | HF API token | ✅ |

## 🧪 Testing

```bash
# Install test deps if added
uv run pytest  # Add tests/ dir for full coverage
```

API tests via Swagger: http://localhost:8000/docs

## 🔒 Security Notes
- PDF-only uploads (validated).
- Local files auto-deleted after processing.
- No persistent storage beyond vector DB.
- Rate limiting recommended for prod (add slowapi).

## 🚀 Deployment
- **Docker**: Add Dockerfile.
- **Railway/Vercel/Render**: Set env vars, `uvicorn main:app`.
- **Scaling**: Pinecone serverless scales automatically.

## 🤝 Contributing
1. Fork & PR.
2. Add tests.
3. Update README.

## 📄 License
MIT (add LICENSE file).

## 🙏 Acknowledgments
Built with ❤️ using FastAPI, LangChain, Pinecone, HuggingFace.

---

**Ready to RAG!** Upload your PDFs and start querying. Questions? Check API docs.

