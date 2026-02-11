"""
Module with mutable functions on lists.

All of these functions modify their list arguments.

"""


def clamp(alist,min,max):
    """
    Modifies alist so that every element is between min and max.
    
    Any number in the list less than min is replaced with min.  Any number
    in the tuple greater than max is replaced with max. Any number between
    min and max is left unchanged.
    
    Examples:
        If a = [-1, 1, 3, 5], clamp(a,0,4) changes a to [0,1,3,4]
        If a = [-1, 1, 3, 5], clamp(a,-2,8) changes a to [-1,1,3,5]
        If a = [-1, 1, 3, 5], clamp(a,-2,-1) changes a to [-1,-1,-1,-1]
        If a = [], clamp(a,0,4) returns []
    
    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)
    
    Parameter min: the minimum value for the list
    Precondition: min <= max is a number
    
    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    
    size = len(alist)

    for pos in range(size):
        if alist[pos] < min:
            alist[pos] = min
        elif alist[pos] > max:
            alist[pos] = max


def removeall(alist,n):
    """
    Removes all instances of n from alist
    
    Examples:
        If a = [1,2,2,3,1], removeall(a,1) changes a to [2,2,3]
        If a = [1,2,2,3,1], removeall(a,2) changes a to [1,3,1]
        If a = [1,2,2,3,1], removeall(a,4) changes a to [1,2,2,3,1]
        If a = [1,1,1], removeall(a,1) changes a to []
        If a = [], removeall(a,1) changes a to []
    
    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)
    
    Parameter n: the number to remove
    Precondition: n is a number
    """

    while n in alist:
        alist.remove(n)


"""
Module with non-mutable functions on lists.

All of these functions make use of accumulators that make new lists.

"""

def clamp(alist,min,max):
    """
    Returns a copy of alist where every element is between min and max.
    
    Any number in the list less than min is replaced with min.  Any number
    in the tuple greater than max is replaced with max. Any number between
    min and max is left unchanged.
    
    Examples:
        clamp([-1, 1, 3, 5],0,4) returns [0,1,3,4]
        clamp([-1, 1, 3, 5],-2,8) returns [-1,1,3,5]
        clamp([-1, 1, 3, 5],-2,-1) returns [-1,-1,-1,-1]
        clamp([],0,4) returns []
    
    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)
    
    Parameter min: the minimum value for the list
    Precondition: min <= max is a number
    
    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """

    copy = []

    for val in alist:
        if val < min:
            copy.append(min)
        elif val > max:
            copy.append(max)
        else:
            copy.append(val)

    return copy



def removeall(alist,n):
    """
    Returns a copy of alist, removing all instances of n
    
    Examples:
        removeall([1,2,2,3,1],1) returns [2,2,3]
        removeall([1,2,2,3,1],2) returns [1,3,1]
        removeall([1,2,2,3,1],4) returns [1,2,2,3,1]
        removeall([1,1,1],1) returns []
        removeall([],1) returns []
    
    Parameter alist: the list to copy
    Precondition: alist is a list of numbers (float or int)
    
    Parameter n: the number to remove
    Precondition: n is a number
    """
    
    copy = []

    for val in alist:
        if val != n:
            copy.append(val)

    return copy


"""
Module demonstrating mutable list functions.

Neither of these functions should use for-lopps.  Instead, they should use 
list methods.

"""


def put_in(alist,value):
    """
    Adds a value to a sorted list, resorting as necessary.
    
    Examples:
        If a = [0,2,3,4], put_in(a,1) makes a = [0,1,2,3,4]
        If a = [0,2,3,4], put_in(a,2) makes a = [0,2,2,3,4]
        If a = [], put_in(a,3) makes a = [3]
    
    Parameter a: The list to append to
    Precondition: a is a sorted list of a single type of element
    
    Parameter value: The value to append
    Precondition: value has the same type as the elements of a
    """
    
    alist.append(value)
    alist.sort()


def rotate(alist):
    """
    Rotates the contents of alist one element to the right.
    
    Rotating a list to the right pushes all elements to the right, and makes
    the previously last element the new first element.
    
    Examples:
        If a = [0,2,3,4], rotate(a) makes a = [4,0,2,3]
        If a = [1], rotate(a) makes a = [1]
    
    Parameter a: The list to rotate
    Precondition: a non-empty list
    """
    len_list = len(alist)
    temp = alist[len_list-1]
    alist.pop()
    alist.insert(0, temp)


