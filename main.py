"""""
Программа для поиска "счастливых" и "палиндромных" чисел.
"палиндромное" число -- число, где обе части числа зеркальны, читаются одинакого "732237" или "101"
"счастливое" число -- число, где сумма цифр в двух частях равны "654825" -> "654" "825", а если 
количество цифр в числе нечетно, то средняя цифра не учитывается в расчетах "3825625" -> "382" "625".
"""""


def get_parts(number_str):
    half_part_number = len(number_str) / 2
    front_part_number = number_str[:int(half_part_number)]

    if len(number_str) % 2 == 0:
        back_part_number = number_str[int(half_part_number):]
    else:
        back_part_number = number_str[(int(half_part_number) + 1):]

    front_part = []
    for i in front_part_number:
        front_part.append(int(i))

    back_part = []
    for i in back_part_number:
        back_part.append(int(i))

    return front_part, back_part


def get_revers(number_str):
    number_list = []
    number_reverse_list = []
    for i in number_str:
        number_list.append(int(i))
        number_reverse_list.insert(0, int(i))

    return number_list, number_reverse_list


def lucky_number(number):
    number_str = str(number)
    if len(number_str) >= 2:
        front_part, back_part = get_parts(number_str)
        number_list, number_reverse_list = get_revers(number_str)

        if number_list == number_reverse_list:
            print(f'Найдено "палиндромное" число: {number}')
        elif sum(front_part) == sum(back_part):
            print(f'Найдено "счастливое" число: {number}')


def start(count):
    for number in range(1, count):
        lucky_number(number=number)


if __name__ == '__main__':
    start(count=100000)
