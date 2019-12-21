try:
    num1 = 5
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("Попытка деления на 0")


def print_list_element(the_list, index):
    print(the_list[index])


try:
    print_list_element([1, 2, 3, 4, 5, ], 10)
except IndexError:
    print("Индекс превышает длину списка")