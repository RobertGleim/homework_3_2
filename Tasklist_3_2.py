class Node:
    def __init__(self, task):
        self.task = task
        self.next = None



class Task:
    def __init__ (self, name):
        self.name = name
        self.completed = "Incomplete"


        

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None
        
        
class TaskList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None    
                
    def append(self, task):
        new_node = Node(task)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node    
            
    def tasklistitems(self):
        print("========= Things To Do =========")
        if self.is_empty():
            print("No tasks in the list.")
            return
        current = self.head
        position = 1
        while current:
            print(f"{position}. {current.task.name} - {current.task.completed}")
            current = current.next
            position += 1
    
    def Insert_at_position(self, task, position):
        new_node = Node(task)
        if position == 0:
            new_node.next = self.head
            return
        
        current = self.head
        counter = 0 
        while counter < position - 1  and current:
            current = current.next
            counter += 1
        if current:
            new_node.next = current.next
            current.next = new_node        
               
    def get_at_potion(self, position):
        current = self.head
        count = 0
        while current <position:
            count += 1
            current = current.next
        return current.task
    
    def delete_at_position(self, position):
        current = self.head
        counter = 0 
        while counter < position - 1:
            current = current.next
            counter += 1
            removing = current.next
            current.next = current.next.next
            return removing
    
    # Instantiate TaskList and print welcome message outside the class definition
tasks = TaskList()
print("========= Task List ========= ")
    
tasks.append(Task("wake up early"))
tasks.append(Task("Eat a Good Breakfest"))
tasks.append(Task("Do some Codewars"))
tasks.append(Task("Eat Lunch"))    
tasks.append(Task("write homeworkcode"))
tasks.append(Task("Complete Python assignment"))
tasks.append(Task("Attend Full Stack Class"))


