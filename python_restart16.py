"""
Module for demonstrating Python iteration techniques and nested loops.
This module contains examples of various iteration patterns including:
- enumerate() for indexed iteration
- while loops with manual counter management
- for-else constructs for search operations
- continue and pass statements for loop control
- Nested for loops with performance timing
The nested for loops section (lines 40+) creates a 100x10000 iteration pattern,
printing zeros to demonstrate nested loop execution and measure the elapsed time
in seconds. This is a performance test that prints 100 rows of 10,000 zeros each,
followed by the total execution time rounded to 2 decimal places.
"""
# ---------------------------------------------------------------------------------------




# -----------------Different ways to iterate through a list-----------------
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
# for idx, desserts in enumerate(favorites):
#     print(idx , desserts)


# count = 0
# while count < len(favorites):
#     print(count, favorites[count])
#     count += 1


# for dessert in favorites:
#     if dessert == 'pudding':
#         print("Yes, One of My faviorite dessert is "+ dessert+ "!")
#         break
# else:
#         print("No sorry, that dessert is not on my list")

# for dessert in favorites:
#     if dessert == 'Churros':
#         continue
#     print('My Other faviorite dessert is '+ dessert+ '!')

# for dessert in favorites:
#     if dessert == 'Churros':
#         pass  # Placeholder for future code
#     print('My Other faviorite dessert is '+ dessert+ '!')

# ______________________________________________________________________________________

# -----------------Nested for loops-----------------
import time
start_time = time.time()

for i in range(100):
    for j in range(10000):
        print(0, end=' ')
    print()
print(round((time.time() - start_time), 2))


# ----------------------------------------------------------------------------------------
# a = isinstance(str, "aa") -- This will return False because the first argument should be an instance, not a type.

# print(a)
# _________________________________________________________________________________________
# a = isinstance( "aa", str) -- This will return True because "aa" is indeed an instance of the str class.

# print(a)
