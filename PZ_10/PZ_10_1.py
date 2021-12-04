# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого максимального элемента:
# Произведение элементов средней трети:
import random
import math
if input('Хотите пересоздать файл? ').upper() == 'да'.upper():
    with open('myfile1.txt', 'w', encoding='utf-8') as f:  # помещаем в первый файл рандомные значения рандомного кол-ва
        number = [random.randint(-100, 100) for i in range(random.randint(1, 20))]
        srez = int(len(number)/3)  # решение 4пункта
        m = number[srez:len(number) - srez]
        print('средняя треть для видимости', m)
        line = ''
        for i in number:
            line += str(i) + ' '
        f.write(line)
with open('myfile2.txt', 'w', encoding='utf-8') as f:  # открывает один файл для записи, другой - для чтения
    with open('myfile1.txt', 'r', encoding='utf-8') as g:
        text = g.read().split()
    line = ''
    for i in text:
        line += str(i) + ' '
    f.write(f'Исходные данные: {line}\n')  # вывод ответа(исходные данные)
    f.write(f'Кол-во элементов: {str(len(text))}\n')  # вывод ответа(кол-во элементов)
    f.write(f'Индекс максимального числа: {str(text.index(max(text)))}\n')  # вывод ответа(индекс максимального числа)
    f.write(f'Умножение средней трети элементов: {math.prod(m)}')  # вывод ответа(умножение элементов средней трети)
