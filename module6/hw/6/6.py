def get_recipe(path, search_id):
    with open(path, "r") as fh:
        lines = fh.readlines()
        for i in lines:
            if search_id in i:
                recipe_food = i.split(',')
                result = {
                    'id': recipe_food[0],
                    'name': recipe_food[1],
                    'ingredients': [i.strip() for i in recipe_food[2:]]
                }
                break
            else:
                result = None

    return result


print(get_recipe('recipe.txt', '60b90c3b13067a15887e1ae4'))
