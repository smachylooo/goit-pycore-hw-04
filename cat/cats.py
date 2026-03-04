import pathlib
from helpers import get_cats_by_id, get_cats_lst

def get_cats_info(path):
    cats_lst = get_cats_lst(path)
    cats_dict = get_cats_by_id(cats_lst)
    return cats_dict

file_in_dir = 'cats.txt'
path = pathlib.Path(__file__).parent / file_in_dir

cats_info = get_cats_info(path)
print(cats_info)
