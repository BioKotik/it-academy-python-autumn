"""Write a program that prints the numbers from 1 to 100,
but for multiples of three print “Fizz” instead of the number
and for multiples of five print “Buzz”. For numbers which are
multiples of both three and five, print “FizzBuzz”."""

for number in range(101):
    if number == 0:
        continue
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(str(number))

"""List"""
"""Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb',
'bc', 'bd']."""

lst1 = [a+b for a in "ab" for b in "bcd"]
print(lst1)

"""Use a slice on the above list to construct the list ['ab', 'ad', 'bc']."""

lst2 = lst1[::2]
print(lst2)

"""Use a list comprehension to construct the list ['1a', '2a', '3a', '4a']."""

lst3 = [str(a)+b for a in range(5) if a > 0 for b in "a"]
print(lst3)

"""Simultaneously remove the element '2a' from the above list and print it."""

print(lst3.pop(1))
print(lst3)

"""Copy the above list and add '2a' back into the list such that the
original is still missing it. """

lst4 = lst3[:]
lst4.append("2a")
print(lst4)

"""Tuple"""
"""Create the list ['a', 'b', 'c'], then create a tuple from that list."""

lst5 = ['a', 'b', 'c']
tpl1 = tuple(lst5)
print(tpl1)

"""Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
(Hint: the material needed to do this has been covered, but it's not entirely obvious)"""

tpl2 = list(lst5)
print(tpl2)

"""Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'. 
(That is, in one line of code)."""

for element in ('a', 2, 'gamma'):
    print(element)
tpl3 = (('a', 'b', 'c'), )
print(tpl3)
print(len(tpl3))
