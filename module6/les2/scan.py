import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_doc = []
DOCX_doc = []
FOLDERS = []
TXT_doc = []
PDF_doc = []
XLSX_doc = []
PPTX_doc = []
MP3_MUS = []
OGG_MUS = []
WAV_MUS = []
AMR_MUS = []
ARCH = []
ZIP_ARCH = []
GZ_ARCH = []
TAR_ARCH = []
OTHER = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {

    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_doc,
    'DOCX': DOCX_doc,
    'TXT': TXT_doc,
    'PDF': PDF_doc,
    'XLSX': XLSX_doc,
    'PPTX': PPTX_doc,
    'MP3': MP3_MUS,
    'OGG': OGG_MUS,
    'WAV': WAV_MUS,
    'AMR': AMR_MUS,
    'ZIP': ARCH,
    # 'GZ': GZ_ARCH,
    # 'TAR': TAR_ARCH

}


def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('JPEG', 'JPG', 'SVG', 'PNG', 'OTHER', 'ARCH', 'AVI', 'MP4', 'MKV', 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'MP3',
                                 'OGG', 'WAV', 'AMR'):

                FOLDERS.append(item)
                scan(item)

            continue
        extension = get_extension(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSION.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)



if __name__ == '__main__':
    scan_path = sys.argv[1]
    print(f'Start in folder {scan_path}')


    sort_folder = Path(scan_path)
    print(sort_folder)

