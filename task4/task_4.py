import re
from datetime import datetime, timedelta , timezone

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Dosde", "birthday": "1985.12.01"},
    {"name": "Jane Smitfdfh", "birthday": "1990.12.5"}
]

def get_upcoming_birthdays(users):
    users_birthdays_list =[]
    date_now = datetime.now().date()
    for user in users:
        user_date_formatted =  datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # print(user_date_formatted.month)
        if user_date_formatted.month >= date_now.month:
            print(user)
    # print(date_now.month)
    # print(date_now-user_date_formatted)



upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)