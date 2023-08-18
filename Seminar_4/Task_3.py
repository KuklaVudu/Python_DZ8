# Функция принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def det_bonusis(names, salarys, bonuss):
    bonus_dict = {}
    for name, salary, bonus in zip(names, salarys, bonuss):
        bonus_dict[name] = salary * float(bonus[: -1]) / 100
    return bonus_dict 


names1 = ['Alex', 'Andrey', 'Vlad']
salary2 = [10000, 20000, 30000]
bonuss3 = ['0.9%', '10.25%', '11.5%']

print(det_bonusis(names1, salary2, bonuss3))