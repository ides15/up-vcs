import hashlib
import os

from verbs.up_init import up_init

def parse_args(args):
    for arg in args:
        parse_arg(arg)

def parse_arg(arg):
    if arg == "init":
        print("init argument flagged")
        up_init()