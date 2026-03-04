def get_cats_lst(path):
        cats_lst = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for row in file:
                    cats_lst.append(row.strip().split(','))
            return cats_lst
        except FileNotFoundError:
             return "File not found"
        
def get_cats_by_id(cats):
    if not cats:
        return []
    cat = cats[0]
    return [{"id": cat[0], "name": cat[1], "age": cat[2]}] + get_cats_by_id(cats[1:])
    