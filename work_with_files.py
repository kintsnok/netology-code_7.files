#import os
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

a_cook_book = read_cook_book('recipes.txt')
                              

pprint(a_cook_book, width=120)