import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks() -> list[str]:
    if not TASKS_FILE.exists():
        return []
    try:
        data = json.loads(TASKS_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) and all(isinstance(item, str) for item in data) else []
    except (OSError, json.JSONDecodeError):
        return []


def save_tasks(tasks: list[str]) -> None:
    TASKS_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def main() -> None:
    tasks = load_tasks()
    while True:
        print("\n1. View tasks\n2. Add task\n3. Delete task\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            if not tasks:
                print("No tasks yet.")
        elif choice == "2":
            task = input("Task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
        elif choice == "3":
            try:
                index = int(input("Task number: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    save_tasks(tasks)
                else:
                    print("Task number not found.")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            break
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
