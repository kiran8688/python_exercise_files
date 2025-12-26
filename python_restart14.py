'''current = False

if current:
    current = False
    print('turning lights off')
if not current:
    current = True
    print('turning lights on')'''

loyal_customer = True
total_bill = 124

if loyal_customer and total_bill > 100:
    discount = 20
    total_bill = total_bill - (float(total_bill) / 100) * discount
    print("Loyal customer discount applied.")
elif total_bill > 100:
    discount = 10
    total_bill = total_bill - (float(total_bill) / 100) * discount
    print("Regular customer discount applied.")
else:
    print("Sorry No discount applied.")

print("Total Bill:", float(total_bill))