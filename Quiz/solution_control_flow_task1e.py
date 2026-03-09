# solution for chapter control flow,  task 1, variant E
attempt = 1
while input("Please enter password: >>>") != "SeCrEt":
    print("wrong")
    attempt += 1
    if attempt > 3:
        print("You failed 3 times")
        break
else:
    print("correct")
print("bye!")