"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""

num = 8


def check_number(n):
    n1 = n / 2
    if n1 == 2 or n1 == 1 or n == 1:
        return True
    elif n > 2:
        return(check_number(n / 2))
    else:
        return False


print(check_number(num))

