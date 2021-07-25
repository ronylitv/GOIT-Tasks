import calendar


def get_days_in_month(month, year):
    # days = calendar.monthrange(year, month)[1]
    return calendar.monthrange(year, month)[1]

print(get_days_in_month(3,2021))


