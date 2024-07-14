# import sys
# import os
# from pathlib import Path
# from colorama import init, Fore, Style
#
# # Ініціалізація colorama для підтримки кольорового виведення в терміналі
# init(autoreset=True)
#
# def list_directory_contents(directory_path):
#     try:
#         # Перетворюємо введений шлях в об'єкт pathlib.Path
#         directory = Path(directory_path)
#
#         # Перевіряємо, чи введений шлях є дійсною директорією
#         if not directory.is_dir():
#             raise NotADirectoryError(f"{directory_path} не є директорією")
#
#         print(f"Contents of directory: {directory}\n")
#
#         # Ітеруємося по вмісту директорії
#         for item in directory.iterdir():
#             if item.is_dir():
#                 print(Fore.BLUE + f"📁 {item.name}")
#             elif item.is_file():
#                 print(Fore.GREEN + f"📄 {item.name}")
#             else:
#                 print(Fore.RED + f"🗂️ {item.name}")  # Якщо щось інше (наприклад, символічне посилання)
#
#     except FileNotFoundError:
#         print(Fore.RED + f"Помилка: {directory_path} не знайдено")
#     except NotADirectoryError as e:
#         print(Fore.RED + f"Помилка: {e}")
#     except Exception as e:
#         print(Fore.RED + f"Помилка: {e}")
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print(Fore.YELLOW + "Використання: python script.py /шлях/до/директорії")
#     else:
#         directory_path = sys.argv[1]
#         list_directory_contents(directory_path)


from colorama import Fore
import sys
from pathlib import Path



parent_folder_path =  Path(".")

def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            parse_folder(element)
            print(Fore.RED + f"Директорія {element.name}")
        if element.is_file():
            print(Fore.GREEN + f"Файл {element.name}")
parse_folder(parent_folder_path)