Hours = (input("Please enter the amount of hours worked\n"))
Rate = (input("Please enter the rate per hour in Rupees\n"))

try:
    hours_fin = float(Hours)
except:
    print("Please enter number in decimal format")
try:
    rate_fin = float(Rate)
except:
    print("Please enter rate in a decimal format")

try:
    if hours_fin > 40:
        amount = (40*rate_fin) + ((hours_fin-40)*rate_fin*1.5)
    else:
        amount = hours_fin*rate_fin

    print ("The amount you earned is", amount)

except:
    print("Please enter inputs in a decimal format")