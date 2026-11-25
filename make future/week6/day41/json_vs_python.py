import json

def bad(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{filename} not found, starting empty.")
        return []

    except json.JSONDecodeError as e:
        print(f"Bad json in {filename}: {e}")
        return []

mew = bad('practice2.json')
print(mew)
