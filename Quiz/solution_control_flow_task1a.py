# solution for chapter control flow,  task 1, variant A
for a in range(3):
    text = input("Please enter password: >>>")
    if text == "SeCrEt":
        print("Correct")
        break
    else:   
        print("Wrong")
else:
    print("You failed 3 times")
print("bye!")
