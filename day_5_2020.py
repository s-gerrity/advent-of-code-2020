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


def find_row_and_column(command):

    row_command = command[:7]
    column_command = command[7:]
    row_and_column = []

    row = find_row(row_command)
    column = find_column(column_command)
    row_and_column = [row, column]
    seat_id = get_seat_id(row_and_column)
    # SEAT_ID_LIST.append(seat_id)

    # max_seat_id = max(SEAT_ID_LIST)
    # print(SEAT_ID_LIST)
    # print(seat_id, "seat id")
    return seat_id


def get_seat_id(row_and_column_list):
    seat_id = (row_and_column_list[0] * 8) + row_and_column_list[1]

    return seat_id


def run_test(testValue, expectedResult, description):
    print(description)
    if (testValue == expectedResult):
        print('    ✅ Test passed')
    else:
        print('    ❌ Test failed!')


# run_test(find_row('FBFBBFF'), [44, 44], "Check first sample of finding a 7 command row")
# run_test(find_row('B'), [64, 127], "B one digit sample of finding a 7 command row")
# run_test(find_row('F'), [0, 63], "F one digit sample of finding a 7 command row") 
# run_test(find_row('BB'), [96, 127], "Two digit sample of finding a 7 command row")
# run_test(find_row('BFFFBBF'), [70, 70], "B one digit sample of finding a 7 command row")
# run_test(find_row('FFFBBBF'), [14, 14], "F one digit sample of finding a 7 command row") 
# run_test(find_row('BBFFBBF'), [102, 102], "Two digit sample of finding a 7 command row")


# run_test(find_column('L'), [0, 3], "R one digit sample of finding a 3 command column")
# run_test(find_column('R'), [4, 7], "L one digit sample of finding a 3 command column") 
# run_test(find_column('RR'), [6, 7], "Check first sample of finding a 3 command column")
# run_test(find_column('RRR'), [7, 7], "Two digit sample of finding a 3 command column") 
# run_test(find_column('RLL'), [4, 4], "Three digit sample of finding a 3 command column")


# run_test(find_row_and_column('BFFFBBFRRR'), [70, 7], "Checking for row and column")
# run_test(find_row_and_column('FFFBBBFRRR'), [14, 7], "Checking for row and column") 
# run_test(find_row_and_column('BBFFBBFRLL'), [102, 4], "Checking for row and column")


# run_test(find_row_and_column('BFFFBBFRRR'), 567, "Get seat ID")
# run_test(find_row_and_column('FFFBBBFRRR'), 119, "Get seat ID")
# run_test(find_row_and_column('BBFFBBFRLL'), 820, "Get seat ID")
# run_test(find_row_and_column(['FFFFBFFLLL',
# 'FFFFBFBLLL',
# 'FFFFBFBLLR',
# 'FFFFBFFLLR',
# 'FFFFBFFLRL',
# 'FFFFBFBLRL',
# 'FFFFBFFLRR',
# 'FFFFBFBLRR']), [32, 32, 33, 33, 34, 34, 35, 35], "Get seat ID")
# run_test(find_row_and_column(['FFFFBFBLLL']), [32], "Get seat ID")

print(find_row_and_column('FFFFBFFLLL'))
print(find_row_and_column('FFFFBFBLLL'))
print(find_row_and_column('FFFFBFBLLR'))
print(find_row_and_column('FFFFBFFLLR'))

