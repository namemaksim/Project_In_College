# Дано целое число N (>1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 2 +...+K
# будет больше или равна N, и саму эту сумму.
def my_work4_2(self):  # создаю функцию, чтобы в дальнейшем ее автоматизировать
    n = input('Введите целое положительное число: ')
    k,c,p = 0, 2, 0
    while type(n) != int:  # проверка условий через созданный список
        try:
            n = int(n)
            while n >= k:  # решение самой задачи
                k += 1
                c = k - 1
                p += c
                print("Сумма чисел: ", p, "Наименьшее целое число: ", k)  # вывод ответа
            break
        except ValueError:
            print('Вы ввели не целые числа ', n, k)


while True:  # автоматизация функции
    print(my_work4_2(None))