from pathlib import Path

folder = Path('temp')
list_data = ['Natalia', 'Inna', 'Andriy', 'Ivan']
try:
    with open(folder / 'data.txt', 'w', encoding='utf-8') as f:
        for line in list_data:
            f.write(line + '\n')

except OSError:
    print('Error in file')
try:
    with open(folder / 'data-all.txt', 'a', encoding='utf-8') as f:
        for line in list_data:
            f.writelines(['Natalia\n', 'Inna\n', 'Andriy\n', 'Ivan\n'])

except OSError:
    print('Error in file')
