# Day 5
# Part 1 complete

import math


# Checks all seat ids in file to locate the highest seat id number
def find_max_row_and_column(file_of_commands):
    locator_command = file_of_commands.readlines()
    seat_ids = []

    for command in locator_command:

        # Splits each command by row or column, example: 'BFFFBBFRRR'
        # row is 'BFFFBBF' and column is 'RRR'
        row_command = command[:7]
        column_command = command[7:]
        row_and_column = []

        row = find_row(row_command)
        column = find_column(column_command)
        row_and_column = [row, column]

        # Transforms the row and column and puts its unique seat id into a list
        seat_id = get_seat_id(row_and_column)
        seat_ids.append(seat_id)

    max_seat_id = max(seat_ids)

    return print("The maximum seat id number is: " + str(max_seat_id))


# @function find_row
# Takes in a string of 'F' (for front) or 'B' (for back)
# Returns: integer
# Between 0 to 127, split the range in half. Use the first half or second 
# depending if the command is F or B (front half 0 - 63 or back half 64 -127)
def find_row(row_locator):
    min_rows = 0
    max_rows = 127
    rows_range = [min_rows, max_rows]
    range_between_rows = max_rows - min_rows
    i = 0

    while i <= len(row_locator):
        for indicator in row_locator:
            if indicator == 'F':
                max_rows = math.floor((min_rows + (range_between_rows) / 2))
                rows_range = [min_rows, max_rows]
                range_between_rows = max_rows - min_rows
                i += 1

            elif indicator == 'B': 
                min_rows = math.ceil((max_rows - (range_between_rows) / 2)) 
                rows_range = [min_rows, max_rows]
                range_between_rows = max_rows - min_rows
                i += 1

        return rows_range[0]


# @function column
# Takes in a string of 'L' (for left) or 'R' (for right)
# Returns: integer
# Between 0 to 7, split the range in half. Use the first half or second 
# depending if the command is F or B (left half 0 - 3 or right half 4 - 7)
def find_column(column_locator):
    min_columns = 0
    max_columns = 7
    columns_range = [min_columns, max_columns]
    range_between_columns = max_columns - min_columns
    i = 0

    while i <= len(column_locator):
        for indicator in column_locator:
            if indicator == 'L':
                max_columns = math.floor(min_columns + (range_between_columns / 2))
                columns_range = [min_columns, max_columns]
                range_between_columns = max_columns - min_columns
                i += 1

            elif indicator == 'R':
                min_columns = math.ceil(max_columns - (range_between_columns / 2))
                columns_range = [min_columns, max_columns]
                range_between_columns = max_columns - min_columns
                i += 1
            
        return columns_range[0]


# Function get_seat_id
# Takes in a list
# Returns an integer
# Multiply the row by 8 and add the column to get the seat id
def get_seat_id(row_and_column_list):

    seat_id = (row_and_column_list[0] * 8) + row_and_column_list[1]

    return seat_id


######### Function for running tests

def run_test(testValue, expectedResult, description):
    print(description)
    if (testValue == expectedResult):
        print('    ✅ Test passed')
    else:
        print('    ❌ Test failed!')


############## Tests to confirm row function separately

# run_test(find_row('FBFBBFF'), [44, 44], "Check first sample of finding a 7 command row")
# run_test(find_row('B'), [64, 127], "B one digit sample of finding a 7 command row")
# run_test(find_row('F'), [0, 63], "F one digit sample of finding a 7 command row") 
# run_test(find_row('BB'), [96, 127], "Two digit sample of finding a 7 command row")
# run_test(find_row('BFFFBBF'), [70, 70], "B one digit sample of finding a 7 command row")
# run_test(find_row('FFFBBBF'), [14, 14], "F one digit sample of finding a 7 command row") 
# run_test(find_row('BBFFBBF'), [102, 102], "Two digit sample of finding a 7 command row")


##################### Test to confirm column function separately 

# run_test(find_column('L'), [0, 3], "R one digit sample of finding a 3 command column")
# run_test(find_column('R'), [4, 7], "L one digit sample of finding a 3 command column") 
# run_test(find_column('RR'), [6, 7], "Check first sample of finding a 3 command column")
# run_test(find_column('RRR'), [7, 7], "Two digit sample of finding a 3 command column") 
# run_test(find_column('RLL'), [4, 4], "Three digit sample of finding a 3 command column")


################### Test to check combo row and column 

# run_test(find_max_row_and_column('BFFFBBFRRR'), [70, 7], "Checking for row and column")
# run_test(find_max_row_and_column('FFFBBBFRRR'), [14, 7], "Checking for row and column") 
# run_test(find_max_row_and_column('BBFFBBFRLL'), [102, 4], "Checking for row and column")


################# Edit find_row_and_column arg input and loop to test retrieving seat ids

# run_test(find_max_row_and_column('BFFFBBFRRR'), 567, "Get seat ID")
# run_test(find_max_row_and_column('FFFBBBFRRR'), 119, "Get seat ID")
# run_test(find_max_row_and_column('BBFFBBFRLL'), 820, "Get seat ID")


f = open("day_5_datafile.txt", "r")

find_max_row_and_column(f)


#######################################################################
# Day 5 PART 2
########################################################################


# Checks all seats to locate my seat id
def find_row_and_column(file_of_commands):
    locator_command = file_of_commands.readlines()
    seat_ids = []

    for command in locator_command:

        # Splits each command by row or column, example: 'BFFFBBFRRR'
        # row is 'BFFFBBF' and column is 'RRR'
        row_command = command[:7]
        column_command = command[7:]
        row_and_column = []

        row = find_row(row_command)
        column = find_column(column_command)
        row_and_column = [row, column]

        # Transforms the row and column and puts its unique seat id into a list
        seat_id = get_seat_id(row_and_column)
        seat_ids.append(seat_id)

    # Find the seat that is empty but occupied on both sides
    my_seat_id = check_lst_values(seat_ids)

    return print("My seat id number is: " + str(my_seat_id))


# @function find_row
# Takes in a string of 'F' (for front) or 'B' (for back)
# Returns: integer
# Between 0 to 127, split the range in half. Use the first half or second 
# depending if the command is F or B (front half 0 - 63 or back half 64 -127)
def find_row(row_locator):
    min_rows = 0
    max_rows = 127
    rows_range = [min_rows, max_rows]
    range_between_rows = max_rows - min_rows
    i = 0

    while i <= len(row_locator):
        for indicator in row_locator:
            if indicator == 'F':
                max_rows = math.floor((min_rows + (range_between_rows) / 2))
                rows_range = [min_rows, max_rows]
                range_between_rows = max_rows - min_rows
                i += 1

            elif indicator == 'B':
                min_rows = math.ceil((max_rows - (range_between_rows) / 2))
                rows_range = [min_rows, max_rows]
                range_between_rows = max_rows - min_rows
                i += 1

        return rows_range[0]


# @function column
# Takes in a string of 'L' (for left) or 'R' (for right)
# Returns: integer
# Between 0 to 7, split the range in half. Use the first half or second 
# depending if the command is F or B (left half 0 - 3 or right half 4 - 7)
def find_column(column_locator):
    min_columns = 0
    max_columns = 7
    columns_range = [min_columns, max_columns]
    range_between_columns = max_columns - min_columns
    i = 0

    while i <= len(column_locator):
        for indicator in column_locator:
            if indicator == 'L':
                max_columns = math.floor(min_columns + (range_between_columns / 2))
                columns_range = [min_columns, max_columns]
                range_between_columns = max_columns - min_columns
                i += 1

            elif indicator == 'R':
                min_columns = math.ceil(max_columns - (range_between_columns / 2))
                columns_range = [min_columns, max_columns]
                range_between_columns = max_columns - min_columns
                i += 1

        return columns_range[0]


# Function get_seat_id
# Takes in a list
# Returns an integer
# Multiply the row by 8 and add the column to get the seat id
def get_seat_id(row_and_column_list):

    seat_id = (row_and_column_list[0] * 8) + row_and_column_list[1]
    
    return seat_id


# Function check_lst_values
# Takes in a list
# Returns a list
# Find the empty seat that is occupied on each side. A seat is open 
# if it is not on the seat id list. There should only be one seat id
# but it is a list that can hold more for debugging. 
def check_lst_values(filled_seats):
    
    # Make sure the seat ids are in numerical order
    filled_seats.sort()
    lst_of_my_seats = []

    for current_id in filled_seats[1:]:
        # Subtract 2 from the current seat id we're checking
        value_of_current_seat_id_minus_two = current_id-2 

        current_id_index = filled_seats.index(current_id)

        # Get the seat id (the value, not index) of the one that comes before it
        current_seat_id_minus_one = filled_seats[current_id_index-1]
        
        # If seat id getting checked is preceeded by a value that is two less,
        # for example 53 is two less than 55, than the num in between will be my seat
        if current_seat_id_minus_one == value_of_current_seat_id_minus_two: 
            
            # Take the value of the current seat id and subtract one from it
            # because that is an empty seat
            lst_of_my_seats.append(current_id-1)

    return lst_of_my_seats


f = open("day_5_datafile.txt", "r")

find_row_and_column(f)


