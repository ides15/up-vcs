import hashlib
import os

from init import init
from hash_object import hash_object
from cat_file import cat_file

def parse_args(args):
    for arg in args:
        parse_arg(arg)

def parse_arg(arg):
    if arg == "init":
        init()
    if arg == "hash-object":
        hash_object()
    if arg == "cat-file":
        cat_file()