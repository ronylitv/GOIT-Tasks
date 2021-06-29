import sys
import os
from pathlib import Path


def parse_folder(path):

    doc_type = ['.docx', '.xlsx', '.xlsm', '.pdf', '.doc', '.txt']
    music_type = ['.mp3', '.ogg', '.wav', '.amr']
    photo_type = ['.jpeg', '.png', '.jpg', '.svg']
    video_type = ['.avi', '.mp4', '.mov', '.mkv']
    archive_type = ['.zip', '.gz', '.tar']

    files_doc = []
    files_music = []
    files_photo = []
    files_video = []
    files_archive = []

    p = Path()
    for i in p.iterdir():
        if i.is_dir():
            print(f'Find new folder: {i.name}')
            parse_folder(i)
        else:
            print(f'Find new file: {i.name}')
            if i.suffix in doc_type:
                files_doc.append(i.name)

            elif i.suffix in photo_type:
                files_photo.append(i.name)
            elif i.suffix in music_type:
                files_music.append(i.name)

            elif i.suffix in archive_type:
                files_archive.append(i.name)
            elif i.suffix in video_type:
                files_video.append(i.name)


parse_folder(sys.argv[1])
