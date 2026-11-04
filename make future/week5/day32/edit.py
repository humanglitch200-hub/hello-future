import json

c = json.load(open("contacts.json"))
for i, c in enumerate(c, 1):
    print(i, c)

try:
    n = int(input("Which: "))
except ValueError:
    print("invalid index.")
    raise SystemExit
try:
    c[n-1]["phone"] = int(input("add phone: "))
except ValueError:
    print("Enter number to add!!!!!!")
    raise SystemExit

json.dump(c, open("contacts.json","w"), indent =2)
print(json.load(open("contacts.json")))

    #all the thins of json #copied by AI.
    #Deep seek providing too hard excercise!
    