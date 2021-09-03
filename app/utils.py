import shutil
import os

def _save_file_to_server(uploaded_file, path=".", save_as="default"):
    temp_file = os.path.join(path, save_as)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return temp_file