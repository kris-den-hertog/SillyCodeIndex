
from datetime import date
today = date.today()
weekday = today.weekday()
date = today.strftime("%b-%d-%Y")

print(date)

if weekday >= 3:

   print("It is almost weekend! 🤯")
elif weekday >= 4:
   print("You have weekend! 🤯 🥳")
else:
   print("No weekend 🤯 😞")
    