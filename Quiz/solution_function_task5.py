# solution function task 5
def greeter2(adjective="good"):
    return adjective + " Morning"


# function call (calling greeter2 with different arguments)
print("---- calling greeter2 -----")
print(greeter2("bad"))
print(greeter2("excellent"))
print(greeter2())
print(greeter2(" "))