import datetime

dt_utc = datetime.datetime.utcnow() + datetime.timedelta(hours=9)

print(dt_utc.year)
print(dt_utc.month)
print(dt_utc.day)
