age = int(input('Enter your age '))
full_price = 6.00

if age < 16:
    print("ticket cost is %.2f" %(full_price/2))
elif age > 16 and age < 60:
    print("ticket cost is %.2f" %(full_price))
else:
    print("ticket cost is %.2f" %(full_price/3))




