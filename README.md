# Kanpur Restaurant Information Assistant (Gen AI Project)

This project is a RAG-based system built for the Zomato Gen AI Internship assignment. It enables users to query restaurant-related information using natural language. The system integrates web scraping, vector databases, and a custom retrieval mechanism with a lightweight LLM-powered chatbot interface.

---

## 🚀 Features

- Scrapes and structures restaurant data from Zomato for Kanpur.
- Converts text chunks into vector embeddings using `HuggingFace`.
- Stores embeddings in a FAISS vector database for efficient similarity search.
- Implements a retrieval-augmented generation (RAG) approach to answer user queries.
- Modular design for easy extension and future improvements.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kanpur-restaurant-assistant.git
cd kanpur-restaurant-assistant
2. Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure Environment (if applicable)
If using OpenAI or any API-based LLMs, set your API key in a .env file:

env
Copy
Edit
OPENAI_API_KEY=your_key_here
⚙️ Usage Instructions
Step 1: Run Web Scraper
Scrape Zomato for restaurant data in Kanpur.

bash
Copy
Edit
python scraper.py
Step 2: Generate Embeddings
Convert restaurant info into embeddings and store in FAISS.

bash
Copy
Edit
python embedder.py
Step 3: Start the Assistant
Launch the query assistant to interact with your chatbot.

bash
Copy
Edit
python query_assistant.py
You’ll be prompted to enter a question like:

arduino
Copy
Edit
"Which restaurants in Kanpur offer North Indian food under ₹500?"
And the assistant will return the most relevant information.

📁 Project Structure
bash
Copy
Edit
kanpur-restaurant-assistant/
│
├── scraper.py               # Web scraping logic for Zomato Kanpur
├── embedder.py              # Converts data into vector embeddings and stores in FAISS
├── query_assistant.py       # Query interface powered by RAG
├── utils/                   # Helper functions
├── data/                    # Stores scraped raw and cleaned data
├── faiss_index/             # FAISS index files
├── requirements.txt         # Python dependencies
└── README.md                # You are here!
📌 Notes
Designed to be lightweight for fast iteration.

Can easily swap embedding model (e.g., sentence-transformers) or LLM backend (e.g., OpenAI, LLama, etc.).

Only tested on Linux and MacOS. Windows users may need slight modifications to path formats.

🔮 Future Improvements
Add user interface (web or CLI chatbot)

Integrate with real-time Zomato API (if accessible)

Improve retrieval accuracy using hybrid ranking

Extend coverage to other cities dynamically
