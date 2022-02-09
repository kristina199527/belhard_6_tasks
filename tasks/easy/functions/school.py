"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def calc_students(some_list):
    result = sum(some_list.values())
    return result


def incr_students(some_list):
    for i, j in some_list.items():
        some_list[i] = j + 1
    return some_list


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students_2(some_list):
    for i, j in some_list.items():
        some_list[i] = j - 1
    return some_list


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def add_class(some_list):
    some_list['3b'] = 0
    return some_list


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def remove_class(some_list):
    some_list = some_list.pop('1a')
    return some_list


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}
