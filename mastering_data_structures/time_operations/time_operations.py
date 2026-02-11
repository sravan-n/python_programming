"""
Module demonstrating how to write functions with objects.

This module contains two versions of the same function.  One version returns a new
value, while other modifies one of the arguments to contain the new value.

"""
import clock


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object
    
    DO NOT ALTER time1 or time2, even though they are mutable
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    
    mins = time1.minutes + time2.minutes
    hrs = time1.hours + time2.hours + mins // 60

    return clock.Time(hrs, mins % 60)



def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2
    
    DO NOT RETURN a new time object.  Modify the object time1 instead.
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    mins = time1.minutes + time2.minutes
    hrs = time1.hours + time2.hours + mins // 60

    time1.hours = hrs
    time1.minutes = mins % 60
