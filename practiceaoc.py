# Day 6

# pseudocode
# 





def read_and_format_day_six(file_of_group_customs_answers):
    # displays as is
    list_of_group_customs_answers = file_of_group_customs_answers.read() 

    # makes into long string with %% for newline w break and % for nextline
    replace_nl_w_percent = list_of_group_customs_answers.replace('\n', '%') 

    # replaced double percent with a linebreak
    replace_double_percents = replace_nl_w_percent.replace('%%', '\n')

    # remove single percentsß
    no_percents = replace_double_percents.replace('%', '')

    # convert from string to list
    split_at_double = no_percents.split('\n')

    list_of_yes_totals = []

    return split_at_double


    # return count_yeses(split_at_double, list_of_yes_totals)


# def count_yeses(list_of_answers, list_of_yes_totals):

    

#     for item in list_of_answers:
#         # print(item, "item1")
#         letters_in_string = []

#         for letter in item:
#             if letter not in letters_in_string:
#                 letters_in_string.append(letter)
#         # print(letters_in_string, "letters_in_string")
#         list_of_yes_totals.append(len(letters_in_string))

#     return sum_list_of_yeses(list_of_yes_totals, 0)

# def sum_list_of_yeses(list_of_yes_totals, accumulated_sum):

#     if len(list_of_yes_totals) == 0:
#         return accumulated_sum
#     else:

#         head = list_of_yes_totals[0]
#         # print(head, "head")
#         accumulated_sum += int(head)
#         # print(accumulated_sum, "accumulated_sum")
        
#         list_of_yes_totals = list_of_yes_totals[1:]

#     return sum_list_of_yeses(list_of_yes_totals, accumulated_sum)




f = open("day_6_datafile.txt", "r")

print(read_and_format_day_six(f))