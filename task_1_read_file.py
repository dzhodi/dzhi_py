"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""
import os
import pytest

from my_module import read_magic_number


def test_read_magic_number():
    """
    This function tests the read_magic_number function with positive and negative test cases.
    """
    # Create a temporary file with a valid number
    with open('test_file.txt', 'w') as f:
        f.write('2')
    # Test with a valid number within the interval
    assert read_magic_number('test_file.txt') == True
    # Create a temporary file with an invalid number
    with open('test_file.txt', 'w') as f:
        f.write('4')
    # Test with an invalid number outside the interval
    assert read_magic_number('test_file.txt') == False
    # Create a temporary file with a non-numeric value
    with open('test_file.txt', 'w') as f:
        f.write('abc')
    # Test with a non-numeric value
    with pytest.raises(ValueError):
        read_magic_number('test_file.txt')
    # Test with a non-existent file
    with pytest.raises(ValueError):
        read_magic_number('nonexistent_file.txt')
    # Remove the temporary file
    os.remove('test_file.txt')