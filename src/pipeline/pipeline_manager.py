from src.meeting_minutes.transcriber import transcribe_all_audios
from src.meeting_minutes.generator import generate_all_minutes
from src.meeting_minutes.processor import process_all_minutes
from src.task_management.complexity_assessor import assess_all_tasks
from src.task_management.task_handler import load_tasks, save_task
from src.task_management.review import review_tasks, save_reviewed_tasks

def manage_pipeline():
    # Transcribe meeting audios
    transcripts = transcribe_all_audios("data/meetings/")
    
    # Generate meeting minutes
    minutes = generate_all_minutes(transcripts)
    
    # Process meeting minutes to extract action items
    action_items = process_all_minutes(minutes)
    
    # Load tasks
    tasks = load_tasks("data/tasks/")
    
    # Assess task complexity
    task_descriptions = {task_id: task["description"] for task_id, task in tasks.items()}
    complexities = assess_all_tasks(task_descriptions)
    
    # Review tasks based on complexity
    reviewed_tasks = review_tasks(tasks, complexities)
    
    # Save reviewed tasks
    save_reviewed_tasks(reviewed_tasks, "data/reviewed_tasks/")
