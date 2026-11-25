import json
from datetime import datetime

collection = {
    "version": 1,
    "contacts":[
        {"name":"jeff", "phone":"123"},
        {"name":"elone", "phone":"456"},
    ],
}

data = {"Saved": datetime.now()}
json.dump(data, open("practice2.json", "w"), default=str)
