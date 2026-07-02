from langchain_chroma import Chroma

from app.chatbot.embeddings import embedding_model

DB_PATH = "chroma_db"

COLLECTION_NAME = "website_data"

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=DB_PATH,
    embedding_function=embedding_model,
)