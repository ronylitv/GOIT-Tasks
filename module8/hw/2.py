import calendar



def get_days_in_month(month, year):
    days = calendar.monthrange(year, month)
    return days[1]
print(get_days_in_month(3,2021))


