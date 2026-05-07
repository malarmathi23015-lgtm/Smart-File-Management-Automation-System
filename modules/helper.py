import os
import hashlib
import logging

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_folder(folder_name):

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def get_file_hash(filepath):

    hasher = hashlib.md5()

    with open(filepath, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)

    return hasher.hexdigest()