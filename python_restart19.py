
"""
Module demonstrating tuple operations and characteristics in Python.
This module showcases various tuple functionalities including:
- Creating tuples with mixed data types
- Unpacking tuples
- Accessing elements by index
- Demonstrating tuple immutability
- Concatenating tuples
- Using tuple methods (count, index)
- Iterating through tuples with enumeration
"""


my_tuple = (1, 'hello', 3.14, True)

print(*my_tuple)  # Unpacking the tuple and printing its elements separated by spaces

print(my_tuple)  # Printing the tuple as a whole

# Tuples are immutable, so we cannot add or remove elements like we do with lists
# However, we can demonstrate accessing elements by index

print(my_tuple[1])  # Accessing the element at index 1

# Trying to modify the tuple will raise an error
# my_tuple[0] = 10  # This will raise a TypeError

# We can create a new tuple by concatenating existing tuples
new_tuple = my_tuple + (42, 'world')
print(new_tuple)  # Printing the new tuple

print(type(my_tuple))  # Printing the type of the tuple

print(my_tuple.count('hello'))  # Counting occurrences of 'hello' in the tuple

print(my_tuple.index(3.14))  # Finding the index of 3.14 in the tuple

for idx, i in enumerate(my_tuple):
    print(idx, i)  # Iterating through the tuple and printing each element with its index