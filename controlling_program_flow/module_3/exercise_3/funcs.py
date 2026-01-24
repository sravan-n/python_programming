"""
Module with range-based for-loop functions.

Author: Sravan Kumar Nuthalapati
Date: 12/01/2025
"""

def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1
    
    0! is 1.  Factorial is undefined for integers < 0.
    
    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120
    
    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    
    # define result accumulator with 1
    result = 1
    # if n is 0 return accumulator with 1
    if n == 0:
        return result
    # else for each element x in given range
    else:
        for x in range(n):
            # multiply  x+1 with accumulator since range starts with 0
            result = result * (x+1)
    # return result
    return result


def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)
    
    Note that this tuple is the reverse of tuple(range(a,b))
    
    Parameter a: the "start" of the range
    Precondition: a is an int <= b
    
    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    
    result = ()
    for x in range(a,b):
        if x >= a:
            result = (x,) + result
    return result
