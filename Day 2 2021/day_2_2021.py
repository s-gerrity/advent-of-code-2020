# Day 2
# PART 1

sample_data = open("day_2_2021_datafile.txt", "r")
sub_movement = sample_data.read()
lst_sub_movement = sub_movement.split('\n')

def sum_movement_totals(lst_of_movements):
    total = 0

    for item in lst_of_movements:
        total += int(item)

    return total


def get_sub_movement(lst_sub_movement):
    forwards_lst = []
    downs_lst = []
    ups_lst =[]

    for item in lst_sub_movement:

        if 'forward' in item:
            forwards_lst.append(item[8:])
        elif 'up' in item:
            ups_lst.append(item[3:])
        else:
            downs_lst.append(item[5:])

    forwards_total_sum = sum_movement_totals(forwards_lst)
    ups_total_sum = sum_movement_totals(ups_lst)
    downs_total_sum = sum_movement_totals(downs_lst)

    depth = downs_total_sum - ups_total_sum

    return print(depth * forwards_total_sum)





if __name__ == '__main__':
    get_sub_movement(lst_sub_movement)