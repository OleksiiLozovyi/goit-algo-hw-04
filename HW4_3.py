from colorama import Fore
import sys


path = sys.argv[1]


from pathlib import Path


parent_folder_path = Path(path)

def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(Fore.RED + f"Директорія {element.name}")
            parse_folder(element)
        if element.is_file():
            print(Fore.GREEN + f"Файл {element.name}")
parse_folder(parent_folder_path)