#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n in {0}:
        return []  # Return an empty list if n is  0
    if n in {1}:
        return [0]  # Return an list if n is 1, this list just contain 1 element

    # Create a list to store Fibonacci sequence
    fib_seq = [0, 1]

    for i in range(2, n):
        # Calculate the next Fibonacci number and append it to the list
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)
    return fib_seq


# Test the function
# print(fibonacci_sequence(6))
# print(fibonacci_sequence(6))
# print(fibonacci_sequence(0))
# print(fibonacci_sequence(20))
