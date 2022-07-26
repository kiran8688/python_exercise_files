######   THIS IS A CODE FOR COUNTING LINES IN THE PARTICULAR FILE #####
print('\n   THIS IS A CODE FOR COUNTING LINES IN THE "PARTICULAR FILE"\n ')
anyfile = input('> enter the File name: ')
afile = open(anyfile) #this is how an external file is been accessed
print(afile)
counter = 0
for line in afile :  #this is the for loop applied to an external file
    counter = counter + 1
print('\n> lines in the file: "', counter, '"\n')