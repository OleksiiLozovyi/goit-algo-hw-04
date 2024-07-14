def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.split(',')
                cats_info.append({"id": id, "name": name, "age": age})
        return cats_info

    except FileNotFoundError:
        print("File not found.")
        return 0, 0
    except ValueError:
        print("File has wrong data.")
        return 0, 0
    finally:
        file.close()


cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
