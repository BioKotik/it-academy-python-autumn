"""Найти самое длинное слово в введенном предложении.
 Учтите что в предложении есть знаки препинания."""

string = input('string = ')
string = string.strip()
words = string.split(' ')
for word in range(len(words)):
    words[word] = words[word].strip(',.!?')
word_w_max_len = words[0]
for word in range(len(words)):
    if len(str(word_w_max_len)) < len(words[word]):
        word_w_max_len = words[word]
print('Слово с максимальной длиной = ' + '"' + str(word_w_max_len) + '"')

"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Считывать только английские буквы."""

uppers = 0
lowers = 0
string = input('string = ')
string = string.strip()
for letter in range(len(string)):
    if string[letter].isupper():
        uppers += 1
    elif string[letter].islower():
        lowers += 1
print("Кол-во символов в верхнем регистре = " + str(uppers))
print("Кол-во символов в нижнем регистре = " + str(lowers))
