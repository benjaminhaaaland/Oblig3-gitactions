# Software Engineering and Testing - Mandatory Assignment 2 "
from main import isLeapYear

""" 
***
* Tests to see if certain years are leap year or not.
***
"""

def test_year_divisible_by_four_but_not_one_hundred():
    assert isLeapYear(2000) == 1
    assert isLeapYear(2004) == 1
    assert isLeapYear(2024) == 1

def test_year_divisible_by_four_hundred():
    assert isLeapYear(1600) == 1
    assert isLeapYear(2000) == 1
    assert isLeapYear(2400) == 1

def test_year_not_divisible_by_four():
    assert isLeapYear(2001) == 0
    assert isLeapYear(2003) == 0
    assert isLeapYear(2006) == 0

def test_year_divisible_by_hundred_and_not_four_hundred():
    assert isLeapYear(2001) == 0
    assert isLeapYear(2003) == 0
    assert isLeapYear(2006) == 0














