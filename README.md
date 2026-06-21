# WebQuery-AI

AI-powered chatbot that answers customer queries using information extracted from a company's website. The system processes website content, prepares it for retrieval, and will later use Large Language Models (LLMs) to provide accurate responses based on company-specific data.

## 🚧 Project Status

**Under Development**  
Completed up to **Phase 5: Text Chunking and Chunk Storage**

---

## 📌 Features

### Completed
- Website content extraction
- Data cleaning and preprocessing
- Text chunking
- Chunk storage in JSON format

### Planned
- Embedding generation
- Vector database integration (ChromaDB)
- Semantic search
- Gemini/OpenAI integration
- Customer support chatbot
- Lead collection system
- Web deployment

---

## 🛠️ Tech Stack

- Python
- BeautifulSoup
- Requests
- JSON
- LangChain (Upcoming)
- ChromaDB (Upcoming)
- Gemini API (Upcoming)
- Flask/FastAPI (Upcoming)

---

## 📂 Project Structure

```text
WebQuery-AI/
│
├── extraction/
│   └── extract_data.py
│
├── chunking/
│   └── chunk_data.py
│
├── data/
│   ├── extracted_data.json
│   └── chunks.json
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Workflow

```text
Website URL
     │
     ▼
Data Extraction
     │
     ▼
Data Cleaning
     │
     ▼
Text Chunking
     │
     ▼
Chunk Storage
     │
     ▼
Embeddings (Upcoming)
     │
     ▼
Vector Database (Upcoming)
     │
     ▼
Semantic Search (Upcoming)
     │
     ▼
LLM Response Generation (Upcoming)
```

---

## ✅ Completed Phases

### Phase 1: Project Setup
- Created project directory structure
- Configured Python environment
- Installed required dependencies

### Phase 2: Website Data Extraction
- Scraped website content using BeautifulSoup
- Extracted relevant textual information
- Stored extracted data in JSON format

### Phase 3: Data Cleaning
- Removed unwanted HTML elements
- Cleaned and standardized extracted text
- Prepared content for processing

### Phase 4: Text Chunking
- Split large text into smaller chunks
- Optimized chunk size for retrieval and embedding generation
- Improved data organization

### Phase 5: Chunk Storage
- Stored generated chunks in JSON format
- Successfully processed and saved chunked data
- Generated 2702 chunks for further processing

---

## 🚀 Upcoming Phases

### Phase 6
- Generate embeddings using embedding models

### Phase 7
- Store embeddings in ChromaDB

### Phase 8
- Implement semantic similarity search

### Phase 9
- Integrate Gemini/OpenAI API

### Phase 10
- Develop chatbot backend using Flask/FastAPI

### Phase 11
- Create chatbot frontend interface

### Phase 12
- Implement lead collection system

### Phase 13
- Deploy application

---

## 🎯 Project Goal

To build an intelligent AI chatbot capable of answering customer queries using information extracted directly from a company's website through Retrieval-Augmented Generation (RAG).

---

## 👥 Contributors

- Sara Maryam
- Sania siddiqui
- Hidayah Kaunain