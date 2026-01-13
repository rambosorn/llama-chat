import os
import uuid
import pypdf
import pandas as pd
from chunking_utils import recursive_character_text_splitter, chunk_structured_data
from embedding_utils import get_embeddings
from db_utils import get_collection

DOCS_DIR = os.path.join(os.getcwd(), "documents")

def process_and_load():
    print("🚀 STARTING COMPLETION: DOCS -> CHUNKS -> EMBEDDINGS -> DB")
    
    # 1. Get Collection
    collection = get_collection()
    print(f"   Connected to collection: '{collection.name}'")
    
    # Reset DB for this major structure change (Optional but cleaner for dev)
    # For now, we'll just add new IDs. Ideally, we'd delete old ones or use a unique key.
    
    # 2. Iterate Files (Walking through directories)
    if not os.path.exists(DOCS_DIR):
        print("❌ Error: Documents directory not found.")
        return

    processed_count = 0
    total_chunks = 0
    
    print(f"   Scanning directory: {DOCS_DIR}")
    
    for root, dirs, files in os.walk(DOCS_DIR):
        for filename in files:
            if not filename.endswith((".txt", ".pdf", ".csv", ".xlsx", ".xls")):
                continue
                
            file_path = os.path.join(root, filename)
            
            # Extract Department from folder name
            # root will be .../documents/HR_Law -> folder is HR_Law
            # if root is .../documents, folder is 'General'
            folder_name = os.path.basename(root)
            department = folder_name if folder_name != "documents" and folder_name != "docs" else "General"
            
            print(f"\n📄 Processing: {filename} [Dept: {department}]")
            
            chunks = []
            try:
                # TEXT & PDF Handling
                if filename.endswith(".pdf"):
                    text = ""
                    reader = pypdf.PdfReader(file_path)
                    for page in reader.pages:
                        extracted = page.extract_text()
                        if extracted:
                            text += extracted + "\n"
                    print(f"   -> Extracted {len(text)} characters from PDF.")
                    chunks = recursive_character_text_splitter(text, chunk_size=500, chunk_overlap=50)

                elif filename.endswith(".txt"):
                    with open(file_path, "r", encoding="utf-8") as f:
                        text = f.read()
                    chunks = recursive_character_text_splitter(text, chunk_size=500, chunk_overlap=50)

                # SPREADSHEET Handling
                elif filename.endswith(".csv"):
                    df = pd.read_csv(file_path)
                    print(f"   -> Loaded CSV with {len(df)} rows.")
                    chunks = chunk_structured_data(df)
                    
                elif filename.endswith((".xlsx", ".xls")):
                    df = pd.read_excel(file_path)
                    print(f"   -> Loaded Excel with {len(df)} rows.")
                    chunks = chunk_structured_data(df)

            except Exception as e:
                print(f"   ❌ Error processing file: {e}")
                continue
                
            print(f"   -> Generated {len(chunks)} chunks.")
            
            if not chunks:
                continue
                
            # 4. Embeddings
            print("   -> Generating embeddings...")
            embeddings = get_embeddings(chunks)
            
            # 5. Store in DB
            ids = [str(uuid.uuid4()) for _ in chunks]
            
            # ADD METADATA: Department
            metadatas = [{
                "source": filename, 
                "chunk_id": i,
                "department": department  # <--- NEW TAG
            } for i in range(len(chunks))]
            
            collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=chunks,
                metadatas=metadatas
            )
            print(f"   -> ✅ Stored {len(chunks)} chunks in DB.")
            
            processed_count += 1
            total_chunks += len(chunks)

    print("\n------------------------------------------------")
    print(f"🎉 OPERATION COMPLETE")
    print(f"   Documents Processed: {processed_count}")
    print(f"   Total Memories Created: {total_chunks}")
    print(f"   Final DB Count: {collection.count()}")

if __name__ == "__main__":
    process_and_load()
