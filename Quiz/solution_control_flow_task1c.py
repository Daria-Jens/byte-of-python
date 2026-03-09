# solution for chapter control flow,  task 1, variant C
attempt = 1
max_attempts = 3
valid_password = "SeCrEt"
while True:
    print(f"this is attempt {attempt} of {max_attempts}")
    text = input("Please enter password: >>>")
    if text == valid_password:
        print("Correct")
        break
    else:
        print("Wrong")
    attempt += 1
    if attempt > 3:
        print("You failed 3 times")
        break
print("bye!")