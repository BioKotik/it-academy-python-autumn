"""string = input("Введите строку - ")
dct = dict()
for item in string:
    dct[item] = dct.get(item, 0) + 1
print(dct)
maxvalue = int(max(dct.values()))
for item in dct.values():
    if item == maxvalue:
        print(dct.items())"""

n = int(input("Введите кол-во стран"))
dct1 = dict()
for towns in range(n):
    print("Введите страну и города")
    string = input().split(" ")
    key = string[0]
    string.remove(string[0])
    dct2 = {key: string}
    dct1.update(dct2)
m = int(input("Введите кол-во городов, которые хотите ввести"))
for towns in range(m):
    print("Введите город, страну которого хотите вывести")
    town = input()
