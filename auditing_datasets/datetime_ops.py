"""
Functions for working with datetime objects / computing time elapsed / parsing time values.
Functions for parsing time values and determining daylight hours.
"""
import datetime
from dateutil.parser import parse
import pytz


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


def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.
    
    If d1 is after d2, or d2 is less than a week after d1, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.  If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The second event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    
    type_d1 = type(d1)
    type_d2 = type(d2)

    if type_d1 == datetime.date:
        d1 = datetime.datetime(d1.year, d1.month, d1.day)

    if type_d2 == datetime.date:
        d2 = datetime.datetime(d2.year, d2.month, d2.day)

    td = d2 - d1

    if td.days >= 7:
        return True
    else:
        return False


def str_to_time(timestamp):
    """
    Returns the datetime object for the given timestamp (or None if the stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to convert the
    timestamp to a datetime object.  If it is not a valid date (so the parser crashes), 
    this function should return None.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    """

    try:
        return parse(timestamp)
    except:
        return None


def sunset(date,daycycle):
    """
    Returns the sunset datetime (day and time) for the given date
    
    This function looks up the sunset from the given daycycle dictionary. If the
    daycycle dictionary is missing the necessary information, this function 
    returns the value None.
    
    A daycycle dictionary has keys for several years (as int).  The value for each year
    is also a dictionary, taking strings of the form 'mm-dd'.  The value for that key 
    is a THIRD dictionary, with two keys "sunrise" and "sunset".  The value for each of 
    those two keys is a string in 24-hour time format.
    
    For example, here is what part of a daycycle dictionary might look like:
        
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    Parameter date: The date to check
    Precondition: date is a date object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    
    year_str = str(date.year)
    date_str = date.strftime('%m-%d')

    try:
        sunset = daycycle[year_str][date_str]['sunset']
        sunset_iso = date.strftime('%Y-%m-%d')+'T'+sunset
        return str_to_time(sunset_iso)
    except:
        return None


def str_to_time_2(timestamp,tzsource=None):
    """
    Returns the datetime object for the given timestamp (or None if timestamp is 
    invalid).
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a time zone, then it should keep that time zone even if
    the value for tzsource is not None.  Otherwise, if timestamp has no time zone 
    and tzsource is not None, then this function will use tzsource to assign 
    a time zone to the new datetime object.
    
    The value for tzsource can be None, a string, or a datetime object.  If it 
    is a string, it will be the name of a time zone, and it should localize the 
    timestamp.  If it is another datetime, then the datetime object created from 
    timestamp should get the same time zone as tzsource.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tzsource: The time zone to use (OPTIONAL)
    Precondition: tzsource is either None, a string naming a valid time zone,
    or a datetime object.
    """
    
    # Try to parse the timestamp string
    try:
        ts = parse(timestamp)
    except:
        # Parsing failed, return None
        return None
    
    # Check if the parsed timestamp already has timezone information
    if ts.tzinfo == None:
        # Timestamp has no timezone, check if we need to add one
        if tzsource != None:
            # If tzsource is a string (timezone name like 'America/Chicago')
            if type(tzsource) == str:
                tz = pytz.timezone(tzsource)
                return tz.localize(ts)
            # If tzsource is a datetime object, extract and apply its timezone
            else:
                return ts.replace(tzinfo=tzsource.tzinfo)
        else:
            # No tzsource provided, return naive datetime
            return ts
    else:
        # Timestamp already has timezone, keep it unchanged
        return ts


def daytime(time,daycycle):
    """
    Returns True if the time takes place during the day, False otherwise (and 
    returns None if a key does not exist in the dictionary).
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dictionary.
    
    A daycycle dictionary has keys for several years (as strings).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects using data from the daycycle dictionary.  Also, if the time
    parameter does not have a timezone, we assume that it is in the same timezone 
    as the daycycle dictionary.
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    
    try:
        # Extract year and date components from the time parameter
        year = str(time.year)
        date = time.strftime('%m-%d')
        
        # Get the timezone from the daycycle dictionary
        timezone = daycycle['timezone']

        # Build ISO format strings for sunset and sunrise times
        sunset_iso =  year + '-' + date + 'T' + daycycle[year][date]['sunset']
        sunrise_iso =  year + '-' + date + 'T' + daycycle[year][date]['sunrise']
        
        # Convert to datetime objects with timezone information
        sunset = str_to_time_2(sunset_iso, timezone)
        sunrise = str_to_time_2(sunrise_iso, timezone)
        
    except:
        # Return None if any key is missing from the dictionary
        return None
    
    # If time parameter has no timezone, add the daycycle timezone to it
    if time.tzinfo == None:
        tz = pytz.timezone(timezone)
        time = tz.localize(time)
    
    # Check if time is between sunrise and sunset
    if sunrise < time and time < sunset:
        return True
    else:
        return False

    