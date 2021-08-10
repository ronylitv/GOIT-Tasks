points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
# coordinates = [0, 1, 3, les2, 0]


def calculate_distance(coordinates):
    cord = []
    val = 0
    wait_for_number = True
    quantity_of_cords = 0
    main_cycle = True
    while main_cycle:
        while wait_for_number:
            for i in coordinates:
                cord.append(i)
                quantity_of_cords += 1
                cord.sort()
                if quantity_of_cords == 2:
                    cord = tuple(cord)
                    wait_for_number = False
                    break

        while not wait_for_number:
            for i in points.keys():
                if cord == i:
                    val += points[i]
                    coordinates = coordinates[1:]
                    quantity_of_cords = 0
                    cord = []
                    wait_for_number = True
                    break
        if len(coordinates) == 1:
            main_cycle = False
    return val


print(calculate_distance([0, 1, 3, 2, 0]))








