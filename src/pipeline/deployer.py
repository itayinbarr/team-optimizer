import json
import os

def deploy_tasks(tasks_directory, deployment_directory):
    for filename in os.listdir(tasks_directory):
        if filename.startswith("reviewed_") and filename.endswith(".json"):
            with open(os.path.join(tasks_directory, filename), 'r') as file:
                task = json.load(file)
                if isinstance(task, dict):  # Only deploy tasks that are not marked for human intervention
                    with open(os.path.join(deployment_directory, filename), 'w') as deploy_file:
                        json.dump(task, deploy_file, indent=4)
