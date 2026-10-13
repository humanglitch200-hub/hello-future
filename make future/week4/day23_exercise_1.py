friend1 = {
    "name":"elone",
    "age" : 21
}

friend2 = {
    "name": "jeff",
    "age" : 20
}

friend3 = {
    "name" : "larry",
    "age"  : 23
}

friend4 = {
    "name" : "michael",
    "age"  : 19
}

friends = {
    "friend1": friend1,
    "friend2": friend2,
    "friend3": friend3,
    "friend4": friend4,

}
for friend, obj in friends.items():         
       print(f"{obj["name"]} is {obj["age"]} years old.")

name ='jeff'   #input("Enter name for age: ")
for friend, obj in friends.get(name, []): 
    if name in obj["name"]:
       print(f"age of {obj["name"]} is {obj["age"]}")

    if name not in obj["name"]:
       print("No such name found! ")

#sking user for a name and printing age if found!
name = 'elone'  #input("Enter name for age: ")
if name in obj["name"]:
    print(obj["age"])
if name not in obj["name"]:
    print("name not found")

#aking for a value(an age)