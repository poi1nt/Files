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
                'quantity' : int(quantity.strip()),
                'measure' : measure.strip()
            })
        cook_book[dish] = ingredients
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    dict_product = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in dict_product:
                    dict_product[ingredient_name] = {'measure' : measure, 'quantity' : quantity}
                else:
                    dict_product[ingredient_name]['quantity'] += quantity  
    return dict_product
                
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))