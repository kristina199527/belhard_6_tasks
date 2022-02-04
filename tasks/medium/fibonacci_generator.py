"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""
num = 0


def fibonacci(n):
    if n == 0:
        raise ValueError('Введите значение больше 1')
    elif n == 1 or n == 2:
        return = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2))


print(fibonacci(num))
