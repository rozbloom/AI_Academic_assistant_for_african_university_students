# AI_Academic_assistant_for_african_university_students
we students struggle with finding an AI to help explain concepts simply, to generate university standards questions, and summarizing lecture Pdfs. here is your solution then for all of it.  

here is the high level architecture diagram :
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