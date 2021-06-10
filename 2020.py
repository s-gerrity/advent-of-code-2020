# ADVENT OF CODE 2020 #

# DAY 1
# Part 1

# <First way I solved the problem> 

def find_pair(nums):
    for num in nums:
        for numo in nums:
            new_var = num + numo
            if new_var == 2020:
                return print(f"{num} multiplied by {numo} equals {num * numo}!")

# <Second way I solved it is better bc runtime>

def find_pair(nums):           
    for num in nums:
        sub = 2020 - num
        if sub in nums:
            return print(f"{num} multiplied by {sub} equals {num * sub}!")


# Part 2

def three_adds(nums):
    for num in nums:
        for item in nums:
            small = 2020 - num - item
            if small in nums:
                return print(f"{num} multiplied by {item} and {small} equals {num * item * small}!")


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


# DAY 3
# Part 1 

def count_trees(map):
    map = map.split('\n')
    counter = 0
    i = 3

    for plot in map:
        
        # pass first row
        if plot in map[0]:
            continue
            
        # second row only
        if plot in map[1] and plot[3] == '#':
            counter += 1
                
        # other rows 
        else:
            i += 3
            if i > (len(plot)-1):
                i = (int(i) % (len(plot)-1)) -1
                
                if plot[i] == '#':
                    counter += 1

            else:
                if plot[i] == '#':
                    counter += 1
            
    return counter

# < Improved version of pt 1 >
def count_trees(map):
    map = map.split('\n')
    counter = 0
    i = 3

    # skip first row
    for plot in map[1:]:

        if plot[i] == '#':
            counter += 1
        i += 3

        if i > (len(plot)-1):
            i = (int(i) % (len(plot)-1)) -1

    return counter

# Part 2

def count_trees(map):
    map = map.split('\n')
    counter = 0
    # change i according to spaces moved right
    i = 3

    # skip first row
    for plot in map[1:]:

        if plot[i] == '#':
            counter += 1
        # change i according to spaces moved right
        i += 3

        if i > (len(plot)-1):
            i = (int(i) % (len(plot)-1)) -1

    return counter


# < right 1, down 2 >
def count_trees(map):
    map = map.split('\n')
    counter = 0
    i = 1

    for plot in map[2::2]:
        if plot[i] in '#0123456789':
            counter += 1
        i += 1
        if i > (len(plot)-1):
            i = (int(i) % (len(plot)-1)) -1
            
    return counter

# DAY 4 
# Part 1

def is_valid_passport(passport_dict):

    if len(passport_dict) == 8:
        return True
    if len(passport_dict) == 7 and 'cid' not in passport_dict:
        return True
    return False


def process_passport_string(passport_string):
    passport_dict = {}
    passport_items_list = passport_string.split() 

    for item in passport_items_list:

        data_pair = item.split(':')
        passport_dict[data_pair[0]] = data_pair[1]
    
    return passport_dict


def process_batch_file(string):
    passport_list = string.split('\n\n')
    valid_passports = 0

    for passport_string in passport_list:
        passport_dict = process_passport_string(passport_string)
        is_valid = is_valid_passport(passport_dict)
        
        if is_valid == True:
            valid_passports += 1
            
    return valid_passports
    
# process_batch_file(str_of_credentials)
