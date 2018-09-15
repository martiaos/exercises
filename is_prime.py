from math import sqrt

def is_prime(n):
    ''' Returns True if the positive integer n is prime, else False '''
    if not isinstance(n, int):
        raise ValueError("Expected int: {}".format(type(n)))
    elif n < 0:
        raise ValueError("Expected positive int: {}".format(n))
    elif n in [1, 2]:
        return True
    for i in range(2, round(sqrt(n))+1):
        if n%i == 0:
            return False

    return True

for i in range(30):
    print(i, is_prime(i))
