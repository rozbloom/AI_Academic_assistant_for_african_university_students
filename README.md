# AI_Academic_assistant_for_african_university_students
we students struggle with finding an AI to help explain concepts simply, to generate university standards questions, and summarizing lecture Pdfs. here is your solution then for all of it.  

here is the high level architecture diagram :
```mermaid
flowchart TD
    A[Frontend<br>Next.js web app] -->|HTTPS API| B[Backend<br>FastAPI]
    B --> C[(PostgreSQL <br> userdata)]
    B --> D[(File Storage<br>PDFs)]
    B --> E[(Vector DB<br>FAISS/Chroma)]
    E --> F[Embedding<br>sentence-BERT]
    F --> G[LLM / Answer Engine]

    linkStyle default stroke:#555,stroke-width:1.5px
```

Next step would be a deailed RAG pipeline design.

```mermaid
flowchart TD
A[Upload PDF] --> B[Extract Text]
B --> C[Chunk Text]
C --> D[Create Embeddings]
D --> E[Store in Vector DB]
E --> F[User Question]
F --> G[Similarity Search]
G --> H[LLM Answer]
```
