while True:
    while True:
        try:
            count = int(input("How many marks do you want to Enter: "))
            if count <= 0:
               print("Please enter a postive number. ")
               continue
            break
        except ValueError:
             print("Invalid input! Enter a whole number")

#collect marks in a loop 
    marks = []
    for i in range(count):
        while True:
            try:
                 mark = float(input(f"Enter marks {i + 1}: "))
                 if 0 <= mark <= 100:
                     marks.append(mark)
                     break
                 else:
                     print("Marks must be between 0 and 100.")

            except ValueError:
                        print("Invalid input. Enter a number. ") 

    below = 0
#acalculation of average:
    average = sum(marks) / len(marks)
    for mark in marks:
        if mark < average:
             below += 1


#Assign gare with if/elif/else

    if average >= 90: grade = 'A'

    elif average >= 80: grade = 'B'
  
    elif average >= 70: grade = 'C'

    elif average >= 60: grade = 'D'

    else:
        grade = 'Study hard! '

#hhighest mark:
    high = max(marks)
    mini = min(marks)
    below_average = int(count / 2)

#print(summary)
    print("--- Results ---")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Your higest mark is: {high}")
    print(f"Your lowest mark is: {mini}")
    print(f"below average marks are: {below_average}")

    continuee = input("Do you want to continue (y/n): ").lower().strip()
    if continuee != 'y':
         break
    


