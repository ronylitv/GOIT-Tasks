import shutil
from pathlib import Path

slovar = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}


def create_backup(path, file_name, employee_residence):

    with open(path + '/' + file_name, 'wb') as f:
        for ind, val in employee_residence.items():
            b = f'{ind} {val}\n'.encode()
            f.write(b)
        arch_name = shutil.make_archive('backup_folder', 'zip', path)


    return arch_name


print(create_backup('C:/Users\Lenovo\Desktop\Folder_for_script\skss_13', 'cook.txt', slovar))
