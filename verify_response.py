import requests
import json

try:
    response = requests.post("http://127.0.0.1:5000/ask", json={"question": "Show me the sales data for the last month."})
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Answer: {data.get('answer')}")
except Exception as e:
    print(f"Error: {e}")
