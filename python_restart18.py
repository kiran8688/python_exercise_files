list1 = [1, 2, 3, 4, 5]

print(*list1)# Unpacking the list and printing its elements separated by spaces

print (list1, sep=" ")# Printing the list as a whole, sep parameter has no effect here

list1.insert(len(list1), 10)# Inserting 10 at the end of the list
print(list1)

list1.append(6)# Appending 6 to the end of the list
print(list1)

list1.extend([7, 8, 9])# Extending the list by adding multiple elements
print(list1)

list1.pop(4)# Removing the element at index 4
print(list1)

del list1[2]# Deleting the element at index 2
print(list1)