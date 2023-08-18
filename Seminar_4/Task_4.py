# Функция получает на вход словарь с названием компании
# в качестве ключа и списком с доходами и расходами (3-10 чисел)
# в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину,
# а если хотя бы одна убыточная - ложь.


def is_all_profit(data):
    counter = 0
    for value in data.values():
        if sum(value) > 0:
            counter += 1
        if counter == len(data.values()):
            return True      
        else:
            return False


def is_all_profit_v2(data):
    return all(map(lambda x: sum(x) > 0, data.values()))


companys = {
    "Рога": [10, 10],
    "Копыта": [20, -220],
    "Хвосты": [30, 30],
}

print(is_all_profit(companys))
print(is_all_profit_v2(companys))