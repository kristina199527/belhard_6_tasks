"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
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


def incr_students(some_dict):
    for i in some_dict.values():
        i = i + 1
    return incr_students


incr_students_1 = incr_students(school_data)
print(incr_students_1)


def decr_students(some_dict):

    for i in some_dict.values():
        if i > 1:
            i = i + 1
        else:
            i == i
    return decr_students



print(decr_students(school_data))

