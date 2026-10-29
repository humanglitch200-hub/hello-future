entries = [("prem", 98), ("Elone", 95), ("jeff", 91)]
def add_entries(entries, name, score):
    entry = (name, score)
    entries.append(entry)

def top_scorer(entries):
    if not entries:
         print("Nothing found on (entires).")
         return None
    
    best_scorer = None
    for value in entries:
        if best_scorer is None or value > best_scorer:   #Teacher: by deepseek
            best_scorer = value
    return best_scorer    

    
def show_sorted(entries):
    if not entries:
        return None
    sorted_entries = sorted(entries, key=lambda x: x[1], reverse=True)
    print(sorted_entries)

def average_score(entries):
    if not entries:
        return None
    x, y = zip(*entries)
    average = sum(y)/ len(entries)
    print(average) 
#   never put it here! can cause error  pass (if no full body!)


if __name__ == "__main__":
     while True:
        print("1. Add name ")
        print("2. Top scorer ")
        print("3. Print sorted list ")
        print("4. See average")
        try:
           choice = int(input("Enter Your Choice: "))
        except ValueError:
           print("Select number from (1-4). ")
           continue

    
     
        if choice == 1:
            try:
                name = str(input("Enter name to add: "))
                if not name:
                    print("Enter name to add. PLEASE: ")
                    continue

                score = int(input(f"Enter score of {name}: "))
            except ValueError:
                print("Error: enter score!")
                continue
            add_entries(entries, name, score)

        elif choice == 2:
            top = top_scorer(entries)
            if top is not None:
                name, score = top
                print(f"Top scorer: {name} with {score} ")
            
        elif choice == 3:
            print("-- Printing sorted list by score 'highest' --")
            show_sorted(entries)

        elif choice == 4:
            average_score(entries)

        else:
            print("Enter number (1-4): ")
            continue
