# solution chapter function task 3, variant B
def complex_greeting(hour_of_day, gender, child):

    # dictionary: key: gender value: (greeting_adult, greeting_child)
    suffix = {"male": ("Sir","young man"),
              "female":("Madam","young lady"),
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
            return timetable[key] + ", " + suffix[gender][child]
            # True has the value of 1, False has the value of 0
            # Therefore, child can be used as index for first/second element
# test
for h in range(1,25):
    for g in ("male", "female"):
        for c in (True, False):
            print(f"hour: {h:>2} gender: {g:<6} child: {str(c):<5} "
                  f"greeting: {complex_greeting(h,g,c)}")