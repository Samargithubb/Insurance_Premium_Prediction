import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Insurance"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",

    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/batch_prediction.py"
    f"{project_name}/utils.py",
    "template/index.html",
    "template/result.html",
    "application.py",
    "requirements.txt",
    ".gitignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")


    else:
        logging.info(f"{filename} is already created")







