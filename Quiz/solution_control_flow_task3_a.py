#solution chapter control flow task 3 variant A
income = input("please enter your monthly (netto) income in €")
income = int(income)
if income < 1000:
    print("you do not earn much...")
elif income < 2000:
    print("it could be better....")
elif income < 3000:
    print("nice")
elif income < 4000:
    print("very nice")
elif income < 5000:
    print("fantastic")
else:
    print("really??")
