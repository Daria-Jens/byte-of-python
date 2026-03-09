# solution for chapter control flow,  task 1, variant B
for _ in range(3):
    if input("Please enter password: >>>") == "SeCrEt":
        print("Correct")
        break
    print("Wrong")
else:
    print("You failed 3 times")
print("bye!")