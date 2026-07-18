# 🎓 AI Student Support Chatbot

An AI-powered Student Support Chatbot built using Retrieval-Augmented Generation (RAG). The chatbot answers Arizona State University student queries using official university documents instead of relying only on a Large Language Model.

---

## 🚀 Features

- AI-powered question answering
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Search
- Sentence Transformers Embeddings
- Google Gemini API
- Streamlit Web Interface
- PDF + Website Knowledge Base
- Fast Semantic Search

---

## 🛠️ Tech Stack

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Google Gemini API
- Hugging Face
- BeautifulSoup
- PyMuPDF

---

## 📂 Project Structure

```
student-support-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│
├── scripts/
│
├── src/
│
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/chauhanshiva5438-lab/student-support-chatbot.git
```

Go to project

```bash
cd student-support-chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a .env file

```
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📚 Knowledge Sources

The chatbot uses:

- Arizona State University Official Website
- ASU Academic Catalog
- Student Services
- Tuition & Fees
- Admissions
- Financial Aid
- Housing
- Library
- Career Services
- Registration Guide

---

## 🤖 How it Works

1. Collect official university documents
2. Clean and preprocess text
3. Split documents into chunks
4. Generate embeddings
5. Store vectors in FAISS
6. Retrieve relevant chunks
7. Send retrieved context to Gemini
8. Generate final answer

---

## 📸 Screenshots

### Home Page

![Home](screenshots/home.png)

### Chat Example

![Chat](screenshots/chat.png)

### Another Example

![Example](screenshots/example.png)

## 🔮 Future Improvements

- Conversation Memory
- Hybrid Search (BM25 + FAISS)
- Better Reranking
- Multi-University Support
- Voice Assistant
- Authentication
- Admin Dashboard

---

## 👨‍💻 Author

Shiva Chauhan

B.Tech Computer Science (Data Science)