from pathlib import Path

folder = Path('Temp')
try:
    with open(folder / 'temp.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.rstrip())

except OSError:
    print('Error in file')

try:
    file = open(folder / 'temp.txt', 'r', encoding='utf-8')
    try:
        while True:
            line = file.read()
            if not line:
                break
            print(line.rstrip())
    except OSError:
        print('Error 10')
    finally:
        file.close()
except OSError:
    print('Error access to file')
