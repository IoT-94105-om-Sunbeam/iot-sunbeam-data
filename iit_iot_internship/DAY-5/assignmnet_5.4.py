import datetime

now = datetime.datetime.now()

print("Current Date and Time:", now) #to display current date and time

print("Day of the Week:", now.strftime("%A")) #to display day of the week
# strftime("%A") → converts date to day name