import requests
import json
import sys

url = "http://127.0.0.1:8000/query"
payload = {
    "query": "What is the fuel used in PSLV?",
    "role": "Public"
}
headers = {'Content-Type': 'application/json'}

print(f"Sending query to {url}...")
try:
    with requests.post(url, headers=headers, data=json.dumps(payload), stream=True) as r:
        r.raise_for_status()
        print("Response stream started:")
        for chunk in r.iter_content(chunk_size=None):
            if chunk:
                sys.stdout.write(chunk.decode('utf-8'))
                sys.stdout.flush()
    print("\n\nStream finished.")
except Exception as e:
    print(f"\nError: {e}")
