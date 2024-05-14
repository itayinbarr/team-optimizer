import requests
import yaml
from src.utils import load_settings

def generate_completion(prompt):
    settings = load_settings()
    url = "http://localhost:11434/api/generate"
    headers = {
        "Authorization": f"Bearer {settings['ollama_api_key']}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    return response_json.get("response", "")
