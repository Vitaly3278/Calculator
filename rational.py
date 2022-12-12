# Обработка рациональных чисел


def rational(data):
    value1, value2, oper, choise = data
    x = value1.split('/')
    y = value2.split('/')
    if oper == '+':
        return (int(x[0]) / int(x[1])) + (int(y[0]) / int(y[1]))
    if oper == '-':
        return (int(x[0]) / int(x[1])) - (int(y[0]) / int(y[1]))
    if oper == '*':
        return (int(x[0]) / int(x[1])) * (int(y[0]) / int(y[1]))
    if oper == '/' and value2 != 0:
        return (int(x[0]) / int(x[1])) / (int(y[0]) / int(y[1]))
    else:
        return 'Ошибка, неправильно введены данные!!!'
