from datetime import datetime, timedelta

# now = datetime.now()
# before = now - timedelta(weeks=2)
#
# today = datetime.today()
#
# print(today)
#
# today + timedelta(days=3)
#
# print(now.year)
# print(now.month)
# print(now.day)

datetime_str = "2023-04-1 12:01:30"

datetime_object = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

# print(datetime_object)
# print(type(datetime_object))

hours72 = datetime_object - timedelta(hours=72)
print(hours72)
print(type(hours72))
hours72_str = hours72.strftime('%Y-%m-%d %H:%M:%S')

print(hours72_str)
print(type(hours72_str))
