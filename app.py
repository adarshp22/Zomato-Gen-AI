


# File: app.py
import streamlit as st
from src.data_loader import load_and_preprocess_data
from src.vector_db import RestaurantVectorDB
from src.rag_pipeline import RAGSystem
from src.config import CSV_PATH, SYSTEM_PROMPT, EMBEDDING_MODEL

# Custom CSS for consistent styling
st.markdown("""
<style>
    [data-testid=stAppViewContainer] {
        background-color: #DD3A58;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .stChatInput {
        background-color: #FFFFFF;
        border-radius: 25px;
        padding: 20px;
        margin-top: 30px;
    }
    .stChatMessage {
        border-radius: 25px!important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1)!important;
    }
    [data-testid="stChatMessage"] {
        max-width: 70%;
    }
    [data-testid="stChatMessage"][aria-label="Posted by assistant"] {
        margin-left: 30%;
        background-color: #E2374410;
    }
    [data-testid="stChatMessage"][aria-label="Posted by user"] {
        margin-right: 30%;
        background-color: #E2374410;
    }
</style>
""", unsafe_allow_html=True)

# Initialize RAG system
@st.cache_resource
def initialize_rag():
    df = load_and_preprocess_data(CSV_PATH)
    vector_db = RestaurantVectorDB(EMBEDDING_MODEL)
    vector_db.build_from_dataframe(df)
    return RAGSystem(vector_db, SYSTEM_PROMPT)

rag_system = initialize_rag()

# Chat interface setup
st.title("🍽️ Kanpur Zomato AI")
st.caption("Ask about restaurants in Kanpur")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# Process user input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get RAG response
    try:
        response = rag_system.generate_response(prompt)
        
        # Format response with Markdown
        formatted_response = response.replace('₹', '💰 ').replace('rating', '⭐').replace('Rating', '⭐')
        formatted_response = formatted_response.replace(' - ', '  \n• ')  # Line breaks for lists
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(f"""
            <div style='line-height: 1.6; color:#FFFFFF; background: #E2374410'>
                {formatted_response}
            </div>
            """, unsafe_allow_html=True)
        
        # Add to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": formatted_response
        })
        
    except Exception as e:
        st.error(f"Error processing request: {str(e)}")


