from sys import argv
import hashlib
import os
import shutil
from pathlib import Path
import paths

def hash_object():
    # tells the hash_object function to hash the last argument as a string
    # if --stdin is not specified, the hash_object function defaults
    # to hashing the last argument as a file (requires a file path)
    if "--stdin" in argv:
        content = argv[-1]
    if "--stdin" not in argv:
        content = argv[-1]

    hashed_content = hashlib.sha1(content.encode("utf-8")).hexdigest()
    hashed_content_dir_path = paths.objects_dir_path + hashed_content[0:2]
    hashed_content_file_path = hashed_content_dir_path + "/{file}".format(file=hashed_content[2:])

    # if the -w flag is included, the function will write the hashed content
    # to a directory / file pair in the .up/objects directory, otherwise
    # it will print out the hashed content
    if "-w" in argv:
        # TODO optimize argv iterator

        def make_content_structure():
            os.mkdir(hashed_content_dir_path)
            Path(hashed_content_file_path).touch()
            with open(hashed_content_file_path, "w") as file:
                file.write(content)

        try:
            make_content_structure()
        except FileExistsError:
            shutil.rmtree(hashed_content_dir_path)
            make_content_structure()

if __name__ == "__main__":
    hash_object()