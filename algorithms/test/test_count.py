from count import count

# sum up all the numbers from 1 to input_num
# if its less than 1 then return 0


def test_input_0():
    '''testing input 0'''
    assert count(0) == 0
    
def test_input_None():
    '''testing input None'''
    assert count(None) == 0
    
def test_input_1():
    '''testing input 1'''
    assert count(1) == 1
    
def test_input_2():
    '''testing input 2'''
    assert count(2) == 3
    
def test_input_5():
    '''testing input 2'''
    assert count(5) == 15
    
def test_input_neg3():
    '''testing input 2'''
    assert count(-3) == 0
    
'''
count(-1) => 0
count(None) => 0
count(0) => 0
count(1) => 1
count(2) => 3
count(3) => 6
count(4) => 10
count(5) => 15
'''
'''
from sample import func

def test_answer():
    assert func(3) == 5

'''