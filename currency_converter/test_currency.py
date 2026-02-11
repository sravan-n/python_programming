"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

"""

import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""
    
    print('Testing before_space')
    
    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello', result)

    result = currency.before_space(' Hello World')
    introcs.assert_equals('', result)

    result = currency.before_space('Hello World Test')
    introcs.assert_equals('Hello', result)

    result  = currency.before_space('Hello ')
    introcs.assert_equals('Hello', result)

    result = currency.before_space(' ')
    introcs.assert_equals('', result)

    result = currency.before_space('Hello   World')
    introcs.assert_equals('Hello', result)


def test_after_space(): 
    """Test procedure for after_space"""
    
    print('Testing after_space')
    
    result = currency.after_space('Hello World')
    introcs.assert_equals('World', result)

    result = currency.after_space(' Hello World')
    introcs.assert_equals('Hello World', result)

    result = currency.after_space('Hello ')
    introcs.assert_equals('', result)

    result = currency.after_space(' Hello')
    introcs.assert_equals('Hello', result)
    
    result = currency.after_space('Hello  World')
    introcs.assert_equals(' World', result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    
    print('Testing first_inside_quotes')

    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('"A B C D"')
    introcs.assert_equals('A B C D', result)

    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A""B')
    introcs.assert_equals('', result)


def test_get_src():
    """Test procedure for get_src"""

    print('Testing get_src')

    json = '{"success": true, "src": "2 United States Dollars", '+\
        '"dst": "1.772814 Euros", "error": ""}'
    result = currency.get_src(json)
    introcs.assert_equals('2 United States Dollars', result)

    json = '{"success":true,"src":"2 United States Dollars",'+\
        '"dst":"1.772814 Euros","error":""}'
    result = currency.get_src(json)
    introcs.assert_equals('2 United States Dollars', result)

    json = '{"success":false,"src":"","dst":"",'+\
        '"error":"Source currency code is invalid."}'
    result = currency.get_src(json)
    introcs.assert_equals('', result)

    json = '{"success": false, "src": "", "dst": "", '+\
        '"error": "Source currency code is invalid."}'
    result = currency.get_src(json)
    introcs.assert_equals('', result)
 
 
def test_get_dst():
    """Test procedure for get_dst"""

    print('Testing get_dst')

    json = '{"success": true, "src": "2 United States Dollars", '+\
        '"dst": "1.772814 Euros", "error": ""}'
    result = currency.get_dst(json)
    introcs.assert_equals('1.772814 Euros', result)

    json = '{"success":true,"src":"2 United States Dollars",'+\
        '"dst":"1.772814 Euros","error":""}'
    result = currency.get_dst(json)
    introcs.assert_equals('1.772814 Euros', result)

    json = '{"success":false,"src":"","dst":"",'+\
        '"error":"Source currency code is invalid."}'
    result = currency.get_dst(json)
    introcs.assert_equals('', result)

    json = '{"success": false, "src": "", "dst": "", '+\
        '"error": "Source currency code is invalid."}'
    result = currency.get_dst(json)
    introcs.assert_equals('', result)


def test_has_error():
    """Test procedure for has_error"""

    print('Testing has_error')

    json = '{"success":false,"src":"","dst":"",'+\
        '"error":"Source currency code is invalid."}'
    result = currency.has_error(json)
    introcs.assert_true(result)

    json = '{"success": false, "src": "", "dst": "", '+\
        '"error": "Source currency code is invalid."}'
    result = currency.has_error(json)
    introcs.assert_true(result)

    json = '{"success": true, "src": "2 United States Dollars", '+\
        '"dst": "1.772814 Euros", "error": ""}'
    result = currency.has_error(json)
    introcs.assert_false(result)

    json = '{"success":true,"src":"2 United States Dollars",'+\
        '"dst":"1.772814 Euros","error":""}'
    result = currency.has_error(json)
    introcs.assert_false(result)


def test_service_response():
    """Test procedure for service_response"""

    print('Testing service_response')

    result = currency.service_response('USD', 'EUR', 2.5)
    json = '{"success": true, "src": "2.5 United States Dollars", '+\
        '"dst": "2.2160175 Euros", "error": ""}'
    introcs.assert_equals(json, result)

    result = currency.service_response('USD', 'TEST', 2.5)
    json = '{"success": false, "src": "", "dst": "", '+\
        '"error": "The rate for currency TEST is not present."}'
    introcs.assert_equals(json, result)

    result = currency.service_response('USD', 'USD', 2.5)
    json = '{"success": true, "src": "2.5 United States Dollars", '+\
        '"dst": "2.5 United States Dollars", "error": ""}'
    introcs.assert_equals(json, result)

    result = currency.service_response('USD', 'EUR', 10)
    json = '{"success": true, "src": "10.0 United States Dollars", '+\
        '"dst": "8.86407 Euros", "error": ""}'
    introcs.assert_equals(json, result)

    result = currency.service_response('USD', 'EUR', -10)
    json = '{"success": true, "src": "-10.0 United States Dollars", '+\
        '"dst": "-8.86407 Euros", "error": ""}'
    introcs.assert_equals(json, result)

    result = currency.service_response('TEST', 'USD', 2.5)
    json = '{"success": false, "src": "", "dst": "", '+\
        '"error": "The rate for currency TEST is not present."}'
    introcs.assert_equals(json, result)


def test_iscurrency():
    """Test procedure for iscurrency"""

    print('Testing iscurrency')

    result = currency.iscurrency('USD')
    introcs.assert_true(result)

    result = currency.iscurrency('abc')
    introcs.assert_false(result)


def test_exchange():
    """Test procedure for exchange"""

    print('Testing exchange')

    result = currency.exchange('USD', 'EUR', 10)
    introcs.assert_floats_equal(8.86407, result)

    result = currency.exchange('USD', 'EUR', -10)
    introcs.assert_floats_equal(-8.86407, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print('All tests completed successfully')