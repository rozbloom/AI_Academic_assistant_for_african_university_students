# AI_Academic_assistant_for_african_university_students
we students struggle with finding an AI to help explain concepts simply, to generate university standards questions, and summarizing lecture Pdfs. here is your solution then for all of it.  

here is the high level architecture diagram :
```yaml
                ┌──────────────────────┐
                │      Frontend        │
                │  (Next.js Web App)   │
                └─────────┬────────────┘
                          │ HTTPS API
                          ▼
                ┌──────────────────────┐
                │      Backend API     │
                │       FastAPI        │
                └─────────┬────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌───────────────┐ ┌───────────────┐ ┌────────────────┐
│ PostgreSQL    │ │ File Storage  │ │ Vector Database│
│ User data     │ │ PDFs          │ │ FAISS/Chroma   │
└───────────────┘ └───────────────┘ └────────────────┘
                                          │
                                          ▼
                                ┌────────────────┐
                                │ Embedding Model│
                                │ sentence-BERT  │
                                └────────────────┘
                                          │
                                          ▼
                                ┌────────────────┐
                                │ LLM (AI Engine)│
                                │ Answer Engine  │
                                └────────────────┘
```

Next step would be a deailed RAG pipeline design.

```yaml 
User uploads PDF
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embeddings Creation
      ↓
Store in Vector Database
      ↓
User asks question
      ↓
Similarity Search
      ↓
Send context to LLM
      ↓
Generate answer
```
