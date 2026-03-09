# solution function task 6
def greeter3(adjective="good", time_of_day="Morning"):
    return adjective + " " + time_of_day

# function call calling greeter3
print("---- calling greeter3 -----")
print(greeter3())
print(greeter3("bad"))
print(greeter3("bad", "evening"))
print(greeter3(time_of_day= "evening"))