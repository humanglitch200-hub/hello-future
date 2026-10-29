friend1 = {
    "name":"elone",
    "age" : 21
}

friend2 = {
    "name": "jeff",
    "age" : 20
}

friend3 = {
      "name" : "michael",
      "age"  : 19
}

friend4 = {
      "name" : "larry",
       "age"  : 23
    
}

friends = {
    "friend1": friend1,
    "friend2": friend2,
    "friend3": friend3,
    "friend4": friend4,

}

#printing "name is X years old" using. items()
for friend, obj in friends.items():         
       print(f"{obj["name"]} is {obj["age"]} years old.")

#asking for name and printing it's age if in friends:
name ='jef'
found = False
for data in friends.values():
       if data["name"] == name:
              print(f"Age of {data['name']} is {data['age']}")
              found = True
              break
       if name not in data['name']:
              continue
       else:
              print("Name not found!")
              
#seeing if there is someone of that age
age =(19)
found = False
for data in friends.values():
    if str(data['age']) == age:
        found = True
        break

if found:
      print("Yes, someone is:", age)
else:
      print("No one is:", age)


#sorted - same dict, all pairs, sorted albhabetically by name.
print(sorted(friends))
for friend, obj in sorted(friends.items()):
      print(friend, obj)

for obj in sorted(friends.values(), key=str):
      print(obj["name"])

for x in sorted(friends.values(), key=lambda x: x["age"]):
      print(x["age"])

print()
#printing each friend's name and age:
for friend, data in friends.items():
      print(f"{data['name']} : {data['age']}")

#SUM/AVG/MAX printing all:
subjects = dict([("python", 99), ("c", 89), ("java", 83)])
total = 0
max_score = 0

for score in subjects.values():
      total += score
      if score > max_score:
            max_score = score

average = total/len(subjects)
print()
print("total:", total)
print("average:", average)
print("max:", max_score)
          





       


    