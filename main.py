# Software Engineering and Testing - Mandatory Assignment 2 "
"""

*****
A year is a leap year if the following conditions are satisfied:

The year is multiple of 400.
The year is multiple of 4 and not multiple of 100.

A Year is not a leap year if the following conditions are satisfied:

The year is not divisible by 4
The year is divisible by 100 but not 400.

*****

"""

def isLeapYear(year_input: int):
    if year_input % 4 == 0 and 100 != 0:
        print("Critera1 -Year is Leap year!")
        return True

    if year_input %  400 == 0:
        print("Criteria2 - Year is leap year!")
        return True

    elif year_input % 4 != 0:
        print ("Critera 3 - Year is not leap year!")
        return False

    if year_input % 100 == 0 and 400 != 0:
        print ("Criteria4 - Year is not a leap year!")
        return false

isLeapYear(2100)
