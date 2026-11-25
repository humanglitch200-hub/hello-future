import os, json
BASE_FILE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_FILE, "practice.json")

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

if isinstance(data, list):
    print("Legacy format: bare list")

elif isinstance(data, dict):
      print(f"New format: wrapped dict, version {data['version']}")

else:
     print("unknown format")
  
