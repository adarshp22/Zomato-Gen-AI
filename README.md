

# 🍽️ Kanpur Restaurant Assistant

A lightweight Retrieval-Augmented Generation (RAG) chatbot that answers questions about restaurants in **Kanpur**, India — built using a semantic search system and integrated with LLM (Groq API using LLaMA-3).

---

## 🚀 Features

- 🔎 Semantic search over restaurant data (ratings, price, cuisine, location)
- 💬 Chat UI with a RAG pipeline (retrieval + generation)
- 🧠 Uses `sentence-transformers` for vector similarity
- 🤖 Powered by Groq's LLaMA-3 models for fast and reliable responses
- 🎨 Zomato-style UI using Streamlit and custom CSS

---

## 🗂️ Project Structure

```
├── app.py                      # Streamlit app interface
├── data/
│   └── restaurant_data.csv     # Raw restaurant data (from Zomato scraping)
├── src/
│   ├── config.py               # Constants and configuration
│   ├── data_loader.py          # Preprocessing logic
│   ├── rag_pipeline.py         # RAG orchestration logic
│   └── vector_db.py            # Semantic vector store and search
└── README.md                   # You're here!
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/kanpur-restaurant-assistant.git
cd kanpur-restaurant-assistant
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

**Required Libraries:**
- `streamlit`
- `pandas`
- `sentence-transformers`
- `groq`
- `numpy`

You can also manually install:
```bash
pip install streamlit pandas sentence-transformers groq numpy
```

---

## 🔐 Set Groq API Key

Create a `.env` file (or export manually):

```bash
export GROQ_API_KEY=your_groq_api_key
```

If you're hardcoding it (for now), you can pass it in `rag_pipeline.py` under:

```python
Groq(api_key="your_key_here")
```

---

## 🧪 Run the App

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 💡 Example Queries

- `"Which restaurants in Tilak Nagar have high ratings?"`
- `"What is the price range of Punjab Grill?"`
- `"Which restaurants serve North Indian cuisine?"`

⚠️ Out-of-scope queries (e.g., contact info, opening hours, specific dishes) will be gracefully declined.

---

## 🧠 How It Works

1. **Data Loading**: `data_loader.py` loads and preprocesses the CSV, extracting location and creating `search_text`.
2. **Vector Embeddings**: `vector_db.py` uses `sentence-transformers` to embed the search text.
3. **Semantic Search**: A similarity search returns the top-matching restaurants.
4. **LLM Generation**: `rag_pipeline.py` formats context and sends it to Groq's LLaMA-3 for response generation.
5. **Chat UI**: `app.py` powers the Streamlit chatbot, with styled assistant and user messages.

---

## 📌 Configurable

All core config (like model name, CSV path, system prompt) is located in `src/config.py`.

---

## 🧹 Future Improvements

- Add vector index persistence
- Add support for filtering by cuisine or price
- Expand to more cities
- Add visual analytics (heatmaps, top cuisines, etc.)

---

## 🧑‍💻 Author

**Adarsh Pal**  
💼 [LinkedIn](https://linkedin.com/in/adarsh-pal-816764255) • 🧑‍💻 [GitHub](https://github.com/adarshp22)  
📫 adarshp22@iitk.ac.in

---

## 📄 License

MIT License — feel free to fork, clone, and customize!

--- 

Let me know if you'd like to auto-generate a `requirements.txt` from your code!
