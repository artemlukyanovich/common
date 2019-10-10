import math

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

