# Day 2
# PART 1

sample_data = open("day_2_2021_datafile.txt", "r")
sub_movement = sample_data.read()
lst_sub_movement = sub_movement.split('\n')

# def sum_movement_totals(lst_of_movements):
#     total = 0

#     for item in lst_of_movements:
#         total += int(item)

#     return total


# def get_sub_movement(lst_sub_movement):
#     forwards_lst = []
#     downs_lst = []
#     ups_lst =[]

#     for item in lst_sub_movement:

#         if 'forward' in item:
#             forwards_lst.append(item[8:])
#         elif 'up' in item:
#             ups_lst.append(item[3:])
#         else:
#             downs_lst.append(item[5:])

#     forwards_total_sum = sum_movement_totals(forwards_lst)
#     ups_total_sum = sum_movement_totals(ups_lst)
#     downs_total_sum = sum_movement_totals(downs_lst)

#     depth = downs_total_sum - ups_total_sum

#     return print(depth * forwards_total_sum)


# PART 2


aim = 0
horizontal = 0
depth = 0


def sum_movement_totals(lst_of_movements):
    total = 0

    for item in lst_of_movements:
        total += int(item)

    return total

def config_up_aim(up_num, aim):
    # up X decreases your aim by X units.

    aim -= int(up_num)

    return aim


def config_down_aim(down_num, aim):
    # down X increases your aim by X units.

    aim += int(down_num)

    return aim


def config_horizontal(forward_num, horizontal):
    # increases your horizontal position by X units.
    
    horizontal += int(forward_num)

    return horizontal


def get_depth(forward_num, aim, depth):
    # increases your depth by your aim multiplied by X.

    depth += int(aim) * int(forward_num)

    return depth

# pseudocode
# need to go through each command one by one in order, cant collect in bunches
# iterate through main datalist
# ex: if item in main list is 'down'
# then save num as 'down_num'
# call helper function for down aim config
# return aim
# make sure aim and horizontal continue to change and save w each iteration


def get_sub_movement(lst_sub_movement, aim, horizontal, depth):

    for item in lst_sub_movement:

        if 'forward' in item:
            forward_num = item[8:]

            # increases your horizontal position by X units.
            horizontal = config_horizontal(forward_num, horizontal)

            # increases your depth by your aim multiplied by X.
            depth = get_depth(forward_num, aim, depth)
            
        elif 'up' in item:
            up_num = item[3:]

            # up X decreases your aim by X units.
            aim = config_up_aim(up_num, aim)

        else:
            down_num = item[5:]

            # adds up down nums to config aim
            aim = config_down_aim(down_num, aim)


    # print("Aim is", aim)
    print("Horizontal is", horizontal)
    print("Depth is", depth)





if __name__ == '__main__':
    get_sub_movement(lst_sub_movement, aim, horizontal, depth)