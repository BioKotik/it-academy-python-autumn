simple_number = input('simple_number = ')
count = 0
for i in range(int(simple_number)):
    if i and int(simple_number) % int(i) == 0:
        count += 1
if int(count) > 2:
    print('not simple')
else:
    print('simple')

palindrome = input('palindrome = ')
buffer = palindrome
result = 0
while palindrome:
    decimal_part = int(palindrome) % 10
    palindrome = int(palindrome) // 10
    result = result * 10 + int(decimal_part)
#result = result // 10
print('result = ' + str(result))
if int(result) == int(buffer):
    print('palindrome')
else:
    print('not palindrome')

count_numbers = int(input('count = '))
buffer1 = 1
buffer2 = 1
for numbers in range(count_numbers - 2):
    buffer1 += buffer2
    print('buffer1 = ' + str(buffer1))
    buffer2 = buffer1 - buffer2
result = buffer1
print(result)

money_int = int(input('money_int = '))
money_cent = int(input('money_change = '))
count_product = int(input('count_product = '))
money_int *= count_product
money_cent *= count_product
while money_cent >= 100:
    money_cent -= 100
    money_int += 1
print('Общая цена ' + str(money_int) + ' рублей ' + str(money_cent) + ' копеек')
