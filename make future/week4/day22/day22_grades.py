grades = {}

def add_student(name):
    if name not in grades:
        grades.setdefault(name, [])
        

def add_grade(name, grade):
    if name not in grades:
        print("No name found ")
        return None 
    grades[name].append(grade)
    

def get_average(name):
    if name not in grades:
        print("No name found!")
        return None
    if not grades[name]:
        print("No  grades found!")
        return None
    return sum(grades[name]) / len(grades[name])
    
def show_all():
    print(grades.keys())
    print(grades.values())
    for name in grades:
        print(f"{name}: {get_average(name)}")
        

if __name__ == "__main__":
    while True:
        print("=== student menu ===")
        print("1. Add Student ")
        print("2. Add Grade ")
        print("3. Get Average ")
        print("4. Show All ")
        print("5. Quit ")
    
    
        try:
            asking = int(input("Enter your choice: "))
        except ValueError:
            print("Enter valid number.")
            continue

        if asking == 1:
            name = input("Enter student name: ")
            print(f"Name({name}) added")
            print()
            add_student(name)
            

        elif asking == 2:
            name = input("Enter student name: ")
            if not name:
                print("Please enter name.")
                continue
            try:
                grade = int(input("Enter grade: "))
            except ValueError:
                print("Invalid grade")
                continue
            add_grade(name, grade)
            print(f"Name({name}) & Grade({grade}) added")
            print()

        elif asking == 3:
            name = input("Enter student name: ")
            avg = get_average(name)
            if avg is not None:
                print(f"{name}: {avg}")
                print()

        elif asking == 4:
            print( )
            show_all()

        elif asking == 5:
            break
        else:
            print("Enter number between 1-5.")


        

