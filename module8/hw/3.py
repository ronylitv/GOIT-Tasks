# from datetime import datetime
#
# def get_str_date(date: str):
#     # date = date[:-1]
#     datetime_var = datetime.strptime('%Y-%m-%d %X', date)
#     str_date = datetime_var.strftime('%A %d %B %Y')
#     return str_date
#
#
# print(get_str_date('2021-05-27 17:08:34'))
from datetime import datetime


def get_str_date(date: str):
    index = date.find(' ')
    date = date[:index]
    datetime_var = datetime.strptime(date,'%Y-%m-%d')
    str_date = datetime_var.strftime('%A %d %B %Y')
    return str_date

print(get_str_date('2021-05-27 17:08:34'))





