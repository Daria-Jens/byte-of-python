# solution chapter function task 1, variant B
def greeting(hour_of_day):

    #  dictionary: key: hour_of_day value: greeting
    timetable = {6:"Good night",
                 11:"Good morning",
                 14:"Good day",
                 18:"Good afternoon",
                 22:"Good evening",
                 24.1:"Good night", # special case to catch 24
                }
    for key in timetable:
        if hour_of_day < key:
            return timetable[key]

# test
for h in range(1,25):
    print(f"hour: {h:>2} greeting: {greeting(h)}")