# day 4



# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in"""


# def is_pid_valid(passport_dict):
#     pid_value = passport_dict['pid']

#     return len(pid_value) == 9
            

# def is_ecl_valid(passport_dict):
#     ecl_value = passport_dict['ecl']
#     list_of_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
#     return ecl_value in list_of_ecl


# def is_hcl_valid(passport_dict):
#     hcl_value = passport_dict['hcl']
#     hcl_num_start = hcl_value[0]
#     hcl_remaining = hcl_value[1:]
#     valid_chars = 'abcdef1234567890'
    
#     if hcl_num_start == '#'and len(hcl_remaining) == 6:
#         # print("YES")
#         for item in hcl_remaining:
#             # print("ITEM", item)
#             if item not in valid_chars:
#                 return print("INVALID 1")
#         return print("VALID YES")
#     return print("LEN WRONG")


# def is_hgt_valid(passport_dict):
#     hgt_metric = passport_dict['hgt'][-2:]
#     hgt_num = passport_dict['hgt'][:-2]
#     print(hgt_metric, hgt_num)
    
#     if len(passport_dict['hgt']) < 4:
#         return print(False, "4")
    
#     if hgt_metric != 'in' and hgt_metric != 'cm':
#         return False
    
#     if hgt_metric == 'cm':
#         if int(hgt_num) < 150 or int(hgt_num) > 193:
#             return print(False, "2")
#     if hgt_metric == 'in':
#         if int(hgt_num) < 59 or int(hgt_num) > 76:
#             return print(False, "3")
#     return True


# def is_eyr_valid(passport_dict):
#     eyr_value = passport_dict['eyr']
#     if int(eyr_value) >= 2020 and int(eyr_value) <= 2030:
#         return print("EYR True")
#     return print("Invalid EYR")
    

# def is_iyr_valid(passport_dict):
#     iyr_value = passport_dict['iyr']
    
#     if int(iyr_value) >= 2010 and int(iyr_value) <= 2020:
#         return print("IYR True")
#     return print("Invalid IYR")
    

# def is_byr_valid(passport_dict):
#     byr_value = passport_dict['byr']

#     if int(byr_value) >= 1920 and int(byr_value) <= 2002:
#         return print("BYR True")
#     return print("Invalid BYR")


# def is_valid_passport(passport_dict):
    
#     if 'cid' in passport_dict:
#         del passport_dict['cid']
    
#     if len(passport_dict) < 7:
#         return False
#     return True
    

# def process_passport_string(passport_string):
#     passport_dict = {}
#     passport_items_list = passport_string.split()
    
#     for item in passport_items_list:

#         data_pair = item.split(':')
#         passport_dict[data_pair[0]] = data_pair[1]
#         # print(passport_dict)
    
#     return passport_dict


# def process_batch_file(string):
#     passport_list = string.split('\n\n')
#     valid_passports = 0

#     for passport_string in passport_list:
#         passport_dict = process_passport_string(passport_string)
#         is_valid = is_valid_passport(passport_dict)
        
#         if is_valid == True:
#             valid_passports += 1
            
#     return print("TOTAL", valid_passports)
    
    
# process_batch_file(str_of_credentials)


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


# LASTEST



# str_of_credentials = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:19a7 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in"""



## PASSPORT DETAILS FUNCTIONS
#true, false (len), true, false (len)



def is_pid_valid(passport_dict):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid_value = passport_dict['pid']

    return len(pid_value) == 9
            

def is_ecl_valid(passport_dict):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    ecl_value = passport_dict['ecl']
    list_of_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    return ecl_value in list_of_ecl


def is_hcl_valid(passport_dict):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl_value = passport_dict['hcl']
    hcl_num_start = hcl_value[0]
    hcl_remaining = hcl_value[1:]
    valid_chars = 'abcdef1234567890'
    
    if hcl_num_start == '#'and len(hcl_remaining) == 6:
        for item in hcl_remaining:
            if item not in valid_chars:
                return print("INVALID 1")
        return print("VALID YES")
    return print("LEN WRONG")

#################################################################

def is_hgt_valid(passport_dict):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.

    hgt_metric = passport_dict['hgt'][-2:]
    hgt_num = passport_dict['hgt'][:-2]
    # print(hgt_metric, hgt_num)
    
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
    return print("Invalid EYR")


def is_iyr_valid(passport_dict):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr_value = passport_dict['iyr']
    
    if int(iyr_value) >= 2010 and int(iyr_value) <= 2020:
        return is_eyr_valid(passport_dict)
    return print("Invalid IYR")


def is_byr_valid(passport_dict):
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    byr_value = passport_dict['byr']
    
    #check to see if it's all integers
    valid_byr_value = is_valid_string(byr_value)
    
    if valid_byr_value == True:

        if int(byr_value) >= 1920 and int(byr_value) <= 2002:
            return is_iyr_valid(passport_dict)
    return print(False, "Invalid BYR")


### SUPPORTING FUNCTION


def is_valid_string(passport_value):
    
    for item in passport_value:
        if item not in '1234567890':
            return False

    return True
    


### MAIN FUNCTIONS


def is_valid_passport(passport_dict):
    
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
        # print(passport_dict)
    
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


str_of_credentials = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2018 cid:147 hgt:44in"""   
    
# First and starting function call to confirm passports
process_batch_file(str_of_credentials)


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





# functions set off other functions
# is_valid_passport triggers the first of all tests to confirm
# is_valid_passport collects and counts trues that come through
# trues are sent to process_batch_file and returned a total of trues
# all falses are ignored
