"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def check_prime(num):
    for i in range(2,int(num/2)):
        if (num%i) == 0:
            return False
    return True

def primes(number_of_primes):
    list = []
    j = 2
    for i in range(number_of_primes):
        while not check_prime(j):
            j = j + 1
        else:
            list.append(j)

    return list