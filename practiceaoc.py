# Day 6

# pseudocode
# for item in list [abc]
# get len of item - 1
# add the len to a new list
# loop through list of string (like part 1) and check if the letter is in the list as many times as the nums list


# for letter in word
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

    # replaced double percent with a linebreak
    replace_double_percents = replace_nl_w_percent.replace('%%', '\n')

    # remove single percentsß
    no_percents = replace_double_percents.replace('%', '')

    # convert from string to list
    split_at_double = no_percents.split('\n')

    list_of_yes_totals = []

    return split_at_double


    # return count_yeses(split_at_double, list_of_yes_totals)


def track_group_yeses(list_of_group_answers):
# consider recursively going through the items in the list to track how many times the 
# answer has been responded to by everyone in the group
# maybe make a list to add the totals to
# when the one list is at 0 then call to sum
# 

    for item in list_of_group_answers:
        head = item[0]
        print(head, "head")
        rest = item[1:]
        for letter in rest:
            if letter == head:
                print("letter equals head")

    
    
    return track_group_yeses()

print(track_group_yeses([
#  [['abc']], 
 [['a'], ['b'], ['c']], 
#  [['ab'], ['ac']], 
 [['a'], ['a'], ['a'], ['a']], 
 [['b']]
]))


f = open("day 6 2020/day_6_datafile.txt", "r")

print(read_and_format_day_six(f))