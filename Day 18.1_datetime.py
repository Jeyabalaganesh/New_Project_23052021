import datetime
from datetime import datetime
import pytz


x = datetime.now()
print(x)
y = datetime.today()
print(y)
z=datetime.utcnow()
print(z)
# print(datetime.timestamp(x))
# print(datetime.timestamp(y))
# print(datetime.timestamp(z))
# print(x.strftime("%a"))
# print(x.strftime("%A"))
# print(x.strftime("%w"))
# print(x.strftime("%d"))
# print(x.strftime("%a"))
print(x.astimezone())
# print(y.astimezone())

local = datetime.now()
utctime = datetime.utcnow()
#
print("The local time is {}".format(local))
print("The local time is {}".format(utctime))
#
# print(datetime(2021,5,21))
#
#
#
# country = 'Europe/Oslo'
# timezone = pytz.timezone(country)

p = pytz.utc.localize(datetime.utcnow())
print(p)
print(datetime.now().astimezone())
print(datetime.utcnow().astimezone())
print(p.astimezone())

print(pytz.utc.localize(datetime.utcnow()).astimezone())
