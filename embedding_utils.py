from sentence_transformers import SentenceTransformer

# Load the model once
# 'all-MiniLM-L6-v2' is a fast, lightweight model perfect for CPUs
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Converts a string of text into a vector (list of floats).
    """
    if not text:
        return []
    
    # Model.encode returns a numpy array, convert to list for DB storage
    return model.encode(text).tolist()

def get_embeddings(text_list):
    """
    Converts a list of strings into a list of vectors.
    """
    if not text_list:
        return []
    
    return model.encode(text_list).tolist()
