def method(a, b):
    return a+b


def method2(a, b=0, *args, c, d=1, **kwargs):
    print(a, b, args, c, d, kwargs)


def method3(a, *, c):
    print(a, c)


def method4(a, b, *, c, d):
    print(a, b, c, d)

"""print(str(method(1, 2.55)))

method2(1, 2, 3, c=5, e=7)
#method2(1, 2, 3, b=8, c=5, e=7)
#method2(c=1, 1, 2, 3)

#method3(1, 2)
method3(3, c=0)"""

"""pos_arg = [1, 2]
pos_tuple = (1, 2, 3, 4)
named_dict = {'c': 5, 'd': 7, 'f': 8}

method4(*pos_arg, **named_dict)
#method4(*pos_tuple, **named_dict)"""


def fun_func(a):
    print(a)


def strange_func():
    print('strange')


#fun_func(strange_func)
#fun_func(strange_func())


def sum_of_number(a):
    c = 0
    while a:
        b = a % 10
        c += b
        a //= 10
    return c


#d = sum_of_number(135)
#print(d)

numbers = "321432532"
numbers = " ".join(numbers)
lst = numbers.split()
sum = 0
for item in lst:
    sum += int(item)
print(sum)