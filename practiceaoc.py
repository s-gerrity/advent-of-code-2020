# day 5 practice

import math


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


def find_row_and_column(file_of_commands):
    locator_command = file_of_commands.readlines()
    seat_ids = []

    for command in locator_command:

        row_command = command[:7]
        column_command = command[7:]
        row_and_column = []

        row = find_row(row_command)
        column = find_column(column_command)
        row_and_column = [row, column]
        seat_id = get_seat_id(row_and_column)
        seat_ids.append(seat_id)

    filled_seats = find_my_seat(seat_ids)
    my_seat_lst = check_lst_values(filled_seats)
    return my_seat_lst


def get_seat_id(row_and_column_list):

    seat_id = (row_and_column_list[0] * 8) + row_and_column_list[1]
    

    return seat_id


def find_my_seat(seat_ids):

    seats_filled = []
    lst_of_possible_seat_ids = all_possible_seats()

    for id in lst_of_possible_seat_ids:
        if id in seat_ids:   
            seats_filled.append(id)
    return seats_filled


def all_possible_seats():
    lst_of_possible_seat_ids = []

    for i in range(881):
        lst_of_possible_seat_ids.append(i)
    return lst_of_possible_seat_ids


def check_lst_values(filled_seats):
    i = 1
    lst_of_my_seats = []
    for id in filled_seats[1:]:
    
        id_index = filled_seats.index(id)
        id_below = filled_seats[id_index-i]
        if id_below == id-2:
            lst_of_my_seats.append(id-1)


    return lst_of_my_seats


f = open("day_5_datafile.txt", "r")

print(find_row_and_column(f))


