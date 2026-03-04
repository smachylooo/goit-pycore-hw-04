import sys
import pathlib
from colorama import Fore

def read_dir(path, level=0):
    for item in pathlib.Path(path).iterdir():
        indent = "  " * level

        if item.is_dir():
            print(indent + Fore.BLUE + item.name + '/')
            read_dir(item, level + 1)
        else:
            print(indent + Fore.GREEN + item.name)

path = pathlib.Path(sys.argv[1])
read_dir(path)