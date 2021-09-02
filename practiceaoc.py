# day 5 practice
import math

def find_row(row_locator):
    max_rows = 127
    min_rows = 0
    rows_range = [min_rows, max_rows]
    range_between_rows = max_rows - min_rows


    i = 0
    while i < len(row_locator):
        for indicator in row_locator:
            if indicator == 'F':
                max_rows = math.floor((min_rows + (math.floor(range_between_rows) / 2)))
                print(max_rows, "F max_rows") # 63
                i += 1
                rows_range = [min_rows, max_rows]
                print(rows_range, "rows_range inside loop")
                range_between_rows = math.floor(max_rows - min_rows)
                print(range_between_rows, "range_between_rows updated inside loop")
  


            if indicator == 'B': 
                min_rows = math.ceil((max_rows - (math.floor(range_between_rows) / 2))) # 127 - (63 / 2) = 96
                print(min_rows, "min_rows") # 96
                i += 1
                rows_range = [min_rows, max_rows]
                range_between_rows = math.floor(max_rows - min_rows)

                print(range_between_rows, "range_between_rows SECOND time", rows_range, "rows range in loop") 
        # print(rows_range, "rows_range at the exit")
        return rows_range

def find_column():
    max_column = 7
    min_column = 0
    columns_range = [min_column, max_column]
    range_between_columns = max_column - min_column


def run_test(testValue, expectedResult, description):
    print(description)
    if (testValue == expectedResult):
        print('    ✅ Test passed')
    else:
        print('    ❌ Test failed!')


run_test(find_row('FBFBBFF'), [44, 44], "Check first sample of finding a 7 command row")
run_test(find_row('B'), [64, 127], "B one digit sample of finding a 7 command row")
run_test(find_row('F'), [0, 63], "F one digit sample of finding a 7 command row") 
run_test(find_row('BB'), [96, 127], "Two digit sample of finding a 7 command row")
run_test(find_row('BFFFBBF'), [70, 70], "B one digit sample of finding a 7 command row")
run_test(find_row('FFFBBBF'), [14, 14], "F one digit sample of finding a 7 command row") 
run_test(find_row('BBFFBBF'), [102, 102], "Two digit sample of finding a 7 command row")


run_test(find_column('L'), [0, 3], "R one digit sample of finding a 3 command column")
run_test(find_column('R'), [4, 7], "L one digit sample of finding a 3 command column") 
run_test(find_column('RR'), [6, 7], "Check first sample of finding a 3 command column")



# pseudocode:
# have a list with min rows max rows [min, max]
# for each item in the command
# check which command it is (front or back of rows)
# if its the back, divide the max rows to find the starting point of the range
# replace min rows with the new starting [min, max]
# 