import sys
from pathlib import Path
import shutil
import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LAT_TRANS = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
             "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}

for key, value in zip(CYRILLIC_SYMBOLS, LAT_TRANS):
    TRANS[ord(key)] = value
    TRANS[ord(key.upper())] = value.upper()


def normalize(string) -> str:
    translated_string = string.translate(TRANS)
    translated_string = re.sub(r'\W', '_', translated_string)
    return translated_string


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
FOLDERS = []
EXTENSIONS = set()
OTHER = []
REGIST_EXT = {

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

p = Path('C:/Users\Lenovo\Desktop\Folder_for_script/fold')



def folder_del(folder:Path):
    try:
        shutil.rmtree(folder)
    except:
        pass





def parse_folder(path):
    p = Path(path)
    for file in p.iterdir():
        if file.is_dir():
            if file.name not in ['IMAGES', 'DOCS', 'ARCH', 'OTHER', 'VIDEOS', 'MUSIC']:
                FOLDERS.append(file)
                parse_folder(file)

            continue
        else:
            ext = file.suffix[1:].upper()
            EXTENSIONS.add(ext)
            if ext in REGIST_EXT.keys():
                REGIST_EXT[ext].append(file)
            else:
                REGIST_EXT['OTHER'].append(file)

    return REGIST_EXT


parse_folder(p)


def handle_image(file: Path, root_folder: Path, dist: str):
    ext = Path(file).suffix
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    new_target_folder = target_folder / ext.upper()
    new_target_folder.mkdir(exist_ok=True)
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(new_target_folder / new_name)


def handle_doc(file: Path, root_folder: Path, dist: str):
    ext = Path(file).suffix
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    new_target_folder = target_folder / ext.upper()
    new_target_folder.mkdir(exist_ok=True)
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(new_target_folder / new_name)


def handle_arch(file: Path, root_folder: Path, dist: str):
    ext: str = Path(file).suffix
    new_name = normalize(file.name.replace(ext, ''))
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    arch_folder = target_folder / new_name
    arch_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(file.resolve()), str(arch_folder.resolve()))
    except:
        arch_folder.rmdir()
        return
    file.unlink()


def handle_other(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


for file in JPEG_IMAGES:
    handle_image(file, p, 'IMAGES')

for file in PNG_IMAGES:
    handle_image(file, p, 'IMAGES')

for file in TAR_ARCH:
    handle_arch(file, p, 'ARCH')

for file in JPG_IMAGES:
    handle_image(file, p, 'IMAGES')

for file in DOCX_DOC:
    handle_doc(file, p, 'DOCS')

for file in DOC_DOC:
    handle_doc(file, p, 'DOCS')

for file in PPTX_DOC:
    handle_doc(file, p, 'DOCS')

for file in XLSX_DOC:
    handle_doc(file, p, 'DOCS')

for file in PDF_DOC:
    handle_doc(file, p, 'DOCS')

for file in ZIP_ARCH:
    handle_arch(file, p, 'ARCH')

for file in OTHER:
    handle_other(file, p, 'OTHER')

for file in FOLDERS:
    folder_del(file)


print(OTHER)
print(FOLDERS)
for ind, val in REGIST_EXT.items():
    print(f'{ind}:{val}')
