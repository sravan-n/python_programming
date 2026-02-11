"""
Module with simple for-loop functions.

Author: Sravan Kumar Nuthalapti
Date: 12/01/2025
"""


def lesser(tup,value):
    """
    Returns the number of elements in tup strictly less than value
    
    Examples: 
        lesser((5, 9, 1, 7), 6) returns 2
        lesser((1, 2, 3), -1) returns 0
    
    Parameter tup: the tuple to check
    Precondition: tup is a non-empty tuple of ints
    
    Parameter value:  the value to compare to the tuple
    Precondition:  value is an int
    """
    # Define a variable for result with 0
    result = 0
    # if element in tuple less than value add 1 to result
    for x in tup:
        if x < value:
            result = result + 1
    # return reslt
    return result


def avg(tup):
    """
    Returns average of all of the elements in the tuple.
    
    Remember that the average of a tuple is the sum of all of the elements in the
    tuple divided by the number of elements in the tuple.
    
    Examples: 
        avg((1.0, 2.0, 3.0)) returns 2.0
        avg((1.0, 1.0, 3.0, 5.0)) returns 2.5
    
    Parameter tup: the tuple to check
    Precondition: tup is a tuple of numbers (int or float)
    """
    # define avg and sum variables with 0
    avg = 0
    sum = 0
    # compute length of tuple
    len_tup = len(tup)
    # add each number in tuple to sum
    for x in tup:
        sum = sum + x
    # compute avg with sum by length - to avoid by 0 exception add try except
    try:
        avg = sum / len_tup
    except:
        avg = 0.0
    # return result
    return avg
