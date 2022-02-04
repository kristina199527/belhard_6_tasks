"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci(n):
    if n < 0:
        raise ValueError('Значение должно быть больше 0')
    first = 1
    second = 1
    yield first
    yield second

    for _ in range(n - 2):
        first, second = second, first + second
        yield second


fibonacci_gen = fibonacci(12)
print(next(fibonacci_gen))




