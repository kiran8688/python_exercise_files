##### THIS IS THE CODE FOR FINDING THE INDEX VALUE OF THE GIVEN STRING IN A FILE  #####
print("\n>   This file is coded for searching a \"string's index number\"\n")
anyfile = input("> enter the file name: ") 
afile = open(anyfile) #this is how an external file is been accessed
# print(afile)
readaf = afile.read() #this is the read method of the file in the python
find_str = readaf.find(input("> search for a string: ") , )
print('\n> the string you entered is found in the index number "', find_str, '"\n') #this is to find index number of the perticular word or letter