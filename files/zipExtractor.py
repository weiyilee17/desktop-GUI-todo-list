from zipfile import ZipFile
from pathlib import Path


def extract_archive(archive_path, destination_directory):
    with ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_directory)


if __name__ == '__main__':
    extract_archive(
        archive_path='/Users/weiyilee/Desktop/code/python/Ardit Sulce Tutorial/Todo List App/files/compressed.zip',
        destination_directory='/Users/weiyilee/Desktop/code/python/Ardit Sulce Tutorial/Todo List App'
    )


