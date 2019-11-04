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


runner()
runner(is_palindrome)
runner(is_palindrome, square)

the_most_meets_word()
