def count(num):
    if( num == None):
        return 0
    sum = 0
    number_range = range(1, num +1)
    for number in number_range:
        sum = sum + number
    # if num == 1:
    #     return 1
    # elif num == 2:
    #     return 3
    return sum