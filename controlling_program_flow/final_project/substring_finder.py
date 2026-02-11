"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Sravan Kumar Nuthalapati
Date: 12/02/2025
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.
    
    If sub does not appears anywhere in text, this function returns the empty tuple ().
    
    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)
    
    Parameter text: The text to search
    Precondition: text is a string
    
    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    
    pos = ()
    str_pos = 0

    going = True

    while going:
        index = introcs.find_str(text, sub, str_pos)
        if index == -1:
            going = False
        else:
            pos =  pos + (index,)
            str_pos = index + 1
    
    return pos
