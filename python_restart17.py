def calculate_tax(bill, tax_rate):
    """Calculate the tax for a given bill amount and tax rate."""
    return (bill * tax_rate)/ 100
# input_bill = 30244
# imput_tax_rate = 12
# tax = calculate_tax(input_bill, imput_tax_rate)
# print(f"The calculated tax is: {tax}")
print(calculate_tax(40233, 12))