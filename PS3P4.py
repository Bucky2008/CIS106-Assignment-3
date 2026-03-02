#input phase
make = input("Enter car make:")
model = input("Enter car model:")
msrp = float(input("Enter MSRP amount:"))
discount = float(input("Enter discount amount percent (as decimal):"))

#process phase
amount_off = msrp * discount
discounted_price = msrp - amount_off

#ouput phase
print("Make:",make)
print("Model:",model)
print("MSRP:",msrp)
print("Discount percent:",discount)
print("Amount off:",amount_off)
print("Discounted price:",discounted_price)