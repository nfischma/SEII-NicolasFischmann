import datetime
import pytz
tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime. timedelta(days=7)

print(tday-tdelta)

bday = datetime.date(2016,9,24)

till_bday = bday-tday
print(till_bday)

print("")
t = datetime.time(9,30,45,100000)
print(t.hour)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today, dt_now, dt_utcnow)

print()
dt_utcnow = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
