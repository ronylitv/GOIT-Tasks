def game(terra, power):
    for i in terra:
        for j in i:
            if power <= j:
                power += j
            else:
                break
    return power


print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))