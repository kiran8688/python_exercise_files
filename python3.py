##### this is the code for the basic operations of file handiling and reading methods ######
##### this is also a 
anyfile = input("enter a file name: ")
afile = open(anyfile) #this is how an external file is been accessed
readfile = afile.read()
# print(afile)
counter = 0
for line in afile :
    line = line.rstrip() # this is used for wiping out the empty lines in the file
    if line :
        findtxt = readfile.find('Author', )
        counter = counter + 1
        print(findtxt)
    # if line.find('From:', ) :
        # line = afile.read()
    print(line)  #this is the for loop applied to an external file

print('there are (', counter, ') lines in the file')

# readaf = afile.read() #this is the read method of the file in the python
# print(readaf)
# print(readaf[14:40]) #this is the string conveyed as an array ***very imp*** ----slice method----

# print(len(readaf)) #this is how to find the length of the file by counting every letter as an index
# print(readaf.find("input", )) #this is to find index number of the perticular word or letter