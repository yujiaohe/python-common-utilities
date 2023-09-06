from datetime import datetime, timedelta

# current datetime
today = datetime.today()
year = today.year
month = today.month
day = today.day
weekday = today.weekday()
time = today.time()
print(f"Today is {today}")
print(f"Year: {year}, Month: {month}, Day: {day}, Weekday: {weekday}, Time: {time}")

# timedelta
delta = timedelta(weeks=1, days=1)
previous_date = today - delta
print(f"Previous date: {previous_date}")

# datetime to string
str_today = today.strftime("%Y-%m-%d %H:%M:%S")  # 2023-09-06 10:21:53
print(f"Type(today): {type(today)}, and today is {today}.")
print(f"Type(str_today): {type(str_today)}, and str_today is {str_today}.")
str_today = today.strftime("%Y-%b %a %I:%M%p")  # 2023-Sep Wed 10:11AM
print(f"Str_today is {str_today}.")

# string to datetime
someday = datetime.strptime("2023-08-08 10:58", "%Y-%m-%d %H:%M")
print(f"Type(someday): {type(someday)}, and someday is {someday}")



