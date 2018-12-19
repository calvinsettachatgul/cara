from create_phone import create_phone_number

# sum up all the numbers from 1 to input_num
# if its less than 1 then return 0


def test_create_phone():
    '''create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890" '''
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    
