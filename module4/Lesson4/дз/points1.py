points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    val = 0
    if len(coordinates) <= 1:
        return 0
    while len(coordinates) != 1:
        new_points = coordinates[:2]
        new_points.sort()
        new_points = tuple(new_points)
        if new_points in points.keys():
            val += points[new_points]
            coordinates = coordinates[1:]

    return val


print(calculate_distance([0, 1, 3, 2, 0]))


points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) > 1:
        distance = 0
        step = []
        #        step = step.sort()
        for i in coordinates[:-1]:
            step.append(sorted(coordinates[0:2]))
            coordinates = coordinates[1:]
    print(step)
    for i in step:
        i = tuple(i)
        if tuple(i) in points.keys():
            distance += points[i]

    return distance





print(calculate_distance([0, 1, 3, 2, 0]))
