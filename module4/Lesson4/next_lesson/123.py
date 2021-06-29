def modeling(factor, *_, correction=1):
    return factor * correction

print(modeling(4,5,6,7,correction=0.2))