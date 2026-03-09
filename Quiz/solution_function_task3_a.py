# solution chapter function task 3, variant A
def complex_greeting(hour_of_day, gender, child):
    suffix = ""
    if gender == "male":
        suffix = ", Sir"
        if child: #  if child == True:
            suffix = ", young man"
    elif gender == "female":
        suffix = ", Madam"
        if child:
            suffix = ", young lady"
    if 6 <= hour_of_day <11:
        return "Good morning" + suffix
    elif 11 <= hour_of_day < 14:
        return "Good day" + suffix
    elif 14 <= hour_of_day < 18:
        return "Good afternoon" + suffix
    elif 18 <= hour_of_day < 22:
        return "Good evening" + suffix
    elif (22 <= hour_of_day) or (hour_of_day <6):
        return "Good night" + suffix
# test
for h in range(1,25):
    for g in ("male", "female"):
        for c in (True, False):
            print(f"hour: {h:>2} gender: {g:<6} child: {str(c):<5} "
                  f"greeting: {complex_greeting(h,g,c)}")