numbers =[]

def add(numbers):
    if not numbers:
        return None
    print("adding successed.")
    return numbers      

def show_stats():
    if not numbers:
        return None
    print("Showing stats..")
    print(numbers)

def show_sum():
    if not numbers:
        return None
    total = 0
    for n in numbers:
        total += n
    print('Sum of numbers:',total)
    return total 

def show_averge():
    if not numbers:
        return None
    total = 0
    for n in numbers:
        total += n
    print('Average of numbers:', total / len(numbers))

while True:      
    if __name__ == "__main__":
        print()
        print('1. Add numbers')
        print('2. Show all stats')
        print('3. Show only sum')
        print('4. Show only average')
        print('5. Quit')

        try:
            print()
            choice = int(input('Enter your choice:'))
        except ValueError:
            print("Please enter your choice!")
            continue

        if choice == 1:
            try:
                num = int(input("Enter number to add: "))
                mew = numbers.append(num)
            except ValueError:
                print("Please Enter number!")
            add(numbers)
            continue
        elif choice == 2:
            show_stats()
            continue
        elif choice == 3:
            show_sum()
            continue
        elif choice == 4:
            show_averge()
            continue
        elif choice == 5:
            break
        else:
            print('Enter your choice (1-4): ')
            continue
