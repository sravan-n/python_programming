"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Sravan Kumar Nuthalapati
Date:   10/28/2025
"""

import introcs

APIKEY = 'sK7fFU3F8eGfcJA9679KDrnbcpmpcASn3CpLfRF2fTYe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, repr(s) + ' is not a string'
    assert introcs.count_str(s, ' ') >= 1, repr(s) + ' has no space in it'

    # Find the index of the first space in the string
    pos = introcs.find_str(s, ' ')
    # Compute the substring from the start to first space
    result = s[:pos]
    # Return the result
    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, repr(s) + ' is not a string'
    assert introcs.count_str(s, ' ') >= 1, repr(s) + ' has no space in it'

    # Find the index of the first space in the string
    pos = introcs.find_str(s, ' ')
    # Compute the substring after the first space
    result = s[pos+1:]
    # Return the result
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """

    assert type(s) == str, repr(s) + ' is not a string'
    assert introcs.count_str(s, '"') >= 2, repr(s) + 'should have 2 double quotes inside'

    # Find postion of first double quote
    pos1 = introcs.find_str(s, '"')
    # Find position of second double quote
    pos2 = introcs.find_str(s, '"', pos1+1)
    # Compute the substring between position 1 and 2
    result = s[pos1+1:pos2]
    # Retun the substring
    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
    
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
    
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, repr(json) + ' is not a string'

    # Find the position of "src"
    pos = introcs.find_str(json, '"src"')
    # Slice the string from "src"
    s = json[pos:]
    # Find the position of the : after src
    pos = introcs.find_str(s, ':')
    # Slice the string from :
    s = s[pos+1:]
    # Compute the substring in first double quotes from sliced string
    result = first_inside_quotes(s)
    # Return the result
    return result

    
def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
    
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
    
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, repr(json) + ' is not a string'

    # Find the position of "dst"
    pos = introcs.find_str(json, '"dst"')
    # Slice the string from "dst"
    s = json[pos:]
    # Find the position of the : after "dst"
    pos = introcs.find_str(s, ':')
    # Slice the string from :
    s = s[pos+1:]
    # Compute the substring in first double quotes from sliced string
    result = first_inside_quotes(s)
    # Return the result
    return result


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
    
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
    
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, repr(json) + ' is not a string'

    # Find the position of "error"
    pos = introcs.find_str(json, '"error"')
    # Slice the string from "error"
    s = json[pos:]
    # Find the position of : after "error"
    pos = introcs.find_str(s, ':')
    # Slice the string from :
    s = s[pos+1:]
    # Compute the substring in first double quotes from sliced string
    result = first_inside_quotes(s)
    # Return True if result is a subsring of result
    return len(result) > 0


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

        '{"success": true, "src": "<src-amount>", "dst": "<dst-amount>", "error": ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    choose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition: src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition: dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """

    assert type(src) == str, repr(src)+' not a string'
    assert introcs.find_str(src, ' '), repr(src) + ' has spaces in it'
    assert len(src) > 0, repr(src) + ' is an empty string'
    assert introcs.isalpha(src), repr(src) + 'has non aplhabetic charecters'

    assert type(dst) == str, repr(dst)+' not a string'
    assert introcs.find_str(dst, ' '), repr(dst)+ ' has spaces in it'
    assert len(dst) > 0, repr(dst)+ ' is an empty string'
    assert introcs.isalpha(dst), repr(dst) + 'has non aplhabetic charecters'

    assert type(amt) == int or type(amt) == float, repr(amt)+' should be int or float'

    # Convert amt to string to pass it to URL
    amt = str(amt)
    # Construct URL
    url = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='+\
        src+'&dst='+dst+'&amt='+amt+'&key='+APIKEY
    # Compute json response
    json = introcs.urlread(url)
    # Return json
    return json


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """

    # Call web service by passing currency and sub values for other fields to get json
    json = service_response(currency, 'EUR', 2.5)
    # check json has error by comparing to False and assign that to result
    result = has_error(json) == False
    # Return result
    return result


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """

    assert iscurrency(src), repr(src)+' is not a valid currency code'
    assert iscurrency(dst), repr(dst)+' is not a valid currency code'
    assert type(amt) == int or type(amt) == float, repr(amt)+' should be int or float'

    # Call web service with src, dst, amt
    json = service_response(src, dst, amt)
    # Compute dst value from json
    dst = get_dst(json)
    # Computer ONLY dst amount by removing current type and converts into float
    result = float(before_space(dst))
    # Return result
    return result