from datetime import datetime, date, tzinfo, time
import pytz
d2 = date.today()
print(d2)

current_date = datetime.now()
lop = current_date.strftime('%d %B %Y')
print(type(lop))
print(lop)
print(datetime.strptime(lop, '%d %B %Y'))

d3 = date(1999, 2, 4)
d4 = time(hour=2, tzinfo=tzinfo.utcoffset(current_date))
print(d4)
print(d3)