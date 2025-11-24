import argparse
from datetime import datetime
import json
import os

TASKS_JSON: str = "tasks.json"


def create_task_data(
    task_id: int,
    description: str = None,
    status: str = "todo",
    updated_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
):
    return {
        "id": task_id,
        "description": description,
        "status": status,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": updated_at,
    }


def create_or_open_file(initial_data=None):
    file_name: str = TASKS_JSON

    if initial_data is None:
        initial_data = {"tasks": []}

    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, indent=4)
            return initial_data
    else:
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                print("File is empty, creating new file")
                with open(file_name, "w", encoding="utf-8") as file:
                    json.dump(initial_data, file, indent=4)
                    return initial_data


def add_task(args):
    if len(args.actions) < 2:
        print("Please provide a task description")
        return
    json_tasks = create_or_open_file()
    task_description = args.actions[1]
    print(len(json_tasks["tasks"]))
    task = create_task_data(len(json_tasks["tasks"]) + 1, task_description)
    json_tasks["tasks"].append(task)
    with open(TASKS_JSON, "w", encoding="utf-8") as f:
        json.dump(json_tasks, f, indent=4)


def list_tasks():
    json_tasks = create_or_open_file()
    for task in json_tasks["tasks"]:
        print(f"{task['id']}: {task['description']}")

def list_tasks_by_status(status):
    json_tasks = create_or_open_file()
    for task in json_tasks["tasks"]:
        if task["status"] == status:
            print(f"{task['id']}: {task['description']}")

def update_task(task_id, index, value):
    json_tasks = create_or_open_file()

    for task in json_tasks["tasks"]:
        if task["id"] == task_id:
            task[index] = value
            break

    with open(TASKS_JSON, "w", encoding="utf-8") as f:
        json.dump(json_tasks, f, indent=4)


def delete_task(task_id):
    json_tasks = create_or_open_file()

    for task in json_tasks["tasks"]:
        if task["id"] == task_id:
            json_tasks["tasks"].remove(task)
            break


def task_executor(args):
    if args.actions[0] == "add":
        add_task(args)
    elif args.actions[0] == "update":
        update_task(int(args.actions[1]), "description", args.actions[2])
    elif args.actions[0] == "mark-in-progress":
        update_task(int(args.actions[1]), "status", "in-progress")
    elif args.actions[0] == "mark-done":
        update_task(int(args.actions[1]), "status", "done")
    elif args.actions[0] == "delete":
        delete_task(int(args.actions[1]))
    elif args.actions[0] == "list":
        print("List of tasks:")
        if len(args.actions) > 1:
            list_tasks_by_status(args.actions[1])
        elif len(args.actions) == 1:
            list_tasks()
    else:
        print()


def main():
    parser = argparse.ArgumentParser(description="CLI for managing tasks")

    parser.add_argument(
        "actions", nargs="*", help="What do you want to do? (add, update, delete, list)"
    )

    args = parser.parse_args()

    print(args)

    task_executor(args)


if __name__ == "__main__":
    main()
