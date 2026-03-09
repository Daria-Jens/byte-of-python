# problem control flow task 14 B
# password creation

while True:
    print("type 'help' to display a help text")
    command = input("please enter a new password >>>")
    if command == "help":
        print("The password must have: ")
        print("At least one digit (0-9) ")
        print("At least one lower-case character (a-z)")
        continue
    # test the password

    for char in "abcdefghijklmnopqrstuvwxyz":
        if char in command:
            break
    else:
        print("no lowercase character (a-z) found. please try again")
        continue

    for number in "0123456789":
        if number in command:
            break
    else:
        print("no digit (0-9) found. please try again")
        continue
    print("Congratulation, your password is accepted")
    break
print("bye bye")