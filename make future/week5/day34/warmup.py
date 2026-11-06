import os
with open('sample.txt', 'w', encoding='utf-8') as f:
    pass

print(os.path.getsize("sample.txt"))
print(os.path.basename("sample.txt"))
print(os.path.dirname(os.getcwd() + "/sample.txt"))
print(os.path.splitext("sample.txt"))
os.rename("sample.txt", "sample_v2.txt")
print(os.path.basename("sample.txt"))
print(os.path.exists("sample.txt"))