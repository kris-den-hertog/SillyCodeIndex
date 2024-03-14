from pyscript import display
from datetime import date


today = date.today()
weekday = today.weekday()
date = today.strftime("%b-%d-%Y")

display(date)

print("Today's date:", date)
print("today:", weekday)

if weekday > 3:
    print("It is almost weekend! 🤯")
    display("It is almost weekend! 🤯")

elif weekday > 4:
    print("You have weekend! 🤯 🥳")
    display("You have weekend! 🤯 🥳")
   

else:
    print("No weekend 🤯 😞")
    display("No weekend 🤯 😞")