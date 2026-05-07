import os
import logging

def rename_files(path, prefix):

    try:

        count = 1

        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):

                extension = os.path.splitext(file)[1]

                new_name = f"{prefix}_{count}{extension}"

                new_path = os.path.join(path, new_name)

                os.rename(file_path, new_path)

                logging.info(f"Renamed {file} to {new_name}")

                print(f"Renamed: {file} -> {new_name}")

                count += 1

    except Exception as e:
        logging.error(f"Error renaming files: {e}")
        print("Error:", e)