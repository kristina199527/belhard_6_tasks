"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""
num = 5


def triangular_sequence(n):
    for i in range(1, n + 1):
        print(str(i) * i)
        return triangular_sequence(n-1)


print(triangular_sequence(num))