"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False

    return True

def primes(number_of_primes):
    list = []
    while len(list) < int(number_of_primes):
        j = 2
        if check_prime(j):
            list.append(j)
        j = j + 1
    else:
        return list
        
    #return list
