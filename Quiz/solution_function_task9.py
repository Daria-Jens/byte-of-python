# solution function task 9
def greeter6(time_of_day="morning", *args, **kwargs):
    text = "What a "
    # iterate over *args
    for a in args:
        text += a + ", "
    if len(args) > 0:
        text = text[:-2] + " "
    text += time_of_day + "!\n"
    # iterate over **kwargs
    for key,value in kwargs.items():
        text += "The " + key + " is " + value + ".\n"
    return text

print("------ calling greeter6 ----")
print(greeter6())
print(greeter6("evening"))
print(greeter6("morning", "sunny", "warm", "emotional"))
print (greeter6("morning", "sunny", "warm", "emotional",
                 air="wonderful", mood="joyful", future="bright"))
print(greeter6(air="smelly"))