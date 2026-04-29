# Home work 7_Ex1

# https://dummyjson.com/todos|

# ToDoList
# хранит задачи
# добавляет задачи         create
# печатает задачи          read
# Обновляет список задач   update
# удаляет задачи           delete


def create_task(max_id):
    auto_id = max_id + 1

    todo = input("Что надо сделать:")
    completed = input("Выполнено? (1 - True, пустой ввод - False):") == "1"   # Не bool - выдает всегда True, без int - при вводе не цифр крашнется  
    userId = int(input("userId:"))
    priority = int(input("Приоритет:"))

    new_task = {auto_id:{
                "Что надо сделать": todo,
                "Выполнено?": completed,
                "userId": userId,
                "Приоритет": priority,
            }
        }

    return new_task


def read_tasks(todos):
    for tk, tdi in todos.items():

        print("Task id:", tk)

        for k, v in tdi.items():
            print("    ", k, ":", v)
        print("__________________________________")


def read_task(tid, todos):
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)

    for k, v in res_task.items():
        print(" ", k, ":", v)

    print("__________________________________")


def delete_task(tid, todos):
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)
    todos.pop(tid)

    print("задача с id:", tid, "удалена.")
    print("__________________________________")

