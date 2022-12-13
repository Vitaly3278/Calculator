#Запуск программы

from console import console
from rational import rational
from complex import complex
from logger import result_logger

data = console()
if data[3] == '1':
    result = complex(data)
elif data[3] == '2':
    result = rational(data)
else:
    result = 'Ошибка, неправильно введены данные!!!'
print(f'Результат вычисления {data[0]} {data[2]} {data[1]} = {result}\n')
print('Результат записан в файл log.txt')
result_logger(data, result)
