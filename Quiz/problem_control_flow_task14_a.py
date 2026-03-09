# problem control flow task 14 A
while True:
    print("What is the answer to THE question?")
    print("type 'help' to see a help text")
    print("type 'quit' to exit this game")
    command = input(">>>")
    if command == "help":
        print("See 'The hitchhikers guide to the galaxy")
        print(" by Douglas Adams")
    elif command == "quit":
        break
    elif command == "42":
        print("Congratulations, you know THE answer")
        print("But what was the question exactly..... ? ")
        break

print("bye-bye")