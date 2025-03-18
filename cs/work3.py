term_time = input("Are you in the term time? ")
day = input("Insert the day: ")

alarm = "7:30 a.m."

if term_time == False:
    alarm = "9:00 a.m."
if term_time == True and day.lower() == "saturday":
    alarm = "8:00 a.m."

print(alarm)