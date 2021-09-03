# Day 5
# Part 1 complete

import math

# SEAT_ID_LIST = set()


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

    while i < len(column_locator):
        for indicator in column_locator:
            if indicator == 'L':
                max_columns = math.floor(
                    min_columns + (range_between_columns / 2))
                columns_range = [min_columns, max_columns]
                range_between_columns = max_columns - min_columns
                i += 1

            elif indicator == 'R':
                min_columns = math.ceil(
                    max_columns - (range_between_columns / 2))
                columns_range = [min_columns, max_columns]
                range_between_columns = max_columns - min_columns
                i += 1

        return columns_range[0]


def find_row_and_column(file_of_commands):
    locator_command = file_of_commands.readlines()
    seat_ids = []

    for command in locator_command:

        row_command = command[:6]
        column_command = command[7:]
        row_and_column = []

        row = find_row(row_command)
        column = find_column(column_command)
        row_and_column = [row, column]
        seat_id_list = get_seat_id(row_and_column)
        seat_ids.append(seat_id_list)
    

    # print(seat_ids, "seat id list")

    filled_seats = find_my_seat(seat_ids)
    # print(filled_seats)
    my_seat_lst = check_lst_values(filled_seats)
    # max_seat_id = max(SEAT_ID_LIST)
    return my_seat_lst


def get_seat_id(row_and_column_list):
    seat_id = (row_and_column_list[0] * 8) + row_and_column_list[1]

    return seat_id


def find_my_seat(seat_id_list):
    seats_filled = []
    lst_of_possible_seat_ids = all_possible_seats()

    for seat_id in lst_of_possible_seat_ids:
        if seat_id in seat_id_list:
            seats_filled.append(seat_id)
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
 
# check_lst_values([5, 6, 7, 16, 17, 18, 19, 20, 21, 22, 23, 32, 33, 34, 35, 36, 37, 38, 39, 48, 49, 50, 51, 52, 53, 54, 55, 64, 65, 66, 67, 68, 69, 70, 71, 80, 81, 82, 83, 84, 85, 87, 96, 97, 98, 99, 100, 101, 102, 103, 112, 113, 114, 115, 116, 117, 118, 119, 128, 129, 130, 131, 132, 133, 134, 135, 144, 145, 146, 147, 148, 149, 150, 151, 160, 161, 162, 163, 164, 165, 166, 167, 176, 177, 178, 179, 180, 181, 182, 183, 192, 193, 194, 195, 196, 197, 198, 199, 208, 209, 210, 211, 212, 213, 214, 215, 224, 225, 226, 227, 228, 229, 230, 231, 240, 241, 242, 243, 244, 245, 246, 247, 256, 257, 258, 259, 260, 261, 262, 263, 272, 273, 274, 275, 276, 277, 278, 279, 288, 289, 290, 291, 292, 293, 294, 295, 304, 305, 306, 307, 308, 309, 310, 311, 320, 321, 322, 323, 324, 325, 326, 327, 336, 337, 338, 339, 340, 341, 342, 343, 352, 353, 354, 355, 356, 357, 358, 359, 368, 369, 370, 371, 372, 373, 374, 375, 384, 385, 386, 387, 388, 389, 390, 391, 400, 401, 402, 403, 404, 405, 406, 407, 416, 417, 418, 419, 420, 421, 422, 423, 432, 433, 434, 435, 436, 437, 438, 439, 448, 449, 450, 451, 452, 453, 454, 455, 464, 465, 466, 467, 468, 469, 470, 471, 480, 481, 482, 483, 484, 485, 486, 487, 496, 497, 498, 499, 500, 501, 502, 503, 512, 513, 514, 515, 516, 517, 518, 519, 528, 529, 530, 531, 532, 533, 534, 535, 544, 545, 546, 547, 548, 549, 550, 551, 560, 561, 562, 563, 564, 565, 566, 567, 576, 577, 578, 579, 580, 581, 582, 583, 592, 593, 594, 595, 596, 597, 598, 599, 608, 609, 610, 611, 612, 613, 614, 615, 624, 625, 626, 627, 628, 629, 630, 631, 640, 641, 642, 643, 644, 645, 646, 647, 656, 657, 658, 659, 660, 661, 662, 663, 672, 673, 674, 675, 676, 677, 678, 679, 688, 689, 690, 691, 692, 693, 694, 695, 704, 705, 706, 707, 708, 709, 710, 711, 720, 721, 722, 723, 724, 725, 726, 727, 736, 737, 738, 739, 740, 741, 742, 743, 752, 753, 754, 755, 756, 757, 758, 759, 768, 769, 770, 771, 772, 773, 774, 775, 784, 785, 786, 787, 788, 789, 790, 791, 800, 801, 802, 803, 804, 805, 806, 807, 816, 817, 818, 819, 820, 821, 822, 823, 832, 833, 834, 835, 836, 837, 838, 839, 848, 849, 850, 851, 852, 853, 854, 855, 864, 865, 866, 867, 868, 869, 870, 871])

# make a list with all possible seat ids
# make a list with all seat ids captured from project
# if seat in total list is not also in project list, add to a list
# seat id's at the beginning and end of list are irrelvent
# seat id in middle of pack with a seat on each side is mine


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
