import openai
import requests
from utils import load_settings

def generate_completion(prompt, system_message, use_openai=True):
    settings = load_settings()
    if use_openai:
        openai.api_key = settings["openai_api_key"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
    else:
        url = "http://localhost:11434/api/generate"
        headers = {
            "Authorization": f"Bearer {settings['ollama_api_key']}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama3",
            "prompt": f"{system_message}\n\n{prompt}",
            "stream": False
        }
        response = requests.post(url, json=payload, headers=headers)
        response_json = response.json()
        return response_json.get("response", "")

def detailed_tasks_extraction(transcription, use_openai=True):
    system_message = (
        "You are a proficient AI with a specialty in project management and task breakdown. Based on the following meeting transcript, "
        "identify detailed tasks for the next sprint. Each task should include: Title, detailed description (enough to implement by someone "
        "who reads this), priority, and complexity level (1-10)."
    )
    return generate_completion(transcription, system_message, use_openai)

def meeting_minutes(transcription, use_openai=True):
    detailed_tasks = detailed_tasks_extraction(transcription, use_openai)
    return detailed_tasks
