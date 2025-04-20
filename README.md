
# Kanpur Zomato AI Assistent

This project provides a semantic search-based Restaurant Assistant application built using the Retrieval-Augmented Generation (RAG) pipeline. It leverages advanced Natural Language Processing (NLP) techniques and a vector database to provide restaurant-related information for users in Kanpur, India. The application is powered by data scraped from Zomato and allows users to ask various restaurant-related queries.

## Features

- **Restaurant Search**: Query information about restaurants based on various attributes such as ratings, price range, cuisines, and locations.
- **RAG Pipeline**: Utilizes a combination of a vector database and a pre-trained model to retrieve contextually relevant information and generate responses.
- **Streamlit Interface**: User-friendly chat interface built with Streamlit for real-time queries and responses.
- **Customizable Model**: The application uses the `all-MiniLM-L6-v2` sentence transformer model for generating restaurant embeddings and performing semantic search.



## Requirements

To run the application, ensure you have the following libraries installed:

- `streamlit`
- `pandas`
- `numpy`
- `sentence-transformers`
- `groq`
- `scikit-learn`

You can install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
Setup
Download Data: Ensure that the restaurant_data.csv file is located in the /data folder of the project.

Preprocessing: The data in the CSV file will be preprocessed automatically when the app starts. The preprocessing involves extracting restaurant location from the URL and creating a searchable text field.

Initialize Vector DB: When the app starts, the RestaurantVectorDB class builds the vector database from the preprocessed data. It uses the SentenceTransformer model to generate embeddings for each restaurant based on its name, cuisine, rating, and price.

Running the Application
Run the Streamlit application by executing the following command:

bash
Copy
Edit
streamlit run src/app.py
The app will open in your browser, where you can interact with the restaurant assistant. Type a query such as:

"Which restaurants in Tilak Nagar have high ratings?"

The application will respond based on the available restaurant data, returning the most relevant results.

RAG System Overview
The system uses a Retrieval-Augmented Generation (RAG) pipeline, which operates in the following steps:

Semantic Search: The query is converted into a vector embedding, and the vector database is searched for the most relevant entries (restaurants).

Context Formatting: The retrieved results are formatted and presented to the system in a manner that is compatible with the language model.

Response Generation: The formatted context is then passed to the Groq model (mocked for now) to generate a response based on the available information.

Customization
You can customize various components of the application:

Model: Modify the model used for embeddings by changing the EMBEDDING_MODEL parameter in the config.py file.

Prompt: Adjust the system prompt in config.py to change how the assistant behaves and what it can respond to.

Data: You can update the restaurant dataset in restaurant_data.csv to reflect new or more restaurant information.
