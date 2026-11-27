import json
def save_bad(path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"x": 1}, f)
    except FileNotFoundError as e:
        print(f"faild: {e}")

save_bad("/nope/this/folder/does/not/exist.json")
#BEFORE:  FileNotFoundError: [Errno 2] No such file or directory: '/nope/this/folder/does/not/exist.json'
#AFTER: faild: [Errno 2] No such file or directory: '/nope/this/folder/does/not/exist.json'

