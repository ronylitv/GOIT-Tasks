from pathlib import Path
import re


def folder_parser_goit(folder: Path):
    FOLDERS = []
    folder = Path(folder)
    for el in folder.iterdir():
        if el.is_dir():
            if not el.name.find('module'):
                FOLDERS.append(el.name)
    return FOLDERS


def new_folder_name(folder: Path):
    folder = Path(folder)
    fold_list = folder_parser_goit(folder)
    fold = []
    for el in fold_list:
        res = re.search(r'\d', el)
        fold.append(res.group())
    last_element = int(fold[-1]) + 1
    new_dir = f'module{last_element}'

    return new_dir


def folder_creator(folder: Path):
    folder_list = ['hw', 'les1', 'les2']
    dir_name = new_folder_name(folder)
    folder = Path(folder)
    lol = folder / dir_name
    lol.mkdir()
    for el in folder_list:
        new_dir = lol / el
        new_dir.mkdir()


def func():
    folder_creator('C:/Users\Lenovo\PycharmProjects\lesson')


