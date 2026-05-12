task = str(input("Enter a task: "))
tasks = []
while task != "done":
    tasks.append(task)
    task = str(input("Enter a task: "))
    print("Your to-do list:")
    for i in range(len(tasks)):
        print(f"{i + 1}  - {tasks[i]}")
        