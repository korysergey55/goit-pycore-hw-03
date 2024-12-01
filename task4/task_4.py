import re
from datetime import datetime, timedelta , timezone

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Dosde", "birthday": "1985.12.01"},
    {"name": "Jane Smitfdfh", "birthday": "1990.12.5"},
    {"name": "Jane Smitfdfh", "birthday": "1990.11.30"}
]

# def get_upcoming_birthdays(users):
#     users_birthdays_list =[]
#     date_now = datetime.now().date()
#     for user in users:
#         user_date_formatted =  datetime.strptime(user["birthday"], "%Y.%m.%d").date()
#         print(user_date_formatted.day - date_now.day)
#         if user_date_formatted.month >= date_now.month and user_date_formatted.day - date_now.day <= -7:
#             print(user)
#             users_birthdays_list.insert(-1,user)
#     return users_birthdays_list

def get_upcoming_birthdays(users):
    today = datetime.today()
    # Визначаємо дату через 7 днів
    next_week = today + timedelta(days=7)
    results = []
    for user in users:
        # Перетворюємо день народження у формат datetime
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d')
        # Оновлюємо рік дня народження до поточного року
        birthday_this_year = birthday.replace(year=today.year)
        # Якщо день народження вже був цього року, перевіряємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        # Перевіряємо, чи день народження потрапляє у проміжок наступних 7 днів
        if today <= birthday_this_year <= next_week:
            # Якщо день народження у вихідний (субота або неділя)
            if birthday_this_year.weekday() in (5, 6):  # 5 - субота, 6 - неділя
                # Переносимо дату привітання на наступний понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            # Додаємо інформацію до результату
            results.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })
    return results


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)