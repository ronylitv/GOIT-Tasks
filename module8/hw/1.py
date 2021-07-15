from datetime import datetime


def get_days_from_today(date):
    current_date = datetime.now()
    given_date = datetime.strptime(date, '%Y-%m-%d')
    difference = current_date.date() - given_date.date()
    return difference.days

print(get_days_from_today('2020-10-05'))




