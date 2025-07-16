
class Task:
    def __init__ (self, name):
        self.name = name
        self.completed = "Incomplete"
    def mark_completed(self):
        self.completed = "Completed"
        return f"{self.completed} {self.name} is now marked as completed."    


        

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
        while current and count <position:
            if count == position:
                return current.task 
            count += 1
            current = current.next
        return None
    
    def delete_at_position(self, position):
        current = self.head
        counter = 0 
        while counter < position - 1:
            current = current.next
            counter += 1
            removing = current.next
            current.next = current.next.next
            return removing
    
    
task = TaskList()
print("========= Task List ========= ")
    
task.append(Task("wake up early"))
task.append(Task("Eat a Good Breakfest"))
task.append(Task("Do some Codewars"))
task.append(Task("Eat Lunch"))    
task.append(Task("write homeworkcode"))
task.append(Task("Complete Python assignment"))
task.append(Task("Attend Full Stack Class"))

print(task.tasklistitems())
