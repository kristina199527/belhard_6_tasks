"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""
num = 123


def sum_of_numbers(n):
    if n == 0:
        return 0

    return (n % 10 + sum_of_numbers(int(n / 10)))


print(sum_of_numbers(num))
