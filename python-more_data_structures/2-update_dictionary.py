#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Update or add key/value in a dictionary"""
    a_dictionary[key] = value


my_dict = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e"}
key = "a"
value = "A"

new_dict = update_dictionary(my_dict, key, value)

# Print the updated dictionary and the old dictionary
print("Updated Dictionary:", new_dict)
print("Old Dictionary:", my_dict)
