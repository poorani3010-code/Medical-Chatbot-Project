import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import os

# 1. Folder check
if not os.path.exists('vectorstore'):
    os.makedirs('vectorstore')

# 2. Excel/CSV Loading
print("Loading your CSV data...")
# Unga file name 'sample_medical.csv' nu inga sariya kudunga
df = pd.read_csv("Data/sample_medical.csv") 

# 3. Converting Excel rows to AI text
documents = []
for index, row in df.iterrows():
    # Ella columns-aiyum sethu oru paragraph-ah mathurom
    combined_text = " ".join(str(value) for value in row.values)
    documents.append(Document(page_content=combined_text))

print(f"Total {len(documents)} rows ready for the brain.")

# 4. Creating the Brain
print("Creating AI database... Please wait.")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = FAISS.from_documents(documents, embeddings)
db.save_local("vectorstore/db_faiss")

print("---------------------------------------")
print("SUCCESS! Your CSV Medical Brain is Ready!")
print("---------------------------------------")