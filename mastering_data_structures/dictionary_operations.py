"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: Sravan Kumar Nuthalapati
Date: 01/30/2026
"""


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    total_students = len(adict)
    total_marks = 0
    avg_grade = 0
    
    for key in adict:
        total_marks = total_marks + adict[key]

    if total_students > 0:
        avg_grade = total_marks / total_students 
    
    return avg_grade


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.
    
    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a 
    new dictionary with netids for keys and letter grades (strings) for values.
    
    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60 
    is an F.
    
    Examples:  
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """

    grades = dict([])

    for key in adict:
          if adict[key] >= 90:
            grades[key] = 'A'
          elif adict[key] >= 80:
            grades[key] = 'B'
          elif adict[key] >= 70:
            grades[key] = 'C'
          elif adict[key] >= 60:
            grades[key] = 'D'
          else:
            grades[key] = 'F'

    return grades


"""
Module to demonstrate functions on nested dictionaries.

This module uses the data in the file 'weather.json'.  This module does not need to
worry about reading and opening the file -- test.py does that.  However, you should 
look at that file to familiarize your self with the data format.

In that file weather is a dictionary whose keys are timestamps (year,month,day,hour,etc.) 
and whose values are weather reports.  For example, here is an example of a 
(small portion of) a weather dictionary:
    
    {
        "2017-04-21T08:00:00-04:00": {
            "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 13.9,
                "units": "C"
            },
            "sky": [
                {
                    "cover": "clouds",
                    "type": "broken",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704211056Z"
        },
        "2017-04-21T07:00:00-04:00": {
            "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 57.0,
                "units": "F"
            },
            "sky": [
                {
                    "type": "overcast",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704210956Z"
        }
        ...
    },
    
The contents of interest in this module is the nested "temperature" dictionary.  

IMPORTANT: Not all weather reports contain a temperature measurement.

Author: Sravan Kumar Nuthalapati
Date: 01/30/2026
"""


# Helper to use in function below
def to_celsius(x):
    """
    Returns x converted to celsius

    The value returned has type float.

    Parameter x: the temperature in fahrenheit
    Precondition: x is a number
    """
    return 5*(x-32)/9.0


# Implement this function
def reports_above_temp(weather,temp):
    """
    Returns the number of weather reports where temperature is above temp (in Celsius)
    
    The parameter weather contains a weather report dictionary.  This function loops
    through the weather reports and counts all reports for which
    (1) the report has a temperature measurement (not all reports do)
    (2) the measured temperature is properly above temp in Celsius
    
    A temperature measurement is itself a dictionary with two keys: 'value' and 'units'.
    For example:
        
        "temperature": {
            "value": 57.0,
            "units": "F"
        }
    
    The units are always either 'F' for fahrenheit or 'C' for celsius.  If the
    measurement is in fahrenheit, the value will need to be converted before it 
    can be compared to temp.
    
    Parameter weather: the weather dictionary
    Precondition: weather has the format described in the module introduction
    
    Parameter temp: the temperature in celsius
    Precondition: temp is a float
    """

    no_of_reports_above_temp = 0

    for reports in weather:
       if 'temperature' in weather[reports]:
          temp_from_report = weather[reports]['temperature']
          if temp_from_report['units'] == 'F':
             temp_in_c = to_celsius(temp_from_report['value'])
             if temp_in_c > temp:
                no_of_reports_above_temp = no_of_reports_above_temp + 1
          elif temp_from_report['units'] == 'C':
             if temp_from_report['value'] > temp:
                no_of_reports_above_temp = no_of_reports_above_temp + 1

    return no_of_reports_above_temp


def drop_below(adict,limit):
    """
    Deletes all students in the dictionary with grades below limit.
    
    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam.
    
    Examples: Suppose a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
        drop_below(a,60) changes a to {'abc3' : 90, 'jms45': 86}
        drop_below(a,90) changes a to {'abc3' : 90}
        drop_below(a,95) changes a to {}
        drop_below(a,50) leaves a unchanged as {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    
    Paramater limit: the cut-off boundary
    Precondition: limit is a number (int or float)
    """
    keys = list(adict.keys())

    for k in keys:
        if adict[k] < limit:
            del adict[k]


