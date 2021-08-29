# ADVENT OF CODE 2020 #
# Final working solutions

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

