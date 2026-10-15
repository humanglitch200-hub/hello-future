print("-------should I go outside -------")
#asking what they has:
weather = input("Is it raining (y/n)? ").lower()
hot_or_not = input("Is it hot outside (y/n)? ").lower()
time = input("Do you have free time (y/n)? ").lower()

#Let's go for command:
if weather != 'y' and time != 'n':
    print("Go chill")

elif weather == 'y':
    umbrella = input("Do you have an umbrella(y/n)? ").lower()
    if umbrella !='n':
        print("Don't go outside!")

    else: print("You can go outside with umbrella")

elif hot_or_not =='y' and weather == 'n':
    print("Go outside, but stay hydrated")

elif time == 'y':
    print("stay home and code ")

else:
    print("Maybe stay inside today")
