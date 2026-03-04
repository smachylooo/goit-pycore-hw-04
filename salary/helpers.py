import pathlib

def extract_workers(path):
    path = pathlib.Path(path)
    worker_lst = []
    try:
        with open(path, 'r', encoding="utf-8") as file:
            for row in file:
                phrase = row.strip().split(',')
                worker_lst.append(phrase)
    except FileNotFoundError:
        return "File not found!"
    return worker_lst

def get_total_salary(worker_lst):
    if not worker_lst:
        return 0
    return int(worker_lst[0][1]) + get_total_salary(worker_lst[1:])
