"""  
A collection of functions to support the translation of words into Pig Latin.

This module contains two functions.  The first function searchs for the location of the 
first vowel.  The second function uses this as a helper to perform the conversion.

Author: Sravan Kumar Nuthalapati
Date: 11/24/2025
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


def pigify(s):
    """
    Returns a copy of s converted to Pig Latin
    
    Pig Latin is childish encoding of English that adheres to the following rules:
    
    1.  The vowels are 'a', 'e', 'i', 'o', 'u', as well as any 'y'
        that is not the first letter of a word. All other letters are consonants.
        
        For example, 'yearly' has three vowels  ('e', 'a', and the last 'y') 
        and three consonants (the first 'y', 'r', and 'l').
    
    2.  If the English word begins with a vowel, append 'hay' to the end of the word 
        to get the Pig Latin equivalent. For example, 'ask 'askhay' and 'use' becomes 
        'usehay'.
    
    3.  If the English word starts with 'q', then it must be followed by'u'; move 
        'qu' to the end of the word, and append 'ay'.  Hence 'quiet' becomes
        'ietquay' and 'quay' becomes 'ayquay'.
    
    4.  If the English word begins with a consonant, move all the consonants up to 
        the first vowel (if any) to the end and add 'ay'.  For example, 'tomato' 
        becomes 'omatotay', 'school' becomes 'oolschay'. 'you' becomes 'ouyay' and 
        'ssssh' becomes 'sssshay'.
    
    Parameter s: the string to change to Pig Latin
    Precondition: s is a nonempty string with only lowercase letters. If s starts with
    'q', then it starts with 'qu'.
    """
    
    if s[1] != 'y' and first_vowel(s) == 0:
        return s + 'hay'
    elif s[:2] == 'qu':
        return s[2:]+'quay'
    elif first_vowel(s) == -1:
        return s+'ay'
    else:
        return s[first_vowel(s):] + s[:first_vowel(s)] + 'ay'
