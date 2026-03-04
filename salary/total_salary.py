from helpers import * # I nee from here all functions as well as imports from file, not good practic but DRY

file_in_dir = 'salary.txt'
path = pathlib.Path(__file__).parent / file_in_dir

def total_salary(path):
    worker_lst = extract_workers(path)
    total = get_total_salary(worker_lst)
    avg = int(total / len(worker_lst))

    return (total, avg)
    
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")