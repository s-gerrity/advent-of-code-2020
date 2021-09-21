def track_group_yeses(list_of_group_answers, list_of_people_in_group, list_of_each_groups_total_yeses):
# consider recursively going through the items in the list to track how many times the 
# answer has been responded to by everyone in the group
# maybe make a list to add the totals to
# when the one list is at 0 then call to sum
    print(list_of_group_answers, "list_of_group_answers")

    if len(list_of_group_answers) == 0:
        return "done"

    
    k_loop_through_each_letter = 0
    j_count_each_letter_occurance = 1
    sum_group_yes = 0
    
    # grab first element in the list of answers
    for item in list_of_group_answers: # abcdeabklpme
        print(item, "item")
        i_count_for_looping_each_group = 0

        # keep looping over the letters in the element until every char has been checked
        while i_count_for_looping_each_group < len(item): # 0 <= 12
            print(i_count_for_looping_each_group, "i_count_for_looping_each_group 1")

            # take the first letter in the answers 
            head = item[k_loop_through_each_letter] # a
            print(head, "head")
            
            # check the rest of the groups answers; we don't want to include the index
            # we're already on
            group_answers = item[k_loop_through_each_letter+1:] # bcdeabklpme
            print(group_answers, "group_answers")
        
            # loop over each letter in the group answers
            for letter in group_answers: # b, c, d, etc
                print(letter, "letter")

                i_count_for_looping_each_group += 1
                print(i_count_for_looping_each_group, "i_count_for_looping_each_group 2")

                # check if the head is the same as another letter in the group answers
                if head == letter: # a == b, a == c, etc
                    print(head, letter, "they're the same")

            
                    # if the answer is the same as the head, increase a counter (it starts at 1)
                    j_count_each_letter_occurance += 1 # 1 + 1 = 2
                    # goes on to check the next letter in the group answers
                    print(j_count_each_letter_occurance, "j_count_each_letter_occurance")

                # if the total count of letter occurances is the same amount as members in the group
                if int(j_count_each_letter_occurance) == int(list_of_people_in_group[0]):

                    # increase the counter
                    sum_group_yes += 1
                    print(sum_group_yes, "sum_group_yes")

            k_loop_through_each_letter += 1
            print(k_loop_through_each_letter, "k_loop_through_each_letter")
        
            
            # when the head has checked each letter in the group, add the total 
            list_of_group_answers = list_of_group_answers[1:2]

    
    return track_group_yeses(list_of_group_answers, list_of_people_in_group, list_of_each_groups_total_yeses)
