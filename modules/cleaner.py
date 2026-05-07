import os
import logging

def remove_empty_folders(path):

    try:

        for foldername, subfolders, filenames in os.walk(
            path,
            topdown=False
        ):

            if not subfolders and not filenames:

                os.rmdir(foldername)

                logging.info(f"Removed empty folder: {foldername}")

                print(f"Removed Empty Folder: {foldername}")

    except Exception as e:
        logging.error(f"Error removing empty folders: {e}")
        print("Error:", e)

        