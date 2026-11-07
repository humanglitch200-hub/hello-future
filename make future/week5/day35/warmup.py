import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("Script folder:", BASE_DIR)

DATA_FILE = os.path.join(BASE_DIR, "test.txt")
print("Data file:", DATA_FILE)

# Create the file at that absolute path
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    f.write("hello from anywhere\n")

print("Exists now?", os.path.exists(DATA_FILE))