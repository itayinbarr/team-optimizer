import json
import os

def load_tasks(directory):
    tasks = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as file:
                tasks[filename] = json.load(file)
    return tasks

def save_task(task, filename, directory):
    with open(os.path.join(directory, filename), 'w') as file:
        json.dump(task, file, indent=4)
