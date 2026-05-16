def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            recipe_name = file.readline().strip()
            if not recipe_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip().split(' | ')
                ingredient_name = ingredient_line[0]
                ingredient_quantity = int(ingredient_line[1])
                ingredient_measure = ingredient_line[2]
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': ingredient_quantity,
                    'measure': ingredient_measure
                }
                ingredients.append(ingredient)
            cook_book[recipe_name] = ingredients
            file.readline()
    return cook_book

cook_book = read_recipes('cook_book.txt')
print(cook_book)