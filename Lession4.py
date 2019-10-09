"""string = input('string = ')
string = string.split()
lst = [element for element in string]
num = [element for element in lst if lst.count(element) == 1]
print(num)
for element in lst:
    if lst.count(element) == 1:
        print(element)"""

x = 1
while x:
    a = int(input('a = '))
    b = int(input('b = '))
    lst = [1, 2, 3, 4, 5, 6, 7, ]
    sub = -(a - b)
    print(sub)
    c = len(lst) // 2
    if a == b:
        print('Draw')
    elif 0 < sub <= c:
        print('a WIN!')
    else:
        print('b WIN')
