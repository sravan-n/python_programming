"""
Functions for working with datetime objects.
"""
import datetime


def christmas_day(year):
    """
    Returns ISO day of the week for Christmas in the given year.
    
    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday 
    and the appropriate number for any day in-between. 
    
    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """

    d = datetime.date(year, 12, 25)

    return d.isoweekday()


def iso_str(d,t):
    """
    Returns the ISO formatted string of date and time together.
    
    When combining, the time must be accurate to the microsecond.
    
    Parameter d: The month-day-year
    Precondition: d is a date object
    
    Parameter t: The time of day
    Precondition: t is a time object
    """

    iso = datetime.datetime(d.year, d.month, d.day, t.hour, t.minute, t.second, t.microsecond).isoformat()

    return iso


def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.
    
    Values d1 and d2 can EITHER be date objects or datetime objects.
    If a date object, assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    type_d1 = type(d1)
    type_d2 = type(d2)

    if type_d1 == type_d2:
        return d1 < d2
    else:
        # Convert date to datetime if needed
        if type_d1 == datetime.date:
            d1 = datetime.datetime(d1.year, d1.month, d1.day)
        
        if type_d2 == datetime.date:
            d2 = datetime.datetime(d2.year, d2.month, d2.day)
        
        return d1 < d2
