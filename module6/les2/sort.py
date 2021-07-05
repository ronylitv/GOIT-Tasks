import sys
from pathlib import Path
import shutil
import scan
from normalize import normalize


def handle_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def handle_doc(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def handle_vid(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def handle_mus(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def handle_other(file, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def handle_archive(file: Path, root_folder: Path, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    folder_for_arch = normalize(file.name.replace(ext, ''))
    archive_folder = target_folder / folder_for_arch
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    file.unlink()




def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        pass


def main(folder):
    scan.scan(folder)

    for file in scan.JPEG_IMAGES:
        handle_image(file, folder, 'IMAGES')

    for file in scan.JPG_IMAGES:
        handle_image(file, folder, 'IMAGES')

    for file in scan.PNG_IMAGES:
        handle_image(file, folder, 'IMAGES')

    for file in scan.SVG_IMAGES:
        handle_image(file, folder, 'IMAGES')

    for file in scan.DOC_doc:
        handle_doc(file, folder, 'DOCUMENTS')

    for file in scan.DOCX_doc:
        handle_doc(file, folder, 'DOCUMENTS')

    for file in scan.TXT_doc:
        handle_doc(file, folder, 'DOCUMENTS')

    for file in scan.PDF_doc:
        handle_doc(file, folder, 'DOCUMENTS')

    for file in scan.XLSX_doc:
        handle_doc(file, folder, 'DOCUMENTS')

    for file in scan.PPTX_doc:
        handle_doc(file, folder, 'DOCUMENTS')

    for file in scan.AVI_VIDEO:
        handle_vid(file, folder, 'VIDEO')

    for file in scan.MP4_VIDEO:
        handle_vid(file, folder, 'VIDEO')

    for file in scan.MOV_VIDEO:
        handle_vid(file, folder, 'VIDEO')

    for file in scan.MKV_VIDEO:
        handle_vid(file, folder, 'VIDEO')

    for file in scan.MP3_MUS:
        handle_mus(file, folder, 'MUSIC')

    for file in scan.OGG_MUS:
        handle_mus(file, folder, 'MUSIC')

    for file in scan.WAV_MUS:
        handle_mus(file, folder, 'MUSIC')

    for file in scan.AMR_MUS:
        handle_mus(file, folder, 'MUSIC')

    for file in scan.OTHER:
        handle_other(file, folder, 'OTHER')

    for file in scan.ARCH:
        handle_archive(file, folder, 'ARCH')

    for f in scan.FOLDERS:
        handle_folder(f)


if __name__ == '__main__':
    scan_path = sys.argv[1]
    print(f'Start in folder {scan_path}')

    sort_folder = Path(scan_path)
    main(sort_folder.resolve())
    print(sort_folder.resolve())
