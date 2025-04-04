import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

files = [
    ".github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",  
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py", 
    "src/utils/__init__.py", 
    "src/utils/utils.py",
    "src/tests/unit/__init__.py",
    "src/tests/integration/__init__.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "init_setup.sh",
    "setup.cfg",
    "setup.py",
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]


for filepath in files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creaing directory:{filedir} for file : {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass ## create a empty file
        logging.info(f"Created empty file: {filepath}")
