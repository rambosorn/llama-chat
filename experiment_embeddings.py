from embedding_utils import get_embedding
from scipy.spatial.distance import cosine
import time

def experiment():
    print("🧠 STARTING EMBEDDING EXPERIMENT")
    print("================================")
    
    # Test Data
    words = ["King", "Queen", "Apple", "Fruit", "Car"]
    
    print(f"Generating embeddings for: {words}")
    start_time = time.time()
    embeddings = {}
    for w in words:
        embeddings[w] = get_embedding(w)
    print(f"✅ Embeddings generated in {time.time() - start_time:.4f} seconds.\n")
    
    # Check Dimensions
    vec_len = len(embeddings["King"])
    print(f"Vector Dimensions: {vec_len} (This is the 'math' representation of the word 'King')\n")
    
    # Similarity Test Helper
    def check_similarity(word1, word2):
        # Cosine distance is 1 - similarity. So smaller distance = more similar.
        dist = cosine(embeddings[word1], embeddings[word2])
        similarity = 1 - dist
        print(f"Sim({word1}, {word2}) = {similarity:.4f}")
        return similarity

    print("--- Semantic Tests ---")
    
    # Test 1: Synonyms/Related
    s1 = check_similarity("King", "Queen")
    
    # Test 2: Unrelated
    s2 = check_similarity("King", "Apple")
    
    # Test 3: Categories
    s3 = check_similarity("Apple", "Fruit")
    s4 = check_similarity("Car", "Fruit")

    print("\n--- Analysis ---")
    if s1 > s2:
        print("✅ SUCCESS: AI understands that 'King' is closer to 'Queen' than 'Apple'.")
    else:
        print("❌ FAILURE: Semantic meaning not captured.")
        
    if s3 > s4:
        print("✅ SUCCESS: AI understands that 'Apple' is a 'Fruit' (and 'Car' is not).")
        
if __name__ == "__main__":
    experiment()
