import useful_funcs as u

todos = {
1:{
"Todo": "Do something nice for someone you care about",
"Done?": False,
"userId": 152,
'Priority': 1
},
2: {
"Todo": "Memorize a poem",
"Done?": True,
"userId": 13,
'Priority': 2
},
3: {
"Todo": "Watch a classic movie",
"Done?": True,
"userId": 68,
'Priority': 3
},
}

def main():
print("""
1 - Create a task
2 - Read a task by ID
3 - Print all tasks
4 - Delete a task by ID
5 - Exit""")
operation = int(input("-->"))

while operation != 5:
if operation == 1:
task = u.create_task(max(todos.keys()))
todos.update(task)
elif operation == 2:
tid = int(input("Enter task id:"))
u.read_task(tid, todos)
elif operation == 3:
u.read_tasks(todos)
elif operation == 4:
tid = int(input("Enter task id:"))
u.delete_task(tid, todos)
else:
print("I didn't understand, try again.")

print("""
1 - Create task
2 - Read task by id
3 - Print all tasks
4 - Delete task by id
5 - Exit""")
operation = int(input("-->"))

print("bye bye")

main()