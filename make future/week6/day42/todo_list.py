
class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.todos = []
        self.load()


    def load(self):
        if not self.filename:
            self.todos = []
            return False

    def add(self, task):
        self.todos.append({"task": task, "done": False})
        return True

    def complete(self, index):
        self.todos[index]["done"] = True
        return True

    def show(self):
        for task in self.todos:
            if task["done"] is True:
                print(f"[x] {task["task"]}")
            else:
                print(f"[ ] {task["task"]}")
            

        

            



    
