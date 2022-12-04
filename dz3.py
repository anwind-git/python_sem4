# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import Random, randint

number = int(input("Сколько элементов будет в списке?: "))

list1 = []
list2 = []
list3 = []
list4 = []

for i in range(number):
    list1.append(randint(1, 20))

for j in list1:
    reset = False
    for x in list3:
        if x == j:
            reset = True
            list2.append(j)
            break
    if not reset:
        list3.append(j)

for d in list3:
    reset = False
    for k in list2:
        if k == d:
            reset = True
            list2.append(d)
            break
    if not reset:
        list4.append(d)

print(f"Исходный список: {list1}")

print(f"Список неповторяющихся элементов: {list3}")

print(f"Список уникальных элементов: {list4}")