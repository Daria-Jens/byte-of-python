# solution function task 8
def greeter5(time_of_day="morning", **kwargs):
    text = "What a " + time_of_day + "!\n"  # \n makes a new line
    for key, value in kwargs.items():
        text += "The " + key + " is " + value + ".\n"
    return text

print("------- calling greeter5 ---------")
print(greeter5())
print(greeter5(air="wonderful", mood="joyful", future="bright"))
print(greeter5("day", temperature="freezing", wind="strong"))