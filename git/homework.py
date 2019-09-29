"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return (first == second)

# print(is_two_object_has_same_value(1, 1))

def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return(type(first)==type(second))

# print(is_two_objects_has_same_type("asfas", "10"))


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return(first is second)

# print(is_two_objects_is_the_same_objects(1, 1))


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if type(first_value) == int and type(second_value) == int:
        return (first_value * second_value)
    else:
        raise ValueError

# print(multiple_ints(1, 2))


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    if type(int(first_value)) == int and type(int(second_value)) == int:
        return(int(first_value)*int(second_value))
    else:
        raise ValueError

# print(multiple_ints_with_conversion(1, 2))

def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    return(word in text)

# print(is_word_in_text("asa","baaaaasd"))

def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    list = []
    i = 0
    while i <= 12:
        if i == 6 or i == 7:
            i +=1
            continue
        list.append(i)
        i += 1
    return(list)

# print(some_loop_exercise())

def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    return([x for x in data if x >= 0])

# print(remove_from_list_all_negative_numbers([1, 5, -7, 8, -1]))

def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    import string
    letters = {}
    i = 1
    while i <= len(string.ascii_lowercase):
        letters.setdefault(i, string.ascii_lowercase[i-1])
        i += 1
    return(letters)

# print(alphabet())

def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    new_list = []
    for n in data:
        if len(new_list) == 0:
            new_list.append(n)
        else:
            for i, n2 in enumerate(new_list):
                if n < n2:
                    new_list.insert(i, n)
                    break
                else:
                    if i == len(new_list)-1:
                        new_list.append(n)
                        break
    return(new_list)

# print(simple_sort([2, 9, 6, 7, 3, 2, 1, 10, 10]))