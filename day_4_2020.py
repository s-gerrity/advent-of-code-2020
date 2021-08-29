# ADVENT OF CODE 2020 #
# Final working solutions

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


# PART 2 #####################


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def is_pid_valid(passport_dict):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid_value = passport_dict['pid']

    if len(pid_value) != 9:
        return print(False, "'pid' must have 9 characters.")

    string_validity = is_valid_string(pid_value, 'pid')
    if string_validity == True:
        return True
                    

def is_ecl_valid(passport_dict):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    ecl_value = passport_dict['ecl']
    list_of_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if ecl_value not in list_of_ecl:
        return print(False, "'ecl' needs to be one of ''amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth''")
    
    return is_pid_valid(passport_dict)


def is_hcl_valid(passport_dict):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl_value = passport_dict['hcl']
    hcl_num_start = hcl_value[0]
    hcl_remaining = hcl_value[1:]
    valid_chars = 'abcdef1234567890'
    
    if hcl_num_start == '#':
        if len(hcl_remaining) == 6:
            for item in hcl_remaining:
                if item not in valid_chars:
                    return print(False, "'hcl' has incorrect values. Must have exactly six characters 0-9 or a-f following the # symbol.")
            return is_ecl_valid(passport_dict)
        return print(False, "'hcl' is too short. The # symbol needs to be followed by exactly six characters 0-9 or a-f.")
    return print(False, "'hcl' needs to start with a # symbol.")


def is_hgt_valid(passport_dict):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.

    hgt_metric = passport_dict['hgt'][-2:]
    hgt_num = passport_dict['hgt'][:-2]
    
    if len(passport_dict['hgt']) < 4:
        return print(False, "'hgt' must have two numbers followed by unit 'cm' or 'in'.")
    
    if hgt_metric != 'in' and hgt_metric != 'cm':
        return print(False, "Height unit incorrect. 'hgt' needs to be inches or centemeters.")
    
    if hgt_metric == 'cm':
        if int(hgt_num) < 150 or int(hgt_num) > 193:
            return print(False, "Must have a height between 150cm and 193cm.")

    if hgt_metric == 'in':
        if int(hgt_num) < 59 or int(hgt_num) > 76:
            return print(False, "Must have a height between 59in and 76in.")

    return is_hcl_valid(passport_dict)


def is_eyr_valid(passport_dict):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr_value = passport_dict['eyr']

    if int(eyr_value) >= 2020 and int(eyr_value) <= 2030:
        return is_hgt_valid(passport_dict)
    return print(False, "'eyr' must be a year between 2019 and 2031.")


def is_iyr_valid(passport_dict):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr_value = passport_dict['iyr']
    
    if int(iyr_value) >= 2010 and int(iyr_value) <= 2020:
        return is_eyr_valid(passport_dict)
    return print(False, "'iyr' must be a year between 2009 and 2021.")


def is_byr_valid(passport_dict):
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    byr_value = passport_dict['byr']
    
    #check to see if the value is all integers
    string_validity = is_valid_string(byr_value, 'byr')
    
    if string_validity == True:

        if int(byr_value) >= 1920 and int(byr_value) <= 2002:
            return is_iyr_valid(passport_dict)
    return print(False, "'byr' must be a year between 1919 and 2003.")


### SUPPORTING FUNCTION


def is_valid_string(passport_value, key):
    
    for item in passport_value:
        if item not in '1234567890':
            return print(False, "Passport is not valid because the " + key + " : " + passport_value + " needs to have numerical characters.")

    return True
    

### MAIN FUNCTIONS


def is_valid_passport(passport_dict):
    
    #cid is an optional category, therefor no need to count it (delete it)
    if 'cid' in passport_dict:
        del passport_dict['cid']
    
    if len(passport_dict) == 7:
        #if any checks are not valid, will print False w error
        #if checks are all true, will send true back for a total count tally
        valid_passport = is_byr_valid(passport_dict)
        return valid_passport


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
            
    return print("TOTAL:", valid_passports)


# First and starting function call to confirm passports
# process_batch_file(str_of_credentials)
