"""
Module with a function to read and write CSV files (using data in a 2D list)
"""

import csv

def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.

    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the
    programmer to interpret this data, since CSV files contain no type information.

    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file
    is a valid CSV file
    """

    file = open(filename)
    wrapper = csv.reader(file)

    result = []

    for data in wrapper:
        result.append(data)

    file.close()

    return result


def write_csv(data,filename):
    """
    Writes the given data out as a CSV file filename.

    To be a proper CSV file, data must be a 2-dimensional list with the first row
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.

    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list

    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """

    file = open(filename, 'w')
    wrapper = csv.writer(file)

    for row in data:
        wrapper.writerow(row)

    file.close()
