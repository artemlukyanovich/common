import math
import string


def fun1(a: list, b: list):
    """Take two lists, say for example these two:
    a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are
    common between the lists (without duplicates). """
    return list(set(a) & set(b))


def fun2(string: str):
    """Return the number of times that the letter “a”
    appears anywhere in the given string"""
    return string.count("a")


def fun3(n):
    """Write a Python program to check if a given positive
    integer is a power of three"""
    x = math.log(n, 3)
    return int(x) == x


def fun4(n: int):
    """Write a Python program to add the digits of a
    positive integer repeatedly until the result has a single digit."""
    while len(str(n)) > 1:
        n = sum(int(x) for x in str(n))
    return n


def fun5(l: list):
    """Write a Python program to push all zeros to the end of a list."""
    c = [x for x in l if x != 0]
    for i in range(l.count(0)):
        c.append(0)
    return c


def fun6(l: list):
    """Write a Python program to check a sequence of numbers is
    an arithmetic progression or not."""
    a = l[1] - l[0]
    for i in range(2, len(l)):
        if l[i] - l[i - 1] != a:
            return False
    else:
        return True


def fun7(l: list):
    """Write a Python program to find the number in a
    list that doesn't occur twice."""
    nums = []
    for i in l:
        if l.count(i) == 1:
            nums.append(i)
    return nums


def fun8(l: list):
    """Write a Python program to find a missing number from a list."""
    nums = []
    for i in range(l[0], l[len(l) - 1]):
        if i not in l:
            nums.append(i)
    return nums


def fun9(l: list):
    """Write a Python program to count the elements
    in a list until an element is a tuple."""
    n = 0
    for i in l:
        if type(i) == tuple:
            break
        n += 1
    return n


def fun10(s: str):
    """Write a program that will take the str parameter being
    passed and return the string in reversed order."""
    return s[::-1]


def fun11(n: int):
    """Write a program that will take the num parameter being
    passed and return the number of hours and minutes the parameter
    converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon."""
    return str(n // 60) + ":" + str(n % 60)


def fun12(s: str):
    """Write a program that will take the parameter being passed and
    return the largest word in the string. If there are two or more words
    that are the same length, return the first word from the string with
    that length. Ignore punctuation"""
    s2 = "".join(l for l in s if l not in string.punctuation)
    return max(s2.split(), key=len)


def fun13():
    s = input("Print some words: ")
    l = s.split()
    l.reverse()
    return " ".join(l)


def fun14():
    # n = list(range(int(input("Print the number: "))+1))
    # fib = [x for x in range(n)]

    n = list(range(2, int(input("Print the number: ")) + 1))
    base = [0, 1]
    for i in n:
        base.append(base[i - 1] + base[i - 2])
    return base[1:]


def fun15(l: list):
    """Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes
    a new list that has only the even elements of this list in it."""
    return [x for x in l if x % 2 == 0]


def fun16(n):
    """Write a program that will add up all the numbers from
    1 to input number. For example: if the input is 4 then your program
    should return 10 because 1 + 2 + 3 + 4 = 10"""
    if n >= 0:
        return sum(range(n + 1))
    else:
        return sum(range(n, 0))


def fun17(n):
    """Write a program that will take the parameter being passed
    and return the factorial of it."""
    if n == 1:
        return 1
    else:
        return n * fun17(n - 1)


def fun18(s: str):
    """Write a program that will take the str parameter being passed
    and modify it using the following algorithm. Replace every letter
    in the string with the letter following it in the alphabet
    (ie. cbecomes d, zbecomes a). Then capitalize every vowel in this
    new string (a, e, i, o, u) and finally return this modified string."""
    vowels = ["a", "e", "i", "o", "u"]
    s2 = [string.ascii_lowercase[str(string.ascii_lowercase).index(x) + 1] if x != "z" else "a" for x in s]
    res = "".join([x.upper() if x in vowels else x for x in s2])
    return res


def fun19(s: str):
    """Write a program that will take the str string parameter being
    passed and return the string with the letters in alphabetical order
    (ie. hello becomes ehllo). Assume numbers and punctuation symbols
    will not be included in the string."""
    return "".join(sorted(s))


def fun20(a, b):
    """Write a program that will take both parameters being passed and
    return the true if num2 is greater than num1, otherwise return the false.
    If the parameter values are equal to each other then return the string -1"""
    if a == b:
        return "-1"
    else:
        return a > b