from sys import argv
import os
import paths

def cat_file(digest):
    digest_file_match = paths.objects_dir_path + digest[0:2] + "/{file}".format(file=digest[2:])

    with open(digest_file_match, "r") as file:
        return file.read()

if __name__ == "__main__":
    print(cat_file("1eebdf4fdc9fc7bf283031b93f9aef3338de9052"))
    print(cat_file("6605780cc62e8ac9104c41a5f7cfac4b14d07cf6"))