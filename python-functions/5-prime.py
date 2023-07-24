#!/usr/bin/env python3
def is_prime(number):
    # is_prime = __import__("5-prime").is_prime
    if number < 2:
        return False
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return False
    else:
        return True
    return True


# print(is_prime(17))
# print(is_prime(15))
# print(is_prime(-5))
# print(is_prime(0))
