# solution functions task 7 variant A
# function that accepts any number of parameters and returns them all
def greeter4(time_of_day="Morning", *args):
    text = ""
    for a in args:
        text += a + ","
    if len(args) > 0:
        text = text[:-1]  # remove last comma
        text += " "
    text += time_of_day
    return text


print("------ calling greeter4 ----")
print(greeter4())
print(greeter4("night"))
print(greeter4("evening", "wonderful", "lovely", "heroic", "romantic"))
print(greeter4("night", "good"))
print(greeter4("day", "sunny", "warm", "emotional"))
