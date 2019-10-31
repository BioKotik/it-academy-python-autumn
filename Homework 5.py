"""Define a dict comprehension which returns a dictionary where the keys are
numbers between 1 and n (both included) and the values are square of keys.
Define a code which count and return the numbers of each character in
a count_me_string argument."""

n = int(input("Введите кол-во чисел "))
dct = {(a, a**2) for a in range(n) if a > 0}
print(dct)

"""Задача. Дан текст (строк может быть много, разделенных \n).
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в
лексикографическом порядке."""

string = input("Введите строку - ")
dct = dict()
for item in string:
    dct[item] = dct.get(item, 0) + 1
print(dct)
maxvalue = int(max(dct.values()))
for item in dct.values():
    if item == maxvalue:
        print(item)

"""Задача Дан список стран и городов каждой страны. 
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится."""

number = int(input('Введите кол-во стран'))
dct1 = dict()
for towns in range(number):
    print("Введите страну и города")
    string = input().split(" ")
    key = string[0]
    string.remove(string[0])
    dct2 = {key: string}
    dct1.update(dct2)

number_cities = int(input('Введите кол-во городов'))
city = []
print('Введите города, которые хотите вывести')
for i in range(number_cities):
    city.append(input())
for city in city:
    print(dct1.get(city))

"""Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно
как в первом списке,так и во втором."""

lst1 = [1, 2, 5, 7, 12]
lst2 = [3, 5, 1, 4, 10, 12, 15]
lst3 = set(lst1) & set(lst2)
print(lst3)

"""Даны два списка чисел. Посчитайте, сколько чисел входит 
только в один из этих списков."""

lst4 = set(lst1) - set(lst2)
print(lst4)
