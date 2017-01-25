from datetime import*

today = datetime.today()
print(today)
print(format(today.strftime('%I:%M %p')))
print(format(today.strftime('%H:%M')))
