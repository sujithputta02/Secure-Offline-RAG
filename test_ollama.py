import requests
import json
import time

url = "http://127.0.0.1:8000/query"
payload = {
    "query": "What is the fuel used in PSLV?",
    "role": "Public"
}
headers = {'Content-Type': 'application/json'}

print(f"Sending query to {url}...")
try:
    start_time = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
    end_time = time.time()
    duration = end_time - start_time
    
    if response.status_code == 200:
        data = response.json()
        print(f"Response received in {duration:.2f} seconds")
        print("Response:")
        print(json.dumps(data, indent=2))
        
        resp_text = data.get("response", "")
        with open("test_result_clean.txt", "w", encoding="utf-8") as f:
            f.write(f"Duration: {duration:.2f}s\n")
            f.write(f"DEBUG: Full Response Text: {resp_text}\n")
            if "(Fallback)" in resp_text:
                f.write("\nRESULT: Fallback mechanism was used.\n")
            else:
                f.write("\nRESULT: Likely used Ollama (No fallback marker found).\n")
        print("Written to test_result_clean.txt")
            
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Request failed: {e}")
