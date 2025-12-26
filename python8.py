entfile = input('> enter the file name: ')
try:
    openfile = open(entfile)
except:
    print("\nfile entered is not available\n")
    quit()
entstr = input('> enter the string of a line starts with: ')
print(entstr)
try:
    split_index = int(input('> enter the index number for splited line: '))
    try:
        confirm_word_split = input(
            '> Do you want to "split the string (y / n)": ')
        if confirm_word_split == "y":
            split_word = (
                input('> enter how do you want to split by character: '))
            word_split_I = int(
                input('> enter the word split index number for access: '))
        else:
            print('you have opted no for spliting the string')
            word_split_I = -1
    except:
        print('> You\'ve entered an invalid word split Index number')
        quit()
except:
    print('> You\'ve entered an invalid Index number')
    quit()
# print(type(split_index))
counter = 0
for line in openfile:
    line = line.rstrip()
    startwith = line.startswith(entstr)
    if startwith is True:
        counter = counter + 1
print('\n> there are "', counter,
      '" lines starting with your given string "', entstr, '"\n')
# confirmation for displaying the whole sheet of matching results
confirm_txt = input(
    '> this may be a huge list "if you need it press (y / n)": ')
confirm = str(confirm_txt)
# print(confirm)
if confirm == "y":
    openfile = open(entfile)  # this is how an external file is been accessed
    counter = 0
    for line in openfile:  # for loop in the file for iterating each line starting with the 'search_txt'
        line = line.rstrip()  # this is used for removing the empty lines in the output
        startwith = line.startswith(entstr)
        # splitlist = startwith.split()
        if startwith is True:
            counter = counter + 1
            # print(counter)
            splitline = line.split()
            # try:
            if len(splitline) >= 0:
                line_split = splitline[split_index]
                print(counter, " --> ", line_split)
                if confirm_word_split == 'y':
                    word_split = line_split.split(split_word)
                    if word_split_I > 0:
                        word_split_ed = word_split[word_split_I]
                        print(counter, " --> ", word_split_ed)
                        continue
                    # elif word_split_ed <= 0:
                    #     print(counter, 'blank')
                continue
            # except :
            #     print(counter ,"0")
            #     continue
