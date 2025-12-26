bill_total = 224

discount1 = 10

discount2 = 20

if bill_total > 100 and bill_total <= 200:
    print("bill total is greater than 100")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("bill total is greater than 200")
    bill_total = bill_total - discount2
else:
    print("bill total is less than or equal to 100")

print("Final bill total is:" + str(bill_total))

