from datetime import datetime, timedelta , timezone

def get_days_from_today(date):
    current_date = datetime.now()
    user_date = datetime.strptime(date,"%Y-%m-%d")
    result = current_date - user_date
    return result.days

print(get_days_from_today('2020-10-09'))