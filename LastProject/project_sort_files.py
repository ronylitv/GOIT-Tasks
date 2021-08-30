from pathlib import Path
import shutil
from collections import UserDict


class SortFolder:
    record = []
    def __init__(self, path: Path):
        self.path = path.resolve()
        self.jpeg = []
        self.jpg = []
        self.png = []
        self.svg = []
        self.doc = []
        self.docx = []
        self.pdf = []
        self.pptx = []
        self.other = []
        self.registered_ext = {
            'JPEG': self.jpeg,
            'JPG': self.jpg,
            'PNG': self.png,
            'SVG': self.svg,
            'DOC': self.doc,
            'DOCX': self.docx,
            'PDF': self.pdf,
            'PPTX': self.pptx,
            'OTHER': self.other,
        }

    def parse_folder(self):
        for folder_item in self.path.iterdir():
            if folder_item.is_dir():
                if folder_item.name not in ['IMAGES', 'VIDEOS', 'DOCS', 'OTHER']:
                    new_folder = SortFolder(folder_item)
                    SortFolder.record.append(new_folder.parse_folder())
                    new_folder.parse_folder()
                    continue
            else:
                ext = folder_item.suffix[1:]
                if ext.upper() in self.registered_ext.keys():
                    self.registered_ext[ext.upper()].append(folder_item)
                else:
                    self.registered_ext['OTHER'].append(folder_item)
        return self.registered_ext

    def handle_file(self, file_path: Path):
        ext = file_path.suffix[1:].upper()
        if ext in ['JPG', 'SVG', 'PNG', 'JPEG']:
            category_folder = self.path / 'IMAGES'
        elif ext in ['DOC', 'DOCX', 'PPTX', 'PDF']:
            category_folder = self.path / 'DOCS'
        else:
            category_folder = self.path / 'OTHER'
        category_folder.mkdir(exist_ok=True)
        type_folder = category_folder / ext
        type_folder.mkdir(exist_ok=True)
        file_path.replace(type_folder / file_path.name)

    def del_unuseful_folders(self):
        for folder in self.path.iterdir():
            if folder.name not in ['IMAGES', 'DOCS', 'ARCH', 'OTHER', 'VIDEOS', 'MUSIC'] and folder.is_dir():
                shutil.rmtree(folder)


if __name__ == '__main__':
    folder_name = Path('C:/Users\Lenovo\Desktop\Folder_for_script/fold')
    folder_to_sort = SortFolder(folder_name)
    file_dict = folder_to_sort.parse_folder()
    for folder_iso in folder_to_sort.record:
        for key, val in folder_iso.items():
            for file in val:
                folder_to_sort.handle_file(file)

