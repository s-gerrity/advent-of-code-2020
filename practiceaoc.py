# Day 6

# pseudocode
# split file by new line
# make into list
# remove duplicates in each index
# iterate through each index, iterate through each letter in the string
# if letter is in alphabet

# DESIRED OUTPUT ['abc', 'abc', 'abac', 'aaaa', 'b']

# regex to remove percents i added
# recursive

# make a counter to count each total and add to a list? return list in the end


f = open("day_6_datafile.txt", "r")


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


    return split_at_double

print(read_and_format_day_six(f))