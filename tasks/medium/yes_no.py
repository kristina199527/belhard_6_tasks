"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

a = [1, 2, 3, 2, 5, 6, 1, 7]


def yes_or_no(n):
    n1 = len(n)
    for i in range(n1):
        if n[i] in n[0:i]:
            print('Yes')
        else:
            print("No")


print(yes_or_no(a))
