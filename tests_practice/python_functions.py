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
        if l[i] - l[i-1] != a:
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
    for i in range(l[0], l[len(l)-1]):
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
    return str(n//60) + ":" + str(n%60)

def fun12(s: str):
    """Write a program that will take the parameter being passed and
    return the largest word in the string. If there are two or more words
    that are the same length, return the first word from the string with
    that length. Ignore punctuation"""
    s2 = "".join(l for l in s if l not in string.punctuation)
    return max(s2.split(), key=len)

