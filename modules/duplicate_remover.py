import os
import logging
from modules.helper import get_file_hash

def remove_duplicates(path):

    try:

        hashes = {}

        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):

                file_hash = get_file_hash(file_path)

                if file_hash in hashes:

                    os.remove(file_path)

                    logging.info(f"Removed duplicate file: {file}")

                    print(f"Duplicate Removed: {file}")

                else:
                    hashes[file_hash] = file

    except Exception as e:
        logging.error(f"Error removing duplicates: {e}")
        print("Error:", e)