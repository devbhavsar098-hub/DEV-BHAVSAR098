vimport json

file = "tasks.json"

try:
    with open(file, "r") as f:
        tasks = json.load(f)
except:
    tasks = []

while True:
    print("\n1.Add  2.View  3.Delete  4.Done  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})

    elif ch == "2":
        for i, t in enumerate(tasks, 1):
            status = "✓" if t["done"] else "✗"
            print(i, t["task"], status)

    elif ch == "3":
        n = int(input("Task number: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n - 1)
        else:
            print("Task not found")

    elif ch == "4":
        n = int(input("Task number: "))
        if 1 <= n <= len(tasks):
            tasks[n - 1]["done"] = True
        else:
            print("Task not found")

    elif ch == "5":
        with open(file, "w") as f:
            json.dump(tasks, f, indent=4)
        print("Saved!")
        break

    else:
        print("Invalid choice")
