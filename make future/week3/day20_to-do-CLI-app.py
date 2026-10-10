tasks = []

def add_task(tasks):
    new_tsk = input("Enter task name: ")
    tasks.append({"task": new_tsk,
                  "done": False
                })
    print("Task added, successfully")

def view(tasks):
    if not tasks:
        print("No task yet!")
        return
    for p, t in enumerate(tasks, start =1):
        print(f"{p}. [{'x' if t ['done'] else ' ' }] {t['task']}")
    
def remove_task(tasks):
    view(tasks)
    if not tasks:
        return
    try:
        index = int(input("""Which task you want to delete.
Enter index number: """))
        tasks.pop(index - 1)
        print("Task removed.")
    except ValueError:
        print("Please Enter a number")
    except IndexError:
        print("That task number doesn't exist")

def mark_done(tasks):
    view(tasks)
    if not tasks:
        return
    try:
        index = int(input("Which task is done? : ")) -1
        tasks[index]["done"] = True
        print("Task marked done.")
    except ValueError:
        print("Please Enter task index number")
    except IndexError:
        print("This task number doesn't exist")

def search_task(tasks):
    view(tasks)
    if not tasks:
        return   
    search = input("Search The Task By Name: ")
    found = False
    for task in tasks:
        if search.lower() in task["task"].lower():
            print(f"- {task['task']}")
            found = True
    if not found:
        print("No matching tasks.")


def show_stats(tasks):
    if not tasks:
        print("No tasks Yet.")
        return
    done = 0
    pending = 0
    for t in tasks:
        if t['done']:
            done += 1
        else:
            pending += 1
    print("===STATS===")
    print(f"- Done:    {done} ")
    print(f"- Pending: {pending}")
    print(f"- Total:   {len(tasks)}")

if __name__ == "__main__":
    while True:
        print()
        print("=== To-DO LIST ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Mark as done")
        print("5. Search tasks")
        print("6. Show stats")
        print("7. Quit")
        print()
        try:
           choice = int(input("Enter your choice: "))
        except ValueError:
            print("Plesae Enter a number")
            continue
 
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
           view(tasks)
        elif choice == 3:
            remove_task(tasks)
        elif choice == 4:
            mark_done(tasks)
        elif choice == 5:
            search_task(tasks)
        elif choice == 6:
            show_stats(tasks)
        elif choice == 7:
           print("see you.")
           break
        else:
            print("Enter a number (1-7)")



    









    

    
    

    
    