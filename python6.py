print("\n>   This file is coded for searching a \"lines by a starting string \"\n")
anyfile = input("> enter the file name: ")
try : # try the code in the loop
    afile = open(anyfile) #this is how an external file is been accessed

except : # helpful for handling the errors 'its super useful'
    print('\n\tThe file your searched for, is not available at the moment\n')
    quit()
# print(afile)
# counter = 0
search_txt = input('> enter the string: ')
print(search_txt)
counter = 0
for line in afile : # for loop in the file for iterating each line starting with the 'search_txt'
    line = line.rstrip() # this is used for removing the empty lines in the output
    search_str = line.startswith(search_txt) # this is important for the search for the lines starts with the given string in params
    if search_str is True :
        counter = counter + 1
        # print(counter, line)
print('\n> there are "', counter, '" lines starting with your given string "', search_txt, '"\n')
confirm_txt = input('this may be a huge list "if you need it press (y / n)": ') # confirmation for displaying the whole sheet of matching results
confirm = str(confirm_txt) 
# print(confirm)
if confirm == "y" :
    afile = open(anyfile) #this is how an external file is been accessed
    counter = 0
    for line in afile :  # for loop in the file for iterating each line starting with the 'search_txt'
        line = line.rstrip() # this is used for removing the empty lines in the output
        search_str = line.startswith(search_txt) # this is important for the search for the lines starts with the given string in params
        if search_str is True :
            counter = counter + 1
            print(counter, line)
else :
    print('\n\t\t"Thank You " for saving lot of space and time\n')