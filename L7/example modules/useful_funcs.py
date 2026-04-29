# Home work 7_Ex1

# https://dummyjson.com/todos|

# ToDoList
# stores tasks
# adds tasks create
# prints tasks read
# updates the task list update
# deletes tasks delete

def create_task(max_id):
auto_id = max_id + 1

todo = input("What needs to be done:")
completed = input("Completed? (1 - True, empty input - False):") == "1" # Not a bool - always returns True; without an int - crashes when entering non-numeric values
userId = int(input("userId:"))
priority = int(input("Priority:"))

new_task = {auto_id:{
"What needs to be done": todo,
"Completed?": completed,
"userId": userId,
"Priority": priority,
}
}

return new_task

def read_tasks(todos):
for tk, tdi in todos.items(): 

print("Task id:", tk) 

for k, v in tdi.items(): 
print(" ", k, ":", v) 
print("_________________________________")


def read_task(tid, todos): 
res_task = todos.get(tid, -1) 

if res_task == -1: 
print("task not found with id:", tid) 
return 

print("Task id:", tid) 

for k, v in res_task.items(): 
print(" ", k, ":", v) 

print("_________________________________")


def delete_task(tid, todos): 
res_task = todos.get(tid, -1) 

if res_task == -1: 
print("task not found with id:", tid) 
return 

print("Task id:", tid) 
todos.pop(tid) 

print("task with id:", tid, "deleted.") 
print("_________________________________")