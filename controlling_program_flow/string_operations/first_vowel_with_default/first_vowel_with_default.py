"""  
A function to search for the first vowel position

"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """

    pos_a = introcs.find_str(s, 'a')
    pos_e = introcs.find_str(s, 'e')
    pos_i = introcs.find_str(s, 'i')
    pos_o = introcs.find_str(s, 'o')
    pos_u = introcs.find_str(s, 'u')
    pos_y = introcs.find_str(s, 'y', 1)

    result = len(s)

    if pos_a > -1 and pos_a < result:
        result = pos_a
    if pos_e > -1 and pos_e < result:
        result = pos_e
    if pos_i > -1 and pos_i < result:
        result = pos_i
    if pos_o > -1 and pos_o < result:
        result = pos_o
    if pos_u > -1 and pos_u < result:
        result = pos_u
    if pos_y > 0 and pos_y < result:
        result = pos_y
    
    return result if result > -1 and result < len(s) else -1
