Hours = float(input("Please enter the amount of hours worked\n"))
Rate = float(input("Please enter the rate per hour in Rupees\n"))
if Hours > 40:
    amount = (40*Rate) + ((Hours-40)*Rate*1.5)
else:
    amount = Hours*Rate

print ("The amount you earned is", amount)