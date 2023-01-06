# i kinda skipped the whole sending email part because it requires you to make your email less secure which i dont feel like doing. i understood what she was doing and could replicate it but ehhhh...

import datetime as dt
import smtplib
from random import choice

import pandas

TEXT_TO_REPLACE = "[NAME]"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays_data = pandas.read_csv("./birthdays.csv")
birthdays_list = pandas.DataFrame.to_dict(birthdays_data, orient="records")

for person in birthdays_list:
    birth_month = person["month"]
    birth_day = person["day"]
    today = dt.datetime.now()
    todays_month = today.month
    todays_day = today.day

    if todays_month == birth_month and todays_day == birth_day:
        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        random_letter = choice(letters)
        name = person["name"]
        with open(f"./letter_templates/{random_letter}", mode="r") as letter:
            message = letter.read()
        new_message = message.replace(TEXT_TO_REPLACE, name)
        print(new_message)
        # with open(f"./letter_templates/{name}", mode="w") as file:
        #     file.write(message)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# my_email = ""
# my_password = ""

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email ,password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs="sabetap590@chnlog.com", msg="hello")
# connection.close()
