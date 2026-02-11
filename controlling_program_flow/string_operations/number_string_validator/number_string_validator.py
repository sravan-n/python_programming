"""  
A function to check the validity of a numerical string

Author: Sravan Kumar Nuthalapati
Date: 11/24/2025
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.
    
    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.
    
    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).
    
    Examples: 
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True 
        valid_format('012') returns False
    
    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """

    if len(s) <= 3:
        if introcs.isnumeric(s):
            if len(s) == 1 and s[0] == '0':
                return True
            elif s[0] != '0':
                return True
            else:
                return False
        else:
            return False
    else:
        pos_comma = introcs.find_str(s, ',')
        after_comma = s[pos_comma+1:]
        before_comma = s[:pos_comma]
        if pos_comma == -1:
            return False
        elif introcs.isnumeric(after_comma) and introcs.isnumeric(before_comma):
            if len(after_comma) == 3 and s[0] != '0':
                return True
            else:
                return False
        else:
            return False
    

