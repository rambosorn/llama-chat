import chromadb
import os

# Store the database locally in the 'chroma_db' folder
DB_PATH = os.path.join(os.getcwd(), "chroma_db")

def get_db_client():
    """Initializes and returns the persistent ChromaDB client."""
    return chromadb.PersistentClient(path=DB_PATH)

def get_collection(name="techcorp_docs"):
    """Gets or creates the specified collection."""
    client = get_db_client()
    return client.get_or_create_collection(name=name)

def reset_db():
    """Resets the database (useful for testing)."""
    client = get_db_client()
    client.reset()
