import os

file_names = ['1.txt', '2.txt', '3.txt']

file_info = {}

for file_name in file_names:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
            line_count = len(content)
            file_info[file_name] = (line_count, content)
    except UnicodeDecodeError:
        print(f"Ошибка при чтении файла {file_name}.")
        try:
            with open(file_name, 'r', encoding='cp1251') as file:
                content = file.readlines()
                line_count = len(content)
                file_info[file_name] = (line_count, content)
        except Exception as e:
            print(f"Не удалось открыть файл {file_name}. Ошибка: {e}")
            continue

sorted_files = sorted(file_info.items(), key=lambda item: item[1][0])

with open('merged_file.txt', 'w', encoding='utf-8') as merged_file:
    for file_name, (line_count, content) in sorted_files:

        merged_file.write(f"{file_name}\n{line_count}\n")

        merged_file.writelines(content)
        merged_file.write("\n")

print("Файлы объединены ")
