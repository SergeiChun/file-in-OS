import os
import time

directory = 'C:/Test'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file},\n'
              f' Путь: {filepath},\n'
              f' Размер: {filesize} байт,\n'
              f' Время изменения: {formatted_time},\n'
              f' Родительская директория: {parent_dir}')
#Выведено в консоль
#Обнаружен файл: test_file.txt,
#Путь: C:/Test\test_file.txt,
#Размер: 173 байт,
#Время изменения: 15.07.2024 14:52,
#Родительская директория: C:/Test
