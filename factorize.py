def factorize(n):
    def is_prime(k):
        for j in range(2,k-1):
            if k % j == 0: #True if divisable
                return False #not a prime, return False
        return True #completes loop; return True for prime

    if is_prime(n): #if n is prime
        return [n] #only element, return in list
    else: #otherwise
        primes = [] #generate list
        for i in range(2, n): #for all numbers to n
            if is_prime(i): #if prime
                primes.append(i) #add to list

    factors = [] #empty list
    for i in primes: #for each prime
        while n % i == 0: #while divisable
            factors.append(i) #add factors
            n = n / i #divide
            if n == 1: #if completed division
                break #stop loop
    return factors #return list

factors = factorize(240880) #test
print(factors)
