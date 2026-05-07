import os
import shutil
import logging
from modules.helper import create_folder

def organize_files(path):

    try:

        file_types = {
            "Images": [".jpg", ".png", ".jpeg"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Videos": [".mp4", ".mkv"],
            "Music": [".mp3"],
            "Python_Files": [".py"]
        }

        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):

                extension = os.path.splitext(file)[1].lower()

                moved = False

                for folder, extensions in file_types.items():

                    if extension in extensions:

                        destination = os.path.join(path, folder)

                        create_folder(destination)

                        shutil.move(
                            file_path,
                            os.path.join(destination, file)
                        )

                        logging.info(f"Moved {file} to {folder}")

                        print(f"Moved: {file} -> {folder}")

                        moved = True
                        break

                if not moved:

                    others = os.path.join(path, "Others")

                    create_folder(others)

                    shutil.move(
                        file_path,
                        os.path.join(others, file)
                    )

    except Exception as e:
        logging.error(f"Error organizing files: {e}")
        print("Error:", e)