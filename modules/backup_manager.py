import os
import shutil
import logging
from datetime import datetime
from modules.helper import create_folder

def backup_files(source_path):

    try:

        backup_folder = "backup"

        create_folder(backup_folder)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_path = os.path.join(
            backup_folder,
            f"backup_{timestamp}"
        )

        shutil.copytree(source_path, backup_path)

        logging.info(f"Backup created at {backup_path}")

        print(f"Backup Created: {backup_path}")

    except Exception as e:
        logging.error(f"Error creating backup: {e}")
        print("Error:", e)