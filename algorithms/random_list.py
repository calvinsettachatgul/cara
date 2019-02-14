import random
# print(random.randint(0,10))
# for i in range(10):
#     print(i)
def random_list():
    result_list = []
    for i in range(10):
        randnum = random.randint(0,10)
        result_list.append(randnum)
    return result_list

print(random_list()) # returns a random list