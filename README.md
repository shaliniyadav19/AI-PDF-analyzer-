# 📄 PDF Analyzer – Semantic PDF Search & Extractive Question Answering

An AI-powered document analysis application that enables users to upload PDF documents, perform semantic search, and retrieve exact answers from the document using an **Extractive Question Answering** pipeline.

The project implements the complete retrieval pipeline manually—from PDF parsing and text preprocessing to embedding generation, vector search with FAISS, and extractive question answering—without using high-level RAG frameworks.

---

# 🚀 Features

* Upload PDF documents
* Extract and preprocess PDF text
* Intelligent text chunking with overlap
* Generate semantic embeddings using Hugging Face Sentence Transformers
* Store embeddings in a FAISS vector index
* Perform semantic similarity search
* Extract exact answers using a Hugging Face Extractive QA model
* Display confidence score and source context
* Generate and download a PDF report

---

# 🏗️ System Workflow

```text
                  PDF Upload
                      │
                      ▼
              Text Extraction
                      │
                      ▼
             Text Preprocessing
                      │
                      ▼
         Chunking with Overlap
                      │
                      ▼
        Sentence Embedding Generation
                      │
                      ▼
          FAISS Vector Index
──────────────────────────────────────────

               User Question
                      │
                      ▼
          Question Embedding
                      │
                      ▼
      Semantic Similarity Search
                      │
                      ▼
          Top-K Relevant Chunks
                      │
                      ▼
      Extractive QA (RoBERTa)
                      │
                      ▼
   Exact Answer + Confidence Score
                      │
                      ▼
      Source Context & PDF Report
```

---

# 📂 Project Structure

```text
PDF-Analyzer/

│
├── app.py
├── requirements.txt
├── README.md
│
├── backend/
│   ├── pdf_parser.py
│   ├── text_cleaner.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── ex_qa.py
│   └── report_generator.py
│
├── uploads/
├── data/
│   └── reports/
│
└── assets/
```

---

# ⚙️ Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* Hugging Face Transformers
* Sentence Transformers

### Vector Search

* FAISS

### PDF Processing

* PyMuPDF
* pdfplumber

### Report Generation

* FPDF2

---

# 🧠 Pipeline Overview

### 1. PDF Processing

* Upload PDF
* Extract text
* Clean and normalize content

### 2. Text Chunking

* Split the document into fixed-size chunks
* Preserve context using overlapping chunks

### 3. Embedding Generation

* Convert each chunk into a dense vector representation
* Generate embeddings for user queries using the same model

### 4. Semantic Retrieval

* Store chunk embeddings in a FAISS index
* Retrieve the Top-K most relevant chunks based on vector similarity

### 5. Extractive Question Answering

Each retrieved chunk is passed to the QA model to predict:

* Answer span
* Confidence score

The highest-confidence answer is returned to the user.

### 6. Report Generation

Generate a downloadable PDF report containing:

* Question
* Extracted answer
* Confidence score
* Source context
* Retrieved chunks

---

# ▶️ Getting Started

## Clone the repository

```bash
git clone https://github.com/shaliniyadav19/PDF-Analyzer.git
```

## Navigate to the project

```bash
cd PDF-Analyzer
```

## Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 💻 How to Use

1. Upload a PDF document.
2. Click **Process PDF**.
3. Wait for text extraction, chunking, embedding generation, and indexing.
4. Enter a natural language question.
5. View:

   * Extracted Answer
   * Confidence Score
   * Source Context
   * Top Retrieved Chunks
6. Download the generated PDF report.

---

# 📌 Current Capabilities

* Semantic PDF Search
* Dense Vector Embeddings
* FAISS Vector Indexing
* Extractive Question Answering
* Confidence-based Answer Selection
* Source Context Retrieval
* PDF Report Generation

---

# 🚀 Future Scope

- Upgrade from **Extractive QA** to a **Generative RAG** system using Large Language Models (LLMs) to generate contextual and conversational answers.
- Enhance the user interface with a modern, responsive, and interactive design to improve the overall user experience.
- Support multiple PDF documents and cross-document semantic search.
- Integrate production-grade vector databases such as **Qdrant** or **Pinecone** for scalable retrieval.
- Add OCR support to process scanned PDFs and image-based documents.
- Implement hybrid retrieval by combining semantic search with keyword-based search.
- Containerize the application using Docker and deploy it on cloud platforms for scalability and easy access.

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Semantic Search
* Vector Embeddings
* FAISS Vector Databases
* Document Chunking
* Information Retrieval
* Extractive Question Answering
* Hugging Face Transformers
* Streamlit Application Development
* End-to-End AI Pipeline Design

---

# 📌 Note

This project focuses on building an **Extractive Question Answering** system. Unlike generative AI applications, it returns answers that exist within the uploaded document, ensuring responses remain grounded in the source content and reducing the likelihood of hallucinated information.
