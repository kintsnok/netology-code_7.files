import os
from pprint import pprint

# >>> with open('dog_breeds.txt', 'r') as reader:
# >>>     # Read and print the entire file line by line
# >>>     for line in reader:
# >>>         print(line, end='')
# This final approach is more Pythonic and can be quicker and more memory efficient.

# Задача №1
def read_cook_book(file_path):
    '''Считывает файл книги рецептов и создаёт словарь требуемого вида'''
    dish_dict = {}
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            # получение названия блюда
            line = line.strip('\n')
            if len(line) == 0:
                continue
            dish_name = line
            # получение количества ингредиентов
            n = 0
            try:
                n = int(f.readline().strip('\n'))
            except:
                continue
            # получение списка ингредиентов
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

# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    '''Создаёт словарь с названием ингредиентов и их количества для блюда'''
    a_cook_book = read_cook_book('recipes.txt')
    ing_dict = {}
    for dish in dishes:
        ings_list = a_cook_book[dish]
        for ing in ings_list:
            ing_name = ing['ingredient_name']
            if ing_name in ing_dict:
                ing_dict[ing_name]['quantity'] += ing['quantity'] * person_count
            else:
                ing_dict[ing_name] = {
                    'measure': ing['measure'],
                    'quantity' : ing['quantity'] * person_count
                    }
    return ing_dict

# Задача №3
def sorted_merge(sorted_dir_path, merged_file_path):
    files_info = []
    try:
        for file_name in os.listdir(sorted_dir_path):
            file_path = os.path.join(sorted_dir_path, file_name)
            with open(file_path, encoding='utf-8') as f:
                files_info.append( [file_name, len(f.readlines())] )
    except:
        return

    files_info.sort(key=lambda x: x[1])

    with open(merged_file_path, 'w') as mf:
        for file_info in files_info:
            file_path = os.path.join(sorted_dir_path, file_info[0])
            with open(file_path, encoding='utf-8') as f:
                mf.write(file_info[0] + '\n')
                mf.write(str(file_info[1]) + '\n')
                text = f.read()
                mf.write(text)
                if len(text) > 0 and text[-1] != '\n':
                    mf.write('\n')


def task1_test():
    print('- Тест №1 -------------------------------------------------------------------')
    cook_book = read_cook_book('recipes.txt')
    print('cook_book =')
    pprint(cook_book, indent=2, width=160)

def task2_test():
    print('- Тест №2 -------------------------------------------------------------------')
    print('Запеченный картофель и Омлет на две персоны')
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    pprint(shop_list, indent=2, width=160)
    print()
    print('Фахитос Омлет на две персоны. Помидоров должно быть восемь')
    shop_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
    pprint(shop_list, indent=2, width=160)

def task3_test():
    print('- Тест №3 -------------------------------------------------------------------')
    sorted_dir_path = os.path.join(os.getcwd(), 'sorted')  # Путь к директории с файлами для сортировки
    merged_file_path = os.path.join(os.getcwd(), 'merged.txt')  # Путь к создаваемому файлу слияния
    sorted_merge(sorted_dir_path, merged_file_path)
    with open(merged_file_path, 'r') as mf:
        print(mf.read())  # Вывод содержимого файла слиняния
    os.remove(merged_file_path)  # Удаляю созданный файл слияния


# Тесты
task1_test()
print()
task2_test()
print()
task3_test()