import sys

def less_than(original, n):
    try:
        less = [i for i in original if i < n]
    except TypeError:
        print("Something seems to have gone wrong!")
        print("Please ensure first argument is a list, and second an integer")
        sys.exit(1)
    return less

original = [2,6,0,22,7,1,77]
n = 7

print(less_than(original, n))
