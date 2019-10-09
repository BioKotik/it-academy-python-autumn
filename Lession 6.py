"""n = int(input("n = "))
dct = {str(item**2): item for item in range(n)}

string = input("string = ")
count = 0
for letter in string:
    if "a" <= letter.lower() <= "z":
        count += 1
print("Кол-во букв в строке = " + str(count))"""

"""numbers = input("numbers = ")
numbers2 = list(numbers.split())
counts = list()
for item in numbers2:
    counts.append(numbers2.count(item))
maxCount = max(counts)
for item in numbers2:
    if maxCount == numbers2.count(item):
        print("Самый часто встречающийся элемент списка - " + str(item))
        break"""

"""numbers = input("numbers = ")
numbers = numbers.split()
dct = dict()
for item in numbers:
    dct[item] = dct.get(item, 0) + 1
print(dct)"""

