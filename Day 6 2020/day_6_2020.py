# Day 6
# Part 1

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

    return count_yeses(split_at_double, list_of_yes_totals)

# Add totals of unique characters from each item in the list to a new list
def count_yeses(list_of_answers, list_of_yes_totals): 

    # Look at the first item in the list and make a new list to save its unique characters
    for item in list_of_answers:
        letters_in_string = []

        for letter in item:
            if letter not in letters_in_string:
                letters_in_string.append(letter)

        list_of_yes_totals.append(len(letters_in_string))

    return sum_list_of_yeses(list_of_yes_totals, 0)


# Recursively sum each items total to the next
def sum_list_of_yeses(list_of_yes_totals, accumulated_sum):
    # Base case
    # When the list is empty we return the sum
    if len(list_of_yes_totals) == 0:
        return accumulated_sum

    # Recursive case
    # Sum the first item in the list and shrink list for recursion
    else:

        head = list_of_yes_totals[0]
        accumulated_sum += int(head)
        
        list_of_yes_totals = list_of_yes_totals[1:]

    return sum_list_of_yeses(list_of_yes_totals, accumulated_sum)


f = open("day_6_datafile.txt", "r")

print(read_and_format_day_six(f))


# Day 6
# Part 2


def count_unaminous_answers_in_groups(textfile):

    answers = 0
    # reads the file and splits at empty lines to form "groups" of data
    for group in f.read().split("\n\n"):
        
        # set.interesection takes two sets and compares them to each other, outputting 
        # into a set the data that is the same in both
        # each response in the group is divided by a new line
        # we loop through each response in the group and if every response has the
        # same character, it is added to the same_answers set
        same_answers = set.intersection(*[set(char) for char in group.split("\n")])
        
        # in this instance, len counts how many answers each group all picked
        # add them together for a running total 
        answers += len(same_answers)
        
    return '> Part two: {}'.format(answers)


f = open("day_6_datafile.txt", "r")

print(count_unaminous_answers_in_groups(f))