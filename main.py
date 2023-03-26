import smtplib
import datetime as dt
import random

# TODO 0. Use datetime to obtain current weekday
now = dt.datetime.now()
weekday = now.weekday()

my_birthday = dt.datetime(year=1998, month=11, day=28, hour=14, minute=23)
print(weekday)

# TODO 1. Open quotes.txt file and choose random quote from a list
with open("quotes.txt", mode="r") as file:
    quote_list = file.readlines()

# TODO 2. Use random module to pick a random quote from our list
random_quote = random.choice(quote_list)
print(random_quote)

if weekday == 6:
    #TODO 3. Use smtp to send emails
    my_email = "surendarprakash0@gmail.com"
    my_email2 = "surendarprakash1@yahoo.com"
    my_pass = "hhuqkbhucuivaqak"
    my_pass2 = "dr.dre123dre"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email2,
            msg=f"Subject: \n\n {random_quote}")
