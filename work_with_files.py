import os
from pprint import pprint

# >>> with open('dog_breeds.txt', 'r') as reader:
# >>>     # Read and print the entire file line by line
# >>>     for line in reader:
# >>>         print(line, end='')
# This final approach is more Pythonic and can be quicker and more memory efficient.

def read_cook_book(file_path):
    dish_dict = {}
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            if len(line) == 0:
                continue
            dish_name = line
            n = int(f.readline().strip('\n'))
            ing_list = []
            for i in range(0, n):
                ingredient = {}
                ln = f.readline().strip('\n')
                ingredient_name, quantity, measure = ln.split('|')
                ingredient['ingredient_name'] = ingredient_name.strip()
                ingredient['quantity'] = int(quantity.strip())
                ingredient['measure'] = measure.strip()
                ing_list.append(ingredient)

            dish_dict[dish_name] = ing_list
    return dish_dict

def get_shop_list_by_dishes(dishes, person_count):
    a_cook_book = read_cook_book('recipes.txt')
    ing_dict = {}
    for dish in dishes:
        ings_list = a_cook_book[dish]
        for ing in ings_list:
            ing_name = ing['ingredient_name']
            if ing_dict.__contains__(ing_name):
                ing_dict[ing_name]['quantity'] += ing['quantity'] * person_count
            else:
                ing_dict[ing_name] = {
                    'measure': ing['measure'],
                    'quantity' : ing['quantity'] * person_count
                    }
    return ing_dict


def sorted_merge(sorted_dir_path, merged_file_path):
    BASE_DIR = sorted_dir_path
    
    files_info = []
    try:
        for file_name in os.listdir(BASE_DIR):
            file_path = os.path.join(BASE_DIR, file_name)
            with open(file_path, encoding='utf-8') as f:
                files_info.append( [file_name, len(f.readlines())] )
    except:
        return

    files_info.sort(key=lambda x: x[1])

    with open(merged_file_path, 'w') as mf:
        for file_info in files_info:
            file_path = os.path.join(BASE_DIR, file_info[0])
            with open(file_path, encoding='utf-8') as f:
                mf.write(file_info[0] + '\n')
                mf.write(str(file_info[1]) + '\n')
                text = f.read()
                mf.write(text)
                if len(text) > 0 and text[-1] != '\n':
                    mf.write('\n')


sorted_dir_path = os.path.join(os.getcwd(), 'sorted')
merged_file_path = os.path.join(os.getcwd(), 'merged.txt')
sorted_merge(sorted_dir_path, merged_file_path)
with open(merged_file_path, 'r') as mf:
    print(mf.read())
os.remove(merged_file_path)