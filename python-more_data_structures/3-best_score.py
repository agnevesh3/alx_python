#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    # Initialize variables to keep track of the maximum score and its corresponding key
    max_score = None
    max_key = None

    for key, value in a_dictionary.items():
        if isinstance(value, int):  # Check if the value is an integer
            if max_score is None or value > max_score:
                max_score = value
                max_key = key

    return max_key
