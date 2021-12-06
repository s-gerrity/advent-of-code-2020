# Day 3
# PART 1

sample_data = open("day_3_2021_datafile.txt", "r")
diagnostic_report = sample_data.read()
lst_diagnostic_report = diagnostic_report.split('\n')

zeroes = 0
ones = 0
i = 0
len_num = 0
zeroes_lst = []
ones_lst = []
gamma_rate_num_lst = []

# pseudocode
# need to iterate through the first char in each item of the list
# add each item to a new list
# call a func that counts the zeroes and ones
# call a func that returns which value is max
# add that item to a list
# join list as string

# or

# iterate through first num of each item in list
# if zero or one, add to a running total for each
# once through the first of all in list, max one of zero and add to list
# using len of item, if i is less than len, increase i and recurssively go again


def max_zeroes_and_ones(gamma_rate_num_lst, zeroes_lst, ones_lst, i):
    if i == 5:
        print(gamma_rate_num_lst)
        return gamma_rate_num_lst

    
    if int(zeroes_lst[i]) > int(ones_lst[i]):
        gamma_rate_num_lst.append('0')
    else:
        gamma_rate_num_lst.append('1')
    i += 1

    max_zeroes_and_ones(gamma_rate_num_lst, zeroes_lst, ones_lst, i)

    return gamma_rate_num_lst


def find_gamma_rate(lst_diagnostic_report, zeroes, ones, i, zeroes_lst, ones_lst):

    for item in lst_diagnostic_report:
        if i == 5:
            print(zeroes_lst)
            print(ones_lst)
            gamma_num_lst = max_zeroes_and_ones(gamma_rate_num_lst, zeroes_lst, ones_lst, 0)
            gamma_num = ''.join(gamma_num_lst)

            epsilion_num = get_epsilion_rate(gamma_num)
            print(epsilion_num, "EP")
            return gamma_num

        bit = item[i]

        if bit == '0':
            zeroes += 1

        else:
            ones += 1
    
    if i < len(item):
        i += 1
        zeroes_lst.append(zeroes)
        zeroes = 0
        ones_lst.append(ones)
        ones = 0
        gamma_num = find_gamma_rate(lst_diagnostic_report, zeroes, ones, i, zeroes_lst, ones_lst) 
        
    return gamma_num


def get_epsilion_rate(gamma_num):
    epsilion_lst = []

    for num in gamma_num:
        if num == '0':
            epsilion_lst.append('1')
        else:
            epsilion_lst.append('0')
    
    epsilion_num = ''.join(epsilion_lst)
    return epsilion_num




if __name__ == '__main__':
    print(find_gamma_rate(lst_diagnostic_report, zeroes, ones, i, zeroes_lst, ones_lst))

