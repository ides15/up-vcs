# import hashlib
import os

def up_init():
    up_dir_path = ".up/"
    uprc_file_path = ".up/uprc"

    uprc_file = generate_structure(up_dir_path, uprc_file_path)

    generate_file_and_dir_list(uprc_file)

    # other config file setups would go here...
    # ...
    # ...

    uprc_file.close()
    exit()

def generate_file_and_dir_list(uprc_file):
    FIL = []
    DIR = {}

    with os.scandir() as dir:
        for node in dir:
            if node.is_file():
                FIL.append(node)

    print(FIL)


def generate_structure(up_dir_path, uprc_file_path):
    # setting up config folder structure, mainly for debugging
    if os.path.exists(up_dir_path):
        print(up_dir_path + " exists")
    else:
        print(up_dir_path + " doesn't exist, creating...")
        os.mkdir(up_dir_path)

    # setting up config file, mainly for debugging
    if os.path.exists(uprc_file_path):
        print(uprc_file_path + " exists")
    else:
        print(uprc_file_path + " doesn't exist, creating...")

    uprc_file = open(uprc_file_path, 'w')

    dir_name = os.path.basename(os.getcwd())
    uprc_file.write("NAME=" + dir_name + "\n")
    print("wrote " + dir_name + " to uprc file")
    # hashlib.md5(dir_name.encode("utf-8")).hexdigest()

    print("created up structure")
    return uprc_file