from datetime import datetime, date, time

# find today
today = date.today()
print(today)

# enter tomorrow as a date
tomorrow = date(2023, 1, 24)
print(tomorrow)


nextWeek = date.fromisoformat('2023-01-03')
print(nextWeek)

# current timestamp
rightNow = datetime.now()
print(rightNow)

# seconds since start of computer clock -- 1969-12-31 18:00:01
print(rightNow.timestamp())

# find a moment by searching seconds since computer clock -- 1969-12-31 18:00:01
myDate = datetime.fromtimestamp(1)
print(myDate)