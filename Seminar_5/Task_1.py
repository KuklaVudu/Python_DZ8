# Пользователь вводит строку из четырёх или более целых чисел, 
# разделённых символом “/”. Сформируйте словарь, где:
# второе и третье число являются ключами
# первое число является значением для первого ключа
# четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа


string = '1/2/3/4/5/6/7'.split('/')
print(string)
a,b,c,*d = string
print(a,b,c,d)
result = {b: a, c: d}
print(result)