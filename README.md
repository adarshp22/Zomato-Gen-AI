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

├── main_app.py                  # Streamlit app interface
├── data/
│   └── restaurant_data.csv      # Raw restaurant data (from Zomato scraping)
├── src/
│   ├── env_config.py            # Constants and configuration
│   ├── data_pipeline.py         # Preprocessing logic
│   ├── rag_generator.py         # RAG orchestration logic
│   └── vector_db.py             # Semantic vector store and search
└── README.md                    # You're here!

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
Required Libraries:

streamlit

pandas

sentence-transformers

groq

numpy

You can also manually install:

bash
Copy
Edit
pip install streamlit pandas sentence-transformers groq numpy
🔐 Set Groq API Key
Create a .env file (or export manually):

bash
Copy
Edit
export GROQ_API_KEY=your_groq_api_key
If you're hardcoding it (for now), you can pass it in rag_generator.py under:

python
Copy
Edit
Groq(api_key="your_key_here")
🧪 Run the App
bash
Copy
Edit
streamlit run main_app.py
Open http://localhost:8501 in your browser.

💡 Example Queries
"Which restaurants in Tilak Nagar Kanpur have high ratings?"

⚠️ Out-of-scope queries (e.g., contact info, opening hours, specific dishes) will be gracefully declined.

🧠 How It Works
Data Loading: data_pipeline.py loads and preprocesses the CSV, extracting location and creating search_text.

Vector Embeddings: vector_db.py uses sentence-transformers to embed the search text.

Semantic Search: A similarity search returns the top-matching restaurants.

LLM Generation: rag_generator.py formats context and sends it to Groq's LLaMA-3 for response generation.

Chat UI: main_app.py powers the Streamlit chatbot, with styled assistant and user messages.

📌 Configurable
All core config (like model name, CSV path, system prompt) is located in src/env_config.py.

🧹 Future Improvements
Add vector index persistence

Add support for filtering by cuisine or price

Expand to more cities

Add visual analytics (heatmaps, top cuisines, etc.)

🧑‍💻 Author
Adarsh Pal
💼 LinkedIn • 🧑‍💻 GitHub
📫 adarshp22@iitk.ac.in

