from pprint import pprint

with open('reciepes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        count = int(file.readline())
        ingredients = []
        for i in range(count):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            ingredients.append({
                'ingredient_name' : ingredient_name.strip(),
                'quantity' : quantity.strip(),
                'measure' : measure.strip()
            })
        cook_book[dish] = ingredients
        file.readline()
    print()
    pprint(cook_book, sort_dicts=False)
