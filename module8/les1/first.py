from datetime import datetime, timedelta


# print(datetime.now().month)
# print(datetime.now().day)
# print(datetime.now().minute)
#
# print(current_date.date())
# print(current_date.time())


# d1 = datetime(year=2011, day=20, month=3, second=45, hour=les2)
# d1 = d1.replace(month=5)
# print(d1)

current_date = datetime.now()
slovar = {
    'milk': datetime(year=2022, month=7, day=10),
    'cheese': datetime(year=2019, month=7, day=10),
    'cola': datetime(year=2020, month=6, day=10)
}

for ind, val in slovar.items():
    if val.month >= current_date.month and current_date.year <= val.year:
        print(f'{ind.title()} is fresh')
    else:
        print(f'{ind.title()} isn`t fresh')



seventh_day_2019 = datetime(year=2018, month=10, day=24, hour=20, second=34, microsecond=100)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)                   # 365 days, 0:00:00
print(difference.total_seconds())   # 31536000.0
count = 0

while datetime.now() - current_date <= timedelta(seconds=5):
    count += 1
print(count)
