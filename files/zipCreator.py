from zipfile import ZipFile
from pathlib import Path


def make_archive(file_paths, destination_directory):
    with ZipFile(Path(destination_directory, 'compressed.zip'), 'w') as archive:
        for singleFilePath in file_paths:
            # Assigning singleFilePath.name to arcname is to prevent the absolute path being generated for the
            # output zip file, ex. Users/as/Downloads/a.txt
            archive.write(singleFilePath, arcname=Path(singleFilePath).name)


if __name__ == '__main__':
    make_archive(file_paths=['experiment.py', 'ideas.txt'], destination_directory='./')


