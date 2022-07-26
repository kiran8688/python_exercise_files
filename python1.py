#### this is the basic code for validating the age by the given input #####
 
x = input("enter your name: ")
y = input("enter your age: ")

if x == None:
    z = print("invalid name provided by the user")
    print(z)
elif int(y) <= 18:
    z = print("users of age below 18years are not allaowed")
    print(z)
else:
    z = print("My name is", x, end=', '), print("And Iam ", y, "years old.", ) # concatinating the x and y with the custom print
    print(z)