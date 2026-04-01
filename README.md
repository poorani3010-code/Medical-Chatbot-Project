My Medical Chatbot Project


What it is?
I creacted this vhatbot to help people find basic medical information easily. the best part is that it works in two languages:English and Tamil.if you ask a question in tamil, it will give the answer back in tamil.


How i built it?
I used Python ans some AI tools like LangChain and Streamlit. I also used a translator libraryso it can umderstand both languages.


How to use it?

If you want to run this on your laptop:
1. Download all the files from this Github.
2. Install the needs by typing:pip install-r requirements.txt.
3. Run the app using:streamlit run app.py


My Files:


app.py:  This is my main code for the chatbot screen.

ingest.py: I used this to process the medical data.

requirements.txt: This has the list of libraries i used.

vectorstore: This folder stores the information the chatbot uses to answer.

Data: This folder has the medical CSV file.


Tools i used:
1. Python
2. Streamlit(for the website)
3. LangChain(for AI)
4. Deep-Translator(for Tamil support)
