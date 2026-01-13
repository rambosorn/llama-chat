import chromadb
import sentence_transformers
import flask
import ollama
import openai
import google.generativeai
import os

print("--------------------------------------------------")
print("EXTENSIVE LIBRARY CHECK")
print("--------------------------------------------------")

try:
    print(f"ChromaDB Version: {chromadb.__version__}")
except Exception as e:
    print(f"ChromaDB Error: {e}")

try:
    print(f"Flask Version: {flask.__version__}")
except Exception as e:
    print(f"Flask Error: {e}")

try:
    print(f"Sentence Transformers loaded successfully.")
except Exception as e:
    print(f"Sentence Transformers Error: {e}")

print("--------------------------------------------------")
print("LLM PROVIDER CHECK")
print("--------------------------------------------------")

# Check Ollama
try:
    # Just checking import here. Actual connection requires running server.
    print("Ollama library imported. Attempting to list models (requires running server)...")
    try:
        models = ollama.list()
        print("Ollama Connection: SUCCESS")
        print(f"Available Models: {[m['name'] for m in models['models']]}")
    except Exception as connection_error:
        print(f"Ollama Connection Warning: Could not connect to Ollama server. Is it running? Error: {connection_error}")
except Exception as e:
    print(f"Ollama Import Error: {e}")

# Check OpenAI
print("OpenAI library imported (Ready for future use).")

# Check Gemini
print("Google Generative AI library imported (Ready for future use).")

print("--------------------------------------------------")
print("Environment Setup Verification Complete.")
