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
        if plot in map[1]:
            spot = plot[3]

            if spot in '#':
                counter += 1
                
        # other rows 
        else:
            i += 3
            if i > 30:
                i = (int(i) % 30) -1
                spot = plot[i]
                
                if spot == '#':
                    counter += 1
                else:
                    continue
            else:
                spot = plot[i]
                if spot == '#':
                    counter += 1
                else:
                    continue
            
    return counter