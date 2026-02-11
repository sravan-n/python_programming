"""  
A test script for the function iso_8601.

"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')
    
    # Put your test cases here

    result = func.iso_8601('01:01:01')
    introcs.assert_equals(True, result)

    result = func.iso_8601('1:1:1')
    introcs.assert_equals(False, result)

    result = func.iso_8601('26:26:26')
    introcs.assert_equals(False, result)

    result = func.iso_8601('time')
    introcs.assert_equals(False, result)

    result = func.iso_8601('01:01')
    introcs.assert_equals(False, result)

    result = func.iso_8601('01:01:01:01')
    introcs.assert_equals(False, result)

    result = func.iso_8601('aa:aa:aa')
    introcs.assert_equals(False, result)

    result = func.iso_8601('111')
    introcs.assert_equals(False, result)

    result = func.iso_8601('11:60:00')
    introcs.assert_equals(False, result)

    result = func.iso_8601('11:59:60')
    introcs.assert_equals(False, result)



if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')