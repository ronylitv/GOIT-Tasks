from pathlib import Path
import shutil


class SortFolder:
    JPEG_IMAGES = []
    JPG_IMAGES = []
    PNG_IMAGES = []
    SVG_IMAGES = []
    DOC_DOC = []
    DOCX_DOC = []
    XLSX_DOC = []
    PPTX_DOC = []
    PDF_DOC = []
    ZIP_ARCH = []
    TAR_ARCH = []
    OTHER = []
    REGISTERED_EXT = {
        'JPEG': JPEG_IMAGES,
        'JPG': JPG_IMAGES,
        'PNG': PNG_IMAGES,
        'SVG': SVG_IMAGES,
        'DOC': DOC_DOC,
        'DOCX': DOCX_DOC,
        'XLSX': XLSX_DOC,
        'PPTX': PPTX_DOC,
        'PDF': PDF_DOC,
        'ZIP': ZIP_ARCH,
        "TAR": TAR_ARCH,
        'OTHER': OTHER
    }

    def __init__(self, path: Path):
        self.path = path.resolve()

    def parse_folder(self):
        for folder_item in self.path.iterdir():
            if folder_item.is_dir():
                if folder_item.name not in ['IMAGES', 'VIDEOS', 'DOCS', 'OTHER']:
                    new_folder = SortFolder(folder_item)
                    new_folder.parse_folder()
                    continue
            else:
                ext = folder_item.suffix[1:]
                if ext.upper() in SortFolder.REGISTERED_EXT.keys():
                    SortFolder.REGISTERED_EXT[ext.upper()].append(folder_item)
                else:
                    SortFolder.REGISTERED_EXT['OTHER'].append(folder_item)
        return SortFolder.REGISTERED_EXT

    def handle_file(self, file_path: Path):
        ext = file_path.suffix[1:].upper()
        if ext in ['JPG', 'SVG', 'PNG', 'JPEG']:
            category_folder = self.path / 'IMAGES'
        elif ext in ['DOC', 'DOCX', 'PPTX', 'PDF', 'XLSX']:
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
    files = folder_to_sort.parse_folder()



