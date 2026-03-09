# solution chapter function task 2, variant B
def improved_greeting(hour_of_day, gender):

    suffix = {"male": "Sir",
              "female":"Madam",
              }

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
            return timetable[key] + ", " + suffix[gender]
# test
for h in range(1,25):
    for g in ("male", "female"):
        print(f"hour: {h:>2} gender: {g:<6} greeting: {improved_greeting(h,g)}")