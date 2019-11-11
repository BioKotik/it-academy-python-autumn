def fibonacci():
    count_numbers = int(input('count = '))
    buffer1 = 1
    buffer2 = 1
    for numbers in range(count_numbers - 2):
        buffer1 += buffer2
        print('buffer1 = ' + str(buffer1))
        buffer2 = buffer1 - buffer2
    result = buffer1
    print(result)


def is_palindrome():
    palindrome = input('palindrome = ')
    buffer = palindrome
    result = 0
    while palindrome:
        decimal_part = int(palindrome) % 10
        palindrome = int(palindrome) // 10
        result = result * 10 + int(decimal_part)
    print('result = ' + str(result))
    if int(result) == int(buffer):
        print('palindrome')
    else:
        print('not palindrome')


def square():
    n = int(input("Введите кол-во чисел "))
    dct = {(a, a ** 2) for a in range(n) if a > 0}
    print(dct)


def runner(*args):
    if args:
        for func in args:
            func()
    else:
        fibonacci()
        is_palindrome()
        square()


def result_of_function(func):
    def wrapper():
        result = func()
        with open("result.txt", "a") as file:
            file.write(str(result) + "\n")
    return wrapper


@result_of_function
def the_most_meets_word():
    string = input("Введите строку - ")
    dict_of_words = dict()

    marks = ",.!?:;()[]{}#$%^&*+-/|><="
    for mark in marks:
        string = string.replace(mark, ' ')
    string = string.split()

    for item in string:
        dict_of_words[item] = dict_of_words.get(item, 0) + 1
    print(dict_of_words)

    list_of_max = []
    maxvalue = int(max(dict_of_words.values()))
    for key in dict_of_words.keys():
        if dict_of_words[key] == maxvalue:
            list_of_max.append(key)
    list_of_max = sorted(list_of_max)
    print(list_of_max[0])
    return list_of_max[0]


def union_numbers(lst_of_numbers):
    result = list()
    result.append(lst_of_numbers[0])
    range_str = ''
    for i in lst_of_numbers[1:]:
        if i - result[-1] == 1:
            if len(result) == 1:
                result.append(i)
            elif len(result) == 2:
                result[-1] = i
        else:
            range_str += '-'.join(map(str, result)) + ', '
            result.clear()
            result.append(i)
    range_str += '-'.join(map(str, result))
    print(range_str)


"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. runner() – все фукнции вызываются по очереди
runner(‘gen_numbers’) – вызывается только функцию gen_numbers. 
runner(‘func’, ‘func1’...) - вызывает все переданные функции 
"""
runner()
runner(is_palindrome)
runner(is_palindrome, square)

"""Создайте декоратор, который хранит в файле результаты вызовы
функций (за все время, не только текущий запуск программы)"""
the_most_meets_word()

"""Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”"""
union_numbers([1, 2, 3, 4, 6, 7, 8, 12, 14, 15, 17, 20])
