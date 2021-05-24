import sys
import os
from typing import final

args = sys.argv

def write_gitignore(folder_path: str) -> None:
    content = ".exercism\n__pycache__"
   
    try:
        if not os.path.isdir(folder_path):
            raise NotADirectoryError()
        file_path = os.path.join(folder_path, ".gitignore")
        print(f"writing to {file_path}")
        with open(file_path, 'w') as file:
            file.write(content)
            file.close()
    except NotADirectoryError:
        sys.stderr('Provided filepath is not a directory.')
    except PermissionError:
        sys.stderr('Access denied. Check file permissions.')
    except FileExistsError:
        sys.stderr('.gitignore file already exists in the foler.')
    except OSError:
        sys.stderr('could not create file')
    finally:
        return None

if __name__=='__main__':
    if len(args) < 2:
        raise ValueError("Must provide path to folder")
    if len(args) > 2:
        raise ValueError("Too many arguments. Provide a single valid folder path.")

    folder_path = args[1]

    write_gitignore(folder_path)
