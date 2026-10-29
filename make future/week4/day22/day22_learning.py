student = {'jack': 4123, 'Ram':4124}
student['Elone'] = 4125   #now it is added in student dict.
print(student['jack'])    #it prints about jack: 4123
#printing  directly can cuase in error instead I can use get()
print(student.get('hari'))   #If there is nothig named hari it return none but doesn't crash
del student['Elone']         #deleting the Elone from dict
student['Prem'] = 4125       #adding details
print(student.get('Prem'))

print(list(student))   #it prints first each: ram , prem, etc.
print(sorted(student))

print('Ram' not in student)


print(dict([('sape', 41), ('guido', 43), ('jack', 42)]))
#dict([(..,..),(..,..)]) it make a dictonary but don't know what is name of that and how to acces.

{x: x**2 for x in (2, 4, 6)}
#I know what prints! {2: 4, 4: 16, 6: 36}

odds = {i: i**2 for i in (1, 3, 5)}
evens = {i: i**2 for i in (2, 4, 6)}
# {**odds **evens}   #'**' is used to combine two dictionaries

#that all is not supported on my python!
all_values = [odds, evens, {0:0}]
for i in all_values:
    print(i)  # {**i for i in all_values} prints all odd, evens 0:0 at once but it doesn't and **i is not supported is my python version

roll_students = dict(sape = 4123, guido=23, jack=345)
print(roll_students)