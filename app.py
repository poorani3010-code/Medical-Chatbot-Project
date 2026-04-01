import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from deep_translator import GoogleTranslator

# 1. Page Config and Title (PDF Requirement)
st.set_page_config(page_title="Medical Chatbot", layout="centered")
st.title("Multilingual Medical Support Chatbot 🏥")

# Medical Disclaimer (MUST have for submission)
st.warning("⚠️ **Disclaimer:** This chatbot provides basic medical information only. It is not a substitute for professional medical advice, diagnosis, or treatment.")

# 2. Load AI Model with Cache
@st.cache_resource
def load_ai_model():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vectorstore/db_faiss", embeddings, allow_dangerous_deserialization=True)
    return db

db = load_ai_model()

# 3. Translation Function
def translate_text(text, target_lang):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

# 4. Chat Interface
user_query = st.text_input("How can I help you today? / நான் உங்களுக்கு எப்படி உதவ முடியும்?")

if user_query:
    with st.spinner("Processing..."):
        # Step 1: Detect and Translate Input to English (PDF Requirement 1)
        translated_query = translate_text(user_query, 'en')
        
        # Step 2: Search Database (PDF Requirement 2)
        docs = db.similarity_search(translated_query)
        
        if docs:
            response_en = docs[0].page_content
            
            # Step 3: Translate Response back to User's Language (PDF Requirement 3)
            # Input Tamil-na output-um Tamil-la varum
            final_response = translate_text(response_en, target_lang='ta' if any(ord(c) > 128 for c in user_query) else 'en')
            
            st.write("### Answer:")
            st.write(final_response)
        else:
            st.write("Sorry, I couldn't find information on that.")