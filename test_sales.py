import requests
import json

questions = [
    "Show me the sales data for the last month.",
    "What are the current product prices?",
    "Hello"
]

for q in questions:
    print(f"\nAsking: {q}")
    try:
        response = requests.post("http://127.0.0.1:5000/ask", json={"question": q})
        print(f"Status: {response.status_code}")
        if response.status_code != 200:
            print(f"Error: {response.text}")
        else:
            print("Success")
    except Exception as e:
        print(f"Request failed: {e}")
