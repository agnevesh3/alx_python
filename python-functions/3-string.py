#!/usr/bin/env python3
def reverse_string(string):
    # reverse_string = __import__('3-string').reverse_string
    reverse_string = string[::-1]
    return reverse_string


print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))
