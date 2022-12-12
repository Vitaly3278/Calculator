# Обработка комплексных чисел


def complex(data):
    value1, value2, oper, choise = data
    if oper == '+':
        return value1 + value2
    if oper == '-':
        return value1 - value2
    if oper == '*':
        return value1 * value2
    if oper == '/':
        return value1 / value2
    else:
        return 'Ошибка, неправильно введены данные!!!'
