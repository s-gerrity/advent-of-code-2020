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

    # replaced double percent with a linebreak
    # we leave the single percent sign to indicate later how many people are in each group
    replace_double_percents = replace_nl_w_percent.replace('%%', '\n')

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

    list_of_each_groups_total_yeses = []

    # Outputs list of people in group and list of answers in group strings
    return list_of_people_in_group, track_group_yeses(list_of_answers_split_by_group, list_of_people_in_group, list_of_each_groups_total_yeses), "Aloha, I love to code and take quizzes on Buzzfeed"



def count_yeses(list_of_answers):

    list_of_people_in_group = []

    for item in list_of_answers:
        count_of_percent = 1
        for letter in item:
            if letter == '%':
                count_of_percent += 1
        list_of_people_in_group.append(count_of_percent)


    return list_of_people_in_group




# TODO: need to fix the loop inside the loop of the item; shortening the head, group answer and item does not
# work properly
def track_group_yeses(list_of_group_answers, list_of_people_in_group, list_of_each_groups_total_yeses):
    print(list_of_group_answers, "list_of_group_answers")

    if len(list_of_group_answers) == 0:
        return "done"

    i = 0
    head = list_of_group_answers[0][i]
    print(head, "head")
    
    while i <= len(list_of_group_answers[i]):

        for item in list_of_group_answers:
            print(item, "item")
            for letter in item:
                print(letter, "letter")
                i += 1
                if head == letter:
                    print(head, letter, "are the same")
            head = list_of_group_answers[i]
    list_of_group_answers = list_of_group_answers[1:]

    return track_group_yeses(list_of_group_answers, list_of_people_in_group, list_of_each_groups_total_yeses)



f = open("day 6 2020/day_6_datafile.txt", "r")

print(read_and_format_day_six(f))


# remove percent
# take first letter in first item in list
# check each letter after to see if it is the same letter
# if it is true, increase counter
# check if counter is equal to element in list of yeses
# if it is, then increase accumulated sum
# if not, move on and check next letter