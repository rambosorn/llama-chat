from db_utils import get_collection, DB_PATH
import os

print(f"Initializing Vector Database at: {DB_PATH}")

try:
    # Attempt to create/get the collection
    collection = get_collection()
    
    print(f"✅ SUCCESS: Collection '{collection.name}' is ready.")
    print(f"📊 Current Document Count: {collection.count()}")
    print("The 'Brain' is ready to store memories.")

except Exception as e:
    print(f"❌ FAILURE: Could not initialize database.")
    print(f"Error details: {e}")
