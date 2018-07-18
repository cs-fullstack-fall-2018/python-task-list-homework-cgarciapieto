

# class task():
#     def __init__(self, task):
#         self.theTask = task
#



def getList():
    print("What would you like to do?")
    print("1.List all the tasks")
    print("2.Add a task")
    print("3.Delete a Task")
    print("4.press q to quit the program")

toDo = []
UserSelection = input("What would you like to do")

while (UserSelection != "q"):

    getList()
    if (UserSelection == "1"):
        for itemsinarray in toDo:
            print(itemsinarray)
        UserSelection = input("What would you like to do")

    if (UserSelection == "2"):
        addTask = input("Add a task")
        toDo.append(addTask)
        UserSelection = input("What would you like to do")

    if (UserSelection == "3"):
        removeTask = input("Delete a Task")
        toDo.remove(removeTask)
        UserSelection = input("What would you like to do")











print(toDo[0])






