from pathlib import Path

p = Path()

def parse_folder(path):
    for i in path.iterdir():
        if i.is_dir():
            print(f'This is folder {i.name}')
        else:
            print(f'THis is file {i.name}')



def parse_folder_recursion(path):
    for i in path.iterdir():
        if i.is_dir():
            parse_folder_recursion(i)
        else:
            print(f'THis is file {i.name}')


parse_folder_recursion(p)