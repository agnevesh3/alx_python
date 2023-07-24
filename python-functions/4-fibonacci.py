#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n in {0, 1}:
        return [n]  # Return a list with a single element if n is 0 or 1

    # Create a list to store Fibonacci sequence
    fib_seq = [0, 1]

    for i in range(2, n):
        # Calculate the next Fibonacci number and append it to the list
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)

    return fib_seq


# Test the function
# print(fibonacci_sequence(6))
# print(fibonacci_sequence(1))
# print(fibonacci_sequence(0))
# print(fibonacci_sequence(20))
