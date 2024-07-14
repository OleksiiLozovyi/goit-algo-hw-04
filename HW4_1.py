def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                name, salary = line.split(',')
                salaries.append(float(salary))

        total = sum(salaries)
        average = total / len(salaries) if salaries else 0

        return total, average

    except FileNotFoundError:
        print("File not found.")
        return 0, 0
    except ValueError:
        print("File has wrong data.")
        return 0, 0
    finally:
        file.close()


# Приклад використання функції
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")