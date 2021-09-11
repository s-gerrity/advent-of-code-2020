# day 5 practice

import math

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

    # Compare the filled seats with the empty seats to find my id
    filled_seats = find_my_seat(seat_ids)
    my_seat_id = check_lst_values(filled_seats)

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


# Function find_my_seat
# Takes in a list
# Returns a list
# Generates a list of all occupied seats by retrieving a list of all seats on 
# the plane and comparing it with the seat ids created. 
def find_my_seat(seat_ids):

    seats_filled = []
    lst_of_possible_seat_ids = all_possible_seats()

    for id in lst_of_possible_seat_ids:
        if id in seat_ids:   
            seats_filled.append(id)
    return seats_filled


# Function all_possible_seats
# No parameters
# Returns a list
# From a part 1 we learned the maximum amount of seats on the plane was 
# 880. This function generates a list of all possible seats on the plane. 
def all_possible_seats():
    lst_of_possible_seat_ids = []

    for i in range(881):
        lst_of_possible_seat_ids.append(i)

    return lst_of_possible_seat_ids


# Function check_lst_values
# Takes in a list
# Returns a list
# Find the empty seat that is occupied on each side. A seat is open 
# if it is not on the seat id list. There should only be one seat id
# but it is a list that can hold more for debugging. 
def check_lst_values(filled_seats):
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


