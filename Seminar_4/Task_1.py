# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки


my_str = 'Это строка текста'
new_str = sorted(my_str.split())
for number, word in enumerate(new_str, start=1):
    print(f'{number}\t{word}')