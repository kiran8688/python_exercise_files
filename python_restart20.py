"""Module demonstrating set operations and methods in Python."""
"""
Module demonstrating set operations and methods in Python.
Sets are unordered collections of unique elements in Python. They are useful for:
- Storing unique values (duplicates are automatically removed)
- Performing mathematical set operations like union, intersection, and difference
- Checking membership efficiently
- Removing duplicates from sequences
Key characteristics of sets:
- Unordered: Elements have no defined order
- Mutable: Can add or remove elements after creation
- Unindexed: Cannot access elements by index
- No duplicates: Only unique elements are stored
- Heterogeneous: Can contain different data types
Common set operations:
- union(): Combines all elements from both sets
- intersection(): Returns common elements between sets
- difference(): Returns elements in first set but not in second
- symmetric_difference(): Returns elements in either set but not in both
- issubset(): Checks if one set is contained in another
- issuperset(): Checks if a set contains another set
- isdisjoint(): Checks if two sets have no common elements
Methods for modifying sets:
- add(): Adds a single element
- remove(): Removes an element (raises error if not found)
- discard(): Removes an element (no error if not found)
- pop(): Removes and returns an arbitrary element
- clear(): Removes all elements
"""
set_a = {1, 2, 3, 4, 5}

# print(*set_a)  # Unpacking the set and printing its elements separated by spaces
# print(len(set_a))  # Printing the length of the set
# set_a.add(6)  # Adding an element to the set
# print(set_a)

# set_a.remove(3)  # Removing an element from the set
# print(set_a)

# set_a.discard(1)  # Discarding an element (no error if not found)
# print(set_a)

set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b))  # Union of two sets
print(set_a | set_b)  # Another way to get the union of two sets


print(set_a.intersection(set_b))  # Intersection of two sets
print(set_a & set_b)  # Another way to get the intersection of two sets

print(set_a.difference(set_b))  # Difference of two sets
print(set_a - set_b)  # Another way to get the difference of two sets

print(set_a.symmetric_difference(set_b))  # Symmetric difference of two sets
print(set_a ^ set_b)  # Another way to get the symmetric difference of two sets

print(set_a.issubset(set_b))  # Check if set_a is a subset of set_b
print(set_a.issuperset(set_b))  # Check if set_a is a superset of set_b
print(set_a.isdisjoint(set_b))  # Check if set_a and set_b are disjoint
for idx, i in enumerate(set_a):
    print(idx, i)  # Iterating through the set and printing each element with its index

print(type(set_a))  # Printing the type of the set

