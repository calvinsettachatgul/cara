# https://www.codewars.com/kata/create-phone-number/train/python

'''
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parentheses!
'''

# TODO: create a test file
def create_phone_number(num_list):
    num_str_list = list(map(str, num_list))
    delimiter = ""
    area_code = delimiter.join(num_str_list[0:3])
    num_part1 = delimiter.join(num_str_list[3:6])
    num_part2 = delimiter.join(num_str_list[6:])
    return "({}) {}-{}".format(area_code, num_part1, num_part2)
