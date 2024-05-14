import json
import os


def review_tasks(tasks, complexities):
    reviewed_tasks = {}
    for task_id, task in tasks.items():
        complexity = complexities.get(task_id, "Unknown")
        if complexity != "Complex":
            reviewed_tasks[task_id] = task
        else:
            reviewed_tasks[task_id] = "Needs human intervention"
    return reviewed_tasks

def save_reviewed_tasks(reviewed_tasks, directory):
    for task_id, task in reviewed_tasks.items():
        with open(os.path.join(directory, f"reviewed_{task_id}.json"), 'w') as file:
            json.dump(task, file, indent=4)
