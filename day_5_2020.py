# Day 5
# Part 1 complete

import math

SEAT_ID_LIST = []

def find_row(row_locator):
    min_rows = 0
    max_rows = 127
    rows_range = [min_rows, max_rows]
    range_between_rows = max_rows - min_rows
    i = 0

    while i < len(row_locator):
        for indicator in row_locator:
            if indicator == 'F':
                max_rows = math.floor((min_rows + (range_between_rows) / 2))
                # print(max_rows, "F max_rows") # 63
                rows_range = [min_rows, max_rows]
                # print(rows_range, "rows_range inside loop")
                range_between_rows = max_rows - min_rows
                # print(range_between_rows, "range_between_rows updated inside loop")
                i += 1

            elif indicator == 'B': 
                min_rows = math.ceil((max_rows - (range_between_rows) / 2)) # 127 - (63 / 2) = 96
                # print(min_rows, "min_rows") # 96
                rows_range = [min_rows, max_rows]
                range_between_rows = max_rows - min_rows
                # print(range_between_rows, "range_between_rows SECOND time", rows_range, "rows range in loop") 
                i += 1

        return rows_range[0]


def find_column(column_locator):
    min_columns = 0
    max_columns = 7
    columns_range = [min_columns, max_columns]
    range_between_columns = max_columns - min_columns
    i = 0

    while i < len(column_locator):
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

    for command in locator_command:

        row_command = command[:6]
        column_command = command[7:]
        row_and_column = []

        row = find_row(row_command)
        column = find_column(column_command)
        row_and_column = [row, column]
        seat_id = get_seat_id(row_and_column)
        SEAT_ID_LIST.append(seat_id)

    max_seat_id = max(SEAT_ID_LIST)
    return max_seat_id


def get_seat_id(row_and_column_list):
    seat_id = (row_and_column_list[0] * 8) + row_and_column_list[1]

    return seat_id



def run_test(testValue, expectedResult, description):
    print(description)
    if (testValue == expectedResult):
        print('    ✅ Test passed')
    else:
        print('    ❌ Test failed!')


# # run_test(find_row('FBFBBFF'), [44, 44], "Check first sample of finding a 7 command row")
# # run_test(find_row('B'), [64, 127], "B one digit sample of finding a 7 command row")
# # run_test(find_row('F'), [0, 63], "F one digit sample of finding a 7 command row") 
# # run_test(find_row('BB'), [96, 127], "Two digit sample of finding a 7 command row")
# # run_test(find_row('BFFFBBF'), [70, 70], "B one digit sample of finding a 7 command row")
# # run_test(find_row('FFFBBBF'), [14, 14], "F one digit sample of finding a 7 command row") 
# # run_test(find_row('BBFFBBF'), [102, 102], "Two digit sample of finding a 7 command row")


# # run_test(find_column('L'), [0, 3], "R one digit sample of finding a 3 command column")
# # run_test(find_column('R'), [4, 7], "L one digit sample of finding a 3 command column") 
# # run_test(find_column('RR'), [6, 7], "Check first sample of finding a 3 command column")
# # run_test(find_column('RRR'), [7, 7], "Two digit sample of finding a 3 command column") 
# # run_test(find_column('RLL'), [4, 4], "Three digit sample of finding a 3 command column")


# # run_test(find_row_and_column('BFFFBBFRRR'), [70, 7], "Checking for row and column")
# # run_test(find_row_and_column('FFFBBBFRRR'), [14, 7], "Checking for row and column") 
# # run_test(find_row_and_column('BBFFBBFRLL'), [102, 4], "Checking for row and column")


# run_test(find_row_and_column('BFFFBBFRRR'), 567, "Get seat ID")
# run_test(find_row_and_column('FFFBBBFRRR'), 119, "Get seat ID")
# run_test(find_row_and_column('BBFFBBFRLL'), 820, "Get seat ID")

f = open("day_5_datafile.txt", "r")

print(find_row_and_column(f))

# # pseudocode:
# # have a list with min rows max rows [min, max]
# # for each item in the command
# # check which command it is (front or back of rows)
# # if its the back, divide the max rows to find the starting point of the range
# # replace min rows with the new starting [min, max]
# # 