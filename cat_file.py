from sys import argv
import os
import paths

def cat_file():
    digest = argv[-1]
    digest_file_match = paths.objects_dir_path + digest[0:2] + "/{file}".format(file=digest[2:])

    with open(digest_file_match, "r") as file:
        for line in file:
            print(line, end="")

if __name__ == "__main__":
    cat_file()