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


def get_gamma_rate(gamma_rate_num_lst, zeroes_lst, ones_lst):

    gamma_num_lst = max_zeroes_and_ones(gamma_rate_num_lst, zeroes_lst, ones_lst, 0)
    gamma_num_binary = ''.join(gamma_num_lst)

    return gamma_num_binary


def max_zeroes_and_ones(gamma_rate_num_lst, zeroes_lst, ones_lst, i):
    
    if i == 12:
        print(gamma_rate_num_lst)
        return gamma_rate_num_lst

    
    if int(zeroes_lst[i]) > int(ones_lst[i]):
        gamma_rate_num_lst.append('0')

    else:
        gamma_rate_num_lst.append('1')
    i += 1

    max_zeroes_and_ones(gamma_rate_num_lst, zeroes_lst, ones_lst, i)

    return gamma_rate_num_lst


def get_epsilion_rate(gamma_num):
    epsilion_lst = []

    for num in gamma_num:
        if num == '0':
            epsilion_lst.append('1')
        else:
            epsilion_lst.append('0')
    
    epsilion_num_binary = ''.join(epsilion_lst)

    return epsilion_num_binary


def binary_to_decimal(binary):
     
   return int(binary, 2)


def find_power_consumption_rate(lst_diagnostic_report, zeroes, ones, i, zeroes_lst, ones_lst):

    for item in lst_diagnostic_report:

        # Base case
        # 12 is len of item in each line
        if i == 12:

            gamma_num_binary = get_gamma_rate(gamma_rate_num_lst, zeroes_lst, ones_lst)
            epsilion_num_binary = get_epsilion_rate(gamma_num_binary)

            gamma_num_decimal = binary_to_decimal(gamma_num_binary)
            epsilion_num_decimal = binary_to_decimal(epsilion_num_binary)

            # Power consumption rate
            return int(gamma_num_decimal) * int(epsilion_num_decimal)

        bit = item[i]

        if bit == '0':
            zeroes += 1

        else:
            ones += 1
    
    # Recursive case
    if i < len(item):
        i += 1
        zeroes_lst.append(zeroes)
        zeroes = 0
        ones_lst.append(ones)
        ones = 0
        gamma_num = find_power_consumption_rate(lst_diagnostic_report, zeroes, ones, i, zeroes_lst, ones_lst) 
        
    return gamma_num


if __name__ == '__main__':
    print(find_power_consumption_rate(lst_diagnostic_report, zeroes, ones, i, zeroes_lst, ones_lst))