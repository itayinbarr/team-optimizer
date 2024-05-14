import os
from meeting_minutes.transcriber import transcribe_all_audios
from meeting_minutes.generator import meeting_minutes
from meeting_minutes.export import save_all_tasks_as_docx, save_simple_tasks_as_docx
from utils import load_settings

def main():
    settings = load_settings()
    transcription_method = settings.get("transcription_method", "local")
    audio_directory = settings.get("meeting_audio_path", "data/meetings/")
    sprint_directory = settings.get("sprint_data_path", "data/sprints/")
    task_directory = settings.get("task_data_path", "data/tasks/")
    
    transcripts = transcribe_all_audios(audio_directory, method=transcription_method)
    
    for filename, transcription in transcripts.items():
        summary = filename.split('.')[0]  # Use the filename as the summary
        minutes = meeting_minutes(transcription, use_openai=False)
        
        save_all_tasks_as_docx(minutes, summary, sprint_directory)
        save_simple_tasks_as_docx(minutes, summary, task_directory)

if __name__ == "__main__":
    main()
