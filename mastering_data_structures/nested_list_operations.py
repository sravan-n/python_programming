"""
Module demonstrating immutable functions on nested lists.

All of these functions make use of accumulators that make new lists.

Author: Sravan Kumar Nuthalapati
Date: 01/29/2026
"""


def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.
    
    This function assumes that table has no header, so each row has only numbers in it.
    
    Examples: 
        row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) returns [0.9, 1.5, 1.7]
        row_sums([[0.2,0.1],[-0.2,0.1],[0.2,-0.1],[-0.2,-0.1]]) returns [0.3, -0.1, 0.1, -0.3]
    
    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words, 
        (1) table is a nested 2D list in row-major order, 
        (2) each row contains only numbers, and 
        (3) each row is the same length.
    """

    result_list = []

    for list in table:
        sum = 0
        for item in list:
            sum = sum + item
        result_list.append(sum)

    return result_list


# Immutable Functions
def crossout(table,row,col):
    """
    Returns a copy of the table, missing the given row and column.
      
    Examples:
        crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
        crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
        crossout([[1,3],[6,2]],0,0) returns [[2]]
        crossout([[6]],0,0) returns []
    
    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words, 
        (1) table is a nested 2D list in row-major order, 
        (2) each row contains only numbers, and 
        (3) each row is the same length.
    
    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table
    
    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    
    crossout_table = []

    total_rows = len(table)
    total_columns = len(table[0])

    for row_pos in range(total_rows):
        if row_pos != row:
            crossout_table_row = []
            for col_pos in range(total_columns):
                if col_pos != col:
                    crossout_table_row.append(table[row_pos][col_pos])

            crossout_table.append(crossout_table_row)

    return crossout_table


# Mutable Functions
def crossout_2(table,row,col):
    """
    Modifies the table to remove the given row and column.
    
    Examples:
        If a = [[1,3,5],[6,2,7],[5,8,4]], crossout(a,1,2) changes a to [[1,3],[5,8]]
        If a = [[1,3,5],[6,2,7],[5,8,4]], crossout(a,0,0) changes a to [[2,7],[8,4]]
        If a = [[1,3],[6,2]], crossout(a,0,0) changes a to [[2]]
        If a = [[6]], crossout(a,0,0) changes a to []
    
    Parameter table: the nested list to modify
    Precondition: table is a table of numbers.  In other words, 
        (1) table is a nested 2D list in row-major order, 
        (2) each row contains only numbers, and 
        (3) each row is the same length.
    
    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table
    
    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """

    table.pop(row)

    for row_in_table in table:
        row_in_table.pop(col)


def place_sums(table):
    """
    Modifies the table to add a column summing the previous elements in the row.
    
    This function assumes that the table has a header, which means the first row
    only has strings in it.  The later rows are only numbers.  This function
    adds the string 'Sum' to the first row.  For each later row, it appends the
    sum of that row.
    
    Example: Suppose that a is
        
        [['First','Second','Third'], [0.1,0.3,0.5], [0.6,0.2,0.7], [0.5,1.1,0.1]]
    
    then place_sums(a) modifies the table a so that it is now
        
        [['First', 'Second', 'Third', 'Sum'],
         [0.1, 0.3, 0.5, 0.9], [0.6, 0.2, 0.7, 1.5], [0.5, 1.1, 0.1, 1.7]]
    
    Parameter table: the nested list to process
    Precondition: table is a table of numbers with a header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) the first row only
    contains strings (the headers) (3) each row after the first contains only
    numbers, and (4) each row is the same length.
    """
    
    total_rows = len(table)
    
    for pos in range(total_rows):
        if pos == 0:
            table[0].append('Sum')
        else:
            sum = 0
            for val in table[pos]:
                sum = sum + val
            table[pos].append(round(sum, 10))

