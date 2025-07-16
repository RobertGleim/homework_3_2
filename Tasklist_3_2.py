
class Task:
    def __init__(self, name):
        self.name = name
        self.completed = "Incomplete"

    def mark_completed(self):
        self.completed = "Completed"
        return f" ✅  {self.completed} {self.name} is now marked as completed."
    def __str__(self):
        return f"{self.name} - {self.completed}"

class Node:
    def __init__(self, task_obj):
        self.task = task_obj
        self.next = None


class Tasklist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, new_task_obj):
        new_node = Node(new_task_obj)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def task_list_items(self, status_filter=None):
        output = "========= Things To Do =========\n"
        if self.is_empty():
            output += "No tasks in the list.\n"
            return output

        current = self.head
        position = 1
        while current:
            if status_filter == "Incomplete" and current.task.completed != "Incomplete":
                current = current.next
                continue
            if status_filter == "Completed" and current.task.completed != "Completed":
                current = current.next
                continue

            output += f"{position}. {current.task}\n"
            current = current.next
            position += 1
        return output    

    def insert_at_position(self, new_task, position):
        new_node = Node(new_task)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return f"Task '{new_task.name}' inserted at position {position}."
            

        current = self.head
        counter = 0
        while counter < position - 1 and current:
            current = current.next
            counter += 1
        if current:
            new_node.next = current.next
            current.next = new_node
        return f"Task '{new_task.name}' inserted at position {position}."

    def get_at_position(self, position):
        current = self.head
        count = 0
        while current:
            if count == position:
                return current.task
            count += 1
            current = current.next
        return None

    def delete_at_position(self, position):
        if self.is_empty():
            print("Cannot delete from an empty list.")
            return None

        if position == 0:
            removed = self.head
            self.head = self.head.next
            return f"Task '{removed.task.name}' deleted from position {position}."
            
        current = self.head
        counter = 0
        while counter < position - 1 and current and current.next:
            current = current.next
            counter += 1

        if current and current.next:
            removing = current.next
            current.next = current.next.next
            return f"Task '{removing.task.name}' deleted from position {position}."
             
        else:
            print("Invalid position.")
            return None

    def traverse(self, filter_incomplete=False):
        current = self.head
        while current:
            if filter_incomplete and current.task.completed == "Incomplete ":
                print(f"{current.task.name} - {current.task.completed}")
            elif not filter_incomplete:
                print(f"{current.task.name} - {current.task.completed}")
            current = current.next

    def mark_completed(self, position):
        current = self.head
        count = 0
        while current:
            if count == position:
                return current.task.mark_completed()
            count += 1
            current = current.next
        return "Task not found at the given position."

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def completion_status(self):
        
        current = self.head
        completed_count = 0
        total_count = 0
        while current:
            total_count += 1
            if current.task.completed == "Completed ✅":
                completed_count += 1
            current = current.next
        if completed_count == 0:
            return "No tasks completed yet."
        if total_count == 0:
            return "No tasks in the list."
        return f"Completed: {completed_count}, Total: {total_count} "
    
    def update_task_name(self, position, new_name):
        task_to_update = self.get_at_position(position)
        if task_to_update:
            old_name = task_to_update.name
            task_to_update.name = new_name
            print(f"Task renamed from '{old_name}' to '{new_name}'.")
        else:
            print("Task not found.")
  
    

    


task = Tasklist()
print("========= Task List ========= ")

task.append(Task("wake up early"))
task.append(Task("Eat a Good Breakfast"))
task.append(Task("Do some Codewars"))
task.append(Task("Eat Lunch"))
task.append(Task("write homeworkcode"))
task.append(Task("Complete Python assignment"))
task.append(Task("Attend Full Stack Class"))



print(task.task_list_items())

print(task.mark_completed(2))  

print(task.completion_status())

print(task.task_list_items("Completed"))
 
print(task.task_list_items("Incomplete")) 
