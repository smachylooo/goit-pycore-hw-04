import pathlib

def extract_workers():
    pass

def total_salary(path):
    path = pathlib.Path(path)
    worker_lst = []
    with open(path, 'r', encoding="utf-8") as file:
        for row in file:
            try:
                phrase = row.strip().split(',')
                worker_lst.append(phrase)
            except FileNotFoundError:
                return "File now found!"
    

path = r'C:\Users\Bohdna Smachylo\projects\goitPython\imports\salary.txt'
total_salary(path)