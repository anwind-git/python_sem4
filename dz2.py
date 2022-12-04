# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число N: '))
lists = []
N = number
if number > 1:
    reset = True
    while reset:
        reset = False
        for i in range(2, number + 1):
            if number % i == 0:
                lists.append(i)
                number = int(number / i)
                reset = True
                break

if N > 1 and lists[0] != N:
    print(f'Cписок простых множителей числа {N} - {lists}')
elif N > 1 and number == 1:
    print(f'{N} простое число')
else:
    print(f'Введенное число меньше 2')