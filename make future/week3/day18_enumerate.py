#Finding winner ny using enumerates():
runner = ["manoj", "rajes", "arjan"]
for winner in enumerate(runner):
    print(winner)

#it prints more better than single comand 'winner'!:
for position, winner in enumerate(runner):
    print(position, winner)                 

#To start with 1 you can do:
for position, name in enumerate(runner, start=1):     
    print(position, name)

#processing items by using enumerate:
tasks_by_priority = ["Learn, learn", "make power, knowledge", "Go on marsh"]
for index, task in enumerate(tasks_by_priority):
    if index == 0:
        print(f"* {task.upper()}!")
    else:
        print(f"* {task}")

#grabing every second item:
secret_message = "3LAigf7eq 5fhionpdDs2 Ra6 nwUalyo.9"
message = ""
for index, char in enumerate(secret_message):
    if index % 2:
        message += char

print(message)

#printing by seeing line, if it has line 'Contains a tab character'
lines = [
    "This is a\tline"
    "This line is fine",
    "Another line with whitespace "
]
for lineno, line in enumerate(lines, start = 1):      #lineao means position.
    if "\t" in line:
        print(f"Line {lineno}: Contains a tab character.")
    if line.rstrip() != line:
        print(f"Line {lineno}: Contains trailing whitespaces.")

