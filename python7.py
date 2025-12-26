#####  this is the code for example of voters eligibility by entering a list of ages as an array using while loop  (using very modern list methods like max, min, sum, etc...)#####
serial_no = 0
avg_age = 0
junior = None
senior = 0
print("applications are open from here")
candidates = list() #declaring an empty list(array)
adultcand = list()
while True: #while loop for iterating the given array
    entcanli = input("enter the candidate's age: ")
    if entcanli != 'done' : ## imp condition *********
        try:
            intper = int(entcanli) ## imp conversion from str to int **************
        except:
            print('invalid age') ## filter the string  and  invalidate the object
            continue ## continue to the if cond in the while loop
        candidates.append(intper) ## very imp method for appending the object into a list (array)************
        
        continue #### continue to the if cond for the while loop
            #[10, 25, 45, 64, 'a', 12, 23, 43, 46, 'b', 13, 21, 75, 27, 57]
    for voter in candidates: ## for loop applied for iterating the filtered ages of the candidates(list)
        if voter < 18: ## below 18 not allowed
            print('candidate not eligible for voting \"please make sure you are atleast 18 years old\"')
        elif voter < 100: ## below 100 are allowed
            adultcand.append(voter) # this is a method of the list for inserting the object into the list
            serial_no = len(adultcand) # this is a method of the list for finding the length of the list
            avg_age = sum(adultcand)/len(adultcand) # this is a method of the list for finding the average of the list
            junior = min(adultcand) # this is a method of the list for inserting the object into the list
            senior = max(adultcand)
            # serial_no = serial_no + 1 # counter for number of voters
            # avg_age = avg_age + voter # logic for summation of average age of all voters
            # if voter > senior: #finding the senior voter
            #     senior = voter
            # elif junior is None: # converting junior in 'None' to the junior to an 'integer'
            #     junior = voter
            # elif voter < junior: # finding the junior voter
            #     junior = voter
            print( voter, "<-->", senior, "senior")
            print( voter, "<-->", junior, "junior")
        else: # condition for filtering ages greater than 100 years
            print('I think you are not a "human" or "eligible"')
    candidates.sort()
    print("\n>  these are the 'sorted list' of ages entered (before filter):\n\n>", candidates)
    print("\n> this is the raw data of the candidates list and the length of the list is: \'" , len(candidates), '\'\n')
    adultcand.sort()
    print("\n>  these are the 'sorted list' of ages entered (after filtering '<18' & '>100'):\n\n>", adultcand)
    print("\n> this is the filtered data of the candidates list and the length of the list(eliminating '<18' & '>100') is: \'" , len(adultcand), '\'\n')
    print("\n\n>", serial_no, "members by far\n>", junior, "is the junior candidate of the voters\n>", senior, "is the senior candidate of the voters \n>", int(avg_age), "is the average age of the voters",)
    quit() ### quiting the code helps break from code instead of reapeating the loop
    #  int(avg_age / serial_no) for finding the average of the list