# def read_recipes(file_name):
#     cook_book = {}
#     with open(file_name, 'r', encoding='utf-8') as file:
#         while True:
#             recipe_name = file.readline().strip()
#             if not recipe_name:
#                 break
            
#             ingredient_count = int(file.readline().strip())
#             ingredients = []
            
#             for _ in range(ingredient_count):
#                 ingredient_line = file.readline().strip().split(' | ')
#                 ingredient_name = ingredient_line[0]
#                 ingredient_quantity = int(ingredient_line[1])
#                 ingredient_measure = ingredient_line[2]
                
#                 ingredient = {
#                     'ingredient_name': ingredient_name,
#                     'quantity': ingredient_quantity,
#                     'measure': ingredient_measure
#                 }
#                 ingredients.append(ingredient)
            
#             cook_book[recipe_name] = ingredients
            
#             file.readline()
            
#     return cook_book


# cook_book = read_recipes('book.txt')
# print(cook_book)

# def read_cook_book(file_path):
#     cook_book = {}
#     with open(file_path, 'r', encoding='utf-8') as file:
#         while True:
#             dish_name = file.readline().strip()
#             if not dish_name:
#                 break


#             ingredient_count = int(file.readline().strip())
#             ingredients = []
#             for _ in range(ingredient_count):
#                 ingredient_info = file.readline().strip().split(' | ')



#                 ingredient = {
#                     'ingredient_name': ingredient_info[0],
#                     'quantity': int(ingredient_info[1]),
#                     'measure': ingredient_info[2]
#                 }
#                 ingredients.append(ingredient)
#             cook_book[dish_name] = ingredients
#             file.readline()
#     return cook_book

# cook_book = read_cook_book('book.txt')

# def get_shop_list_by_dishes(dishes, person_count):
#     shop_list = {}
#     for dish in dishes:
#         for ingredient in cook_book[dish]:
#             ingredient_name = ingredient['ingredient_name']
#             measure = ingredient['measure']
#             quantity = ingredient['quantity'] * person_count
#             if ingredient_name in shop_list:
#                 shop_list[ingredient_name]['quantity'] += quantity
#             else:
#                 shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
#     return shop_list
# def print_shop_list(shop_list):
#     for ingredient, details in shop_list.items():
#         measure = details['measure']
#         quantity = details['quantity']
#         print(f'{ingredient}: {quantity} {measure}')

# dishes = ['Запеченный картофель', 'Омлет']
# person_count = 2

# shop_list = get_shop_list_by_dishes(dishes, person_count)
# print_shop_list(shop_list)
