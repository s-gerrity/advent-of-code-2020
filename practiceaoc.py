# Day 6

# pseudocode
# for item in list [abc]
# get len of item - 1
# add the len to a new list
# loop through list of string (like part 1) and check if the letter is in the list as many times as the nums list


# 
# 


# DESIRED OUTCOME 
[
 [['abc']], 
 [['a'], ['b'], ['c']], 
 [['ab'], ['ac']], 
 [['a'], ['a'], ['a'], ['a']], 
 [['b']]
]



def read_and_format_day_six(file_of_group_customs_answers):
    # displays as is
    list_of_group_customs_answers = file_of_group_customs_answers.read() 

    # makes into long string with %% for newline w break and % for nextline
    replace_nl_w_percent = list_of_group_customs_answers.replace('\n', '%') 
    # print(replace_nl_w_percent)

    # replaced double percent with a linebreak
    # we leave the single percent sign to indicate later how many people are
    # in each group
    replace_double_percents = replace_nl_w_percent.replace('%%', '\n')
    

    # remove single percents
    # no_percents = replace_double_percents.replace('%', '')

    # convert from string to list
    split_at_double = replace_double_percents.split('\n')

    # KEEP: Call the count yeses function w `split at double` to create list of ints
    list_of_people_in_group = count_yeses(split_at_double)

    # Remove percents from answers; saves as one long string inside a list though
    condensed_list_of_string_answers = replace_double_percents.replace('%', '')

    # Splits each group into list elements
    list_of_answers_split_by_group = condensed_list_of_string_answers.split('\n')

    # TODO: Create function call that takes in count of people in group, accumulated sum, and the answers; loop over
    # answers, if a letter appears more than once, increase a counter; if that counter is equal to count of people in
    # group, sum that amount to accumulated sum

    return list_of_people_in_group, list_of_answers_split_by_group, "Aloha, I love to code and take quizzes on Buzzfeed"



def count_yeses(list_of_answers):

    list_of_people_in_group = []

    for item in list_of_answers:
        count_of_percent = 1
        for letter in item:
            if letter == '%':
                count_of_percent += 1
        list_of_people_in_group.append(count_of_percent)


    return list_of_people_in_group





# def track_group_yeses(list_of_group_answers):
# # consider recursively going through the items in the list to track how many times the 
# # answer has been responded to by everyone in the group
# # maybe make a list to add the totals to
# # when the one list is at 0 then call to sum
# # 

#     for item in list_of_group_answers:
#         head = item[0]
#         print(head, "head")
#         rest = item[1:]
#         for letter in rest:
#             if letter == head:
#                 print("letter equals head")

    
    
#     return track_group_yeses()

# print(track_group_yeses([
# #  [['abc']], 
#  [['a'], ['b'], ['c']], 
# #  [['ab'], ['ac']], 
#  [['a'], ['a'], ['a'], ['a']], 
#  [['b']]
# ]))


f = open("day 6 2020/day_6_datafile.txt", "r")

print(read_and_format_day_six(f))


# remove percent
# take first letter in first item in list
# check each letter after to see if it is the same letter
# if it is true, increase counter
# check if counter is equal to element in list of yeses
# if it is, then increase accumulated sum
# if not, move on and check next letter