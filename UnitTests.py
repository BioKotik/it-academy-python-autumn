import unittest


def is_palindrome(palindrome):
    buffer = palindrome
    result = 0
    while palindrome:
        decimal_part = int(palindrome) % 10
        palindrome = int(palindrome) // 10
        result = result * 10 + int(decimal_part)
    print('result = ' + str(result))
    if int(result) == int(buffer):
        return True
    else:
        return False


def is_simple(number):
    count = 0
    for i in range(int(number)):
        if i and int(number) % int(i) == 0:
            count += 1
    if int(count) > 2:
        return False
    else:
        return True


def fibonacci(count):
    buffer1 = 1
    buffer2 = 1
    for numbers in range(count - 2):
        buffer1 += buffer2
        print('buffer1 = ' + str(buffer1))
        buffer2 = buffer1 - buffer2
    result = buffer1
    return result


class TestSimpleNumber(unittest.TestCase):

    def test_positive(self):
        result = is_simple(7)
        self.assertEqual(result, True)

    def test_negative(self):
        result = is_simple(15)
        self.assertEqual(result, True)


class TestFibonacci(unittest.TestCase):

    def test_positive(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_negative(self):
        result = fibonacci(5)
        self.assertEqual(result, 20)


class TestPalindrome(unittest.TestCase):

    def test_positive(self):
        result = is_palindrome(727)
        self.assertEqual(result, True)

    def test_negative(self):
        result = is_palindrome(522)
        self.assertEqual(result, True)
