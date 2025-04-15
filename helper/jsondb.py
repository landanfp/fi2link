import json
import os

DB_FILE = "data.json"

def save_file_info(file_id, file_name):
    data = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            data = json.load(f)
    data[file_id] = {"name": file_name}
    with open(DB_FILE, "w") as f:
        json.dump(data, f)
        
def get_file_info(file_id):
    if not os.path.exists(DB_FILE):
        return None
    with open(DB_FILE, "r") as f:
        data = json.load(f)
    return data.get(file_id)