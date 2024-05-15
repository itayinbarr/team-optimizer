# LLM Optimization Project

This project aims to optimize development tasks using Large Language Models (LLMs). The repository includes modules for handling meeting minutes, assessing task complexity, and integrating with the Ollama API.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Update the `config/settings.yaml` file with your API keys and paths.

## Usage

```bash
python src/main.py
```

## Structure

```
team-optimizer/
├── README.md
├── requirements.txt
├── config/
│   ├── settings.yaml
├── data/
│   ├── meetings/
│   ├── sprints/
│   ├── tasks/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   ├── ollama_api.py
│   ├── meeting_minutes/
│   │   ├── __init__.py
│   │   ├── transcriber.py
│   │   ├── generator.py
│   │   ├── processor.py
│   │   ├── export.py
│   ├── task_management/
│   │   ├── __init__.py
│   │   ├── complexity_assessor.py
│   │   ├── task_handler.py
│   │   ├── review.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── pipeline_manager.py
│   │   ├── deployer.py
├── tests/
│   ├── __init__.py
│   ├── test_transcriber.py
│   ├── test_generator.py
│   ├── test_processor.py
│   ├── test_complexity_assessor.py
│   ├── test_task_handler.py
│   ├── test_review.py
│   ├── test_pipeline_manager.py
│   ├── test_deployer.py

```
