# solution for chapter control flow,  task 1, variant D
attempt = 0
while attempt < 3:
    attempt += 1
    if input("Please enter password: >>>") == "SeCrEt":
        print("Correct")
        break
    print("Wrong")
else:
    print("You failed 3 times")
print("bye!")