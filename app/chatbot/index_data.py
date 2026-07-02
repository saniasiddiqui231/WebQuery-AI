import json
import time
from pathlib import Path

from langchain_core.documents import Document

from app.chatbot.chunker import create_chunks
from app.chatbot.preprocessor import clean_text
from app.chatbot.vector_store import vector_store

# try:
#     vector_store.delete_collection()
# except Exception:
#     pass
# from app.chatbot.vector_store import vector_store

DATA_FILE = Path("data/raw/pages.json")

def load_pages():
    """Load all scraped website pages."""

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def batch_documents(documents, ids, batch_size=20):
    """Yield documents and IDs in batches."""

    for i in range(0, len(documents), batch_size):
        yield (
            documents[i:i + batch_size],
            ids[i:i + batch_size]
        )
      
# def load_website_data() -> str:
#     """Load the scraped website text."""

#     return DATA_FILE.read_text(encoding="utf-8")
def index_website():

    pages = load_pages()

    documents = []

    ids = []

    for page in pages:

        cleaned_text = clean_text(page["content"])

        chunks = create_chunks(cleaned_text)

        for index, chunk in enumerate(chunks):

            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "url": page["url"],
                        "title": page["title"]
                    }
                )
            )

            ids.append(
                f"{page['url']}_{index}"
            )
    try:
        vector_store.reset_collection()
    except Exception:
        pass
    from app.chatbot.vector_store import vector_store

    for batch_docs, batch_ids in batch_documents(documents, ids):

        vector_store.add_documents(
        documents=batch_docs,
        ids=batch_ids
    )

        print(f"Indexed {len(batch_docs)} documents...")

        time.sleep(2)
