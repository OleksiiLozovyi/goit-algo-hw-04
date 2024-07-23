def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.replace("\n","").split(",")
                cats_info.append({"id": id, "name": name, "age": age})

        return cats_info

    except FileNotFoundError:
        print("File not found.")

    except ValueError:
        print("File has wrong data.")



cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
