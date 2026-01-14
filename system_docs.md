# 📘 Cambot AI - System Documentation

**Version:** 1.2.0  
**Last Updated:** January 2026

---

## 🏗️ 1. System Architecture

Cambot AI is a **Retrieval-Augmented Generation (RAG)** chatbot designed to act as an intelligent corporate consultant. It integrates a local knowledge base with an LLM to provide role-specific, reasoned answers.

```mermaid
graph TD
    User[User (Web/Mobile)] -->|HTTP Request| app_py[Flask Server (app.py)]
    
    subgraph "Backend Core"
        app_py -->|1. Route Request| RAG[RAG Pipeline (rag_pipeline.py)]
        RAG -->|2. Analyze Intent| Router[Intent Router]
        Router -->|3. Query Vector DB| Chroma[ChromaDB (Vector Store)]
        Chroma -->|4. Retrieve Documents| RAG
        RAG -->|5. Augment Prompt| LLM[Ollama (Llama 3.2)]
    end
    
    subgraph "Security Layer"
        Env[.env File] -- Load Secrets --> app_py
    end
    
    LLM -->|6. Generate Response| RAG
    RAG -->|7. JSON Response| app_py
    app_py -->|8. Render UI| User
```

---

## 🛠️ 2. Technology Stack

*   **Frontend:** HTML5, CSS3 (Variables, Flexbox/Grid), JavaScript (Vanilla).
*   **Backend:** Python 3.12+, Flask.
*   **AI/ML:**
    *   **LLM:** Ollama (Llama 3.2 model).
    *   **Vector DB:** ChromaDB (Persistent).
    *   **Embeddings:** SentenceTransformer (`all-MiniLM-L6-v2`).
*   **Security:** `python-dotenv` for secrets management.

---

## 📂 3. Project Structure

```text
d:/lama/
├── app.py                 # Main Flask Application (Routes, Auth)
├── rag_pipeline.py        # Core Logic: Intent Routing, Prompting, RAG
├── query_db.py            # Utility to search ChromaDB directly
├── populate_database.py   # Script to ingest PDF/TXT/CSV into ChromaDB
├── test_reasoning.py      # Automated test for logic verification
├── db_utils.py            # Database connection helper
├── embedding_utils.py     # Embedding generation helper
├── requirements.txt       # Python Dependencies
├── .env                   # Secrets (Excluded from Git)
├── documents/             # Knowledge Base (Categorized by Dept)
│   ├── HR/
│   ├── IT/
│   └── ...
├── templates/
│   ├── index.html         # Main Chat UI (Desktop/Mobile)
│   └── login.html         # Login Page
└── chroma_db/             # Vector Database Storage (Created at runtime)
```

---

## ✨ 4. Key Features

### 🧠 A. Consultative Reasoning
Unlike standard chatbots, Cambot AI structures its response into three distinct parts:
1.  **🎯 Answer:** The direct factual response based *only* on retrieved documents.
2.  **💡 Recommendation:** Proactive advice derived from the context (e.g., "Check the budget policy").
3.  **⚖️ Logical Reasoning:** Explanation of *why* the recommendation was made (e.g., "Spending exceeds Q4 limits").

### 🎭 B. Multi-Agent Routing
The system dynamically selects a "Persona" based on the user's query intent:
*   **Executive:** Access to all files, synthesizes high-level strategy (Profit vs Budget).
*   **HR:** Strict adherence to policy documents.
*   **IT:** Technical support focus.
*   **Sales:** Growth and metrics focus.

### 📱 C. Adaptive UI (Mobile & Desktop)
*   **Desktop:** Fullsidebar with "Toggle" button to collapse/expand.
*   **Mobile:** "Drawer" style navigation. Hidden by default, slides in via Hamburger menu.
*   **Night Mode:** System-wide dark theme preference (persisted in LocalStorage).

### 🔒 D. Security Hardening
*   **No Hardcoded Secrets:** All sensitive keys (`FLASK_SECRET_KEY`, `ADMIN_PASS`) are loaded from `.env`.
*   **Debug Mode Disabled:** `FLASK_DEBUG=False` by default for production safety.
*   **Hallucination Control:** Strict temperature (`0.1`) and relevance filters to prevent inventing facts.

---

## 🚀 5. Installation & Setup

### Prerequisites
*   Python 3.10+
*   Ollama (installed and running `llama3.2`)
*   Git

### Steps
1.  **Clone Repository:**
    ```bash
    git clone https://github.com/rambosorn/llama-chat.git
    cd llama-chat
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment:**
    Create a `.env` file in the root:
    ```ini
    FLASK_SECRET_KEY=your_secure_random_string
    ADMIN_USER=rambo
    ADMIN_PASS=123
    FLASK_DEBUG=False
    ```

4.  **Ingest Data:**
    Place your `.pdf`, `.txt`, or `.csv` files in `documents/` folders, then run:
    ```bash
    python populate_database.py
    ```

5.  **Run Application:**
    ```bash
    python app.py
    ```
    Access at: `http://localhost:5000`

---

## 🔧 6. API Documentation

### `POST /ask`
Submit a query to the AI agent.

**Request:**
```json
{
  "question": "What is the budget for Project Pegasus?"
}
```

**Response:**
```json
{
  "answer": "**🎯 Answer:** ... \n **💡 Recommendation:** ...",
  "time_taken": "2.45s",
  "metrics": {
    "department": "Executive",
    "retrieval_time": 0.3,
    "generation_time": 2.1
  }
}
```

---

## ⚠️ 7. Troubleshooting

*   **"No relevant documents found":**
    *   Check if files are in `documents/`.
    *   Run `python populate_database.py --reset` to rebuild the index.
    *   Check `valid_results` threshold in `rag_pipeline.py`.

*   **Menu Not Showing on Mobile:**
    *   Ensure browser window is < 1024px width.
    *   Clear browser cache (Ctrl + F5).
    *   Restart server (`python app.py`) to apply HTML changes.

*   **Ollama Connection Error:**
    *   Ensure Ollama is running (`ollama serve`).
    *   Check if `llama3.2` model is pulled (`ollama pull llama3.2`).
