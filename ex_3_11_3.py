score = float(input('Please enter your grade:\n'))
if score>=0 and score<=1:
    if score>=0.9:
        print ('A')
    if score>=0.8:
        print('B')
    elif score>=0.7:
        print('C')
    if score>=0.6:
        print ('D')
    else:
        print("F")
else:
    print("Enter grades between 0 and 1")