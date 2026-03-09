# solution chapter function task 1, variant A
def greeting(time_of_day):
    if 6 <= time_of_day <11:
        return "Good morning"
    elif 11 <= time_of_day < 14:
        return "Good day"
    elif 14 <= time_of_day < 18:
        return "Good afternoon"
    elif 18 <= time_of_day < 22:
        return "Good evening"
    elif (22 <= time_of_day) or (time_of_day <6):
        return "Good night"
# test
for h in range(1,25):
    print(f"hour: {h:>2} greeting: {greeting(h)}")
