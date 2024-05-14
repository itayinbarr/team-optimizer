from ollama_api import generate_completion

def assess_task_complexity(task_description):
    prompt = f"Assess the complexity of the following task:\n{task_description}"
    response = generate_completion(prompt)
    return response

def assess_all_tasks(task_descriptions):
    complexities = {}
    for task_id, description in task_descriptions.items():
        complexities[task_id] = assess_task_complexity(description)
    return complexities
