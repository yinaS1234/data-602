# 1. Function to calculate area and perimeter of a rectangle
def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# 2. Function to check if a number is even or not
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 3. Function to calculate number of upper and lower case letters
def count_case_letters(string):
    upper_cnt = sum(1 for char in string if char.isupper())
    lower_cnt = sum(1 for char in string if char.islower())
    return upper_cnt, lower_cnt
count_case_letters('Silly')


# 4. Function to sum all numbers in a list
def sum_list(num):
    return sum(num)

# 5. Example of global vs local variables
global_var = 10

def example_variables():
    local_var = 5
    print("global variable:", global_var)
    print("local variable:", local_var)

# 6. Function to multiply argument with an unknown given number
def multiply_with_unknown(argument):
    unknown_number = 5
    return argument * unknown_number




