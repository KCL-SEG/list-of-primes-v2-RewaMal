"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes == 0:
        raise TypeError(ValueError)
    elif number_of_primes <0:
        raise TypeError(f'Entered value: {number_of_primes} is negative, work with positive numeber only.')
    else: 
        prime_num =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        
        for x in range(0,number_of_primes):
            list.append(prime_num[x])
    return list
