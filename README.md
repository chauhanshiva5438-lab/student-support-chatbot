# 🎓 Arizona State University Student Support Chatbot

An AI-powered Student Support Chatbot built using Retrieval-Augmented Generation (RAG). The chatbot answers student queries by retrieving relevant information from the Arizona State University Academic Catalog and generating accurate responses using Google's Gemini model.

---

## 🚀 Features

- RAG (Retrieval-Augmented Generation)
- FAISS Vector Search
- Sentence Transformers Embeddings
- Google Gemini Integration
- Streamlit Web Interface
- Semantic Search
- Context-based Question Answering

---

## 🛠 Tech Stack

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Google Gemini API
- NumPy
- JSON

---

## 📂 Project Structure

```
student_support_chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── src/
│   ├── rag_pipeline.py
│   └── gemini_client.py
│
├── scripts/
│   ├── create_embeddings.py
│   ├── build_faiss.py
│   └── ...
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── vector_store/
│
├── notebook/
├── reports/
└── images/
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone <repository-url>
cd student_support_chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 📚 Dataset

The chatbot uses the Arizona State University Academic Catalog as its knowledge base. The documents are processed into chunks, converted into embeddings using Sentence Transformers, indexed with FAISS, and queried during runtime.

---

## 📌 Future Improvements

- Hybrid Search (BM25 + FAISS)
- Conversation Memory
- Multi-document Support
- Citation Highlighting
- Admin Dashboard

---

## 👨‍💻 Author

Shiva Chauhan

B.Tech Computer Science (Data Science)