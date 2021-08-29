# ADVENT OF CODE 2020 #
# Final working solutions

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
