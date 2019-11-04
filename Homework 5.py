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

"""Задача Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится."""

number = int(input('Введите количество стран'))
county_n_cities = {}
for i in range(number):
    country, *cities = input('Ввдеите страну и его города ').split()
    for city in cities:
        county_n_cities[city] = country

number = int(input('Введите количество городов, которые хотите вывести'))
list_city = []
for i in range(number):
    print('Введите город')
    list_city.append(input())
for city in list_city:
    print(county_n_cities.get(city))

"""Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно
как в первом списке,так и во втором."""

lst1 = [1, 2, 5, 7, 12]
lst2 = [3, 5, 1, 4, 10, 12, 15]

print(len(set(lst1) & set(lst2)))

"""Даны два списка чисел. Посчитайте, сколько чисел входит
только в один из этих списков."""

print(len(set(lst1) ^ set(lst2)))
