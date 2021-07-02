def get_recipe(path, search_id):
    with open(path, 'r') as fh:

        while True:
            line = fh.readline()
            if search_id in line:
                list_of_recipe = line.split(',')

            if not line:
                break
    return list_of_recipe

print(get_recipe('recipe.txt', '60b90c4613067a15887e1ae5'))


