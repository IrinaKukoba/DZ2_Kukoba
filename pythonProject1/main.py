import json


def parse_cookbook(filename):
    cook_book = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                # Пропуск пустых строк
                if not lines[i].strip():
                    i += 1
                    continue

                dish_name = lines[i].strip()  # Название блюд
                i += 1


                while i < len(lines) and not lines[i].strip():
                    i += 1

                if i >= len(lines) or not lines[i].strip().isdigit():
                    raise ValueError("Недостаточно строк для количества ингредиентов или неверный формат.")

                ingredients_count = int(lines[i].strip())  # Кол-во ингред.
                i += 1
                ingredients = []

                while i < len(lines) and not lines[i].strip():
                    i += 1

                for _ in range(ingredients_count):
                    if i >= len(lines):
                        raise ValueError("Недостаточно строк для описания ингредиента.")

                    ingredient_line = lines[i].strip().split(
                        ' | ')
                    if len(ingredient_line) != 3:
                        print(
                            f"Ошибка в формате ингредиента: '{lines[i].strip()}'. Ожидалось 'название | количество | единицы измерения'.")
                        break

                    ingredients.append({
                        'ingredient_name': ingredient_line[0],
                        'quantity': ingredient_line[1],
                        'measure': ingredient_line[2]
                    })
                    i += 1

                cook_book[dish_name] = ingredients
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]

            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = float(ingredient['quantity']) * person_count
                measure = ingredient['measure']

                if name in shop_list:

                    shop_list[name]['quantity'] += quantity
                else:

                    shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list

if __name__ == "__main__":
    filename = 'resept.txt'
    cook_book = parse_cookbook(filename)

    result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

    print(json.dumps(result, ensure_ascii=False, indent=2))
