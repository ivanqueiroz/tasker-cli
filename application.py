import argparse
from datetime import datetime
import json
import os


def create_task_data(task_id, description=None, status='todo',
                         updated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    return {
        "id": task_id,
        "description": description,
        "status": status,
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": updated_at
    }


def create_or_open_file(initial_data=None):
    file_name = 'tasks.json'

    if initial_data is None:
        initial_data = {
            "tasks": []
        }

    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, indent=4)
            return initial_data
    else:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)


def add_task(task_description):
    tasks = create_or_open_file()
    print(len(tasks['tasks']))
    task = create_task_data(len(tasks['tasks']) + 1, task_description)
    tasks['tasks'].append(task)
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def task_executor(args):
    if args.action == 'add':
        add_task(args.description)
        print(f"Adding task: {args.description}")
    elif args.action == 'update':
        print(f"Updating task: {args.description}")
    elif args.action == 'delete':
        print(f"Deleting task: {args.description}")
    elif args.action == 'list':
        print("Listing tasks")
    else:
        print()


def main():
    parser = argparse.ArgumentParser(
        description='CLI for managing tasks'
    )

    parser.add_argument('action', help='Name of action (add, update, delete and list')
    parser.add_argument('description', help='Task description')

    args = parser.parse_args()

    task_executor(args)


if __name__ == '__main__':
    main()
