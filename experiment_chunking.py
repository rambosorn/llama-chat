import os
from chunking_utils import recursive_character_text_splitter

DOCS_DIR = os.path.join(os.getcwd(), "documents")

def load_documents():
    docs = {}
    if not os.path.exists(DOCS_DIR):
        print("No documents found!")
        return docs
        
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".txt"):
            path = os.path.join(DOCS_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                docs[filename] = f.read()
    return docs

def  experiment():
    print("🧪 STARTING CHUNKING EXPERIMENT")
    print("================================")
    
    documents = load_documents()
    if not documents:
        return

    # Strategy 1: Small Chunks (Good for precise facts)
    print("\n🔵 Strategy 1: Micro Chunks (Size=100, Overlap=20)")
    print("   -> Best for: Extracting specific numbers or dates.")
    sample_text = documents.get("techcorp_policy.txt", "")
    chunks = recursive_character_text_splitter(sample_text, 100, 20)
    for i, chunk in enumerate(chunks[:3]): # Show first 3
        print(f"   [Chunk {i+1}]: {repr(chunk)}")

    # Strategy 2: Medium Chunks (Balanced)
    print("\n🟢 Strategy 2: Paragraph Chunks (Size=300, Overlap=50)")
    print("   -> Best for: General QA and context.")
    sample_text = documents.get("project_pegasus.txt", "")
    chunks = recursive_character_text_splitter(sample_text, 300, 50)
    for i, chunk in enumerate(chunks[:3]):
        print(f"   [Chunk {i+1}]: {repr(chunk)}")

    # Strategy 3: Large Chunks (Good for summaries)
    print("\n🟠 Strategy 3: Page Chunks (Size=1000, Overlap=200)")
    print("   -> Best for: Summarization and complex reasoning.")
    sample_text = documents.get("monthly_report.txt", "")
    chunks = recursive_character_text_splitter(sample_text, 1000, 200)
    for i, chunk in enumerate(chunks[:3]):
        print(f"   [Chunk {i+1}]: {repr(chunk)}")

    print("\n✅ RECOMMENDATION: 'Paragraph Chunks' (Size=300-500) seem versatile for our mixed content.")

if __name__ == "__main__":
    experiment()
