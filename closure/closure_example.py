# closure example

# def make_adder_of(count):
#     def adder(x):
#         print("before {}".format(count))
#         count + x
#         print("after {}".format(count))
#     return add_one
    
# add1 = make_adder_of(1)
# add2 = make_adder_of(2)
# add5 = make_adder_of(5)

# print(add5(4))

# my_adder()
# my_adder()
# my_adder()

def adder(count):
    count
    def addOne():
        print("before {}".format(count))
        nonlocal count
        count = count + 1
        print("after {}".format(count))
    return addOne

adderA = adder(0)
adderA()
adderA()
adderA()
adderB = adder(0)

def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        # msg = msg + " and goodbye"
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))
