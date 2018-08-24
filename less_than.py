import sys #allows for sys.exit

def less_than(original, n): #def function
    try: #try to make list directly
        less = [i for i in original if i < n]
    except TypeError: #if not list or int
        print("Something seems to have gone wrong!") #print message
        print("Please ensure first argument is a list, and second an integer")
        sys.exit(1) #exit
    return less #otherwise return list

original = [2,6,0,22,7,1,77]
n = 7

print(less_than(original, n)) #function call
