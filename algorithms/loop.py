def loop_recurse(arr, ind =0):
    # closure_variable
    # base case
    if ind >= len(arr):
        print('this is base case')
        return
    # recursive case
    else:
        if ind == 0:
            closure_variable = {"even": 0, "odd": 0}
        print("this is the recurive case ind {}".format(ind))
        print(arr[ind])
        # if arr[ind] % 2 == 0:
        #     closure_variable["even"] = closure_variable["even"] + 1
        # else:
        #     closure_variable["odd"] = closure_variable["odd"] + 1
        # print("closure_variable {}".format(closure_variable))
        ind += 1
        loop_recurse(arr, ind)
        
loop_recurse([1,2,3, 3, 4, 5])

''' 
ind = 3 returns through each function call. Total of 3 times
ind = 2 calls with loop_recurse(arr, 2)
    ind = 1 calls with loop_recurse(arr, 1)
            ind = 0 calls with loop_recurse(arr, 0)
            
ind = 0 calls with loop_recurse(arr, 0)
    ind = 1 calls with loop_recurse(arr, 1)
        ind = 2 calls with loop_recurse(arr, 2)
            ind = 3 returns
        ind = 2 returns # do we return this first? this will execute print(arr[2]) so this gets executed last?
    ind = 1 returns
ind = 0 returns
        




'''