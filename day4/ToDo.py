# Python to-do app
from datetime import datetime

class Task:
    def createTask(self):
        task_text = input("Enter task: ")
        try:
            deadline = datetime.strptime(input("Enter deadline (d/m/yyyy %H:%M:%S): "), '%d/%m/%Y %H:%M:%S')
        except:
            deadline = datetime.now()
        print(task_text)
        print(deadline)
    

# creating a Task
task1 = Task()
task1.createTask()
