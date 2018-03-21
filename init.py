import os
from pathlib import Path
import paths

def init():
    generate_structure()

def generate_structure():
    try:
        os.mkdir(paths.up_dir_path)
        os.mkdir(paths.hooks_dir_path)
        os.mkdir(paths.info_dir_path)
        generate_objects_structure()
        os.mkdir(paths.refs_dir_path)

        Path(paths.HEAD_path).touch()
        Path(paths.config_path).touch()
        Path(paths.index_path).touch()

        print('Initialized empty Up repository in {cwd}'.format(cwd=os.getcwd() + '/.up/'))

    except FileExistsError:
        print('Up repository already exists')

def generate_objects_structure():
    os.mkdir(paths.objects_dir_path)
    os.mkdir(paths.objects_dir_path + 'info/')
    os.mkdir(paths.objects_dir_path + 'pack/')