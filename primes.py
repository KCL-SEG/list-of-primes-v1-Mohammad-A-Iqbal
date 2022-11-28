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
    while len(list) < number_of_primes:
        i = 1
        if check_prime(i):
            list.append(i)
        i = i + 1
        
    return list
