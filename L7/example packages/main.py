from todolist_pkg import useful_funcs as u
from todolist_pkg import stats as s
from todolist_pkg import backup as b

##import useful_funcs as u
##import statka as s
##import backup as b

todos = {
1:{
"To do": "Do something nice for someone you care about",
"Done?": False,
"userId": 152,
'Priority': 1
},
2: {
"To do": "Memorize a poem",
"Done?": True,
"userId": 13,
'Priority': 2
},
3: {
"To do": "Watch a classic movie",
"Done?": True,
"userId": 68,
'Priority': 3
},
}

def main():
print("""
1 - Create task
2 - Read task by id
3 - Display all tasks
4 - Delete task by id
5 - stats
6 - backup
0 - Exit""")
operation = int(input("-->"))

while operation != 0:
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
elif operation == 5:
s.statistica()
elif operation == 6:
b.backup()
else:
print("I didn't understand, try again.")

print("""
1 - Create task
2 - Read task by ID
3 - Print all tasks
4 - Delete task by ID
5 - statistica
6 - backup
0 - Exit""")
operation = int(input("-->"))

print("bye bye")

main()