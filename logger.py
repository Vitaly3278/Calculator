#Логирование в файл
from datetime import datetime as dt


def result_logger(data, result):
    value1, value2, oper, choise = data
    time = dt.now().strftime('%H:%M:%S')
    log = f'\nВремя: {time}\nРезультат вычисления {value1} {oper} {value2} = {result}'
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(log)
