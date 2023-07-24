#!/usr/bin/env python3
def is_prime(number):
    # is_prime = __import__("5-prime").is_prime
    prime_list = []
    deviders = range(1, 10)
    for i in deviders:
        calculation = bool(number / i)
        prime_list.append(calculation)
        print(prime_list)


print(is_prime(16))