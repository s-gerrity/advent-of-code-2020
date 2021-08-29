# ADVENT OF CODE 2020 #
# Final working solutions

# DAY 2
# Part 1

def make_list(pwords):
    valid_counter = 0
    pwords = pwords.replace('-', ' ').replace(':', '').split('\n')
    pwords = [i.split(' ') for i in pwords]
    
    for item in pwords:
        letter_counter = 0
        minim = int(item[0])
        maxim = int(item[1])
        special = item[2]
        word = item[3]

        for letter in word:
            if letter is special:
                 letter_counter += 1

        if letter_counter >= minim and letter_counter <= maxim:
            valid_counter += 1
            
    return valid_counter


# Part 2

def validate_list(pwords):
    valid_counter = 0
    pwords = pwords.replace('-', ' ').replace(':', '').split('\n')
    pwords = [i.split(' ') for i in pwords]
    
    for item in pwords:
        f = (int(item[0]) -1)
        s = (int(item[1]) -1)
        special = item[2]
        word = item[3]

        if word[f] is special and word[s] is special:
            continue
        if word[f] is special and not word[s] is special:
            valid_counter += 1
        if word[f] is not special and word[s] is special:
            valid_counter += 1
        if word[f] is not special and word[s] is not special:
            continue
            
    return valid_counter