# Project Structure
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Lip2SpeechAI'

list_of_files = [
    ".github/workflows/.gitkeep",
    # Data
    "data/raw/", # Raw data (videos, audio, etc.)
    "data/preprocessed/", # Preprocessed data
    "data/logs/", # Logs for data preprocessing
    "data/README.md",
    # ML Model
    "ml_model/lip_reading/preprocess.py", # Data preprocessing script
    "ml_model/lip_reading/model.py", # Model definition
    "ml_model/lip_reading/train.py", # Model training
    "ml_model/lip_reading/inference.py", # Model inference
    "ml_model/speech_synthesis/preprocess.py", 
    "ml_model/speech_synthesis/model.py", 
    "ml_model/speech_synthesis/train.py", 
    "ml_model/speech_synthesis/inference.py", 
    # Backend
    "backend/routes/processRoutes.js", # Video processing routes
    "backend/services/lipReadingService.js",
    "backend/services/ttsService.js", # Service for running ML inference
    "backend/app.js",
    "backend/package.json",
    # Frontend
    "frontend/public/", # Static files (CSS, JS)
    "frontend/src/components/VideoToSpeech.js", # Component for video upload and interaction
    "frontend/src/App.js", # Main frontend app entry point
    "frontend/package.json", # Frontend dependencies
    # Deployment
    "deployment/__init__.py",
    # Notebook
    "notebook/ml_model.ipynb",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with  open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists.")