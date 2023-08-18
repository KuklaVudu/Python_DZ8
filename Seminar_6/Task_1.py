# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное число в указанных границах 
# и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.


import random


def guess_game(low_lim = 1, ap_lim = 10, tryes = 3):
    res = random.randint(low_lim,ap_lim)
    for i in range(tryes):
        res_us = int(input(f'Введите число от {low_lim} до {ap_lim}: '))
        if res == res_us:
            print('Вы угадали')
            return True
        elif res > res_us:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
    else:
        return False

if __name__ == '__main__':
    guess_game()

