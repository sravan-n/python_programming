"""
Functions for simple reading to and writing from a file.
"""


def count_lines(filepath):
    """
    Returns the number of lines in the given file.

    Lines are separated by the '\n' character, which is standard for Unix files.

    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    # HINT: Remember, you can use a file in a for-loop

    file = open(filepath)

    no_of_line = 0

    for line in file:
        no_of_line = no_of_line+1

    file.close()
    return no_of_line


def write_numbers(filepath,n):
    """
    Writes the numbers 0..n-1 to a file.

    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character,
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'

    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file

    Parameter n: The number of lines to write
    Precondition: n is an int > 0.
    """
    # HINT: You can only write strings to a file, so convert the numbers first

    file = open(filepath, 'w')

    no_of_entries = 0

    while no_of_entries < n:
        entry = str(no_of_entries)
        if (no_of_entries == n-1):
            file.write(entry)
        else:
            file.write(entry)
            file.write('\n')

        no_of_entries = no_of_entries+1

    file.close()
