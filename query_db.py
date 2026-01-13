from db_utils import get_collection
from embedding_utils import get_embedding

def search_documents(query, n_results=3, **kwargs):
    """
    Searches the vector database for the most relevant document chunks.
    """
    print(f"🔍 SEARCHING: '{query}'")
    
    # 1. Convert Query to Embedding
    query_embedding = get_embedding(query)
    
    # 2. Search Database
    collection = get_collection()
    
    # Optional: Filter by Metadata (e.g., Department)
    where_filter = kwargs.get("where", None)
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        where=where_filter # <--- Pass the filter to ChromaDB
    )
    
    # 3. Process Results
    # ChromaDB returns lists of lists (one list per query)
    documents = results['documents'][0]
    metadatas = results['metadatas'][0]
    distances = results['distances'][0] # Smaller distance = better match
    
    print(f"   -> Found {len(documents)} results.")
    
    formatted_results = []
    
    for i in range(len(documents)):
        doc_text = documents[i]
        meta = metadatas[i]
        score = 1 - distances[i] # Approximate similarity score
        
        result = {
            "content": doc_text,
            "source": meta['source'],
            "source_dept": meta.get('department', 'General'), # Extract department
            "score": score
        }
        formatted_results.append(result)
        
        print(f"\n   [{i+1}] {meta['source']} (Score: {score:.4f})")
        print(f"       \"{doc_text[:100]}...\"")
        
    return formatted_results

if __name__ == "__main__":
    # Test Queries
    print("------------------------------------------------")
    search_documents("What is the budget for the toaster project?")
    
    print("\n------------------------------------------------")
    search_documents("policies about ai tools")
