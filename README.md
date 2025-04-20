# 🍽️ Kanpur Restaurant Assistant

A lightweight Retrieval-Augmented Generation (RAG) chatbot that answers questions about restaurants in **Kanpur**, India — built using a semantic search system and integrated with LLM (Groq API using LLaMA-3).

---

## 🚀 Features

- 🔎 Semantic search over restaurant data (ratings, price, cuisine, location)
- 💬 Chat UI with a RAG pipeline (retrieval + generation)
- 🤖 Powered by Groq's LLaMA-3 models for fast and reliable responses
- 🎨 Zomato-style UI using Streamlit and custom CSS

---

---

## 🛠️ Setup Instructions

1. **Clone the Repository**  
   Clone the project repository to your local machine.

2. **Install Requirements**  
   Install the necessary libraries by running the following command:

3. **Set Up the API Key**  
Create a `.env` file to store your Groq API key or manually update it in the `src/env_config.py` file.

---

## 🧪 Run the App that is main_app.py 

1. Run the following command to start the app:


2. Open your browser and visit `http://localhost:8501` to interact with the Kanpur Restaurant Assistant chatbot.

---

## 💡 Example Queries

- `"Which restaurants in Tilak Nagar Kanpur have high ratings?"`

Note: Out-of-scope queries will be declined.

---

## 🧠 How It Works

1. **Data Loading**: The data is loaded and preprocessed in `data_pipeline.py`.
2. **Vector Embeddings**: The `vector_db.py` generates embeddings of the restaurant data using `sentence-transformers`.
3. **Semantic Search**: The top-matching restaurants are fetched using vector similarity search.
4. **LLM Generation**: The RAG pipeline in `rag_generator.py` formats the response and uses Groq's LLaMA-3 for response generation.
5. **Chat UI**: The app is powered by Streamlit, providing an interactive user interface.

---

## 📌 Configurable

You can modify configurations like the model name, restaurant data file path, and system prompts in the `src/env_config.py` file.

---

## 🧹 Future Improvements

- Add vector index persistence
- Add support for filtering by cuisine or price
- Expand to more cities
- Add visual analytics (heatmaps, top cuisines, etc.)

---
## DEMO VIDEO LINK
 [demo_video](https://drive.google.com/file/d/1g1nrMgarzDeX1S4BBnr0SNFjPgwEO-He/view?usp=drive_link)
---

## 🧑‍💻 Author

**Adarsh Pal**  
💼 [LinkedIn](https://linkedin.com/in/adarsh-pal-816764255) • 🧑‍💻 [GitHub](https://github.com/adarshp22)  
📫 adarshp22@iitk.ac.in

---
